# 06 Troubleshooting / 故障排查

[English](#en) | [中文](#zh-cn)

<a id="en"></a>

## English

### Troubleshooting checklist

| Symptom | Check in this order |
|---|---|
| Python not found | Use your platform installer or verify Python 3.12; do not alter system Python links |
| Download fails | Check official-source connectivity, certificates and proxy settings; never bypass a failed hash check |
| Missing model | Run `scripts/setup_assets.py --download-models` with the project Python and inspect verification results |
| Missing macOS helper | Install Apple Command Line Tools, then run `bash scripts/build_capture.sh` |
| Black/stale video | Read `src/runtime/vision.log`; verify live playback, permission and window visibility; the browser hides images older than 2 seconds |
| No skeleton | Check camera position, occlusion, person size and original video quality; never draw a fabricated skeleton |
| No queued clip yet | Wait for post-event recording; treat missing pre-event footage after startup according to its actual status |
| Button does nothing | Check the session token, RUNNING review service and explicit acknowledgement |
| Submission not confirmed | Do not repeatedly submit; inspect review-supervisor logs and command acknowledgement |
| Threshold cannot be applied | Insufficient data is not a software failure; a PROPOSED result and explicit approval are required |
| No sound | Default is none; tests and levels 1–2 stay silent; enabled output still requires valid human authorization |
| UNO not detected | Check firmware, one supported board, port permissions and reconnection; never write blindly to arbitrary serial ports |
| Application still runs | Closing the browser does not stop the backend; press Ctrl+C in its launch terminal |
| Port already in use | Stop the old instance or select `--port 8766`; do not kill unrelated processes |

Start diagnosis with `horizon.py doctor` and `horizon.py test` using your platform's project Python. Report version, OS, error text, reproduction steps and sanitized logs—not worker footage or credentials.

---

<a id="zh-cn"></a>

## 中文

| 现象 | 检查顺序 |
|---|---|
| 找不到 Python | 按对应平台安装器安装，或确认 Python 3.12 可用；不要改系统 Python 链接 |
| 下载失败 | 检查官方源网络、证书与代理；校验失败不可继续 |
| 模型缺失 | `scripts/setup_assets.py --download-models`，看哈希校验结果 |
| macOS 采集助手不存在 | 安装 Apple Command Line Tools，再 `bash scripts/build_capture.sh` |
| 黑屏 / 旧画面 | 查看 `src/runtime/vision.log`，确认直播、授权和窗口；浏览器隐藏超过 2 秒的图像 |
| 没有骨架 | 机位、遮挡、目标尺寸和原始视频质量；不画假骨架 |
| 队列暂无片段 | 等待后录结束；刚启动缺前录要按真实状态处理 |
| 按钮无反应 | 当前页面是否带会话 token；审核服务是否 RUNNING；看明确回执 |
| 未确认成功 | 不要连续重复提交；查 review-supervisor 日志和命令回执 |
| 阈值无法应用 | 样本不足不是错误；要有 PROPOSED 和明确人工审批 |
| 没声音 | 默认 none，测试不响，1–2 级不响；开启提醒后仍需有效人工授权 |
| UNO 无法识别 | 正确固件、唯一受支持板卡、端口权限、拔插；不要盲目写任意串口 |
| 程序还在运行 | 关闭浏览器不会关闭后端，在启动终端 Ctrl+C |
| 地址已被占用 | 先关闭旧实例，或 `--port 8766`；不要随意杀陌生进程 |

排查先运行 `horizon.py doctor` 和 `horizon.py test`。报告问题时提供版本、系统、错误文本、步骤和脱敏日志，不上传员工视频或凭据。
