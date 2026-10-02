# Safety Horizon v0.3.0

[English](#en) | [中文](#zh-cn)

<a id="en"></a>

## English

**Safety Horizon--Lrj · Pre-release**

### Downloads

| Platform | Package |
|---|---|
| macOS · Apple Silicon (M-series) | `SafetyHorizon-v0.3.0-macOS-arm64.zip` |
| Windows 10/11 · x64 | `SafetyHorizon-v0.3.0-Windows-x64.zip` |

Extract the complete package and read `00_START_HERE.md`. These packages include source and installation scripts; the first installation downloads Python 3.12, dependencies and models. TouchDesigner is optional. Use the attached `SHA256SUMS` to verify the downloads.

### Licensing

**v0.3.0 and later use dual licensing.** Under [LICENSE](LICENSE), covered material may be used, copied, modified and distributed free of charge for non-commercial learning, research, teaching demonstrations and personal projects.

Commercial use requires a separately signed agreement. This includes sales, for-profit projects or services, internal enterprise production or operations, and deployment for commercial customers. See [Commercial licensing](COMMERCIAL_LICENSE.md#en). Third-party licenses remain applicable.

Commercial contact: `__CONTACT_EMAIL__`. You can also request contact details through [GitHub Issues](https://github.com/RjLiu-design/safety-horizon/issues). Do not post private business information publicly. An inquiry or download does not grant commercial rights.

### Documentation update · 2026-10-02

The repository documents and platform packages now focus on the terms for v0.3.0 and later. File descriptions and checksums are updated. Monitoring, review, annotation storage and buzzer behavior are unchanged.

### Verification and safety

The v0.3.0 runtime passed the macOS and Windows CI checks: [run 36826892463](https://github.com/RjLiu-design/safety-horizon/actions/runs/36826892463). Automated tests are not field safety certification. See [Validation](docs/08_VALIDATION.md#en) for coverage and limitations.

Software is provided **as is**, to the extent permitted by law. Safety Horizon is an auxiliary monitoring tool and **does not replace machine interlocks or physical safety protection**.

### Installation

Stop running instances and keep existing data. Extract into a new folder and install using the platform guide. Do not overwrite review records or reuse an existing `.venv`. Test the configured input before live use. Alerts are off by default.

<a id="zh-cn"></a>

## 中文

**Safety Horizon--Lrj · 预发布**

### 下载

| 系统 | 安装包 |
|---|---|
| macOS · 苹果 M 系列 | `SafetyHorizon-v0.3.0-macOS-arm64.zip` |
| Windows 10/11 · x64 | `SafetyHorizon-v0.3.0-Windows-x64.zip` |

完整解压后，先读 `00_START_HERE.md`。安装包包含源码和安装脚本，首次安装需要联网下载 Python 3.12、依赖及模型，TouchDesigner 为可选项。附件 `SHA256SUMS` 用于核验下载文件。

### 许可

**v0.3.0 及后续版本采用双许可。** 根据 [LICENSE](LICENSE)，受许可材料可免费用于非商业学习、研究、教学展示及个人项目，允许在该范围内使用、复制、修改和分发。

商业使用须另行签署协议，包括销售、营利性项目或服务、企业内部生产运营，以及为商业客户部署。申请流程见[商业许可说明](COMMERCIAL_LICENSE.md#zh-cn)。第三方许可继续有效。

商业联系：`__CONTACT_EMAIL__`。也可通过 [GitHub Issues](https://github.com/RjLiu-design/safety-horizon/issues) 索取联系地址，请勿公开业务隐私。咨询或下载不构成商业授权。

### 文档更新 · 2026-10-02

仓库说明和两平台安装包统一说明 v0.3.0 及后续版本的许可条款，文件说明和校验值同步更新。识别、审核、标注存储及蜂鸣器逻辑不变。

### 验证与安全

v0.3.0 运行代码已通过 macOS 和 Windows CI 检查：[测试记录 36826892463](https://github.com/RjLiu-design/safety-horizon/actions/runs/36826892463)。自动化测试不等于现场安全认证，具体范围与限制见[验证记录](docs/08_VALIDATION.md#zh-cn)。

软件在法律允许范围内按**现状**提供。Safety Horizon 是辅助监测工具，**不替代机器联锁与物理安全防护**。

### 安装

停止运行中的实例并保留数据，解压到新目录，按照对应平台说明安装。不覆盖审核记录，不复用已有 `.venv`。接入实时监测前验证输入配置。默认关闭声音提醒。
