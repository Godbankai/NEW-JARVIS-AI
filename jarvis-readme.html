<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>JARVIS AI – Intelligent Virtual Assistant</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #050a12;
    --bg2: #070d1a;
    --panel: #0a1628;
    --border: #0d3a6b;
    --accent: #00d4ff;
    --accent2: #0084ff;
    --accent3: #00ff88;
    --text: #c8e4ff;
    --muted: #4a7aa0;
    --red: #ff4444;
    --gold: #ffd700;
  }

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  html { scroll-behavior: smooth; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Inter', sans-serif;
    font-size: 15px;
    line-height: 1.7;
    overflow-x: hidden;
  }

  /* ─── SCANLINE OVERLAY ─── */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background: repeating-linear-gradient(
      0deg,
      transparent,
      transparent 2px,
      rgba(0,212,255,0.015) 2px,
      rgba(0,212,255,0.015) 4px
    );
    pointer-events: none;
    z-index: 9999;
  }

  /* ─── GRID BG ─── */
  .grid-bg {
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(0,132,255,0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,132,255,0.04) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
  }

  /* ─── HERO ─── */
  .hero {
    position: relative;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 60px 20px;
    z-index: 1;
    overflow: hidden;
  }

  .hero::before {
    content: '';
    position: absolute;
    width: 600px; height: 600px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(0,132,255,0.12) 0%, transparent 70%);
    top: 50%; left: 50%;
    transform: translate(-50%,-50%);
    animation: pulse-glow 4s ease-in-out infinite;
  }

  @keyframes pulse-glow {
    0%,100% { transform: translate(-50%,-50%) scale(1); opacity: 0.6; }
    50% { transform: translate(-50%,-50%) scale(1.15); opacity: 1; }
  }

  /* Arc Reactor */
  .arc-reactor {
    position: relative;
    width: 140px; height: 140px;
    margin-bottom: 40px;
    animation: float 3s ease-in-out infinite;
  }

  @keyframes float {
    0%,100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
  }

  .arc-reactor svg { width: 100%; height: 100%; filter: drop-shadow(0 0 20px rgba(0,212,255,0.8)); }

  .arc-ring {
    animation: spin-ring 8s linear infinite;
    transform-origin: 70px 70px;
  }
  .arc-ring-2 {
    animation: spin-ring 5s linear infinite reverse;
    transform-origin: 70px 70px;
  }

  @keyframes spin-ring {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
  }

  .arc-core {
    animation: core-pulse 2s ease-in-out infinite;
  }

  @keyframes core-pulse {
    0%,100% { opacity: 0.8; }
    50% { opacity: 1; filter: brightness(1.5); }
  }

  .hero-eyebrow {
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
    letter-spacing: 4px;
    color: var(--accent3);
    text-transform: uppercase;
    margin-bottom: 12px;
    opacity: 0;
    animation: fade-up 0.8s ease forwards 0.3s;
  }

  .hero h1 {
    font-family: 'Orbitron', monospace;
    font-size: clamp(42px, 9vw, 88px);
    font-weight: 900;
    letter-spacing: -2px;
    line-height: 0.95;
    background: linear-gradient(135deg, #fff 0%, var(--accent) 40%, var(--accent2) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 8px;
    opacity: 0;
    animation: fade-up 0.8s ease forwards 0.5s;
  }

  .hero h1 span {
    display: block;
    font-size: 0.42em;
    letter-spacing: 8px;
    font-weight: 400;
    background: linear-gradient(90deg, var(--accent), var(--accent3));
    -webkit-background-clip: text;
    background-clip: text;
    margin-top: 4px;
  }

  .hero-sub {
    font-size: 16px;
    color: var(--muted);
    max-width: 560px;
    margin: 24px auto 40px;
    opacity: 0;
    animation: fade-up 0.8s ease forwards 0.7s;
  }

  .hero-badges {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    justify-content: center;
    margin-bottom: 48px;
    opacity: 0;
    animation: fade-up 0.8s ease forwards 0.9s;
  }

  .badge {
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
    padding: 5px 12px;
    border-radius: 20px;
    border: 1px solid;
    text-transform: uppercase;
    letter-spacing: 1px;
  }
  .badge-blue { border-color: var(--accent2); color: var(--accent2); background: rgba(0,132,255,0.1); }
  .badge-cyan { border-color: var(--accent); color: var(--accent); background: rgba(0,212,255,0.1); }
  .badge-green { border-color: var(--accent3); color: var(--accent3); background: rgba(0,255,136,0.1); }

  .status-bar {
    display: flex;
    gap: 24px;
    justify-content: center;
    opacity: 0;
    animation: fade-up 0.8s ease forwards 1.1s;
  }

  .status-item {
    display: flex;
    align-items: center;
    gap: 8px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 12px;
    color: var(--muted);
  }

  .status-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: var(--accent3);
    box-shadow: 0 0 8px var(--accent3);
    animation: blink 2s ease-in-out infinite;
  }
  .status-dot.red { background: var(--red); box-shadow: 0 0 8px var(--red); }
  .status-dot.blue { background: var(--accent); box-shadow: 0 0 8px var(--accent); animation-delay: 0.5s; }

  @keyframes blink {
    0%,100% { opacity: 1; }
    50% { opacity: 0.3; }
  }

  @keyframes fade-up {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }

  /* ─── SCROLL INDICATOR ─── */
  .scroll-hint {
    position: absolute;
    bottom: 32px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
    opacity: 0;
    animation: fade-up 0.8s ease forwards 1.4s;
  }
  .scroll-hint span {
    font-family: 'Share Tech Mono', monospace;
    font-size: 10px;
    color: var(--muted);
    letter-spacing: 2px;
  }
  .scroll-arrow {
    width: 20px; height: 20px;
    border-right: 2px solid var(--accent);
    border-bottom: 2px solid var(--accent);
    transform: rotate(45deg);
    animation: bounce 1.5s ease-in-out infinite;
  }
  @keyframes bounce {
    0%,100% { transform: rotate(45deg) translateY(0); }
    50% { transform: rotate(45deg) translateY(4px); }
  }

  /* ─── SECTION WRAPPER ─── */
  .section { position: relative; z-index: 1; padding: 80px 20px; max-width: 1100px; margin: 0 auto; }

  .section-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 10px;
    letter-spacing: 4px;
    color: var(--accent);
    text-transform: uppercase;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, var(--border), transparent);
  }

  .section-title {
    font-family: 'Orbitron', monospace;
    font-size: clamp(24px, 4vw, 38px);
    font-weight: 700;
    color: #fff;
    margin-bottom: 48px;
  }

  /* ─── FEATURES GRID ─── */
  .features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 16px;
  }

  .feat-card {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 24px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.3s, transform 0.3s;
    opacity: 0;
    transform: translateY(20px);
  }

  .feat-card.visible {
    animation: card-in 0.5s ease forwards;
  }

  @keyframes card-in {
    to { opacity: 1; transform: translateY(0); }
  }

  .feat-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--accent2), var(--accent));
    transform: scaleX(0);
    transition: transform 0.3s;
    transform-origin: left;
  }

  .feat-card:hover {
    border-color: var(--accent);
    transform: translateY(-4px);
  }
  .feat-card:hover::before { transform: scaleX(1); }

  .feat-icon {
    font-size: 28px;
    margin-bottom: 12px;
  }

  .feat-card h3 {
    font-family: 'Orbitron', monospace;
    font-size: 13px;
    font-weight: 700;
    color: var(--accent);
    margin-bottom: 10px;
    letter-spacing: 1px;
  }

  .feat-card p {
    font-size: 13px;
    color: var(--muted);
    line-height: 1.6;
  }

  .feat-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 14px;
  }

  .feat-tag {
    font-family: 'Share Tech Mono', monospace;
    font-size: 10px;
    padding: 3px 8px;
    border: 1px solid rgba(0,212,255,0.2);
    border-radius: 4px;
    color: var(--accent);
    background: rgba(0,212,255,0.05);
  }

  /* ─── TECH STACK ─── */
  .tech-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 12px;
  }

  .tech-item {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 16px 20px;
    display: flex;
    align-items: center;
    gap: 14px;
    transition: border-color 0.3s, background 0.3s;
    opacity: 0;
    animation: none;
  }
  .tech-item.visible {
    animation: card-in 0.4s ease forwards;
  }

  .tech-item:hover {
    border-color: var(--accent2);
    background: rgba(0,132,255,0.08);
  }

  .tech-icon {
    width: 36px; height: 36px;
    border-radius: 8px;
    background: rgba(0,212,255,0.1);
    border: 1px solid rgba(0,212,255,0.2);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    flex-shrink: 0;
  }

  .tech-info { min-width: 0; }
  .tech-name {
    font-family: 'Share Tech Mono', monospace;
    font-size: 13px;
    color: #fff;
    font-weight: 600;
  }
  .tech-purpose {
    font-size: 11px;
    color: var(--muted);
    margin-top: 2px;
  }

  /* ─── WORKFLOW DIAGRAM ─── */
  .workflow {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 48px 32px;
    position: relative;
    overflow: hidden;
  }

  .workflow::before {
    content: '';
    position: absolute;
    inset: -1px;
    border-radius: 16px;
    background: linear-gradient(135deg, rgba(0,212,255,0.2), transparent 50%, rgba(0,255,136,0.1));
    pointer-events: none;
  }

  .flow-steps {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0;
    position: relative;
  }

  .flow-step {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 10px;
    opacity: 0;
  }

  .flow-step.visible {
    animation: flow-in 0.5s ease forwards;
  }

  @keyframes flow-in {
    from { opacity: 0; transform: scale(0.8); }
    to { opacity: 1; transform: scale(1); }
  }

  .flow-node {
    width: 70px; height: 70px;
    border-radius: 50%;
    border: 2px solid var(--accent);
    background: rgba(0,212,255,0.08);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 26px;
    position: relative;
    box-shadow: 0 0 20px rgba(0,212,255,0.2);
    transition: box-shadow 0.3s;
  }

  .flow-step:hover .flow-node {
    box-shadow: 0 0 30px rgba(0,212,255,0.5);
    background: rgba(0,212,255,0.15);
  }

  .flow-node .node-ring {
    position: absolute;
    inset: -8px;
    border-radius: 50%;
    border: 1px solid rgba(0,212,255,0.2);
    animation: spin-ring 6s linear infinite;
  }

  .flow-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 10px;
    color: var(--muted);
    letter-spacing: 1px;
    max-width: 80px;
    text-align: center;
    line-height: 1.4;
  }

  .flow-arrow {
    width: 40px; height: 2px;
    background: linear-gradient(90deg, var(--accent), var(--accent2));
    position: relative;
    margin-bottom: 30px;
    flex-shrink: 0;
  }
  .flow-arrow::after {
    content: '';
    position: absolute;
    right: -1px; top: -4px;
    border: 5px solid transparent;
    border-left-color: var(--accent2);
  }

  .flow-arrow.animated::before {
    content: '';
    position: absolute;
    top: -2px; left: 0;
    width: 6px; height: 6px;
    border-radius: 50%;
    background: var(--accent);
    animation: data-flow 1.5s linear infinite;
  }

  @keyframes data-flow {
    from { left: 0; opacity: 1; }
    to { left: calc(100% - 6px); opacity: 0.3; }
  }

  /* ─── ARCHITECTURE ─── */
  .arch-diagram {
    font-family: 'Share Tech Mono', monospace;
    font-size: 13px;
    line-height: 1.8;
    background: rgba(0,0,0,0.4);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 32px;
    color: var(--accent);
    overflow-x: auto;
    white-space: pre;
  }

  .arch-diagram .highlight { color: var(--accent3); }
  .arch-diagram .dim { color: var(--muted); }

  /* ─── OBJECTIVES ─── */
  .objectives-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 14px;
  }

  .obj-item {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 18px;
    transition: border-color 0.3s;
    opacity: 0;
  }
  .obj-item.visible { animation: card-in 0.4s ease forwards; }
  .obj-item:hover { border-color: var(--accent3); }

  .obj-num {
    font-family: 'Orbitron', monospace;
    font-size: 11px;
    color: var(--accent3);
    background: rgba(0,255,136,0.08);
    border: 1px solid rgba(0,255,136,0.2);
    border-radius: 6px;
    padding: 4px 8px;
    flex-shrink: 0;
  }

  .obj-text {
    font-size: 13px;
    color: var(--text);
    line-height: 1.5;
  }

  /* ─── FUTURE ─── */
  .future-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 12px;
  }

  .future-item {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px 18px;
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 13px;
    color: var(--text);
    transition: border-color 0.3s, background 0.3s;
    opacity: 0;
    cursor: default;
  }
  .future-item.visible { animation: card-in 0.4s ease forwards; }
  .future-item:hover {
    border-color: var(--accent2);
    background: rgba(0,132,255,0.06);
  }
  .future-item span:first-child { font-size: 20px; }

  /* ─── DEVELOPER CARD ─── */
  .dev-section { text-align: center; padding: 80px 20px 100px; position: relative; z-index: 1; }

  .dev-card {
    display: inline-flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 48px;
    max-width: 480px;
    position: relative;
    overflow: hidden;
  }

  .dev-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 50% 0%, rgba(0,212,255,0.08), transparent 60%);
    pointer-events: none;
  }

  .dev-avatar {
    width: 90px; height: 90px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--accent2), var(--accent));
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Orbitron', monospace;
    font-size: 32px;
    font-weight: 900;
    color: #fff;
    box-shadow: 0 0 30px rgba(0,132,255,0.4);
  }

  .dev-name {
    font-family: 'Orbitron', monospace;
    font-size: 22px;
    font-weight: 700;
    color: #fff;
  }

  .dev-title {
    font-family: 'Share Tech Mono', monospace;
    font-size: 12px;
    color: var(--accent);
    letter-spacing: 2px;
    text-transform: uppercase;
  }

  .dev-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    justify-content: center;
  }

  .dev-tag {
    font-size: 12px;
    padding: 5px 12px;
    border-radius: 20px;
    border: 1px solid rgba(0,212,255,0.25);
    color: var(--muted);
    background: rgba(0,212,255,0.05);
  }

  .dev-uni {
    font-size: 13px;
    color: var(--muted);
  }
  .dev-uni strong { color: var(--accent3); }

  .star-cta {
    margin-top: 8px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 13px;
    color: var(--gold);
    border: 1px solid rgba(255,215,0,0.3);
    border-radius: 8px;
    padding: 10px 20px;
    background: rgba(255,215,0,0.05);
    display: flex;
    align-items: center;
    gap: 8px;
    transition: background 0.3s, box-shadow 0.3s;
  }
  .star-cta:hover {
    background: rgba(255,215,0,0.1);
    box-shadow: 0 0 20px rgba(255,215,0,0.2);
  }

  /* ─── DIVIDER ─── */
  .divider {
    position: relative;
    z-index: 1;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--border), transparent);
    margin: 0 40px;
  }

  /* ─── TERMINAL TYPING ─── */
  .terminal {
    background: #020913;
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 24px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 13px;
    margin-top: 40px;
    overflow: hidden;
  }

  .terminal-bar {
    display: flex;
    gap: 6px;
    margin-bottom: 16px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--border);
  }

  .t-dot { width: 12px; height: 12px; border-radius: 50%; }
  .t-dot:nth-child(1) { background: #ff5f57; }
  .t-dot:nth-child(2) { background: #febc2e; }
  .t-dot:nth-child(3) { background: #28c840; }
  .t-title { margin-left: auto; color: var(--muted); font-size: 11px; }

  .t-line { margin-bottom: 6px; }
  .t-prompt { color: var(--accent3); }
  .t-cmd { color: #fff; }
  .t-out { color: var(--muted); padding-left: 16px; }
  .t-out.success { color: var(--accent3); }
  .t-out.info { color: var(--accent); }

  .typing-cursor {
    display: inline-block;
    width: 8px; height: 14px;
    background: var(--accent);
    animation: cursor-blink 1s step-end infinite;
    vertical-align: text-bottom;
    margin-left: 2px;
  }

  @keyframes cursor-blink {
    0%,100% { opacity: 1; }
    50% { opacity: 0; }
  }

  /* ─── RESPONSIVE ─── */
  @media (max-width: 640px) {
    .flow-arrow { width: 20px; }
    .flow-node { width: 54px; height: 54px; font-size: 20px; }
    .dev-card { padding: 32px 24px; }
  }

  /* ─── INTERSECTION OBSERVER CLASSES ─── */
  .animate-on-scroll { opacity: 0; transform: translateY(20px); transition: opacity 0.5s ease, transform 0.5s ease; }
  .animate-on-scroll.in-view { opacity: 1; transform: translateY(0); }

</style>
</head>
<body>

<div class="grid-bg"></div>

<!-- ══════════ HERO ══════════ -->
<section class="hero">
  <!-- Arc Reactor -->
  <div class="arc-reactor">
    <svg viewBox="0 0 140 140" fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="glow" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#00d4ff" stop-opacity="0.4"/>
          <stop offset="100%" stop-color="#0084ff" stop-opacity="0"/>
        </radialGradient>
      </defs>
      <!-- Outer glow -->
      <circle cx="70" cy="70" r="68" fill="url(#glow)"/>
      <!-- Rings -->
      <g class="arc-ring">
        <circle cx="70" cy="70" r="62" stroke="#0d3a6b" stroke-width="1"/>
        <circle cx="70" cy="8" r="5" fill="#00d4ff" opacity="0.8"/>
        <circle cx="70" cy="132" r="5" fill="#00d4ff" opacity="0.8"/>
        <circle cx="8" cy="70" r="5" fill="#00d4ff" opacity="0.8"/>
        <circle cx="132" cy="70" r="5" fill="#00d4ff" opacity="0.8"/>
      </g>
      <g class="arc-ring-2">
        <circle cx="70" cy="70" r="48" stroke="rgba(0,132,255,0.4)" stroke-width="1.5" stroke-dasharray="8 4"/>
      </g>
      <!-- Middle ring -->
      <circle cx="70" cy="70" r="35" stroke="rgba(0,212,255,0.3)" stroke-width="1.5"/>
      <!-- Hex lines -->
      <line x1="70" y1="35" x2="70" y2="55" stroke="#00d4ff" stroke-width="1.5" opacity="0.6"/>
      <line x1="70" y1="85" x2="70" y2="105" stroke="#00d4ff" stroke-width="1.5" opacity="0.6"/>
      <line x1="35" y1="70" x2="55" y2="70" stroke="#00d4ff" stroke-width="1.5" opacity="0.6"/>
      <line x1="85" y1="70" x2="105" y2="70" stroke="#00d4ff" stroke-width="1.5" opacity="0.6"/>
      <line x1="44.5" y1="44.5" x2="58" y2="58" stroke="#00d4ff" stroke-width="1" opacity="0.4"/>
      <line x1="82" y1="82" x2="95.5" y2="95.5" stroke="#00d4ff" stroke-width="1" opacity="0.4"/>
      <!-- Core -->
      <g class="arc-core">
        <circle cx="70" cy="70" r="20" fill="rgba(0,132,255,0.15)" stroke="#00d4ff" stroke-width="2"/>
        <circle cx="70" cy="70" r="12" fill="rgba(0,212,255,0.2)"/>
        <circle cx="70" cy="70" r="7" fill="#00d4ff"/>
        <circle cx="70" cy="70" r="4" fill="#ffffff"/>
      </g>
    </svg>
  </div>

  <p class="hero-eyebrow">▶ System Online · AI Core Active</p>

  <h1>
    JARVIS
    <span>Intelligent Virtual Assistant</span>
  </h1>

  <p class="hero-sub">
    Inspired by Iron Man's J.A.R.V.I.S. — an advanced Python-powered AI assistant combining voice recognition, NLP, and intelligent automation into one seamless platform.
  </p>

  <div class="hero-badges">
    <span class="badge badge-blue">Python</span>
    <span class="badge badge-cyan">AI + NLP</span>
    <span class="badge badge-green">Voice Controlled</span>
    <span class="badge badge-blue">Open Source</span>
    <span class="badge badge-cyan">Machine Learning</span>
  </div>

  <div class="status-bar">
    <div class="status-item"><div class="status-dot"></div> Voice Engine: Active</div>
    <div class="status-item"><div class="status-dot blue"></div> AI Core: Online</div>
    <div class="status-item"><div class="status-dot"></div> All Systems Go</div>
  </div>

  <div class="scroll-hint">
    <span>SCROLL</span>
    <div class="scroll-arrow"></div>
  </div>
</section>

<div class="divider"></div>

<!-- ══════════ FEATURES ══════════ -->
<section class="section">
  <p class="section-label">02 · Capabilities</p>
  <h2 class="section-title">Core Features</h2>
  <div class="features-grid">
    <div class="feat-card">
      <div class="feat-icon">🎤</div>
      <h3>Voice Recognition</h3>
      <p>Converts speech to text in real-time, understands natural language commands, and enables seamless voice-driven interaction.</p>
      <div class="feat-tags"><span class="feat-tag">SpeechRecognition</span><span class="feat-tag">Real-time</span></div>
    </div>
    <div class="feat-card">
      <div class="feat-icon">🗣️</div>
      <h3>Text-to-Speech</h3>
      <p>Delivers human-like voice responses using Pyttsx3 for a natural and conversational AI experience.</p>
      <div class="feat-tags"><span class="feat-tag">Pyttsx3</span><span class="feat-tag">Voice Output</span></div>
    </div>
    <div class="feat-card">
      <div class="feat-icon">🌐</div>
      <h3>Web Automation</h3>
      <p>Opens websites, searches Google, plays YouTube videos, and browses online content hands-free.</p>
      <div class="feat-tags"><span class="feat-tag">Selenium</span><span class="feat-tag">Automation</span></div>
    </div>
    <div class="feat-card">
      <div class="feat-icon">🤖</div>
      <h3>AI Chatbot</h3>
      <p>Intelligent conversation engine with context-aware responses powered by OpenAI and Hugging Face models.</p>
      <div class="feat-tags"><span class="feat-tag">OpenAI</span><span class="feat-tag">HuggingFace</span></div>
    </div>
    <div class="feat-card">
      <div class="feat-icon">📅</div>
      <h3>Productivity</h3>
      <p>Tells date and time, sets reminders, manages tasks, and handles quick calculations on command.</p>
      <div class="feat-tags"><span class="feat-tag">Task Manager</span><span class="feat-tag">Reminders</span></div>
    </div>
    <div class="feat-card">
      <div class="feat-icon">🎵</div>
      <h3>Entertainment</h3>
      <p>Plays music, opens Spotify, streams YouTube content, and delivers fun interactive experiences.</p>
      <div class="feat-tags"><span class="feat-tag">Spotify</span><span class="feat-tag">YouTube</span></div>
    </div>
    <div class="feat-card">
      <div class="feat-icon">💻</div>
      <h3>System Control</h3>
      <p>Launches applications, executes system commands, and automates computer operations via voice.</p>
      <div class="feat-tags"><span class="feat-tag">OS Automation</span><span class="feat-tag">Commands</span></div>
    </div>
    <div class="feat-card">
      <div class="feat-icon">👤</div>
      <h3>Face Recognition</h3>
      <p>Optional biometric authentication using OpenCV for personalized, secure user interaction.</p>
      <div class="feat-tags"><span class="feat-tag">OpenCV</span><span class="feat-tag">Optional</span></div>
    </div>
  </div>
</section>

<div class="divider"></div>

<!-- ══════════ WORKFLOW ══════════ -->
<section class="section">
  <p class="section-label">03 · How It Works</p>
  <h2 class="section-title">Animated Workflow</h2>
  <div class="workflow">
    <div class="flow-steps" id="flow-steps">
      <div class="flow-step" style="--delay:0s">
        <div class="flow-node">
          🎙️
          <div class="node-ring"></div>
        </div>
        <div class="flow-label">Voice Input</div>
      </div>
      <div class="flow-arrow animated"></div>
      <div class="flow-step" style="--delay:0.15s">
        <div class="flow-node">🔊<div class="node-ring" style="animation-direction:reverse"></div></div>
        <div class="flow-label">Speech Recognition</div>
      </div>
      <div class="flow-arrow animated"></div>
      <div class="flow-step" style="--delay:0.3s">
        <div class="flow-node">🧠<div class="node-ring"></div></div>
        <div class="flow-label">Intent Analysis</div>
      </div>
      <div class="flow-arrow animated"></div>
      <div class="flow-step" style="--delay:0.45s">
        <div class="flow-node">⚡<div class="node-ring" style="animation-direction:reverse"></div></div>
        <div class="flow-label">Task Execution</div>
      </div>
      <div class="flow-arrow animated"></div>
      <div class="flow-step" style="--delay:0.6s">
        <div class="flow-node">📢<div class="node-ring"></div></div>
        <div class="flow-label">Voice Response</div>
      </div>
    </div>

    <!-- Terminal preview -->
    <div class="terminal">
      <div class="terminal-bar">
        <div class="t-dot"></div>
        <div class="t-dot"></div>
        <div class="t-dot"></div>
        <span class="t-title">jarvis_main.py</span>
      </div>
      <div class="t-line"><span class="t-prompt">$ </span><span class="t-cmd">python jarvis_main.py</span></div>
      <div class="t-line t-out info">▶  Initializing JARVIS AI System...</div>
      <div class="t-line t-out success">✓  Speech Recognition Engine: Ready</div>
      <div class="t-line t-out success">✓  Text-to-Speech Module: Active</div>
      <div class="t-line t-out success">✓  AI Chatbot Core: Loaded</div>
      <div class="t-line t-out success">✓  Web Automation: Standby</div>
      <div class="t-line t-out info">◈  Listening for commands...</div>
      <div class="t-line"><span class="t-prompt">JARVIS &gt; </span><span class="t-cmd" id="typing-text"></span><span class="typing-cursor"></span></div>
    </div>
  </div>
</section>

<div class="divider"></div>

<!-- ══════════ TECH STACK ══════════ -->
<section class="section">
  <p class="section-label">04 · Technology</p>
  <h2 class="section-title">Technology Stack</h2>
  <div class="tech-grid" id="tech-grid">
    <div class="tech-item"><div class="tech-icon">🐍</div><div class="tech-info"><div class="tech-name">Python</div><div class="tech-purpose">Core Development</div></div></div>
    <div class="tech-item"><div class="tech-icon">🎤</div><div class="tech-info"><div class="tech-name">SpeechRecognition</div><div class="tech-purpose">Voice Input</div></div></div>
    <div class="tech-item"><div class="tech-icon">🔊</div><div class="tech-info"><div class="tech-name">Pyttsx3</div><div class="tech-purpose">Text-to-Speech</div></div></div>
    <div class="tech-item"><div class="tech-icon">👁️</div><div class="tech-info"><div class="tech-name">OpenCV</div><div class="tech-purpose">Face Recognition</div></div></div>
    <div class="tech-item"><div class="tech-icon">📝</div><div class="tech-info"><div class="tech-name">NLTK</div><div class="tech-purpose">NLP Processing</div></div></div>
    <div class="tech-item"><div class="tech-icon">🧠</div><div class="tech-info"><div class="tech-name">TensorFlow</div><div class="tech-purpose">AI Models</div></div></div>
    <div class="tech-item"><div class="tech-icon">🌐</div><div class="tech-info"><div class="tech-name">Selenium</div><div class="tech-purpose">Browser Automation</div></div></div>
    <div class="tech-item"><div class="tech-icon">🤖</div><div class="tech-info"><div class="tech-name">OpenAI API</div><div class="tech-purpose">Intelligent Responses</div></div></div>
    <div class="tech-item"><div class="tech-icon">🤗</div><div class="tech-info"><div class="tech-name">Hugging Face</div><div class="tech-purpose">AI Integration</div></div></div>
    <div class="tech-item"><div class="tech-icon">🗄️</div><div class="tech-info"><div class="tech-name">SQLite / MySQL</div><div class="tech-purpose">Data Storage</div></div></div>
  </div>
</section>

<div class="divider"></div>

<!-- ══════════ OBJECTIVES ══════════ -->
<section class="section">
  <p class="section-label">05 · Goals</p>
  <h2 class="section-title">Project Objectives</h2>
  <div class="objectives-list" id="obj-list">
    <div class="obj-item"><span class="obj-num">01</span><span class="obj-text">Build a smart voice-controlled assistant with real-time response capabilities.</span></div>
    <div class="obj-item"><span class="obj-num">02</span><span class="obj-text">Automate repetitive computer tasks to boost productivity and efficiency.</span></div>
    <div class="obj-item"><span class="obj-num">03</span><span class="obj-text">Integrate cutting-edge AI and NLP technologies into a unified platform.</span></div>
    <div class="obj-item"><span class="obj-num">04</span><span class="obj-text">Improve human-computer interaction through natural conversation and voice.</span></div>
    <div class="obj-item"><span class="obj-num">05</span><span class="obj-text">Create a scalable, modular personal assistant platform for future growth.</span></div>
  </div>
</section>

<div class="divider"></div>

<!-- ══════════ FUTURE ══════════ -->
<section class="section">
  <p class="section-label">06 · Roadmap</p>
  <h2 class="section-title">Future Enhancements</h2>
  <div class="future-grid" id="future-grid">
    <div class="future-item"><span>🤖</span><span>ChatGPT / GPT-4 Integration</span></div>
    <div class="future-item"><span>🏠</span><span>Smart Home Automation</span></div>
    <div class="future-item"><span>📡</span><span>IoT Device Control</span></div>
    <div class="future-item"><span>🌍</span><span>Multi-language Support</span></div>
    <div class="future-item"><span>😊</span><span>Emotion Detection</span></div>
    <div class="future-item"><span>🧠</span><span>Personal Memory System</span></div>
    <div class="future-item"><span>📱</span><span>Mobile Application</span></div>
    <div class="future-item"><span>☁️</span><span>Cloud-Based Deployment</span></div>
  </div>
</section>

<div class="divider"></div>

<!-- ══════════ DEVELOPER ══════════ -->
<section class="dev-section">
  <p class="section-label" style="justify-content:center;max-width:400px;margin:0 auto 40px;">07 · Developer</p>
  <div class="dev-card animate-on-scroll">
    <div class="dev-avatar">AT</div>
    <div>
      <div class="dev-name">Ayush Trivedi</div>
      <div class="dev-title" style="margin-top:6px">MCA Student · LPU</div>
    </div>
    <p class="dev-uni">🎓 <strong>Lovely Professional University</strong></p>
    <div class="dev-tags">
      <span class="dev-tag">Python Developer</span>
      <span class="dev-tag">AI Enthusiast</span>
      <span class="dev-tag">Web Developer</span>
      <span class="dev-tag">🎮 Valorant · eSports</span>
    </div>
    <div class="star-cta">⭐ Star this repo if you found it useful!</div>
  </div>
</section>

<script>
// ─── INTERSECTION OBSERVER FOR CARDS ───
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible', 'in-view');
    }
  });
}, { threshold: 0.1 });

