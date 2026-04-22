---
layout: page
title: 个人知识维基 · 搭建服务
subtitle: 让知识真正成为资产
---

<style>
/* ================================================
   服务产品页 — B方案风格
   ================================================ */

.service-hero {
  text-align: center;
  padding: 100px 24px 60px;
  max-width: 680px;
  margin: 0 auto;
}
.service-hero h1 {
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(32px, 5vw, 48px);
  font-weight: 600;
  color: #1A1A2E;
  margin-bottom: 16px;
  line-height: 1.2;
}
.service-hero h1 em {
  font-style: italic;
  color: #C4882F;
}
.service-hero-sub {
  font-size: 17px;
  color: #666;
  line-height: 1.7;
  margin-bottom: 32px;
}
.service-hero-tagline {
  font-family: 'DM Sans', sans-serif;
  font-size: 13px;
  letter-spacing: 2px;
  color: #C4882F;
  text-transform: uppercase;
}

/* 痛点区域 */
.pain-section {
  padding: 60px 24px;
  max-width: 720px;
  margin: 0 auto;
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
  font-family: 'Cormorant Garamond', serif;
  font-size: 18px;
  font-weight: 600;
  color: #1A1A2E;
  margin-bottom: 8px;
}
.pain-card p {
  font-size: 13px;
  color: #888;
  line-height: 1.6;
  margin: 0;
}

/* 价值主张 */
.value-section {
  padding: 80px 24px;
  max-width: 780px;
  margin: 0 auto;
  text-align: center;
}
.value-box {
  padding: 48px 40px;
  border-radius: 20px;
  background: #1A1A2E;
  color: #FAFAF8;
}
.value-box h2 {
  font-family: 'Cormorant Garamond', serif;
  font-size: 28px;
  font-weight: 600;
  margin-bottom: 20px;
}
.value-box h2 em {
  color: #E8A838;
  font-style: italic;
}
.value-box p {
  font-size: 15px;
  line-height: 1.8;
  color: rgba(250,250,248,0.75);
}
.value-box strong {
  color: #E8A838;
}

/* 服务版本 */
.pricing-section {
  padding: 80px 24px;
  max-width: 960px;
  margin: 0 auto;
}
.pricing-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-top: 48px;
}
.pricing-card {
  padding: 36px 28px;
  border-radius: 18px;
  background: #fff;
  border: 1px solid rgba(26,26,46,0.06);
  transition: all 0.35s;
}
.pricing-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 16px 44px rgba(26,26,46,0.08);
  border-color: transparent;
}
.pricing-card.featured {
  background: #1A1A2E;
  color: #FAFAF8;
  border-color: transparent;
  transform: scale(1.02);
}
.pricing-card.featured:hover {
  transform: scale(1.02) translateY(-5px);
}
.pricing-level {
  font-family: 'DM Sans', sans-serif;
  font-size: 10px;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: #C4882F;
  margin-bottom: 8px;
}
.pricing-card.featured .pricing-level {
  color: #E8A838;
}
.pricing-card h3 {
  font-family: 'Cormorant Garamond', serif;
  font-size: 22px;
  font-weight: 600;
  margin-bottom: 8px;
  color: #1A1A2E;
}
.pricing-card.featured h3 {
  color: #FAFAF8;
}
.pricing-price {
  font-family: 'DM Sans', sans-serif;
  font-size: 32px;
  font-weight: 700;
  color: #C4882F;
  margin-bottom: 4px;
}
.pricing-card.featured .pricing-price {
  color: #E8A838;
}
.pricing-price span {
  font-size: 14px;
  font-weight: 400;
  color: #999;
}
.pricing-card.featured .pricing-price span {
  color: rgba(250,250,248,0.5);
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
  border-bottom: 1px solid #F0EEEA;
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
  color: #C4882F;
  flex-shrink: 0;
}
.pricing-card.featured .pricing-features .check {
  color: #E8A838;
}

