# macOS（苹果电脑） / Apple computers

[中文](#zh-cn) | [English](#en)

<a id="zh-cn"></a>

适用：Apple Silicon Mac，Python 3.12；TouchDesigner 可选。

1. 解压完整 macOS 包，不要只拷贝本文件夹。
2. 终端进入解压根目录，执行 `bash platforms/macos/01_install.command`。按提示安装 Python、依赖和模型。
3. 窗口采集另需 Apple 编译工具：`xcode-select --install`，安装后执行 `bash scripts/build_capture.sh`；允许录屏权限。
4. 执行 `bash platforms/macos/02_run.command`，选 `1` 萤石窗口、`2` RTSP、`3` 本地视频或 `4` 仅审核界面。
5. 浏览器自动打开；退出在启动终端按 `Ctrl+C`。

萤石窗口需登录并播放实时视频。RTSP 使用自有设备授权地址，不需要窗口采集助手。本地视频先放在 `src/test_videos`，只做测试，不能触发真实提醒。

已有 Python：在根目录创建 `.venv`，使用 `requirements.lock` 安装；不要使用 Windows 锁文件。完整命令见根 README。

默认静音；需要实际提醒时，核验设备后显式使用 `--alerts computer` 或 `--alerts uno`，仍须人工审核授权。更换机位、画面尺寸或来源需要重新标定工位配置。

---

<a id="en"></a>

## English

### macOS (Apple computers)

Target: **Apple Silicon Mac**, Python 3.12. TouchDesigner is optional.

1. Extract the entire macOS archive; do not copy only this subfolder.
2. Open Terminal in the extracted project root and run `bash platforms/macos/01_install.command`. Follow the prompts to install Python, dependencies and models.
3. Window capture additionally requires Apple tools: run `xcode-select --install`, then `bash scripts/build_capture.sh`, and grant screen-recording permission.
4. Run `bash platforms/macos/02_run.command`. Choose `1` EZVIZ window, `2` RTSP, `3` local test video or `4` review interface only.
5. The browser opens automatically. Stop by pressing `Ctrl+C` in the launch terminal.

For window input, sign in to EZVIZ and play the live video. RTSP uses an authorized device address and does not need the window helper. Put local files in `src/test_videos`; they are test inputs and cannot activate real alerts.

If Python 3.12 is already installed, create `.venv` at the root and install from `requirements.lock`, not the Windows lock file. See the root README for complete commands.

Alerts are off by default. After checking devices, explicitly enable `--alerts computer` or `--alerts uno`; human-review authorization is still required. Recalibrate the workstation configuration after changing the camera position, frame dimensions or source.
