---
layout: page
title: 鐭ヨ瘑鍩虹璁炬柦 路 鏈嶅姟浜у搧
subtitle: 璁╃煡璇嗙湡姝ｆ垚涓鸿祫浜?---

<style>
/* ================================================
   鏈嶅姟浜у搧椤?鈥?涓夊眰鏋舵瀯椋庢牸
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

/* 宸紓鍖栨爣绛?*/
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

/* 鍦烘櫙鍒嗗壊绾?*/
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

/* 涓夊眰鏋舵瀯姒傝 */
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

/* 鐥涚偣 */
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

/* 瀹氫环 */
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

/* Agent 浜у搧绾?*/
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

/* 宸ヤ綔娴佺▼ */
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

/* AGENTS.md 璇存槑鍧?*/
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

/* 鍝嶅簲寮?*/
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
  <div class="hero-eyebrow">鐭ヨ瘑鍩虹璁炬柦 路 鏈嶅姟浜у搧</div>
  <h1>璁?AI 鎴愪负浣犵殑<em>澶栬剳</em></h1>
  <p class="hero-sub">
    涓嶅彧鏄瑪璁版暣鐞嗏€斺€斿府浣犳惌寤轰竴濂?strong>AI鍙洿鎺ヨ皟鐢ㄧ殑鐭ヨ瘑璧勪骇绯荤粺</strong>銆?br>
    浣犲彧绠＄Н绱紝AI缂栬瘧鎴愮粨鏋勫寲缃戠粶锛孉gent瓒婄敤瓒婃噦浣犮€?  </p>
  <div class="hero-tags">
    <span class="hero-tag">Obsidian 鏈湴閮ㄧ讲</span>
    <span class="hero-tag">AI 澧為噺缂栬瘧</span>
    <span class="hero-tag highlight">鈽?Agent 鐩磋繛璋冪敤</span>
    <span class="hero-tag">MCP Server</span>
    <span class="hero-tag">MEMORY.md 鍗忚</span>
  </div>
</div>

<!-- 鍦烘櫙鍒嗗壊绾匡細缁?Agent 鐢?-->
<div class="scene-bar">
  <p>涓嶅彧鏄粰浜虹湅鐨勭煡璇嗗簱鈥斺€?strong>浣犵殑 Agent 涔熷彲浠ヨ皟鐢ㄥ畠</strong></p>
</div>

<!-- 涓夊眰鏋舵瀯姒傝 -->
<div class="architecture-section">
  <div class="section-label">浜у搧鏋舵瀯</div>
  <h2 class="section-title">涓夊眰浣撶郴锛屼粠绉疮鍒版櫤鑳?/h2>
  <div class="arch-grid">
    <div class="arch-card">
      <div class="arch-num">Layer 1</div>
      <div class="arch-icon">馃摜</div>
      <h3>鐭ヨ瘑娌夌Н</h3>
      <div class="arch-en">Vault Design</div>
      <p>Obsidian Vault 瑙勫垝銆佺洰褰曠粨鏋勩€佸師濮嬬礌鏉愬綊妗?/p>
      <div class="arch-tags">
        <span class="arch-tag">Obsidian</span>
        <span class="arch-tag">鐩綍璁捐</span>
        <span class="arch-tag">鏍煎紡瀵煎叆</span>
      </div>
    </div>
    <div class="arch-card">
      <div class="arch-num">Layer 2 路 鏍稿績</div>
      <div class="arch-icon">鈿欙笍</div>
      <h3>缂栬瘧鍔犲伐</h3>
      <div class="arch-en">LLM Compilation</div>
      <p>AI澧為噺缂栬瘧銆佸弻閾剧敓鎴愩€佺煕鐩炬娴嬨€佺煡璇嗙綉缁滆嚜鍔ㄦ瀯寤?/p>
      <div class="arch-tags">
        <span class="arch-tag">OpenClaw 缂栬瘧</span>
        <span class="arch-tag">鍙岄摼鐢熸垚</span>
        <span class="arch-tag">鐭涚浘妫€娴?/span>
      </div>
    </div>
    <div class="arch-card">
      <div class="arch-num">Layer 3 路 澹佸瀿</div>
      <div class="arch-icon">馃攲</div>
      <h3>杩炴帴浣跨敤</h3>
      <div class="arch-en">Agent Interface</div>
      <p>MCP Server銆丷AG API銆丱penClaw 鐩磋繛鈥斺€擜gent鍙富鍔ㄨ鍐?/p>
      <div class="arch-tags">
        <span class="arch-tag">MCP Server</span>
        <span class="arch-tag">RAG API</span>
        <span class="arch-tag">OpenClaw</span>
      </div>
    </div>
  </div>
