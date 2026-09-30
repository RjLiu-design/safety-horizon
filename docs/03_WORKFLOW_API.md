# 03 Workflow & File Contracts / 工作流与文件契约

[English](#en) | [中文](#zh-cn)

<a id="en"></a>

## English

### Processing stages

```text
01 Capture -> 02 Pose/Risk -> 03 Queue + Clip -> 04 Human Review
                                                  |-> 05 JSON/CSV + feedback proposal
                                                  |-> 06 Authorized buzzer
07 TouchDesigner OR Browser UI observes/controls the same services
```

| Stage | Implementation | Input → Output |
|---|---|---|
| 01 Capture | `ezviz_window_monitor.py`, `window_capture_device.py`, `windows_capture.py`, `live_sources.py`, `input_router.py` | Window / RTSP / test video → cropped frames and source preview |
| 02 Pose/risk | `ezviz_multistation_fatigue_monitor.py`, `fatigue_engine.py`, `multistation_fatigue.py` | Workstation frames → skeleton, risk advice, `artifacts/ezviz-window-captures/live-status.json` |
| 03 Queue/evidence | `safety_officer_review.py`, `pre_event_buffer.py`, `review_controller.py` | Risk + fresh JPEGs → persistent queue and event clips |
| 04 Review | `web_portal.py` / `td_runtime.py`, `review_contract.py` | Human actions → command JSON → acknowledged state JSON |
| 05 Storage/feedback | `review_store.py`, `threshold_optimizer.py` | Review outcome → `annotations/_records`, daily exports and proposals |
| 06 Alerts | `indicator_bridge.py`, `computer_buzzer_simulator.py` | Only `runtime/review-actuator.json` → one alert sequence |
| 07 TD | `build_touchdesigner_project.py`, `td_runtime.py` | The same file contracts → node interface |

Runtime paths in this table are relative to `src`. The existing internal ID `upper_station` is retained; the interface calls it the left workstation. Database IDs are not renamed.

### Command acknowledgement

`runtime/safety-officer-review-command.json` contains a unique `command_id`, `action` and action fields. A review submission includes event_id, review_level, primary_action, hand_zone, material_occluded, frame_annotations and notes. Validate against `review_contract.py`.

The service writes `last_command_id` and `last_result.ok` to `runtime/safety-officer-review-state.json`. Wait for a successful acknowledgement matching the command ID. Do not automatically retry a timeout with a new ID. Unacknowledged commands are cancelled across restart, not replayed.

Only one interface may write commands. Do not operate TD and the standalone interface against the same directory concurrently. The browser API is local-only, uses a temporary capability token and validates Origin on writes; it is not a multi-user remote-review service.

### Persistence

`annotations/_records/*.json` stores authoritative reviews; `_queue` stores queued events, `_state` approval audits and `_tests` simulation records. CSV headers are defined by `review_store.CSV_FIELDS`. A visible Table DAT alone does not prove that data was saved.

### Feedback limits

Feedback currently proposes score thresholds from human-reviewed records; it does not automatically train a new model. Occluded and uncertain samples are classified separately. Insufficient real positive/negative data must not be presented as high accuracy or used for automatic parameter application.

---

<a id="zh-cn"></a>

## 中文

```text
01 Capture → 02 Pose/Risk → 03 Queue + Clip → 04 Human Review
                                                 ├→ 05 JSON/CSV + feedback proposal
                                                 └→ 06 Authorized buzzer
07 TouchDesigner OR Browser UI observes/controls the same services
```

| 阶段 | 真实程序 | 输入 → 输出 |
|---|---|---|
| 01 采集 | `ezviz_window_monitor.py`, `window_capture_device.py`, `windows_capture.py`, `live_sources.py`, `input_router.py` | 窗口 / RTSP / 测试视频 → 裁切帧、source preview |
| 02 姿态风险 | `ezviz_multistation_fatigue_monitor.py`, `fatigue_engine.py`, `multistation_fatigue.py` | 工位帧 → 骨架、风险建议、`artifacts/ezviz-window-captures/live-status.json` |
| 03 队列证据 | `safety_officer_review.py`, `pre_event_buffer.py`, `review_controller.py` | 风险 + 新鲜 JPEG → 持久队列、前后片段 |
| 04 审核 | `web_portal.py` / `td_runtime.py`, `review_contract.py` | 人工按钮 → command JSON → 服务确认 state JSON |
| 05 存储反馈 | `review_store.py`, `threshold_optimizer.py` | 人工结论 → `annotations/_records` + 日期导出 + 参数建议 |
| 06 提醒 | `indicator_bridge.py`, `computer_buzzer_simulator.py` | **仅** `runtime/review-actuator.json` → 单次提醒 |
| 07 TD | `build_touchdesigner_project.py`, `td_runtime.py` | 同样的文件契约 → 节点界面 |

所有 `src/` 下的相对路径以 `src` 为项目根。此处采用既有 `upper_station` 内部 ID，界面显示左侧工位，不更改数据库 ID。

## Command handshake / 命令回执

文件 `runtime/safety-officer-review-command.json`：`command_id`（唯一值）、`action` 及动作字段。提交至少包含 event_id、review_level、primary_action、hand_zone、material_occluded、frame_annotations、notes。参照 `review_contract.py` 校验。

服务输出 `runtime/safety-officer-review-state.json`：`last_command_id` 与 `last_result.ok`。提交方必须等 ID 对应的成功回执；超时不能自动重发新 ID。重启前未确认命令被取消，不重放。

只允许一个界面向命令文件提交，禁止同时开 TD 和独立版操作同一目录。浏览器接口仅本机、带临时 capability token，写操作还验证 Origin；不是多人远程审核服务。

## Persistence / 持久化

`annotations/_records/*.json` 是审核事实记录，`_queue` 为队列，`_state` 存审批审计，`_tests` 为模拟记录。CSV 表头由 `review_store.CSV_FIELDS` 定义，不凭 GUI 上有一个 Table DAT 就宣称落盘完成。

## Feedback limitations / 反馈边界

当前迭代是基于人工记录的评分阈值建议，不是自动训练新模型。遮挡、不确定样本单独分类。没有足够真实正负样本就不生成“准确率很好”或自动应用参数。
