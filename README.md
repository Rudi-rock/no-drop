# No-Drop 🎓
### Academic Early-Warning System to Prevent Student Failure

## Overview
No-Drop is an early-warning system designed to identify students at risk of academic failure **before** they fail examinations.

Unlike traditional systems that rely on marks, No-Drop focuses on **behavioral learning signals** such as:
- Study inactivity
- Revision gaps
- Missed academic tasks
- Sudden drops in engagement

The system generates a **risk classification** and enables early, targeted interventions.

---

## Problem Statement
Academic failure is rarely sudden.  
Students typically experience a gradual decline in engagement, consistency, and confidence — which current academic systems fail to detect in time.

Most institutions act **after exam results**, when recovery is no longer possible.

---

## Solution
No-Drop continuously monitors student activity patterns and assigns a dynamic risk score.

Based on this score, students are classified into:
- Safe
- Warning
- Critical

This allows educators to intervene early through academic counseling, workload adjustment, or personalized support.

---

## System Design
**Input**
- Study time logs
- Revision intervals
- Assignment submission data

**Processing**
- Rule-based risk scoring (AI-ready architecture)

**Output**
- Risk category per student
- Actionable intervention triggers

---

## Current Implementation (v1)
- Rule-based risk scoring engine
- CSV-based input simulation
- Python-based logic layer

---

## Tech Stack
- Python
- Pandas
- Modular rule engine

---

## Future Enhancements
- Machine learning–based risk prediction
- LMS integration (Moodle, Google Classroom)
- Real-time dashboards for faculty
- Automated student nudges

---

## Author
Rudra Pratap Singh  
B.Tech CSE — SRM Kattankulathur

## Running the Project
pip install -r requirements.txt
python src/risk_engine.py














