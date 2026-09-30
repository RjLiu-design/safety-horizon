# 04 Optional TouchDesigner / 可选节点界面

[English](#en) | [中文](#zh-cn)

<a id="en"></a>

## English

### Optional interface

The standalone application does not require TD. The package retains workflow-builder and runtime source without deleting or rewriting existing formal projects. Original `.toe` binaries containing site caches are excluded from public downloads.

These optional build steps target **macOS**. On Windows use `platforms/windows/02_run.cmd`; Windows TD startup and save support is not claimed.

### Build in a NEW project

1. Complete installation from the package root so `.venv`, models and any required live-capture helper are ready.
2. Stop the standalone browser application to avoid concurrent submissions.
3. Create a blank TD project. Do not run the builder inside an existing formal project. It refuses to destroy existing `safety_td` or `safety_window` nodes.
4. Open Textport and replace the path below with your extracted location:

```python
from pathlib import Path
p = Path('/absolute/path/SafetyHorizon/src/touchdesigner/build_touchdesigner_project.py')
exec(compile(p.read_text(encoding='utf-8'), str(p), 'exec'), dict(globals(), __file__=str(p)))
```

5. The output is saved as `src/touchdesigner/SafetyHorizon.toe`. Confirm the title-bar path; do not use a temporary project or numbered backup as the launch entry.
6. Close and reopen it, checking stage nodes, video and the review interface. The vision runtime uses external Python 3.12, not TD's bundled Python.
7. Interact through the component Viewer or its active viewer mode. Selecting a node is not clicking its buttons. Persistence and alert authorization still require target-site checks.

The builder is preserved, but a newly generated, untested TD layout is not claimed to match every manually arranged position in the original. The original complete project remains in its original location and is not rebuilt.

### Alerts

The packaged TD launcher is silent by default. To enable reviewed alerts, an administrator may explicitly add `--alerts computer` or `--alerts uno` to the `horizon.py run` command in the release copy of `src/start_touchdesigner_engine.command`. Do not bypass the review service.

### Relocation

Some generated nodes store build-time paths. After moving the package, recreate the Python environment and generate a new blank TD project at the new location. Do not modify the original project or assume a copied `.toe` is portable by itself.

---

<a id="zh-cn"></a>

## 中文

独立版不需要 TD。本目录保留原工作流构建与运行源码，**不会删除或改写你已有的正式工程**。出于现场缓存隐私，未将原 `.toe` 二进制放入公开包。

以下可选构建步骤面向 **macOS**。Windows 请使用 `platforms/windows/02_run.cmd` 的独立浏览器界面；本版不声称 Windows TD 启动与保存链路已适配。

## Build in a NEW project / 在全新工程生成

1. 完成根目录安装，使 `.venv`、模型和实时采集器准备好。
2. 停止独立浏览器版，避免两套 UI 并行提交。
3. 在 TD 新建一个空白工程，不能打开旧正式工程运行构建脚本。脚本发现已有 `safety_td` / `safety_window` 会拒绝，不销毁它们。
4. 打开 Textport，将下面的路径替换成自己解压的位置：

```python
from pathlib import Path
p = Path('/absolute/path/SafetyHorizon/src/touchdesigner/build_touchdesigner_project.py')
exec(compile(p.read_text(encoding='utf-8'), str(p), 'exec'), dict(globals(), __file__=str(p)))
```

5. 输出保存到 `src/touchdesigner/SafetyHorizon.toe`。确认标题路径后再使用，不使用临时工程或编号备份作为入口。
6. 关闭后重新打开该工程，检查所有阶段节点、视频和安全员界面。TD 使用外部 Python 3.12，不把 TD 自带 Python 当作项目视觉环境。
7. 交互应通过组件 Viewer / 激活可交互 Viewer 使用；仅选中节点不是点击按钮。按钮实际落盘与授权还需现场验收。

发布源码对应现有构建脚本，不声称未经 TD 实测的新生成界面与原本每个手工位置完全一致。原本完整工程仍留在你的原目录；本次不重建它。

## Alerts / 提醒设置

新包 TD 启动脚本默认不启用声音。需要审核后提示时，由管理员在发布副本 `src/start_touchdesigner_engine.command` 的 `horizon.py run` 参数末尾明确增加 `--alerts computer` 或 `--alerts uno`，不要绕开审核服务。

## Relocation / 换位置

TD 构建时部分节点会保存生成位置。移动发布包后在新位置重新建立 Python 环境并在空白 TD 中重新生成，不修改原工程，不假装复制 `.toe` 就能跨机器启动。
