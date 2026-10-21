#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sesion 2 · Taller practico · SIP (propuesta 2026-046). Once decks en tres partes:
01 Repaso · 02-06 lo nuevo de la Sesion 2 · 07-10 ejercicios · 11 cierre.
Usa el motor de la Sesion 1 (sesion-1/build/deck.py). Primero build_materiales2.py (escribe esperados2.json).
Cada ejercicio tiene dos slides: la ficha (qué se logra, qué necesitas, pasos) y el prompt con Copiar.
Uso:  python3 build_decks2.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "sesion-1", "build")))

import contenido as C1  # noqa: E402
import contenido2 as C  # noqa: E402
import deck  # noqa: E402
from deck import (agenda2, bl, card, dl, dlrow, eyebrow, gcard, grid, gwrap, h1, lst, mcell, mrow,  # noqa: E402
                  note, p, prompt_long, quote, rule, slide, start, st, steps, sub, write)

deck.PROGRAMA = "Taller de IA con Claude · SIP"
deck.OUT_DIR = os.path.abspath(os.path.join(HERE, ".."))
deck.HTML = deck.HTML.replace('href="index.html"', 'href="../sesion-1/index.html#s2"')
E = json.load(open(os.path.join(HERE, "esperados2.json"), encoding="utf-8"))
DL = E["rutas"]
FILES = C.FILES2

deck.EXT_CSS += """
/* ---------- sip · sesion 2 ---------- */
.rows.dense .row{padding:3px 18px}
.rows.dense .rt{font-size:13px}
.rows.dense .rd{font-size:11.5px}
.modo{flex:none;height:auto;display:inline-flex;align-items:center;gap:7px;font-family:var(--fm);font-size:11px;border-radius:999px;padding:5px 12px;margin-bottom:8px;align-self:flex-start}
.modo.demo{background:rgba(56,89,249,.10);color:var(--blue)}
.modo.juntos{background:var(--lemon);color:#06182D;font-weight:500}
.modo .para{color:var(--mut);margin-left:6px}
.ej{display:grid;grid-template-columns:1.05fr 1fr 1.1fr;gap:12px;margin-top:16px;flex:none;min-height:300px}
.ej .ebx{background:#fff;border:1px solid var(--line);border-radius:var(--r-l);padding:18px 20px;display:flex;flex-direction:column;min-height:0}
.ej .ebx .k{font-family:var(--fm);font-size:10.5px;letter-spacing:.05em;color:var(--blue)}
.ej .ebx.obj{background:#06182D;border-color:#06182D}
.ej .ebx.obj .k{color:var(--lemon)}
.ej .ebx.obj p{font-size:19px;line-height:1.5;color:#fff;margin-top:10px;font-weight:500}
.ej .ebx.obj .ok{margin-top:auto;padding-top:14px;font-size:13px;line-height:1.5;color:#C9D3E0}
.ej .ebx.obj .ok b{color:var(--lemon);font-weight:500}
.ej ul{list-style:none;margin-top:10px}
.ej ul li{font-size:13.5px;line-height:1.45;color:var(--ink);padding:5px 0 5px 20px;position:relative;border-bottom:1px solid var(--line)}
.ej ul li:last-child{border-bottom:0}
.ej ul li::before{content:"\\1F4C4";position:absolute;left:0;font-size:11px;top:6px}
.ej ul li.b2::before{content:"\\2713";color:#1F8A5B;font-weight:700}
.ej ul li .f{font-family:var(--fm);font-size:11.5px}
.ej ol{list-style:none;margin-top:10px;counter-reset:n}
.ej ol li{counter-increment:n;font-size:14.5px;line-height:1.45;color:var(--ink);padding:5px 0 5px 28px;position:relative}
.ej ol li::before{content:counter(n);position:absolute;left:0;top:5px;width:19px;height:19px;border-radius:50%;background:var(--blue);color:#fff;font-family:var(--fm);font-size:10.5px;display:flex;align-items:center;justify-content:center}
.ej .sep{font-family:var(--fm);font-size:10px;color:var(--mut);margin-top:10px;letter-spacing:.04em}
.lista{display:grid;gap:10px;margin-top:20px;flex:none}
.lista.c2{grid-template-columns:1fr 1fr}.lista.c3{grid-template-columns:repeat(3,1fr)}
.lista .it{background:#fff;border:1px solid var(--line);border-radius:var(--r-l);padding:18px 20px}
.lista .it.juntos{border:2px solid var(--lemon);box-shadow:0 0 0 3px rgba(252,190,17,.18)}
.lista .it .n{font-family:var(--fm);font-size:10.5px;color:var(--mut)}
.lista .it h4{font-size:19px;font-weight:600;color:var(--ink);margin-top:5px;letter-spacing:-.01em}
.lista .it p{font-size:14.5px;line-height:1.45;color:var(--mut);margin-top:5px}
.lista .it .who{font-family:var(--fm);font-size:10.5px;margin-top:8px;display:block;color:var(--blue)}
.lista .it.juntos .who{color:#8A6400}
.prompt.long{max-height:520px}
"""


def titulo(i):
    return "%s · Taller de IA con Claude · SIP" % FILES[i][1]


def soles(x):
    return "S/ {:,.2f}".format(x)


def cover(num, titulo_, bajada, celdas):
    deck.SLIDES.append(
        '<section class="slide"><div class="pad cover">\n'
        + deck.top("Bloque %s · %s" % (num, deck._DECK["bloque"]))
        + '\n<div class="body" style="justify-content:center">\n'
        + eyebrow("Bloque %s de 11" % num, "Sesión 2 · Taller práctico: Conectores, Skills y Artefactos")
        + '\n<h1 class="anim" style="margin-top:18px">%s</h1>\n' % titulo_
        + sub(bajada)
        + '\n' + mrow(celdas, tight=False)
        + '\n<div class="who anim"><span class="n">Santiago Franco</span>'
          '<span class="r">CTO · MyWorkIn</span></div>\n</div></div></section>')


def modo(juntos, para=""):
    m = ('<span class="modo juntos anim">&#9733; En conjunto: lo hacemos todos' if juntos
         else '<span class="modo demo anim">&#9654; Demo: lo hago yo, tú miras')
    return m + ('<span class="para">· Para: %s</span>' % para if para else "") + '</span>'


def lista(items, cols=3):
    """items: [(titulo, texto, juntos)]. El mapa de ejercicios de cada bloque."""
    out = []
    for i, (t, x, j) in enumerate(items):
        out.append('<div class="it%s"><span class="n">EJERCICIO %d</span><h4>%s</h4><p>%s</p>'
                   '<span class="who">%s</span></div>' % (" juntos" if j else "", i + 1, t, x,
                                                        "&#9733; En conjunto" if j else "&#9654; Demo"))
    return '<div class="lista c%d anim">%s</div>' % (cols, "".join(out))


