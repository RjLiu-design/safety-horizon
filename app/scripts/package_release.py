"""Allowlisted source packaging / 白名单打包，不打包现场数据或环境。"""
from pathlib import Path
import argparse
import ast
import hashlib
import json
import zipfile

APP_ROOT = Path(__file__).resolve().parents[1]
ROOT = APP_ROOT.parent
GENERATED = {"release/FILE_INDEX.md", "release/SHA256SUMS", "release/BUILD_MANIFEST.json"}
TOP_FILES = {"README.md", "LICENSE", "COMMERCIAL_LICENSE.md", ".gitignore"}
RELEASE_FILES = {"README.md", "RELEASE_NOTES.md", "THIRD_PARTY_NOTICES.md", "SOURCE_PROVENANCE.json"}
APP_FILES = {"README.md", "VERSION", "requirements.in", "requirements.lock", "requirements-windows.lock",
    ".python-version", "horizon.py", "web_portal.py", "01_install_macos.command",
    "02_run_standalone.command", "03_test.command"}
PRIVATE_PARTS = {"__pycache__", ".git", ".venv", ".tools", ".cache", "runtime", "annotations", "artifacts", "events"}


def allowed(rel):
    rel = Path(rel)
    if rel.is_absolute() or ".." in rel.parts or not rel.parts:
        return False
    s = rel.as_posix()
    if PRIVATE_PARTS.intersection(rel.parts) or rel.name.endswith((".private.json", ".active.json", ".proposed.json")):
        return False
    if s in TOP_FILES or s in GENERATED:
        return True
    if len(rel.parts) == 2 and rel.parts[0] == "release":
        return rel.name in RELEASE_FILES
    if len(rel.parts) == 2 and rel.parts[0] == "app" and rel.name in APP_FILES:
        return True
    if any(part.startswith(".") for part in rel.parts if part != ".github"):
        return False
    if rel.parts[0] == "docs":
        return rel.suffix == ".md"
    if rel.parts[0] == ".github":
        return rel.suffix in {".md", ".yml", ".yaml"}
    if rel.parts[0] != "app" or len(rel.parts) < 3:
        return False
    rel = Path(*rel.parts[1:])
    if rel.parts[0] in {"release_tests", "scripts", "ui", "platforms"}:
        return rel.suffix in {".md", ".py", ".html", ".css", ".js", ".yml", ".sh", ".ps1", ".cmd", ".command"}
    if rel.parts[0] != "src":
        return False
    if len(rel.parts) == 2:
        return rel.suffix in {".py", ".command"}
    folder = rel.parts[1]
    if folder in {"safety_monitor", "tests", "touchdesigner"}:
        return rel.suffix == ".py"
    if folder == "config":
        return rel.suffix == ".json" and not rel.name.endswith((".active.json", ".proposed.json"))
    if folder == "macos_window_capture":
        return rel.suffix in {".c", ".swift"}
    if folder == "hardware":
        return rel.suffix == ".ino"
    if folder in {"models", "test_videos"}:
        return len(rel.parts) == 3 and rel.name == "README.md"
    if folder == "assets":
        return len(rel.parts) == 4 and rel.parts[2] == "sounds" and rel.suffix == ".wav"
    return False


def purpose(path, root=ROOT):
    rel = path.relative_to(root)
    license_purposes = {
        "LICENSE": "v0.3.0+ non-commercial terms and safety disclaimer / v0.3.0 起的非商业条款与安全免责声明",
        "COMMERCIAL_LICENSE.md": "Commercial licensing process and agreement outline / 商业授权流程与协议条款骨架",
    }
    if rel.as_posix() in license_purposes:
        return license_purposes[rel.as_posix()]
    detail = None
    if path.suffix == ".py":
        try:
            doc = ast.get_docstring(ast.parse(path.read_text(encoding="utf-8")))
        except (SyntaxError, UnicodeError):
            doc = None
        if doc:
            detail = doc.splitlines()[0].replace("|", "/")[:160]
    categories = [("app/platforms/macos/", "macOS install/run/test guide / 苹果电脑入口"),
        ("app/platforms/windows/", "Windows install/run/test guide / Windows 电脑入口"),
        (".github/", "Cross-platform CI / 两平台自动化验证"),
        ("app/src/tests/", "Core regression / 核心模块测试"),
        ("app/release_tests/", "Release integration tests / 发布接口测试"),
        ("app/src/config/", "Example / research configuration; recalibrate / 示例配置需现场标定"),
        ("app/src/hardware/", "Arduino firmware / 板卡固件"),
        ("app/src/assets/", "Generated diagnostic sound; not default alert / 生成的旧诊断音效"),
        ("app/src/macos_window_capture/", "Native macOS capture helper source / 原生采集源码"),
        ("app/src/safety_monitor/", "Shared vision/review library / 共享视觉审核库"),
        ("app/ui/", "Standalone local review interface / 独立本地审核界面"),
        ("docs/modules/", "Numbered module guide / 编号模块说明"),
        ("release/", "Release notices and provenance / 发布说明与来源记录"),
        ("docs/", "Numbered deployment documentation / 部署文档")]
    category = next((v for k,v in categories if rel.as_posix().startswith(k)), "Release source or metadata / 发布源码与元数据")
    if detail:
        has_chinese = any('\u4e00' <= c <= '\u9fff' for c in detail)
        has_english = any('a' <= c.lower() <= 'z' for c in detail)
        return detail if has_chinese and has_english else detail + ' — ' + category
    return category


