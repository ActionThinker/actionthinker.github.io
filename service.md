---
layout: page
title: 知识基础设施 · 服务产品
subtitle: 让知识真正成为资产
---

<style>
/* ================================================
   服务产品页 — 三层架构风格
   ================================================ */

:root {
  --ink: #1A1A2E;
  --gold: #E8A838;
  --amber: #C4882F;
  --cream: #FAFAF8;
  --gray-mid: #888;
  --gray-light: #F0EEEA;
  --font-serif: 'Cormorant Garamond', Georgia, serif;
  --font-sans: 'DM Sans', system-ui, sans-serif;
}

/* HERO */
.service-hero {
  text-align: center;
  padding: 90px 24px 80px;
  max-width: 760px;
  margin: 0 auto;
}
.hero-eyebrow {
  font-family: var(--font-sans);
  font-size: 11px;
  letter-spacing: 3px;
  color: var(--amber);
  text-transform: uppercase;
  margin-bottom: 20px;
}
.service-hero h1 {
  font-family: var(--font-serif);
  font-size: clamp(36px, 5vw, 58px);
  font-weight: 600;
  color: var(--ink);
  line-height: 1.15;
  margin-bottom: 20px;
}
.service-hero h1 em {
  font-style: italic;
  color: var(--amber);
}
.hero-sub {
  font-size: 17px;
  color: #666;
  line-height: 1.75;
  margin-bottom: 36px;
}
.hero-sub strong {
  color: var(--ink);
}

/* 差异化标签 */
.hero-tags {
  display: flex;
  gap: 10px;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 0;
}
.hero-tag {
  font-family: var(--font-sans);
  font-size: 12px;
  padding: 6px 14px;
  border-radius: 20px;
  background: rgba(26,26,46,0.05);
  color: var(--ink);
  border: 1px solid rgba(26,26,46,0.1);
}
.hero-tag.highlight {
  background: var(--ink);
  color: var(--gold);
  border-color: var(--ink);
}

/* 场景分割线 */
.scene-bar {
  background: var(--ink);
  color: var(--cream);
  padding: 32px 24px;
  text-align: center;
}
.scene-bar p {
  font-family: var(--font-serif);
  font-size: 20px;
  font-style: italic;
  margin: 0;
  color: rgba(250,250,248,0.85);
}
.scene-bar strong {
  color: var(--gold);
  font-style: normal;
}

/* 三层架构概览 */
.architecture-section {
  padding: 80px 24px;
  max-width: 960px;
  margin: 0 auto;
}
.section-label {
  font-family: var(--font-sans);
  font-size: 11px;
  letter-spacing: 2px;
  color: var(--amber);
  text-transform: uppercase;
  text-align: center;
  margin-bottom: 10px;
}
.section-title {
  font-family: var(--font-serif);
  font-size: clamp(24px, 3.5vw, 34px);
  font-weight: 600;
  color: var(--ink);
  text-align: center;
  margin-bottom: 48px;
}
.arch-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}
.arch-card {
  padding: 32px 24px;
  border-radius: 16px;
  background: #fff;
  border: 1px solid rgba(26,26,46,0.07);
  text-align: center;
  transition: all 0.3s;
}
.arch-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 36px rgba(26,26,46,0.08);
  border-color: transparent;
}
.arch-num {
  font-family: var(--font-sans);
  font-size: 10px;
  letter-spacing: 2px;
  color: var(--amber);
  text-transform: uppercase;
  margin-bottom: 10px;
}
.arch-icon {
  font-size: 36px;
  margin-bottom: 14px;
}
.arch-card h3 {
  font-family: var(--font-serif);
  font-size: 20px;
  font-weight: 600;
  color: var(--ink);
  margin-bottom: 6px;
}
.arch-card .arch-en {
  font-family: var(--font-sans);
  font-size: 11px;
  color: var(--amber);
  margin-bottom: 14px;
  letter-spacing: 1px;
}
.arch-card p {
  font-size: 13px;
  color: #888;
  line-height: 1.65;
  margin: 0 0 18px;
}
.arch-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  justify-content: center;
}
.arch-tag {
  font-size: 11px;
  padding: 3px 10px;
  border-radius: 12px;
  background: rgba(26,26,46,0.05);
  color: var(--ink);
}

/* 痛点 */
.pain-section {
  padding: 60px 24px;
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}
.pain-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin-top: 40px;
}
.pain-card {
  padding: 28px 20px;
  border-radius: 14px;
  background: #fff;
  border: 1px solid rgba(26,26,46,0.06);
  text-align: center;
}
.pain-card h4 {
  font-family: var(--font-serif);
  font-size: 18px;
  font-weight: 600;
  color: var(--ink);
  margin-bottom: 8px;
}
.pain-card p {
  font-size: 13px;
  color: #888;
  line-height: 1.6;
  margin: 0;
}

