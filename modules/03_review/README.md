# 03 Human Review / 安全员审核程序

[中文](#zh-cn) | [English](#en)

<a id="zh-cn"></a>

**输入**：风险状态 + 新鲜视频。**输出**：队列、目标前 3 秒/后 5 秒片段、人工判断与唯一的提醒授权。下一步：04 Storage / 06 Actuation。

服务源码：`src/safety_officer_review.py`、`src/safety_monitor/review_controller.py`、`review_contract.py`、`pre_event_buffer.py`。界面源码：`web_portal.py` + `ui/`，或 TD。

仅启动审核界面：`.venv/bin/python horizon.py run --no-vision`。仅启动服务供自行集成：`cd src` 后 `../.venv/bin/python safety_officer_review.py --project-root .`。没有上游状态时不生成假事件。

审核按钮通过唯一 command_id 与回执对接；不能把表面按钮/连线当作已落盘。真实记录需要持久化服务确认。

## Platform commands / 平台命令

以下 `.venv/bin/python` 是 macOS 写法。Windows 在项目根目录用 `.venv\Scripts\python.exe`，进入 `src` 后用 `..\.venv\Scripts\python.exe`；命令其余参数相同（使用 PowerShell）。完整工作流优先使用对应平台的 `02_run` 菜单，不单独运行模块。

---

<a id="en"></a>

## English

### Inputs, outputs and next step

**Input:** risk state and fresh video. **Output:** queued events, clips targeting 3 seconds before/5 seconds after the event, human decisions and the sole alert authorization. **Next:** 04 Storage / 06 Actuation.

Service source: `src/safety_officer_review.py`, `src/safety_monitor/review_controller.py`, `review_contract.py` and `pre_event_buffer.py`. Interface source: `web_portal.py` with `ui/`, or TD.

Review interface only on macOS: `.venv/bin/python horizon.py run --no-vision`. For a standalone service integration, enter `src` and run `../.venv/bin/python safety_officer_review.py --project-root .`. No upstream state means no fabricated events.

Buttons use unique command IDs and service acknowledgements. A visible button or wire is not evidence of persistence; the storage service must confirm the record.

### Platform commands

On Windows PowerShell, replace `.venv/bin/python` with `.venv\Scripts\python.exe`; from `src`, use `..\.venv\Scripts\python.exe`. Other arguments are unchanged. Use the platform's `02_run` menu for the full workflow.
