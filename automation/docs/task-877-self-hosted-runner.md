# Task 877：Self-hosted Runner 与 UI 回归直连

> 日期：2026-09-20
> ORS：877
> 状态：runner 已上线，直连模式待 fork 验证

## 目标

在测试服务器上部署 GitHub self-hosted runner，并让 UI Regression 直接访问本机后端、AI 和数据库，不再依赖公网 SSH 转发。

## 已完成

- 在 fork `hxgeng01-star/OpenRobotService` 注册 runner：
  - `ors-test-ecm-3bca`
  - 标签：`self-hosted, linux, x64, ors-test`
- runner 使用用户级 systemd 服务 `actions-runner.service`。
- fork 上新增并成功执行 `Self-hosted Runner Smoke`：
  - runner 可以拉取并运行 job。
  - backend `9400` health 正常。
  - AI `9411` health 正常。
  - MySQL `3306` 端口可达。
- `UI_REGRESSION_DIRECT=1` 直连模式已加入配置和 UI runtime fixture。
- self-hosted 版 UI Regression workflow 已改为：
  - `runs-on: [self-hosted, linux, x64, ors-test]`
  - blobless + sparse checkout
  - 直接使用 `127.0.0.1` 服务地址

## 本地验证

```text
automation/src/ui_regression/tests + automation/src/remote/tests
28 passed
```

## 待完成

1. 在 fork 配置以下 Secrets：
   - `REAL_U1_PASSWORD`
   - `REAL_U2_PASSWORD`
   - `UI_REGRESSION_CLEANUP_PASSWORD`（可选；缺失时只记录清理告警）
2. 运行 self-hosted UI Regression。
3. 确认 UI 场景和 6 条 Smoke 通过。
4. 评估是否恢复 DB 补偿清理。
