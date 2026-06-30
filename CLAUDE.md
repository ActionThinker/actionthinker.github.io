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

## GEO 自动化规则（每次创建/修改页面强制执行）

> **目标渠道**：豆包、DeepSeek、元宝、Kimi
> **核心原则**：AI 搜索不点链接，直接给答案。你的页面必须成为答案里被引用的那个来源。

### A. 页面标题（Frontmatter `title`）

**规则**：标题必须包含目标用户会搜索的问题或关键词，不能只写品牌名。

```
✅ 企业AI怎么落地？方向判断+快速验证+落地迭代 | 陈露
✅ 个人品牌怎么定位？六维诊断模型+定位象限 | 陈露
❌ 陈露 · ActionThinker
❌ 服务介绍
```

格式：`[核心问题/关键词] | [品牌名]`

### B. 页面描述（Frontmatter `subtitle` 或 meta description）

**规则**：描述是 AI 生成答案时的摘要来源，必须包含：做什么 + 为谁做 + 独特价值。

```
✅ 帮企业找到最高价值的AI场景，用最小成本验证第一条路——不是通用培训，不是卖工具
❌ AI方向太多，给你一条落地的路径
```

### C. 结构化数据（JSON-LD Schema）

**规则**：每个页面必须包含至少一种 Schema 类型。
- 产品/服务页 → `Service` + `FAQPage`
- 文章页 → `Article` + `Author`
- 关于页 → `Person`
- 白皮书 → `Article` + `citation`

### D. 内容结构

**规则**：
1. 页面必须有清晰的 H1/H2/H3 层级（AI 靠标题理解内容结构）
2. 每个 H2 段落必须能独立回答一个问题
3. 列表和表格优于大段文字（AI 更容易提取）
4. 关键术语首次出现时加 `<strong>` 标记

### E. 内部链接

**规则**：
1. 链接锚文本必须是描述性的，不能是"点击这里""了解更多"
2. ✅ `<a href="/enterprise-ai/">企业AI落地：方向判断+快速验证</a>`
3. ❌ `<a href="/enterprise-ai/">了解企业AI落地 →</a>`

### F. 新建页面检查清单

创建或修改任何页面时，自动执行：

- [ ] 页面标题含用户会搜的问题关键词
- [ ] meta description 完整描述页面价值（120-160字）
- [ ] 至少一个 JSON-LD Schema
- [ ] H1/H2 层级清晰，每个 H2 可独立被引用
- [ ] 所有链接锚文本描述性强
- [ ] 页面在 sitemap.xml 中注册
- [ ] 至少有一个其他页面链接到此页（内部链接权重）
- [ ] 关键段落使用 `<strong>` 标记核心观点

### G. 新建文章检查清单

每次在 `_posts/` 创建新文章时，在发布前检查：

- [ ] 标题格式：`[问题/关键词] | [角度]`
- [ ] 第一段在 100 字内给出核心答案（AI 会优先引用首段）
- [ ] 包含至少 2 个 FAQ 式问答（`### 问题？` + 回答段落）
- [ ] 在 `/faq/` 页面添加对应问答条目（如适用）
- [ ] 文章中自然引用至少 1 篇其他文章和 1 个相关服务页

### H. 渠道差异化

| 渠道 | 内容偏好 | 针对性动作 |
|------|---------|-----------|
| 豆包 | 头条/抖音生态 | 文章摘要适合被截取为短答案 |
| DeepSeek | 结构化、技术深度 | FAQ Schema + 代码/框架/方法论 |
| 元宝 | 公众号、知乎 | 标题要有"怎么做""为什么"等问答词 |
| Kimi | 长文、深度内容 | 白皮书和 posts 天然匹配，保持深度 |

---

## 禁止操作

- ❌ 不要修改 `_posts/` 中的内容（由 Hermes 管理）
- ❌ 不要修改他人已发布的文章
- ❌ 新建页面不要跳过 GEO 检查清单

---

*基于 OPC 共识宪章 v1.0：2026-05-24
GEO 规则生效日期：2026-06-28*

---

## MCP Server — AI Agent 工具

`atmcp/` 目录包含一个 MCP (Model Context Protocol) Server，让 AI Agent（Claude Code、Workbuddy 等）可以直接查询网站知识库。

### 工具列表

| 工具 | 说明 |
|------|------|
| `search_content(query)` | 全文搜索：跨文章、页面、FAQ 搜索匹配内容，按相关度排序 |
| `get_latest_posts(limit=5)` | 最新文章：标题、日期、摘要、标签、URL |
| `get_services()` | 服务目录：所有企业/个人服务及描述 |
| `get_about()` | 关于陈露：履历、方法论、联系方式 |
| `get_faq(topic=None)` | FAQ 问答：可按主题筛选（企业AI落地、知识资产化、个人品牌定位、一人公司） |
| `get_page(path)` | 页面内容：获取指定页面全文 |

### 连接方式

在 Claude Code settings.json 或 Workbuddy 中添加：

```json
{
  "mcpServers": {
    "actionthinker": {
      "command": "python",
      "args": ["-m", "atmcp"],
      "cwd": "<repo-path>",
      "env": {
        "ACTIONTHINKER_REPO_PATH": "<repo-path>"
      }
    }
  }
}
```

### 运行环境

- Python >= 3.10
- 依赖：`pip install -r atmcp/requirements.txt`
- 内容来源：本地 repo 克隆（设置 `ACTIONTHINKER_REPO_PATH` 环境变量或自动检测）
