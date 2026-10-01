# Safety Horizon v0.3.0 — Dual licensing / 双许可更新

[English](#en) | [中文](#zh-cn)

<a id="en"></a>

## English

**Safety Horizon--Lrj · Non-commercial + commercial licensing · Pre-release**

### Downloads

- macOS, Apple Silicon (M-series): `SafetyHorizon-v0.3.0-macOS-arm64.zip`
- Windows 10/11 x64: `SafetyHorizon-v0.3.0-Windows-x64.zip`
- `SHA256SUMS`: SHA-256 checksums for both ZIPs.

These are complete **source + guided installation** packages, not self-contained executables. Extract the whole package and read `00_START_HERE.md`. First installation downloads Python 3.12, locked dependencies and models. TouchDesigner is optional.

### What changed

- English-first bilingual non-commercial license and a separate commercial-licensing guide.
- Non-commercial learning, research, teaching demonstrations and personal projects are free under LICENSE; commercial use of covered material requires a separate signed agreement.
- Commercial use includes sales, for-profit projects or services, internal enterprise production/operations and deployment for commercial customers.
- Version, license notices, packaging allowlist, file index and checksums are synchronized; both ZIPs include `LICENSE` and `COMMERCIAL_LICENSE.md`.
- Monitoring, review, annotation storage and buzzer behavior are **unchanged**. This is a licensing/release update, not a new algorithm, accuracy claim or safety certification.

Commercial contact remains the requested placeholder `__CONTACT_EMAIL__`; the author must replace it with a working address. Until then, use [GitHub Issues](https://github.com/RjLiu-design/safety-horizon/issues) to request a contact address without posting private information. Neither an inquiry nor a download grants commercial rights.

### Earlier versions

The v0.2.0-rc.1 and rc.2 Release pages and their attachments have been withdrawn at the author's request. Historical tags and commits remain. Existing MIT rights, including commercial rights in previously MIT-licensed material carried into later versions, are not revoked by withdrawing downloads or changing the license. Third-party licenses remain applicable.

### Verification and safety

The existing macOS/Windows CI checks cover regression tests, dependency consistency, model inference, synthetic video, Windows installation and extracted-package validation. Check the run for this release's commit in [Actions](https://github.com/RjLiu-design/safety-horizon/actions); historical test results are not a substitute for that run.

No runtime behavior or target-site acceptance claim is added by this release. Software is provided **as is**, to the extent allowed by law. This auxiliary monitoring tool **does not replace machine interlocks or physical safety protection**. See [LICENSE](LICENSE), [commercial licensing](COMMERCIAL_LICENSE.md#en) and [validation scope](docs/08_VALIDATION.md#en).

### Updating

Stop the old instance, keep existing data, extract the new package into a new folder and reinstall. Do not overwrite review records or reuse an old `.venv`. Check the license and test footage before live use. Alerts remain off by default.

<a id="zh-cn"></a>

## 中文

**Safety Horizon--Lrj · 非商业许可 + 商业授权 · 预发布**

### 下载

- macOS，苹果 M 系列：`SafetyHorizon-v0.3.0-macOS-arm64.zip`
- Windows 10/11 x64：`SafetyHorizon-v0.3.0-Windows-x64.zip`
- `SHA256SUMS`：两个 ZIP 的 SHA-256 校验值。

这两份是完整的**源码 + 引导安装包**，不是免环境独立可执行程序。完整解压，先读 `00_START_HERE.md`；首次安装联网下载 Python 3.12、锁定依赖与模型。TouchDesigner 为可选项。

### 本次变化

- 英文在前的双语非商业许可，以及独立商业授权申请说明。
- 依据 LICENSE，非商业学习、研究、教学展示与个人项目可免费使用；受许可材料的商业使用须另行签约。
- 商业用途包括销售、营利性项目或服务、企业内部生产运营、为商业客户部署。
- 同步版本号、授权说明、打包白名单、文件索引及校验值；两个 ZIP 均包含 `LICENSE` 与 `COMMERCIAL_LICENSE.md`。
- 识别、审核、标注存储及蜂鸣器逻辑**不变**。本次是许可与发布更新，不是算法升级、新的准确率声明或安全认证。

商业联系按要求保留占位符 `__CONTACT_EMAIL__`，作者需替换为有效邮箱。在此之前，可通过 [GitHub Issues](https://github.com/RjLiu-design/safety-horizon/issues) 索取联系地址，请勿公开私人信息。咨询或下载不授予商业权利。

### 历史版本

按作者要求下架 v0.2.0-rc.1、rc.2 的 Release 页面与附件，保留历史标签和提交。下架下载或修改许可不撤销既有 MIT 权利，包括后续版本沿用的 MIT 材料所具有的商用权利。第三方许可仍然有效。

### 验证与安全

既有 macOS/Windows CI 覆盖回归测试、依赖一致性、模型推理、合成视频、Windows 安装及解压包检查。请在 [Actions](https://github.com/RjLiu-design/safety-horizon/actions) 查看本版提交对应的结果，历史测试不能代替本次检查。

本版不改变运行行为，也不新增目标现场验收声明。软件在法律允许范围内按**现状**提供。本软件是辅助监测工具，**不替代机器联锁与物理安全防护**。详见 [LICENSE](LICENSE)、[商业许可](COMMERCIAL_LICENSE.md#zh-cn)及[验证范围](docs/08_VALIDATION.md#zh-cn)。

### 更新方式

停止旧实例并保留数据，解压新包到新目录后重新安装。不覆盖审核记录，不复用旧 `.venv`。接入实时来源前确认许可并使用测试视频验证。默认静音。