def ejercicio(n, herramienta, titulo_, objetivo, sale_bien, construir, probar, pasos, kitkey, prompt_txt,
              juntos=False, para="", label="PROMPT", extra=None):
    """Dos slides: la ficha completa del ejercicio y el prompt para copiar. Las dos con el kit."""
    ins = "".join('<li><span class="f">%s</span></li>' % x for x in construir)
    pru = "".join('<li class="b2"><span class="f">%s</span></li>' % x for x in probar)
    pas = "".join("<li>%s</li>" % x for x in pasos)
    slide("%s · Ejercicio %d" % (herramienta, n), [
        eyebrow("Ejercicio %d" % n, herramienta),
        modo(juntos, para),
        h1(titulo_, "font-size:32px;max-width:none"),
        '<div class="ej anim">'
        '<div class="ebx obj"><span class="k">QUÉ QUEREMOS LOGRAR</span><p>%s</p>'
        '<div class="ok"><b>Sale bien si:</b> %s</div></div>'
        '<div class="ebx"><span class="k">EN EL KIT · 1_PARA_CONSTRUIR</span><ul>%s</ul>'
        '<span class="sep">2_PARA_PROBAR</span><ul>%s</ul></div>'
        '<div class="ebx"><span class="k">PASOS</span><ol>%s</ol></div></div>'
        % (objetivo, sale_bien, ins, pru, pas),
        dlrow([dl(DL[kitkey], "Descargar el material del ejercicio")]),
    ])
    blocks = [eyebrow("Ejercicio %d" % n, herramienta + " · el prompt"),
              h1(titulo_, "font-size:26px;max-width:none"),
              prompt_long("%s · TAMBIÉN ESTÁ EN 1_PARA_CONSTRUIR/%s" % (label, "Prompt.txt" if label == "PROMPT" else label.split(" · ")[-1]),
                          prompt_txt, xl=len(prompt_txt) > 900)]
    if extra:
        blocks.append(extra)
    blocks.append(dlrow([dl(DL[kitkey], "Descargar el material del ejercicio")]))
    slide("%s · Ejercicio %d · Prompt" % (herramienta, n), blocks)


# ================================================================ 01 repaso
def deck1():
    start("Repaso", "Repaso")
    cover("01", "Repaso de la Sesión 1", "Lo que armamos la semana pasada, en un slide por tema, antes de seguir.",
          [mcell("Temas", "05"), mcell("Casos vistos", "12"), mcell("Hoy", "Taller")])
    slide("Repaso · Prompting", [eyebrow("Prompting", "Cómo pedir bien"), h1("Los 5 ingredientes"),
                                 steps([st("1", "Rol", "Quién quieres que sea."), st("2", "Contexto", "Qué necesita saber."),
                                        st("3", "Tarea", "Qué tiene que hacer, en concreto."), st("4", "Formato", "Cómo lo quieres."),
                                        st("5", "Criterio de éxito", "Cuándo está bien hecho. «Si falta un dato, pregúntame.»")]),
                                 rule("Hoy", "Todos los prompts de los ejercicios ya vienen con los 5 ingredientes: <b>Copiar</b> y pegar.")])
    slide("Repaso · Skills", [eyebrow("Skills", "La receta que no se reescribe"), h1("La tarea, siempre igual"),
                              grid(3, [card("blue", "Caso 1", "Respuesta a reclamos", p("Un reclamo pegado → la respuesta con la estructura y el tono de atención.")),
                                       card("lemon", "Caso 2", "Conciliación de cashback", p("Dos Excel de OneDrive → cada diferencia entre lo esperado y lo abonado.")),
                                       card("fruit", "Caso 3", "Comunicado de mantenimiento", p("Formato fijo: solo cambian fecha, horario y servicios."))]),
                              rule("Hoy", "Creas <b>tu segunda Skill</b> con la tarea que trajiste, y vemos 2 Skills nuevas.")])
    slide("Repaso · Conectores", [eyebrow("Conectores", "Claude dentro de Microsoft 365"), h1("Tu correo, tu calendario y tus archivos"),
                                  grid(3, [card("blue", "Caso 1", "Resumir un hilo", p("5 viñetas y un borrador de respuesta.")),
                                           card("lemon", "Caso 2", "Preparar mi reunión", p("Con quién, qué correos y qué llevar.")),
                                           card("fruit", "Caso 3", "Preguntarle a un documento", p("La respuesta y en qué sección está."))]),
                                  rule("Hoy", "Cada uno <b>conecta su cuenta</b> y lo usa con su propia bandeja.")])
    slide("Repaso · Projects", [eyebrow("Projects", "El contexto que no se repite"), h1("Cada chat adentro ya llega sabiendo"),
                                grid(3, [card("blue", "Caso 1", "Atención al cliente", p("Productos, preguntas frecuentes y guía de respuesta.")),
                                         card("lemon", "Caso 2", "Reporte de transacciones", p("El Excel del mes con cifras rastreables.")),
                                         card("fruit", "Caso 3", "Campañas y comunicación", p("Voz de Sip, calendario y resultados."))]),
                                rule("Hoy", "Dos Projects nuevos: <b>comercios afiliados</b> y <b>riesgo y cumplimiento</b>.")])
    slide("Repaso · Design", [eyebrow("Claude Design", "De datos a una pieza"), h1("Datos + ficha de marca = la pieza"),
                              grid(3, [card("blue", "Caso 1", "Resultados del mes", p("Excel de transacciones → 6 slides.")),
                                       card("lemon", "Caso 2", "One-pager de campaña", p("Brief de noviembre → una página.")),
                                       card("fruit", "Caso 3", "Reclamos del trimestre", p("Excel de reclamos → 5 slides."))]),
                              rule("Hoy", "Un <b>banner de promo</b> y el <b>prototipo de una pantalla</b> de la app.")])
    slide("Repaso · Tu Skill de correos", [eyebrow("La tarea", "Tu Skill de correos"), h1("¿Qué tuviste que corregir?"),
                                           bl(["¿La usaste en correos reales? ¿En cuántos?",
                                               "¿Qué le corregiste más: el saludo, el largo, el tono o los datos?",
                                               "¿Le pediste que se actualizara? Si no, hoy es el momento: «actualiza la skill para que…»."],
                                              style="margin-top:20px"),
                                           rule("Y la otra tarea", "Ten a mano <b>la tarea que repites</b> y <b>tu Excel anonimizado</b>: los usamos hoy.")])
    slide("Sesión 2 · Agenda", [eyebrow("Agenda", "Sesión 2 · Research, que quedó pendiente, va completo hoy"), h1("Lo que vamos a hacer hoy"),
                                agenda2([(m, t, d) for m, t, d in C.AGENDA_S2], now=0)])
    write(FILES[0][0], titulo(0))


