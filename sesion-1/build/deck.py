# -*- coding: utf-8 -*-
"""
Motor de los decks de SIP: helpers del motor de Motivarte/Monte Azul con el sistema visual de Interbank (base.css, Figtree). Replica el sistema de diseno de los
talleres de Interbank e inLearning (mismo CSS base, misma navegacion, archivo
unico con assets embebidos en base64).

Logos embebidos: cada HTML es un solo archivo.
"""
import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.abspath(os.path.join(HERE, ".."))
ASSETS = os.path.join(OUT_DIR, "assets")

PROGRAMA = "Workshop de IA con Claude · SIP"


def datauri(path):
    ext = os.path.splitext(path)[1].lower().lstrip(".")
    mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg", "svg": "image/svg+xml"}[ext]
    with open(path, "rb") as f:
        return "data:%s;base64,%s" % (mime, base64.b64encode(f.read()).decode())


LOGO_MW = datauri(os.path.join(ASSETS, "logo_myworkin.png"))
LOGO_SIP = datauri(os.path.join(ASSETS, "logo_sip.svg"))


def logo_em():
    return '<span class="sep"></span><img src="%s" class="ib" alt="SIP">' % LOGO_SIP


with open(os.path.join(HERE, "base.css"), encoding="utf-8") as f:
    BASE_CSS = f.read()

