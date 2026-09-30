# Third-party Software & Models / 第三方软件与模型

[English](#en) | [中文](#zh-cn)

<a id="en"></a>

## English

### Third-party software and models

Project code is MIT-licensed. Dependencies, models, operating-system SDKs and applications retain their own licenses; MIT does not relicense them. Source packages do not bundle existing virtual environments, commercial software or factory data.

| Component | Use | Official source |
|---|---|---|
| CPython 3.12 | External vision/review runtime | https://www.python.org/ |
| uv | Managed Python and isolated dependencies | https://docs.astral.sh/uv/getting-started/installation/ |
| OpenCV | Image/video processing | https://opencv.org/ |
| MediaPipe | Hand and body landmarks | https://developers.google.com/edge/mediapipe/solutions/setup_python |
| MediaPipe models | Official files pinned by SHA-256 during setup | https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker |
| NumPy | Numerical processing | https://numpy.org/ |
| pySerial | Optional serial communication | https://pyserial.readthedocs.io/ |
| pywin32 | Windows information and process cleanup | https://github.com/mhammond/pywin32 |
| MSS | Selected video-region capture on Windows | https://github.com/BoboTiG/python-mss |
| tzdata | Shared timezone data | https://github.com/python/tzdata |
| TouchDesigner | Optional node interface; separate account/license | https://derivative.ca/download / https://derivative.ca/UserGuide/Licensing |
| EZVIZ | User-authenticated camera client | https://www.ys7.com/ |
| Arduino | Optional firmware tools and boards | https://www.arduino.cc/en/software |

Models are not bundled. Lite/Hand use version 1; Full uses the original project's official latest URL while pinning content with a fixed hash. Upstream changes stop installation rather than silently upgrading. uv-managed Python comes from python-build-standalone and is not compiled by this project. Third-party trademarks do not imply endorsement.

---

<a id="zh-cn"></a>

## 中文

项目自身代码使用 MIT。依赖、模型、操作系统 SDK 和应用仍遵循各自许可证，MIT 不重新授权这些内容。源码包不捆绑原虚拟环境、商业软件或工厂数据。

| Component | 用途 / Use | 官方来源 |
|---|---|---|
| CPython 3.12 | 外部视觉 / 审核运行时 | https://www.python.org/ |
| uv | 托管 Python / 隔离依赖 | https://docs.astral.sh/uv/getting-started/installation/ |
| OpenCV | 图像和视频处理 | https://opencv.org/ |
| MediaPipe | 手部及身体关键点 | https://developers.google.com/edge/mediapipe/solutions/setup_python |
| MediaPipe models | 官方来源，安装时用固定 SHA-256 锁定内容 | https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker |
| NumPy | 数值计算 | https://numpy.org/ |
| pySerial | 可选串口 | https://pyserial.readthedocs.io/ |
| pywin32 | Windows 窗口信息及进程回收 | https://github.com/mhammond/pywin32 |
| MSS | Windows 指定视频区域采集 | https://github.com/BoboTiG/python-mss |
| tzdata | 两平台统一时区数据 | https://github.com/python/tzdata |
| TouchDesigner | 可选节点界面，单独账号/授权 | https://derivative.ca/download / https://derivative.ca/UserGuide/Licensing |
| 萤石 | 用户登录并授权的摄像头客户端 | https://www.ys7.com/ |
| Arduino | 可选固件工具及板卡 | https://www.arduino.cc/en/software |

模型不捆绑源码包。Lite/Hand 使用版本 1；Full 使用原工程对应的官方 latest 地址，但以固定 SHA-256 锁定内容，上游改变即停止，不能静默升级。uv 托管 Python 来自 python-build-standalone，并非本项目编译。第三方商标不表示其背书。
