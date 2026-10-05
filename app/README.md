# Application / 程序

[English](#en) | [中文](#zh-cn)

<a id="en"></a>

## English

This folder contains the complete application. Keep its contents together. From the repository or extracted package root, run `cd app` before following runtime commands.

| Folder / file | Purpose |
|---|---|
| [platforms](platforms) | [macOS installation](platforms/macos/README.md#en) and [Windows installation](platforms/windows/README.md#en) |
| [src](src) | Capture, pose analysis, review, storage and hardware modules |
| [ui](ui) | Browser review interface |
| [horizon.py](horizon.py) | Main entry: configure, run, doctor and test |
| [scripts](scripts) | Model setup, capture build, package and verification tools |
| [release_tests](release_tests) | Platform and review-interface regression tests |

Dependency locks, `VERSION` and `.python-version` remain here with the runtime. Installation creates `app/.venv`. Private configuration, clips and annotations stay under `app/src` and are excluded from Git and release archives.

[Project overview](../README.md#en) · [Workflow guides](../docs/README.md#en) · [Release files](../release/README.md#en)

<a id="zh-cn"></a>

## 中文

本目录包含完整程序，请保持目录结构。从仓库或解压根目录执行 `cd app` 后，再运行文档中的程序命令。

| 目录 / 文件 | 用途 |
|---|---|
| [platforms](platforms) | [macOS 安装](platforms/macos/README.md#zh-cn)与 [Windows 安装](platforms/windows/README.md#zh-cn) |
| [src](src) | 采集、姿态分析、审核、存储与硬件模块 |
| [ui](ui) | 浏览器审核界面 |
| [horizon.py](horizon.py) | 主入口：配置、运行、自检与测试 |
| [scripts](scripts) | 模型下载、采集编译、打包与校验工具 |
| [release_tests](release_tests) | 平台和审核接口回归测试 |

依赖锁、`VERSION` 和 `.python-version` 与程序放在一起。安装环境位于 `app/.venv`；私有配置、视频及标注存放在 `app/src` 下，不进入 Git 或发布包。

[项目介绍](../README.md#zh-cn) · [工作流说明](../docs/README.md#zh-cn) · [发布资料](../release/README.md#zh-cn)