EXT_CSS = """
/* ---------- extensiones ---------- */
[hidden]{display:none!important}
h1.t{max-width:32ch}
.plate img.ib{height:30px}
.em-ph{font-family:var(--fm);font-size:10.5px;color:var(--mut);border:1px dashed #C9D2DF;
  border-radius:6px;padding:3px 9px;letter-spacing:.02em;white-space:nowrap}
.dark .mcell{background:var(--navy-2);border-color:var(--line-d)}
.dark .mcell .k{color:var(--mut-d)}
.dark .mcell .v{color:var(--oat)}
.dark .mcell .v span{color:var(--mut-d)}
.mrow.tight{margin-top:24px}
.dv.quote h1{font-size:40px;line-height:1.14;max-width:28ch;letter-spacing:-.028em}
.card .steps{margin-top:13px}
.card .lst{margin-top:10px;list-style:none}
.card .lst li{font-size:13.5px;line-height:1.6;color:var(--mut);padding-left:22px;position:relative}
.card .lst li + li{margin-top:6px}
.rule{margin-bottom:12px}
.gwrap.tight .gcard{padding:16px 20px}
.gwrap.tight .gcard h4{font-size:17px}
.gwrap.tight .gcard p{font-size:12.5px;line-height:1.45;margin-top:5px}
.gwrap.tight .gcard .bdg{margin-bottom:9px}
.card.tight{padding:18px 22px}
.card.tight h3{font-size:21px;margin-top:10px}
.card.tight .lst{margin-top:8px}
.card.tight .lst li{line-height:1.5}
.card.tight .lst li + li{margin-top:4px}
.demo.wide{grid-template-columns:.92fr 1.18fr;gap:30px}
.demo.wide .shot{align-items:center}
.demo.wide .shot img{height:auto;width:100%;max-height:100%;object-fit:contain}
.demo .note{margin-top:16px}
.dark .card .lst li{color:var(--mut-d)}
.card .lst li::before{content:"\\2014";position:absolute;left:0;color:var(--blue)}
.dark .card .lst li::before{color:var(--lemon)}
.card .lst li b{color:var(--ink);font-weight:600}
.dark .card .lst li b{color:var(--oat)}
.ctl .back{color:#FFFFFF;text-decoration:none;font-family:var(--fm);font-size:11.5px;padding:3px 10px;border-radius:999px;background:rgba(56,89,249,.55);transition:background .2s ease}
.ctl .back:hover{background:#3859F9}
.ctl .div{width:1px;height:16px;background:rgba(255,255,255,.18)}
.hint a{color:#8391AA;text-decoration:none}
.hint a:hover{color:#8FB4F8}
/* agenda con minutos */
.row{grid-template-columns:40px 300px 1fr 92px}
.row.now{border-color:var(--blue);box-shadow:0 0 0 1px var(--blue) inset}
.row.now .rm{background:var(--blue);color:#fff;border-color:var(--blue)}
/* bloque de prompt */
.prompt{margin-top:16px;background:#0D1B3A;border:1px solid #243A66;border-radius:var(--r-l);padding:16px 20px;
  font-family:var(--fm);font-size:12.5px;line-height:1.62;color:#E3E9F3;flex:none}
.prompt .pl{display:block;font-size:10px;color:var(--lemon);letter-spacing:.06em;margin-bottom:7px}
.prompt b{color:#fff;font-weight:500}
.prompt{position:relative}
.prompt .cp{position:absolute;top:12px;right:14px;font-family:var(--fm);font-size:11px;color:#E3E9F3;
  background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.18);border-radius:999px;
  padding:4px 12px;cursor:pointer;transition:background .2s ease,color .2s ease}
.prompt .dp{position:absolute;top:12px;right:92px;font-family:var(--fm);font-size:11px;color:#E3E9F3;
  background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.18);border-radius:999px;
  padding:4px 12px;cursor:pointer;transition:background .2s ease,color .2s ease}
.prompt .dp:hover{background:var(--blue);border-color:var(--blue);color:#fff}
.prompt .dp.ok{background:#1F8A5B;border-color:#1F8A5B;color:#fff}
.prompt .pl{padding-right:200px}
.prompt .cp:hover{background:var(--blue);border-color:var(--blue);color:#fff}
.prompt .cp.ok{background:#1F8A5B;border-color:#1F8A5B;color:#fff}
.dark .prompt{background:rgba(250,249,245,.06);border-color:var(--line-d)}
/* ficha de caso */
.case{display:grid;grid-template-columns:1.05fr 1fr;gap:16px;margin-top:20px;margin-bottom:14px;flex:1;min-height:0}
.case .cbox{background:#fff;border:1px solid var(--line);border-radius:var(--r-l);padding:20px 24px;display:flex;flex-direction:column;justify-content:center;min-height:0}
.dark .case .cbox{background:var(--navy-2);border-color:var(--line-d)}
.case .k{font-family:var(--fm);font-size:10.5px;color:var(--blue);letter-spacing:.04em}
.dark .case .k{color:var(--lemon)}
.case .cbox p{font-size:14px;line-height:1.58;color:var(--ink);margin-top:7px}
.dark .case .cbox p{color:var(--oat)}
.case .cbox p + .k{margin-top:16px}
.case .who{margin-top:14px;font-family:var(--fm);font-size:11px;color:var(--mut);display:block}
.dark .case .who{color:var(--mut-d)}
.dlbtn{margin-top:18px;align-self:flex-start;display:inline-flex;align-items:center;gap:9px;
  font-family:var(--fm);font-size:12.5px;color:#fff;background:var(--blue);border-radius:999px;
  padding:10px 20px;text-decoration:none;transition:transform .2s ease,background .2s ease}
.dlbtn:hover{background:#2440D8;transform:translateY(-2px)}
.dlbtn .ic{font-size:14px}
/* timeline */
.tl{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:26px}
.tl .ti{background:#fff;border:1px solid var(--line);border-radius:var(--r-l);padding:18px 20px;position:relative}
.dark .tl .ti{background:var(--navy-2);border-color:var(--line-d)}
.tl .ti .d{font-family:var(--fm);font-size:11px;color:var(--mut)}
.dark .tl .ti .d{color:var(--mut-d)}
.tl .ti h4{font-size:18px;font-weight:600;letter-spacing:-.02em;color:var(--ink);margin-top:8px}
.dark .tl .ti h4{color:var(--oat)}
.tl .ti p{font-size:13px;line-height:1.5;color:var(--mut);margin-top:6px}
.dark .tl .ti p{color:var(--mut-d)}
.tl .ti .st8{position:absolute;top:16px;right:16px;font-family:var(--fm);font-size:9.5px;border-radius:999px;padding:3px 9px}
.st8.done{background:rgba(29,28,26,.07);color:var(--mut)}
.st8.now{background:var(--blue);color:#fff}
.st8.goal{background:var(--lemon);color:#06182D}
.tl .ti.goal{border-color:var(--lemon);box-shadow:0 0 0 1px var(--lemon) inset}

/* ---------- sesion 3 ---------- */
.sem{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:18px;flex:1;min-height:0}
.sem .sm{background:#fff;border:1px solid var(--line);border-radius:var(--r-l);padding:0 18px 16px;display:flex;flex-direction:column;overflow:hidden}
.sem .sm .bd{height:8px;margin:0 -18px 14px}
.sem .sm .k{font-family:var(--fm);font-size:11px;color:var(--ink);letter-spacing:.03em;font-weight:500}
.sem .sm h4{font-size:17px;font-weight:600;letter-spacing:-.02em;color:var(--ink);margin-top:6px}
.sem .sm p{font-size:13px;line-height:1.5;color:var(--mut);margin-top:8px;flex:1}
.sem .sm .use{font-size:12.5px;line-height:1.45;color:var(--ink);background:var(--oat-2);border-radius:10px;padding:9px 11px;margin-top:12px}
.dv.quote.center{align-items:center;text-align:center}
.dv.quote.center .big:empty{display:none}
.dv.quote.center h1{max-width:none;font-size:96px;margin-top:0}
.mini3{display:grid;grid-template-columns:1.25fr 1fr 1fr;gap:14px;margin-top:18px}
.mini3 .mt{background:#fff;border:1px solid var(--line);border-radius:var(--r-l);overflow:hidden}
.mini3 .mt .hd{font-family:var(--fm);font-size:10.5px;letter-spacing:.05em;padding:9px 12px;color:#fff;background:#06182D}
.mini3 .mt.bad .hd{background:#B3261E}.mini3 .mt.ok .hd{background:#1F8A5B}.mini3 .mt.key .hd{background:#06182D}
.mini3 table{width:100%;border-collapse:collapse;font-size:11.5px}
.mini3 th{font-family:var(--fm);font-size:9.5px;color:var(--mut);text-align:left;padding:6px 8px;border-bottom:1px solid var(--line);font-weight:500}
.mini3 td{padding:6px 8px;border-bottom:1px solid var(--line);color:var(--ink);white-space:nowrap}
.mini3 td.pii{color:#B3261E}
.mini3 .ft{font-size:11.5px;color:var(--mut);padding:8px 12px;line-height:1.4}
.vs{display:grid;grid-template-columns:1fr 1fr;gap:15px;margin-top:22px;flex:1;min-height:0}
.vs .col{border-radius:var(--r-l);padding:22px 24px;display:flex;flex-direction:column;justify-content:center}
.vs .col.no{background:#fff;border:1px solid var(--line)}
.vs .col.si{background:linear-gradient(160deg,#0C1A38 0%,#16294F 100%);color:var(--oat)}
.vs .col .k{font-family:var(--fm);font-size:11px;letter-spacing:.05em}
.vs .col.no .k{color:#B3261E}.vs .col.si .k{color:var(--lemon)}
.vs .col h3{font-size:23px;font-weight:600;letter-spacing:-.02em;margin-top:8px;line-height:1.2}
.vs .col.no h3{color:var(--ink)}
.vs .col ul{list-style:none;margin-top:14px}
.vs .col li{font-size:14px;line-height:1.5;padding:5px 0 5px 24px;position:relative}
.vs .col.no li{color:var(--mut)}.vs .col.si li{color:var(--mut-d)}
.vs .col.no li::before{content:"\\2717";position:absolute;left:0;color:#B3261E}
.vs .col.si li::before{content:"\\2713";position:absolute;left:0;color:var(--lemon)}
/* ---------- sesion 2: diagrama del agente ---------- */
.dg{display:grid;grid-template-columns:1fr 30px 2.35fr 30px 1fr;align-items:stretch;gap:8px;margin-top:22px;flex:1;min-height:0;max-height:370px}
.dg .io{background:#fff;border:1px solid var(--line);border-radius:var(--r-l);padding:20px 20px;display:flex;flex-direction:column;justify-content:center}
.dark .dg .io{background:var(--navy-2);border-color:var(--line-d)}
.dg .k{font-family:var(--fm);font-size:10.5px;color:var(--blue);letter-spacing:.05em}
.dark .dg .k{color:var(--lemon)}
.dg .io h4{font-size:21px;font-weight:600;letter-spacing:-.02em;color:var(--ink);margin-top:8px;line-height:1.2}
.dark .dg .io h4{color:var(--oat)}
.dg .io p{font-size:14px;line-height:1.5;color:var(--mut);margin-top:7px}
.dark .dg .io p{color:var(--mut-d)}
.dg .ar{display:flex;align-items:center;justify-content:center;font-size:24px;color:var(--blue)}
.dark .dg .ar{color:var(--lemon)}
.dg .ag{background:linear-gradient(160deg,#0C1A38 0%,#16294F 100%);border-radius:var(--r-l);padding:20px 20px 18px;display:flex;flex-direction:column;gap:14px}
.dark .dg .ag{background:rgba(250,249,245,.08);border:1px solid var(--line-d)}
.dg .ag .k{color:var(--lemon)}
.dg .ag h4{font-size:22px;font-weight:600;letter-spacing:-.02em;color:var(--oat);margin-top:6px}
.dg .parts{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;flex:1;min-height:0}
.dg .pt{background:rgba(250,249,245,.08);border:1px solid rgba(250,249,245,.16);border-radius:var(--r-m);padding:16px 16px;display:flex;flex-direction:column;justify-content:center}
.dg .pt .ic{font-size:34px;line-height:1}
.dg .pt h5{font-size:20px;font-weight:600;color:var(--oat);margin-top:9px;letter-spacing:-.01em}
.dg .pt p{font-size:14px;line-height:1.45;color:var(--mut-d);margin-top:5px}
.dg .pt.on{background:var(--lemon);border-color:var(--lemon)}
.dg .pt.on h5,.dg .pt.on p{color:#06182D}
.dg.blank .io{border-style:dashed;border-width:1.5px;border-color:#C9D2DF}
.dg.blank .io p,.dg.blank .pt p{font-style:italic}
.dg.blank .pt{border-style:dashed}
.dg-sub{font-family:var(--fm);font-size:12px;color:var(--mut);margin-top:12px;text-align:center}
.dark .dg-sub{color:var(--mut-d)}
/* prompt largo */
.prompt.long{font-size:11.2px;line-height:1.52;padding:14px 20px;overflow:hidden}
.prompt.xl{font-size:10.6px;line-height:1.47}
/* boton de descarga en cualquier slide */
.dlrow{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px;margin-bottom:12px;flex:none}
.dlrow .dlbtn{margin-top:0}
.dlbtn.ghost{background:#fff;color:var(--ink);border:1px solid var(--line)}
.dlbtn.ghost:hover{background:var(--oat-2)}
.dark .dlbtn.ghost{background:rgba(250,249,245,.08);color:var(--oat);border-color:var(--line-d)}
.card .dlbtn{font-size:11.5px;padding:8px 16px;margin-top:14px}
/* agenda de 9 filas */
.rows.dense .row{padding:6px 18px}
.rows.dense .rt{font-size:14px}
.rows.dense .rd{font-size:12.5px}
.row.pausa{background:var(--oat-2);border-style:dashed}
"""

