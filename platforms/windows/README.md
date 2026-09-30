# Windows（电脑） / Windows PCs

[中文](#zh-cn) | [English](#en)

<a id="zh-cn"></a>

适用：Windows 10/11 **x64**，Python 3.12；不要求 TouchDesigner。

1. 解压完整 Windows 包，例如 `C:\SafetyHorizon`，不要只复制本文件夹。
2. 在解压根目录打开 PowerShell，运行 `powershell -NoProfile -ExecutionPolicy RemoteSigned -File platforms\windows\01_install.ps1`。按提示安装项目内 Python、依赖和模型，不替换系统 Python。
3. 双击 `platforms\windows\02_run.cmd`，选择输入：

| 选择 | 使用方法 |
|---|---|
| 1 萤石 PC 窗口 | 打开并播放直播，选对应窗口编号；输入视频区域 `x0,y0,x1,y1`（窗口客户区归一化坐标，范围 0–1）。如画面占左半边：`0,0,0.5,1`。不得把控制区/广告当视频 |
| 2 RTSP | 输入自有摄像头授权 RTSP 地址，输入不回显；无需打开萤石窗口 |
| 3 本地视频 | 先把素材放入 `src\test_videos`，输入相对路径，如 `src/test_videos/sample.mp4`；测试永远静音 |
| 4 审核界面 | 无视频时查看界面，不生成虚假检测 |

4. 浏览器自动打开。退出在启动终端按 `Ctrl+C`；关闭浏览器不等于退出后端。

窗口模式要求视频区域可见、无遮挡且未最小化；被遮挡时不提供新帧，不回退截取整个桌面。双显示器布局、DPI 缩放和各萤石客户端版本仍需目标电脑实测。RTSP 需要设备支持并开启对应服务，不保证所有型号支持。

源中断可能联动停止本次会话；恢复直播并关闭遮挡窗口后，重新运行 `02_run.cmd`。

私有地址保存在 `src/runtime/source.private.json`，勿分享或上传该目录。更换来源/机位后须重新标定 `src/config` 的工位范围。

已有 Python 3.12 可在根目录执行：

```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install --require-hashes -r requirements-windows.lock
.venv\Scripts\python.exe scripts/setup_assets.py --download-models
.venv\Scripts\python.exe horizon.py configure
```

运行检查：`platforms\windows\03_test.cmd`。默认无声音；实际输出要显式启用并经人工审核。Windows 原生节点版 TouchDesigner 启动/保存适配不在本版范围，请使用独立浏览器入口。

若脚本被系统或公司策略阻止，核对发布包校验值并按组织流程授权，不关闭安全软件或全局放开脚本执行策略。

---

<a id="en"></a>

## English

### Windows (PCs)

Target: **Windows 10/11 x64**, Python 3.12. TouchDesigner is not required.

1. Extract the whole Windows package, for example to `C:\SafetyHorizon`; do not copy only this subfolder.
2. Open PowerShell at the extracted root and run `powershell -NoProfile -ExecutionPolicy RemoteSigned -File platforms\windows\01_install.ps1`. Follow the prompts to install project-local Python, dependencies and models without replacing system Python.
3. Double-click `platforms\windows\02_run.cmd` and select an input:

| Choice | Instructions |
|---|---|
| 1 EZVIZ PC window | Play the live stream, select the window number and enter video bounds `x0,y0,x1,y1` normalized to the window client area (0–1). For the left half, use `0,0,0.5,1`. Exclude controls and advertisements |
| 2 RTSP | Enter your authorized camera URL; input is hidden. An open EZVIZ window is not required |
| 3 Local video | Put footage in `src\test_videos` and enter a path such as `src/test_videos/sample.mp4`. Tests always remain silent |
| 4 Review interface | View the interface without video; no detections are fabricated |

4. The browser opens automatically. Press `Ctrl+C` in the launch terminal to stop; closing the browser alone does not stop the backend.

Window capture requires a visible, unobstructed, non-minimized video area. Occlusion yields no fresh frame; the system does not fall back to capturing the entire desktop. Dual monitors, DPI scaling and specific EZVIZ client versions still need target-PC checks. RTSP requires support and authorization on the device; not every model supports it.

Source loss may stop the session. Restore playback, remove obstructions and restart `02_run.cmd`.

Private addresses are stored in `src/runtime/source.private.json`; do not share or upload this directory. Recalibrate workstation regions in `src/config` when changing sources or camera positions.

If Python 3.12 is already installed, run from the project root:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install --require-hashes -r requirements-windows.lock
.venv\Scripts\python.exe scripts/setup_assets.py --download-models
.venv\Scripts\python.exe horizon.py configure
```

Run checks with `platforms\windows\03_test.cmd`. Sound is off by default; actual outputs need explicit enabling and human review. Native Windows TD launch/save integration is outside this release; use the standalone browser entry.

If system or organizational policy blocks a script, verify the package checksums and follow the approved authorization process. Do not disable security software or globally relax execution policies.
