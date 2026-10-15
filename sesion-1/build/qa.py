#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QA del deck: sintaxis HTML/JS, conteo de slides, paginacion, y renderizado
headless en Chrome midiendo desbordes y contenido recortado dentro de las cajas.

Uso:  python3 qa.py                      (los 5 decks)
      python3 qa.py 02_Claude.html --shot 3 5
"""
import html
import html.parser
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.abspath(os.path.join(HERE, ".."))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Ruido estructural que el deck original de Interbank tambien tiene: el .body
# mide 11px de mas por el borde superior del pie. No es un defecto visual.
RUIDO = {"body:11", "demo wide:11", "col-l:11", "anim:5", "anim:3"}

QA_JS = r"""
<pre id="qa"></pre>
<script>
try{
  const out=[];
  const els=[...document.querySelectorAll('.slide')];
  els.forEach((sl,i)=>{
    els.forEach(x=>x.classList.remove('active'));
    sl.classList.add('active');
    void sl.offsetHeight;
    const pad=sl.querySelector('.pad');
    const ovPad=pad.scrollHeight-pad.clientHeight;
    let bad=[];
    sl.querySelectorAll('*').forEach(n=>{
      const o=n.scrollHeight-n.clientHeight;
      if(o>5 && n.clientHeight>0) bad.push('SCROLL '+(n.className||n.tagName)+':'+o);
    });
    sl.querySelectorAll('.card,.gcard,.st,.bi,.eb,.mcell,.panel,.mx,.rule,.note,.shot')
      .forEach(box=>{
        const cs=getComputedStyle(box);
        if(cs.overflow==='visible' && cs.overflowY==='visible') return;
        const rb=box.getBoundingClientRect();
        box.querySelectorAll('*').forEach(ch=>{
          const rc=ch.getBoundingClientRect();
          if(rc.height===0) return;
          const cut=Math.max(rc.bottom-rb.bottom, rb.top-rc.top);
          if(cut>1.5) bad.push('CORTE '+box.className.split(' ')[0]+'>'+
            (ch.className||ch.tagName)+':'+cut.toFixed(0));
        });
      });
    out.push('slide '+String(i+1).padStart(2,'0')+' padOv='+ovPad+' | '+
      ([...new Set(bad)].join(' , ')||'ok'));
  });
  document.getElementById('qa').textContent='QAX'+String.fromCharCode(10)+out.join(String.fromCharCode(10));
}catch(e){document.getElementById('qa').textContent='ERR '+e.message}
</script>
"""

SHOT_JS = ("\n<script>show(parseInt(location.hash.slice(1)||'1',10)-1);"
           "document.querySelectorAll('.anim').forEach(e=>{e.style.transition='none';"
           "e.style.opacity=1;e.style.transform='none'});"
           "document.querySelector('.ctl').style.display='none';"
           "document.querySelector('.hint').style.display='none';</script>\n")


def check_static(s):
    fallos = []
    n = len(re.findall(r'<section class="slide', s))
    for pat in [r'%\(', r'%s(?![a-zA-Z])', r'\{\{', r'\bNone\b', r'&lt;div', r'\\n']:
        if re.search(pat, s):
            fallos.append("residuo de plantilla: %s" % pat)

    void = {'img', 'br', 'hr', 'meta', 'link', 'input', 'source'}

    class P(html.parser.HTMLParser):
        def __init__(x):
            super().__init__(); x.st = []; x.e = []
        def handle_starttag(x, t, a):
            if t not in void: x.st.append(t)
        def handle_endtag(x, t):
            if t in void: return
            if not x.st or x.st[-1] != t: x.e.append(t)
            else: x.st.pop()

    p = P(); p.feed(s)
    if p.e: fallos.append("tags mal cerrados: %s" % p.e[:5])
    if p.st: fallos.append("tags sin cerrar: %s" % p.st)

    # cada pie debe mostrar el numero de su propio slide (portada y frases van sin pie)
    secciones = re.split(r'(?=<section class="slide)', s)[1:]
    for i, sec in enumerate(secciones, 1):
        m = re.search(r'<span class="pg">(\d+)</span>', sec)
        if m and int(m.group(1)) != i:
            fallos.append("pie del slide %d dice %s" % (i, m.group(1)))

    js = "\n".join(re.findall(r'<script>(.*?)</script>', s, re.S))
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
        f.write(js); jsp = f.name
    r = subprocess.run(["node", "--check", jsp], capture_output=True, text=True)
    os.unlink(jsp)
    if r.returncode: fallos.append("JS invalido: %s" % r.stderr.strip()[:200])

    return n, fallos


def render(path, url_extra="", size="1280,720", screenshot=None):
    cmd = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
           "--window-size=" + size, "--virtual-time-budget=12000"]
    if screenshot:
        cmd.append("--screenshot=" + screenshot)
    else:
        cmd.append("--dump-dom")
    cmd.append("file://" + path + url_extra)
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.stdout


DECKS = sorted(f for f in os.listdir(OUT_DIR) if re.match(r"0[1-9]_.*\.html$", f))  # noqa


def main():
    args = sys.argv[1:]
    decks = [a for a in args if a.endswith(".html")] or DECKS
    shots = args[args.index("--shot") + 1:] if "--shot" in args else []
    mal = False
    for d in decks:
        print("=" * 12, d)
        mal |= qa_deck(os.path.join(OUT_DIR, d), shots)
    sys.exit(1 if mal else 0)


def qa_deck(DECK, shots):
    s = open(DECK, encoding="utf-8").read()
    n, fallos = check_static(s)
    print("slides: %d" % n)
    print("estatico: %s" % ("OK" if not fallos else fallos))

    tmp = tempfile.mkdtemp()
    qa_path = os.path.join(tmp, "qa.html")
    open(qa_path, "w").write(s.replace("</body>", QA_JS + "</body>"))
    dom = render(qa_path)
    m = re.search(r'<pre id="qa">(.*?)</pre>', dom, re.S)
    if not m:
        print("render: NO SE PUDO LEER EL RESULTADO"); sys.exit(1)
    lineas = html.unescape(m.group(1)).strip().split("\n")[1:]

    problemas = []
    for l in lineas:
        cab, _, det = l.partition(" | ")
        items = [i.strip() for i in det.split(",") if i.strip() and i.strip() != "ok"]
        items = [i for i in items if i.split(" ", 1)[-1] not in RUIDO]
        if "padOv=0" not in cab or items:
            problemas.append("%s | %s" % (cab, ", ".join(items) or "desborde del marco"))

    print("renderizados: %d" % len(lineas))
    print("problemas: %s" % ("ninguno" if not problemas else ""))
    for p in problemas:
        print("  " + p)

    if shots:
        shot_path = os.path.join(tmp, "shot.html")
        open(shot_path, "w").write(s.replace("</body>", SHOT_JS + "</body>"))
        outdir = os.path.join(tmp, "shots"); os.makedirs(outdir, exist_ok=True)
        for num in shots:
            dst = os.path.join(outdir, "%s_s%s.png" % (os.path.basename(DECK)[:2], num))
            render(shot_path, "#" + num, screenshot=dst)
            print("captura: " + dst)

    return bool(fallos or problemas)


if __name__ == "__main__":
    main()