def entry_guide(module, root, platform=False):
    """Link from archive root rather than copying a guide with stale relative links."""
    target = (module / "README.md").relative_to(root).as_posix()
    title = "Start here / 从这里开始" if platform else "Selected workflow module / 所选工作流模块"
    text = f'''# {title}

[English](#en) | [中文](#zh-cn)

<a id="en"></a>

## English

Extract the complete archive, then follow the [selected guide]({target}#en).
All shared application code is in `app/`; enter that directory before running
the guide's terminal commands. Keep `docs/` and `release/` alongside `app/`.
This package includes the shared core; it is not an independently installed module.
Read the [license](LICENSE) before use. File checksums in `release/SHA256SUMS`
are relative to this archive's root directory, not the `release/` directory.

<a id="zh-cn"></a>

## 中文

完整解压后，按[所选说明]({target}#zh-cn)操作。
共享程序位于 `app/`；执行说明中的终端命令前先进入该目录。
保留与 `app/` 同级的 `docs/` 和 `release/`。
本包包含共享核心，并非单独安装的模块。使用前阅读[许可](LICENSE)。
`release/SHA256SUMS` 中的路径相对于解压根目录，而非 `release/` 目录。
'''
    return text.encode("utf-8")


def build(output, components=False, platforms=False, source_root=None):
    root = Path(source_root).resolve() if source_root is not None else ROOT
    app_root = root / "app"
    version = (app_root / "VERSION").read_text(encoding="utf-8").strip()
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    files = sorted(p for p in root.rglob("*") if p.is_file() and not p.is_symlink()
                   and allowed(p.relative_to(root)) and p.relative_to(root).as_posix() not in GENERATED
                   and not any((root / parent).is_symlink() for parent in p.relative_to(root).parents))
    for p in files:
        rel = p.relative_to(root)
        if any(ord(c) > 127 for c in str(rel)):
            raise ValueError(f"Non-ASCII release filename: {rel}")
        if p.suffix in {".py", ".json", ".md", ".command", ".sh"}:
            content = p.read_text(encoding="utf-8")
            if "/Users/" in content and p.name not in {"package_release.py", "test_portal.py"}:
                raise ValueError(f"Personal absolute path in {rel}")
    release_root = root / "release"
    release_root.mkdir(exist_ok=True)
    index = ["# File Index / 逐文件索引", "", "Paths are relative to the repository/archive root. See docs/modules for numbered workflow guides; Python import modules retain their original names.", "", "路径相对于仓库/解压根目录。编号模块导航见 docs/modules；不更名原 Python 导入模块。", "", "| File / 文件 | Purpose / 用途 |", "|---|---|"]
    index += [f"| `{p.relative_to(root).as_posix()}` | {purpose(p, root)} |" for p in files]
    (release_root / "FILE_INDEX.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    manifest = {"version": version, "author": "Safety Horizon--Lrj",
                "license": "LicenseRef-Safety-Horizon-NonCommercial OR LicenseRef-Safety-Horizon-Commercial",
                "license_files": ["LICENSE", "COMMERCIAL_LICENSE.md"],
                "license_scope": "v0.3.0 and later; covered material as defined in LICENSE",
                "commercial_license_requires_signed_agreement": True, "contains_factory_data": False,
                "application_root": "app", "checksum_path_base": "repository/archive root",
                "policy": "explicit allowlist; models/environments/runtime/annotations excluded", "files": [p.relative_to(root).as_posix() for p in files]}
    (release_root / "BUILD_MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    files += [release_root / "FILE_INDEX.md", release_root / "BUILD_MANIFEST.json"]
    checksums = "".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(root).as_posix()}\n" for p in sorted(files))
    (release_root / "SHA256SUMS").write_text(checksums, encoding="utf-8")
    files.append(release_root / "SHA256SUMS")
    names = [(f"SafetyHorizon-v{version}-source.zip", None, False)]
    if platforms:
        names = [(f'SafetyHorizon-v{version}-macOS-arm64.zip', app_root/'platforms/macos', True),
                 (f'SafetyHorizon-v{version}-Windows-x64.zip', app_root/'platforms/windows', True)]
    if components:
        names += [(f"SafetyHorizon-v{version}-{d.name}.zip", d, False)
                  for d in sorted((root / "docs/modules").iterdir()) if d.is_dir() and (d / "README.md").is_file()]
    outputs = []
    for name, module, is_platform in names:
        out = output / name
        with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as z:
            for p in sorted(files):
                if module and p.relative_to(root).as_posix() == 'release/SHA256SUMS':
                    continue
                z.write(p, "SafetyHorizon/" + p.relative_to(root).as_posix())
            if module:
                intro_name = "00_START_HERE.md" if is_platform else "00_SELECTED_MODULE.md"
                intro = entry_guide(module, root, platform=is_platform)
                z.writestr('SafetyHorizon/' + intro_name, intro)
                z.writestr('SafetyHorizon/release/SHA256SUMS', checksums +
                    hashlib.sha256(intro).hexdigest() + '  ' + intro_name + '\n')
        outputs.append((name, hashlib.sha256(out.read_bytes()).hexdigest()))
    (output / "SHA256SUMS").write_text("".join(f"{digest}  {name}\n" for name,digest in outputs), encoding="utf-8")
    print(json.dumps({"release_files": len(files), "archives": [name for name,_ in outputs]}, indent=2))
    return outputs

if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path, default=ROOT / "dist")
    p.add_argument("--components", action="store_true")
    p.add_argument('--platforms', action='store_true')
    a = p.parse_args()
    build(a.output, a.components, a.platforms)