<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>NoDrop — Academic Early-Warning System</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<style>
  /* ─── THEME VARIABLES ─── */
  :root {
    --bg: #000;
    --bg-secondary: #111;
    --bg-card: #1a1a1a;
    --bg-card-hover: #222;
    --text: #fff;
    --text-muted: #a1a1aa;
    --text-dim: #636366;
    --border: rgba(255,255,255,0.08);
    --border-hover: rgba(255,255,255,0.18);
    --accent: #fff;
    --cta-bg: #fff;
    --cta-text: #000;
    --btn-ghost-border: rgba(255,255,255,0.25);
    --btn-ghost-text: #fff;
    --logo-bg: #fff;
    --logo-text: #000;
    --num-color: rgba(255,255,255,0.07);
    --cta-section-bg: #fff;
    --cta-section-text: #000;
    --cta-section-muted: #71717a;
    --cta-btn-bg: #000;
    --cta-btn-text: #fff;
    --icon-bg: rgba(255,255,255,0.08);
  }

  [data-theme="light"] {
    --bg: #fff;
    --bg-secondary: #f4f4f5;
    --bg-card: #f4f4f5;
    --bg-card-hover: #e4e4e7;
    --text: #000;
    --text-muted: #52525b;
    --text-dim: #a1a1aa;
    --border: rgba(0,0,0,0.08);
    --border-hover: rgba(0,0,0,0.18);
    --accent: #000;
    --cta-bg: #000;
    --cta-text: #fff;
    --btn-ghost-border: rgba(0,0,0,0.2);
    --btn-ghost-text: #000;
    --logo-bg: #000;
    --logo-text: #fff;
    --num-color: rgba(0,0,0,0.06);
    --cta-section-bg: #111;
    --cta-section-text: #fff;
    --cta-section-muted: #a1a1aa;
    --cta-btn-bg: #fff;
    --cta-btn-text: #000;
    --icon-bg: rgba(0,0,0,0.06);
  }

  * { margin:0; padding:0; box-sizing:border-box; }
  html { scroll-behavior:smooth; }
  body {
    font-family: 'Inter', sans-serif;
    background: var(--bg);
    color: var(--text);
    transition: background .35s, color .35s;
    -webkit-font-smoothing: antialiased;
    overflow-x: hidden;
  }

  /* ─── NAV ─── */
  nav {
    position:fixed; top:0; left:0; right:0; z-index:100;
    display:flex; align-items:center; justify-content:space-between;
    padding:0 40px; height:64px;
    background: var(--bg);
    border-bottom: 1px solid var(--border);
    transition: background .35s, border-color .35s;
  }
  .nav-left { display:flex; align-items:center; gap:10px; }
  .nav-logo-box {
    width:32px; height:32px; border-radius:8px;
    background: var(--logo-bg); color: var(--logo-text);
    display:flex; align-items:center; justify-content:center;
    font-weight:800; font-size:16px; transition: background .35s, color .35s;
  }
  .nav-brand { font-weight:600; font-size:17px; color:var(--text); transition:color .35s; }
  .nav-center { display:flex; gap:28px; }
  .nav-center a {
    color: var(--text-muted); text-decoration:none; font-size:14px; font-weight:500;
    transition: color .25s;
  }
  .nav-center a:hover { color: var(--text); }
  .nav-right { display:flex; align-items:center; gap:20px; }
  .theme-toggle {
    background:none; border:none; cursor:pointer;
    color: var(--text-muted); font-size:18px; padding:4px;
    transition: color .25s;
  }
  .theme-toggle:hover { color: var(--text); }
  .nav-signin { color: var(--text-muted); font-size:14px; font-weight:500; text-decoration:none; transition:color .25s; }
  .nav-signin:hover { color: var(--text); }
  .btn-get-started {
    background: var(--cta-bg); color: var(--cta-text);
    border:none; padding:8px 20px; border-radius:8px;
    font-size:14px; font-weight:600; cursor:pointer;
    transition: background .35s, color .35s, opacity .2s;
  }
  .btn-get-started:hover { opacity:.8; }

  /* ─── HERO ─── */
  .hero {
    padding: 140px 40px 100px;
    max-width:1200px; margin:0 auto;
    display:grid; grid-template-columns: 1fr 1fr; gap:40px; align-items:center;
  }
  .hero-left { }
  .hero h1 {
    font-size: clamp(48px,6.5vw,80px);
    font-weight:900; line-height:1.03; letter-spacing:-3px;
    color: var(--text); transition:color .35s;
  }
  .hero-sub {
    margin-top:28px; color:var(--text-muted); font-size:17px; line-height:1.65; max-width:460px;
    transition:color .35s;
  }
  .hero-btns { display:flex; gap:12px; margin-top:36px; }
  .btn-primary {
    display:inline-flex; align-items:center; gap:8px;
    background: var(--cta-bg); color: var(--cta-text);
    border:none; padding:11px 24px; border-radius:8px;
    font-size:15px; font-weight:600; cursor:pointer;
    transition: background .35s, color .35s, opacity .2s;
    text-decoration:none;
  }
  .btn-primary:hover { opacity:.8; }
  .btn-primary .arrow { font-size:16px; transition:transform .2s; }
  .btn-primary:hover .arrow { transform:translateX(3px); }
  .btn-outline {
    display:inline-flex; align-items:center;
    background:transparent; color: var(--btn-ghost-text);
    border:1px solid var(--btn-ghost-border); padding:11px 24px; border-radius:8px;
    font-size:15px; font-weight:500; cursor:pointer; text-decoration:none;
    transition: border-color .25s, color .35s;
  }
  .btn-outline:hover { border-color: var(--border-hover); }

  /* Hero right — trust pills */
  .hero-right {
    display:flex; flex-direction:column; align-items:flex-start; gap:0;
    padding-left:20px;
  }
  .trust-strip {
    text-align:center; color:var(--text-dim); font-size:13px; font-weight:500;
    margin-bottom:24px; width:100%; letter-spacing:0.3px; transition:color .35s;
  }
  .trust-grid {
    display:grid; grid-template-columns:1fr 1fr; gap:16px; width:100%;
  }
  .trust-card {
    background:var(--bg-card); border:1px solid var(--border);
    border-radius:16px; padding:24px 20px;
    text-align:center; transition: background .35s, border-color .3s, transform .2s;
  }
  .trust-card:hover { border-color: var(--border-hover); transform:translateY(-2px); }
  .trust-icon { font-size:24px; margin-bottom:10px; }
  .trust-card h4 { font-size:14px; font-weight:600; color:var(--text); margin-bottom:5px; transition:color .35s; }
  .trust-card p { font-size:12px; color:var(--text-dim); line-height:1.5; transition:color .35s; }

  /* ─── DIVIDER ─── */
  .divider { border:none; border-top:1px solid var(--border); max-width:1200px; margin:0 auto; transition:border-color .35s; }

  /* ─── SECTION SHARED ─── */
  .section { padding:100px 40px; max-width:1200px; margin:0 auto; }
  .section-label { font-size:13px; font-weight:500; color:var(--text-dim); margin-bottom:12px; transition:color .35s; }
  .section-title {
    font-size:clamp(28px,3.5vw,40px); font-weight:800; line-height:1.15;
    letter-spacing:-1.2px; color:var(--text); max-width:520px; transition:color .35s;
  }
  .section-desc {
    color:var(--text-muted); font-size:15px; line-height:1.7; max-width:480px; margin-top:14px; transition:color .35s;
  }

  /* ─── FEATURES (6 grid) ─── */
  .features-grid {
    display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin-top:48px;
  }
  .feat-card {
    background:var(--bg-card); border:1px solid var(--border);
    border-radius:16px; padding:32px 28px;
    transition: background .35s, border-color .3s, transform .2s;
  }
  .feat-card:hover { border-color:var(--border-hover); transform:translateY(-2px); }
  .feat-icon-wrap {
    width:40px; height:40px; border-radius:10px;
    background: var(--icon-bg); display:flex; align-items:center; justify-content:center;
    font-size:19px; margin-bottom:20px; transition:background .35s;
  }
  .feat-card h3 { font-size:16px; font-weight:600; color:var(--text); margin-bottom:8px; transition:color .35s; }
  .feat-card p { font-size:13px; color:var(--text-muted); line-height:1.6; transition:color .35s; }

  /* ─── HOW IT WORKS (4 col) ─── */
  .how-grid {
    display:grid; grid-template-columns:repeat(4,1fr); gap:32px; margin-top:56px;
  }
  .how-item { position:relative; }
  .how-num {
    font-size:72px; font-weight:900; line-height:1; color:var(--num-color);
    letter-spacing:-2px; margin-bottom:12px; transition:color .35s;
  }
  .how-item h3 { font-size:16px; font-weight:600; color:var(--text); margin-bottom:10px; transition:color .35s; }
  .how-item p { font-size:13px; color:var(--text-muted); line-height:1.65; transition:color .35s; }

  /* ─── WHAT NODROP DOES (4 cards) ─── */
  .what-section {
    padding:100px 40px;
    background: var(--bg-secondary);
    transition: background .35s;
  }
  .what-inner { max-width:1200px; margin:0 auto; }
  .what-header { text-align:center; margin-bottom:48px; }
  .what-header h2 {
    font-size:clamp(30px,4vw,44px); font-weight:800; letter-spacing:-1.5px;
    color:var(--text); transition:color .35s;
  }
  .what-header p { color:var(--text-muted); font-size:15px; margin-top:10px; transition:color .35s; }
  .what-grid {
    display:grid; grid-template-columns:repeat(4,1fr); gap:16px;
  }
  .what-card {
    background:var(--bg-card); border:1px solid var(--border);
    border-radius:16px; padding:32px 24px;
    transition: background .35s, border-color .3s, transform .2s;
  }
  .what-card:hover { border-color:var(--border-hover); transform:translateY(-2px); }
  .what-icon { font-size:28px; margin-bottom:18px; display:block; }
  .what-card h3 { font-size:15px; font-weight:600; color:var(--text); margin-bottom:8px; transition:color .35s; }
  .what-card p { font-size:12.5px; color:var(--text-muted); line-height:1.6; transition:color .35s; }

  /* ─── CTA BANNER ─── */
  .cta-section {
    padding:80px 40px;
  }
  .cta-banner {
    max-width:1200px; margin:0 auto;
    background: var(--cta-section-bg);
    border-radius:24px; padding:72px 64px;
    transition: background .35s;
  }
  .cta-banner h2 {
    font-size:clamp(26px,3.5vw,38px); font-weight:800;
    letter-spacing:-1px; color:var(--cta-section-text);
    max-width:480px; line-height:1.2; transition:color .35s;
  }
  .cta-banner p {
    color:var(--cta-section-muted); font-size:15px; margin-top:16px;
    max-width:500px; line-height:1.65; transition:color .35s;
  }
  .cta-btns { display:flex; gap:16px; margin-top:32px; align-items:center; }
  .cta-btn-primary {
    display:inline-flex; align-items:center; gap:8px;
    background: var(--cta-btn-bg); color: var(--cta-btn-text);
    border:none; padding:12px 26px; border-radius:8px;
    font-size:15px; font-weight:600; cursor:pointer; text-decoration:none;
    transition: background .35s, color .35s, opacity .2s;
  }
  .cta-btn-primary:hover { opacity:.8; }
  .cta-btn-primary .arrow { transition:transform .2s; }
  .cta-btn-primary:hover .arrow { transform:translateX(3px); }
  .cta-btn-signin {
    color:var(--cta-section-muted); font-size:15px; font-weight:500;
    text-decoration:none; transition:color .25s;
  }
  .cta-btn-signin:hover { color:var(--cta-section-text); }

  /* ─── FOOTER ─── */
  footer {
    padding:40px; border-top:1px solid var(--border);
    transition:border-color .35s;
  }
  .footer-inner {
    max-width:1200px; margin:0 auto;
    display:flex; justify-content:space-between; align-items:center;
  }
  .footer-left { display:flex; align-items:center; gap:10px; }
  .footer-logo-box {
    width:28px; height:28px; border-radius:7px;
    background:var(--logo-bg); color:var(--logo-text);
    display:flex; align-items:center; justify-content:center;
    font-weight:800; font-size:14px; transition:background .35s, color .35s;
  }
  .footer-brand { font-weight:600; font-size:15px; color:var(--text); transition:color .35s; }
  .footer-right { font-size:13px; color:var(--text-dim); transition:color .35s; }

  /* ─── RESPONSIVE ─── */
  @media(max-width:900px){
    .hero { grid-template-columns:1fr; }
    .hero-right { padding-left:0; margin-top:40px; }
    .features-grid { grid-template-columns:repeat(2,1fr); }
    .how-grid { grid-template-columns:repeat(2,1fr); gap:40px; }
    .what-grid { grid-template-columns:repeat(2,1fr); }
  }
  @media(max-width:600px){
    nav { padding:0 20px; }
    .nav-center { display:none; }
    .hero { padding:110px 20px 70px; }
    .section { padding:70px 20px; }
    .features-grid { grid-template-columns:1fr; }
    .how-grid { grid-template-columns:1fr; gap:32px; }
    .what-section { padding:70px 20px; }
    .what-grid { grid-template-columns:1fr; }
    .cta-banner { padding:48px 28px; }
    .trust-grid { grid-template-columns:1fr 1fr; }
  }
