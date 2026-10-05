"""Archive layout and private-data exclusion / 发布目录与私有数据隔离回归。"""
from contextlib import redirect_stdout
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile


APP_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = APP_ROOT.parent


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, APP_ROOT / "scripts" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


packager = load_script("package_release")
verifier = load_script("verify_distribution")


class DistributionLayoutTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="horizon-layout-test-")
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.root = self.base / "source"
        self.output = self.base / "archives"
        guide = '# Guide\n\n<a id="en"></a>\n\nEnglish guide.\n\n<a id="zh-cn"></a>\n\n中文说明。\n'
        files = {
            "README.md": guide,
            "LICENSE": (REPO_ROOT / "LICENSE").read_text(encoding="utf-8"),
            "COMMERCIAL_LICENSE.md": (REPO_ROOT / "COMMERCIAL_LICENSE.md").read_text(encoding="utf-8"),
            "app/VERSION": "0.3.0\n",
            "app/.python-version": "3.12\n",
            "app/README.md": guide,
            "app/horizon.py": "raise SystemExit(0)\n",
            "app/src/safety_monitor/review_store.py": '"""Fixture / 测试替身。"""\n',
            "app/src/config/example.json": '{}\n',
            "app/src/models/README.md": guide,
            "app/src/test_videos/README.md": guide,
            "app/platforms/macos/README.md": guide,
            "app/platforms/windows/README.md": guide,
            "docs/README.md": guide,
            "docs/modules/01_capture/README.md": guide,
            "release/README.md": guide,
            "release/SOURCE_PROVENANCE.json": '{}\n',
            "app/src/runtime/account.py": "PRIVATE\n",
            "app/src/annotations/worker.py": "PRIVATE\n",
            "app/src/config/source.private.json": "PRIVATE\n",
            "app/src/config/thresholds.active.json": "PRIVATE\n",
            "app/src/models/model.task": "PRIVATE\n",
            "app/src/test_videos/site.mp4": "PRIVATE\n",
            "app/.venv/lib/runtime.py": "PRIVATE\n",
            "release/private.md": "PRIVATE\n",
        }
        for name, content in files.items():
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

    def build(self, **kwargs):
        with redirect_stdout(io.StringIO()):
            outputs = packager.build(self.output, source_root=self.root, **kwargs)
        outer = dict((name, digest) for digest, name in
                     (line.split("  ", 1) for line in (self.output / "SHA256SUMS").read_text().splitlines()))
        self.assertEqual(set(outer), {name for name, _ in outputs})
        for name, digest in outputs:
            archive = self.output / name
            self.assertEqual(hashlib.sha256(archive.read_bytes()).hexdigest(), digest)
            self.assertEqual(outer[name], digest)
            with redirect_stdout(io.StringIO()):
                verifier.verify(archive, self.base / ("extracted-" + name))
        return [self.output / name for name, _ in outputs]

    def test_script_roots_distinguish_application_from_repository(self):
        self.assertEqual(packager.APP_ROOT, APP_ROOT)
        self.assertEqual(packager.ROOT, REPO_ROOT)
        self.assertEqual(verifier.APP_ROOT, APP_ROOT)
        self.assertEqual(verifier.ROOT, REPO_ROOT)

    def test_allowlist_excludes_private_and_generated_runtime_files(self):
        for name in ("LICENSE", "app/VERSION", "app/.python-version", "app/src/config/example.json",
                     "docs/modules/01_capture/README.md", "release/SOURCE_PROVENANCE.json"):
            with self.subTest(allowed=name):
                self.assertTrue(packager.allowed(Path(name)))
        for name in ("app/src/runtime/account.py", "app/src/annotations/worker.py",
                     "app/src/config/source.private.json", "app/src/config/thresholds.active.json",
                     "app/src/config/thresholds.proposed.json", "app/src/models/model.task",
                     "app/src/test_videos/site.mp4", "app/src/test_videos/nested/worker.py",
                     "app/.venv/lib/runtime.py", "app/.tools/tool.py", "app/.cache/frame.py",
                     "app/src/artifacts/cache.py", "app/src/events/event.py", "release/private.md",
                     "docs/.private/notes.md", "../LICENSE"):
            with self.subTest(denied=name):
                self.assertFalse(packager.allowed(Path(name)))

    def test_source_archive_preserves_layout_and_excludes_private_data(self):
        archives = self.build()
        self.assertEqual(len(archives), 1)
        with zipfile.ZipFile(archives[0]) as archive:
            names = set(archive.namelist())
            self.assertIn("SafetyHorizon/app/horizon.py", names)
            self.assertIn("SafetyHorizon/docs/modules/01_capture/README.md", names)
            self.assertIn("SafetyHorizon/release/SHA256SUMS", names)
            self.assertNotIn("SafetyHorizon/horizon.py", names)
            self.assertNotIn("SafetyHorizon/SHA256SUMS", names)
            self.assertFalse(any(archive.read(name) == b"PRIVATE\n" for name in names))
            manifest = json.loads(archive.read("SafetyHorizon/release/BUILD_MANIFEST.json"))
            self.assertEqual(manifest["application_root"], "app")
            self.assertIn("app/VERSION", manifest["files"])

    def test_component_intro_is_linked_and_covered_by_checksums(self):
        archives = self.build(components=True)
        self.assertEqual(len(archives), 2)
        component = next(path for path in archives if path.name.endswith("01_capture.zip"))
        with zipfile.ZipFile(component) as archive:
            intro = archive.read("SafetyHorizon/00_SELECTED_MODULE.md").decode()
            self.assertIn("docs/modules/01_capture/README.md#en", intro)
            self.assertIn("00_SELECTED_MODULE.md", archive.read("SafetyHorizon/release/SHA256SUMS").decode())

    def test_platform_and_component_modes_keep_their_own_entry_guides(self):
        archives = self.build(platforms=True, components=True)
        self.assertEqual(len(archives), 3)
        for path in archives:
            with zipfile.ZipFile(path) as archive:
                if path.name.endswith("01_capture.zip"):
                    self.assertIn("SafetyHorizon/00_SELECTED_MODULE.md", archive.namelist())
                    self.assertNotIn("SafetyHorizon/00_START_HERE.md", archive.namelist())
                else:
                    platform = "windows" if "Windows" in path.name else "macos"
                    intro = archive.read("SafetyHorizon/00_START_HERE.md").decode()
                    self.assertIn(f"app/platforms/{platform}/README.md#en", intro)
                    self.assertIn("00_START_HERE.md", archive.read("SafetyHorizon/release/SHA256SUMS").decode())


if __name__ == "__main__":
    unittest.main()
