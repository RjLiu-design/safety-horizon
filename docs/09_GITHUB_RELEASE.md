# 09 GitHub Release Checklist / 发布顺序

[English](#en) | [中文](#zh-cn)

<a id="en"></a>

## English

### Release sequence

1. Check README, the Safety Horizon--Lrj attribution, LICENSE, COMMERCIAL_LICENSE.md, third-party notices and validation limits for accuracy. For v0.3.0+, distinguish non-commercial permission from separately signed commercial authorization; preserve historical MIT rights.
2. Run allowlisted packaging and inspect FILE_INDEX, BUILD_MANIFEST and SHA256SUMS.
3. Commit only release-listed source to the intended repository—not the entire original running project.
4. Public publishing is authorized for [RjLiu-design/safety-horizon](https://github.com/RjLiu-design/safety-horizon). Never upload site data.
5. After macOS and Windows Actions jobs pass, create the version tag specified in VERSION (this licensing update: `v0.3.0`). Mark the release **Pre-release**.
6. Use RELEASE_NOTES.md as the release body. Attach the two complete platform ZIPs (`macOS-arm64.zip` and `Windows-x64.zip`) plus external SHA256SUMS. Run `python scripts/package_release.py --platforms --output dist`, then `python scripts/verify_distribution.py --archives dist`, and verify downloaded artifact hashes.
7. Attribute field/hardware acceptance and 91%–100% accuracy to the author as described in [10_PROJECT_STATEMENT](10_PROJECT_STATEMENT.md#en), not as independent certification, universal performance or unconditional production readiness. Do not display unexecuted CI or performance claims.

Retain prior releases/history by default. Remove old assets only with explicit authorization and after verifying the new release; retain tags and backups. Removing downloads does not revoke previously granted MIT rights. Use a new version for future changes. Migrate only authorized site configuration and data, not the old `.venv`, and do not run old and new instances together.

---

<a id="zh-cn"></a>

## 中文

1. 检查 README、作者 Safety Horizon--Lrj、LICENSE、COMMERCIAL_LICENSE.md、第三方说明和 08_VALIDATION 的限制是否真实。v0.3.0 起须区分非商业许可与另行签署的商业授权，并保留历史 MIT 权利。
2. 执行白名单打包脚本；审阅 FILE_INDEX、BUILD_MANIFEST 和 SHA256SUMS。
3. 在指定 GitHub 仓库初始化/提交，仅提交源码清单内文件。不要上传整个原运行工程。
4. 所有者已确认公开发布。仓库：[RjLiu-design/safety-horizon](https://github.com/RjLiu-design/safety-horizon)。仅上传发布清单中的内容，不上传现场数据。
5. GitHub Actions 的 macOS 与 Windows 测试均通过后按 VERSION 创建版本标签（本次许可更新为 `v0.3.0`），Release 选 **Pre-release**。
6. 正文用根目录 RELEASE_NOTES.md；仅附 `macOS-arm64.zip`、`Windows-x64.zip` 两个完整平台包及外部 `SHA256SUMS`。执行 `python scripts/package_release.py --platforms --output dist`；随后执行 `python scripts/verify_distribution.py --archives dist`，再核对下载回来的文件哈希。
7. 作者现场及硬件验收、91%–100% 准确率按 `docs/10_PROJECT_STATEMENT.md` 明确归属于作者报告；不要改写为第三方认证、全场景保证或无条件直接投产。不展示未实际运行的 CI / 性能徽章。

默认保留旧 Release 和历史。只有获得明确授权且新 Release 已校验后，才移除旧下载附件；保留旧标签与备份。移除下载不撤销已经通过 MIT 授予的权利。后续接口或依赖变更使用新版本。迁移只复制经授权的现场配置与数据，不复制旧 `.venv`，不要同时启动新旧实例。