</div>

<!-- 鐥涚偣 -->
<div class="pain-section">
  <div class="section-label">鐥涚偣</div>
  <h2 class="section-title">鐭ヨ瘑绠＄悊鐨勪笁澶у洶澧?/h2>
  <div class="pain-grid">
    <div class="pain-card">
      <h4>绉疮浜嗭紝鎵句笉鍒?/h4>
      <p>鍑犵櫨绡囨枃绔犮€佷笂鍗冩潯绗旇<br>鐪熸瑕佺敤鐨勬椂鍊欐棤浠庝笅鎵?/p>
    </div>
    <div class="pain-card">
      <h4>鏁寸悊浜嗭紝鏃犱綋绯?/h4>
      <p>鏀惰棌浜嗕竴鍫嗭紝娌℃湁缁撴瀯<br>鐭ヨ瘑鏃犳硶澶嶅埄澧為暱</p>
    </div>
    <div class="pain-card">
      <h4>鎯虫暣鐞嗭紝瀚岄夯鐑?/h4>
      <p>鐭ラ亾鐭ヨ瘑绠＄悊閲嶈<br>浣嗘病鏈夋椂闂寸簿鍔涘幓鍋?/p>
    </div>
  </div>
</div>

<!-- AGENTS.md 璇存槑鍧?-->
<div class="agentsmd-block">
  <div class="agentsmd-inner">
    <h3>馃搵 AGENTS.md 鈥?Agent 鐨勮涓鸿鏄庝功</h3>
    <p>杩欐槸浣犵煡璇嗗簱鐨?Agent鎺ュ叆灞?鏍囧噯鏂囦欢銆傚畠鍛婅瘔Agent锛氬摢浜涚洰褰曞彲璇汇€佸摢浜涘彲鍐欍€佸浣曟洿鏂癕EMORY.md銆佸浣曞缓绔嬪弻閾俱€?/p>
    <p>Karpathy 鍦?026骞?鏈堝垎浜簡瀹屽叏鐩稿悓鐨勬柟娉曡锛屽苟鎸囧嚭锛?em>"涓洪潪寮€鍙戜汉鍛樻惌寤烘绫荤郴缁熺殑浜у搧鍖栨柟妗堬紝钑村惈鐫€宸ㄥぇ鏈洪亣銆?</em></p>
    <div class="code-preview">
<span class="comment"># AGENTS.md 鈥?鐭ヨ瘑搴撴搷浣滆鑼?/span>
<span class="key">## 鐩綍鏉冮檺</span>
<span class="key">00-Inbox/</span>    <span class="val">鍙鍙啓</span>  <span class="comment">// 鏂板唴瀹规姇閫掑尯</span>
<span class="key">01-Raw/</span>     <span class="val">鍙</span>       <span class="comment">// 鍘熷妗ｆ锛岀姝慨鏀?/span>
<span class="key">02-Wiki/</span>     <span class="val">鍙鍙啓</span>  <span class="comment">// LLM 缂栬瘧鍖?/span>
<span class="key">05-Agent-Space/</span> <span class="val">鍙鍙啓</span>  <span class="comment">// Agent 涓撳睘闅旂鍖?/span>
<span class="key">MEMORY.md</span>   <span class="val">杩藉姞鍐欏叆</span>  <span class="comment">// Agent 鎸佷箙璁板繂</span>
    </div>
  </div>
</div>