/* 工作流程 */
.flow-section {
  padding: 80px 24px;
  max-width: 780px;
  margin: 0 auto;
}
.flow-steps {
  display: flex;
  flex-direction: column;
  gap: 24px;
  margin-top: 48px;
}
.flow-step {
  display: flex;
  gap: 20px;
  padding: 24px;
  border-radius: 14px;
  background: #fff;
  border: 1px solid rgba(26,26,46,0.06);
}
.flow-num {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: #1A1A2E;
  color: #E8A838;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Cormorant Garamond', serif;
  font-size: 18px;
  font-weight: 700;
  flex-shrink: 0;
}
.flow-content h4 {
  font-family: 'Cormorant Garamond', serif;
  font-size: 18px;
  font-weight: 600;
  color: #1A1A2E;
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
  max-width: 600px;
  margin: 0 auto;
}
.service-cta h2 {
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(26px, 4vw, 36px);
  font-weight: 600;
  color: #1A1A2E;
  margin-bottom: 16px;
}
.service-cta p {
  font-size: 14px;
  color: #888;
  margin-bottom: 32px;
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
  background: #1A1A2E;
  color: #E8A838;
  text-decoration: none;
  border-radius: 10px;
  font-family: 'DM Sans', sans-serif;
  font-size: 15px;
  font-weight: 600;
  transition: all 0.3s;
}
.btn-primary:hover {
  background: #C4882F;
  color: #fff;
}
.btn-secondary {
  display: inline-block;
  padding: 14px 32px;
  border: 1.5px solid #D4D0CA;
  color: #666;
  text-decoration: none;
  border-radius: 10px;
  font-family: 'DM Sans', sans-serif;
  font-size: 15px;
  font-weight: 500;
  transition: all 0.3s;
}
.btn-secondary:hover {
  border-color: #C4882F;
  color: #C4882F;
}

@media (max-width: 768px) {
  .pain-grid, .pricing-grid {
    grid-template-columns: 1fr;
  }
  .pricing-card.featured {
    transform: none;
    order: -1;
  }
  .pricing-card.featured:hover {
    transform: translateY(-5px);
  }
  .service-hero { padding: 60px 20px 40px; }
  .flow-step { flex-direction: column; text-align: center; }
  .flow-num { margin: 0 auto; }
}
</style>

<!-- HERO -->
<div class="service-hero">
  <div class="service-hero-tagline">知识即资产 · 交付服务</div>
  <h1>个人知识维基<br><em>搭建服务</em></h1>
  <p class="service-hero-sub">你只管积累，AI帮你整理。<br>一次部署，持续增值。</p>
</div>

<!-- 痛点 -->
<div class="pain-section">
  <div class="section-label">你是不是也有这样的困扰</div>
  <h2 class="section-title">知识管理三大难题</h2>
  <div class="pain-grid">
    <div class="pain-card">
      <h4>积累了，找不到</h4>
      <p>几百篇文章、上千条笔记<br>真正要用的时候无从下手</p>
    </div>
    <div class="pain-card">
      <h4>整理了，无体系</h4>
      <p>收藏了一堆，没有结构<br>知识无法复利增长</p>
    </div>
    <div class="pain-card">
      <h4>想整理，嫌麻烦</h4>
      <p>知道知识管理重要<br>但没有时间精力去做</p>
    </div>
  </div>
</div>

<!-- 价值主张 -->
<div class="value-section">
  <div class="value-box">
    <h2>让知识真正成为<em>资产</em></h2>
    <p>我们帮你搭建一套<strong>AI驱动的个人知识库</strong>。<br><br>
    不需要你整理分类，不需要你维护链接。<br>
    你只管积累，AI自动编译成结构化知识网络。<br><br>
    <strong>下次写文章、做决策、找素材</strong>，直接问AI就能调出。</p>
  </div>
</div>

