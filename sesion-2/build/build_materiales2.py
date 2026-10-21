#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera los kits de la Sesion 2 de SIP en ../materiales/Presentacion_<NN>_<deck>/<Kit>.zip.
Formato de cada kit: LEEME.txt + 1_Para_construir/ (todo lo que se usa, incluido el prompt en .txt)
+ 2_Para_probar/ (casos de prueba y resultados esperados). Las Skills van tambien como .zip con su SKILL.md.
Escribe esperados2.json para que build_decks2.py muestre los resultados sin copiarlos a mano.
Requiere openpyxl y Google Chrome (para los PDF de Cowork).   Uso:  python3 build_materiales2.py
"""
import csv
import json
import math
import os
import random
import shutil
import subprocess
import sys
import tempfile
import zipfile
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
S1_BUILD = os.path.abspath(os.path.join(HERE, "..", "..", "sesion-1", "build"))
sys.path.insert(0, S1_BUILD)

import openpyxl  # noqa: E402

import contenido as C1  # noqa: E402
import contenido2 as C  # noqa: E402
from build_materiales import GRUPO, VISA, hoja, skill_zip, txt  # noqa: E402

MAT = os.path.abspath(os.path.join(HERE, "..", "materiales"))
DS = os.path.join(S1_BUILD, "fuentes_design_system")
A, B = "1_Para_construir", "2_Para_probar"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

KITS = {}


def kit(clave, pres, nombre):
    KITS[clave] = (pres, nombre)
    return os.path.join(MAT, pres, nombre)


def leeme(base, titulo, objetivo, construir, probar, pasos):
    t = "%s\n%s\n%s\n\nQUÉ QUEREMOS LOGRAR\n%s\n\n%s\n%s\n\n%s\n%s\n\nCÓMO HACERLO\n%s" % (
        titulo, "=" * len(titulo), C.AVISO, objetivo, A, construir, B, probar,
        "\n".join("%d. %s" % (i + 1, p) for i, p in enumerate(pasos)))
    txt(os.path.join(base, "LEEME.txt"), t)


def soles(x):
    return "S/ {:,.2f}".format(x)


def xlsx(path, titulo, cols, filas, anchos, fmt=None, notas=None):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = titulo
    hoja(ws, cols, filas, anchos, fmt)
    if notas:
        n = wb.create_sheet("Notas")
        for t in notas:
            n.append([t])
        n.column_dimensions["A"].width = 110
    os.makedirs(os.path.dirname(path), exist_ok=True)
    wb.save(path)


# ============================================================ outlook (02)
def kits_outlook():
    pres = "Presentacion_02_Outlook_conectado"
    for clave, nombre, titulo, objetivo, prompt, esperado in (
            ("ol1", "Kit_Ejercicio_1_Priorizar_la_bandeja", "PRIORIZAR LA BANDEJA DEL LUNES",
             "Que Claude lea lo que llegó desde el viernes y te diga qué atender primero.", C.PROMPT_BANDEJA, C.ESPERADO_BANDEJA),
            ("ol2", "Kit_Ejercicio_2_Responder_en_lote", "RESPONDER 3 CORREOS EN LOTE",
             "Encontrar lo que tienes sin responder y salir con 3 borradores listos para revisar.", C.PROMPT_LOTE, C.ESPERADO_LOTE),
            ("ol3", "Kit_Ejercicio_3_Tu_semana_en_el_calendario", "TU SEMANA EN EL CALENDARIO",
             "Ver tu semana entera, qué llevar a cada reunión y dónde tienes tiempo libre.", C.PROMPT_SEMANA, C.ESPERADO_SEMANA)):
        base = kit(clave, pres, nombre)
        txt(os.path.join(base, A, "Prompt.txt"), prompt)
        txt(os.path.join(base, A, "Como_conectar_tu_cuenta.txt"), C.ACTIVAR_CONECTOR)
        txt(os.path.join(base, B, "Que_deberias_ver.txt"), esperado)
        txt(os.path.join(base, B, "Que_revisar_antes_de_usarlo.txt"), C.QUE_REVISAR_CONECTOR)
        leeme(base, "KIT · OUTLOOK · " + titulo, objetivo,
              "Prompt.txt: el pedido, listo para pegar.\nComo_conectar_tu_cuenta.txt: los pasos para activar Microsoft 365.",
              "Que_deberias_ver.txt: cómo se ve un buen resultado.\nQue_revisar_antes_de_usarlo.txt: 4 controles.",
              ["Conecta tu cuenta de Microsoft 365 (Como_conectar_tu_cuenta.txt).",
               "Abre un chat nuevo y pega Prompt.txt.",
               "Compara con Que_deberias_ver.txt y revisa con los 4 controles."])


# ======================================================= segunda skill (04)
def kit_segunda_skill():
    base = kit("sk", "Presentacion_04_Tu_segunda_Skill", "Kit_Tu_segunda_Skill")
    txt(os.path.join(base, A, "Prompt.txt"), C.PROMPT_SEGUNDA_SKILL)
    txt(os.path.join(base, A, "Ficha_de_tu_tarea.txt"), C.FICHA_TAREA)
    txt(os.path.join(base, A, "Ficha_de_ejemplo.txt"), C.FICHA_EJEMPLO)
    txt(os.path.join(base, B, "Como_probar_tu_skill.txt"), C.COMO_PROBAR_SKILL)
    leeme(base, "KIT · TU SEGUNDA SKILL", "Convertir la tarea repetitiva que trajiste en una Skill que sale siempre igual.",
          "Ficha_de_tu_tarea.txt: complétala primero (8 preguntas).\nFicha_de_ejemplo.txt: una ficha ya llena.\n"
          "Prompt.txt: el pedido para crear la Skill; al final pegas tu ficha.",
          "Como_probar_tu_skill.txt: cómo probarla en un chat nuevo y qué revisar.",
          ["Completa Ficha_de_tu_tarea.txt (mira la de ejemplo).", "En un chat nuevo, pega Prompt.txt y tu ficha al final.",
           "Responde las preguntas de Claude y guarda la Skill.", "Pruébala con Como_probar_tu_skill.txt."])


# ============================================================ research (07)
def kits_research():
    pres = "Presentacion_07_Ejercicios_Research"
    for clave, nombre, titulo, objetivo, pr in (
            ("re1", "Kit_Ejercicio_1_Mercado_de_billeteras", "MERCADO DE BILLETERAS DIGITALES",
             "Un resumen ejecutivo del mercado de billeteras en el Perú, con fuente y fecha en cada dato.", C1.PROMPT_R1),
            ("re2", "Kit_Ejercicio_2_Regulacion", "QUÉ EXIGE LA REGULACIÓN",
             "Una tabla con las normas que aplican a una billetera, separando lo vigente de lo anunciado.", C1.PROMPT_R2),
            ("re3", "Kit_Ejercicio_3_Sip_vs_competencia", "SIP VS. COMPETENCIA",
             "Una tabla que compare los beneficios de Sip con los de la competencia y 3 conclusiones.", C1.PROMPT_R3)):
        base = kit(clave, pres, nombre)
        txt(os.path.join(base, A, "Prompt.txt"), pr)
        txt(os.path.join(base, B, "Checklist_de_verificacion.txt"), C1.CHECKLIST_RESEARCH)
        leeme(base, "KIT · RESEARCH · " + titulo, objetivo, "Prompt.txt: el pedido completo.",
              "Checklist_de_verificacion.txt: 6 controles antes de usar el informe.",
              ["Abre un chat nuevo y activa Research (botón debajo de la caja de texto).", "Pega Prompt.txt y espera el informe (tarda unos minutos).",
               "Verifica con el checklist: abre al menos 2 fuentes."])


# ========================================================== micro-apps (08)
def simulador(cl, co, ti, pct, tope, pres):
    bruto = co * ti * pct / 100
    porcli = min(bruto, tope)
    costo = cl * porcli
    return {"por_cliente": round(porcli, 2), "costo": round(costo, 2), "por_compra": round(costo / (cl * co), 2),
            "alcanza": math.floor(pres / porcli + 1e-9), "topa": "Sí" if bruto >= tope else "No",
            "supera": "Sí" if costo > pres else "No"}


ESC_SIM = [("A", 20000, 3, 85, 2.0, 40, 150000), ("B", 30000, 6, 250, 3.0, 40, 1000000), ("C", 5000, 2, 60, 5.0, 10, 50000)]


def comision(rubro, ventas, n):
    base = dict(C.TARIFA)[rubro]
    desc = next((d for v, d in C.TRAMOS if ventas >= v), 0.0)
    tasa = base - desc
    com = ventas * tasa / 100
    minimo = n * C.MINIMO_TX
    aplica_min = com < minimo
    com = max(com, minimo)
    igv = com * C.IGV
    return {"tasa": round(tasa, 2), "desc": desc, "minimo": aplica_min, "comision": round(com, 2),
            "igv": round(igv, 2), "total": round(com + igv, 2), "neto": round(ventas - com - igv, 2)}


ESC_COM = [("Farmacias", 80000, 2000), ("Restaurantes y cafeterías", 30000, 1200),
           ("Supermercados", 250000, 9000), ("Entretenimiento", 4000, 900)]

RECLAMOS_CLASIF = [
    ("Compré en Promart S/ 329 el 9 de octubre pagando con mi tarjeta Sip y todavía no veo el cashback. ¿Cuándo llega?",
     "Cashback no abonado", "Media", "No"),
    ("Me aparece un cargo de S/ 1,450 en una tienda de electrónica que no conozco. Yo no hice esa compra.",
     "Cobro no reconocido", "Alta", "Sí"),
    ("Quiero pasar a cuotas mi compra de S/ 600 en Oechsle, ¿cómo lo hago desde la app?", "Pase a cuotas", "Baja", "No"),
    ("Ayer le transferí S/ 250 a mi mamá por número de celular y a ella no le llega. A mí ya me descontaron.",
     "Transferencia no llegó", "Media", "No"),
    ("Es la tercera vez que escribo: mi cuenta sigue bloqueada desde el lunes y no puedo pagar nada.",
     "Bloqueo de cuenta", "Alta", "Sí"),
    ("En el módulo de plazaVea San Miguel esperé 40 minutos y nadie me supo explicar el pase a cuotas.",
     "Atención en módulo", "Baja", "No"),
    ("Me llamó alguien que dijo ser de Sip, le di un código que me llegó y ahora no tengo saldo en la billetera.",
     "Cobro no reconocido", "Alta", "Sí"),
    ("¿Pueden enviarme una tarjeta de otro color? La mía es negra y quiero la celeste.", "Otros", "Baja", "No"),
]


def reclamos_octubre():
    rnd = random.Random(2110)
    motivos = [("Cashback no abonado", .26), ("Cobro no reconocido", .20), ("Transferencia no llegó", .18),
               ("Pase a cuotas", .12), ("Bloqueo de cuenta", .11), ("Atención en módulo", .08), ("Otros", .05)]
    prod = {"Cashback no abonado": "Billetera", "Cobro no reconocido": "Tarjeta de crédito",
            "Transferencia no llegó": "Billetera", "Pase a cuotas": "Tarjeta de crédito",
            "Bloqueo de cuenta": "Billetera", "Atención en módulo": "Atención", "Otros": "Otros"}
    canales = [("App", .47), ("Web", .16), ("Módulo de Atención", .23), ("Teléfono", .14)]
    rango = {"App": (3, 14), "Web": (4, 17), "Módulo de Atención": (2, 12), "Teléfono": (5, 21)}
    filas = []
    for _ in range(186):
        f = date(2026, 10, rnd.randint(1, 31))
        mot = rnd.choices([m for m, _ in motivos], [w for _, w in motivos])[0]
        can = rnd.choices([c for c, _ in canales], [w for _, w in canales])[0]
        abierto_max = (date(2026, 10, 31) - f).days
        if rnd.random() < (.55 if f.day > 15 else .12):
            est, dr, da = "En proceso", "", abierto_max
        else:
            est, dr, da = "Resuelto", rnd.randint(*rango[can]), ""
        sem = "S%d" % min(5, (f.day - 1) // 7 + 1)
        filas.append(["", f.isoformat(), sem, mot, can, prod[mot], est, dr, da])
    filas.sort(key=lambda x: x[1])
    for i, r in enumerate(filas):
        r[0] = "R-%04d" % (3001 + i)
    return filas


def esperados_reclamos(filas):
    fuera = [r for r in filas if (r[7] != "" and r[7] > 15) or (r[8] != "" and r[8] > 15)]
    mot, sem = {}, {}
    for r in filas:
        mot[r[3]] = mot.get(r[3], 0) + 1
        sem[r[2]] = sem.get(r[2], 0) + 1
    abiertos_fuera = [r for r in filas if r[6] == "En proceso" and r[8] > 15]
    app = [r for r in filas if r[4] == "App"]
    app_fuera = [r for r in app if (r[7] != "" and r[7] > 15) or (r[8] != "" and r[8] > 15)]
    return {"total": len(filas), "resueltos": sum(r[6] == "Resuelto" for r in filas),
            "en_proceso": sum(r[6] == "En proceso" for r in filas), "fuera": len(fuera),
            "pct_fuera": round(len(fuera) / len(filas) * 100, 1),
            "por_motivo": sorted(mot.items(), key=lambda x: -x[1]), "por_semana": sorted(sem.items()),
            "abiertos_fuera": [r[0] for r in abiertos_fuera],
            "app": {"total": len(app), "pct_fuera": round(len(app_fuera) / len(app) * 100, 1)}}


def conciliacion2():
    """Segunda quincena de octubre: mismos tipos de diferencia que en la Sesion 1, con otros datos."""
    rnd = random.Random(3110)
    compras = []
    for _ in range(140):
        f = date(2026, 10, 16) + timedelta(days=rnd.randint(0, 15))
        g = rnd.random() < .6
        monto = round(rnd.uniform(15, 560), 2)
        pct = 0.01 if g else 0.005
        compras.append(["", f, rnd.choice(GRUPO if g else VISA), "Grupo" if g else "Visa", monto,
                        "%.1f%%" % (pct * 100), round(monto * pct, 2)])
    compras.sort(key=lambda x: x[1])
    for i, c in enumerate(compras):
        c[0] = "CB-%04d" % (6001 + i)
    faltan = set(rnd.sample(range(140), 7))
    mal = set(rnd.sample([i for i in range(140) if i not in faltan and compras[i][3] == "Grupo"], 5))
    abonos = []
    for i, c in enumerate(compras):
        if i in faltan:
            continue
        abonos.append([c[0], c[1] + timedelta(days=rnd.randint(2, 6)), round(c[4] * 0.005, 2) if i in mal else c[6]])
    dups = [abonos[rnd.randint(10, 50)], abonos[rnd.randint(60, 110)]]
    abonos += [[d[0], d[1], d[2]] for d in dups]
    abonos += [["CB-6211", date(2026, 10, 24), 2.40], ["CB-6224", date(2026, 10, 29), 0.95]]
    abonos.sort(key=lambda x: x[1])
    esp = {"compras": len(compras), "abonos": len(abonos),
           "sin_abono": sorted(compras[i][0] for i in faltan), "monto_distinto": sorted(compras[i][0] for i in mal),
           "duplicado": sorted(d[0] for d in dups), "sin_compra": ["CB-6211", "CB-6224"],
           "esperado": round(sum(c[6] for c in compras), 2), "abonado": round(sum(a[2] for a in abonos), 2)}
    esp["diferencia"] = round(esp["esperado"] - esp["abonado"], 2)
    return compras, abonos, esp


def kits_microapps():
    pres = "Presentacion_08_Ejercicios_Micro_apps"
    esp = {}

    # 1 · simulador
    base = kit("ma1", pres, "Kit_Ejercicio_1_Simulador_de_cashback")
    txt(os.path.join(base, A, "Prompt.txt"), C.PROMPT_SIMULADOR)
    txt(os.path.join(base, A, "Como_usar_y_compartir.txt"), C.COMO_PUBLICAR)
    sims = {}
    l = ["CASOS DE PRUEBA · SIMULADOR DE CAMPAÑA DE CASHBACK", C.AVISO, "",
         "Pon estos valores en el simulador y compara las 4 tarjetas.", ""]
    for k, cl, co, ti, pct, tope, prs in ESC_SIM:
        r = simulador(cl, co, ti, pct, tope, prs)
        sims[k] = r
        l += ["ESCENARIO %s" % k,
              "  Entradas: %s clientes · %d compras · ticket %s · %.1f%% · tope %s · presupuesto %s"
              % ("{:,}".format(cl), co, soles(ti), pct, soles(tope), soles(prs)),
              "  Cashback por cliente: %s" % soles(r["por_cliente"]),
              "  Costo total: %s" % soles(r["costo"]),
              "  Costo por compra: %s" % soles(r["por_compra"]),
              "  Clientes que alcanza el presupuesto: %s" % "{:,}".format(r["alcanza"]),
              "  Llega al tope: %s · Supera el presupuesto (aviso rojo): %s" % (r["topa"], r["supera"]), ""]
    txt(os.path.join(base, B, "Casos_de_prueba_y_resultados.txt"), "\n".join(l))
    esp["sim"] = sims
    leeme(base, "KIT · MICRO-APP · SIMULADOR DE CAMPAÑA DE CASHBACK",
          "Una herramienta para que Marketing pruebe una campaña antes de lanzarla: cuánto cuesta y si entra en el presupuesto.",
          "Prompt.txt: el pedido completo para crear el artefacto.\nComo_usar_y_compartir.txt: cómo probarlo y publicarlo.",
          "Casos_de_prueba_y_resultados.txt: 3 escenarios con los resultados que debe dar.",
          ["Abre un chat nuevo en claude.ai y pega Prompt.txt.", "Cuando aparezca el simulador, carga el escenario A y compara.",
           "Prueba B (debe salir el aviso rojo) y C.", "Si cuadra, publícalo y comparte el enlace."])

    # 2 · dashboard
    base = kit("ma2", pres, "Kit_Ejercicio_2_Dashboard_de_reclamos")
    filas = reclamos_octubre()
    os.makedirs(os.path.join(base, A), exist_ok=True)
    with open(os.path.join(base, A, "Reclamos_Octubre_2026.csv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ID", "Fecha", "Semana", "Motivo", "Canal", "Producto", "Estado", "Dias_respuesta", "Dias_abierto"])
        w.writerows(filas)
    txt(os.path.join(base, A, "Prompt.txt"), C.PROMPT_DASHBOARD)
    txt(os.path.join(base, A, "Como_usar_y_compartir.txt"), C.COMO_PUBLICAR)
    e = esperados_reclamos(filas)
    esp["rec"] = e
    txt(os.path.join(base, B, "Resultados_esperados.txt"), "\n".join(
        ["RESULTADOS ESPERADOS · DASHBOARD DE RECLAMOS · OCTUBRE 2026", C.AVISO, "",
         "Total: %d · Resueltos: %d · En proceso: %d" % (e["total"], e["resueltos"], e["en_proceso"]),
         "Fuera de plazo: %d (%.1f%%)" % (e["fuera"], e["pct_fuera"]), "", "Por motivo:"]
        + ["  %s · %d" % m for m in e["por_motivo"]] + ["", "Por semana:"] + ["  %s · %d" % s for s in e["por_semana"]]
        + ["", "En proceso y fuera de plazo (%d): %s" % (len(e["abiertos_fuera"]), ", ".join(e["abiertos_fuera"])), "",
           "PRUEBA DEL FILTRO: con el canal «App» el total debe ser %d y el %% fuera de plazo %.1f%%."
           % (e["app"]["total"], e["app"]["pct_fuera"])]))
    with open(os.path.join(base, B, "Archivo_con_columna_faltante.csv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ID", "Fecha", "Semana", "Motivo", "Canal", "Producto", "Estado", "Dias_respuesta"])
        w.writerows(r[:8] for r in filas[:20])
    txt(os.path.join(base, B, "Prueba_de_error.txt"),
        "Carga Archivo_con_columna_faltante.csv. Lo correcto: el dashboard avisa que falta la columna «Dias_abierto» en vez de mostrar cifras.")
    leeme(base, "KIT · MICRO-APP · DASHBOARD DE RECLAMOS",
          "Un dashboard al que Atención le carga el CSV del mes y ve al instante los reclamos por motivo, por semana y los que están fuera de plazo.",
          "Prompt.txt: el pedido.\nReclamos_Octubre_2026.csv: los reclamos del mes (ficticios, sin datos de clientes).\nComo_usar_y_compartir.txt.",
          "Resultados_esperados.txt: las cifras que debe mostrar.\nArchivo_con_columna_faltante.csv y Prueba_de_error.txt: para ver que avisa el error.",
          ["Abre un chat nuevo y pega Prompt.txt.", "En el artefacto, carga Reclamos_Octubre_2026.csv.",
           "Compara las tarjetas y gráficos con Resultados_esperados.txt.", "Prueba el filtro «App» y luego el archivo con error."])

    # 3 · conciliador
    base = kit("ma3", pres, "Kit_Ejercicio_3_Conciliador_visual")
    compras, abonos, ce = conciliacion2()
    xlsx(os.path.join(base, A, "Compras_elegibles_cashback_Oct_Q2_2026.xlsx"), "Compras elegibles",
         ["ID compra", "Fecha", "Comercio", "Grupo", "Monto (S/)", "% cashback", "Cashback esperado (S/)"], compras,
         [11, 12, 14, 8, 12, 11, 22], {"B": "dd/mm/yyyy", "E": "#,##0.00", "G": "#,##0.00"})
    xlsx(os.path.join(base, A, "Cashback_abonado_Oct_Q2_2026.xlsx"), "Cashback abonado",
         ["ID compra", "Fecha de abono", "Cashback abonado (S/)"], abonos, [11, 15, 22], {"B": "dd/mm/yyyy", "C": "#,##0.00"})
    txt(os.path.join(base, A, "Prompt.txt"), C.PROMPT_CONCILIADOR)
    txt(os.path.join(base, A, "Como_usar_y_compartir.txt"), C.COMO_PUBLICAR)
    txt(os.path.join(base, B, "Resultados_esperados.txt"), "\n".join([
        "RESULTADOS ESPERADOS · CONCILIADOR · SEGUNDA QUINCENA DE OCTUBRE", C.AVISO, "",
        "Compras elegibles: %d filas · Abonos: %d filas" % (ce["compras"], ce["abonos"]),
        "Total esperado: %s · Total abonado: %s · Diferencia: %s" % (soles(ce["esperado"]), soles(ce["abonado"]), soles(ce["diferencia"])), "",
        "Compras sin abono (%d): %s" % (len(ce["sin_abono"]), ", ".join(ce["sin_abono"])),
        "Monto distinto (%d): %s · se abonó 0.5%% en vez de 1%%" % (len(ce["monto_distinto"]), ", ".join(ce["monto_distinto"])),
        "Abonos duplicados (%d): %s" % (len(ce["duplicado"]), ", ".join(ce["duplicado"])),
        "Abonos sin compra (%d): %s" % (len(ce["sin_compra"]), ", ".join(ce["sin_compra"])), "",
        "Es la misma lógica de la Skill de conciliación de la Sesión 1, ahora como herramienta que cualquiera usa sin chat."]))
    esp["conc"] = ce
    leeme(base, "KIT · MICRO-APP · CONCILIADOR VISUAL DE CASHBACK",
          "Que Operaciones cargue los dos Excel de la quincena y vea las diferencias resaltadas, sin cruzar nada a mano.",
          "Prompt.txt.\nLos dos Excel de la segunda quincena de octubre (tienen diferencias a propósito).\nComo_usar_y_compartir.txt.",
          "Resultados_esperados.txt: los totales y los ID de cada tipo de diferencia.",
          ["Abre un chat nuevo y pega Prompt.txt.", "En el artefacto, carga los dos Excel.",
           "Compara los totales y los ID con Resultados_esperados.txt.", "Prueba el botón «Descargar diferencias»."])

    # 4 · comisiones
    base = kit("ma4", pres, "Kit_Ejercicio_4_Calculadora_de_comisiones")
    txt(os.path.join(base, A, "Prompt.txt"), C.PROMPT_COMISIONES)
    txt(os.path.join(base, A, "Tarifario_de_comisiones.txt"), C.tarifario_txt())
    txt(os.path.join(base, A, "Como_usar_y_compartir.txt"), C.COMO_PUBLICAR)
    coms = []
    l = ["CASOS DE PRUEBA · CALCULADORA DE COMISIONES", C.AVISO, ""]
    for i, (rub, v, n) in enumerate(ESC_COM, 1):
        r = comision(rub, v, n)
        coms.append([rub, v, n, r])
        nota = []
        if r["desc"]:
            nota.append("descuento por volumen de %.2f puntos" % r["desc"])
        if r["minimo"]:
            nota.append("aplica la comisión mínima (%d × S/ 0.15)" % n)
        l += ["CASO %d · %s · ventas %s · %s transacciones" % (i, rub, soles(v), "{:,}".format(n)),
              "  Tasa aplicada: %.2f%%%s" % (r["tasa"], (" · " + ", ".join(nota)) if nota else ""),
              "  Comisión: %s · IGV: %s · Total descontado: %s" % (soles(r["comision"]), soles(r["igv"]), soles(r["total"])),
              "  Abono neto: %s" % soles(r["neto"]), ""]
    txt(os.path.join(base, B, "Casos_de_prueba_y_resultados.txt"), "\n".join(l))
    esp["com"] = coms
    leeme(base, "KIT · MICRO-APP · CALCULADORA DE COMISIONES",
          "Que el equipo de Comercios Afiliados le diga a un comercio, en segundos, cuánto pagará y cuánto recibirá.",
          "Prompt.txt (ya trae el tarifario adentro).\nTarifario_de_comisiones.txt: el tarifario de referencia.\nComo_usar_y_compartir.txt.",
          "Casos_de_prueba_y_resultados.txt: 4 casos; el 3 tiene descuento por volumen y el 4 la comisión mínima.",
          ["Abre un chat nuevo y pega Prompt.txt.", "Prueba los 4 casos y compara el abono neto.",
           "Si un caso no cuadra, dile a Claude qué regla no aplicó."])

    # 5 · clasificador
    base = kit("ma5", pres, "Kit_Ejercicio_5_Clasificador_de_reclamos")
    txt(os.path.join(base, A, "Prompt.txt"), C.PROMPT_CLASIFICADOR)
    txt(os.path.join(base, A, "Como_usar_y_compartir.txt"), C.COMO_PUBLICAR + "\n\nOJO: este artefacto usa a Claude por dentro. "
        "Quien lo abre desde el enlace usa su propia cuenta de Claude.")
    l = ["RECLAMOS DE PRUEBA · PÉGALOS DE UNO EN UNO", C.AVISO, ""]
    l2 = ["RESULTADOS ESPERADOS · CLASIFICADOR DE RECLAMOS", C.AVISO, "",
          "N°  Categoría                 Urgencia  Escalar"]
    for i, (t, cat, urg, esc) in enumerate(RECLAMOS_CLASIF, 1):
        l += ["RECLAMO %d" % i, t, ""]
        l2.append("%-3d %-25s %-9s %s" % (i, cat, urg, esc))
    l2 += ["", "En las respuestas revisa que: tutee, tenga máximo 100 palabras, no prometa devoluciones y no pida claves.",
           "El 7 es posible fraude: debe ir con urgencia Alta aunque no diga un monto."]
    txt(os.path.join(base, B, "Reclamos_de_prueba.txt"), "\n".join(l))
    txt(os.path.join(base, B, "Resultados_esperados.txt"), "\n".join(l2))
    esp["clasif"] = [(cat, urg, esc) for _, cat, urg, esc in RECLAMOS_CLASIF]
    leeme(base, "KIT · MICRO-APP · CLASIFICADOR DE RECLAMOS CON IA",
          "Una herramienta en la que Atención pega un reclamo y recibe la categoría, la urgencia, si se escala y la respuesta sugerida.",
          "Prompt.txt: el pedido (el artefacto usa a Claude por dentro).\nComo_usar_y_compartir.txt.",
          "Reclamos_de_prueba.txt: 8 reclamos.\nResultados_esperados.txt: la categoría, urgencia y escalar de cada uno.",
          ["Abre un chat nuevo y pega Prompt.txt.", "Pega los 8 reclamos de prueba, uno por uno.",
           "Compara con Resultados_esperados.txt: al menos 7 de 8 deben coincidir.", "Revisa 2 respuestas sugeridas completas."])
    return esp


# ================================================ skills, projects, design (09)
def kits_spd():
    pres = "Presentacion_09_Ejercicios_Skills_Projects_Design"

    base = kit("ej1", pres, "Kit_Ejercicio_1_Skill_Acta_de_reunion")
    skill_zip(os.path.join(base, A), C.SKILL_ACTAS)
    txt(os.path.join(base, A, "Prompt.txt"), "Usa la skill acta-de-reunion con estas notas:\n\n[pega aquí las notas]")
    txt(os.path.join(base, B, "Notas_reunion_1.txt"), C.NOTAS_REUNION_1)
    txt(os.path.join(base, B, "Notas_reunion_2_con_datos_faltantes.txt"), C.NOTAS_REUNION_2)
    txt(os.path.join(base, B, "Resultado_esperado.txt"), C.ESPERADO_ACTAS)
    leeme(base, "KIT · SKILL · ACTA DE REUNIÓN", "Que unas notas desordenadas salgan como acta con acuerdos, responsables y fechas, siempre con el mismo formato.",
          "acta-de-reunion.zip: la Skill lista para subir.\nSkill_..._(para_leer).txt: el mismo contenido para leerlo.\nPrompt.txt: el pedido.",
          "Notas_reunion_1.txt y Notas_reunion_2_con_datos_faltantes.txt.\nResultado_esperado.txt: qué acuerdos deben salir.",
          ["Sube la Skill: Configuración > Capacidades > Skills > Subir skill.", "En un chat nuevo pega Prompt.txt con las notas 1.",
           "Repite con las notas 2: debe poner «por definir» y no inventar responsables."])

    base = kit("ej2", pres, "Kit_Ejercicio_2_Skill_Reporte_semanal")
    skill_zip(os.path.join(base, A), C.SKILL_REPORTE)
    txt(os.path.join(base, A, "Prompt_con_conector.txt"), C.PROMPT_REPORTE_CONECTOR)
    txt(os.path.join(base, A, "Prompt_sin_conector.txt"), C.PROMPT_REPORTE_PEGADO)
    txt(os.path.join(base, A, "Correos_de_ejemplo.txt"), C.CORREOS_EJEMPLO)
    txt(os.path.join(base, B, "Resultado_esperado_con_correos_de_ejemplo.txt"), C.ESPERADO_REPORTE)
    leeme(base, "KIT · SKILL · REPORTE SEMANAL DESDE TUS CORREOS",
          "Que tu reporte semanal salga solo a partir de tus correos, siempre con las mismas 5 secciones.",
          "reporte-semanal-de-correos.zip: la Skill.\nPrompt_con_conector.txt: si tienes Microsoft 365 activo.\n"
          "Prompt_sin_conector.txt y Correos_de_ejemplo.txt: si no lo tienes.",
          "Resultado_esperado_con_correos_de_ejemplo.txt: qué debe salir con los 10 correos de ejemplo.",
          ["Sube la Skill.", "Primero hazlo con los correos de ejemplo (Prompt_sin_conector.txt) y compara.",
           "Después, con el conector activo, pega Prompt_con_conector.txt para tu semana real."])

    base = kit("ej3", pres, "Kit_Ejercicio_3_Project_Comercios_afiliados")
    txt(os.path.join(base, A, "00_Instrucciones_del_Project.txt"), C.PC_INSTR)
    txt(os.path.join(base, A, "01_Condiciones_de_afiliacion.txt"), C.PC_CONDICIONES)
    txt(os.path.join(base, A, "02_Tarifario_de_comisiones.txt"), C.tarifario_txt())
    txt(os.path.join(base, A, "03_Proceso_de_onboarding.txt"), C.PC_ONBOARDING)
    txt(os.path.join(base, A, "04_Preguntas_frecuentes_comercios.txt"), C.PC_FAQ)
    txt(os.path.join(base, B, "Preguntas_de_prueba_y_respuestas.txt"), C.PC_PRUEBAS)
    leeme(base, "KIT · PROJECT · COMERCIOS AFILIADOS",
          "Un Project que responde a comercios con las condiciones, el tarifario y el onboarding de Sip, citando el documento.",
          "00_Instrucciones_del_Project.txt: va en Instrucciones.\n01 a 04: los documentos que subes al Project.",
          "Preguntas_de_prueba_y_respuestas.txt: 5 preguntas con lo que debería responder; la 5 es trampa.",
          ["Projects > Nuevo proyecto: «Comercios afiliados · Sip».", "Pega las instrucciones y sube los 4 documentos.",
           "Abre un chat dentro del Project y haz las 5 preguntas en orden."])

    base = kit("ej4", pres, "Kit_Ejercicio_4_Project_Riesgo_y_cumplimiento")
    txt(os.path.join(base, A, "00_Instrucciones_del_Project.txt"), C.PR_INSTR)
    txt(os.path.join(base, A, "01_Politica_de_prevencion_de_fraude.txt"), C.PR_FRAUDE)
    txt(os.path.join(base, A, "02_Politica_de_datos_personales.txt"), C.PR_DATOS)
    txt(os.path.join(base, A, "03_Procedimiento_de_reclamos.txt"), C.PR_RECLAMOS)
    txt(os.path.join(base, B, "Preguntas_de_prueba_y_respuestas.txt"), C.PR_PRUEBAS)
    leeme(base, "KIT · PROJECT · RIESGO Y CUMPLIMIENTO",
          "Un Project al que cualquiera le pregunta qué dice la política, con el documento y la sección.",
          "00_Instrucciones_del_Project.txt y las 3 políticas de ejemplo (01 a 03).",
          "Preguntas_de_prueba_y_respuestas.txt: 5 casos; la 5 es trampa.",
          ["Crea el Project «Riesgo y cumplimiento · Sip».", "Pega las instrucciones y sube las 3 políticas.",
           "Haz las 5 preguntas: cada respuesta debe citar documento y sección."])

    base = kit("ej5", pres, "Kit_Ejercicio_5_Design_Banner_de_promo")
    txt(os.path.join(base, A, "Prompt.txt"), C.PROMPT_BANNER)
    txt(os.path.join(base, A, "Brief_Navidad_te_devuelve.txt"), C.BRIEF_BANNER)
    txt(os.path.join(base, A, "Identidad_visual_Sip.txt"), C.IDENTIDAD)
    shutil.copy2(os.path.join(DS, "logo_sip.png"), os.path.join(base, A, "logo_sip.png"))
    txt(os.path.join(base, B, "Checklist_de_revision.txt"), C.CHECK_BANNER)
    leeme(base, "KIT · DESIGN · BANNER DE UNA PROMO DE CASHBACK",
          "Las 2 piezas de la campaña «Navidad te devuelve» (banner de la app e historia de Instagram) con la identidad de Sip.",
          "Prompt.txt, el brief, la ficha de identidad y el logo de Sip.", "Checklist_de_revision.txt: 7 controles.",
          ["Abre Claude Design.", "Sube el brief, la ficha y el logo.", "Pega Prompt.txt.", "Revisa las 2 piezas con el checklist."])

    base = kit("ej6", pres, "Kit_Ejercicio_6_Design_Pantalla_de_la_app")
    txt(os.path.join(base, A, "Prompt.txt"), C.PROMPT_PANTALLA)
    txt(os.path.join(base, A, "Brief_pantalla_Mis_cashbacks.txt"), C.BRIEF_PANTALLA)
    txt(os.path.join(base, A, "Identidad_visual_Sip.txt"), C.IDENTIDAD)
    os.makedirs(os.path.join(base, A, "capturas_sip"), exist_ok=True)
    for f in ("sip_captura_1_hero.jpg", "sip_captura_2_productos.jpg", "sip_captura_3_mundo_digital.jpg"):
        shutil.copy2(os.path.join(DS, f), os.path.join(base, A, "capturas_sip", f))
    shutil.copy2(os.path.join(DS, "logo_sip.png"), os.path.join(base, A, "logo_sip.png"))
    txt(os.path.join(base, B, "Checklist_de_revision.txt"), C.CHECK_PANTALLA)
    leeme(base, "KIT · DESIGN · PANTALLA NUEVA DE LA APP",
          "El prototipo interactivo de la pantalla «Mis cashbacks» para celular, con el estilo de la app Sip.",
          "Prompt.txt, el brief de la pantalla, la ficha de identidad, el logo y 3 capturas de sip.pe.",
          "Checklist_de_revision.txt: 7 controles (incluye probar los filtros).",
          ["Abre Claude Design.", "Sube el brief, la ficha, el logo y las 3 capturas.", "Pega Prompt.txt.",
           "Prueba los filtros y revisa con el checklist."])


# ===================================================== chrome y cowork (10)
PROVEEDORES = [("Imprenta La Prensa S.A.C.", "20512345671", "ImprentaLaPrensa", "Impresión de volantes y afiches de campaña"),
               ("Servicios Gráficos Andinos S.A.C.", "20498765432", "ServiciosGraficosAndinos", "Diseño e impresión de material POP"),
               ("Limpieza Total Perú S.A.C.", "20605544332", "LimpiezaTotalPeru", "Servicio de limpieza de oficinas"),
               ("Courier Rápido Express S.A.C.", "20556677881", "CourierRapidoExpress", "Envío de tarjetas a clientes"),
               ("Cafetería Buen Día E.I.R.L.", "20601122334", "CafeteriaBuenDia", "Refrigerios para capacitación")]
NOMBRES_FEOS = ["scan0001.pdf", "factura (2).pdf", "IMG_2034.pdf", "doc nuevo.pdf", "comprobante final.pdf",
                "Factura_octubre.pdf", "scan0007.pdf", "WhatsApp PDF 2026-10-14.pdf", "factura.pdf", "archivo(1).pdf",
                "Documento escaneado.pdf", "FACT 0412.pdf", "pago courier.pdf", "scan0012.pdf"]


def html_pdf(html_, dst):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html_)
        src = f.name
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    "--print-to-pdf=" + dst, "file://" + src], capture_output=True)
    os.unlink(src)


def html_doc(tipo, prov, ruc, num, fecha, concepto, sub, nota=""):
    igv = round(sub * 0.18, 2)
    return ("<html><head><meta charset='utf-8'><style>body{font-family:Arial;margin:50px;color:#222}"
            "h1{font-size:22px;margin:0}table{border-collapse:collapse;width:100%%;margin-top:24px}"
            "td{border:1px solid #999;padding:8px;font-size:13px}.box{border:2px solid #222;padding:12px;float:right;text-align:center}"
            "</style></head><body><div class='box'><b>RUC %s</b><br>%s<br><b>%s</b></div>"
            "<h1>%s</h1><p>Av. Ejemplo 123, Lima · Documento ficticio para práctica</p>"
            "<p style='clear:both;margin-top:40px'><b>Cliente:</b> SIP (billetera digital) · <b>Fecha de emisión:</b> %s</p>"
            "<table><tr><td><b>Concepto</b></td><td><b>Importe</b></td></tr><tr><td>%s</td><td>S/ %s</td></tr>"
            "<tr><td>Subtotal</td><td>S/ %s</td></tr><tr><td>IGV 18%%</td><td>S/ %s</td></tr>"
            "<tr><td><b>Total</b></td><td><b>S/ %s</b></td></tr></table><p>%s</p></body></html>"
            % (ruc, tipo, num, prov, fecha.strftime("%d/%m/%Y"), concepto, "{:,.2f}".format(sub), "{:,.2f}".format(sub),
               "{:,.2f}".format(igv), "{:,.2f}".format(sub + igv), nota))


def comprobantes(dst):
    rnd = random.Random(1410)
    facts = []
    for i in range(13):
        p = PROVEEDORES[i % 5]
        f = date(2026, 10, 1) + timedelta(days=rnd.randint(0, 27))
        sub = round(rnd.uniform(180, 4200), 2)
        num = "F001-%04d" % rnd.randint(100, 980)
        facts.append({"prov": p[0], "ruc": p[1], "corto": p[2], "concepto": p[3], "fecha": f, "num": num, "sub": sub,
                      "igv": round(sub * .18, 2), "total": round(sub + round(sub * .18, 2), 2)})
    os.makedirs(dst, exist_ok=True)
    nombres = list(NOMBRES_FEOS)
    for i, fa in enumerate(facts):
        fa["archivo"] = nombres[i]
        fa["nuevo"] = "%s_%s_%s.pdf" % (fa["fecha"].isoformat(), fa["corto"], fa["num"])
        html_pdf(html_doc("FACTURA ELECTRÓNICA", fa["prov"], fa["ruc"], fa["num"], fa["fecha"], fa["concepto"], fa["sub"]),
                 os.path.join(dst, fa["archivo"]))
    # una cotizacion (no es factura) y una copia repetida
    html_pdf(html_doc("COTIZACIÓN", PROVEEDORES[0][0], PROVEEDORES[0][1], "COT-2026-118", date(2026, 10, 20),
                      "Impresión de afiches de Navidad", 2650.00, "Esta cotización no es un comprobante de pago."),
             os.path.join(dst, nombres[13]))
    shutil.copy2(os.path.join(dst, facts[2]["archivo"]), os.path.join(dst, "IMG_2034 (copia).pdf"))
    por = {}
    for fa in facts:
        a = por.setdefault(fa["prov"], [0, 0.0])
        a[0] += 1
        a[1] += fa["total"]
    return facts, por, [nombres[13], "IMG_2034 (copia).pdf"]


def semanas_cowork(dst):
    rnd = random.Random(2510)
    tipos = [("Pago QR", 410, 62), ("Compra con tarjeta", 330, 95), ("Transferencia", 280, 210),
             ("Pago de servicios", 150, 120), ("Recarga celular", 120, 14)]
    rangos = [(1, 7), (8, 14), (15, 21), (22, 31)]
    resumen = []
    os.makedirs(dst, exist_ok=True)
    por_tipo = {}
    for s, (d0, d1) in enumerate(rangos, 1):
        filas = []
        for d in range(d0, d1 + 1):
            for t, ops, tick in tipos:
                for canal, w in (("App", .86), ("Web", .14)):
                    o = max(1, int(ops * w * rnd.uniform(.8, 1.25) * (1.15 if s == 4 else 1)))
                    m = round(o * tick * rnd.uniform(.9, 1.1), 2)
                    filas.append([date(2026, 10, d), canal, t, o, m])
                    pt = por_tipo.setdefault(t, [0, 0.0])
                    pt[0] += o
                    pt[1] += m
        xlsx(os.path.join(dst, "Operaciones_semana_%d_octubre.xlsx" % s), "Operaciones",
             ["Fecha", "Canal", "Tipo", "Operaciones", "Monto (S/)"], filas, [12, 8, 20, 12, 14],
             {"A": "dd/mm/yyyy", "E": "#,##0.00"})
        resumen.append({"semana": s, "filas": len(filas), "ops": sum(f[3] for f in filas),
                        "monto": round(sum(f[4] for f in filas), 2)})
    txt(os.path.join(dst, "Notas_del_equipo.txt"), "\n".join([
        "NOTAS DEL EQUIPO · OCTUBRE 2026", C.AVISO, "",
        "- 06/10: caída del pago con QR entre 19:00 y 19:40 por mantenimiento del proveedor.",
        "- 13/10: se activó «Octubre sipeado» con sorteo semanal en la app.",
        "- 20/10: lentitud en transferencias por la mañana; se resolvió a las 11:15.",
        "- 27/10: pico de recargas por campaña de un operador móvil.",
        "- 31/10: la semana 4 tiene 10 días (del 22 al 31)."]))
    for i, r in enumerate(resumen):
        r["var"] = None if i == 0 else round((r["monto"] / resumen[i - 1]["monto"] - 1) * 100, 1)
    return resumen, {k: [v[0], round(v[1], 2)] for k, v in sorted(por_tipo.items(), key=lambda x: -x[1][1])}


def kits_chrome_cowork():
    pres = "Presentacion_10_Ejercicios_Chrome_y_Cowork"
    esp = {}

    base = kit("ch1", pres, "Kit_Ejercicio_1_Chrome_Llenar_un_formulario")
    txt(os.path.join(base, A, "Prompt.txt"), C.prompt_formulario())
    txt(os.path.join(base, A, "Comercios_por_afiliar.txt"), C.tabla_comercios())
    xlsx(os.path.join(base, A, "Comercios_por_afiliar.xlsx"), "Comercios",
         ["RUC", "Razón social", "Nombre comercial", "Rubro", "Distrito", "Correo", "Teléfono", "Ventas mensuales (S/)"],
         [[c["ruc"], c["razon"], c["nombre"], c["rubro"], c["distrito"], c["correo"], c["telefono"], c["ventas"]]
          for c in C.COMERCIOS_FORM], [14, 44, 20, 32, 24, 34, 12, 18], {"H": "#,##0"}, [C.AVISO])
    txt(os.path.join(base, A, "Como_instalar_Claude_en_Chrome.txt"), C.INSTALAR_CHROME)
    cods = [(c["nombre"], c["ruc"], C.codigo_afiliacion(c["ruc"])) for c in C.COMERCIOS_FORM]
    txt(os.path.join(base, B, "Resultados_esperados.txt"), "\n".join(
        ["RESULTADOS ESPERADOS · FORMULARIO DE AFILIACIÓN", C.AVISO, "",
         "Cada comercio enviado muestra un código de solicitud. Deben salir estos 3:"]
        + ["  %-12s RUC %s · %s" % c for c in cods]
        + ["", "Abajo del formulario aparece la lista «Solicitudes enviadas»: deben ser 3, con los datos de la tabla.",
           "Si sale un código distinto, algún dato del RUC se escribió mal."]))
    esp["form"] = cods
    leeme(base, "KIT · CLAUDE EN CHROME · LLENAR UN FORMULARIO",
          "Que Claude registre 3 comercios en un formulario web, campo por campo, mientras tú miras.",
          "Prompt.txt: el pedido con el enlace del formulario y los datos de los 3 comercios.\n"
          "Comercios_por_afiliar (.xlsx y .txt): los mismos datos.\nComo_instalar_Claude_en_Chrome.txt.",
          "Resultados_esperados.txt: los 3 códigos de solicitud que deben salir.",
          ["Instala la extensión (Como_instalar_Claude_en_Chrome.txt).", "Abre el panel de Claude en Chrome y pega Prompt.txt.",
           "Mira cómo llena cada campo y compara los códigos con Resultados_esperados.txt."])

    base = kit("ch2", pres, "Kit_Ejercicio_2_Chrome_Webs_de_la_competencia")
    txt(os.path.join(base, A, "Prompt.txt"), C.PROMPT_WEB_COMPETENCIA)
    txt(os.path.join(base, A, "Como_instalar_Claude_en_Chrome.txt"), C.INSTALAR_CHROME)
    txt(os.path.join(base, B, "Checklist_de_revision.txt"), C.CHECK_WEB)
    leeme(base, "KIT · CLAUDE EN CHROME · WEBS DE LA COMPETENCIA",
          "Que Claude recorra las webs oficiales de 4 billeteras y arme una tabla de beneficios con el enlace de cada dato.",
          "Prompt.txt: el pedido con las 4 webs.\nComo_instalar_Claude_en_Chrome.txt.", "Checklist_de_revision.txt: 6 controles.",
          ["Abre el panel de Claude en Chrome y pega Prompt.txt.", "Dale permiso para cada sitio cuando lo pida.",
           "Revisa la tabla con el checklist y abre 2 enlaces."])

    base = kit("cw1", pres, "Kit_Ejercicio_3_Cowork_Ordenar_comprobantes")
    facts, por, revisar = comprobantes(os.path.join(base, A, "Comprobantes_octubre"))
    txt(os.path.join(base, A, "Prompt.txt"), C.PROMPT_COMPROBANTES)
    txt(os.path.join(base, A, "Como_preparar_Cowork.txt"), C.INSTALAR_COWORK)
    total = round(sum(f["total"] for f in facts), 2)
    l = ["RESULTADOS ESPERADOS · ORDENAR COMPROBANTES", C.AVISO, "",
         "La carpeta tiene 15 PDF: 13 facturas, 1 cotización y 1 copia repetida.", "",
         "FACTURAS (nombre original → nombre nuevo · total)"]
    l += ["  %-30s → %s · %s" % (f["archivo"], f["nuevo"], soles(f["total"])) for f in sorted(facts, key=lambda x: x["fecha"])]
    l += ["", "A «Revisar» (2): %s (es una cotización) y %s (copia de %s)" % (revisar[0], revisar[1], facts[2]["archivo"]), "",
          "TOTAL POR PROVEEDOR"]
    l += ["  %-36s %d facturas · %s" % (k, v[0], soles(v[1])) for k, v in sorted(por.items())]
    l += ["", "Total general de las 13 facturas: %s" % soles(total)]
    txt(os.path.join(base, B, "Resultados_esperados.txt"), "\n".join(l))
    esp["comp"] = {"facturas": len(facts), "total": total, "proveedores": len(por)}
    leeme(base, "KIT · COWORK · ORDENAR Y RENOMBRAR COMPROBANTES",
          "Que Claude lea 15 PDF con nombres desordenados, los renombre, los ordene por proveedor y arme el Excel resumen.",
          "Comprobantes_octubre/: la carpeta con los 15 PDF (ficticios).\nPrompt.txt.\nComo_preparar_Cowork.txt.",
          "Resultados_esperados.txt: el nombre nuevo de cada factura, lo que va a «Revisar» y los totales.",
          ["Descomprime el kit en tu Escritorio.", "En Cowork, dale acceso a la carpeta Comprobantes_octubre.",
           "Pega Prompt.txt.", "Compara los nombres y totales con Resultados_esperados.txt."])

    base = kit("cw2", pres, "Kit_Ejercicio_4_Cowork_Reporte_desde_varios_archivos")
    sem, tipo = semanas_cowork(os.path.join(base, A, "Reporte_octubre"))
    txt(os.path.join(base, A, "Prompt.txt"), C.PROMPT_REPORTE_COWORK)
    txt(os.path.join(base, A, "Como_preparar_Cowork.txt"), C.INSTALAR_COWORK)
    ops = sum(s["ops"] for s in sem)
    monto = round(sum(s["monto"] for s in sem), 2)
    mx = max(sem, key=lambda s: s["monto"])
    mn = min(sem, key=lambda s: s["monto"])
    l = ["RESULTADOS ESPERADOS · REPORTE MENSUAL DE OCTUBRE", C.AVISO, "",
         "Filas por archivo: " + " · ".join("semana %d: %d" % (s["semana"], s["filas"]) for s in sem),
         "Total del mes: %s operaciones · %s" % ("{:,}".format(ops), soles(monto)), "", "POR SEMANA"]
    l += ["  Semana %d · %s operaciones · %s%s" % (s["semana"], "{:,}".format(s["ops"]), soles(s["monto"]),
                                                  "" if s["var"] is None else " · %+.1f%%" % s["var"]) for s in sem]
    l += ["", "Mayor monto: semana %d · Menor monto: semana %d" % (mx["semana"], mn["semana"]),
          "(Ojo: la semana 4 tiene 10 días; un buen reporte lo menciona.)", "", "POR TIPO"]
    l += ["  %-20s %s operaciones · %s" % (k, "{:,}".format(v[0]), soles(v[1])) for k, v in tipo.items()]
    l += ["", "INCIDENCIAS: las 5 de Notas_del_equipo.txt."]
    txt(os.path.join(base, B, "Resultados_esperados.txt"), "\n".join(l))
    esp["rep"] = {"ops": ops, "monto": monto, "semanas": sem}
    leeme(base, "KIT · COWORK · REPORTE DESDE VARIOS ARCHIVOS",
          "Que Claude junte 4 Excel semanales y unas notas en un reporte mensual en Word, más un Excel consolidado.",
          "Reporte_octubre/: 4 Excel semanales y Notas_del_equipo.txt.\nPrompt.txt.\nComo_preparar_Cowork.txt.",
          "Resultados_esperados.txt: totales por semana y por tipo para comparar.",
          ["Descomprime el kit en tu Escritorio.", "En Cowork, dale acceso a la carpeta Reporte_octubre.",
           "Pega Prompt.txt.", "Abre el Word y compara 3 cifras con Resultados_esperados.txt."])
    return esp


def zipear():
    out = {}
    for clave, (pres, nombre) in KITS.items():
        base = os.path.join(MAT, pres)
        z = os.path.join(base, nombre + ".zip")
        with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
            for r, _, fs in os.walk(os.path.join(base, nombre)):
                for f in sorted(fs):
                    p = os.path.join(r, f)
                    zf.write(p, os.path.relpath(p, base))
        shutil.rmtree(os.path.join(base, nombre))
        out[clave] = "materiales/%s/%s.zip" % (pres, nombre)
    return out


def main():
    if os.path.isdir(MAT):
        shutil.rmtree(MAT)
    kits_outlook()
    kit_segunda_skill()
    kits_research()
    esp = kits_microapps()
    kits_spd()
    esp.update(kits_chrome_cowork())
    rutas = zipear()
    json.dump({"rutas": rutas, **esp}, open(os.path.join(HERE, "esperados2.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1, default=str)
    print("%d kits" % len(rutas))
    print("reclamos: %d · fuera de plazo %.1f%%" % (esp["rec"]["total"], esp["rec"]["pct_fuera"]))
    print("conciliacion: diferencia %s" % soles(esp["conc"]["diferencia"]))
    print("comprobantes: %d facturas · %s" % (esp["comp"]["facturas"], soles(esp["comp"]["total"])))


if __name__ == "__main__":
    main()