<!-- Human 浜у搧绾垮畾浠?-->
<div class="pricing-section">
  <div class="section-label">鏈嶅姟鏂规</div>
  <h2 class="section-title">涓汉 / 鍥㈤槦绾?/h2>
  <p style="font-size:13px;color:#999;text-align:center;margin-top:-32px;margin-bottom:0;font-family:var(--font-sans);">
    涓夊眰鍙嫭绔嬭喘涔帮紝涔熷彲鎵撳寘浜彈鍏ㄩ摼璺紭鎯犱环
  </p>
  <div class="pricing-grid">
    <div class="pricing-card">
      <div class="pricing-level">L1 路 DIY</div>
      <h3>妯℃澘 + 鎸囧崡</h3>
      <div class="pricing-price">楼299<span> / 娆?/span></div>
      <p class="pricing-desc">閫傚悎鏈変竴瀹氭妧鏈兘鍔涳紝鎯宠嚜宸卞姩鎵嬬殑鐢ㄦ埛</p>
      <ul class="pricing-features">
        <li><span class="check">鉁?/span> Obsidian Vault 妯℃澘搴?/li>
        <li><span class="check">鉁?/span> 鐩綍缁撴瀯璁捐瑙勮寖</li>
        <li><span class="check">鉁?/span> 鍩虹瀵煎叆浣跨敤鎸囧崡</li>
        <li><span class="check">鉁?/span> AGENTS.md 妯℃澘</li>
        <li><span class="check">鉁?/span> Agent 鎺ュ彛閰嶇疆璇存槑</li>
      </ul>
    </div>

    <div class="pricing-card featured">
      <div class="pricing-level">L2 路 鎺ㄨ崘 鈽?/div>
      <h3>蹇€熸惌寤?+ AI缂栬瘧</h3>
      <div class="pricing-price">楼999<span> / 娆?/span></div>
      <div class="pricing-tag">鍚?Layer 1 + Layer 2</div>
      <p class="pricing-desc">閫傚悎鎯冲揩閫熻鏁堬紝涓嶆効鑷繁鏁寸悊鐨勭敤鎴?/p>
      <ul class="pricing-features">
        <li><span class="check">鉁?/span> L1 鍏ㄩ儴鍐呭</li>
        <li><span class="check">鉁?/span> 棣栨 AI 澧為噺缂栬瘧</li>
        <li><span class="check">鉁?/span> 鍙岄摼鍏崇郴缃戠粶鐢熸垚</li>
        <li><span class="check">鉁?/span> MEMORY.md 鍒濆鍖?/li>
        <li><span class="check">鉁?/span> MCP Server 鍩虹閰嶇疆</li>
        <li><span class="check">鉁?/span> 3涓湀鍐呭閲忕紪璇戯紙浜哄伐瑙﹀彂锛屾垜鏉ュ仛锛?/li>
      </ul>
    </div>

    <div class="pricing-card">
      <div class="pricing-level">L3 路 瀹氬埗</div>
      <h3>鍏ㄦ祦绋嬫墭绠?/h3>
      <div class="pricing-price">楼2999<span> 璧?/span></div>
      <div class="pricing-tag">鍚?Layer 1 + Layer 2 + Layer 3</div>
      <p class="pricing-desc">閫傚悎鍐呭閲忓ぇ锛岄渶瑕佹繁搴﹀畾鍒剁殑鐢ㄦ埛</p>
      <ul class="pricing-features">
        <li><span class="check">鉁?/span> L2 鍏ㄩ儴鍐呭</li>
        <li><span class="check">鉁?/span> 鍐呭鏁寸悊鍜ㄨ锛堜笉闄愭鏁帮級</li>
        <li><span class="check">鉁?/span> 姣忓懆澧為噺缂栬瘧锛堟垜鏉ュ仛锛?/li>
        <li><span class="check">鉁?/span> 鐭涚浘妫€娴嬫湇鍔?/li>
        <li><span class="check">鉁?/span> 鍋ュ悍妫€鏌ユ姤鍛?/li>
        <li><span class="check">鉁?/span> RAG API 鎼缓 + MCP Server</li>
      </ul>
    </div>
  </div>

  <!-- 缂栬瘧璇存槑 -->
  <div style="text-align:center;margin-top:28px;font-size:13px;color:#999;font-family:var(--font-sans);">
    <strong style="color:var(--ink)">鈽?缂栬瘧娴佺▼璇存槑</strong><br>
    澧為噺缂栬瘧 = 鍗婅嚜鍔細宸ュ叿鍏ㄨ嚜鍔ㄨ窇锛屼綘楠屾敹纭銆傚井淇?閭欢鍙戞垜 鈫?鎴戣Е鍙戠紪璇?鈫?浜や粯缁欎綘銆?  </div>
</div>