# ======================================================== 02 outlook conectado
def deck2():
    H = "Outlook conectado"
    start(H, H)
    cover("02", "Outlook conectado", "En la Sesión 1 lo viste en mi pantalla. Hoy cada uno conecta su cuenta y lo usa con su bandeja.",
          [mcell("Ejercicios", "03"), mcell("Suite", "M365"), mcell("Envía correos", "No")])
    slide("Outlook · Conectar", [eyebrow("Paso 0", "Conecta tu cuenta"), h1("Cuatro clics y Claude ve tu Outlook"),
                                 steps([st("1", "Configuración > Conectores", "En claude.ai, menú de tu perfil."),
                                        st("2", "Microsoft 365 > Conectar", "Inicia sesión con tu cuenta de SIP y acepta los permisos."),
                                        st("3", "Abre un chat nuevo", "En el menú de herramientas, verifica que Microsoft 365 esté activo."),
                                        st("4", "¿No aparece?", "Lo habilita TI. Sigue los ejercicios en pantalla y lo repites después.")], sm=False),
                                 dlrow([dl(DL["ol1"], "Descargar el material", ghost=True)])])
    slide("Outlook · Qué puede", [eyebrow("Qué puede y qué no", "Antes de usarlo"), h1("Lee todo lo que tú ves. No envía nada."),
                                  grid(3, [card("blue", "Lee", "Correo, calendario y archivos", p("Tu bandeja, tus reuniones y tu OneDrive o SharePoint: solo lo que tu cuenta ya ve.")),
                                           card("lemon", "Prepara", "Resúmenes y borradores", p("Te muestra en el chat el resumen, la tabla o el borrador. Tú lo copias a Outlook.")),
                                           card("fruit", "No hace", "Enviar, borrar ni agendar", p("No envía correos, no mueve ni borra nada, no crea reuniones."))]),
                                  rule("Buenas prácticas", "Pide siempre <b>asunto y fecha</b> de lo que usó, abre 1 correo para contrastar y <b>lee el borrador entero</b> antes de copiarlo.")])
    slide("Outlook · Los 3 ejercicios", [eyebrow("Outlook conectado", "Tres ejercicios"), h1("Lo que vamos a hacer"),
                                         lista([("Priorizar la bandeja del lunes", "Lo que llegó desde el viernes, en 4 categorías, y qué hacer primero.", False),
                                                ("Responder en lote", "Lo que tienes sin responder y 3 borradores listos para revisar.", False),
                                                ("Tu semana en el calendario", "Horas en reuniones, choques, qué llevar y bloques libres.", True)])])
    ejercicio(1, H, "Priorizar la bandeja del lunes",
              "Que Claude lea todo lo que llegó desde el viernes y te diga qué atender primero.",
              "cada correo queda en una sola categoría y «Urgente hoy» cumple la regla del prompt.",
              ["Prompt.txt", "Como_conectar_tu_cuenta.txt"], ["Que_deberias_ver.txt", "Que_revisar_antes_de_usarlo.txt"],
              ["Conecta tu cuenta de Microsoft 365.", "Abre un chat nuevo y pega el prompt.",
               "Pídele: «¿por qué pusiste este correo en Urgente hoy?».", "Contrasta 1 correo abriéndolo en Outlook."],
              "ol1", C.PROMPT_BANDEJA, para="todos")
    ejercicio(2, H, "Responder 3 correos en lote",
              "Encontrar lo que tienes sin responder y salir con 3 borradores listos para revisar y copiar.",
              "los 3 borradores tienen máximo 100 palabras y lo que falta va entre [corchetes].",
              ["Prompt.txt", "Como_conectar_tu_cuenta.txt"], ["Que_deberias_ver.txt", "Que_revisar_antes_de_usarlo.txt"],
              ["Con el conector activo, pega el prompt en un chat nuevo.", "Revisa la tabla de pendientes.",
               "Pide un cambio a un solo borrador: «el segundo, más corto».", "Copia el que te sirva a Outlook y envíalo tú."],
              "ol2", C.PROMPT_LOTE, para="todos")
    ejercicio(3, H, "Tu semana en el calendario",
              "Ver tu semana entera: cuántas horas tienes en reuniones, qué llevar a las importantes y dónde hay tiempo libre.",
              "la tabla coincide con tu calendario y los 2 bloques de 90 minutos están de verdad libres.",
              ["Prompt.txt", "Como_conectar_tu_cuenta.txt"], ["Que_deberias_ver.txt", "Que_revisar_antes_de_usarlo.txt"],
              ["Conecta tu cuenta (si no lo hiciste).", "Pega el prompt en un chat nuevo.",
               "Abre tu calendario de Outlook y contrasta un día.", "Reserva tú los bloques libres en Outlook."],
              "ol3", C.PROMPT_SEMANA, juntos=True, para="todos")
    write(FILES[1][0], titulo(1))


# ================================================================ 03 research
def deck3():
    H = "Research"
    start(H, H)
    cover("03", "Research", "Lo que quedó pendiente de la Sesión 1: Claude revisa decenas de fuentes y te entrega un informe que puedes verificar.",
          [mcell("Fuentes", "Siempre"), mcell("Tarda", "Minutos"), mcell("Ejercicios", "Bloque 07")])
    slide("Research · Qué es", [eyebrow("Research", "Búsqueda web vs. investigación"), h1("Dos formas de traer datos de hoy"),
                                grid(2, [card("blue", "Búsqueda web", "El dato puntual", lst(["Una tasa, una noticia, una norma vigente", "Responde en segundos y cita el enlace", "Se activa sola cuando el dato puede haber cambiado"])),
                                         card("lemon", "Research", "El informe", lst(["Revisa muchas fuentes y las compara", "Entrega un informe con citas", "Tarda de 5 a 15 minutos: lánzalo y sigue trabajando"]))]),
                                rule("La condición", "Fuente y fecha en cada dato. <b>Lo que no tiene fuente, no se usa.</b>")])
    slide("Research · Cómo se usa", [eyebrow("En el navegador", "Cómo se lanza"), h1("Tres pasos"),
                                     steps([st("1", "Chat nuevo > botón Research", "Debajo de la caja de texto. Si no lo ves, activa la búsqueda web en Configuración."),
                                            st("2", "Pega un pedido con reglas", "Qué cubrir, qué formato y «si no lo encuentras, escribe no encontrado»."),
                                            st("3", "Mientras investiga, ves las fuentes", "Al terminar, el informe trae las citas al lado de cada dato.")], sm=False)])
    slide("Research · Cómo verificar", [eyebrow("Antes de usarlo", "El checklist"), h1("Seis controles antes de compartirlo"),
                                        bl(["¿Cada dato tiene fuente y fecha?", "Abre 2 enlaces al azar: ¿dicen lo que la IA dice?",
                                            "¿Las fechas son recientes?", "¿Separó lo confirmado de lo anunciado o «no encontrado»?",
                                            "¿Las fuentes son oficiales (SBS, BCRP, la empresa) o medios reconocidos?", "¿Lo firmarías con tu nombre?"],
                                           style="margin-top:18px"),
                                        rule("Los ejercicios", "Mercado, regulación y Sip vs. competencia: en el <b>bloque 07</b>, después de la pausa.")])
    write(FILES[2][0], titulo(2))