<!-- 服务版本 -->
<div class="pricing-section">
  <div class="section-label">选择适合你的版本</div>
  <h2 class="section-title">三级服务方案</h2>
  <div class="pricing-grid">
    <div class="pricing-card">
      <div class="pricing-level">L1 基础版</div>
      <h3>模板包 + 指南</h3>
      <div class="pricing-price">¥299<span>/次</span></div>
      <p class="pricing-desc">适合有一定技术能力，想自己操作的用户</p>
      <ul class="pricing-features">
        <li><span class="check">✓</span> Obsidian 模板库</li>
        <li><span class="check">✓</span> 使用指南文档</li>
        <li><span class="check">✓</span> 目录结构说明</li>
        <li><span class="check">✓</span> 自己导入内容</li>
      </ul>
    </div>

    <div class="pricing-card featured">
      <div class="pricing-level">L2 标准版 · 推荐</div>
      <h3>模板 + 编译服务</h3>
      <div class="pricing-price">¥999<span>/次</span></div>
      <p class="pricing-desc">适合想快速见效，不愿自己整理的用户</p>
      <ul class="pricing-features">
        <li><span class="check">✓</span> L1 全部内容</li>
        <li><span class="check">✓</span> 首次AI编译服务</li>
        <li><span class="check">✓</span> 提供1次编译指导</li>
        <li><span class="check">✓</span> 使用答疑支持</li>
      </ul>
    </div>
    
    <div class="pricing-card">
      <div class="pricing-level">L3 定制版</div>
      <h3>全流程托管服务</h3>
      <div class="pricing-price">¥2999<span>起</span></div>
      <p class="pricing-desc">适合内容量大，需要深度定制的用户</p>
      <ul class="pricing-features">
        <li><span class="check">✓</span> L2 全部内容</li>
        <li><span class="check">✓</span> 知识需求轻咨询</li>
        <li><span class="check">✓</span> 提供3次持续编译</li>
        <li><span class="check">✓</span> 专属技术支持</li>
      </ul>
    </div>
  </div>
</div>

<!-- 工作流程 -->
<div class="flow-section">
  <div class="section-label">如何交付</div>
  <h2 class="section-title">四步完成搭建</h2>
  <div class="flow-steps">
    <div class="flow-step">
      <div class="flow-num">1</div>
      <div class="flow-content">
        <h4>发送模板包</h4>
        <p>收到订单后，我们发送 Obsidian 模板库和安装指南</p>
      </div>
    </div>
    <div class="flow-step">
      <div class="flow-num">2</div>
      <div class="flow-content">
        <h4>导入你的内容</h4>
        <p>把现有文章、笔记、素材复制到对应目录，格式不限</p>
      </div>
    </div>
    <div class="flow-step">
      <div class="flow-num">3</div>
      <div class="flow-content">
        <h4>AI 编译知识库</h4>
        <p>我们的AI读取内容、提炼关键信息、生成结构化Wiki页面</p>
      </div>
    </div>
    <div class="flow-step">
      <div class="flow-num">4</div>
      <div class="flow-content">
        <h4>开始使用</h4>
        <p>在 Obsidian 中查看效果，随时搜索、浏览、关联</p>
      </div>
    </div>
  </div>
</div>

<!-- 差异化优势 -->
<div class="pain-section">
  <div class="section-label">为什么选择我们</div>
  <h2 class="section-title">与传统方案的区别</h2>
  <div class="pain-grid">
    <div class="pain-card">
      <h4>vs 印象笔记/Notion</h4>
      <p>数据在本地，完全自主<br>可接任意AI模型，不受平台限制</p>
    </div>
    <div class="pain-card">
      <h4>vs 手动整理</h4>
      <p>AI自动编译，无需维护<br>一次部署，持续增值</p>
    </div>
    <div class="pain-card">
      <h4>vs 学习方法论</h4>
      <p>不用学复杂体系<br>只管积累，整理交给AI</p>
    </div>
  </div>
</div>

<!-- CTA -->
<div class="service-cta">
  <h2>让知识真正为你工作</h2>
  <p>一次搭建，持续增值。你的积累值得被激活。</p>
  <div class="cta-buttons">
    <a href="mailto:chenluaihr@gmail.com?subject=知识维基服务咨询" class="btn-primary">立即咨询 →</a>
    <a href="/about" class="btn-secondary">了解更多</a>
  </div>
</div>