# --------------------------------------------------------------- estado ---
SLIDES = []
_DECK = {}


def start(bloque, seccion_pie):
    """Reinicia el deck. `bloque` va en la cabecera, `seccion_pie` en el pie."""
    SLIDES.clear()
    _DECK["bloque"] = bloque
    _DECK["pie"] = seccion_pie


# -------------------------------------------------------------- helpers ---
def top(meta):
    return ('<div class="top anim"><div class="plate">'
            '<img src="%s" class="mw" alt="MyWorkIn">%s</div>'
            '<span class="tmeta">%s</span></div>' % (LOGO_MW, logo_em(), meta))


def foot(sec):
    pg = len(SLIDES) + 1
    return ('<div class="foot anim"><span>%s</span>'
            '<span>%s &nbsp;·&nbsp; <span class="pg">%02d</span></span></div>'
            % (PROGRAMA, sec, pg))


def eyebrow(ac, rest):
    return '<div class="eyebrow anim"><span class="ac">%s</span> — %s</div>' % (ac, rest)


def h1(txt, style=""):
    st_ = ' style="%s"' % style if style else ""
    return '<h1 class="t anim"%s>%s</h1>' % (st_, txt)


def sub(txt):
    return '<p class="sub anim">%s</p>' % txt


def rule(k, txt, style=""):
    st_ = ' style="%s"' % style if style else ""
    return '<div class="rule anim"%s><span class="k">%s</span><p>%s</p></div>' % (st_, k, txt)