# ======================================================= 04 tu segunda skill
def deck4():
    H = "Tu segunda Skill"
    start(H, H)
    cover("04", "Tu segunda Skill", "La tarea que trajiste de tarea, convertida en una Skill que te sale siempre igual.",
          [mcell("Ficha", "8 preguntas"), mcell("Prompt", "01"), mcell("Meta", "Tu Skill")])
    slide("Skill · Señales", [eyebrow("¿Sirve tu tarea?", "Las señales"), h1("Si respondes «sí» a dos, hazla Skill"),
                              gwrap([gcard("b1", "01", "¿Se repite?", "Cada semana o cada mes, siempre parecida."),
                                     gcard("b2", "02", "¿Siempre empiezas de cero?", "Vuelves a explicar todo en un chat nuevo."),
                                     gcard("b3", "03", "¿Tiene un formato fijo?", "Misma estructura: cambian algunos datos."),
                                     gcard("b4", "04", "¿Pegas el mismo prompt largo?", "Lo tienes guardado en un bloc de notas."),
                                     gcard("b1", "05", "¿Cada persona lo hace distinto?", "Y el resultado cambia según quién."),
                                     gcard("b2", "06", "¿Hay reglas que no se olvidan?", "Lo que nunca se promete, lo que se revisa.")],
                                    c3=True, tight=True)])
    slide("Skill · La ficha", [eyebrow("Antes de abrir Claude", "Llena la ficha"), h1("Ocho preguntas sobre tu tarea"),
                               grid(2, [card("blue", "1 a 4", "Qué es", lst(["Nombre de la tarea", "Cada cuánto la haces", "Qué recibes para hacerla", "Qué entregas al final"])),
                                        card("lemon", "5 a 8", "Cómo se hace bien", lst(["El formato que siempre tiene", "Reglas que no se olvidan", "Qué haces si falta un dato", "Un ejemplo que salió bien, sin datos de clientes"]))]),
                               rule("En el kit", "La ficha en blanco y <b>una de ejemplo ya llena</b>: resumen semanal de reclamos para la jefatura."),
                               dlrow([dl(DL["sk"], "Descargar el material", ghost=True)])])
    ejercicio(1, H, "Crea tu segunda Skill",
              "Convertir la tarea repetitiva que trajiste en una Skill que cualquiera de tu equipo use y le salga igual.",
              "en un chat nuevo sale siempre con el mismo formato y, si falta un dato, te lo pregunta.",
              ["Prompt.txt", "Ficha_de_tu_tarea.txt", "Ficha_de_ejemplo.txt"], ["Como_probar_tu_skill.txt"],
              ["Completa la ficha (mira la de ejemplo).", "En un chat nuevo, pega el prompt y tu ficha al final.",
               "Responde las preguntas de Claude y guarda la Skill.", "Pruébala en otro chat nuevo con los 2 pedidos que te dio."],
              "sk", C.PROMPT_SEGUNDA_SKILL, juntos=True, para="todos")
    slide("Skill · Cómo probarla", [eyebrow("Antes de compartirla", "La prueba"), h1("Una Skill está bien hecha si…"),
                                    bl(["Se activa sola en un chat nuevo, sin la conversación donde la creaste.",
                                        "Sale siempre con el mismo formato.",
                                        "Cuando falta un dato, lo pregunta en vez de inventarlo.",
                                        "Otra persona la usa con el mismo pedido y le sale lo mismo que a ti."], style="margin-top:20px"),
                                    rule("Si algo falla", "Díselo en el chat: <b>«actualiza la skill para que…»</b>.")])
    write(FILES[3][0], titulo(3))


# ============================================================== 05 artefactos
def deck5():
    H = "Artefactos"
    start(H, H)
    cover("05", "Artefactos", "Una herramienta que funciona dentro de Claude: la pides en un mensaje, la pruebas y la compartes con un enlace.",
          [mcell("Programar", "No"), mcell("Se comparte", "Enlace"), mcell("Ejercicios", "Bloque 08")])
    slide("Artefactos · Qué es", [eyebrow("Qué es un artefacto", "Una app dentro del chat"), h1("Le describes la herramienta y aparece al lado"),
                                  grid(3, [card("blue", "Se ve al lado", "Funciona en el momento", p("Calculadoras, dashboards, simuladores: con botones, sliders y gráficos.")),
                                           card("lemon", "Lee archivos", "Tus Excel y CSV", p("Les cargas un archivo y lo procesa en el navegador, sin subirlo a otro sistema.")),
                                           card("fruit", "Con IA adentro", "Usa a Claude por dentro", p("Puede clasificar o redactar: por ejemplo, un clasificador de reclamos."))])])
    slide("Artefactos · Cómo pedirlo", [eyebrow("Cómo se pide", "Cinco piezas"), h1("Un buen pedido de artefacto"),
                                        steps([st("1", "Qué es y para quién", "«Simulador de campaña de cashback para Marketing.»"),
                                               st("2", "Entradas", "Qué carga o escribe la persona: un CSV, montos, una lista desplegable."),
                                               st("3", "Reglas y cálculos", "Las fórmulas exactas. Si no las das, las inventa."),
                                               st("4", "Qué muestra", "Tarjetas, gráficos, tablas, avisos."),
                                               st("5", "Diseño", "Colores de Sip, montos en S/ con 2 decimales.")]),
                                        rule("Regla", "Prueba con <b>casos que ya sabes el resultado</b> antes de compartirlo.")])
    slide("Artefactos · Compartir y límites", [eyebrow("Compartir", "Y lo que no hace"), h1("Se comparte con un enlace"),
                                               grid(2, [card("blue", "Compartir", "Publicar > copiar enlace",
                                                             lst(["Quien lo abre ve la herramienta, no tu conversación", "Si usa IA por dentro, usa la cuenta de quien lo abre", "Para cambiarlo, lo pides en el mismo chat"])),
                                                        card("fruit", "Lo que no hace", "No es un sistema de SIP",
                                                             lst(["No se conecta a los sistemas internos", "No guarda los datos que le cargas", "No reemplaza una validación: tú revisas los cálculos"]))]),
                                               rule("Los ejercicios", "Cinco micro-apps en el <b>bloque 08</b>, con sus archivos y casos de prueba.")])
    write(FILES[4][0], titulo(4))


