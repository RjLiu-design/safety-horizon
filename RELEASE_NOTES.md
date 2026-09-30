# Safety Horizon v0.2.0-rc.2 — 中英双语 / Bilingual documentation

[中文](#zh-cn) | [English](#en)

<a id="zh-cn"></a>

**两个电脑平台，同一套视觉风险与人工审核工作流。** Safety Horizon--Lrj · MIT · Pre-release。

## 下载

- 苹果 M 系列电脑：`SafetyHorizon-v0.2.0-rc.2-macOS-arm64.zip`
- Windows 10/11 x64：`SafetyHorizon-v0.2.0-rc.2-Windows-x64.zip`
- `SHA256SUMS`：附件校验清单。

每包先读 `00_START_HERE.md`，均含完整共享源码，不要求安装 TouchDesigner。

## rc.2 更新

- 项目 README、两平台说明、七个工作流、部署文档及第三方说明均提供完整中英文正文。
- 文档顶部增加语言跳转；命令、参数、测试范围和安全边界保持两种语言一致。
- 仓库链接更新为 RjLiu-design/safety-horizon。
- 两个下载包同步双语文档，重新生成文件索引和校验清单。
- 视觉、审核、标注存储和审核后提醒逻辑与 rc.1 相同；这是文档更新，不是算法更新或新的准确率声明。

rc.1 的功能全部保留：两平台安装/启动/测试入口及依赖锁，窗口/RTSP/本地视频输入，Windows 区域采集、互斥、进程回收和声音支持，视频证据、回放标注、存储及人工授权提醒。测试模式不能驱动真实输出。

## 验证与限制

[rc.1 基线记录](https://github.com/RjLiu-design/safety-horizon/actions/runs/35723516394)：macOS ARM64 与 Windows x64 各 147 项通过、1 项非本平台测试跳过；另包含真实模型推理、合成视频处理、解压回归及 Windows 安装器新环境验证。本次发布检查见 [Actions](https://github.com/RjLiu-design/safety-horizon/actions)。

软件检查不代替实际萤石客户端、摄像头、板卡和目标现场验收。Windows 视频区域需可见、无遮挡；RTSP 需要设备支持和授权。新机位须重新标定。Windows 使用浏览器界面，不提供已验收的 Windows TD 工程。

作者原现场准确率 91%–100% 不自动代表 Windows 适配结果。系统不替代机器联锁和安全防护。

## 更新方式

停止旧实例，保留旧数据，解压新包到新目录并重新安装。不复用旧 .venv，不覆盖审核记录。先用测试视频核验，再接实时来源。默认静音。

---

<a id="en"></a>

## English

### Safety Horizon v0.2.0-rc.2 — bilingual documentation

**Two desktop platforms, one visual-risk and human-review workflow.** Safety Horizon--Lrj · MIT · Pre-release.

### Downloads

- Apple M-series Macs: `SafetyHorizon-v0.2.0-rc.2-macOS-arm64.zip`
- Windows 10/11 x64: `SafetyHorizon-v0.2.0-rc.2-Windows-x64.zip`
- `SHA256SUMS`: artifact integrity checks.

Read `00_START_HERE.md` first. Each package includes the full shared source and does not require TouchDesigner.

### Changes in rc.2

- Complete Chinese and English text for the project README, platform instructions, seven workflow guides, deployment documents and third-party notices.
- Language links at the top of each guide, with matching commands, parameters, testing scope and safety statements.
- Repository links updated to RjLiu-design/safety-horizon.
- Both downloadable packages include the bilingual documentation and refreshed file/checksum indexes.
- Monitoring, review, annotation storage and reviewed-alert logic are unchanged from rc.1; this is a documentation release, not a new algorithm or accuracy claim.

The rc.1 features remain: platform-specific install/run/test entries and dependency locks; window, RTSP and local-video input; Windows region capture, locking, process cleanup and sound support; evidence replay, annotations, persistence and human-authorized alerts. Test mode cannot drive real outputs.

### Verification and limits

The [rc.1 baseline](https://github.com/RjLiu-design/safety-horizon/actions/runs/35723516394) passed on macOS ARM64 and Windows x64: 147 tests passed and one other-platform test was skipped on each. It also exercised real-model inference, synthetic-video processing, extracted-package regression and the Windows installer's new environment. Current release checks are available in [Actions](https://github.com/RjLiu-design/safety-horizon/actions).

Software checks do not replace acceptance of physical cameras, specific EZVIZ clients, boards or target sites. Windows window capture needs a visible, unobstructed video region. RTSP needs device support and authorization. New camera positions require calibration. Windows uses the browser interface, not a verified Windows TD project.

The author's original 91%–100% field-accuracy report does not automatically apply to the Windows port. The system does not replace machine interlocks or protective measures.

### Updating

Stop the old instance, keep existing data, extract the new package into a new folder and reinstall. Do not reuse an old `.venv` or overwrite review records. Verify with test footage before connecting live input. Alerts remain off by default.