def mcell(k, v, unit=""):
    u = '<span>%s</span>' % unit if unit else ""
    return ('<div class="mcell"><div class="k">%s</div>'
            '<div class="v">%s%s</div></div>' % (k, v, u))


def mrow(cells, tight=True, style=""):
    cls = "mrow tight anim" if tight else "mrow anim"
    st_ = ' style="%s"' % style if style else ""
    return '<div class="%s"%s>%s</div>' % (cls, st_, "".join(cells))


def card(bar, tag, h3, body, cls=""):
    return ('<div class="card%s"><span class="bar %s"></span><span class="tag">%s</span>'
            '<h3>%s</h3>%s</div>' % ((" " + cls) if cls else "", bar, tag, h3, body))


def p(txt):
    return "<p>%s</p>" % txt


def lst(items):
    return '<ul class="lst">%s</ul>' % "".join("<li>%s</li>" % i for i in items)


def grid(n, cards, style=""):
    st_ = ' style="%s"' % style if style else ""
    return '<div class="grid%d anim"%s>%s</div>' % (n, st_, "".join(cards))


def gcard(bdg, num, h4_, txt=""):
    return ('<div class="gcard"><span class="bdg %s">%s</span><h4>%s</h4>%s</div>'
            % (bdg, num, h4_, ("<p>%s</p>" % txt) if txt else ""))


