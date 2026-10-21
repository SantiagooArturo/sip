#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera el index.html de la Sesion 1 de SIP (indice clasico de MyWorkIn):
intro animada palabra por palabra -> home con una tarjeta por bloque.
"""
import os

from build_decks import FILES
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "sesion-2", "build"))
from contenido2 import FILES2  # noqa: E402
from deck import LOGO_MW, OUT_DIR, HERE, logo_em

with open(os.path.join(HERE, "index_base.css"), encoding="utf-8") as f:
    BASE_CSS = f.read()

EXT_CSS = """
/* ---------- extensiones ---------- */
[hidden]{display:none!important}
.allses{font-family:var(--fm);font-size:12px;color:#C3CEDF;text-decoration:none;border:1px solid rgba(255,255,255,.18);border-radius:999px;padding:8px 16px;background:rgba(255,255,255,.05);align-self:center;line-height:1}
.allses:hover{color:#8FB4F8;border-color:#8FB4F8}
.plate img.ib{height:34px}
#l2 .intro-plate img.ib{height:32px}
.em-ph{font-family:var(--fm);font-size:10.5px;color:var(--mut);border:1px dashed #B9B5AA;
  border-radius:6px;padding:3px 9px;letter-spacing:.02em;white-space:nowrap}
.intro-wrap{width:100%}
.intro-line{word-break:normal;overflow-wrap:break-word}
.cards{grid-template-columns:repeat(8,1fr);gap:16px}
.cards .card{grid-column:span 2;padding:22px 22px 20px}
.cards .card:nth-child(9){grid-column:2 / span 2}
.cards .card h2{font-size:22px}
.cards .card p{font-size:13.5px}
.card .mins{position:absolute;top:22px;right:22px;font-family:var(--fm);font-size:10.5px;color:var(--lemon)}
@media (max-width:900px){
  .cards{grid-template-columns:1fr 1fr}
  .cards .card,.cards .card:nth-child(9){grid-column:auto}
}
@media (max-width:560px){
  .cards{grid-template-columns:1fr}
  .intro-wrap{padding:0 24px}
  .intro-line{font-size:26px}
  .home-inner{padding:0 24px}
  .session-chip{flex-direction:column;gap:3px;text-align:center;border-radius:18px;padding:10px 18px}
  .session-chip .dot,.session-chip .sep{display:none}
  .ses-h{flex-wrap:wrap;gap:4px 12px}
  .ses-h .n{flex-basis:100%}
}
.ses-h{display:flex;align-items:baseline;gap:14px;margin:46px 0 16px;scroll-margin-top:30px}
.ses-h:first-of-type{margin-top:40px}
.ses-h .n{font-family:var(--fm);font-size:12px;color:var(--lemon);letter-spacing:.05em}
.ses-h h3{font-size:22px;font-weight:600;color:var(--oat);letter-spacing:-.02em}
.ses-h .d{font-family:var(--fm);font-size:11.5px;color:#C3CEDF}
"""

CARD = """      <a class="card" href="%(href)s">
        <span class="bar"></span>
        <span class="tag">Bloque %(n)d de 11</span><span class="mins">%(mins)s</span>
        <h2>%(title)s</h2>
        <p>%(desc)s</p>
        <span class="cta">Entrar al bloque <span class="arrow">&rarr;</span></span>
      </a>"""

cards = "\n".join(CARD % {"href": f, "n": i + 1, "mins": mins, "title": t, "desc": d}
                  for i, (f, t, mins, d) in enumerate(FILES))
cards2 = "\n".join(CARD % {"href": "../sesion-2/" + f, "n": i + 1, "mins": mins, "title": t, "desc": d}
                   for i, (f, t, mins, d) in enumerate(FILES2))

HTML = """<!doctype html>
<html lang="es"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Workshop de IA con Claude &middot; SIP</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
%(css)s
</style></head>
<body>
<div class="bg"></div>

<div id="intro">
  <div class="intro-wrap">
    <div class="intro-line" id="l1"></div>
    <div class="intro-line" id="l2"></div>
  </div>
  <div class="intro-skip">clic para continuar</div>
</div>

<div id="home">
  <div class="home-inner">
    <div class="home-top" style="justify-content:center">
      <div class="plate"><img src="%(logo)s" class="mw" alt="MyWorkIn">%(logo_em)s</div>
    </div>
    <div style="display:flex;justify-content:center">
      <div class="session-chip"><span class="dot"></span><span>Sesiones 1 y 2 &middot; Workshop y taller pr&aacute;ctico</span><span class="sep">&middot;</span><span><b>Santiago Franco</b> &middot; MyWorkIn</span></div>
    </div>
    <div class="home-eyebrow">Workshop de IA con Claude &middot; SIP</div>
    <h1 class="home-title">Elige el bloque que quieres revisar</h1>

    <div class="ses-h" id="s1"><span class="n">SESI&Oacute;N 1</span><h3>Fundamentos de IA y entornos de Claude</h3><span class="d">11 bloques</span></div>
    <div class="cards">
%(cards)s
    </div>
    <div class="ses-h" id="s2"><span class="n">SESI&Oacute;N 2</span><h3>Taller pr&aacute;ctico: Conectores, Skills y Artefactos</h3><span class="d">11 bloques</span></div>
    <div class="cards">
%(cards2)s
    </div>

    <div class="home-foot">MyWorkIn &times; SIP &mdash; 2026</div>
  </div>
</div>

<script>
// build the two intro lines word-by-word
function buildLine(el, text, delayStart, gap){
  const words = text.split(' ');
  let delay = delayStart;
  words.forEach((w,i)=>{
    const span = document.createElement('span');
    span.className = 'w';
    span.style.animationDelay = delay + 's';
    span.textContent = w;
    el.appendChild(span);
    // el espacio va FUERA del inline-block: dentro, WebKit (Safari/iOS) lo colapsa
    if (i < words.length-1) el.appendChild(document.createTextNode(' '));
    delay += gap;
  });
  return delay;
}
const l1 = document.getElementById('l1');
const l2 = document.getElementById('l2');
let t = buildLine(l1, 'Aumenta tu productividad 10x con IA,', 0.15, 0.10);
l1.appendChild(document.createTextNode(' '));
t = buildLine(l1, 'MyWorkIn te ense\\u00f1a c\\u00f3mo.', t + 0.12, 0.10);
const introPlate = document.createElement('div');
introPlate.className = 'intro-plate';
introPlate.style.animationDelay = (t + 0.35) + 's';
// se clona el contenido de la placa con los dos logos
introPlate.innerHTML = document.querySelector('.plate').innerHTML;
l2.appendChild(introPlate);

const intro = document.getElementById('intro');
const home = document.getElementById('home');
let entered = false;
function enter(){
  if(entered) return;
  entered = true;
  try{ sessionStorage.setItem('sip1_intro','1'); }catch(e){}
  intro.classList.add('hide');
  home.classList.add('show');
  setTimeout(()=>{ intro.style.display='none'; }, 600);
}
// la intro se ve una sola vez por pestaña: al volver de un bloque se entra directo
let visto = false;
try{ visto = sessionStorage.getItem('sip1_intro') === '1'; }catch(e){}
if(visto){
  entered = true;
  intro.style.display = 'none';
  home.style.transition = 'none';
  home.classList.add('show');
}else{
  intro.addEventListener('click', enter);
  setTimeout(enter, 3600);
}
// al volver de un bloque de la Sesion 2 (index.html#s2) se baja a esa seccion
if(location.hash){
  setTimeout(()=>{ const el=document.querySelector(location.hash); if(el) el.scrollIntoView(); }, visto ? 50 : 4300);
}
</script>
</body></html>
""" % {"css": BASE_CSS + EXT_CSS, "logo": LOGO_MW, "logo_em": logo_em(), "cards": cards, "cards2": cards2}

out = os.path.join(OUT_DIR, "index.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(HTML)
print("%-38s %7d bytes" % ("index.html", os.path.getsize(out)))
