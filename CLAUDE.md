# CLAUDE.md — actionthinker.com

> **主 CLAUDE.md**：`D:\OPC\CLAUDE.md`
> **宪章引用**：`D:\OPC\OPC-共识宪章.md`
>
> 本文件仅包含本项目的本地上下文。完整的 OPC 生态认知和 Agent 协议请读主 CLAUDE.md。

## 项目信息

- **站点**：actionthinker.com v4.0
- **框架**：Jekyll
- **设计系统**：Navy (#1a2a3a) + Gold (#c9a96e)，Cormorant Garamond / DM Sans
- **部署**：GitHub Pages（push 即部署）

## 关键路径

| 路径 | 用途 | 写入者 |
|:---|:---|:---|
| `_posts/` | 博客内容 | Hermes 写入，ClaudeCode git push |
| `_posts/.pending-push` | 推送信号 | Hermes 创建，ClaudeCode 检测后删除 |
| `_config.yml` | Jekyll 配置 | ClaudeCode 维护 |
| `_layouts/` | 页面模板 | ClaudeCode 维护 |
| `_includes/` | 组件片段 | ClaudeCode 维护 |
| `assets/` | CSS/JS/图片 | ClaudeCode 维护 |
| `tools/` | 工具页面 | ClaudeCode 构建 |

## Git 工作流

1. Hermes 写入 `_posts/xxx.md` + 创建 `.pending-push`
2. ClaudeCode 检测 `.pending-push` → 确认格式 → `git add + commit + push`
3. 推送成功后删除 `.pending-push`

## 禁止操作

- ❌ 不要修改 `_posts/` 中的内容（由 Hermes 管理）
- ❌ 不要修改他人已发布的文章

---

*基于 OPC 共识宪章 v1.0：2026-05-24*
