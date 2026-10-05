"""Verify both platform ZIPs and run regression from the current-platform extracted copy."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import tempfile
import zipfile

APP_ROOT = Path(__file__).resolve().parents[1]
ROOT = APP_ROOT.parent


def verify(archive, target):
    with zipfile.ZipFile(archive) as bundle:
        names = bundle.namelist()
        assert len(names) == len(set(names)), 'Duplicate archive members'
        for entry in bundle.infolist():
            name = entry.filename
            rel = PurePosixPath(name)
            assert not rel.is_absolute() and '..' not in rel.parts and '\\' not in name
            assert rel.parts[0] == 'SafetyHorizon'
            assert not {'runtime', 'annotations', 'artifacts', 'events', '__pycache__', '.venv', '.git', '.tools', '.cache'} & set(rel.parts)
            assert not stat.S_ISLNK(entry.external_attr >> 16), 'Symlink archive member'
        bundle.extractall(target)
    root = target / 'SafetyHorizon'
    checksums = (root/'release/SHA256SUMS').read_text(encoding='utf-8').splitlines()
    expected = set()
    for line in checksums:
        digest, name = line.split('  ', 1)
        rel = PurePosixPath(name)
        assert not rel.is_absolute() and '..' not in rel.parts and '\\' not in name
        assert re.fullmatch('[0-9a-f]{64}', digest), 'Invalid digest'
        assert name not in expected, 'Duplicate checksum entry'
        expected.add(name)
        assert hashlib.sha256((root/name).read_bytes()).hexdigest() == digest, name
    actual = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
    assert actual == expected | {'release/SHA256SUMS'}, 'Incomplete checksum coverage'
    manifest = json.loads((root/'release/BUILD_MANIFEST.json').read_text(encoding='utf-8'))
    assert manifest['version'] == (root/'app/VERSION').read_text(encoding='utf-8').strip(), 'Version mismatch'
    assert manifest['application_root'] == 'app'
    assert manifest['checksum_path_base'] == 'repository/archive root'
    assert set(manifest['files']).issubset(expected), 'Manifest references missing files'
    assert manifest['license'] == 'LicenseRef-Safety-Horizon-NonCommercial OR LicenseRef-Safety-Horizon-Commercial'
    assert manifest['commercial_license_requires_signed_agreement'] is True
    assert set(manifest['license_files']) == {'LICENSE', 'COMMERCIAL_LICENSE.md'}
    for name in manifest['license_files']:
        assert name in expected and name in manifest['files'], 'Missing licensed release file: ' + name
    license_text = ' '.join((root/'LICENSE').read_text(encoding='utf-8').split())
    assert 'does not replace machine interlocks or physical safety protection' in license_text
    assert '不替代机器联锁与物理安全防护' in license_text
    assert 'Starting with v0.3.0' in license_text
    assert 'This license does not limit rights you hold under another applicable license.' in license_text
    assert '本许可不限制使用者依据其他适用许可已享有的权利' in license_text
    assert (root/'app/horizon.py').is_file() and (root/'app/src/safety_monitor/review_store.py').is_file()
    for intro in ('00_START_HERE.md', '00_SELECTED_MODULE.md'):
        if (root / intro).exists():
            for href in re.findall(r'\]\(([^)]+)\)', (root / intro).read_text(encoding='utf-8')):
                target, _, anchor = href.partition('#')
                page = root / target if target else root / intro
                assert page.is_file(), 'Broken entry-guide link: ' + href
                if anchor in ('en', 'zh-cn'):
                    assert f'<a id="{anchor}"></a>' in page.read_text(encoding='utf-8')
    print(f'{archive.name}: {len(expected)} file hashes PASS', flush=True)
    return root


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archives', type=Path, help='Validate existing published artifacts instead of rebuilding')
    parser.add_argument('--skip-tests', action='store_true')
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix='safety-release-') as tmp:
        tmp = Path(tmp)
        archives = args.archives or tmp/'archives'
        if args.archives is None:
            subprocess.run([sys.executable, str(APP_ROOT/'scripts/package_release.py'), '--platforms', '--output', str(archives)], check=True)
        zips = sorted(archives.glob('*.zip'))
        assert len(zips) == 2, 'Expected exactly macOS and Windows archives'
        outer = {name: digest for digest, name in (line.split('  ',1) for line in (archives/'SHA256SUMS').read_text(encoding='utf-8').splitlines())}
        assert set(outer) == {p.name for p in zips}
        selected = None
        for index, archive in enumerate(zips):
            assert hashlib.sha256(archive.read_bytes()).hexdigest() == outer[archive.name]
            root = verify(archive, tmp/str(index))
            if ('Windows-x64' if os.name == 'nt' else 'macOS-arm64') in archive.name:
                selected = root
        assert selected is not None
        if not args.skip_tests:
            subprocess.run([sys.executable, str(selected/'app/horizon.py'), 'test'], cwd=selected/'app', check=True, timeout=180)
        print('Distribution validation PASS', flush=True)


if __name__ == '__main__':
    main()
