"""Check bilingual coverage, navigation and local links / 检查双语正文、导航和文档链接。"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def main():
    pages = [ROOT/'README.md', ROOT/'RELEASE_NOTES.md', ROOT/'THIRD_PARTY_NOTICES.md',
             *sorted((ROOT/'docs').glob('*.md')), *sorted((ROOT/'modules').glob('*/README.md')),
             *sorted((ROOT/'platforms').glob('*/README.md')),
             ROOT/'src/models/README.md', ROOT/'src/test_videos/README.md']
    for page in pages:
        text = page.read_text(encoding='utf-8')
        assert text.count('<a id="zh-cn"></a>') == 1, page
        assert text.count('<a id="en"></a>') == 1, page
        assert text.index('<a id="en"></a>') < text.index('<a id="zh-cn"></a>'), page
        en = text.split('<a id="en"></a>', 1)[1].split('<a id="zh-cn"></a>', 1)[0]
        zh = text.split('<a id="zh-cn"></a>', 1)[1]
        assert re.search(r'[\u4e00-\u9fff]', zh), page
        assert len(re.findall(r'[A-Za-z]{2,}', en)) >= 20, page
        assert text.count('```') % 2 == 0, page
        assert 'github.com/lrj2004424-star/' not in text, page
        for href in re.findall(r'\]\(([^)]+)\)', text):
            if href.startswith(('https://', 'http://', 'mailto:')):
                continue
            relative, _, anchor = href.partition('#')
            target = (page.parent/relative) if relative else page
            assert target.exists(), (page, href)
            if anchor in ('en', 'zh-cn'):
                assert f'<a id="{anchor}"></a>' in target.read_text(encoding='utf-8'), (page, href)
    index = (ROOT/'FILE_INDEX.md').read_text(encoding='utf-8')
    for row in index.splitlines():
        if row.startswith('| `'):
            purpose = row.split('|')[2]
            assert re.search(r'[\u4e00-\u9fff]', purpose) and re.search(r'[A-Za-z]', purpose), row
    print(f'PASS: {len(pages)} bilingual guides; navigation, links, code fences and file-index language coverage')


if __name__ == '__main__':
    main()