# ======================================================== 06 claude en chrome
def deck6():
    H = "Claude en Chrome"
    start(H, H)
    cover("06", "Claude en Chrome", "Una extensión que deja a Claude trabajar en la pestaña que tienes abierta: leer, hacer clic y escribir.",
          [mcell("Instala", "Extensión"), mcell("Permisos", "Por sitio"), mcell("Ejercicios", "02")])
    slide("Chrome · Qué es", [eyebrow("Qué es", "Claude en una pestaña"), h1("Claude ve la página y la usa como tú"),
                              grid(3, [card("blue", "Lee", "La página abierta", p("Entiende lo que hay en la pestaña: textos, tablas, formularios.")),
                                       card("lemon", "Actúa", "Clic, escribe, navega", p("Llena un formulario, recorre varias páginas, copia datos de una a otra.")),
                                       card("fruit", "Pregunta", "Antes de lo importante", p("Antes de enviar o publicar algo te pide confirmación."))])])
    slide("Chrome · Instalar", [eyebrow("Cómo se instala", "Cuatro pasos"), h1("De la Chrome Web Store al panel lateral"),
                                steps([st("1", "Chrome Web Store > «Claude»", "Agregar a Chrome y fija el ícono."),
                                       st("2", "Inicia sesión", "Con tu cuenta de Claude de SIP."),
                                       st("3", "Abre el panel", "Clic en el ícono: se abre al costado de la página."),
                                       st("4", "Da permiso por sitio", "La primera vez que entra a una web te lo pide.")], sm=False),
                                note("Ojo", "Instalar extensiones en las laptops de SIP lo autoriza <b>TI</b>. Si no te deja, sigue la demo en pantalla.")])
    slide("Chrome · Sí y no", [eyebrow("Uso responsable", "Dónde sí y dónde no"), h1("Úsalo en lo que harías tú, no en lo delicado"),
                               '<div class="vs anim"><div class="col si"><span class="k">SÍ</span><h3 style="color:#fff">Tareas repetitivas en la web</h3>'
                               '<ul><li>Llenar formularios internos o de práctica</li><li>Recorrer webs públicas y armar una tabla</li><li>Copiar datos de una página a otra</li></ul></div>'
                               '<div class="col no"><span class="k">NO</span><h3>Donde hay dinero o claves</h3>'
                               '<ul><li>Banca en línea, pagos o transferencias</li><li>Escribir contraseñas o códigos</li><li>Sistemas con datos de clientes sin autorización</li></ul></div></div>',
                               rule("Más ejercicios", "Un formulario de práctica y las webs de la competencia, en el <b>bloque 10</b>, junto con Cowork.")])
    slide("Chrome · Los 2 ejercicios", [eyebrow("Claude en Chrome", "Dos ejercicios para probarlo"), h1("Primero lee, después actúa"),
                                        lista([("Leer y comparar una web", "Navega sip.pe hasta las tarjetas y arma una tabla con lo que encuentra.", False),
                                               ("Gestionar reclamos en un portal", "Filtra, abre cada reclamo vencido, lo escala con una nota y guarda.", True)], cols=2)])
    ejercicio(1, H, "Leer y comparar una web",
              "Ver cómo Claude navega una web como tú: abre menús, cambia de página, baja y junta lo que encuentra en una tabla.",
              "la tabla coincide con la web, cada dato tiene su enlace y se detiene antes de «Solicitar».",
              ["Prompt.txt", "Como_instalar_Claude_en_Chrome.txt"], ["Checklist_de_revision.txt"],
              ["Instala la extensión y abre su panel.", "Pega el prompt.", "Mira cómo navega sip.pe.", "Abre un enlace y contrasta la tabla."],
              "chx1", C.PROMPT_CHROME_LEER, para="todos")
    ejercicio(2, H, "Gestionar reclamos en un portal",
              "Ver cómo Claude actúa en una página: filtra la tabla, abre cada reclamo vencido, cambia el estado, escribe la nota y guarda.",
              "escala solo %s y el contador «Escalados» del portal dice %d." % (", ".join(E["portal"]), len(E["portal"])),
              ["Prompt.txt (con el enlace del portal)", "Como_instalar_Claude_en_Chrome.txt"], ["Resultado_esperado.txt"],
              ["Abre el panel de Claude en Chrome.", "Pega el prompt.", "Mira cómo gestiona cada reclamo.", "Revisa el contador y el historial."],
              "chx2", C.PROMPT_CHROME_ACTUAR, juntos=True, para="Atención al Cliente")
    write(FILES[5][0], titulo(5))


