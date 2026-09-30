# 02 Pose & Risk / 身体识别与风险程序

[English](#en) | [中文](#zh-cn)

<a id="en"></a>

## English

### Inputs, outputs and next step

**Input:** single-workstation video from 01. **Output:** skeletons, posture features, advisory risk and uncertainty states. **Next:** 03 Review.

Source: `src/ezviz_multistation_fatigue_monitor.py`, `src/safety_monitor/fatigue_engine.py`, `src/safety_monitor/multistation_fatigue.py` and the adjacent pose/geometry modules.

For development, enter `src` and run `../.venv/bin/python ezviz_multistation_fatigue_monitor.py --help` on macOS. The full workflow uses the root `horizon.py run` entry with the appropriate source configuration; the platform's `02_run` menu is preferred. Do not mistake default multi-workstation settings for the current single-workstation configuration.

Outputs are advisory risk—not a medical fatigue diagnosis or proof of injury. Missing skeletons, unreliable viewpoints and occlusion must not be classified as safe.

### Platform commands

macOS uses `.venv/bin/python` at the root. Windows PowerShell uses `.venv\Scripts\python.exe`, or `..\.venv\Scripts\python.exe` after entering `src`. Other arguments are unchanged. Prefer the platform launcher for the complete workflow.

---

<a id="zh-cn"></a>

## 中文

**输入**：01 的单工位视频。**输出**：骨架、姿态特征、风险建议和不确定状态。下一步：03 Review。

源码：`src/ezviz_multistation_fatigue_monitor.py`、`src/safety_monitor/fatigue_engine.py`、`src/safety_monitor/multistation_fatigue.py` 及同目录的姿态、几何模块。

开发参数：`cd src` 后 `../.venv/bin/python ezviz_multistation_fatigue_monitor.py --help`。完整启动使用根目录 `horizon.py run`，不要将默认多工位配置误当成当前单工位配置。

此模块产生的是辅助风险，不是疲劳医学诊断或已发生伤害。缺失骨架、不可靠机位、遮挡不能判定安全。

## Platform commands / 平台命令

以下 `.venv/bin/python` 是 macOS 写法。Windows 在项目根目录用 `.venv\Scripts\python.exe`，进入 `src` 后用 `..\.venv\Scripts\python.exe`；命令其余参数相同（使用 PowerShell）。完整工作流优先使用对应平台的 `02_run` 菜单，不单独运行模块。
