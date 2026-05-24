---
title: "OPC 通信协议 v1.0 链路试跑"
date: 2026-05-25 00:15:00 +0800
author: ActionThinker
tags: [OPC, Agent, 自动化]
excerpt: "这是 Claude × Hermes L0 心跳链路的自动化验证文章。"
---

# OPC 通信协议 v1.0 链路试跑

这篇文章由 Claude 手动写入 `_posts/`，创建 `.pending-push` 信号文件。

当 push-monitor.py（每分钟执行一次）检测到信号后，自动执行：

1. 读取信号 → 验证 frontmatter
2. CRLF 修复
3. `git add` + `git commit`
4. `git push origin master`
5. 删除信号文件
6. 写入 `.push-success.json`

如果这篇文章出现在 actionthinker.com，说明 **L0 心跳链路验证成功**。
