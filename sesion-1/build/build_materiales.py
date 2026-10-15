#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera los kits de la Sesion 1 de SIP en ../materiales/Presentacion_<NN>_<deck>/<Kit>/ + un .zip por kit.
Formato de cada kit: LEEME.txt + 1_Para_construir/ + 2_Para_probar/. Todo en .txt (las Skills van ademas
como .zip con su SKILL.md, que es el formato que Claude pide para subirlas).
Escribe esperados.json para que build_decks.py muestre los resultados sin copiarlos a mano.
Requiere openpyxl.   Uso:  python3 build_materiales.py
"""
import json
import os
import random
import shutil
import zipfile
from datetime import date, timedelta

import openpyxl
from openpyxl.styles import Font, PatternFill

import contenido as C

HERE = os.path.dirname(os.path.abspath(__file__))
MAT = os.path.abspath(os.path.join(HERE, "..", "materiales"))
A, B = "1_Para_construir", "2_Para_probar"

KITS = {}   # clave -> (carpeta de presentacion, nombre del kit)


def kit(clave, pres, nombre):
    KITS[clave] = (pres, nombre)
    return os.path.join(MAT, pres, nombre)


def txt(path, texto):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(texto.strip() + "\n")


def leeme(base, titulo, para_que, construir, probar, pasos):
    t = "%s\n%s\n%s\n\nPARA QUÉ SIRVE\n%s\n\n%s\n%s\n\n%s\n%s\n\nCÓMO USARLO\n%s" % (
        titulo, "=" * len(titulo), C.AVISO, para_que, A, construir, B, probar,
        "\n".join("%d. %s" % (i + 1, p) for i, p in enumerate(pasos)))
    txt(os.path.join(base, "LEEME.txt"), t)


def hoja(ws, cols, filas, anchos, fmt=None):
    ws.append(cols)
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="1B1B1D")
    for f in filas:
        ws.append(list(f))
    for i, w in enumerate(anchos):
        ws.column_dimensions[openpyxl.utils.get_column_letter(i + 1)].width = w
    for col, nf in (fmt or {}).items():
        for c in ws[col][1:]:
            c.number_format = nf
    ws.freeze_panes = "A2"


def skill_zip(dst_dir, sk):
    """Paquete de Skill: <slug>/SKILL.md dentro de un .zip, listo para subir a Claude."""
    md = "---\nname: %s\ndescription: %s\n---\n\n%s" % (sk["slug"], sk["desc"], sk["cuerpo"].strip() + "\n")
    os.makedirs(dst_dir, exist_ok=True)
    with zipfile.ZipFile(os.path.join(dst_dir, sk["slug"] + ".zip"), "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("%s/SKILL.md" % sk["slug"], md)
    txt(os.path.join(dst_dir, "Skill_%s_(para_leer).txt" % sk["slug"].replace("-", "_")), md)


# ------------------------------------------------------------- datasets ---
GRUPO = ["plazaVea", "Inkafarma", "Mass", "Makro", "Oechsle", "Promart"]
VISA = ["Tottus", "Wong", "Metro", "Falabella", "Ripley", "Rappi", "Cineplanet", "Starbucks"]


def transacciones():
    rnd = random.Random(1015)
    tipos = [("Pago QR", .30), ("Compra con tarjeta", .27), ("Transferencia", .22),
             ("Pago de servicios", .13), ("Recarga celular", .08)]
    regiones = [("Lima", .55), ("Norte", .17), ("Sur", .14), ("Centro", .08), ("Oriente", .06)]
    filas = []
    for i in range(800):
        f = date(2026, 9, 1) + timedelta(days=rnd.randint(0, 29))
        tipo = rnd.choices([t for t, _ in tipos], [w for _, w in tipos])[0]
        reg = rnd.choices([r for r, _ in regiones], [w for _, w in regiones])[0]
        canal = "App" if rnd.random() < .86 else "Web"
        cli = "Nuevo" if rnd.random() < .27 else "Recurrente"
        if tipo in ("Pago QR", "Compra con tarjeta"):
            g = rnd.random() < .58
            com = rnd.choice(GRUPO if g else VISA)
            grupo = "Grupo" if g else "Visa"
            monto = round(rnd.uniform(12, 480), 2)
            cb = round(monto * (0.01 if g else 0.005), 2)
        else:
            com, grupo, cb = "—", "—", 0.0
            monto = {"Transferencia": round(rnd.uniform(20, 900), 2),
                     "Pago de servicios": round(rnd.uniform(35, 260), 2),
                     "Recarga celular": float(rnd.choice([5, 10, 15, 20, 30]))}[tipo]
        filas.append(["", f, tipo, com, grupo, canal, reg, monto, cb, cli])
    filas.sort(key=lambda x: x[1])
    for i, f in enumerate(filas):
        f[0] = "T-%05d" % (i + 1)
    return filas


def reclamos():
    rnd = random.Random(2026)
    motivos = [("Cashback no abonado", .27), ("Cobro no reconocido", .21), ("Transferencia no llegó", .17),
               ("Pase a cuotas", .12), ("Bloqueo de cuenta", .10), ("Atención en módulo", .08), ("Otros", .05)]
    canal_dias = {"App": (3, 9), "Web": (4, 11), "Módulo de Atención": (2, 7), "Teléfono": (5, 13)}
    canales = [("App", .48), ("Web", .17), ("Módulo de Atención", .22), ("Teléfono", .13)]
    prod = {"Cashback no abonado": "Billetera", "Cobro no reconocido": "Tarjeta de crédito",
            "Transferencia no llegó": "Billetera", "Pase a cuotas": "Tarjeta de crédito",
            "Bloqueo de cuenta": "Billetera", "Atención en módulo": "Atención", "Otros": "Otros"}
    n_mes = {7: 72, 8: 81, 9: 97}
    filas = []
    for mes, n in n_mes.items():
        for _ in range(n):
            f = date(2026, mes, rnd.randint(1, 30 if mes == 9 else 31))
            mot = rnd.choices([m for m, _ in motivos], [w for _, w in motivos])[0]
            can = rnd.choices([c for c, _ in canales], [w for _, w in canales])[0]
            lo, hi = canal_dias[can]
            dias = rnd.randint(lo, hi)
            if mes == 9 and f.day > 22 and rnd.random() < .6:
                est, dias = "En proceso", None
            else:
                est = "Resuelto a favor" if rnd.random() < .58 else "Resuelto en contra"
            filas.append(["", f, {7: "Julio", 8: "Agosto", 9: "Septiembre"}[mes], mot, prod[mot], can, dias, est])
    filas.sort(key=lambda x: x[1])
    for i, f in enumerate(filas):
        f[0] = "R-%04d" % (i + 1)
    return filas


def xlsx_transacciones(path, filas):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Transacciones"
    hoja(ws, ["ID", "Fecha", "Tipo", "Comercio", "Grupo", "Canal", "Región", "Monto (S/)", "Cashback (S/)", "Cliente"],
         filas, [10, 12, 20, 14, 8, 8, 10, 12, 13, 12], {"B": "dd/mm/yyyy", "H": "#,##0.00", "I": "#,##0.00"})
    n = wb.create_sheet("Notas")
    for t in ["Transacciones de la billetera · Septiembre 2026", C.AVISO,
              "Archivo anonimizado: sin nombres, DNI ni números de tarjeta."]:
        n.append([t])
    n.column_dimensions["A"].width = 110
    os.makedirs(os.path.dirname(path), exist_ok=True)
    wb.save(path)


def xlsx_reclamos(path, filas):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Reclamos"
    hoja(ws, ["ID", "Fecha", "Mes", "Motivo", "Producto", "Canal de ingreso", "Días de respuesta", "Estado"],
         filas, [9, 12, 12, 24, 18, 20, 17, 20], {"B": "dd/mm/yyyy"})
    n = wb.create_sheet("Notas")
    for t in ["Reclamos del tercer trimestre 2026", C.AVISO,
              "Días de respuesta vacío = reclamo en proceso. Sin datos personales de clientes."]:
        n.append([t])
    n.column_dimensions["A"].width = 110
    os.makedirs(os.path.dirname(path), exist_ok=True)
    wb.save(path)


def esperados_tx(f):
    def s(it):
        return round(sum(it), 2)
    por_tipo = {}
    for r in f:
        t = por_tipo.setdefault(r[2], [0, 0.0])
        t[0] += 1
        t[1] += r[7]
    cb_com = {}
    for r in f:
        if r[8]:
            cb_com[r[3]] = cb_com.get(r[3], 0) + r[8]
    seg = {k: s(r[7] for r in f if r[9] == k) for k in ("Nuevo", "Recurrente")}
    reg = {}
    for r in f:
        a = reg.setdefault(r[6], [0, 0.0])
        a[0] += 1
        a[1] += r[7]
    tick = {k: round(v[1] / v[0], 2) for k, v in reg.items()}
    return {"filas": len(f), "monto": s(r[7] for r in f), "cashback": s(r[8] for r in f),
            "por_tipo": {k: [v[0], round(v[1], 2)] for k, v in sorted(por_tipo.items(), key=lambda x: -x[1][1])},
            "top_cashback": [[k, round(v, 2)] for k, v in sorted(cb_com.items(), key=lambda x: -x[1])[:3]],
            "segmento": seg, "ticket_region": dict(sorted(tick.items(), key=lambda x: -x[1]))}


def esperados_rc(f):
    mes = {}
    for r in f:
        mes[r[2]] = mes.get(r[2], 0) + 1
    mot = {}
    for r in f:
        mot[r[3]] = mot.get(r[3], 0) + 1
    can = {}
    for r in f:
        if r[6] is not None:
            a = can.setdefault(r[5], [0, 0])
            a[0] += 1
            a[1] += r[6]
    return {"filas": len(f), "por_mes": mes,
            "top_motivos": sorted(mot.items(), key=lambda x: -x[1])[:3],
            "dias_por_canal": {k: round(v[1] / v[0], 1) for k, v in sorted(can.items(), key=lambda x: x[1][1] / x[1][0])},
            "en_proceso": sum(1 for r in f if r[7] == "En proceso")}


def texto_esperados_tx(e):
    l = ["RESULTADOS ESPERADOS · TRANSACCIONES SEPTIEMBRE 2026", C.AVISO, "",
         "Filas: %d · Monto total: S/ {:,.2f} · Cashback total: S/ {:,.2f}".format(e["monto"], e["cashback"]) % e["filas"], "",
         "Por tipo (operaciones · monto):"]
    l += ["  %-20s %4d · S/ {:,.2f}".format(v[1]) % (k, v[0]) for k, v in e["por_tipo"].items()]
    l += ["", "Top 3 comercios por cashback:"] + ["  %s · S/ {:,.2f}".format(v) % k for k, v in e["top_cashback"]]
    l += ["", "Monto por segmento:"] + ["  %s · S/ {:,.2f}".format(v) % k for k, v in e["segmento"].items()]
    l += ["", "Ticket promedio por región:"] + ["  %s · S/ {:,.2f}".format(v) % k for k, v in e["ticket_region"].items()]
    return "\n".join(l)


def texto_esperados_rc(e):
    l = ["RESULTADOS ESPERADOS · RECLAMOS T3 2026", C.AVISO, "", "Total: %d reclamos" % e["filas"], "", "Por mes:"]
    l += ["  %s · %d" % (k, v) for k, v in e["por_mes"].items()]
    l += ["", "Top 3 motivos:"] + ["  %s · %d" % (k, v) for k, v in e["top_motivos"]]
    l += ["", "Días promedio de respuesta por canal (solo resueltos):"] + ["  %s · %.1f" % (k, v) for k, v in e["dias_por_canal"].items()]
    l += ["", "En proceso: %d" % e["en_proceso"]]
    return "\n".join(l)


def conciliacion():
    """Dos archivos que no cuadran a proposito: compras elegibles a cashback y cashback abonado."""
    rnd = random.Random(1510)
    compras = []
    for i in range(120):
        f = date(2026, 10, 1) + timedelta(days=rnd.randint(0, 14))
        g = rnd.random() < .6
        com = rnd.choice(GRUPO if g else VISA)
        monto = round(rnd.uniform(15, 520), 2)
        pct = 0.01 if g else 0.005
        compras.append(["", f, com, "Grupo" if g else "Visa", monto, "%.1f%%" % (pct * 100), round(monto * pct, 2)])
    compras.sort(key=lambda x: x[1])
    for i, c in enumerate(compras):
        c[0] = "CB-%04d" % (5001 + i)
    faltan = set(rnd.sample(range(120), 6))
    mal = set(rnd.sample([i for i in range(120) if i not in faltan and compras[i][3] == "Grupo"], 4))
    abonos, dif = [], []
    for i, c in enumerate(compras):
        if i in faltan:
            continue
        ab = round(c[4] * 0.005, 2) if i in mal else c[6]
        abonos.append([c[0], c[1] + timedelta(days=rnd.randint(2, 6)), ab])
    dup = abonos[rnd.randint(10, 60)]
    abonos.append([dup[0], dup[1], dup[2]])
    abonos.append(["CB-5199", date(2026, 10, 9), 3.15])
    abonos.append(["CB-5207", date(2026, 10, 12), 1.80])
    abonos.sort(key=lambda x: x[1])
    esp = {"compras": len(compras), "abonos": len(abonos),
           "sin_abono": sorted(compras[i][0] for i in faltan),
           "monto_distinto": sorted(compras[i][0] for i in mal),
           "duplicado": dup[0], "sin_compra": ["CB-5199", "CB-5207"],
           "esperado": round(sum(c[6] for c in compras), 2), "abonado": round(sum(a[2] for a in abonos), 2)}
    return compras, abonos, esp


def xlsx_conciliacion(dst, compras, abonos):
    os.makedirs(dst, exist_ok=True)
    wb = openpyxl.Workbook(); ws = wb.active; ws.title = "Compras elegibles"
    hoja(ws, ["ID compra", "Fecha", "Comercio", "Grupo", "Monto (S/)", "% cashback", "Cashback esperado (S/)"],
         compras, [11, 12, 14, 8, 12, 11, 22], {"B": "dd/mm/yyyy", "E": "#,##0.00", "G": "#,##0.00"})
    a = os.path.join(dst, "Compras_elegibles_cashback_Oct_2026.xlsx"); wb.save(a)
    wb = openpyxl.Workbook(); ws = wb.active; ws.title = "Cashback abonado"
    hoja(ws, ["ID compra", "Fecha de abono", "Cashback abonado (S/)"], abonos, [11, 15, 22],
         {"B": "dd/mm/yyyy", "C": "#,##0.00"})
    b = os.path.join(dst, "Cashback_abonado_Oct_2026.xlsx"); wb.save(b)
    return a, b


# ----------------------------------------------------------------- kits ---
def kits_skills(conc):
    pres = "Presentacion_05_Skills"
    base = kit("sk1", pres, "Kit_Caso_1_Respuesta_a_reclamos")
    skill_zip(os.path.join(base, A), C.SKILL_RECLAMOS)
    txt(os.path.join(base, B, "Reclamos_de_prueba.txt"), C.RECLAMOS_PRUEBA)
    txt(os.path.join(base, B, "Prompt_para_probar.txt"),
        "Usa la skill respuesta-a-reclamos para responder el RECLAMO 1 del archivo Reclamos_de_prueba.txt. Luego haz lo mismo con el 2 y el 3.")
    leeme(base, "KIT · SKILL RESPUESTA A RECLAMOS", C.SKILL_RECLAMOS["desc"],
          "respuesta-a-reclamos.zip: la Skill lista para subir (adentro va su SKILL.md).\nSkill_..._(para_leer).txt: el mismo contenido para leerlo.",
          "Reclamos_de_prueba.txt y Prompt_para_probar.txt.",
          ["En claude.ai: Configuración > Capacidades > Skills > Subir skill, y elige el .zip.",
           "Abre un chat nuevo y pega el prompt.", "Revisa cada respuesta contra las reglas de la Skill."])

    compras, abonos, esp = conc
    base = kit("sk2", pres, "Kit_Caso_2_Conciliacion_de_cashback")
    skill_zip(os.path.join(base, A), C.SKILL_CONCILIACION)
    a, b = xlsx_conciliacion(os.path.join(base, A), compras, abonos)
    txt(os.path.join(base, B, "Como_preparar_tu_OneDrive.txt"), C.COMO_SUBIR_ONEDRIVE)
    txt(os.path.join(base, B, "Prompt_para_probar.txt"),
        "Usa la skill conciliacion-de-cashback para conciliar el cashback de la primera quincena de octubre.")
    txt(os.path.join(base, B, "Resultados_esperados.txt"), "\n".join([
        "RESULTADOS ESPERADOS · CONCILIACIÓN DE CASHBACK", C.AVISO, "",
        "Compras elegibles: %d filas · Abonos: %d filas" % (esp["compras"], esp["abonos"]),
        "Total esperado: S/ {:,.2f} · Total abonado: S/ {:,.2f} · Diferencia: S/ {:,.2f}".format(
            esp["esperado"], esp["abonado"], esp["esperado"] - esp["abonado"]), "",
        "Compras sin abono (%d): %s" % (len(esp["sin_abono"]), ", ".join(esp["sin_abono"])),
        "Monto distinto (%d): %s · se abonó 0.5%% en vez de 1%%" % (len(esp["monto_distinto"]), ", ".join(esp["monto_distinto"])),
        "Abono duplicado (1): %s" % esp["duplicado"],
        "Abonos sin compra (2): %s" % ", ".join(esp["sin_compra"])]))
    leeme(base, "KIT · SKILL CONCILIACIÓN DE CASHBACK", C.SKILL_CONCILIACION["desc"],
          "conciliacion-de-cashback.zip: la Skill.\nLos dos Excel que van en tu OneDrive, en la carpeta «%s»." % C.CARPETA_ONEDRIVE,
          "Como_preparar_tu_OneDrive.txt, Prompt_para_probar.txt y Resultados_esperados.txt.",
          ["Crea la carpeta en tu OneDrive y sube los dos Excel.", "Sube la Skill y activa el conector de Microsoft 365.",
           "Pega el prompt y compara con los resultados esperados."])

    base = kit("sk3", pres, "Kit_Caso_3_Comunicado_de_mantenimiento")
    skill_zip(os.path.join(base, A), C.SKILL_COMUNICADO)
    txt(os.path.join(base, B, "Datos_de_prueba.txt"), C.DATOS_COMUNICADO)
    txt(os.path.join(base, B, "Prompt_para_probar.txt"),
        "Usa la skill comunicado-de-mantenimiento con estos datos: [pega la PRUEBA 1 de Datos_de_prueba.txt]")
    leeme(base, "KIT · SKILL COMUNICADO DE MANTENIMIENTO", C.SKILL_COMUNICADO["desc"],
          "comunicado-de-mantenimiento.zip: la Skill con el formato fijo.",
          "Datos_de_prueba.txt (la prueba 2 tiene un campo vacío) y Prompt_para_probar.txt.",
          ["Sube la Skill: Configuración > Capacidades > Skills > Subir skill.",
           "Pega el prompt con la PRUEBA 1 y revisa el Word que genera.",
           "Prueba la PRUEBA 2: debe preguntarte la hora de fin."])
    return esp


def kits_conectores():
    pres = "Presentacion_06_Conectores"
    for clave, nombre, pr in (("co1", "Kit_Caso_1_Resumir_un_hilo", C.PROMPT_HILO),
                              ("co2", "Kit_Caso_2_Preparar_mi_reunion", C.PROMPT_REUNION),
                              ("co3", "Kit_Caso_3_Buscar_en_OneDrive", C.PROMPT_ONEDRIVE)):
        base = kit(clave, pres, nombre)
        txt(os.path.join(base, A, "Como_activar_el_conector.txt"), C.ACTIVAR_CONECTOR)
        txt(os.path.join(base, B, "Prompt.txt"), pr)
        txt(os.path.join(base, B, "Que_revisar_antes_de_usarlo.txt"), C.QUE_REVISAR_CONECTOR)
        leeme(base, "KIT · CONECTOR MICROSOFT 365", "Usar Claude sobre tu correo, calendario y OneDrive sin descargar nada.",
              "Como_activar_el_conector.txt: los pasos y qué necesitas de TI.",
              "Prompt.txt: el pedido (cambia lo que está entre corchetes).\nQue_revisar_antes_de_usarlo.txt: 4 controles.",
              ["Activa el conector (o confirma con TI que esté habilitado).",
               "Abre un chat nuevo y pega el prompt.", "Revisa con la lista antes de usar el resultado."])


def kits_projects(tx_path_files):
    pres = "Presentacion_07_Projects"
    base = kit("pr1", pres, "Kit_Caso_1_Atencion_al_cliente")
    txt(os.path.join(base, A, "00_Instrucciones_del_Project.txt"), C.P1_INSTR)
    txt(os.path.join(base, A, "01_Productos_Sip.txt"), C.P1_PRODUCTOS)
    txt(os.path.join(base, A, "02_Preguntas_frecuentes.txt"), C.P1_FAQ)
    txt(os.path.join(base, A, "03_Guia_de_respuesta.txt"), C.P1_GUIA)
    txt(os.path.join(base, B, "Preguntas_de_prueba.txt"), C.P1_PRUEBAS)
    leeme(base, "KIT · PROJECT ATENCIÓN AL CLIENTE", "Un Project que responde como el equipo de Atención al Cliente.",
          "00_Instrucciones_del_Project.txt: va en Instrucciones.\n01 a 03: los documentos que subes al Project.",
          "Preguntas_de_prueba.txt: 5 preguntas, la última es trampa.",
          ["Projects > Nuevo proyecto: «Atención al cliente · Sip».", "Pega las instrucciones y sube los 3 documentos.",
           "Abre un chat dentro del Project y prueba las preguntas en orden."])

    base = kit("pr2", pres, "Kit_Caso_2_Reporte_de_transacciones")
    txt(os.path.join(base, A, "00_Instrucciones_del_Project.txt"), C.P2_INSTR)
    shutil.copy2(tx_path_files[0], os.path.join(base, A, "Transacciones_Septiembre_2026.xlsx"))
    txt(os.path.join(base, A, "Diccionario_de_datos.txt"), C.P2_DICCIONARIO)
    txt(os.path.join(base, B, "Preguntas_de_prueba.txt"), C.P2_PRUEBAS)
    txt(os.path.join(base, B, "Resultados_esperados.txt"), tx_path_files[1])
    leeme(base, "KIT · PROJECT REPORTE DE TRANSACCIONES", "Un Project que analiza las transacciones del mes.",
          "00_Instrucciones_del_Project.txt, el Excel y el diccionario de datos.",
          "Preguntas_de_prueba.txt y Resultados_esperados.txt para comparar.",
          ["Crea el Project «Canales digitales · Reporte».", "Pega las instrucciones y sube el Excel y el diccionario.",
           "Haz las preguntas y compara con los resultados esperados."])

    base = kit("pr3", pres, "Kit_Caso_3_Campanas_y_comunicacion")
    txt(os.path.join(base, A, "00_Instrucciones_del_Project.txt"), C.P3_INSTR)
    txt(os.path.join(base, A, "01_Guia_de_voz.txt"), C.P3_VOZ)
    txt(os.path.join(base, A, "02_Calendario_de_campanas.txt"), C.P3_CALENDARIO)
    txt(os.path.join(base, A, "03_Resultados_de_campanas.txt"), C.P3_RESULTADOS)
    txt(os.path.join(base, B, "Pedidos_de_prueba.txt"), C.P3_PRUEBAS)
    leeme(base, "KIT · PROJECT CAMPAÑAS Y COMUNICACIÓN", "Un Project para el equipo de marketing: ideas, copies y evaluación de campañas.",
          "00_Instrucciones_del_Project.txt y los documentos 01 a 03.", "Pedidos_de_prueba.txt: 4 pedidos, el último es trampa.",
          ["Crea el Project «Marketing · Sip».", "Pega las instrucciones y sube los 3 documentos.", "Prueba los pedidos en orden."])


def kits_research():
    pres = "Presentacion_08_Research"
    for clave, nombre, pr in (("re1", "Kit_Caso_1_Mercado_de_billeteras", C.PROMPT_R1),
                              ("re2", "Kit_Caso_2_Regulacion", C.PROMPT_R2),
                              ("re3", "Kit_Caso_3_Beneficios_de_la_competencia", C.PROMPT_R3)):
        base = kit(clave, pres, nombre)
        txt(os.path.join(base, A, "Prompt.txt"), pr)
        txt(os.path.join(base, B, "Checklist_de_verificacion.txt"), C.CHECKLIST_RESEARCH)
        leeme(base, "KIT · RESEARCH", "Una investigación con fuentes, lista para revisar.",
              "Prompt.txt: el pedido completo.", "Checklist_de_verificacion.txt: 6 controles antes de usarla.",
              ["En un chat nuevo, activa Research.", "Pega el prompt.", "Verifica con la lista: abre al menos 2 fuentes."])


def kits_design(tx, rc):
    pres = "Presentacion_09_Design"
    base = kit("de1", pres, "Kit_Caso_1_Resultados_del_mes")
    shutil.copy2(tx[0], os.path.join(base, A, "Transacciones_Septiembre_2026.xlsx")) if os.makedirs(os.path.join(base, A), exist_ok=True) is None else None
    txt(os.path.join(base, A, "Identidad_visual_Sip.txt"), C.IDENTIDAD)
    txt(os.path.join(base, B, "Prompt.txt"), C.PROMPT_D1)
    txt(os.path.join(base, B, "Resultados_esperados.txt"), tx[1])
    leeme(base, "KIT · DESIGN · RESULTADOS DEL MES", "Una presentación ejecutiva desde un Excel.",
          "El Excel de transacciones y la ficha de identidad visual.", "Prompt.txt y los resultados para revisar las cifras.",
          ["Abre Claude Design.", "Sube el Excel y la ficha.", "Pega el prompt y revisa 2 cifras contra los resultados esperados."])

    base = kit("de2", pres, "Kit_Caso_2_One_pager_de_campana")
    txt(os.path.join(base, A, "Brief_campana_noviembre.txt"), C.BRIEF_CAMPANA)
    txt(os.path.join(base, A, "Identidad_visual_Sip.txt"), C.IDENTIDAD)
    txt(os.path.join(base, B, "Prompt.txt"), C.PROMPT_D2)
    leeme(base, "KIT · DESIGN · ONE-PAGER DE CAMPAÑA", "Una página para presentar una campaña al equipo comercial.",
          "El brief y la ficha de identidad visual.", "Prompt.txt.",
          ["Abre Claude Design.", "Sube el brief y la ficha.", "Pega el prompt y revisa que todo salga del brief."])

    base = kit("de3", pres, "Kit_Caso_3_Reclamos_del_trimestre")
    os.makedirs(os.path.join(base, A), exist_ok=True)
    shutil.copy2(rc[0], os.path.join(base, A, "Reclamos_T3_2026.xlsx"))
    txt(os.path.join(base, A, "Identidad_visual_Sip.txt"), C.IDENTIDAD)
    txt(os.path.join(base, B, "Prompt.txt"), C.PROMPT_D3)
    txt(os.path.join(base, B, "Resultados_esperados.txt"), rc[1])
    leeme(base, "KIT · DESIGN · RECLAMOS DEL TRIMESTRE", "Una presentación de 5 slides desde el Excel de reclamos.",
          "El Excel de reclamos y la ficha de identidad visual.", "Prompt.txt y los resultados esperados.",
          ["Abre Claude Design.", "Sube el Excel y la ficha.", "Pega el prompt y compara las cifras."])


def kit_design_system():
    """Lo que usamos para armar el design system de Sip en Claude Design: prompt, respuesta, CSS en bruto, capturas y logo."""
    src = os.path.join(HERE, "fuentes_design_system")
    base = kit("ds", "Presentacion_09_Design", "Kit_Design_System_Sip")
    for d in ("capturas", "logo"):
        os.makedirs(os.path.join(base, d), exist_ok=True)
    shutil.copy2(os.path.join(src, "Prompt_y_formulario.txt"), os.path.join(base, "Prompt_y_formulario.txt"))
    shutil.copy2(os.path.join(src, "sip_styles.css"), os.path.join(base, "CSS_sip_en_bruto.txt"))
    for f in ("sip_captura_1_hero.jpg", "sip_captura_2_productos.jpg", "sip_captura_3_mundo_digital.jpg"):
        shutil.copy2(os.path.join(src, f), os.path.join(base, "capturas", f))
    for f in ("logo_sip.png", "logo_sip.svg"):
        shutil.copy2(os.path.join(src, f), os.path.join(base, "logo", f))
    txt(os.path.join(base, "LEEME.txt"), "\n".join([
        "KIT · DESIGN SYSTEM DE SIP", "==========================", "",
        "PARA QUÉ SIRVE", "Crear el design system de Sip en Claude Design para que cada diseño salga con su identidad.", "",
        "QUÉ TRAE",
        "Prompt_y_formulario.txt: el prompt que usamos y qué poner en cada campo del formulario.",
        "CSS_sip_en_bruto.txt: el CSS completo de sip.pe, tal como lo sirve la web.",
        "capturas: 3 capturas de sip.pe. logo: el logo de Sip en PNG y SVG.", "",
        "CÓMO USARLO",
        "1. En Claude Design, abre «Set up your design system».",
        "2. Copia el blurb y las notas de Prompt_y_formulario.txt en sus campos.",
        "3. En «Add fonts, logos and assets» sube el logo, las 3 capturas y la tipografía Poppins.",
    ]))


def kit_practica():
    base = kit("pra", "Presentacion_10_Practica_guiada", "Kit_Mi_Project")
    txt(os.path.join(base, A, "Plantilla_instrucciones.txt"), C.PLANTILLA_INSTR)
    txt(os.path.join(base, A, "Plantilla_contexto_de_mi_area.txt"), C.PLANTILLA_CONTEXTO)
    txt(os.path.join(base, B, "Como_probar_tu_Project.txt"), C.PRUEBAS_PRACTICA)
    leeme(base, "KIT · MI PROJECT", "Las plantillas para crear el Project de tu área.",
          "Plantilla de instrucciones y plantilla de contexto.", "Cómo probar tu Project en 4 pasos.",
          ["Completa las plantillas con lo de tu área.", "Crea tu Project y pega las instrucciones.", "Pruébalo con los 4 pasos."])


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
    tmp = os.path.join(HERE, "_tmp")
    tx, rc = transacciones(), reclamos()
    tx_x, rc_x = os.path.join(tmp, "tx.xlsx"), os.path.join(tmp, "rc.xlsx")
    xlsx_transacciones(tx_x, tx)
    xlsx_reclamos(rc_x, rc)
    etx, erc = esperados_tx(tx), esperados_rc(rc)
    ttx, trc = texto_esperados_tx(etx), texto_esperados_rc(erc)
    conc = conciliacion()
    esp_conc = kits_skills(conc)
    kits_conectores()
    kits_projects((tx_x, ttx))
    kits_research()
    kits_design((tx_x, ttx), (rc_x, trc))
    kit_design_system()
    kit_practica()
    rutas = zipear()
    shutil.rmtree(tmp)
    json.dump({"rutas": rutas, "tx": etx, "rc": erc, "conc": esp_conc}, open(os.path.join(HERE, "esperados.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("%d kits" % len(rutas))
    print(ttx.split("\n")[3])
    print("reclamos: %d · en proceso %d" % (erc["filas"], erc["en_proceso"]))


if __name__ == "__main__":
    main()