def gwrap(cards, c3=False, style="", tight=False):
    cls = "gwrap c3 anim" if c3 else "gwrap anim"
    if tight:
        cls += " tight"
    st_ = ' style="%s"' % style if style else ""
    return '<div class="%s"%s>%s</div>' % (cls, st_, "".join(cards))


def st(n, h4_, txt=""):
    return ('<div class="st"><span class="num">%s</span><div><h4>%s</h4>%s</div></div>'
            % (n, h4_, ("<p>%s</p>" % txt) if txt else ""))


def steps(items, sm=True, style=""):
    cls = "steps sm anim" if sm else "steps anim"
    st_ = ' style="%s"' % style if style else ""
    return '<div class="%s"%s>%s</div>' % (cls, st_, "".join(items))


def bl(items, style=""):
    st_ = ' style="%s"' % style if style else ""
    body = "".join('<div class="bi"><span class="n">%02d</span><p>%s</p></div>' % (i + 1, t)
                   for i, t in enumerate(items))
    return '<div class="bl sm anim"%s>%s</div>' % (st_, body)


def note(k, txt):
    return '<div class="note anim"><span class="k">%s</span><p>%s</p></div>' % (k, txt)


def prompt(label, txt):
    return ('<div class="prompt anim"><span class="pl">%s</span>'
            '<button class="cp" onclick="copyPrompt(event,this)">Copiar</button>'
            '<button class="dp" onclick="dlPrompt(event,this)">&#8681; Descargar</button>'
            '<span class="ptxt">%s</span></div>' % (label, txt))


def agenda(rows, now=None):
    """rows: [(minutos, titulo, detalle)]. `now` = indice del bloque actual."""
    out = []
    for i, (mins, t, d) in enumerate(rows):
        cls = "row now" if i == now else "row"
        out.append('<div class="%s"><span class="rn">%02d</span><span class="rt">%s</span>'
                   '<span class="rd">%s</span><span class="rm">%s</span></div>'
                   % (cls, i + 1, t, d, mins))
    return '<div class="rows anim">%s</div>' % "".join(out)