// Observe feat cards
document.querySelectorAll('.feat-card, .tech-item, .obj-item, .future-item, .animate-on-scroll').forEach((el, i) => {
  el.style.animationDelay = (i * 0.07) + 's';
  observer.observe(el);
});

// Observe flow steps
const flowObs = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      document.querySelectorAll('.flow-step').forEach((s, i) => {
        s.style.animationDelay = (i * 0.2) + 's';
        s.classList.add('visible');
      });
    }
  });
}, { threshold: 0.3 });
const flowEl = document.getElementById('flow-steps');
if (flowEl) flowObs.observe(flowEl);

// ─── TERMINAL TYPING EFFECT ───
const commands = [
  "Hey JARVIS, what's the time?",
  "Open YouTube...",
  "Search for AI news today",
  "Play my playlist on Spotify",
];
let ci = 0, li = 0;
const typingEl = document.getElementById('typing-text');

function typeNext() {
  if (!typingEl) return;
  const cmd = commands[ci];
  if (li < cmd.length) {
    typingEl.textContent += cmd[li++];
    setTimeout(typeNext, 60 + Math.random() * 40);
  } else {
    setTimeout(() => {
      typingEl.textContent = '';
      li = 0;
      ci = (ci + 1) % commands.length;
      typeNext();
    }, 2200);
  }
}
setTimeout(typeNext, 1500);

// ─── PARALLAX HERO GRID ───
document.addEventListener('mousemove', (e) => {
  const x = (e.clientX / window.innerWidth - 0.5) * 20;
  const y = (e.clientY / window.innerHeight - 0.5) * 20;
  document.querySelector('.grid-bg').style.transform = `translate(${x}px, ${y}px)`;
});
</script>
</body>
</html>