/* 定价 */
.pricing-section {
  padding: 80px 24px;
  max-width: 1040px;
  margin: 0 auto;
}
.pricing-header {
  margin-bottom: 16px;
}
.pricing-tabs {
  display: flex;
  gap: 8px;
  justify-content: center;
  margin-bottom: 48px;
}
.pricing-tab {
  font-family: var(--font-sans);
  font-size: 13px;
  padding: 8px 20px;
  border-radius: 20px;
  border: 1.5px solid #D4D0CA;
  color: #888;
  cursor: pointer;
  background: none;
  transition: all 0.25s;
}
.pricing-tab.active {
  background: var(--ink);
  border-color: var(--ink);
  color: var(--gold);
}
.pricing-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-top: 0;
}
.pricing-card {
  padding: 36px 28px;
  border-radius: 18px;
  background: #fff;
  border: 1px solid rgba(26,26,46,0.06);
  transition: all 0.35s;
  position: relative;
}
.pricing-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 16px 44px rgba(26,26,46,0.08);
  border-color: transparent;
}
.pricing-card.featured {
  background: var(--ink);
  color: var(--cream);
  border-color: transparent;
  transform: scale(1.02);
}
.pricing-card.featured:hover {
  transform: scale(1.02) translateY(-5px);
}
.pricing-level {
  font-family: var(--font-sans);
  font-size: 10px;
  letter-spacing: 2px;
  color: var(--amber);
  text-transform: uppercase;
  margin-bottom: 8px;
}
.pricing-card.featured .pricing-level {
  color: var(--gold);
}
.pricing-card h3 {
  font-family: var(--font-serif);
  font-size: 21px;
  font-weight: 600;
  margin-bottom: 6px;
  color: var(--ink);
}
.pricing-card.featured h3 {
  color: var(--cream);
}
.pricing-price {
  font-family: var(--font-sans);
  font-size: 30px;
  font-weight: 700;
  color: var(--amber);
  margin-bottom: 4px;
}
.pricing-card.featured .pricing-price {
  color: var(--gold);
}
.pricing-price span {
  font-size: 13px;
  font-weight: 400;
  color: #999;
}
.pricing-card.featured .pricing-price span {
  color: rgba(250,250,248,0.5);
}
.pricing-tag {
  display: inline-block;
  font-size: 10px;
  padding: 2px 8px;
  border-radius: 10px;
  background: rgba(232,168,56,0.15);
  color: var(--amber);
  margin-top: 6px;
  margin-bottom: 12px;
}
.pricing-card.featured .pricing-tag {
  background: rgba(232,168,56,0.2);
  color: var(--gold);
}
.pricing-desc {
  font-size: 13px;
  color: #888;
  margin-bottom: 20px;
  line-height: 1.6;
}
.pricing-card.featured .pricing-desc {
  color: rgba(250,250,248,0.65);
}
.pricing-features {
  list-style: none;
  padding: 0;
  margin: 0;
}
.pricing-features li {
  font-size: 13px;
  padding: 6px 0;
  border-bottom: 1px solid var(--gray-light);
  display: flex;
  align-items: center;
  gap: 8px;
}
.pricing-card.featured .pricing-features li {
  border-color: rgba(250,250,248,0.1);
  color: rgba(250,250,248,0.8);
}
.pricing-features li:last-child {
  border-bottom: none;
}
.pricing-features .check {
  color: var(--amber);
  flex-shrink: 0;
}
.pricing-card.featured .pricing-features .check {
  color: var(--gold);
}

/* Agent 产品线 */
.agent-section {
  padding: 60px 24px;
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}
.agent-badge {
  display: inline-block;
  font-family: var(--font-sans);
  font-size: 10px;
  letter-spacing: 2px;
  color: var(--gold);
  background: var(--ink);
  padding: 4px 12px;
  border-radius: 12px;
  margin-bottom: 16px;
}
.agent-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin-top: 36px;
  text-align: left;
}
.agent-card {
  padding: 32px 28px;
  border-radius: 18px;
  background: var(--ink);
  color: var(--cream);
  border: 1px solid rgba(250,250,248,0.06);
  transition: all 0.3s;
}
.agent-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 40px rgba(26,26,46,0.25);
}
.agent-card h3 {
  font-family: var(--font-serif);
  font-size: 20px;
  font-weight: 600;
  color: var(--cream);
  margin-bottom: 4px;
}
.agent-card .price {
  font-family: var(--font-sans);
  font-size: 26px;
  font-weight: 700;
  color: var(--gold);
  margin-bottom: 12px;
}
.agent-card .price span {
  font-size: 13px;
  font-weight: 400;
  color: rgba(250,250,248,0.5);
}
.agent-card p {
  font-size: 13px;
  color: rgba(250,250,248,0.7);
  line-height: 1.6;
  margin: 0 0 18px;
}
.agent-features {
  list-style: none;
  padding: 0;
  margin: 0;
}
.agent-features li {
  font-size: 12px;
  padding: 5px 0;
  border-bottom: 1px solid rgba(250,250,248,0.1);
  display: flex;
  align-items: center;
  gap: 8px;
  color: rgba(250,250,248,0.8);
}
.agent-features li:last-child {
  border-bottom: none;
}
.agent-features .check {
  color: var(--gold);
}

