# 04 Annotation Storage / 标注与存储程序

[中文](#zh-cn) | [English](#en)

<a id="zh-cn"></a>

**输入**：人工审核记录。**输出**：原始 JSON、日期/工位导出 CSV/JSONL、队列和审计。下一步：05 Feedback。

源码：`src/safety_monitor/review_store.py`、`review_contract.py`。这是共享库，不是必须独立常驻的应用；审核服务调用它可避免两份进程重复写入。

测试：`cd src` 后 `../.venv/bin/python -m unittest discover -s tests -p 'test_review_workflow.py' -v`。

发布源码不附现场 annotations。不能将审核记录提交 GitHub。文件结构/字段详见 `docs/03_WORKFLOW_API.md`。

## Platform commands / 平台命令

以下 `.venv/bin/python` 是 macOS 写法。Windows 在项目根目录用 `.venv\Scripts\python.exe`，进入 `src` 后用 `..\.venv\Scripts\python.exe`；命令其余参数相同（使用 PowerShell）。完整工作流优先使用对应平台的 `02_run` 菜单，不单独运行模块。

---

<a id="en"></a>

## English

### Inputs, outputs and next step

**Input:** human-review records. **Output:** original JSON, daily/per-workstation CSV/JSONL exports, queue state and audits. **Next:** 05 Feedback.

Source: `src/safety_monitor/review_store.py` and `review_contract.py`. This is a shared library, not a required independent daemon. The review service calls it to avoid duplicate writer processes.

Test from `src` on macOS:

```bash
../.venv/bin/python -m unittest discover -s tests -p 'test_review_workflow.py' -v
```

On Windows PowerShell, use `..\.venv\Scripts\python.exe` with the same arguments. At the project root the Python paths are `.venv/bin/python` and `.venv\Scripts\python.exe` respectively. Prefer the platform's `02_run` for the complete workflow.

Site annotations are not included in public source. Never commit review records to GitHub. File structures and fields are documented in `docs/03_WORKFLOW_API.md`.
