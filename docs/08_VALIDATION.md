# 08 Validation / 双平台验证记录

[English](#en) | [中文](#zh-cn)

<a id="en"></a>

## English

### Verification record

CI record: **2026-10-01 · v0.3.0 · Python 3.12 · Pre-release**, tested commit [`b95271b`](https://github.com/RjLiu-design/safety-horizon/commit/b95271b499c574048f9e41c23624e068cb99aeb5). Both macOS and Windows jobs passed. The table below records that run's software checks; this documentation revision does not change runtime code or establish new field or physical-hardware acceptance.

[Auditable v0.3.0 dual-platform run](https://github.com/RjLiu-design/safety-horizon/actions/runs/36826892463). For later documentation revisions, check the corresponding commit's run in repository Actions; do not treat this record as evidence for an unexecuted run.

| Check | macOS | Windows |
|---|---|---|
| Environment | macOS 14 ARM64 hosted runner | Windows Server 2025 x64 hosted runner |
| Hash-locked install and pip check | Pass | Pass |
| 132 core tests | 132 passed | 131 passed; 1 macOS helper test skipped |
| 16 release/interface/platform tests | 15 passed; 1 Windows Job test skipped | 16 passed |
| Three real model downloads, hashes and blank-image inference | Pass | Pass |
| Synthetic video → real pose model → TEST dashboard | Pass | Pass |
| File-by-file verification of both ZIPs | Pass | Pass |
| Full regression from the current-platform extracted ZIP | Pass; same counts/skips as above | Pass; same counts/skips as above |
| Windows installer and new .venv regression | Not applicable | Pass, with uv already provided by the runner |

Platform coverage includes file-lock exclusion, source validation, crop boundaries, RTSP timeout settings, review-service startup/shutdown and forced cleanup of owned Windows processes. Interface tests cover authorization, persistence acknowledgements, duplicate-submit protection, test silence and video decoding. Business assertions were not weakened to hide platform failures.

A separate CPython 3.12.13 environment on the local Mac also tested an extracted package without reusing the original TD environment. Restricted sandboxes can block HTTP ports; interface tests require permission to bind localhost.

### Scope

- Windows 10/11 x64 is the target platform. Tests on a Windows Server runner do not establish field acceptance for every client version and camera.
- Real model inference was executed, but synthetic footage is not footage of workers or accidents. Test pass rates are not detection accuracy.
- Not independently executed: real Windows EZVIZ client capture, physical RTSP cameras, dual-monitor/DPI combinations, real UNO hot-plug and sound, full factory shifts, or the entire setup on a machine with no tools installed.
- macOS native helpers compiled successfully in the previous local verification. The original formal TD project is unchanged. Windows TD projects are outside this release's supported path.
- Packages contain allowlisted source, documentation and generated diagnostic sounds—not site recordings, review data, accounts, models or old environments.

### Author field report

Safety Horizon--Lrj reports completing acceptance at the original site with physical hardware, with **91%–100% accuracy**. This is attributed to the author, not combined with automated-test results or extended to the Windows port or every deployment. See [target-site acceptance](07_FACTORY_ACCEPTANCE.md#en).

---

<a id="zh-cn"></a>

## 中文

CI 记录：**2026-10-01 · v0.3.0 · Python 3.12 · Pre-release**，已测试提交 [`b95271b`](https://github.com/RjLiu-design/safety-horizon/commit/b95271b499c574048f9e41c23624e068cb99aeb5)。macOS 与 Windows 两个平台任务均通过。

下表记录该次软件检查结果；本次文档修订不修改运行代码，也不构成新的现场或真实硬件验收。

## Automated verification / 已通过的软件检查

[可核对的 v0.3.0 双平台运行记录](https://github.com/RjLiu-design/safety-horizon/actions/runs/36826892463)。后续文档修订请在仓库 Actions 核对对应提交的运行记录，不将本记录当作尚未执行的检查结果。

| 检查 | macOS | Windows |
|---|---|---|
| 环境 | macOS 14 ARM64 云端执行器 | Windows Server 2025 x64 云端执行器 |
| 锁定依赖安装及 pip check | 通过 | 通过 |
| 132 项核心测试 | 132 通过 | 131 通过；跳过 1 项 macOS 原生助手测试 |
| 16 项发布接口/平台测试 | 15 通过；跳过 1 项 Windows Job 测试 | 16 通过 |
| 三个真实模型下载、哈希及空白图推理 | 通过 | 通过 |
| 合成视频 → 实际姿态模型 → TEST 仪表盘 | 通过 | 通过 |
| 两个 ZIP 的逐文件校验 | 通过 | 通过 |
| 本平台 ZIP 解压后全部回归 | 通过，数量及跳过项同上 | 通过，数量及跳过项同上 |
| Windows 安装脚本及新 .venv 回归 | 不适用 | 通过（执行器已提供 uv） |

跨平台测试包括文件锁互斥、来源校验、裁切边界、RTSP 超时参数、审核服务启停、Windows 子进程强制回收；接口测试包含身份校验、落盘回执、重复提交保护、测试静音和视频解码。未通过降低业务断言来消除平台错误。

本机另使用独立 CPython 3.12.13 环境验证 macOS 解压副本；不复用原 TD 虚拟环境。受限沙盒会禁止本地 HTTP 端口，接口测试须在允许 localhost 的环境执行。

## Scope / 不混淆验证范围

- Windows 10/11 x64 是目标使用平台；云端 Windows Server 测试不等于每种 Windows 客户端和摄像头都已现场验收。
- 实际模型推理已运行，但合成视频不是员工或事故样本，测试通过率不是识别准确率。
- 未独立执行：Windows 萤石 PC 客户端实机采集、实际 RTSP 摄像头、双屏/DPI、真实 UNO 热插拔与声音、厂家整班运行，以及完全没有工具的新机全流程。
- macOS 原生采集助手在上一版本机已编译通过；本次不改原正式 TD 工程。Windows TD 节点工程不在本版支持路径。
- 包含白名单源码、文档、生成诊断音效；不包含现场录像、审核记录、账户、模型或旧虚拟环境。

## Author field report / 作者现场报告

Safety Horizon--Lrj 确认已完成其原现场及真实硬件验收，报告准确率 **91%–100%**。该结论归属于作者，不与上述自动化测试混算，也不自动延伸为新 Windows 适配或所有部署场景的性能保证。目标现场核验见 [07_FACTORY_ACCEPTANCE](07_FACTORY_ACCEPTANCE.md)。
