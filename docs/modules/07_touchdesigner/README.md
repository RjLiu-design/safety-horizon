# 07 TouchDesigner / 可视化工作流适配器

[English](#en) | [中文](#zh-cn)

<a id="en"></a>

## English

**Working directory:** from the extracted `SafetyHorizon/` folder, run `cd app` first. Unless a step explicitly enters `src`, commands and source paths below are relative to `app/`, not this documentation folder.

### Workflow adapter

**Input:** the same core state, video, queue and review contracts. **Output:** a node interface, workflow connections and review actions. This is not a separate vision algorithm.

Source: `src/touchdesigner/build_touchdesigner_project.py` and `src/touchdesigner/td_runtime.py`. Follow [04 Optional TouchDesigner](../../04_TOUCHDESIGNER.md#en) for installation and use; the optional TD build path targets macOS.

Release preparation does not delete or rebuild the original formal `.toe`, nodes or workflows. Binaries containing site caches are excluded; users generate a new blank project. Its layout, buttons and restart behavior need real TD acceptance tests and cannot be verified by Python unit tests alone.

---

<a id="zh-cn"></a>

## 中文

**工作目录：**先从解压后的 `SafetyHorizon/` 根目录执行 `cd app`。除步骤明确要求进入 `src` 外，下文命令与源码路径均以 `app/` 为基准，不在本说明所在目录执行。

**输入**：同一套核心状态、视频、队列与审核契约。**输出**：节点界面、流程连接和审核操作。不是独立视觉算法。

源码：`src/touchdesigner/build_touchdesigner_project.py`、`src/touchdesigner/td_runtime.py`。安装和运行严格按[04 可选节点界面](../../04_TOUCHDESIGNER.md#zh-cn)。

原正式 `.toe`、原节点和原工作流没有被这次发布整理删除或重建。发布包不带含现场缓存的旧二进制，由用户在空白工程生成。新工程的位置、按钮可用性和重启行为需 TD 实机验收，不能由 Python 单元测试代替。