/* 工作流程 */
.flow-section {
  padding: 80px 24px;
  max-width: 700px;
  margin: 0 auto;
}
.flow-steps {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-top: 48px;
}
.flow-step {
  display: flex;
  gap: 20px;
  padding: 24px;
  border-radius: 14px;
  background: #fff;
  border: 1px solid rgba(26,26,46,0.06);
  align-items: flex-start;
}
.flow-num {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: var(--ink);
  color: var(--gold);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-serif);
  font-size: 18px;
  font-weight: 700;
  flex-shrink: 0;
}
.flow-content h4 {
  font-family: var(--font-serif);
  font-size: 18px;
  font-weight: 600;
  color: var(--ink);
  margin-bottom: 6px;
}
.flow-content p {
  font-size: 13px;
  color: #666;
  line-height: 1.6;
  margin: 0;
}

/* CTA */
.service-cta {
  text-align: center;
  padding: 80px 24px;
  max-width: 620px;
  margin: 0 auto;
  background: var(--cream);
  border-radius: 24px;
}
.service-cta h2 {
  font-family: var(--font-serif);
  font-size: clamp(26px, 4vw, 38px);
  font-weight: 600;
  color: var(--ink);
  margin-bottom: 14px;
}
.service-cta p {
  font-size: 14px;
  color: #888;
  margin-bottom: 32px;
  line-height: 1.7;
}
.cta-buttons {
  display: flex;
  gap: 12px;
  justify-content: center;
  flex-wrap: wrap;
}
.btn-primary {
  display: inline-block;
  padding: 14px 32px;
  background: var(--ink);
  color: var(--gold);
  text-decoration: none;
  border-radius: 10px;
  font-family: var(--font-sans);
  font-size: 15px;
  font-weight: 600;
  transition: all 0.3s;
}
.btn-primary:hover {
  background: var(--amber);
  color: #fff;
}
.btn-secondary {
  display: inline-block;
  padding: 14px 32px;
  border: 1.5px solid #D4D0CA;
  color: #666;
  text-decoration: none;
  border-radius: 10px;
  font-family: var(--font-sans);
  font-size: 15px;
  font-weight: 500;
  transition: all 0.3s;
}
.btn-secondary:hover {
  border-color: var(--amber);
  color: var(--amber);
}