</style>
</head>
<body>

<!-- NAV -->
<nav>
  <div class="nav-left">
    <div class="nav-logo-box">N</div>
    <span class="nav-brand">NoDrop</span>
  </div>
  <div class="nav-center">
    <a href="#features">Features</a>
    <a href="#how">How It Works</a>
    <a href="#impact">Impact</a>
  </div>
  <div class="nav-right">
    <button class="theme-toggle" onclick="toggleTheme()" id="themeIcon">☀️</button>
    <a href="#" class="nav-signin">Sign in</a>
    <button class="btn-get-started">Get Started</button>
  </div>
</nav>

<!-- HERO -->
<section class="hero">
  <div class="hero-left">
    <h1>Stop students<br>from falling<br>behind.</h1>
    <p class="hero-sub">NoDrop uses AI to detect learning decay before it becomes failure. Identify at-risk students early and intervene with precision.</p>
    <div class="hero-btns">
      <a href="#" class="btn-primary">Get started <span class="arrow">→</span></a>
      <a href="#how" class="btn-outline">See how it works</a>
    </div>
  </div>
  <div class="hero-right">
    <p class="trust-strip">Built on spaced repetition and learning science principles</p>
    <div class="trust-grid">
      <div class="trust-card">
        <div class="trust-icon">🧠</div>
        <h4>AI-Powered</h4>
        <p>Detects learning decay before it becomes failure</p>
      </div>
      <div class="trust-card">
        <div class="trust-icon">🕐</div>
        <h4>Real-Time</h4>
        <p>Monitors student progress continuously</p>
      </div>
      <div class="trust-card">
        <div class="trust-icon">🎯</div>
        <h4>Targeted</h4>
        <p>Suggests specific interventions for each student</p>
      </div>
      <div class="trust-card">
        <div class="trust-icon">♥️</div>
        <h4>Free Forever</h4>
        <p>No cost for educators or students</p>
      </div>
    </div>
  </div>
