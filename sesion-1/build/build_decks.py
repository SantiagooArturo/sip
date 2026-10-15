#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sesion 1 · Workshop · Fundamentos de IA y entornos de Claude · SIP (propuesta 2026-046).
Once decks, uno por bloque. Primero build_materiales.py (escribe esperados.json).
Por herramienta: 3 casos; los 2 primeros los hace el facilitador y el 3ro se hace en conjunto.
Uso:  python3 build_decks.py
"""
import json
import os

import contenido as C
import deck
from deck import (agenda2, bl, card, cover, demo_slide, diagram, dl, dlrow, eyebrow, gcard, grid, gwrap, h1, lst,
                  mcell, mrow, note, p, prompt, prompt_long, quote, rule, slide, start, st, steps, sub, write)

E = json.load(open(os.path.join(deck.HERE, "esperados.json"), encoding="utf-8"))
DL = E["rutas"]
TX, RC = E["tx"], E["rc"]
ARMADOR = ("https://firebasestorage.googleapis.com/v0/b/myworkin-b2c.firebasestorage.app/o/"
           "armador-de-prompts.skill?alt=media&amp;token=d8ede666-386c-4774-9aa4-56c22d808d7e")

AGENDA = [
    ("Contexto", "Apertura", "Qué está pasando con la IA y por qué importa"),
    ("Teoría", "Fundamentos", "LLM, contexto, modelos, alucinaciones y fecha de corte"),
    ("Reglas", "Uso responsable", "Qué se sube, qué no y quién responde"),
    ("Base", "Prompting", "Los 5 ingredientes, en 10 minutos"),
    ("3 casos", "Skills", "Recetas que se escriben una vez"),
    ("3 casos", "Conectores", "Claude dentro de Microsoft 365"),
    ("3 casos", "Projects", "El contexto que no se repite"),
    ("3 casos", "Research", "Investigar con fuentes"),
    ("3 casos", "Design", "De datos a una presentación"),
    ("Práctica", "Práctica guiada", "Tu Skill de correos con tu estilo"),
    ("Cierre", "Cierre", "Lo que armaste y la Sesión 2"),
]

FILES = [
    ("01_Apertura.html", "Apertura", "Contexto", "La adopción más rápida de la historia, el tráfico de bots, los despidos y equipos con agentes."),
    ("02_Fundamentos.html", "Fundamentos", "Teoría", "Qué es un LLM, ventana de contexto, modelos de Claude, alucinaciones y fecha de corte."),
    ("03_Uso_responsable.html", "Uso responsable", "Reglas", "Tú respondes por el resultado, el semáforo de datos y cómo anonimizar."),
    ("04_Prompting.html", "Prompting", "Base", "Los 5 ingredientes y la skill que arma el prompt por ti."),
    ("05_Skills.html", "Skills", "3 casos", "Respuesta a reclamos, conciliación de cashback y comunicado de mantenimiento."),
    ("06_Conectores.html", "Conectores", "3 casos", "Resumir un hilo, preparar una reunión y preguntarle a un documento."),
    ("07_Projects.html", "Projects", "3 casos", "Atención al cliente, reporte de transacciones y campañas."),
    ("08_Research.html", "Research", "3 casos", "Mercado de billeteras, regulación y beneficios de la competencia."),
    ("09_Design.html", "Design", "3 casos", "Resultados del mes, one-pager de campaña y reclamos del trimestre."),
    ("10_Practica_guiada.html", "Práctica guiada", "Práctica", "Cada uno crea una Skill que escribe correos con su estilo."),
    ("11_Cierre.html", "Cierre", "Cierre", "Lo que armaste hoy, la tarea y qué viene en la Sesión 2."),
]

deck.EXT_CSS += """
/* ---------- sip ---------- */
.rows.dense .row{padding:4px 18px}
.rows.dense .rt{font-size:13.5px}
.rows.dense .rd{font-size:12px}
.adop{display:flex;flex-direction:column;gap:14px;margin-top:28px}
.adop .r{display:grid;grid-template-columns:150px 1fr 96px;align-items:center;gap:14px}
.adop .r .n{font-weight:600;font-size:17px;color:var(--ink)}
.adop .r .tr{height:34px;background:#E9E7DF;border-radius:8px;overflow:hidden}
.adop .r .b{height:100%;background:#A9A59A;border-radius:8px}
.adop .r .v{font-family:var(--fm);font-size:13px;color:var(--mut);text-align:right}
.adop .r.hot .n,.adop .r.hot .v{color:var(--blue);font-weight:700}
.adop .r.hot .b{background:var(--blue);min-width:10px}
.org{display:flex;flex-direction:column;align-items:center;margin-top:18px;flex:1;min-height:0;justify-content:center}
.org .lvl{display:flex;gap:14px;justify-content:center}
.org .node{min-width:168px;padding:12px 16px;border-radius:14px;text-align:center;border:1px solid var(--line);background:#fff}
.org .node .k{font-family:var(--fm);font-size:10px;letter-spacing:.06em;color:var(--mut)}
.org .node b{display:block;font-size:15px;color:var(--ink);margin-top:4px}
.org .node.ai{background:#06182D;border-color:#06182D}
.org .node.ai .k{color:var(--lemon)}
.org .node.ai b{color:#fff}
.org .wire{width:2px;height:22px;background:#CFCBBF;margin:0 auto}
.org .bus{height:2px;background:#CFCBBF;width:78%;margin:0 auto}
.org .lvl.kids .col{display:flex;flex-direction:column;align-items:center}
.org .legend{display:flex;gap:18px;margin-top:16px;font-family:var(--fm);font-size:11px;color:var(--mut)}
.org .legend i{display:inline-block;width:10px;height:10px;border-radius:3px;margin-right:6px;vertical-align:-1px}
.modo{flex:none;height:auto;display:inline-flex;align-items:center;gap:7px;font-family:var(--fm);font-size:11px;border-radius:999px;padding:5px 12px;margin-bottom:10px;align-self:flex-start}
.modo.demo{background:rgba(56,89,249,.10);color:var(--blue)}
.modo.juntos{background:var(--lemon);color:#06182D;font-weight:500}
.cs{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-top:22px;flex:none;min-height:230px}
.cs .cb{background:#fff;border:1px solid var(--line);border-radius:var(--r-l);padding:22px 24px;display:flex;flex-direction:column}
.cs .cb .k{font-family:var(--fm);font-size:10.5px;letter-spacing:.05em;color:var(--blue)}
.cs .cb.hoy .k{color:#B3261E}
.cs .cb h4{font-size:17px;font-weight:600;color:var(--ink);margin-top:8px;letter-spacing:-.01em}
.cs .cb p{font-size:16px;line-height:1.55;color:var(--mut);margin-top:10px}
.cs .cb.clau{background:#06182D;border-color:#06182D}
.cs .cb.clau .k{color:var(--lemon)}
.cs .cb.clau h4{color:#fff}.cs .cb.clau p{color:#C9D3E0}
.mapa{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:24px;flex:none;min-height:250px}
.mapa .mc{background:#fff;border:1px solid var(--line);border-radius:var(--r-l);padding:20px 22px;display:flex;flex-direction:column}
.mapa .mc.juntos{border:2px solid var(--lemon);box-shadow:0 0 0 3px rgba(252,190,17,.18)}
.mapa .mc .n{font-family:var(--fm);font-size:11px;color:var(--mut)}
.mapa .mc h4{font-size:22px;font-weight:600;color:var(--ink);margin-top:8px;letter-spacing:-.015em}
.mapa .mc p{font-size:15.5px;line-height:1.5;color:var(--mut);margin-top:10px;flex:1}
.mapa .mc .who{font-family:var(--fm);font-size:11px;margin-top:12px}
"""


def titulo(i):
    return "%s · Workshop de IA con Claude · SIP" % FILES[i][1]


def soles(x):
    return "S/ {:,.2f}".format(x)


def modo(juntos):
    return ('<span class="modo juntos anim">&#9733; En conjunto: lo hacemos todos</span>' if juntos
            else '<span class="modo demo anim">&#9654; Demo: lo hago yo, tú miras</span>')


def mapa(casos):
    """casos: [(titulo, texto)] x3; el 3ro es en conjunto."""
    out = []
    for i, (t, x) in enumerate(casos):
        j = i == 2
        out.append('<div class="mc%s"><span class="n">CASO %d</span><h4>%s</h4><p>%s</p>'
                   '<span class="who">%s</span></div>' % (" juntos" if j else "", i + 1, t, x,
                                                        "&#9733; En conjunto" if j else "&#9654; Demo"))
    return '<div class="mapa anim">%s</div>' % "".join(out)


def caso(n, herramienta, titulo_, hoy, claude, objetivo, kitkey, juntos=False):
    slide("%s · Caso %d" % (herramienta, n), [
        eyebrow("Caso %d" % n, herramienta),
        modo(juntos),
        h1(titulo_, "font-size:36px;max-width:none"),
        '<div class="cs anim">'
        '<div class="cb hoy"><span class="k">HOY</span><p>%s</p></div>'
        '<div class="cb clau"><span class="k">CON CLAUDE</span><p>%s</p></div>'
        '<div class="cb"><span class="k">%s</span><p>%s</p></div></div>'
        % (hoy, claude, "LO QUE HACEMOS JUNTOS" if juntos else "QUÉ VAS A VER", objetivo),
        dlrow([dl(DL[kitkey], "Descargar el material del caso")]),
    ])


def caso_prompt(n, herramienta, titulo_, label, texto, kitkey, extra=None, juntos=False, pasos=None):
    blocks = [eyebrow("Caso %d" % n, herramienta + (" · ahora tú" if juntos else " · el pedido")), modo(juntos),
              h1(titulo_, "font-size:28px;max-width:none")]
    if pasos:
        blocks.append(steps([st(str(i + 1), a, b) for i, (a, b) in enumerate(pasos)], style="margin-top:4px"))
    blocks.append(prompt_long(label, texto))
    if extra:
        blocks.append(extra)
    blocks.append(dlrow([dl(DL[kitkey], "Descargar el material del caso")]))
    slide("%s · Caso %d · Prompt" % (herramienta, n), blocks)


# ================================================================ 01
def deck1():
    start("Apertura", "Apertura")
    cover("01", "Fundamentos de IA y entornos de Claude",
          "Sesión 1 del workshop para SIP: qué es la IA de verdad, cómo usarla con criterio y las herramientas de Claude, con casos de una billetera digital.",
          [mcell("Bloques", "11"), mcell("Casos", "15"), mcell("Para", "SIP")])
    slide("Sesión 1 · Agenda", [eyebrow("Agenda", "Sesión 1 · Workshop"), h1("Lo que vamos a ver hoy"),
                                agenda2(AGENDA, now=0)])
    slide("Cómo trabajamos", [
        eyebrow("Cómo trabajamos", "Tres casos por herramienta"),
        h1("Primero miras, después lo hacemos juntos"),
        grid(3, [
            card("blue", "Caso 1 y 2", "Demo", p("Los hago yo en pantalla. Tú miras y ves el resultado. El material queda en la slide por si quieres seguirme.")),
            card("lemon", "Caso 3", "En conjunto", p("Lo hacemos todos a la vez, con el material descargado. Ahí se levanta la mano.")),
            card("fruit", "En cada slide", "El material", p("Botón <b>Descargar</b> para el kit y botones <b>Copiar</b> y <b>Descargar</b> en cada prompt.")),
        ]),
        rule("Hoy", "Todo corre en <b>Claude en el navegador</b> (claude.ai). No hace falta instalar nada."),
    ])
    quote("Apertura · La idea", "La idea de hoy", "La IA no es solo una herramienta. Es una nueva capa de trabajo.")
    ADOP = [("Teléfono", 75 * 12, "75 años"), ("Televisión", 13 * 12, "13 años"), ("Internet", 7 * 12, "7 años"),
            ("Facebook", 54, "4.5 años"), ("Instagram", 30, "2.5 años"), ("ChatGPT", 2, "2 meses")]
    filas = "".join('<div class="r%s"><span class="n">%s</span><div class="tr"><div class="b" style="width:%.2f%%"></div></div>'
                    '<span class="v">%s</span></div>' % (" hot" if n == "ChatGPT" else "", n, m / 900 * 100, v) for n, m, v in ADOP)
    slide("Apertura · Adopción", [eyebrow("El estado de la IA", "Tiempo para llegar a 100 millones de usuarios"),
                                 h1("La adopción más rápida de la historia"), '<div class="adop anim">%s</div>' % filas,
                                 rule("La idea", "ChatGPT llegó a 100 millones de usuarios en <b>2 meses</b>. Internet tardó 7 años. "
                                      "<span style='color:var(--mut-d)'>Fuente: UBS / SimilarWeb vía Reuters (feb. 2023).</span>", "margin-top:20px")])
    demo_slide("Apertura · Tráfico", [eyebrow("El estado de la IA", "Dato de 2025"),
                                      h1("La mayoría de internet ya no es humano", "font-size:36px;max-width:16ch"),
                                      sub("Más de la mitad de lo que se pide en internet lo piden bots y agentes de IA."),
                                      mrow([mcell("Automatizado", "53", "%"), mcell("Humano", "47", "%")], style="margin-top:22px"),
                                      note("Fuente", "<b>Imperva / Thales, Bad Bot Report 2026</b>: tráfico web de 2025.")],
               "nbc_bots_traffic.png", "NBC News: el tráfico de bots superó al humano")
    demo_slide("Apertura · Despidos", [eyebrow("El estado de la IA", "EE. UU. · primer semestre 2026"),
                                       h1("La IA ya es la primera razón de despidos", "font-size:34px;max-width:16ch"),
                                       mrow([mcell("Despidos por IA · ene–jun 2026", "101,743"), mcell("Del total", "23", "%")], style="margin-top:20px"),
                                       note("Ojo", "Lo que desaparece son <b>tareas</b>; quien sabe delegarlas vale más. Fuente: Challenger, Gray &amp; Christmas.")],
               "cnn_ai_layoffs.png", "CNN: Record layoffs driven by AI")
    slide("Apertura · Equipos", [
        eyebrow("El estado de la IA", "Cómo se ve un equipo de una billetera digital"),
        h1("Personas y agentes en el mismo equipo"),
        '<div class="org anim"><div class="lvl"><div class="node"><span class="k">PERSONA</span><b>Jefe de canales digitales</b></div></div>'
        '<div class="wire"></div><div class="bus"></div><div class="lvl kids">'
        '<div class="col"><div class="wire"></div><div class="node"><span class="k">PERSONA</span><b>Analista de atención</b></div></div>'
        '<div class="col"><div class="wire"></div><div class="node ai"><span class="k">AGENTE IA</span><b>Borradores de reclamos</b></div></div>'
        '<div class="col"><div class="wire"></div><div class="node"><span class="k">PERSONA</span><b>Analista de marketing</b></div></div>'
        '<div class="col"><div class="wire"></div><div class="node ai"><span class="k">AGENTE IA</span><b>Reporte de transacciones</b></div></div>'
        '<div class="col"><div class="wire"></div><div class="node ai"><span class="k">AGENTE IA</span><b>Vigila a la competencia</b></div></div>'
        '</div><div class="legend"><span><i style="background:#fff;border:1px solid #ccc"></i>Persona</span>'
        '<span><i style="background:#06182D"></i>Agente de IA</span></div></div>',
        rule("La idea", "La IA no reemplaza el criterio: <b>lo amplifica</b>. Quien sabe dirigirla hace más, y mejor."),
    ])
    write(FILES[0][0], titulo(0))


# ================================================================ 02
def deck2():
    start("Fundamentos", "Fundamentos")
    cover("02", "Fundamentos sin humo", "Lo mínimo que tienes que saber para usar Claude con criterio, sin teoría pesada.",
          [mcell("Conceptos", "05"), mcell("Modelos", "03"), mcell("Jerga", "0")])
    slide("Fundamentos · LLM", [eyebrow("Qué es un LLM", "Modelo de lenguaje"), h1("Un modelo entrenado con enormes cantidades de texto"),
                               grid(3, [card("blue", "Cómo aprende", "Lee muchísimo texto", p("Libros, webs y documentos: aprende cómo se escribe y cómo se relacionan las ideas.")),
                                        card("lemon", "Cómo responde", "Predice la siguiente palabra", p("Escribe la palabra más probable, una tras otra. Por eso responde distinto cada vez.")),
                                        card("fruit", "Lo que NO es", "No es un buscador", p("No consulta una base de verdades. <b>Cuando no sabe, a veces adivina.</b>"))])])
    slide("Fundamentos · Contexto", [eyebrow("Tokens y ventana de contexto", "Cómo lee Claude"), h1("Lo que Claude tiene a la vista"),
                                    grid(2, [card("blue", "Token", "Un pedacito de texto", p("Más o menos tres cuartos de una palabra. Los límites de uso se miden en tokens.")),
                                             card("lemon", "Ventana de contexto", "Su memoria de trabajo", p("Tu pedido, sus respuestas y los archivos de esa conversación. Lo que no está ahí, no lo sabe."))]),
                                    rule("La regla", "Cuanto más contexto útil le das, <b>mejor responde</b>. Un chat muy largo también se satura: abre uno nuevo.")])
    slide("Fundamentos · Modelos", [eyebrow("Modelos", "En el selector, debajo de la caja de texto"), h1("Tres modelos, una sola lógica"),
                                   grid(3, [card("lemon", "Rápido", "Haiku", p("Tareas simples: resumir, reformatear, extraer un dato.")),
                                            card("blue", "Por defecto", "Sonnet", p("El del día a día. <b>Resuelve la gran mayoría</b> de los casos.")),
                                            card("fruit", "Potente", "Opus", p("Razonamiento largo, muchas reglas a la vez. Consume más de tu límite."))]),
                                   rule("Regla práctica", "Empieza en <b>Sonnet</b>. Sube a <b>Opus</b> solo si falló con un buen pedido. El <b>pensamiento extendido</b> razona más, pero tarda y consume más.")])
    slide("Fundamentos · Alucinaciones", [eyebrow("El riesgo principal", "Alucinaciones"), h1("Brillante y muy segura de cosas falsas"),
                                         grid(3, [card("blue", "Por qué pasa", "Predice, no verifica", p("Cuando no sabe, a veces adivina en lugar de decir «no sé».")),
                                                  card("lemon", "Dónde pasa más", "Datos exactos", p("Cifras, normas, tasas, nombres y todo lo reciente.")),
                                                  card("fruit", "Cómo te defiendes", "Pide la fuente", p("Pregúntale de dónde sacó el dato y qué no pudo confirmar."))])])
    demo_slide("Fundamentos · Fecha de corte", [eyebrow("Fecha de corte", "Lo que pasó después, no lo sabe"),
                                                h1("Cada modelo aprende hasta un mes", "font-size:36px;max-width:16ch"),
                                                steps([st("1", "Se entrena hasta una fecha", "Lo posterior no está en su memoria."),
                                                       st("2", "Si lo obligas, puede inventar", "Aquí Claude reconoce su límite."),
                                                       st("3", "La búsqueda web lo resuelve", "Busca en el momento y cita la fuente.")], style="margin-top:18px"),
                                                note("Regla", "Si el dato <b>puede haber cambiado</b> (tasas, normas, promociones), que busque en la web.")],
               "claude_training_cutoff.png", "Claude reconociendo su fecha de corte")
    quote("Fundamentos · Regla", "Regla práctica", "La IA ayuda. Tú validas.")
    write(FILES[1][0], titulo(1))


# ================================================================ 03
def deck3():
    start("Uso responsable", "Uso responsable")
    cover("03", "Uso responsable", "En una billetera digital, los datos de los clientes son lo más delicado. Qué se sube, qué no y quién responde.",
          [mcell("Colores", "04"), mcell("Pasos para anonimizar", "04"), mcell("Responsable", "Tú")])
    quote("Uso responsable · Tú firmas", "Lo primero", "Tú firmas todo lo que hace la IA. Si se equivoca, el responsable eres tú.")
    slide("Uso responsable · Semáforo", [
        eyebrow("Semáforo de datos", "Antes de pegar o subir algo, ubícalo"), h1("¿Qué se puede subir a Claude?"),
        grid(2, [card("blue", "Verde y amarillo", "Sí, en la cuenta de la empresa",
                      lst(["Información pública: web, tarifario publicado, noticias", "Procedimientos, plantillas y reportes <b>sin nombres</b>"])),
                 card("fruit", "Rojo y negro", "No, o solo anonimizado",
                      lst(["Nombre, DNI, celular o correo de clientes", "Números de tarjeta, CVV, claves y códigos",
                           "Saldos o movimientos de una persona identificable"]))]),
        rule("La regla simple", "¿Lo enviarías por correo a alguien de fuera de la empresa? <b>Si no, no lo pegues.</b>"),
    ])
    slide("Uso responsable · Anonimizar", [
        eyebrow("Anonimización", "Tu dataset tiene datos personales"), h1("Cambia a cada cliente por un ID"),
        steps([st("1", "Haz una copia en Excel, antes de abrir Claude", "Reemplaza nombre y DNI por C-001, C-002… El original no se sube."),
               st("2", "Guarda la llave en tu computadora", "La tabla ID ↔ nombre ↔ DNI. Nunca se sube."),
               st("3", "Sube la copia y pide el análisis", "Claude responde con IDs: «los clientes con más reclamos son C-014 y C-027»."),
               st("4", "Relaciona los IDs con la llave", "Con BUSCARV recuperas el nombre y armas tu entregable.")]),
        rule("Prioridad", "Si el análisis no necesita saber <b>quién</b> es el cliente, no se lo des."),
    ])
    slide("Uso responsable · Qué no se delega", [
        eyebrow("Humano en el circuito", "No todo se revisa igual"), h1("Qué se automatiza y qué no"),
        grid(3, [card("blue", "Automatiza", "Bajo riesgo", p("Resumir, ordenar, dar formato, primeros borradores.")),
                 card("lemon", "Con revisión", "Sale hacia afuera", p("Respuestas a clientes, reportes a la gerencia, comunicados.")),
                 card("fruit", "Nunca se delega", "Dinero o personas", p("Aprobar una devolución, decidir un bloqueo, temas regulatorios."))]),
    ])
    write(FILES[2][0], titulo(2))


# ================================================================ 04
def deck4():
    start("Prompting", "Prompting")
    cover("04", "Prompting", "Cinco ingredientes y una skill que te pregunta lo que falta.",
          [mcell("Ingredientes", "05"), mcell("Skill", "01"), mcell("Minutos", "10")])
    slide("Prompting · 5 ingredientes", [
        eyebrow("Prompting", "Cómo pedir bien"), h1("Los 5 ingredientes de un buen pedido"),
        steps([st("1", "Rol", "Quién quieres que sea. «Eres analista de atención al cliente de una billetera digital.»"),
               st("2", "Contexto", "Qué necesita saber: para quién es, de dónde salen los datos."),
               st("3", "Tarea", "Qué tiene que hacer, en concreto."),
               st("4", "Formato", "Cómo lo quieres: tabla, correo, máximo N palabras."),
               st("5", "Criterio de éxito", "Cuándo está bien hecho. «Si falta un dato, pregúntame.»")]),
        dlrow([dl(ARMADOR, "Descargar la skill armador de prompts")]),
    ])
    slide("Prompting · Ejemplo", [
        eyebrow("Prompting", "El mismo pedido, bien escrito"), h1("Así se ve con los 5 ingredientes", "font-size:30px;max-width:none"),
        prompt_long("EJEMPLO · PÉGALO EN UN CHAT NUEVO",
                    "Rol: eres analista de atención al cliente de una billetera digital peruana.\n"
                    "Contexto: este mes subieron los reclamos por cashback no abonado. El texto va en la app, en la sección de ayuda.\n"
                    "Tarea: escribe un mensaje que explique en cuánto tiempo se refleja el cashback y qué hacer si no aparece.\n"
                    "Formato: máximo 80 palabras, 3 viñetas y un título corto.\n"
                    "Criterio de éxito: lenguaje simple, sin prometer plazos que no te di. Si necesitas un plazo, pregúntamelo."),
        rule("Atajo", "La skill <b>armador de prompts</b> convierte un pedido vago en uno así: te pregunta lo que falta.", "margin-top:14px"),
        dlrow([dl(ARMADOR, "Descargar la skill armador de prompts")]),
    ])
    write(FILES[3][0], titulo(3))


# ================================================================ 05 skills
def deck5():
    H = "Skills"
    start(H, H)
    cover("05", "Skills", "Una receta que escribes una vez y Claude sigue siempre igual. Tres casos del día a día de SIP.",
          [mcell("Casos", "03"), mcell("Demo", "02"), mcell("En conjunto", "01")])
    slide("Skills · Qué es", [eyebrow("Qué es una Skill", "La receta que no se reescribe"), h1("Una Skill: la tarea, siempre igual"),
                             grid(3, [card("blue", "Qué es", "Un paso a paso con reglas", p("Pasos, formato de salida y lo que nunca debe hacer.")),
                                      card("lemon", "Cuándo se activa", "Sola, cuando la necesitas", p("Claude la usa cuando el pedido calza con su descripción.")),
                                      card("fruit", "Para quién", "Todo el equipo", p("Se comparte: todos responden con el mismo estándar."))]),
                             rule("Cuándo hacer una", "Cuando la tarea <b>se repite, tiene formato fijo</b> y hoy la haces desde cero.")])
    slide("Skills · Señales", [eyebrow("¿Necesitas una Skill?", "Las señales"), h1("Si respondes «sí» a dos, hazla Skill"),
                              gwrap([gcard("b1", "01", "¿Se repite?", "La haces cada semana o cada mes, siempre parecida."),
                                     gcard("b2", "02", "¿Siempre empiezas de cero?", "Abres un chat nuevo y vuelves a explicar todo."),
                                     gcard("b3", "03", "¿Tiene un formato fijo?", "Misma estructura: solo cambian algunos datos."),
                                     gcard("b4", "04", "¿Le pegas el mismo prompt largo?", "Lo tienes guardado en un bloc de notas."),
                                     gcard("b1", "05", "¿Cada persona lo hace distinto?", "Y el resultado cambia según quién lo hizo."),
                                     gcard("b2", "06", "¿Hay reglas que no se pueden olvidar?", "Lo que nunca se promete, lo que siempre se revisa.")],
                                    c3=True, tight=True)])
    slide("Skills · Cómo se instala", [eyebrow("En el navegador", "Cómo se sube una Skill"), h1("Tres pasos en claude.ai"),
                                      steps([st("1", "Configuración > Capacidades", "Verifica que la ejecución de código esté activa."),
                                             st("2", "Skills > Subir skill", "Eliges el .zip del kit. Adentro va su archivo SKILL.md: no lo abras ni lo cambies."),
                                             st("3", "Abre un chat nuevo y pídela", "«Usa la skill respuesta-a-reclamos con este reclamo…»")], sm=False),
                                      note("Ojo", "Si no ves la opción de subir Skills, la habilita TI. En la Sesión 2 creamos las tuyas.")])
    slide("Skills · Los 3 casos", [eyebrow("Skills", "Tres casos"), h1("Lo que vamos a hacer"),
                                  mapa([("Respuesta a reclamos", "Un reclamo pegado → la respuesta con la estructura y el tono de atención."),
                                        ("Conciliación de cashback", "Dos Excel de OneDrive → las diferencias entre lo que se debía abonar y lo que se abonó."),
                                        ("Comunicado de mantenimiento", "Un documento con formato fijo → solo cambian la fecha, el horario y los servicios.")])])
    caso(1, H, "Respuesta a reclamos",
         "Cada respuesta se escribe desde cero: el tono y la estructura cambian según quién la escriba.",
         "La Skill aplica siempre la misma estructura, tutea, no promete devoluciones y no pide claves.",
         "Subo la Skill, le paso 3 reclamos (cashback, cobro no reconocido y transferencia) y comparamos las respuestas.", "sk1")
    caso_prompt(1, H, "Pídele la respuesta", "PROMPT · CASO 1",
                "Usa la skill respuesta-a-reclamos para responder este reclamo:\n\n" + C.RECLAMOS_PRUEBA.split("\n\n")[0], "sk1")
    k = E["conc"]
    caso(2, H, "Conciliación de cashback con dos archivos de OneDrive",
         "Cada quincena se cruzan a mano dos Excel: las compras que debían recibir cashback y el cashback abonado.",
         "La Skill abre los dos archivos de la carpeta «%s» con el conector de Microsoft 365, los cruza por ID y lista cada diferencia." % C.CARPETA_ONEDRIVE,
         "Lo corro con los archivos de mi OneDrive. Tienen diferencias a propósito: compras sin abono, montos distintos, un duplicado y abonos sin compra.", "sk2")
    caso_prompt(2, H, "Pídele la conciliación", "PROMPT · CASO 2",
                "Usa la skill conciliacion-de-cashback para conciliar el cashback de la primera quincena de octubre.", "sk2",
                pasos=[("Los dos Excel están en OneDrive, en la carpeta «%s»" % C.CARPETA_ONEDRIVE, "La Skill sabe dónde buscarlos: no hay que adjuntarlos."),
                       ("El conector de Microsoft 365 tiene que estar activo", "Claude solo lee los archivos: no los modifica.")],
                extra=mrow([mcell("Esperado", soles(k["esperado"])), mcell("Abonado", soles(k["abonado"])),
                            mcell("Sin abono", "%02d" % len(k["sin_abono"])), mcell("Monto distinto", "%02d" % len(k["monto_distinto"]))],
                           style="margin-top:12px"))
    caso(3, H, "Comunicado de mantenimiento programado",
         "Cada comunicado se copia del anterior y se cambian los datos a mano: a veces queda una fecha vieja.",
         "La Skill tiene el texto fijo y solo completa los campos: fecha, horario, servicios y canal alternativo. Si falta uno, lo pregunta.",
         "Cada uno sube la Skill, genera el comunicado con la prueba 1 y después prueba la 2, a la que le falta un dato.", "sk3", juntos=True)
    caso_prompt(3, H, "Ahora tú: genera el comunicado", "PROMPT · CASO 3",
                "Usa la skill comunicado-de-mantenimiento con estos datos:\n\n" + C.DATOS_COMUNICADO.split("\n\n")[1], "sk3", juntos=True,
                pasos=[("Descarga el kit y sube comunicado-de-mantenimiento.zip", "Configuración > Capacidades > Skills."),
                       ("Pega el prompt y revisa el Word", "Luego prueba la PRUEBA 2 del kit: debe preguntarte la hora de fin.")])
    write(FILES[4][0], titulo(4))


# ================================================================ 06 conectores
def deck6():
    H = "Conectores"
    start(H, H)
    cover("06", "Conectores", "Claude trabajando sobre tu correo, tu calendario y tus archivos de Microsoft 365, sin descargar nada.",
          [mcell("Casos", "03"), mcell("Suite", "M365"), mcell("Configuración", "Sesión 2")])
    slide("Conectores · Qué son", [eyebrow("Qué es un conector", "Claude dentro de tus apps"), h1("Outlook, calendario y OneDrive"),
                                  grid(3, [card("blue", "Outlook", "Tu bandeja", p("Resume hilos, encuentra lo pendiente y prepara borradores.")),
                                           card("lemon", "Calendario", "Tu semana", p("Qué reuniones tienes y qué llevar a cada una.")),
                                           card("fruit", "OneDrive", "Tus archivos", p("Busca un documento y responde sobre él, citando dónde."))]),
                                  rule("Permisos", "Claude solo ve <b>lo que tu cuenta ya puede ver</b>. Y tú decides qué se envía.")])
    slide("Conectores · Antes de empezar", [eyebrow("Importante", "Lo habilita TI"), h1("Si no lo ves, todavía no está habilitado"),
                                           steps([st("1", "TI de SIP lo habilita", "Para toda la organización, en el plan de Claude."),
                                                  st("2", "Tú lo conectas", "Configuración > Conectores > Microsoft 365, con tu cuenta corporativa."),
                                                  st("3", "Hoy lo vemos; en la Sesión 2 lo configuramos juntos", "Si ya lo tienes activo, haz el caso 3 conmigo.")], sm=False),
                                           dlrow([dl(DL["co1"], "Descargar cómo activar el conector", ghost=True)])])
    slide("Conectores · Los 3 casos", [eyebrow("Conectores", "Tres casos"), h1("Lo que vamos a hacer"),
                                      mapa([("Resumir un hilo", "El hilo más reciente sobre un tema → 5 viñetas y un borrador de respuesta."),
                                            ("Preparar mi reunión", "Mi calendario de mañana → con quién, qué correos y qué llevar."),
                                            ("Preguntarle a un documento", "Un archivo de OneDrive → la respuesta y dónde está.")])])
    caso(1, H, "Resumir un hilo y proponer la respuesta", "Un hilo de 20 correos sobre una campaña: hay que leerlo entero para saber qué falta.",
         "Claude lo encuentra, lo resume en 5 viñetas y deja un borrador. No envía nada.", "Lo hago con mi bandeja: el resumen, el borrador y cómo verifico que usó el hilo correcto.", "co1")
    caso_prompt(1, H, "El pedido", "PROMPT · CASO 1", C.PROMPT_HILO, "co1")
    caso(2, H, "Preparar mi reunión de mañana", "Antes de cada reunión buscas a mano los correos y documentos relacionados.",
         "Claude cruza calendario, correo y OneDrive y te da qué llevar a cada reunión.", "Lo hago con mi calendario de mañana.", "co2")
    caso_prompt(2, H, "El pedido", "PROMPT · CASO 2", C.PROMPT_REUNION, "co2")
    caso(3, H, "Preguntarle a un documento de OneDrive", "Un procedimiento de 30 páginas: encontrar una respuesta toma tiempo.",
         "Claude busca el documento, responde la pregunta y dice en qué sección está.",
         "Quienes ya tengan el conector activo lo hacen conmigo; el resto lo ve y lo repite en la Sesión 2.", "co3", juntos=True)
    caso_prompt(3, H, "Ahora tú: pregúntale a tu documento", "PROMPT · CASO 3", C.PROMPT_ONEDRIVE, "co3", juntos=True,
                pasos=[("Verifica que el conector esté activo", "Menú de herramientas del chat."),
                       ("Cambia lo que está entre corchetes", "Un tema y una pregunta de tu área.")])
    write(FILES[5][0], titulo(5))


# ================================================================ 07 projects
def deck7():
    H = "Projects"
    start(H, H)
    cover("07", "Projects", "La carpeta donde Claude ya sabe de qué se trata: instrucciones fijas y tus documentos. Aquí se juntan las piezas.",
          [mcell("Casos", "03"), mcell("Piezas", "02"), mcell("Repeticiones", "0")])
    slide("Projects · Qué es", [eyebrow("Qué es un Project", "El contexto que no se repite"), h1("Cada chat adentro ya llega sabiendo"),
                               grid(2, [card("blue", "Instrucciones", "Quién es y cómo responde", lst(["Rol y área", "Formato y tono", "Lo que nunca hace"])),
                                        card("lemon", "Documentos", "Lo que tiene que saber", lst(["Productos, procesos, glosario", "Reportes y datos (anonimizados)", "Ejemplos de trabajos bien hechos"]))]),
                               rule("Con lo que ya viste", "Un Project usa tus <b>Skills</b> y tus <b>conectores</b>: es donde se junta todo.")])
    slide("Projects · Los 3 casos", [eyebrow("Projects", "Tres casos"), h1("Lo que vamos a hacer"),
                                    mapa([("Atención al cliente", "Productos, preguntas frecuentes y guía de respuesta → respuestas consistentes."),
                                          ("Reporte de transacciones", "El Excel del mes → análisis con cifras rastreables."),
                                          ("Campañas y comunicación", "Voz de marca, calendario y resultados → ideas y copies que no chocan.")])])
    caso(1, H, "Atención al cliente", "Cada analista responde con lo que recuerda de los productos y las condiciones.",
         "Un Project con productos, preguntas frecuentes y guía de respuesta: responde igual para todos y cita el documento.",
         "Lo creo en vivo y lo pruebo con 5 preguntas; la última es trampa: el dato no está.", "pr1")
    caso_prompt(1, H, "Las instrucciones del Project", "INSTRUCCIONES · CASO 1", C.P1_INSTR, "pr1")
    t = TX
    caso(2, H, "Reporte de transacciones del mes", "El reporte mensual se arma a mano con tablas dinámicas y se demora días.",
         "Un Project con el Excel del mes y su diccionario: responde con cifras que se pueden rastrear.",
         "Le pido el resumen del mes y lo comparo con los resultados esperados.", "pr2")
    caso_prompt(2, H, "Las instrucciones del Project", "INSTRUCCIONES · CASO 2", C.P2_INSTR, "pr2",
                extra=mrow([mcell("Transacciones", "%d" % t["filas"]), mcell("Monto", soles(t["monto"])),
                            mcell("Cashback", soles(t["cashback"]))], style="margin-top:14px"))
    caso(3, H, "Campañas y comunicación", "Las ideas de campaña se proponen sin mirar el calendario ni los resultados anteriores.",
         "Un Project con la voz de Sip, el calendario del trimestre y los resultados: propone sin chocar y evalúa con datos.",
         "Cada uno crea el Project, sube los 3 documentos y prueba los 4 pedidos.", "pr3", juntos=True)
    caso_prompt(3, H, "Ahora tú: crea el Project de Marketing", "INSTRUCCIONES · CASO 3", C.P3_INSTR, "pr3", juntos=True,
                pasos=[("Projects > Nuevo proyecto: «Marketing · Sip»", "Pega estas instrucciones."),
                       ("Sube los 3 documentos del kit y prueba los pedidos", "El 4 es trampa: debe decir que no hay dato.")])
    write(FILES[6][0], titulo(6))


# ================================================================ 08 research
def deck8():
    H = "Research"
    start(H, H)
    cover("08", "Research", "Investigación con fuentes: Claude revisa decenas de páginas y te entrega un informe que puedes verificar.",
          [mcell("Casos", "03"), mcell("Fuentes", "Siempre"), mcell("Sin fuente", "No entra")])
    slide("Research · Qué es", [eyebrow("Research", "Búsqueda web vs. investigación"), h1("Dos formas de traer datos de hoy"),
                               grid(2, [card("blue", "Búsqueda web", "El dato puntual", p("Una tasa, una noticia, una norma vigente. Responde en segundos y cita el enlace.")),
                                        card("lemon", "Research", "El informe", p("Revisa muchas fuentes, compara y entrega un informe. Tarda minutos."))]),
                               rule("La condición", "Fuente y fecha en cada dato. <b>Lo que no tiene fuente, no se usa.</b>")])
    slide("Research · Los 3 casos", [eyebrow("Research", "Tres casos"), h1("Lo que vamos a hacer"),
                                    mapa([("Mercado de billeteras", "Quiénes son, cuántos usuarios y qué tendencias, con fuente."),
                                          ("Regulación", "Qué exigen BCRP y SBS a una billetera, vigente vs. en consulta."),
                                          ("Beneficios de la competencia", "Cashback, promociones y costos frente a Sip.")])])
    caso(1, H, "El mercado de billeteras digitales", "Armar un panorama del mercado toma días de buscar reportes y notas.",
         "Research arma el resumen ejecutivo con una tabla de billeteras, cada dato con fuente y fecha.", "Lo lanzo en vivo y abro 2 fuentes al azar.", "re1")
    caso_prompt(1, H, "El pedido", "PROMPT · CASO 1", C.PROMPT_R1, "re1")
    caso(2, H, "Qué exige la regulación", "Las normas cambian y es fácil quedarse con una versión vieja.",
         "Research lista norma, entidad, fecha y qué exige, separando lo vigente de lo anunciado.", "Lo lanzo y revisamos qué no pudo confirmar.", "re2")
    caso_prompt(2, H, "El pedido", "PROMPT · CASO 2", C.PROMPT_R2, "re2")
    caso(3, H, "Beneficios de la competencia", "Comparar cashback y promociones de la competencia se hace web por web.",
         "Research arma la tabla comparativa y 3 conclusiones sobre dónde se diferencia Sip.", "Cada uno lo lanza y verifica con el checklist.", "re3", juntos=True)
    caso_prompt(3, H, "Ahora tú: lanza la investigación", "PROMPT · CASO 3", C.PROMPT_R3, "re3", juntos=True,
                pasos=[("Activa Research en un chat nuevo y pega el prompt", "Mientras investiga, verás las fuentes que revisa."),
                       ("Verifica con el checklist del kit", "Abre 2 enlaces: ¿dicen lo que la tabla dice?")])
    write(FILES[7][0], titulo(7))


# ================================================================ 09 design
def deck9():
    H = "Design"
    start(H, H)
    cover("09", "Claude Design", "De un Excel o un brief a una presentación con la identidad de Sip.",
          [mcell("Casos", "03"), mcell("Identidad", "Sip"), mcell("Diseño manual", "0")])
    slide("Design · Qué es", [eyebrow("Claude Design", "En el navegador"), h1("Le das datos y una ficha de marca, sale la pieza"),
                             steps([st("1", "Sube los datos", "Un Excel, un brief o un documento."),
                                    st("2", "Sube la ficha de identidad", "Colores, tipografía y qué no usar: la del kit es un ejemplo."),
                                    st("3", "Pide el contenido, no el diseño", "Qué historia contar y para quién."),
                                    st("4", "Ajusta conversando", "«La slide 3 con un gráfico de barras», «cifras más grandes».")], sm=False),
                             dlrow([dl(DL["ds"], "Descargar el kit del design system de Sip", ghost=True)])])
    slide("Design · Los 3 casos", [eyebrow("Design", "Tres casos"), h1("Lo que vamos a hacer"),
                                  mapa([("Resultados del mes", "Excel de transacciones → presentación ejecutiva de 6 slides."),
                                        ("One-pager de campaña", "Brief de «Noviembre te devuelve» → una página para comercial."),
                                        ("Reclamos del trimestre", "Excel de reclamos → 5 slides para la jefatura de atención.")])])
    caso(1, H, "Resultados del mes en 6 slides", "La presentación del comité se arma copiando tablas a PowerPoint.",
         "Design lee el Excel y arma la presentación con las cifras y los colores de Sip.", "La armo en vivo y reviso 2 cifras contra los resultados esperados.", "de1")
    caso_prompt(1, H, "El pedido", "PROMPT · CASO 1", C.PROMPT_D1, "de1",
                extra=mrow([mcell("Monto del mes", soles(TX["monto"])), mcell("Cashback", soles(TX["cashback"])),
                            mcell("Top comercio", TX["top_cashback"][0][0])], style="margin-top:14px"))
    caso(2, H, "One-pager de una campaña", "El resumen de cada campaña se diseña desde cero para cada área.",
         "Design convierte el brief en una página con el beneficio en grande y las condiciones claras.", "Lo armo en vivo con el brief de noviembre.", "de2")
    caso_prompt(2, H, "El pedido", "PROMPT · CASO 2", C.PROMPT_D2, "de2")
    r = RC
    caso(3, H, "Reclamos del trimestre en 5 slides", "El reporte de reclamos se arma a mano cada trimestre.",
         "Design lee el Excel de reclamos y arma la presentación con motivos, tiempos y recomendaciones.", "Cada uno la arma con el kit y compara las cifras.", "de3", juntos=True)
    caso_prompt(3, H, "Ahora tú: arma la presentación", "PROMPT · CASO 3", C.PROMPT_D3, "de3", juntos=True,
                extra=mrow([mcell("Reclamos", str(r["filas"])), mcell("Motivo principal", r["top_motivos"][0][0]),
                            mcell("En proceso", "%02d" % r["en_proceso"])], style="margin-top:12px"))
    write(FILES[8][0], titulo(8))


# ================================================================ 10 practica
def deck10():
    start("Práctica guiada", "Práctica")
    cover("10", "Práctica guiada", "Claude lee tus últimos 5 correos en Outlook, aprende cómo escribes y crea una Skill con tu estilo.",
          [mcell("Pasos", "04"), mcell("Correos que lee", "05"), mcell("Meta", "Tu Skill")])
    slide("Práctica · Los pasos", [eyebrow("Práctica guiada", "Tu Skill de correos"), h1("Una Skill que escribe como tú"),
                                  steps([st("1", "Activa el conector de Microsoft 365", "Configuración > Conectores, con tu cuenta de la empresa."),
                                         st("2", "Pega el prompt en un chat nuevo", "Claude lee tus últimos 5 correos enviados y te muestra tus patrones."),
                                         st("3", "Guarda la Skill", "Con el botón que te da Claude, o súbela en Configuración > Capacidades > Skills."),
                                         st("4", "Pruébala con un borrador vago", "«avísale a mi jefe que el informe se retrasa». ¿Suena a ti?")], sm=False)])
    slide("Práctica · El prompt", [eyebrow("El prompt", "Cópialo tal cual en un chat nuevo"), h1("Crea tu Skill de correos", "font-size:28px;max-width:none"),
                                  prompt_long("PROMPT · CREAR LA SKILL", C.PROMPT_SKILL_CORREOS, xl=True)])
    write(FILES[9][0], titulo(9))


# ================================================================ 11 cierre
def deck11():
    start("Cierre", "Cierre")
    cover("11", "Lo que armaste hoy", "Las herramientas de Claude con casos de Sip, y la tarea para la Sesión 2.",
          [mcell("Herramientas", "05"), mcell("Casos", "15"), mcell("Sesión 2", "Taller")])
    slide("Cierre · Lo que viste", [eyebrow("Resumen", "Cada pieza, para qué"), h1("Cinco herramientas, una lógica"),
                                   gwrap([gcard("b1", "Sk", "Skills", "La receta: respuestas, conciliaciones y comunicados siempre iguales."),
                                          gcard("b2", "Co", "Conectores", "Claude sobre tu correo, calendario y OneDrive."),
                                          gcard("b3", "Pr", "Projects", "El contexto que no se repite: donde se juntan las piezas."),
                                          gcard("b4", "Re", "Research", "Datos de hoy, con fuente y fecha."),
                                          gcard("b1", "De", "Design", "De datos a una presentación con la marca de Sip."),
                                          gcard("b2", "Tú", "Tú", "Revisas y firmas. La IA acelera; tú decides.")], c3=True, tight=True)])
    slide("Cierre · Tarea", [eyebrow("Tarea", "Para la Sesión 2"), h1("Trae esto"), bl(C.TAREA, style="margin-top:20px")])
    slide("Cierre · Qué sigue", [eyebrow("Qué sigue", "Sesión 2 · Taller práctico"), h1("Conectores, Skills y artefactos"),
                                grid(3, [card("blue", "Outlook", "Conector configurado", p("Cada uno conecta su cuenta y resuelve un caso real de su correo.")),
                                         card("lemon", "Skills", "Las tuyas", p("Presentaciones con la identidad de SIP, actas, correos con formato estándar.")),
                                         card("fruit", "Artefactos", "Una herramienta", p("Un dashboard o herramienta simple con datos de tu equipo."))]),
                                rule("Cowork", "Es la versión de escritorio de Claude: <b>cuando tengan la app</b>, hace tareas de varios pasos sobre tus archivos.")])
    quote("Cierre · Preguntas", "", "¿Preguntas?", center=True)
    write(FILES[10][0], titulo(10))


if __name__ == "__main__":
    for d in (deck1, deck2, deck3, deck4, deck5, deck6, deck7, deck8, deck9, deck10, deck11):
        d()