/* AGENTS.md 说明块 */
.agentsmd-block {
  padding: 60px 24px;
  max-width: 720px;
  margin: 0 auto;
  text-align: center;
}
.agentsmd-inner {
  padding: 40px;
  border-radius: 18px;
  background: rgba(26,26,46,0.04);
  border: 1px solid rgba(26,26,46,0.08);
  text-align: left;
}
.agentsmd-inner h3 {
  font-family: var(--font-serif);
  font-size: 20px;
  color: var(--ink);
  margin-bottom: 12px;
}
.agentsmd-inner p {
  font-size: 13px;
  color: #666;
  line-height: 1.7;
  margin: 0 0 16px;
}
.code-preview {
  background: var(--ink);
  color: var(--cream);
  font-family: 'Courier New', monospace;
  font-size: 12px;
  padding: 20px;
  border-radius: 10px;
  overflow-x: auto;
  line-height: 1.7;
}
.code-preview .comment { color: rgba(250,250,248,0.4); }
.code-preview .key { color: var(--gold); }
.code-preview .val { color: #98C379; }

/* 响应式 */
@media (max-width: 768px) {
  .arch-grid, .pain-grid, .pricing-grid { grid-template-columns: 1fr; }
  .agent-grid { grid-template-columns: 1fr; }
  .pricing-card.featured { transform: none; }
  .pricing-card.featured:hover { transform: translateY(-5px); }
  .flow-step { flex-direction: column; text-align: center; }
  .flow-num { margin: 0 auto; }
  .service-hero { padding: 60px 20px 50px; }
  .cta-buttons { flex-direction: column; align-items: center; }
}
</style>

<!-- HERO -->
<div class="service-hero">
  <div class="hero-eyebrow">知识基础设施 · 服务产品</div>
  <h1>让 AI 成为你的<em>外脑</em></h1>
  <p class="hero-sub">
    不只是笔记整理——帮你搭建一套<strong>AI可直接调用的知识资产系统</strong>。<br>
    你只管积累，AI编译成结构化网络，Agent越用越懂你。
  </p>
  <div class="hero-tags">
    <span class="hero-tag">Obsidian 本地部署</span>
    <span class="hero-tag">AI 增量编译</span>
    <span class="hero-tag highlight">★ Agent 直连调用</span>
    <span class="hero-tag">MCP Server</span>
    <span class="hero-tag">MEMORY.md 协议</span>
  </div>
<!-- Karpathy 热点背书 -->
<div style="padding:60px 24px;max-width:800px;margin:0 auto;text-align:center;">
  <div style="padding:32px;border-radius:16px;background:rgba(232,168,56,0.08);border:1px solid rgba(232,168,56,0.15);">
    <div style="font-family:var(--font-sans);font-size:11px;letter-spacing:2px;color:var(--amber);text-transform:uppercase;margin-bottom:12px;">热点速览</div>
    <p style="font-family:var(--font-serif);font-size:18px;font-style:italic;color:var(--ink);line-height:1.7;margin:0 0 16px;">
      "为非开发人员搭建此类系统的产品化方案，蕴含着巨大机遇。"
    </p>
    <p style="font-size:13px;color:#888;margin:0;">
      — Andrej Karpathy，2026年4月
    </p>
    <p style="font-size:13px;color:#666;margin:16px 0 0;line-height:1.6;">
      Karpathy 开源了 LLM Wiki 思路，我们把它做成了<strong>完整商业产品</strong>。他提供想法，我们提供交付。
    </p>
  </div>
</div>

</div><!-- 场景分割线：给 Agent 用 -->
<div class="scene-bar">
  <p>不只是给人看的知识库——<strong>你的 Agent 也可以调用它</strong></p>
</div>



<!-- 效果图 — Obsidian 图谱 -->
<div style="padding:0 24px 80px;max-width:960px;margin:0 auto;text-align:center;">
  <div style="font-family:var(--font-sans);font-size:11px;letter-spacing:2px;color:var(--amber);text-transform:uppercase;margin-bottom:10px;">交付效果</div>
  <h2 style="font-family:var(--font-serif);font-size:clamp(22px,3vw,30px);font-weight:600;color:var(--ink);margin-bottom:8px;">编译完成后，你的知识网络长这样</h2>
  <p style="font-size:14px;color:#888;margin-bottom:36px;line-height:1.7;">Obsidian 图谱不只是好看的图——它是你的<strong style="color:var(--ink)">第二大脑可视化</strong>。每个节点都是一条积累的知识，连接线是 AI 发现的关系。</p>

  <!-- 截图占位符：替换 src 为你的 Obsidian 图谱截图 -->
  <div style="position:relative;border-radius:16px;overflow:hidden;border:1px solid rgba(26,26,46,0.08);background:#f5f4f2;padding:40px 20px;">
    <img
      src="/assets/images/obsidian-graph-demo.png"
      alt="Obsidian 知识图谱示例"
      style="max-width:100%;border-radius:10px;box-shadow:0 8px 32px rgba(26,26,46,0.12);"
      onerror="this.style.display='none';this.nextElementSibling.style.display='flex';"
    >
    <!-- 截图加载失败占位 -->
    <div style="display:none;align-items:center;justify-content:center;min-height:200px;flex-direction:column;gap:12px;color:#999;">
      <div style="font-size:48px;">🔍</div>
      <div style="font-family:var(--font-sans);font-size:14px;">📸 截图占位：/assets/images/obsidian-graph-demo.png</div>
      <div style="font-family:var(--font-sans);font-size:12px;color:#bbb;">请上传你的 Obsidian 图谱截图 → 保存到 /assets/images/obsidian-graph-demo.png</div>
    </div>
    <div style="position:absolute;bottom:16px;right:16px;background:rgba(26,26,46,0.75);color:var(--gold);font-size:11px;padding:4px 10px;border-radius:8px;font-family:var(--font-sans);">
      Obsidian 本地截图 · Graph View
    </div>
  </div>
  <p style="font-size:12px;color:#bbb;margin-top:14px;font-family:var(--font-sans);">
    ▲ 上图为陈露个人知识库截图（2026年4月），已获授权展示
  </p>
</div>


<!-- 信任背书：自己的案例 -->
<div style="padding:0 24px 60px;max-width:760px;margin:0 auto;">
  <div style="text-align:center;margin-bottom:32px;">
    <div style="font-family:var(--font-sans);font-size:11px;letter-spacing:2px;color:var(--amber);text-transform:uppercase;margin-bottom:10px;">真实案例</div>
    <h2 style="font-family:var(--font-serif);font-size:clamp(22px,3vw,30px);font-weight:600;color:var(--ink);">陈露自己的知识资产系统</h2>
  </div>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;">
    <div style="padding:32px;border-radius:16px;background:#fff;border:1px solid rgba(26,26,46,0.07);text-align:center;">
      <div style="font-size:36px;margin-bottom:12px;">📚</div>
      <div style="font-family:var(--font-serif);font-size:32px;font-weight:700;color:var(--ink);">1500+</div>
      <div style="font-family:var(--font-sans);font-size:12px;color:#888;margin-top:4px;">篇文章与笔记</div>
    </div>
    <div style="padding:32px;border-radius:16px;background:#fff;border:1px solid rgba(26,26,46,0.07);text-align:center;">
      <div style="font-size:36px;margin-bottom:12px;">🕸️</div>
      <div style="font-family:var(--font-serif);font-size:32px;font-weight:700;color:var(--ink);">1:7</div>
      <div style="font-family:var(--font-sans);font-size:12px;color:#888;margin-top:4px;">引用连接比（AI生成双链）</div>
    </div>
    <div style="padding:32px;border-radius:16px;background:#fff;border:1px solid rgba(26,26,46,0.07);text-align:center;">
      <div style="font-size:36px;margin-bottom:12px;">🤖</div>
      <div style="font-family:var(--font-serif);font-size:32px;font-weight:700;color:var(--ink);">3个</div>
      <div style="font-family:var(--font-sans);font-size:12px;color:#888;margin-top:4px;">专属 AI Agent 直连调用</div>
    </div>
    <div style="padding:32px;border-radius:16px;background:#fff;border:1px solid rgba(26,26,46,0.07);text-align:center;">
      <div style="font-size:36px;margin-bottom:12px;">💡</div>
      <div style="font-family:var(--font-serif);font-size:32px;font-weight:700;color:var(--ink);">15年</div>
      <div style="font-family:var(--font-sans);font-size:12px;color:#888;margin-top:4px;">持续积累沉淀</div>
    </div>
  </div>

  <div style="margin-top:28px;padding:28px 32px;border-radius:16px;background:rgba(232,168,56,0.06);border:1px solid rgba(232,168,56,0.12);border-left:3px solid var(--gold);">
    <p style="font-family:var(--font-serif);font-size:17px;font-style:italic;color:var(--ink);line-height:1.7;margin:0 0 12px;">
      "我做了15年的个人知识管理，用过 印象笔记、Notion、飞书……最终选 Obsidian + AI 编译这条路，因为它解决了所有我踩过的坑。"
    </p>
    <p style="font-family:var(--font-sans);font-size:13px;color:#888;margin:0;">
      — 陈露，OPClab 发起人，前NPLUS Digital 首席知识官
    </p>
  </div>
</div>



<!-- AGENTS.md 说明块 -->
<div class="agentsmd-block">
  <div class="agentsmd-inner">
    <h3>📋 AGENTS.md — Agent 的行为说明书</h3>
    <p>这是你知识库的"Agent接入层"标准文件。它告诉Agent：哪些目录可读、哪些可写、如何更新MEMORY.md、如何建立双链。</p>
    <p>Karpathy 在2026年4月分享了完全相同的方法论，并指出：<em>"为非开发人员搭建此类系统的产品化方案，蕴含着巨大机遇。"</em></p>
    <div class="code-preview">
<span class="comment"># AGENTS.md — 知识库操作规范</span>
<span class="key">## 目录权限</span>
<span class="key">00-Inbox/</span>    <span class="val">可读可写</span>  <span class="comment">// 新内容投递区</span>
<span class="key">01-Raw/</span>     <span class="val">只读</span>       <span class="comment">// 原始档案，禁止修改</span>
<span class="key">02-Wiki/</span>     <span class="val">可读可写</span>  <span class="comment">// LLM 编译区</span>
<span class="key">05-Agent-Space/</span> <span class="val">可读可写</span>  <span class="comment">// Agent 专属隔离区</span>
<span class="key">MEMORY.md</span>   <span class="val">追加写入</span>  <span class="comment">// Agent 持久记忆</span>
    </div>
  </div>
</div>

<!-- Human 产品线定价 -->
<div class="pricing-section">
  <div class="section-label">服务方案</div>
  <h2 class="section-title">个人 / 团队线</h2>
  <p style="font-size:13px;color:#999;text-align:center;margin-top:-32px;margin-bottom:0;font-family:var(--font-sans);">
    三层可独立购买，也可打包享受全链路优惠价
  </p>
  <div class="pricing-grid">
    <div class="pricing-card">
      <div class="pricing-level">L1 · DIY</div>
      <h3>模板 + 指南</h3>
      <div class="pricing-price">¥299<span> / 次</span></div>
      <p class="pricing-desc">适合有一定技术能力，想自己动手的用户</p>
      <ul class="pricing-features">
        <li><span class="check">✓</span> Obsidian Vault 模板库</li>
        <li><span class="check">✓</span> 目录结构设计规范</li>
        <li><span class="check">✓</span> 基础导入使用指南</li>
        <li><span class="check">✓</span> AGENTS.md 模板</li>
        <li><span class="check">✓</span> Agent 接口配置说明</li>
      </ul>
    </div>

    <div class="pricing-card featured">
      <div class="pricing-level">L2 · 推荐 ★</div>
      <h3>快速搭建 + AI编译</h3>
      <div class="pricing-price">¥999<span> / 次</span></div>
      <div class="pricing-tag">含 Layer 1 + Layer 2</div>
      <p class="pricing-desc">适合想快速见效，不愿自己整理的用户</p>
      <ul class="pricing-features">
        <li><span class="check">✓</span> L1 全部内容</li>
        <li><span class="check">✓</span> 首次 AI 增量编译</li>
        <li><span class="check">✓</span> 双链关系网络生成</li>
        <li><span class="check">✓</span> MEMORY.md 初始化</li>
        <li><span class="check">✓</span> MCP Server 基础配置</li>
        <li><span class="check">✓</span> <strong>3次增量编译</strong>（微信/邮件发我，48小时内完成）</li>
        <li><span class="check">✓</span> 超出次数按 ¥200/次 补价，不强制</li>
      </ul>
    </div>

    <div class="pricing-card">
      <div class="pricing-level">L3 · 定制</div>
      <h3>全流程托管</h3>
      <div class="pricing-price">¥2999<span> 起</span></div>
      <div class="pricing-tag">含 Layer 1 + Layer 2 + Layer 3</div>
      <p class="pricing-desc">适合内容量大，需要深度定制的用户</p>
      <ul class="pricing-features">
        <li><span class="check">✓</span> L2 全部内容</li>
        <li><span class="check">✓</span> 内容整理咨询（不限次数）</li>
        <li><span class="check">✓</span> 每周增量编译（我来做）</li>
        <li><span class="check">✓</span> 矛盾检测服务</li>
        <li><span class="check">✓</span> 健康检查报告</li>
        <li><span class="check">✓</span> RAG API 搭建 + MCP Server</li>
      </ul>
    </div>
  </div>

  <!-- 编译说明 -->
  <div style="text-align:center;margin-top:28px;font-size:13px;color:#999;font-family:var(--font-sans);">
    <strong style="color:var(--ink)">★ 编译流程说明</strong><br>
    增量编译 = 半自动：工具全自动跑，你验收确认。提交方式：微信/邮件 → 我触发编译 → 48小时内交付。
  </div>
</div>

<!-- 全链路打包套餐 -->
<div style="padding:0 24px 60px;max-width:1040px;margin:0 auto;">
  <div style="padding:48px 40px;border-radius:20px;background:var(--ink);color:var(--cream);text-align:center;max-width:640px;margin:0 auto;">
    <div style="font-family:var(--font-sans);font-size:11px;letter-spacing:3px;color:var(--gold);text-transform:uppercase;margin-bottom:12px;">一站式解决方案</div>
    <h2 style="font-family:var(--font-serif);font-size:28px;font-weight:600;color:var(--cream);margin-bottom:8px;">知识资产化全链路套餐</h2>
    <p style="font-size:14px;color:rgba(250,250,248,0.7);line-height:1.7;margin-bottom:24px;">Layer 1 + Layer 2 + Layer 3 全部包含，一步到位<br>比单买省 <strong style="color:var(--gold)">¥1298</strong></p>
    <div style="font-family:var(--font-sans);font-size:36px;font-weight:700;color:var(--gold);margin-bottom:24px;">¥4999 <span style="font-size:14px;font-weight:400;color:rgba(250,250,248,0.5);">/ 全套</span></div>
    <ul style="list-style:none;padding:0;margin:0 0 28px;text-align:left;display:inline-block;">
      <li style="font-size:13px;padding:6px 0;color:rgba(250,250,248,0.8);display:flex;align-items:center;gap:10px;">
        <span style="color:var(--gold);">✓</span> Obsidian Vault 完整搭建 + 目录规范
      </li>
      <li style="font-size:13px;padding:6px 0;color:rgba(250,250,248,0.8);display:flex;align-items:center;gap:10px;">
        <span style="color:var(--gold);">✓</span> 全量内容首次 AI 编译
      </li>
      <li style="font-size:13px;padding:6px 0;color:rgba(250,250,248,0.8);display:flex;align-items:center;gap:10px;">
        <span style="color:var(--gold);">✓</span> 每月增量编译（持续6个月）
      </li>
      <li style="font-size:13px;padding:6px 0;color:rgba(250,250,248,0.8);display:flex;align-items:center;gap:10px;">
        <span style="color:var(--gold);">✓</span> 矛盾检测 + 健康检查
      </li>
      <li style="font-size:13px;padding:6px 0;color:rgba(250,250,248,0.8);display:flex;align-items:center;gap:10px;">
        <span style="color:var(--gold);">✓</span> MCP Server + RAG API 配置
      </li>
      <li style="font-size:13px;padding:6px 0;color:rgba(250,250,248,0.8);display:flex;align-items:center;gap:10px;">
        <span style="color:var(--gold);">✓</span> OpenClaw 直连测试
      </li>
    </ul>
    <a href="https://www.zaih.com/falcon/mentors/2bhjbfp3t2q" class="btn-primary" style="background:var(--gold);color:var(--ink);">预约全链路咨询 →</a>
  </div>
</div>

<!-- Agent 基础设施线 -->
<div class="agent-section">
  <div class="agent-badge">★ 差异化壁垒</div>
  <h2 class="section-title">Agent 基础设施线</h2>
  <p style="font-size:14px;color:#888;max-width:520px;margin:0 auto 0;line-height:1.7;">
    你的知识库不只是给人看——<strong style="color:var(--ink)">Agent 也可以主动调用它</strong>。这是真正的知识资产化：AI系统拥有持续学习的"企业外脑"。
  </p>
  <div class="agent-grid">
    <div class="agent-card">
      <div class="arch-num">Agent Starter</div>
      <h3>给 Agent 配一个外脑</h3>
      <div class="price">¥1999<span> / 次</span></div>
      <p>适合 AI 开发者、个人 Agent 用户：给 Agent 一个可读写的知识库，让它越用越懂你的业务。</p>
      <p style="font-size:12px;color:rgba(250,250,248,0.5);margin-top:8px;">💡 人用 + Agent 用 = 双向价值最大化（联系陈露定制组合方案）</p>
      <ul class="agent-features">
        <li><span class="check">✓</span> Vault 搭建 + MCP Server 配置</li>
        <li><span class="check">✓</span> MEMORY.md 协议初始化</li>
        <li><span class="check">✓</span> OpenClaw / Claude 接入测试</li>
        <li><span class="check">✓</span> AGENTS.md 定制编写</li>
      </ul>
    </div>
    <div class="agent-card">
      <div class="arch-num">Agent Business</div>
      <h3>企业 Agent 知识中台</h3>
      <div class="price">¥4999<span> 起</span></div>
      <p>适合企业 AI 部署团队：多 Agent 共享知识库，权限分级，自动编译，持续学习。</p>
      <ul class="agent-features">
        <li><span class="check">✓</span> Agent Starter 全部内容</li>
        <li><span class="check">✓</span> 多 Agent 共享知识库架构</li>
        <li><span class="check">✓</span> 每周自动编译 + 健康检查</li>
        <li><span class="check">✓</span> 知识审计日志</li>
        <li><span class="check">✓</span> MCP 协议年度适配</li>
      </ul>
    </div>
  </div>
</div>

<!-- 工作流程 -->
<div class="flow-section">
  <div class="section-label">交付流程</div>
  <h2 class="section-title">四步完成搭建</h2>
  <div class="flow-steps">
    <div class="flow-step">
      <div class="flow-num">1</div>
      <div class="flow-content">
        <h4>发送模板包</h4>
        <p>收到订单后发送 Obsidian Vault 模板库、安装指南、AGENTS.md 模板</p>
      </div>
    </div>
    <div class="flow-step">
      <div class="flow-num">2</div>
      <div class="flow-content">
        <h4>导入你的内容</h4>
        <p>把现有文章、笔记、素材复制到对应目录，支持 URL、PDF、Markdown、微信笔记等格式</p>
      </div>
    </div>
    <div class="flow-step">
      <div class="flow-num">3</div>
      <div class="flow-content">
        <h4>AI 编译知识库</h4>
        <p>OpenClaw 读取内容 → 增量编译 → 生成双链 → 更新 MEMORY.md → 构建知识网络</p>
      </div>
    </div>
    <div class="flow-step">
      <div class="flow-num">4</div>
      <div class="flow-content">
        <h4>连接 Agent</h4>
        <p>配置 MCP Server / RAG API / OpenClaw 直连——你的 Agent 从此可以主动读写知识库</p>
      </div>
    </div>
  </div>
</div>



<!-- FAQ -->
<div style="padding:0 24px 60px;max-width:720px;margin:0 auto;">
  <div style="text-align:center;margin-bottom:40px;">
    <div style="font-family:var(--font-sans);font-size:11px;letter-spacing:2px;color:var(--amber);text-transform:uppercase;margin-bottom:10px;">常见问题</div>
    <h2 style="font-family:var(--font-serif);font-size:clamp(22px,3vw,30px);font-weight:600;color:var(--ink);">FAQ</h2>
  </div>

  <div style="display:flex;flex-direction:column;gap:16px;">

    <details style="border-radius:14px;border:1px solid rgba(26,26,46,0.08);overflow:hidden;background:#fff;">
      <summary style="padding:20px 24px;cursor:pointer;font-family:var(--font-serif);font-size:16px;font-weight:600;color:var(--ink);list-style:none;display:flex;justify-content:space-between;align-items:center;">
        需要准备什么资料？
        <span style="font-size:18px;color:var(--amber);transition:transform 0.2s;" id="arrow1">▾</span>
      </summary>
      <div style="padding:0 24px 20px;font-size:14px;color:#666;line-height:1.7;font-family:var(--font-sans);">
        只需要你的<strong style="color:var(--ink)">原始积累</strong>：收藏的文章、微信笔记、有道云笔记、印象笔记……任何格式都可以，我们帮你统一整理进 Obsidian。不需要你自己整理。
      </div>
    </details>

    <details style="border-radius:14px;border:1px solid rgba(26,26,46,0.08);overflow:hidden;background:#fff;">
      <summary style="padding:20px 24px;cursor:pointer;font-family:var(--font-serif);font-size:16px;font-weight:600;color:var(--ink);list-style:none;display:flex;justify-content:space-between;align-items:center;">
        增量编译是什么？我需要懂技术吗？
        <span style="font-size:18px;color:var(--amber);">▾</span>
      </summary>
      <div style="padding:0 24px 20px;font-size:14px;color:#666;line-height:1.7;font-family:var(--font-sans);">
        增量编译 = <strong style="color:var(--ink)">你把新内容发我，我自动更新你的知识网络</strong>。你不需要懂任何技术——工具全自动跑，你只需要验收最终结果。整个过程微信里完成。
      </div>
    </details>

    <details style="border-radius:14px;border:1px solid rgba(26,26,46,0.08);overflow:hidden;background:#fff;">
      <summary style="padding:20px 24px;cursor:pointer;font-family:var(--font-serif);font-size:16px;font-weight:600;color:var(--ink);list-style:none;display:flex;justify-content:space-between;align-items:center;">
        3次编译用完了怎么办？
        <span style="font-size:18px;color:var(--amber);">▾</span>
      </summary>
      <div style="padding:0 24px 20px;font-size:14px;color:#666;line-height:1.7;font-family:var(--font-sans);">
        L2 用户可随时按 <strong style="color:var(--ink)">¥200/次</strong> 追加编译次数，不强制。也可以升级 L3 享受每月一次的定期编译。
      </div>
    </details>

    <details style="border-radius:14px;border:1px solid rgba(26,26,46,0.08);overflow:hidden;background:#fff;">
      <summary style="padding:20px 24px;cursor:pointer;font-family:var(--font-serif);font-size:16px;font-weight:600;color:var(--ink);list-style:none;display:flex;justify-content:space-between;align-items:center;">
        Obsidian 是免费软件吗？数据存在哪？
        <span style="font-size:18px;color:var(--amber);">▾</span>
      </summary>
      <div style="padding:0 24px 20px;font-size:14px;color:#666;line-height:1.7;font-family:var(--font-sans);">
        Obsidian <strong style="color:var(--ink)">完全免费</strong>（本地版），没有订阅费。你的数据存在你自己的电脑/硬盘里，不在任何云端——这是它比 Notion、飞书笔记最大的优势：数据完全属于你。
      </div>
    </details>

    <details style="border-radius:14px;border:1px solid rgba(26,26,46,0.08);overflow:hidden;background:#fff;">
      <summary style="padding:20px 24px;cursor:pointer;font-family:var(--font-serif);font-size:16px;font-weight:600;color:var(--ink);list-style:none;display:flex;justify-content:space-between;align-items:center;">
        Agent Starter 和 L2/L3 有什么关系？
        <span style="font-size:18px;color:var(--amber);">▾</span>
      </summary>
      <div style="padding:0 24px 20px;font-size:14px;color:#666;line-height:1.7;font-family:var(--font-sans);">
        <strong style="color:var(--ink)">L1/L2/L3 是给人用的知识库</strong>，<strong style="color:var(--ink)">Agent Starter 是给 AI Agent 用的</strong>。两者可以独立购买，也可以一起买——陈露自己的知识库就是 L3 + Agent Starter 的组合。<a href="#agent-section" style="color:var(--amber);text-decoration:none;">查看 Agent 产品线 →</a>
      </div>
    </details>

  </div>
</div>



<!-- CTA -->
<div class="service-cta">
  <h2>让知识真正为你和你的 Agent 工作</h2>
  <p>一次搭建，持续增值。你的积累值得被激活——不只是给你自己用，也给你的 AI Agent 用。</p>
  <div class="cta-buttons">
    <a href="https://www.zaih.com/falcon/mentors/2bhjbfp3t2q" class="btn-primary">在行约见咨询 →</a>
    <a href="mailto:chenluaihr@gmail.com?subject=知识基础设施服务咨询" class="btn-secondary">邮件联系</a>
  </div>
</div>