def case(problema, solucion, meta_, who, descarga=None, k3="QUÉ MEJORA SI SE RESUELVE"):
    # el clic no debe llegar al stage, que lo tomaria como "siguiente slide"
    btn = ('<a class="dlbtn" href="%s" target="_blank" rel="noopener" '
           'onclick="event.stopPropagation()"><span class="ic">&#8681;</span> Descargar material</a>'
           % descarga) if descarga else ""
    return ('<div class="case anim"><div class="cbox"><span class="k">EL PROBLEMA</span>'
            '<p>%s</p><span class="k">LO QUE QUIEREN CONSTRUIR</span><p>%s</p></div>'
            '<div class="cbox"><span class="k">%s</span><p>%s</p>'
            '<span class="who">%s</span>%s</div></div>' % (problema, solucion, k3, meta_, who, btn))


# ------------------------------------------------------- sesion 2 extras ---
def diagram(entrada, salida, partes, agente=("AGENTE DE IA", "Recibe, decide y responde"),
            blank=False, on=None, pie="Un asistente que piensa, recuerda y actúa"):
    """entrada/salida: (k, titulo, texto). partes: [(icono, nombre, texto)] x3.
    `on` resalta una de las tres piezas (0, 1, 2)."""
    def io(k, t, x):
        return '<div class="io"><span class="k">%s</span><h4>%s</h4>%s</div>' % (
            k, t, ("<p>%s</p>" % x) if x else "")
    pts = "".join('<div class="pt%s"><span class="ic">%s</span><h5>%s</h5><p>%s</p></div>'
                  % (" on" if i == on else "", ic, n, x) for i, (ic, n, x) in enumerate(partes))
    ag = ('<div class="ag"><div><span class="k">%s</span><h4>%s</h4></div>'
          '<div class="parts">%s</div></div>' % (agente[0], agente[1], pts))
    out = ('<div class="dg%s anim">%s<div class="ar">&#8594;</div>%s<div class="ar">&#8594;</div>%s</div>'
           % (" blank" if blank else "", io(*entrada), ag, io(*salida)))
    if pie:
        out += '<div class="dg-sub anim">%s</div>' % pie
    return out


def br(txt):
    """Texto con saltos de linea reales -> HTML con <br> (para bloques de prompt)."""
    import html as _h
    return "<br>".join(_h.escape(l, quote=False) for l in txt.split("\n"))


def prompt_long(label, txt, xl=False):
    cls = "prompt long xl anim" if xl else "prompt long anim"
    return ('<div class="%s"><span class="pl">%s</span>'
            '<button class="cp" onclick="copyPrompt(event,this)">Copiar</button>'
            '<button class="dp" onclick="dlPrompt(event,this)">&#8681; Descargar</button>'
            '<span class="ptxt">%s</span></div>' % (cls, label, br(txt)))


def dl(href, label, ghost=False):
    return ('<a class="dlbtn%s" href="%s" download onclick="event.stopPropagation()">'
            '<span class="ic">&#8681;</span> %s</a>' % (" ghost" if ghost else "", href, label))


def dlrow(btns):
    return '<div class="dlrow anim">%s</div>' % "".join(btns)


def agenda2(rows, now=None):
    """Como agenda() pero admite filas de pausa (titulo que empieza con 'Pausa')."""
    out = []
    n = 0
    for i, (mins, t, d) in enumerate(rows):
        pausa = t.startswith("Pausa")
        cls = "row" + (" now" if i == now else "") + (" pausa" if pausa else "")
        if not pausa:
            n += 1
        out.append('<div class="%s"><span class="rn">%s</span><span class="rt">%s</span>'
                   '<span class="rd">%s</span><span class="rm">%s</span></div>'
                   % (cls, "··" if pausa else "%02d" % n, t, d, mins))
    return '<div class="rows dense anim">%s</div>' % "".join(out)