# ===================================================== 07 ejercicios research
def deck7():
    H = "Ejercicios · Research"
    start(H, H)
    cover("07", "Ejercicios · Research", "Tres investigaciones para SIP, cada una con su prompt y su checklist de verificación.",
          [mcell("Ejercicios", "03"), mcell("Demo", "02"), mcell("En conjunto", "01")])
    slide("Research · Los 3 ejercicios", [eyebrow("Research", "Tres ejercicios"), h1("Lo que vamos a hacer"),
                                          lista([("Mercado de billeteras", "Quiénes son, cuántos usuarios y qué tendencias, con fuente.", False),
                                                 ("Qué exige la regulación", "BCRP y SBS: lo vigente separado de lo anunciado.", False),
                                                 ("Sip vs. competencia", "La tabla de beneficios frente a Yape, Plin, BIM y tarjetas.", True)])])
    comun = (["Prompt.txt"], ["Checklist_de_verificacion.txt"])
    pasos = ["Chat nuevo y activa Research.", "Pega el prompt y espera el informe.", "Verifica con el checklist: abre 2 fuentes."]
    ejercicio(1, H, "El mercado de billeteras digitales",
              "Un resumen ejecutivo de una página del mercado de billeteras en el Perú, con una tabla de billeteras.",
              "cada dato tiene fuente y fecha, y al final lista lo que no pudo confirmar.",
              *comun, pasos, "re1", C1.PROMPT_R1, para="Producto y Estrategia")
    ejercicio(2, H, "Qué exige la regulación",
              "Una tabla con las normas que aplican a una billetera como Sip: entidad, fecha, qué exige y enlace oficial.",
              "separa lo VIGENTE de lo EN CONSULTA y cada fila tiene enlace oficial.",
              *comun, pasos, "re2", C1.PROMPT_R2, para="Riesgo y Cumplimiento")
    ejercicio(3, H, "Sip vs. competencia",
              "Comparar los beneficios de Sip con los de Yape, Plin, BIM y 2 tarjetas digitales, y ver dónde Sip se diferencia.",
              "la tabla tiene fuente y fecha por dato, «no encontrado» cuando falta, y 3 conclusiones.",
              *comun, pasos, "re3", C1.PROMPT_R3, juntos=True, para="Marketing y Producto")
    write(FILES[6][0], titulo(6))


# =================================================== 08 ejercicios micro-apps
def deck8():
    H = "Ejercicios · Micro-apps"
    start(H, H)
    cover("08", "Ejercicios · Micro-apps", "Cinco herramientas para áreas de SIP, hechas con artefactos: un pedido, sus archivos y sus casos de prueba.",
          [mcell("Micro-apps", "05"), mcell("Áreas", "04"), mcell("Programar", "No")])
    slide("Micro-apps · Las 5", [eyebrow("Micro-apps", "Cinco ejercicios"), h1("Lo que vamos a construir"),
                                 lista([("Simulador de campaña de cashback", "Marketing: cuánto cuesta una campaña y si entra en el presupuesto.", False),
                                        ("Dashboard de reclamos", "Atención: cargas el CSV del mes y ves motivos, semanas y fuera de plazo.", False),
                                        ("Conciliador visual", "Operaciones: dos Excel de cashback y las diferencias resaltadas.", False),
                                        ("Calculadora de comisiones", "Comercios: cuánto paga y cuánto recibe un comercio.", False),
                                        ("Clasificador de reclamos con IA", "Atención: pegas un reclamo y sale categoría, urgencia y respuesta.", True)])])
    s = E["sim"]["A"]
    ejercicio(1, H, "Simulador de campaña de cashback",
              "Que Marketing pruebe una campaña antes de lanzarla: cuánto cuesta, cuánto cuesta cada compra y si entra en el presupuesto.",
              "con el escenario A da costo total %s y costo por compra %s." % (soles(s["costo"]), soles(s["por_compra"])),
              ["Prompt.txt", "Como_usar_y_compartir.txt"], ["Casos_de_prueba_y_resultados.txt"],
              ["Chat nuevo y pega el prompt.", "Pon los valores del escenario A y compara.", "Prueba el B: debe salir el aviso rojo.", "Publícalo y comparte el enlace."],
              "ma1", C.PROMPT_SIMULADOR, para="Marketing")
    r = E["rec"]
    ejercicio(2, H, "Dashboard de reclamos",
              "Un dashboard al que Atención le carga el CSV del mes y ve al instante los reclamos por motivo, por semana y fuera de plazo.",
              "muestra %d reclamos y %.1f%% fuera de plazo con el CSV del kit." % (r["total"], r["pct_fuera"]),
              ["Prompt.txt", "Reclamos_Octubre_2026.csv", "Como_usar_y_compartir.txt"],
              ["Resultados_esperados.txt", "Archivo_con_columna_faltante.csv"],
              ["Chat nuevo y pega el prompt.", "Carga Reclamos_Octubre_2026.csv en el artefacto.", "Compara con los resultados y prueba el filtro «App».",
               "Carga el archivo con error: debe avisar."],
              "ma2", C.PROMPT_DASHBOARD, para="Atención al Cliente")
    k = E["conc"]
    ejercicio(3, H, "Conciliador visual de cashback",
              "Que Operaciones cargue los dos Excel de la quincena y vea cada diferencia resaltada, sin cruzar nada a mano.",
              "da diferencia de %s y encuentra %d compras sin abono." % (soles(k["diferencia"]), len(k["sin_abono"])),
              ["Prompt.txt", "Compras_elegibles_cashback_Oct_Q2_2026.xlsx", "Cashback_abonado_Oct_Q2_2026.xlsx"],
              ["Resultados_esperados.txt"],
              ["Chat nuevo y pega el prompt.", "Carga los dos Excel.", "Compara totales e ID con los resultados.", "Prueba «Descargar diferencias»."],
              "ma3", C.PROMPT_CONCILIADOR, para="Operaciones y Finanzas")
    c = E["com"][0]
    ejercicio(4, H, "Calculadora de comisiones para comercios",
              "Que Comercios Afiliados le diga a un comercio, en segundos, cuánto pagará de comisión y cuánto recibirá.",
              "una farmacia con %s en ventas recibe %s de abono neto." % (soles(c[1]), soles(c[3]["neto"])),
              ["Prompt.txt (trae el tarifario)", "Tarifario_de_comisiones.txt", "Como_usar_y_compartir.txt"],
              ["Casos_de_prueba_y_resultados.txt"],
              ["Chat nuevo y pega el prompt.", "Prueba los 4 casos.", "El 3 tiene descuento por volumen; el 4, comisión mínima.", "Si uno no cuadra, dile qué regla no aplicó."],
              "ma4", C.PROMPT_COMISIONES, para="Comercios Afiliados")
    ejercicio(5, H, "Clasificador de reclamos con IA",
              "Una herramienta en la que Atención pega un reclamo y recibe la categoría, la urgencia, si se escala y la respuesta sugerida.",
              "al menos 7 de los 8 reclamos de prueba coinciden con los resultados esperados.",
              ["Prompt.txt", "Como_usar_y_compartir.txt"], ["Reclamos_de_prueba.txt", "Resultados_esperados.txt"],
              ["Chat nuevo y pega el prompt.", "Pega los 8 reclamos de prueba, uno por uno.", "Compara categoría, urgencia y escalar.",
               "Lee 2 respuestas completas: ¿tutean y no prometen?"],
              "ma5", C.PROMPT_CLASIFICADOR, juntos=True, para="Atención al Cliente")
    write(FILES[7][0], titulo(7))


