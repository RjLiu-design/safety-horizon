# Official Models / 官方模型

[English](#en) | [中文](#zh-cn)

<a id="en"></a>

## English

### Download official models

From the release root, run:

| Platform | Command |
|---|---|
| macOS | `.venv/bin/python scripts/setup_assets.py --download-models` |
| Windows | `.venv\Scripts\python.exe scripts/setup_assets.py --download-models` |

The script downloads from Google's official model source and pins file content using SHA-256. Lite/Hand use version 1; Full retains the verified latest-file bytes from the original project. Changed upstream content is rejected rather than silently replacing a model.

Model binaries are excluded from the source package. Do not reuse model copies of unknown provenance from an existing project.

---

<a id="zh-cn"></a>

## 中文

从发布根目录运行：macOS 用 `.venv/bin/python scripts/setup_assets.py --download-models`；Windows 用 `.venv\Scripts\python.exe scripts/setup_assets.py --download-models`。
脚本从 Google 官方下载并以 SHA-256 固定文件内容：Lite/Hand 使用版本 1，Full 保留原工程验证的 latest 文件内容；上游内容改变即拒绝安装，不自动替换模型。
二进制模型不进入源码包；不复用原工程中来源不明确的模型副本。