IMGS = {}


def img(name):
    if name not in IMGS:
        IMGS[name] = datauri(os.path.join(ASSETS, name))
    return IMGS[name]


# --------------------------------------------------------------- slides ---
def slide(meta, blocks, dark=False):
    cls = "slide dark" if dark else "slide"
    SLIDES.append('<section class="%s"><div class="pad">\n%s\n<div class="body">\n%s\n</div></div></section>'
                  % (cls, top(meta), "\n".join(blocks + [foot(_DECK["pie"])])))


def cover(num, titulo, bajada, celdas):
    SLIDES.append(
        '<section class="slide"><div class="pad cover">\n'
        + top("Bloque %s · %s" % (num, _DECK["bloque"]))
        + '\n<div class="body" style="justify-content:center">\n'
        + eyebrow("Bloque %s de 11" % num, "Sesión 1 · Fundamentos de IA y entornos de Claude")
        + '\n<h1 class="anim" style="margin-top:18px">%s</h1>\n' % titulo
        + sub(bajada)
        + '\n' + mrow(celdas, tight=False)
        + '\n<div class="who anim"><span class="n">Santiago Franco</span>'
          '<span class="r">CTO · MyWorkIn</span></div>\n</div></div></section>')


def quote(meta, big, frase, center=False):
    """Slide oscuro de una sola frase: sin pie, como en Interbank. `center` la centra en la slide."""
    SLIDES.append(
        '<section class="slide dark"><div class="pad">\n' + top(meta)
        + '\n<div class="body dv quote%s">\n<div class="big anim">%s</div>\n' % (" center" if center else "", big)
        + '<h1 class="anim">%s</h1>\n</div></div></section>' % frase)


def demo_slide(meta, col_left, image, alt):
    SLIDES.append(
        '<section class="slide dark"><div class="pad">\n' + top(meta)
        + '\n<div class="body" style="padding-top:16px">\n<div class="demo wide">\n<div class="col-l">\n'
        + "\n".join(col_left)
        + '\n</div>\n<div class="shot anim"><img src="%s" alt="%s"></div>\n</div>\n' % (img(image), alt)
        + foot(_DECK["pie"]) + '\n</div></div></section>')



def qr_slide(meta, image, alt):
    """Slide final con solo un QR centrado sobre una tarjeta blanca."""
    SLIDES.append(
        '<section class="slide dark"><div class="pad">\n' + top(meta)
        + '\n<div class="body" style="align-items:center;justify-content:center">\n'
        + '<div class="anim" style="background:#fff;border-radius:28px;padding:28px;line-height:0">'
        + '<img src="%s" alt="%s" style="display:block;width:min(56vh,440px);height:auto;image-rendering:pixelated"></div>\n' % (img(image), alt)
        + '</div></div></section>')

def split(meta, eyebrow_, titulo, kick, items, extra=""):
    """Panel editorial: texto a la izquierda, lista numerada a la derecha."""
    pis = "".join('<div class="pi"><span class="n">%02d</span><div><div class="lab">%s</div>'
                  '<div class="txt">%s</div></div></div>' % (i + 1, lab, txt)
                  for i, (lab, txt) in enumerate(items))
    SLIDES.append(
        '<section class="slide"><div class="pad">\n' + top(meta)
        + '\n<div class="body">\n<div class="split anim"><div class="lft">'
        + '<div class="eyebrow"><span class="ac">%s</span> — %s</div>' % eyebrow_
        + '<h1 class="t">%s</h1><p class="kick">%s</p>%s' % (titulo, kick, extra)
        + '</div><div class="panel">%s</div></div>\n' % pis
        + foot(_DECK["pie"]) + '\n</div></div></section>')