# ====================================== 09 ejercicios skills, projects y design
def deck9():
    H = "Ejercicios · Skills, Projects y Design"
    start(H, H)
    cover("09", "Ejercicios · Skills, Projects y Design", "Seis casos nuevos de SIP con las herramientas que ya conoces de la Sesión 1.",
          [mcell("Skills", "02"), mcell("Projects", "02"), mcell("Design", "02")])
    slide("Skills, Projects y Design · Los 6", [eyebrow("Skills, Projects y Design", "Seis ejercicios"), h1("Lo que vamos a hacer"),
                          lista([("Skill · Acta de reunión", "Notas desordenadas → acta con acuerdos, responsables y fechas.", True),
                                 ("Skill · Reporte semanal", "Tus correos de la semana → el reporte con 5 secciones fijas.", False),
                                 ("Project · Comercios afiliados", "Condiciones, tarifario y onboarding → respuestas a comercios.", False),
                                 ("Project · Riesgo y cumplimiento", "Tres políticas → qué hacer, con documento y sección.", False),
                                 ("Design · Banner de promo", "Brief de Navidad → banner de la app e historia.", False),
                                 ("Design · Pantalla de la app", "Brief de «Mis cashbacks» → prototipo para celular.", False)])])
    ejercicio(1, "Skills", "Acta de reunión",
              "Que unas notas desordenadas salgan como acta con acuerdos, responsables y fechas, siempre con el mismo formato.",
              "con las notas 2 pone «por definir» donde falta y no inventa responsables.",
              ["acta-de-reunion.zip", "Prompt.txt"], ["Notas_reunion_1.txt", "Notas_reunion_2_con_datos_faltantes.txt", "Resultado_esperado.txt"],
              ["Sube la Skill: Configuración > Capacidades > Skills.", "Chat nuevo: pega el prompt con las notas 1.", "Repite con las notas 2.", "Compara con el resultado esperado."],
              "ej1", "Usa la skill acta-de-reunion con estas notas:\n\n" + C.NOTAS_REUNION_1, juntos=True, para="todos")
    ejercicio(2, "Skills", "Reporte semanal desde tus correos",
              "Que tu reporte semanal salga solo de tus correos, siempre con 5 secciones: cerrado, en curso, bloqueos, sin responder y próxima semana.",
              "con los correos de ejemplo usa 9 de 10 (salta el automático) y no inventa fechas.",
              ["reporte-semanal-de-correos.zip", "Prompt_con_conector.txt", "Prompt_sin_conector.txt", "Correos_de_ejemplo.txt"],
              ["Resultado_esperado_con_correos_de_ejemplo.txt"],
              ["Sube la Skill.", "Pruébala con los correos de ejemplo y compara.", "Con el conector activo, pide tu semana real."],
              "ej2", C.PROMPT_REPORTE_CONECTOR + "\n\n(Sin conector: «" + C.PROMPT_REPORTE_PEGADO.replace("\n\n", " ") + "»)",
              para="todos", label="PROMPT · Prompt_con_conector.txt")
    ejercicio(3, "Projects", "Comercios afiliados",
              "Un Project que responde a comercios con las condiciones, el tarifario y el onboarding de Sip, y cita el documento.",
              "calcula la comisión paso a paso y en la pregunta 5 dice que el rubro no está en el tarifario.",
              ["00_Instrucciones_del_Project.txt", "01 a 04: condiciones, tarifario, onboarding y FAQ"], ["Preguntas_de_prueba_y_respuestas.txt"],
              ["Projects > Nuevo: «Comercios afiliados · Sip».", "Pega las instrucciones y sube los 4 documentos.", "Haz las 5 preguntas y compara."],
              "ej3", C.PC_INSTR, para="Comercios Afiliados", label="INSTRUCCIONES · 00_Instrucciones_del_Project.txt")
    ejercicio(4, "Projects", "Riesgo y cumplimiento",
              "Un Project al que cualquiera le pregunta qué dice la política, con el documento y la sección.",
              "cada respuesta cita documento y sección, y en la 5 dice que ninguna política lo cubre.",
              ["00_Instrucciones_del_Project.txt", "01 a 03: fraude, datos personales y reclamos"], ["Preguntas_de_prueba_y_respuestas.txt"],
              ["Projects > Nuevo: «Riesgo y cumplimiento · Sip».", "Pega las instrucciones y sube las 3 políticas.", "Haz las 5 preguntas y compara."],
              "ej4", C.PR_INSTR, para="Riesgo y todas las áreas", label="INSTRUCCIONES · 00_Instrucciones_del_Project.txt")
    ejercicio(5, "Design", "Banner de una promo de cashback",
              "Las 2 piezas de «Navidad te devuelve»: el banner de la app y la historia de Instagram, con la identidad de Sip.",
              "el 3% es lo más grande, aparece el tope de S/ 60 y el texto legal está completo.",
              ["Prompt.txt", "Brief_Navidad_te_devuelve.txt", "Identidad_visual_Sip.txt", "logo_sip.png"], ["Checklist_de_revision.txt"],
              ["Abre Claude Design.", "Sube el brief, la ficha y el logo.", "Pega el prompt.", "Revisa las 2 piezas con el checklist."],
              "ej5", C.PROMPT_BANNER, para="Marketing")
    ejercicio(6, "Design", "Pantalla nueva de la app",
              "El prototipo interactivo de la pantalla «Mis cashbacks» para celular, con el estilo de la app Sip.",
              "tiene las 7 partes del brief y el filtro «Abonados» muestra 4 movimientos.",
              ["Prompt.txt", "Brief_pantalla_Mis_cashbacks.txt", "Identidad_visual_Sip.txt", "logo_sip.png", "capturas_sip/ (3)"],
              ["Checklist_de_revision.txt"],
              ["Abre Claude Design.", "Sube el brief, la ficha, el logo y las capturas.", "Pega el prompt.", "Prueba los filtros y revisa."],
              "ej6", C.PROMPT_PANTALLA, para="Producto")
    write(FILES[8][0], titulo(8))