<!-- 鍏ㄩ摼璺墦鍖呭椁?-->
<div style="padding:0 24px 60px;max-width:1040px;margin:0 auto;">
  <div style="padding:48px 40px;border-radius:20px;background:var(--ink);color:var(--cream);text-align:center;max-width:640px;margin:0 auto;">
    <div style="font-family:var(--font-sans);font-size:11px;letter-spacing:3px;color:var(--gold);text-transform:uppercase;margin-bottom:12px;">涓€绔欏紡瑙ｅ喅鏂规</div>
    <h2 style="font-family:var(--font-serif);font-size:28px;font-weight:600;color:var(--cream);margin-bottom:8px;">鐭ヨ瘑璧勪骇鍖栧叏閾捐矾濂楅</h2>
    <p style="font-size:14px;color:rgba(250,250,248,0.7);line-height:1.7;margin-bottom:24px;">Layer 1 + Layer 2 + Layer 3 鍏ㄩ儴鍖呭惈锛屼竴姝ュ埌浣?br>姣斿崟涔扮渷 <strong style="color:var(--gold)">楼1298</strong></p>
    <div style="font-family:var(--font-sans);font-size:36px;font-weight:700;color:var(--gold);margin-bottom:24px;">楼4999 <span style="font-size:14px;font-weight:400;color:rgba(250,250,248,0.5);">/ 鍏ㄥ</span></div>
    <ul style="list-style:none;padding:0;margin:0 0 28px;text-align:left;display:inline-block;">
      <li style="font-size:13px;padding:6px 0;color:rgba(250,250,248,0.8);display:flex;align-items:center;gap:10px;">
        <span style="color:var(--gold);">鉁?/span> Obsidian Vault 瀹屾暣鎼缓 + 鐩綍瑙勮寖
      </li>
      <li style="font-size:13px;padding:6px 0;color:rgba(250,250,248,0.8);display:flex;align-items:center;gap:10px;">
        <span style="color:var(--gold);">鉁?/span> 鍏ㄩ噺鍐呭棣栨 AI 缂栬瘧
      </li>
      <li style="font-size:13px;padding:6px 0;color:rgba(250,250,248,0.8);display:flex;align-items:center;gap:10px;">
        <span style="color:var(--gold);">鉁?/span> 姣忔湀澧為噺缂栬瘧锛堟寔缁?涓湀锛?      </li>
      <li style="font-size:13px;padding:6px 0;color:rgba(250,250,248,0.8);display:flex;align-items:center;gap:10px;">
        <span style="color:var(--gold);">鉁?/span> 鐭涚浘妫€娴?+ 鍋ュ悍妫€鏌?      </li>
      <li style="font-size:13px;padding:6px 0;color:rgba(250,250,248,0.8);display:flex;align-items:center;gap:10px;">
        <span style="color:var(--gold);">鉁?/span> MCP Server + RAG API 閰嶇疆
      </li>
      <li style="font-size:13px;padding:6px 0;color:rgba(250,250,248,0.8);display:flex;align-items:center;gap:10px;">
        <span style="color:var(--gold);">鉁?/span> OpenClaw 鐩磋繛娴嬭瘯
      </li>
    </ul>
    <a href="https://www.zaihang.com/expert/detail?eid=2bhjbfp3t2q" class="btn-primary" style="background:var(--gold);color:var(--ink);">棰勭害鍏ㄩ摼璺挩璇?鈫?/a>
  </div>
</div>

<!-- Agent 鍩虹璁炬柦绾?-->
<div class="agent-section">
  <div class="agent-badge">鈽?宸紓鍖栧鍨?/div>
  <h2 class="section-title">Agent 鍩虹璁炬柦绾?/h2>
  <p style="font-size:14px;color:#888;max-width:520px;margin:0 auto 0;line-height:1.7;">
    浣犵殑鐭ヨ瘑搴撲笉鍙槸缁欎汉鐪嬧€斺€?strong style="color:var(--ink)">Agent 涔熷彲浠ヤ富鍔ㄨ皟鐢ㄥ畠</strong>銆傝繖鏄湡姝ｇ殑鐭ヨ瘑璧勪骇鍖栵細AI绯荤粺鎷ユ湁鎸佺画瀛︿範鐨?浼佷笟澶栬剳"銆?  </p>
  <div class="agent-grid">
    <div class="agent-card">
      <div class="arch-num">Agent Starter</div>
      <h3>缁?Agent 閰嶄竴涓鑴?/h3>
      <div class="price">楼1999<span> / 娆?/span></div>
      <p>閫傚悎 AI 寮€鍙戣€呫€佷釜浜?Agent 鐢ㄦ埛锛氱粰 Agent 涓€涓彲璇诲啓鐨勭煡璇嗗簱锛岃瀹冭秺鐢ㄨ秺鎳備綘鐨勪笟鍔°€?/p>
      <ul class="agent-features">
        <li><span class="check">鉁?/span> Vault 鎼缓 + MCP Server 閰嶇疆</li>
        <li><span class="check">鉁?/span> MEMORY.md 鍗忚鍒濆鍖?/li>
        <li><span class="check">鉁?/span> OpenClaw / Claude 鎺ュ叆娴嬭瘯</li>
        <li><span class="check">鉁?/span> AGENTS.md 瀹氬埗缂栧啓</li>
      </ul>
    </div>
    <div class="agent-card">
      <div class="arch-num">Agent Business</div>
      <h3>浼佷笟 Agent 鐭ヨ瘑涓彴</h3>
      <div class="price">楼4999<span> 璧?/span></div>
      <p>閫傚悎浼佷笟 AI 閮ㄧ讲鍥㈤槦锛氬 Agent 鍏变韩鐭ヨ瘑搴擄紝鏉冮檺鍒嗙骇锛岃嚜鍔ㄧ紪璇戯紝鎸佺画瀛︿範銆?/p>
      <ul class="agent-features">
        <li><span class="check">鉁?/span> Agent Starter 鍏ㄩ儴鍐呭</li>
        <li><span class="check">鉁?/span> 澶?Agent 鍏变韩鐭ヨ瘑搴撴灦鏋?/li>
        <li><span class="check">鉁?/span> 姣忓懆鑷姩缂栬瘧 + 鍋ュ悍妫€鏌?/li>
        <li><span class="check">鉁?/span> 鐭ヨ瘑瀹¤鏃ュ織</li>
        <li><span class="check">鉁?/span> MCP 鍗忚骞村害閫傞厤</li>
      </ul>
    </div>
  </div>
