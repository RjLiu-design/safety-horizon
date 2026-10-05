# Safety Horizon · 安全视界

[English](#en) | [中文](#zh-cn)

<a id="en"></a>

## English

**Visual risk monitoring for cutting-table workstations.**

Designed by **Safety Horizon--Lrj**, Safety Horizon connects video evidence, pose analysis and human review in one traceable workflow. It runs in a local browser on macOS or Windows; TouchDesigner is optional.

**v0.3.0 · Pre-release · Non-commercial + commercial licensing**

### What it does

- **Observe:** capture an authorized video source and analyze workstation posture.
- **Review:** replay event clips, step through frames and annotate actions.
- **Decide:** let a safety officer assign a risk level from 1 to 5.
- **Trace:** store review records and authorize alerts only after human review.

### Explore the project

| I want to… | Go to |
|---|---|
| Understand the design and scope | [Project statement](docs/10_PROJECT_STATEMENT.md#en) |
| Follow the workflow | [Workflow and module guides](docs/README.md#en) |
| Read or run the code | [Application](app/README.md#en) |
| Install on my computer | [macOS guide](app/platforms/macos/README.md#en) · [Windows guide](app/platforms/windows/README.md#en) |
| Check tests and limitations | [Validation](docs/08_VALIDATION.md#en) |
| Find release notes and checksums | [Release files](release/README.md#en) |

The root contains the project overview and licenses. Program files are in `app/`, guides in `docs/`, and package records in `release/`. No workflow modules have been removed.

### Download and run

Download the complete [macOS or Windows package](https://github.com/RjLiu-design/safety-horizon/releases/tag/v0.3.0), extract it and read `00_START_HERE.md`. The first installation downloads Python 3.12, locked dependencies and models.

**macOS · Apple Silicon**

From the extracted root:

```bash
cd app
bash platforms/macos/01_install.command
bash platforms/macos/02_run.command
```

Window capture additionally needs Apple Command Line Tools, `bash scripts/build_capture.sh` and screen-recording permission. Follow the [macOS guide](app/platforms/macos/README.md#en) before using that input.

**Windows 10/11 · x64**

From the extracted root in PowerShell:

```powershell
cd app
powershell -NoProfile -ExecutionPolicy RemoteSigned -File platforms\windows\01_install.ps1
.\platforms\windows\02_run.cmd
```

Choose a live window, authorized RTSP stream, local test video or review-only mode. Stop with **Ctrl+C in the launch terminal**. Closing the browser alone does not stop the service. See the [runbook](docs/02_RUNBOOK.md#en).

Already have Python 3.12? Follow the manual environment setup in your platform guide. Dependencies live in `app/.venv`; system Python is not replaced. Intel Macs, Windows ARM and Linux are outside this release's verified scope.

### Safety and support

Alerts are off by default. Live events need human review at level 3–5 before authorizing a buzzer sequence. Tests, unreviewed events and levels 1–2 remain silent. Recalibrate after camera or source changes.

This is an auxiliary monitoring tool: **it does not replace machine interlocks or physical safety protection**. Software checks and the author's field report are described separately in [Validation](docs/08_VALIDATION.md#en).

[Common problems](docs/06_TROUBLESHOOTING.md#en) · [Report an issue](https://github.com/RjLiu-design/safety-horizon/issues) · [Privacy](docs/05_PRIVACY_SECURITY.md#en)

### Author and license

**Safety Horizon--Lrj** · Copyright © 2026

**v0.3.0 and later use dual licensing:**

- **Non-commercial:** copying, modification, distribution and use of covered material are free solely for non-commercial learning, research, teaching demonstrations and personal projects.
- **Commercial:** sales, for-profit projects or services, internal enterprise production or operations, and deployment for commercial customers require a separately signed agreement, including when no separate software fee is charged.

Commercial contact: `__CONTACT_EMAIL__`. See [LICENSE](LICENSE) and [Commercial licensing](COMMERCIAL_LICENSE.md#en). Third-party licenses remain applicable. The non-commercial license is source-available, not OSI-approved open source. Software is provided **as is**, with warranties and liability excluded to the extent permitted by law.

---

<a id="zh-cn"></a>

## 中文

**面向裁床作业的视觉风险辅助监测系统。**

由 **Safety Horizon--Lrj** 设计，将视频证据、姿态分析和人工审核连接成可追溯的工作流。支持 macOS 和 Windows，在本地浏览器运行，TouchDesigner 为可选界面。

**v0.3.0 · 预发布 · 非商业许可 + 商业授权**

### 核心功能

- **观察：**采集授权视频，分析工位姿态。
- **复核：**回放事件片段，逐帧查看并标注行为。
- **判定：**由安全员选择 1–5 级风险等级。
- **追溯：**保存审核记录，经人工审核后授权声音提醒。

### 项目导航

| 你想了解 | 查看这里 |
|---|---|
| 设计思路与项目范围 | [项目说明](docs/10_PROJECT_STATEMENT.md#zh-cn) |
| 各步骤如何衔接 | [工作流与模块文档](docs/README.md#zh-cn) |
| 程序代码与启动入口 | [程序目录](app/README.md#zh-cn) |
| 在自己的电脑上安装 | [macOS 说明](app/platforms/macos/README.md#zh-cn) · [Windows 说明](app/platforms/windows/README.md#zh-cn) |
| 已完成哪些测试 | [验证记录](docs/08_VALIDATION.md#zh-cn) |
| 版本内容与文件校验 | [发布资料](release/README.md#zh-cn) |

根目录只保留项目介绍和许可。程序放在 `app/`，说明放在 `docs/`，发布资料放在 `release/`，全部工作流模块均保留。

### 下载与运行

下载完整的 [macOS 或 Windows 安装包](https://github.com/RjLiu-design/safety-horizon/releases/tag/v0.3.0)，解压后先读 `00_START_HERE.md`。首次安装需要联网下载 Python 3.12、锁定依赖及模型。

**macOS · 苹果 M 系列**

在解压根目录打开终端：

```bash
cd app
bash platforms/macos/01_install.command
bash platforms/macos/02_run.command
```

窗口采集另需 Apple Command Line Tools、`bash scripts/build_capture.sh` 及录屏权限。使用该输入前请按 [macOS 说明](app/platforms/macos/README.md#zh-cn) 完成准备。

**Windows 10/11 · x64**

在解压根目录打开 PowerShell：

```powershell
cd app
powershell -NoProfile -ExecutionPolicy RemoteSigned -File platforms\windows\01_install.ps1
.\platforms\windows\02_run.cmd
```

启动后选择实时窗口、授权 RTSP、本地测试视频或仅审核界面。退出时在启动终端按 **Ctrl+C**；只关闭浏览器不会停止服务。详见[运行说明](docs/02_RUNBOOK.md#zh-cn)。

已有 Python 3.12 可按对应平台文档手动安装。依赖环境保存在 `app/.venv`，不替换系统 Python。Intel Mac、Windows ARM 和 Linux 不在本版验证范围内。

### 安全与支持

默认关闭声音提醒。实时事件须经人工评为 3–5 级，才授权一次蜂鸣器提醒；测试、未审核及 1–2 级保持静音。更换来源或机位后需要重新标定。

本项目是辅助监测工具，**不替代机器联锁与物理安全防护**。软件测试与作者现场报告分别列于[验证记录](docs/08_VALIDATION.md#zh-cn)。

[常见问题](docs/06_TROUBLESHOOTING.md#zh-cn) · [问题反馈](https://github.com/RjLiu-design/safety-horizon/issues) · [隐私说明](docs/05_PRIVACY_SECURITY.md#zh-cn)

### 作者与许可

**Safety Horizon--Lrj** · Copyright © 2026

**v0.3.0 及后续版本采用双许可：**

- **非商业用途：**仅为非商业学习、研究、教学展示及个人项目，可以免费复制、修改、分发和使用受许可材料。
- **商业用途：**销售、营利性项目或服务、企业内部生产运营、为商业客户部署，均须另行签署协议，即使不单独收取软件费用也不例外。

商业联系：`__CONTACT_EMAIL__`。完整条款见 [LICENSE](LICENSE) 和[商业许可说明](COMMERCIAL_LICENSE.md#zh-cn)。第三方许可继续有效。非商业许可属于源码开放，不是 OSI 认可的开源许可。软件按**现状**提供，在法律允许范围内排除保证与责任。