</section>

<hr class="divider"/>

<!-- FEATURES -->
<section class="section" id="features">
  <div class="section-label">Features</div>
  <h2 class="section-title">Everything you need to prevent academic failure</h2>
  <p class="section-desc">Comprehensive tools for educators and students to stay ahead of learning challenges.</p>

  <div class="features-grid">
    <div class="feat-card">
      <div class="feat-icon-wrap">🧠</div>
      <h3>AI-Powered Detection</h3>
      <p>Machine learning algorithms analyze student behavior patterns to identify early signs of learning decay.</p>
    </div>
    <div class="feat-card">
      <div class="feat-icon-wrap">📊</div>
      <h3>Risk Heatmaps</h3>
      <p>Visual dashboards show at-a-glance which students need attention, organized by risk level.</p>
    </div>
    <div class="feat-card">
      <div class="feat-icon-wrap">🔔</div>
      <h3>Smart Alerts</h3>
      <p>Automated notifications when students show declining engagement or performance trends.</p>
    </div>
    <div class="feat-card">
      <div class="feat-icon-wrap">🎓</div>
      <h3>Questions-First Learning</h3>
      <p>Students engage with adaptive questions that reinforce concepts before they're forgotten.</p>
    </div>
    <div class="feat-card">
      <div class="feat-icon-wrap">⚡</div>
      <h3>Real-time Insights</h3>
      <p>Track learning progress as it happens with instant analytics and reporting.</p>
    </div>
    <div class="feat-card">
      <div class="feat-icon-wrap">🛡️</div>
      <h3>Privacy First</h3>
      <p>FERPA compliant with end-to-end encryption. Student data is always protected.</p>
    </div>
  </div>