# ---------------------------------------------------------------- build ---
NAV_JS = """
const els=[...document.querySelectorAll('.slide')];
document.getElementById('total').textContent=els.length;
let idx=0;
function show(n){
  n=Math.max(0,Math.min(els.length-1,n));
  els.forEach((s,i)=>s.classList.toggle('active',i===n));
  idx=n;
  document.getElementById('cur').textContent=n+1;
  document.getElementById('progress').style.width=((n+1)/els.length*100)+'%';
  els[n].querySelectorAll('.anim').forEach((el,k)=>{el.style.transitionDelay=(0.03+k*0.05)+'s'});
}
function copyPrompt(e,btn){
  e.stopPropagation();
  const txt=btn.parentElement.querySelector('.ptxt').innerText.trim();
  const done=()=>{btn.textContent='Copiado ✓';btn.classList.add('ok');
    setTimeout(()=>{btn.textContent='Copiar';btn.classList.remove('ok')},1800)};
  // file:// y navegadores viejos no siempre exponen la Clipboard API
  const legacy=()=>{const ta=document.createElement('textarea');ta.value=txt;
    ta.style.position='fixed';ta.style.opacity='0';document.body.appendChild(ta);ta.select();
    try{document.execCommand('copy');done()}finally{ta.remove()}};
  if(navigator.clipboard&&window.isSecureContext)navigator.clipboard.writeText(txt).then(done,legacy);
  else legacy();
}
function dlPrompt(e,btn){
  e.stopPropagation();
  const box=btn.parentElement, txt=box.querySelector('.ptxt').innerText.trim();
  const sl=box.closest('.slide'), h=sl&&sl.querySelector('h1');
  const name=('Prompt_'+(h?h.textContent:'SIP')).normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').replace(/[^A-Za-z0-9]+/g,'_').replace(/^_+|_+$/g,'').slice(0,60);
  const b=new Blob([String.fromCharCode(65279)+txt+String.fromCharCode(10)],{type:'text/plain;charset=utf-8'}),u=URL.createObjectURL(b),a=document.createElement('a');
  a.href=u;a.download=name+'.txt';document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(u),1500);
  btn.classList.add('ok');btn.textContent='Descargado ✓';setTimeout(()=>{btn.classList.remove('ok');btn.innerHTML='&#8681; Descargar'},1800);
}
function next(){show(idx+1)} function prev(){show(idx-1)}
document.getElementById('next').onclick=next;
document.getElementById('prev').onclick=prev;
document.addEventListener('keydown',e=>{
  if(['ArrowRight',' ','PageDown','Enter'].includes(e.key)){e.preventDefault();next()}
  else if(['ArrowLeft','PageUp'].includes(e.key)){e.preventDefault();prev()}
  else if(e.key==='Home')show(0); else if(e.key==='End')show(els.length-1);
  else if(e.key.toLowerCase()==='f'){if(!document.fullscreenElement)document.documentElement.requestFullscreen();else document.exitFullscreen()}
});
document.getElementById('stage').addEventListener('click',e=>{const r=e.currentTarget.getBoundingClientRect();if(e.clientX>r.left+r.width*0.5)next();else prev()});
function fit(){const s=Math.min(window.innerWidth/1280,window.innerHeight/720);document.getElementById('deck').style.transform=`scale(${s})`}
window.addEventListener('resize',fit);fit();
show(0);
"""

HTML = """<!doctype html>
<html lang="es"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>%(title)s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
%(css)s
</style></head><body>
<div class="progress" id="progress"></div>
<div class="hint"><a href="index.html">&#8592; &iacute;ndice</a> &middot; &#8592; &#8594; navegar &middot; F pantalla completa</div>
<div class="viewport"><div class="deck" id="deck"><div class="stage" id="stage">%(slides)s</div></div></div>
<div class="ctl"><a class="back" href="index.html">&#8592; Regresar</a><span class="div"></span><button id="prev">&#8249;</button><span class="count"><span id="cur">1</span> / <span id="total">1</span></span><button id="next">&#8250;</button></div>
<script>%(js)s</script></body></html>
"""


def write(filename, title):
    html_ = HTML % {"title": title, "css": BASE_CSS + EXT_CSS,
                    "slides": "".join(SLIDES), "js": NAV_JS}
    out = os.path.join(OUT_DIR, filename)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html_)
    print("%-38s slides: %2d  %7d bytes" % (filename, len(SLIDES), os.path.getsize(out)))
