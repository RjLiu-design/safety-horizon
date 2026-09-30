# 01 Capture / 视觉采集程序

[中文](#zh-cn) | [English](#en)

<a id="zh-cn"></a>

**输入**：已授权的萤石实时窗口、RTSP 或测试视频。**输出**：完整帧、左侧工位裁切、预览与图像新鲜度。下一步：02 Pose Risk。

源码：`src/ezviz_window_monitor.py`、`src/safety_monitor/window_capture_device.py`、`src/safety_monitor/input_router.py`、`src/macos_window_capture/`。

完整启动：使用 `platforms/macos/02_run.command` 或 `platforms/windows/02_run.cmd`，选择输入。单模块开发时用对应 `.venv` 的 Python 在 `src` 下运行 `ezviz_window_monitor.py --help`，显式使用 `--manifest config/ezviz-fatigue-single-upper.json`。缺少后续审核服务时，单独采集不会形成审核闭环。

需要 OpenCV/MediaPipe 依赖及官方模型。macOS 窗口输入使用原生采集器及录屏权限；Windows 使用 `windows_capture.py`，只采选定窗口视频区域，要求无遮挡。RTSP 与窗口配置见 `live_sources.py`。摄像头硬件及萤石客户端不捆绑在 Python 包内。

---

<a id="en"></a>

## English

### Inputs, outputs and next step

**Input:** an authorized EZVIZ live window, RTSP stream or test video. **Output:** full frames, the left-workstation crop, previews and freshness information. **Next:** 02 Pose/Risk.

Source: `src/ezviz_window_monitor.py`, `src/safety_monitor/window_capture_device.py`, `src/safety_monitor/input_router.py` and `src/macos_window_capture/`.

For the complete workflow, use `platforms/macos/02_run.command` or `platforms/windows/02_run.cmd` and select an input. For module development, run `ezviz_window_monitor.py --help` from `src` using the platform's project Python and explicitly select `--manifest config/ezviz-fatigue-single-upper.json`. Capture alone does not provide a complete review loop without the downstream service.

OpenCV/MediaPipe and official models are required. macOS uses its native capture helper with recording permission. Windows uses `windows_capture.py` and captures only the selected unobstructed video region. RTSP and window configuration are handled by `live_sources.py`. Camera hardware and the EZVIZ client are not bundled as Python dependencies.