</section>

<hr class="divider"/>

<!-- HOW IT WORKS -->
<section class="section" id="how">
  <div class="section-label">How it works</div>
  <h2 class="section-title">From integration to intervention in four steps</h2>

  <div class="how-grid">
    <div class="how-item">
      <div class="how-num">01</div>
      <h3>Connect your LMS</h3>
      <p>Integrate with Canvas, Blackboard, Moodle, or any major learning management system in minutes.</p>
    </div>
    <div class="how-item">
      <div class="how-num">02</div>
      <h3>AI analyzes patterns</h3>
      <p>Our algorithms track engagement, performance trends, and behavioral signals across all students.</p>
    </div>
    <div class="how-item">
      <div class="how-num">03</div>
      <h3>Get actionable insights</h3>
      <p>Receive risk scores, heatmaps, and specific recommendations for each at-risk student.</p>
    </div>
    <div class="how-item">
      <div class="how-num">04</div>
      <h3>Intervene early</h3>
      <p>Reach out to struggling students before they fall too far behind with targeted support.</p>
    </div>
  </div>
</section>

<!-- WHAT NODROP DOES -->
<section class="what-section" id="impact">
  <div class="what-inner">
    <div class="what-header">
      <h2>What NoDrop Does</h2>
      <p>Built to catch students before they fall. Prevention over cure.</p>
    </div>
    <div class="what-grid">
      <div class="what-card">
        <span class="what-icon">🧠</span>
        <h3>AI-Powered Detection</h3>
        <p>Identifies learning decay patterns before they become failures</p>
      </div>
      <div class="what-card">
        <span class="what-icon">🕐</span>
        <h3>Early Warning System</h3>
        <p>Alerts teachers when students show signs of struggle</p>
      </div>
      <div class="what-card">
        <span class="what-icon">🎯</span>
        <h3>Targeted Interventions</h3>
        <p>Suggests specific actions to help each at-risk student</p>
      </div>
      <div class="what-card">
        <span class="what-icon">🎓</span>
        <h3>Free for Schools</h3>
        <p>Prevention should be accessible to every student</p>
      </div>
    </div>
  </div>
</section>

<!-- CTA BANNER -->
<section class="cta-section">
  <div class="cta-banner">
    <h2>Ready to help every student succeed?</h2>
    <p>Join hundreds of institutions already using NoDrop to prevent academic failure and improve student outcomes.</p>
    <div class="cta-btns">
      <a href="#" class="cta-btn-primary">Start free trial <span class="arrow">→</span></a>
      <a href="#" class="cta-btn-signin">Sign in</a>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-inner">
    <div class="footer-left">
      <div class="footer-logo-box">N</div>
      <span class="footer-brand">NoDrop</span>
    </div>
    <div class="footer-right">© 2025 NoDrop. All rights reserved.</div>
  </div>
</footer>

<!-- JS -->
<script>
  // Dark mode default
  document.body.setAttribute('data-theme','dark');

  function toggleTheme(){
    const current = document.body.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.body.setAttribute('data-theme', next);
    document.getElementById('themeIcon').textContent = next === 'dark' ? '☀️' : '🌙';
  }
</script>
</body>
</html>