</div>

<!-- 宸ヤ綔娴佺▼ -->
<div class="flow-section">
  <div class="section-label">浜や粯娴佺▼</div>
  <h2 class="section-title">鍥涙瀹屾垚鎼缓</h2>
  <div class="flow-steps">
    <div class="flow-step">
      <div class="flow-num">1</div>
      <div class="flow-content">
        <h4>鍙戦€佹ā鏉垮寘</h4>
        <p>鏀跺埌璁㈠崟鍚庡彂閫?Obsidian Vault 妯℃澘搴撱€佸畨瑁呮寚鍗椼€丄GENTS.md 妯℃澘</p>
      </div>
    </div>
    <div class="flow-step">
      <div class="flow-num">2</div>
      <div class="flow-content">
        <h4>瀵煎叆浣犵殑鍐呭</h4>
        <p>鎶婄幇鏈夋枃绔犮€佺瑪璁般€佺礌鏉愬鍒跺埌瀵瑰簲鐩綍锛屾敮鎸?URL銆丳DF銆丮arkdown銆佸井淇＄瑪璁扮瓑鏍煎紡</p>
      </div>
    </div>
    <div class="flow-step">
      <div class="flow-num">3</div>
      <div class="flow-content">
        <h4>AI 缂栬瘧鐭ヨ瘑搴?/h4>
        <p>OpenClaw 璇诲彇鍐呭 鈫?澧為噺缂栬瘧 鈫?鐢熸垚鍙岄摼 鈫?鏇存柊 MEMORY.md 鈫?鏋勫缓鐭ヨ瘑缃戠粶</p>
      </div>
    </div>
    <div class="flow-step">
      <div class="flow-num">4</div>
      <div class="flow-content">
        <h4>杩炴帴 Agent</h4>
        <p>閰嶇疆 MCP Server / RAG API / OpenClaw 鐩磋繛鈥斺€斾綘鐨?Agent 浠庢鍙互涓诲姩璇诲啓鐭ヨ瘑搴?/p>
      </div>
    </div>
  </div>
</div>

<!-- CTA -->
<div class="service-cta">
  <h2>璁╃煡璇嗙湡姝ｄ负浣犲拰浣犵殑 Agent 宸ヤ綔</h2>
  <p>涓€娆℃惌寤猴紝鎸佺画澧炲€笺€備綘鐨勭Н绱€煎緱琚縺娲烩€斺€斾笉鍙槸缁欎綘鑷繁鐢紝涔熺粰浣犵殑 AI Agent 鐢ㄣ€?/p>
  <div class="cta-buttons">
    <a href="https://www.zaihang.com/expert/detail?eid=2bhjbfp3t2q" class="btn-primary">鍦ㄨ绾﹁鍜ㄨ 鈫?/a>
    <a href="mailto:chenluaihr@gmail.com?subject=鐭ヨ瘑鍩虹璁炬柦鏈嶅姟鍜ㄨ" class="btn-secondary">閭欢鑱旂郴</a>
  </div>
</div>