# ============================================== 10 ejercicios chrome y cowork
def deck10():
    H = "Ejercicios · Chrome y Cowork"
    start(H, H)
    cover("10", "Ejercicios · Claude en Chrome y Cowork", "Claude trabajando en una pestaña del navegador y en las carpetas de tu computadora.",
          [mcell("Chrome", "02"), mcell("Cowork", "02"), mcell("Requiere", "TI")])
    slide("Cowork · Qué es", [eyebrow("Cowork", "Claude en tu computadora"), h1("Le das una carpeta y trabaja adentro"),
                              grid(3, [card("blue", "Dónde", "App de escritorio", p("Se descarga de claude.com/download y se abre la pestaña Cowork.")),
                                       card("lemon", "Qué toca", "Solo la carpeta que le das", p("Lee, renombra, mueve y crea archivos dentro de esa carpeta.")),
                                       card("fruit", "Cómo", "Te muestra cada paso", p("Ves lo que hace y te pregunta antes de borrar algo."))]),
                              note("Ojo", "Instalar la app de escritorio y la extensión de Chrome lo autoriza <b>TI</b>. Si no están, los 4 ejercicios van como demo.")])
    slide("Chrome y Cowork · Los 4", [eyebrow("Chrome y Cowork", "Cuatro ejercicios"), h1("Lo que vamos a hacer"),
                                      lista([("Chrome · Llenar un formulario", "3 comercios registrados en un formulario web, campo por campo.", False),
                                             ("Chrome · Webs de la competencia", "4 webs oficiales recorridas y una tabla con el enlace de cada dato.", False),
                                             ("Cowork · Ordenar comprobantes", "15 PDF con nombres desordenados → renombrados, por proveedor y con Excel.", False),
                                             ("Cowork · Reporte desde varios archivos", "4 Excel semanales y unas notas → el reporte mensual en Word.", False)], cols=2)])
    cods = E["form"]
    ejercicio(1, "Claude en Chrome", "Llenar un formulario web",
              "Que Claude registre 3 comercios en un formulario web, campo por campo, mientras tú miras cómo lo hace.",
              "salen los 3 códigos de solicitud: %s." % ", ".join(c[2] for c in cods),
              ["Prompt.txt (enlace y datos)", "Comercios_por_afiliar.xlsx y .txt", "Como_instalar_Claude_en_Chrome.txt"],
              ["Resultados_esperados.txt"],
              ["Instala la extensión y abre su panel.", "Pega el prompt.", "Mira cómo llena cada campo.", "Compara los 3 códigos."],
              "ch1", C.prompt_formulario(), para="Comercios Afiliados")
    ejercicio(2, "Claude en Chrome", "Webs de la competencia",
              "Que Claude recorra las webs oficiales de Sip, Yape, Plin y BIM y arme una tabla de beneficios con el enlace de cada dato.",
              "cada dato tiene su enlace y usa «no publicado» cuando no lo encuentra.",
              ["Prompt.txt", "Como_instalar_Claude_en_Chrome.txt"], ["Checklist_de_revision.txt"],
              ["Abre el panel de Claude en Chrome.", "Pega el prompt.", "Dale permiso en cada sitio.", "Revisa con el checklist y abre 2 enlaces."],
              "ch2", C.PROMPT_WEB_COMPETENCIA, para="Marketing")
    cp = E["comp"]
    ejercicio(3, "Cowork", "Ordenar y renombrar comprobantes",
              "Que Claude lea 15 PDF con nombres desordenados, los renombre, los ordene por proveedor y arme el Excel resumen.",
              "ordena %d facturas de %d proveedores por %s y manda 2 archivos a «Revisar»." % (cp["facturas"], cp["proveedores"], soles(cp["total"])),
              ["Comprobantes_octubre/ (15 PDF)", "Prompt.txt", "Como_preparar_Cowork.txt"], ["Resultados_esperados.txt"],
              ["Descomprime el kit en tu Escritorio.", "En Cowork, dale acceso a Comprobantes_octubre.", "Pega el prompt.", "Compara nombres y totales."],
              "cw1", C.PROMPT_COMPROBANTES, para="Finanzas y Administración")
    rp = E["rep"]
    ejercicio(4, "Cowork", "Reporte desde varios archivos",
              "Que Claude junte 4 Excel semanales y unas notas en un reporte mensual en Word, más un Excel consolidado.",
              "el total del mes da %s operaciones y %s." % ("{:,}".format(rp["ops"]), soles(rp["monto"])),
              ["Reporte_octubre/ (4 Excel y notas)", "Prompt.txt", "Como_preparar_Cowork.txt"], ["Resultados_esperados.txt"],
              ["Descomprime el kit en tu Escritorio.", "En Cowork, dale acceso a Reporte_octubre.", "Pega el prompt.", "Abre el Word y compara 3 cifras."],
              "cw2", C.PROMPT_REPORTE_COWORK, para="Canales Digitales")
    write(FILES[9][0], titulo(9))


# ================================================================ 11 cierre
def deck11():
    start("Cierre", "Cierre")
    cover("11", "Lo que te llevas", "Qué herramienta se lleva cada área de SIP después de estas dos sesiones.",
          [mcell("Ejercicios", "22"), mcell("Kits", "22"), mcell("Sesiones", "02")])
    slide("Cierre · Por área", [eyebrow("Qué se lleva cada área", "Para usar desde mañana"), h1("Cada área, sus herramientas"),
                                gwrap([gcard("b1", "At", "Atención al Cliente", "Dashboard de reclamos, clasificador con IA y Project de riesgo."),
                                       gcard("b2", "Mk", "Marketing", "Simulador de cashback, banner con Design y Research de la competencia."),
                                       gcard("b3", "Op", "Operaciones y Finanzas", "Conciliador visual y Cowork para ordenar comprobantes."),
                                       gcard("b4", "Co", "Comercios Afiliados", "Calculadora de comisiones, Project de comercios y formulario con Chrome."),
                                       gcard("b1", "Pr", "Producto", "Prototipo de pantalla con Design y Research de mercado y regulación."),
                                       gcard("b2", "Tú", "Todos", "Outlook conectado, tu segunda Skill, acta y reporte semanal.")], c3=True, tight=True)])
    slide("Cierre · Siguiente paso", [eyebrow("Siguiente paso", "Esta semana"), h1("Tres cosas para no perder lo de hoy"),
                                      bl(["Usa tu segunda Skill en una tarea real y compártela con alguien de tu equipo.",
                                          "Publica una micro-app y pásale el enlace a tu jefe o a tu equipo.",
                                          "Cuando TI habilite Chrome y Cowork, repite los ejercicios del bloque 10 con el kit."], style="margin-top:20px"),
                                      rule("El material", "Todos los kits quedan en el índice: <b>sip.myworkin.ai</b>.")])
    quote("Cierre · Preguntas", "", "¿Preguntas?", center=True)
    deck.qr_slide("Cierre · QR", "qr_lanzamiento_claude.png", "QR: Lanzamiento Claude y Uso seguro de la IA")
    write(FILES[10][0], titulo(10))


if __name__ == "__main__":
    for d in (deck1, deck2, deck3, deck4, deck5, deck6, deck7, deck8, deck9, deck10, deck11):
        d()
