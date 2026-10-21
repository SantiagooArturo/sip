# -*- coding: utf-8 -*-
"""
Contenido de la Sesion 2 de SIP: textos de los ejercicios, prompts y documentos de los kits.
Cada ejercicio tiene su kit: 1_Para_construir (todo lo que se usa para hacerlo, incluido el prompt
en .txt) y 2_Para_probar (casos de prueba y resultados esperados).
Datos de negocio FICTICIOS: no son condiciones, clientes ni cifras reales de Sip.
"""
import contenido as C1   # contenido de la Sesion 1 (research, identidad, skill de actas)

AVISO = C1.AVISO
URL_BASE = "https://sip.myworkin.ai"
URL_FORMULARIO = URL_BASE + "/sesion-2/formulario/afiliacion_de_comercios.html"

# ------------------------------------------------------------- outlook ---
ACTIVAR_CONECTOR = """CÓMO CONECTAR TU CUENTA DE MICROSOFT 365 EN CLAUDE (NAVEGADOR)

1. En claude.ai, entra a Configuración > Conectores.
2. Busca «Microsoft 365» y elige Conectar.
3. Inicia sesión con tu cuenta corporativa de SIP y acepta los permisos.
4. Abre un chat nuevo. En el menú de herramientas (debajo de la caja de texto) verifica que
   Microsoft 365 esté activo.

SI NO TE APARECE
- El conector lo habilita TI de SIP para toda la organización. Si no lo ves en la lista,
  avisa al facilitador: sigue el ejercicio en pantalla y lo repites cuando TI lo active.

QUÉ PUEDE Y QUÉ NO
- Lee tu correo, tu calendario y tus archivos de OneDrive y SharePoint: solo lo que tu cuenta ya ve.
- No envía correos, no crea reuniones y no borra nada. Los borradores te los muestra en el chat."""

QUE_REVISAR_CONECTOR = """ANTES DE USAR LO QUE TE DEVUELVE CLAUDE
1. ¿Usó los correos o reuniones correctos? Pídele el asunto, la fecha y el remitente de cada uno.
2. Abre 1 correo de los que citó y contrasta un dato: ¿dice lo que Claude dice?
3. ¿El borrador sale con tu nombre? Léelo completo antes de copiarlo a Outlook.
4. ¿Hay datos de clientes en la respuesta? No los pegues en otros chats ni los reenvíes fuera de SIP."""

PROMPT_BANDEJA = """Revisa los correos que recibí en mi bandeja de entrada desde el viernes a las 18:00 hasta hoy.

1. Clasifícalos en una tabla con 4 categorías: Urgente hoy · Esta semana · Solo informativo · Puede esperar.
   Columnas: categoría, remitente, asunto, por qué está ahí (una línea) y qué acción tomo.
2. Es urgente si me piden algo para hoy o mañana, si viene de mi jefe directo o de un cliente, o si avisa de un problema en la app.
3. Al final, dime las 3 cosas que debo hacer primero, en orden.

No abras adjuntos ni respondas nada. Si un correo no se entiende sin el adjunto, márcalo como «revisar adjunto»."""

PROMPT_LOTE = """Busca en mi bandeja los correos de los últimos 3 días que me hacen una pregunta o me piden algo y que todavía no he respondido.

1. Lístalos en una tabla: remitente, asunto, qué me piden y para cuándo.
2. Elige los 3 más importantes y redacta un borrador de respuesta para cada uno:
   - Máximo 100 palabras, tono cordial y directo, con mi nombre al final.
   - Si para responder necesitas un dato que no está en el correo, déjalo entre [corchetes]. No lo inventes.
3. Muéstrame los 3 borradores en el chat, cada uno con el asunto original arriba.

No envíes nada."""

PROMPT_SEMANA = """Revisa mi calendario de esta semana, de lunes a viernes.

1. Una tabla por día: hora, reunión, con quién y cuánto dura.
2. Cuántas horas tengo en reuniones y cuántas libres entre las 9:00 y las 18:00.
3. Reuniones que se cruzan o que están pegadas sin pausa.
4. Para las 3 reuniones más importantes: el correo más reciente que tengo con esos asistentes y 3 puntos que debería llevar.
5. Dos bloques de 90 minutos libres que podría reservar para trabajo concentrado.

No crees ni cambies eventos. Si un día no tiene reuniones, dilo."""

ESPERADO_BANDEJA = """QUÉ DEBERÍAS VER (cambia según tu bandeja)
- Una tabla con TODOS los correos desde el viernes 18:00, cada uno en una sola categoría.
- En «Urgente hoy», solo correos que cumplen la regla: fecha de hoy o mañana, tu jefe, un cliente o un problema en la app.
- 3 acciones concretas al final, en orden.
- Ningún correo respondido ni adjunto abierto.

PRUEBA EXTRA
Pídele: «¿Por qué pusiste [asunto] en Urgente hoy?». Debe explicarlo con la regla, no con una suposición."""

ESPERADO_LOTE = """QUÉ DEBERÍAS VER (cambia según tu bandeja)
- Una tabla con los correos sin responder de los últimos 3 días.
- 3 borradores de máximo 100 palabras, con tu nombre al final.
- Datos que faltan entre [corchetes], no inventados.

PRUEBA EXTRA
Pídele: «Haz el segundo borrador más corto y más formal». Debe cambiar solo ese borrador."""

ESPERADO_SEMANA = """QUÉ DEBERÍAS VER (cambia según tu calendario)
- Una tabla por día con hora, reunión, asistentes y duración.
- La suma de horas en reuniones y horas libres entre 9:00 y 18:00.
- Los cruces o reuniones pegadas, si los hay.
- 2 bloques de 90 minutos libres que de verdad estén libres en tu calendario.

CÓMO VERIFICARLO
Abre tu calendario de Outlook y contrasta un día completo con la tabla."""

# ------------------------------------------------------- segunda skill ---
PROMPT_SEGUNDA_SKILL = """Quiero crear una Skill para una tarea que repito siempre igual. Abajo te paso la ficha de mi tarea.

Antes de crearla, hazme en una sola tanda las preguntas que necesites (máximo 5).

Después, crea la Skill con:
- Un nombre en minúsculas y con guiones.
- Una descripción que diga cuándo usarla.
- Los pasos que sigue, en orden.
- El formato de salida, siempre igual.
- Las reglas: lo que nunca debe hacer y qué hacer si falta un dato (preguntar, no inventar).

Al final, dame la Skill lista para guardar y 2 pedidos para probarla: uno completo y uno al que le falte un dato.

FICHA DE MI TAREA
[pega aquí tu ficha completa]"""

FICHA_TAREA = """FICHA DE MI TAREA (complétala antes de abrir Claude)

1. Nombre de la tarea:
2. Cada cuánto la hago (diario, semanal, mensual):
3. Qué recibo para hacerla (un correo, un Excel, notas, un formulario):
4. Qué entrego al final (un correo, un reporte, una tabla, un documento):
5. El formato que siempre tiene (secciones, columnas, largo):
6. Reglas que no se pueden olvidar (qué nunca se promete, qué siempre se revisa):
7. Qué hago hoy cuando me falta un dato:
8. Un ejemplo de una vez que salió bien (pégalo sin datos de clientes):"""

FICHA_EJEMPLO = """FICHA DE EJEMPLO (para ver cómo se llena)

1. Nombre de la tarea: resumen semanal de reclamos para la jefatura de Atención al Cliente.
2. Cada cuánto: todos los lunes.
3. Qué recibo: el Excel de reclamos de la semana (ID, fecha, motivo, canal, estado, días de respuesta).
4. Qué entrego: un correo a la jefatura.
5. Formato: asunto «Reclamos semana [n]», 3 cifras arriba (total, resueltos, fuera de plazo),
   top 3 motivos con su número, reclamos fuera de plazo con su ID y 2 acciones sugeridas.
6. Reglas: nunca nombrar clientes; el plazo es de 15 días; si un dato no está en el Excel, «no disponible».
7. Si falta un dato: lo marco y pregunto al analista que armó el Excel.
8. Ejemplo: «Reclamos semana 41 · 46 reclamos · 39 resueltos · 3 fuera de plazo. Top: cashback no
   abonado (14), cobro no reconocido (9), transferencia no llegó (7)…»"""

COMO_PROBAR_SKILL = """CÓMO PROBAR TU SEGUNDA SKILL

1. Guárdala: con el botón que te da Claude o en Configuración > Capacidades > Skills > Subir skill.
2. Abre un chat NUEVO (la Skill tiene que activarse sola, sin la conversación donde la creaste).
3. Pega el pedido completo que te dio Claude. Revisa:
   - ¿Sale siempre con el mismo formato?
   - ¿Cumple las reglas de tu ficha?
4. Pega el pedido al que le falta un dato. Lo correcto: que te PREGUNTE el dato, no que lo invente.
5. Si algo no te gusta, díselo en el chat: «actualiza la skill para que…».

SEÑAL DE QUE ESTÁ BIEN HECHA
Otra persona de tu equipo la usa con el mismo pedido y le sale lo mismo que a ti."""

# ---------------------------------------------------------- micro-apps ---
DISENO_SIP = ("Diseño: colores de Sip (celeste #00B1FF, negro #1B1B1D, blanco y celeste claro #DEF2FF), "
              "tipografía sans serif, cifras grandes, montos en S/ con 2 decimales y separador de miles.")

PROMPT_SIMULADOR = """Crea un artefacto interactivo: «Simulador de campaña de cashback · Sip».

Controles (slider con el valor visible y una caja para escribir el número):
- Clientes que activan la campaña: de 1,000 a 50,000 (inicia en 20,000)
- Compras por cliente en el mes: de 1 a 10 (inicia en 3)
- Ticket promedio por compra (S/): de 20 a 500 (inicia en 85)
- % de cashback: de 0.5% a 5%, en pasos de 0.5 (inicia en 2%)
- Tope de cashback por cliente (S/): de 5 a 100 (inicia en 40)
- Presupuesto de la campaña (S/): de 10,000 a 1,500,000 (inicia en 150,000)

Cálculos:
- Cashback por cliente = el menor entre (compras × ticket × %) y el tope.
- Costo total = clientes × cashback por cliente.
- Costo por compra = costo total ÷ (clientes × compras).
- Clientes que alcanza el presupuesto = presupuesto ÷ cashback por cliente, redondeado hacia abajo.
- Llega al tope = Sí, si compras × ticket × % es mayor o igual al tope.

Muestra 4 tarjetas (costo total, costo por compra, clientes que alcanza el presupuesto y si llega al tope), un aviso en rojo si el costo total supera el presupuesto y un gráfico de barras con el costo total para cada % de 0.5% a 5%.
""" + DISENO_SIP

PROMPT_DASHBOARD = """Crea un artefacto: «Dashboard de reclamos · Sip».

Entrada: un botón para cargar un archivo CSV con estas columnas:
ID, Fecha, Semana, Motivo, Canal, Producto, Estado, Dias_respuesta, Dias_abierto
(Estado es «Resuelto» o «En proceso». Dias_respuesta solo viene en los resueltos y Dias_abierto solo en los que están en proceso.)

Regla del plazo: un reclamo está FUERA DE PLAZO si Dias_respuesta es mayor a 15 o si Dias_abierto es mayor a 15.

Muestra:
1. 4 tarjetas: total de reclamos, resueltos, en proceso y % fuera de plazo (con un decimal).
2. Barras de reclamos por motivo, de mayor a menor.
3. Línea de reclamos por semana.
4. Tabla de los reclamos EN PROCESO y FUERA DE PLAZO: ID, fecha, motivo, canal y días abierto.
5. Un filtro por canal que actualice todo.

Si el archivo no tiene alguna columna, muestra un aviso con el nombre de la columna que falta.
""" + DISENO_SIP

PROMPT_CONCILIADOR = """Crea un artefacto: «Conciliador de cashback · Sip».

Entrada: dos botones para cargar dos Excel:
- Compras elegibles: columnas «ID compra», «Fecha», «Comercio», «Grupo», «Monto (S/)», «% cashback», «Cashback esperado (S/)».
- Cashback abonado: columnas «ID compra», «Fecha de abono», «Cashback abonado (S/)».

Cruza los dos archivos por «ID compra» y clasifica cada diferencia:
- Compra sin abono: está en compras y no en abonos.
- Monto distinto: el abonado no es igual al esperado.
- Abono duplicado: el mismo ID aparece más de una vez en abonos.
- Abono sin compra: está en abonos y no en compras.

Muestra:
1. 3 tarjetas: total esperado, total abonado y diferencia.
2. Cuántas diferencias hay de cada tipo.
3. Una tabla por tipo con ID, fecha, comercio, esperado, abonado y diferencia, resaltando en rojo lo que falta abonar.
4. Un botón «Descargar diferencias» que baje un CSV con todas las filas con diferencia.

Lee los Excel en el navegador: no los modifica ni los envía a ningún lado.
""" + DISENO_SIP

TARIFA = [("Supermercados", 1.40), ("Farmacias", 1.60), ("Mejoramiento del hogar", 1.80),
          ("Retail y tiendas por departamento", 1.90), ("Restaurantes y cafeterías", 2.20),
          ("Entretenimiento", 2.50)]
TRAMOS = [(200000, 0.40), (50000, 0.20)]    # ventas >= monto -> descuento en puntos porcentuales
MINIMO_TX = 0.15
IGV = 0.18


def tarifario_txt():
    l = ["TARIFARIO DE COMISIONES PARA COMERCIOS AFILIADOS A SIP (EJEMPLO PARA PRACTICAR)", AVISO, "",
         "Comisión base por rubro (sobre el monto vendido con Sip):"]
    l += ["  %-36s %.2f%%" % (r, t) for r, t in TARIFA]
    l += ["", "Descuento por volumen de ventas mensuales con Sip (no se suman):",
          "  Desde S/ 200,000: se restan 0.40 puntos a la comisión base",
          "  Desde S/ 50,000:  se restan 0.20 puntos a la comisión base",
          "  Menos de S/ 50,000: sin descuento", "",
          "Comisión mínima: S/ %.2f por transacción. Si la comisión calculada es menor que" % MINIMO_TX,
          "transacciones × S/ %.2f, se cobra ese mínimo." % MINIMO_TX, "",
          "IGV: 18%% sobre la comisión.",
          "Abono neto al comercio = ventas − comisión − IGV de la comisión.",
          "El abono se hace al día hábil siguiente en la cuenta que registró el comercio."]
    return "\n".join(l)


PROMPT_COMISIONES = """Crea un artefacto: «Calculadora de comisiones para comercios · Sip».

Entradas:
- Rubro del comercio (lista desplegable).
- Ventas del mes con Sip (S/).
- Número de transacciones del mes.

Tarifario (comisión base sobre lo vendido):
- Supermercados 1.40% · Farmacias 1.60% · Mejoramiento del hogar 1.80%
- Retail y tiendas por departamento 1.90% · Restaurantes y cafeterías 2.20% · Entretenimiento 2.50%

Reglas, en este orden:
1. Descuento por volumen (no se suman): desde S/ 200,000 se restan 0.40 puntos; desde S/ 50,000, 0.20 puntos.
2. Comisión = ventas × tasa con descuento.
3. Comisión mínima: si la comisión es menor que transacciones × S/ 0.15, se cobra ese mínimo.
4. IGV = 18% de la comisión.
5. Abono neto = ventas − comisión − IGV.

Muestra: la tasa aplicada, si aplicó descuento o mínimo, la comisión, el IGV, el total descontado y el abono neto en grande. Debajo, una tabla que compare el resultado con las mismas ventas en los 6 rubros.
""" + DISENO_SIP

CATEGORIAS = ["Cashback no abonado", "Cobro no reconocido", "Transferencia no llegó", "Pase a cuotas",
              "Bloqueo de cuenta", "Atención en módulo", "Otros"]

PROMPT_CLASIFICADOR = """Crea un artefacto que use a Claude por dentro: «Clasificador de reclamos · Sip».

Pantalla: una caja de texto para pegar un reclamo y un botón «Clasificar».

Al hacer clic, el artefacto le pide a Claude que devuelva, en JSON:
- categoria: una de estas 7: Cashback no abonado, Cobro no reconocido, Transferencia no llegó, Pase a cuotas, Bloqueo de cuenta, Atención en módulo, Otros.
- urgencia: Alta, Media o Baja.
    Alta: posible fraude o cobro no reconocido, montos mayores a S/ 1,000 o el cliente reclama por tercera vez.
    Media: el cliente espera dinero (cashback o transferencia).
    Baja: todo lo demás.
- escalar: Sí si la urgencia es Alta; No en los demás casos.
- resumen: una línea.
- respuesta: borrador para el cliente, máximo 100 palabras, tuteando, sin prometer devoluciones y sin pedir claves ni CVV.

Muestra el resultado en una tarjeta con la categoría y la urgencia en color (Alta rojo, Media ámbar, Baja verde) y un botón para copiar la respuesta.
Debajo, un historial de los reclamos clasificados en esta sesión: resumen, categoría, urgencia y escalar.
""" + DISENO_SIP

COMO_PUBLICAR = """CÓMO SE USA Y SE COMPARTE UN ARTEFACTO

1. Abre un chat nuevo en claude.ai y pega el prompt completo (Prompt.txt).
2. El artefacto aparece al lado del chat. Pruébalo con los casos de 2_Para_probar.
3. Si algo no está bien, pídelo en el chat: «el gráfico, de barras horizontales», «el aviso más grande».
4. Para compartirlo: botón Publicar del artefacto > copia el enlace.
   Quien lo abre ve la herramienta; no ve tu conversación.

ANTES DE COMPARTIRLO
- Pruébalo con los casos de prueba y compara con los resultados esperados.
- No dejes datos de clientes escritos dentro del artefacto."""

# --------------------------------------------- skills, projects y design ---
SKILL_ACTAS = C1.SKILL_ACTAS
NOTAS_REUNION_1 = C1.NOTAS_REUNION
NOTAS_REUNION_2 = """reunion operaciones + atencion - jue 15 oct
estuvieron martín (operaciones), rocío (atención), kevin (atención), lu (calidad)
- tiempos de respuesta en módulo subieron a 6 días promedio en sept, la meta es 5
- kevin propone plantilla de respuesta para cobros no reconocidos, la revisan con legal
- lu va a auditar 30 reclamos cerrados en sept para ver calidad de respuesta, para fin de mes
- se acordó reforzar el turno de la tarde en módulos de plazaVea San Miguel pero nadie quedó a cargo
- martín pregunta si se puede automatizar el aviso de transferencia no llegada, queda en evaluar
- prox reunion: no se definió"""

ESPERADO_ACTAS = """RESULTADO ESPERADO · ACTA DE REUNIÓN

NOTAS 1 (comité del lunes 12 de octubre)
Acuerdos que deben aparecer:
1. Paola (TI) revisa si el abono de cashback puede correr a diario · fecha: viernes 16 de octubre.
2. Diego pide el ok de legal para los TyC de «Noviembre te devuelve» · fecha: lunes 12 de octubre.
3. Rocío arma el texto que explica los plazos del cashback en la app · fecha: 19 de octubre.
Pendiente: definir si el tope de S/ 40 va en el push o solo en los TyC.
Próxima reunión: lunes 19.

NOTAS 2 (operaciones + atención del jueves 15)
Lo que debe hacer la Skill:
- «Reforzar el turno de la tarde en el módulo de plazaVea San Miguel» → Responsable: por definir.
- «Plantilla para cobros no reconocidos» → Responsable: Kevin · Fecha: por definir.
- «Auditar 30 reclamos cerrados» → Responsable: Lu · Fecha: fin de mes.
- Próxima reunión: por definir.
Lo que NO debe hacer: inventar un responsable o una fecha."""

SKILL_REPORTE = {
    "slug": "reporte-semanal-de-correos",
    "desc": ("Arma el reporte semanal de un colaborador de Sip a partir de sus correos de los últimos 7 días "
             "(con el conector de Microsoft 365) o de correos pegados en el chat. Úsala cuando piden el "
             "reporte semanal, el resumen de la semana o el avance para la jefatura."),
    "cuerpo": """# Reporte semanal desde mis correos · Sip

Armas el reporte semanal con lo que pasó en los correos de la persona.

## De dónde salen los datos
1. Si el conector de Microsoft 365 está activo, lee los correos recibidos y enviados de los últimos 7 días.
   Salta boletines, notificaciones automáticas e invitaciones sin texto.
2. Si no hay conector o la persona pega correos en el chat, usa solo esos correos.
3. Confirma al inicio, en una línea, cuántos correos usaste y el rango de fechas.

## Formato (siempre igual)
REPORTE SEMANAL · [nombre de la persona] · semana del [fecha] al [fecha]

1. LO QUE SE CERRÓ: máximo 5 viñetas, cada una con el correo que lo respalda (asunto y fecha).
2. EN CURSO: tarea · responsable · próxima fecha.
3. BLOQUEOS: qué está frenado, por qué y de quién depende.
4. CORREOS SIN RESPONDER: remitente · asunto · días esperando.
5. LA PRÓXIMA SEMANA: 3 prioridades.

## Reglas
- Todo lo que pongas tiene que estar en un correo. Si no hay datos para una sección, escribe «Sin novedades».
- No copies datos de clientes (nombres, DNI, celulares): resume el tema.
- Máximo una página.
""",
}

CORREOS_EJEMPLO = """CORREOS DE EJEMPLO · SEMANA DEL 12 AL 16 DE OCTUBRE DE 2026
(Úsalos si no tienes el conector activo: pégalos en el chat después del prompt.)
""" + AVISO + """

1) Lun 12/10 09:14 · De: Martín Rojas (Operaciones) · Para: Ana Torres · Asunto: Proceso de abono de cashback
Ana, confirmamos que el proceso de abono pasó a correr martes y viernes. Desde la próxima semana debería bajar el reclamo por cashback no abonado.

2) Lun 12/10 11:40 · De: Ana Torres · Para: Legal · Asunto: TyC campaña «Noviembre te devuelve»
Hola equipo, les envío los términos y condiciones para su revisión. Necesitamos el ok antes del viernes 16 para lanzar el 1 de noviembre.

3) Mar 13/10 10:02 · De: Paola Díaz (TI) · Para: Ana Torres · Asunto: RE: Abono diario de cashback
Ana, revisamos y el abono diario se puede, pero recién en diciembre por la congelación de cambios de noviembre.

4) Mar 13/10 16:25 · De: Ana Torres · Para: Diego Salas (Marketing) · Asunto: Push de noviembre
Diego, te paso las 2 opciones de push aprobadas por producto. Quedamos en lanzarlas el 1/11 a las 10:00.

5) Mié 14/10 08:50 · De: Rocío Vega (Atención) · Para: Ana Torres · Asunto: Texto de plazos del cashback
Ana, te comparto el texto para la sección de ayuda de la app. ¿Me confirmas si va el plazo de 5 días hábiles para comercios del grupo?

6) Mié 14/10 12:10 · De: Notificaciones Sip · Para: Ana Torres · Asunto: Resumen automático del sistema
(Correo automático: no se usa en el reporte.)

7) Jue 15/10 09:30 · De: Ana Torres · Para: Comité de canales · Asunto: Resultados de septiembre
Comparto los resultados de septiembre: 800 transacciones de la muestra y crecimiento del pago con QR. Detalle en la presentación adjunta.

8) Jue 15/10 15:45 · De: Legal · Para: Ana Torres · Asunto: RE: TyC campaña «Noviembre te devuelve»
Ana, falta definir si el tope de S/ 40 se menciona en el push. Sin eso no podemos dar el ok.

9) Vie 16/10 10:05 · De: Lucía Paredes (Producto) · Para: Ana Torres · Asunto: Pantalla «Mis cashbacks»
Ana, ¿puedes mandarme el lunes los textos de la nueva pantalla «Mis cashbacks» para el prototipo?

10) Vie 16/10 17:20 · De: Ana Torres · Para: Martín Rojas · Asunto: RE: Proceso de abono de cashback
Gracias Martín. El lunes medimos si bajaron los reclamos con el cambio a martes y viernes."""

PROMPT_REPORTE_CONECTOR = "Usa la skill reporte-semanal-de-correos para armar mi reporte de esta semana."
PROMPT_REPORTE_PEGADO = ("Usa la skill reporte-semanal-de-correos para armar el reporte semanal de Ana Torres "
                         "con estos correos:\n\n[pega aquí los correos de Correos_de_ejemplo.txt]")

ESPERADO_REPORTE = """RESULTADO ESPERADO · REPORTE CON LOS CORREOS DE EJEMPLO
Debe decir al inicio que usó 9 correos (el 6 es automático y se salta) del 12 al 16 de octubre.

LO QUE SE CERRÓ
- El abono de cashback pasó a martes y viernes (correo 1).
- Push de noviembre aprobado: se lanza el 1/11 a las 10:00 (correo 4).
- Resultados de septiembre enviados al comité (correo 7).

EN CURSO
- TyC de «Noviembre te devuelve» · Legal · ok antes del viernes 16 (correos 2 y 8).
- Medir si bajaron los reclamos de cashback · Ana · lunes (correo 10).

BLOQUEOS
- Legal no da el ok de los TyC hasta definir si el tope de S/ 40 va en el push (correo 8).
- El abono diario recién en diciembre por la congelación de cambios de noviembre (correo 3).

CORREOS SIN RESPONDER
- Rocío Vega · Texto de plazos del cashback (correo 5).
- Lucía Paredes · Pantalla «Mis cashbacks» (correo 9).

Lo que NO debe pasar: usar el correo 6 o inventar fechas que no están en los correos."""

# Project: comercios afiliados
PC_INSTR = """Eres el asistente del equipo de Comercios Afiliados de Sip.

Ayudas a responder a comercios que quieren afiliarse o que ya están afiliados.
- Responde solo con la información de los documentos del Project. Si algo no está, di: «No tengo ese dato en los documentos» y sugiere a quién preguntar.
- Cuando des una condición, una comisión o un plazo, di de qué documento lo sacaste.
- Si te piden calcular una comisión, muestra la cuenta paso a paso con el tarifario.
- Respuestas a comercios: trato de usted, claras y de máximo 150 palabras.
- No prometas aprobaciones ni plazos distintos a los del documento de onboarding."""

PC_CONDICIONES = """CONDICIONES DE AFILIACIÓN A SIP (EJEMPLO PARA PRACTICAR)
""" + AVISO + """

QUIÉN PUEDE AFILIARSE
- Personas jurídicas con RUC activo y habido.
- Personas naturales con negocio y RUC 10 activo.
- Rubros aceptados: los 6 del tarifario. Otros rubros se evalúan caso por caso con el área comercial.

QUÉ RECIBE EL COMERCIO
- Cobro con QR Sip en caja y link de pago para ventas por redes.
- Abono al día hábil siguiente en su cuenta bancaria registrada.
- Acceso al portal de comercios con el detalle de sus ventas y comisiones.
- Participación en campañas de cashback de Sip, si el área comercial lo invita.

DOCUMENTOS QUE PIDE
- Ficha RUC.
- DNI del representante legal.
- Vigencia de poder del representante (solo personas jurídicas), con antigüedad máxima de 30 días.
- Constancia de la cuenta bancaria a nombre del comercio.

CUÁNDO SE RECHAZA
- RUC no habido o con baja de oficio.
- La cuenta bancaria no está a nombre del comercio.
- Rubros no permitidos: casas de cambio no autorizadas, apuestas no reguladas y venta de armas."""

PC_ONBOARDING = """PROCESO DE ONBOARDING DE COMERCIOS (EJEMPLO PARA PRACTICAR)
""" + AVISO + """

PASO 1 · Solicitud (día 0)
El comercio llena el formulario de afiliación en la web y adjunta los documentos.

PASO 2 · Validación (hasta 3 días hábiles)
Comercios Afiliados revisa el RUC, los documentos y la cuenta bancaria.
Si falta un documento, se le avisa por correo y el plazo se detiene hasta que lo envíe.

PASO 3 · Firma del contrato (hasta 2 días hábiles)
El representante firma el contrato digital desde el enlace que recibe por correo.

PASO 4 · Activación (1 día hábil)
Se crea el usuario del portal de comercios y se envía el QR para imprimir.

PLAZO TOTAL: hasta 6 días hábiles desde que el comercio envía todos los documentos.

CONTACTO
comercios@sip.example · el equipo responde en máximo 1 día hábil."""

PC_FAQ = """PREGUNTAS FRECUENTES DE COMERCIOS (EJEMPLO PARA PRACTICAR)
""" + AVISO + """

¿Cuánto cuesta afiliarse?
La afiliación no tiene costo. Solo se cobra la comisión por cada venta, según el tarifario.

¿Cuándo recibo el dinero de mis ventas?
Al día hábil siguiente de la venta, en la cuenta bancaria registrada.

¿Puedo cambiar la cuenta de abono?
Sí, desde el portal de comercios. El cambio se aplica en 2 días hábiles.

¿Puedo cobrar sin QR impreso?
Sí, con el link de pago desde el portal.

¿Qué pasa si un cliente pide la devolución de una compra?
El comercio hace la devolución desde el portal y la comisión de esa venta se devuelve al comercio.

¿Cómo participo en una campaña de cashback?
El área comercial invita a los comercios según su rubro y sus ventas. No se puede pedir por el portal."""

PC_PRUEBAS = """PREGUNTAS PARA PROBAR EL PROJECT (y qué debería responder)

1. Una farmacia vende S/ 80,000 al mes con Sip en 2,000 transacciones. ¿Cuánto paga de comisión y cuánto recibe?
   Esperado: tasa 1.40% (1.60% − 0.20). Comisión S/ 1,120.00 · IGV S/ 201.60 · abono neto S/ 78,678.40.

2. Un restaurante quiere afiliarse. ¿Qué documentos necesita y cuánto demora?
   Esperado: ficha RUC, DNI del representante, vigencia de poder (si es persona jurídica, máx. 30 días)
   y constancia de cuenta bancaria. Hasta 6 días hábiles desde que envía todo. Fuente: condiciones y onboarding.

3. Redacta la respuesta a un comercio que pregunta cuándo le llega el dinero de sus ventas.
   Esperado: al día hábil siguiente, trato de usted, máximo 150 palabras.

4. Un comercio envió su solicitud hace 4 días, pero le faltaba la vigencia de poder. ¿Ya debería estar activo?
   Esperado: no necesariamente; el plazo se detiene mientras falta un documento.

5. PRUEBA TRAMPA: ¿Cuál es la comisión para estaciones de servicio (grifos)?
   Esperado: que diga que ese rubro no está en el tarifario y que se evalúa con el área comercial."""

# Project: riesgo y cumplimiento
PR_INSTR = """Eres el asistente del equipo de Riesgo y Cumplimiento de Sip.

Respondes preguntas de cualquier colaborador sobre las políticas internas.
- Usa solo los documentos del Project. Cita siempre el documento y la sección (por ejemplo: «Política de prevención de fraude, sección 3»).
- Si la política no cubre el caso, dilo y recomienda consultar a Cumplimiento. No completes con lo que harías tú.
- Primero la respuesta corta (sí, no o qué hacer); después el detalle.
- Nunca autorices una excepción: solo explicas lo que dice la política."""

PR_FRAUDE = """POLÍTICA DE PREVENCIÓN DE FRAUDE (EJEMPLO PARA PRACTICAR)
""" + AVISO + """

1. ALCANCE
Aplica a todos los colaboradores que atienden clientes o revisan operaciones.

2. SEÑALES DE ALERTA
- Más de 5 transferencias a cuentas distintas en menos de 1 hora.
- Una compra mayor a S/ 3,000 en un comercio en el que el cliente nunca compró.
- Cambio de celular o de correo y una transferencia en las 24 horas siguientes.
- El cliente dice que un «asesor de Sip» le pidió una clave o un código.

3. QUÉ HACER ANTE UNA SEÑAL DE ALERTA
- Bloquear la tarjeta o la billetera de forma preventiva desde el sistema de atención.
- Registrar el caso en la bandeja de Riesgo en máximo 2 horas.
- No decirle al cliente que su caso es «fraude confirmado»: decir que está en revisión.

4. CLIENTE QUE RECONOCE HABER DADO SU CLAVE
- Se bloquea la cuenta y se registra el caso. La devolución la decide Riesgo, nunca el colaborador.

5. LO QUE NUNCA SE HACE
- Pedir claves, CVV o códigos de verificación.
- Desbloquear una cuenta bloqueada por Riesgo sin su autorización escrita."""

PR_DATOS = """POLÍTICA DE DATOS PERSONALES (EJEMPLO PARA PRACTICAR)
""" + AVISO + """

1. QUÉ ES UN DATO PERSONAL
Nombre, DNI, celular, correo, dirección y cualquier movimiento que permita identificar al cliente.

2. DÓNDE SE PUEDEN USAR
- Solo en los sistemas de SIP y en la cuenta corporativa de Claude.
- En Claude, solo si la tarea lo necesita. Si no necesitas saber quién es el cliente, anonimiza (C-001, C-002).

3. LO QUE NUNCA SE HACE
- Subir datos de clientes a herramientas personales (cuentas de IA personales, correo personal, USB).
- Compartir datos de un cliente con otro cliente o con un tercero sin autorización.
- Pegar números completos de tarjeta, CVV o claves en cualquier herramienta.

4. PEDIDOS DEL CLIENTE
- Un cliente puede pedir ver, corregir o eliminar sus datos. Se registra en la app o en un Módulo de Atención
  y se responde en máximo 20 días hábiles.

5. SI HUBO UN ERROR
Si enviaste datos de un cliente a quien no correspondía, avisa a Cumplimiento el mismo día."""

PR_RECLAMOS = """PROCEDIMIENTO DE ATENCIÓN DE RECLAMOS (EJEMPLO PARA PRACTICAR)
""" + AVISO + """

1. CANALES DE INGRESO
App Sip, sip.pe, Módulos de Atención Sip y central telefónica.

2. PLAZOS
- Constancia del reclamo: al momento de registrarlo, con su número.
- Respuesta al cliente: máximo 15 días hábiles. Se puede ampliar una vez por 15 días más si el caso lo
  justifica, avisando al cliente antes de que venza el primer plazo.

3. QUIÉN RESPONDE
- Atención al Cliente responde todos los reclamos.
- Reclamos mayores a S/ 1,000 o con señal de fraude: los revisa Riesgo antes de responder.

4. LO QUE SE GUARDA
Cada reclamo y su respuesta se guardan 5 años."""

PR_PRUEBAS = """PREGUNTAS PARA PROBAR EL PROJECT (y qué debería responder)

1. Un cliente hizo 7 transferencias a cuentas distintas en 40 minutos. ¿Qué hago?
   Esperado: es señal de alerta (sección 2). Bloqueo preventivo y registro en la bandeja de Riesgo en máx. 2 horas (sección 3).

2. ¿Puedo pegar en Claude el Excel de reclamos con nombres y DNI para hacer un análisis por motivo?
   Esperado: el análisis por motivo no necesita saber quién es el cliente: anonimizar primero (Política de datos, sección 2).

3. Un reclamo vence mañana y todavía falta información. ¿Qué puedo hacer?
   Esperado: ampliar una vez por 15 días hábiles, avisando al cliente antes de que venza (Procedimiento, sección 2).

4. Un cliente reconoce que le dio su código a un «asesor». Pide que le devuelvan el dinero hoy. ¿Qué le digo?
   Esperado: bloqueo y registro; la devolución la decide Riesgo; no prometer nada (Fraude, sección 4).

5. PRUEBA TRAMPA: ¿Cuál es el monto máximo que puede transferir un cliente por día?
   Esperado: que diga que ninguna política lo dice y que se consulte a Cumplimiento."""

# Design
IDENTIDAD = C1.IDENTIDAD

BRIEF_BANNER = """BRIEF · CAMPAÑA «NAVIDAD TE DEVUELVE» (EJEMPLO PARA PRACTICAR)
""" + AVISO + """

Producto: tarjeta de crédito y débito Sip.
Beneficio: 3% de cashback en compras en Oechsle y plazaVea.
Vigencia: del 1 al 24 de diciembre de 2026.
Condición: pagar con tarjeta Sip y activar la campaña desde la app.
Tope: S/ 60 de cashback por cliente en toda la campaña.
Público: todos los clientes Sip.

PIEZAS QUE SE NECESITAN
1. Banner para la pantalla de inicio de la app: 1200 × 600 px.
   Título de máximo 5 palabras, subtítulo de máximo 10 y botón «Actívala».
2. Historia para Instagram: 1080 × 1920 px.
   El 3% en grande, los dos comercios, la vigencia y el tope.

TEXTO LEGAL (va en las dos piezas, en letra chica)
Válido del 01/12/2026 al 24/12/2026. Tope de S/ 60 por cliente. Aplican términos y condiciones en sip.pe."""

PROMPT_BANNER = """Con el brief de «Navidad te devuelve», la ficha de identidad de Sip y el logo, diseña las 2 piezas del brief:

1. Banner para la app de 1200 × 600 px.
2. Historia para Instagram de 1080 × 1920 px.

Reglas:
- El 3% es lo más grande de cada pieza.
- Los textos salen del brief: no inventes comercios, fechas ni condiciones.
- El texto legal completo va en las dos piezas.
- Colores y logo de la ficha. Máximo un signo de exclamación por pieza.
- Un toque navideño sutil: no uses los colores rojo y verde como fondo."""

CHECK_BANNER = """CHECKLIST · REVISA LAS PIEZAS ANTES DE APROBARLAS
1. ¿El 3% es lo más grande de cada pieza?
2. ¿Aparecen Oechsle y plazaVea, y ningún otro comercio?
3. ¿La vigencia dice del 1 al 24 de diciembre?
4. ¿El tope de S/ 60 está en las dos piezas?
5. ¿El texto legal está completo y se lee?
6. ¿El banner tiene título de máximo 5 palabras y el botón «Actívala»?
7. ¿Colores de Sip y el logo arriba? ¿Máximo un signo de exclamación?
Si algo falla, pídelo en el chat: «en la historia, el tope más visible»."""

BRIEF_PANTALLA = """BRIEF · PANTALLA NUEVA «MIS CASHBACKS» EN LA APP SIP (EJEMPLO PARA PRACTICAR)
""" + AVISO + """

OBJETIVO
Que el cliente vea cuánto cashback ganó y cuándo le llega, para bajar los reclamos por «cashback no abonado».

CONTENIDO DE LA PANTALLA (de arriba a abajo)
1. Título «Mis cashbacks» y flecha para volver.
2. Tarjeta grande: «Ganaste este mes» S/ 23.40 · «En camino» S/ 6.85.
3. Filtros: Todos · Abonados · En camino.
4. Lista de movimientos (comercio · fecha · compra · cashback · estado):
   plazaVea       · 02/10 · S/ 186.40 · S/ 1.86 · Abonado
   Inkafarma      · 05/10 · S/ 64.90  · S/ 0.65 · Abonado
   Promart        · 09/10 · S/ 329.00 · S/ 3.29 · Abonado
   Tottus         · 12/10 · S/ 145.20 · S/ 0.73 · En camino
   Oechsle        · 14/10 · S/ 612.00 · S/ 6.12 · En camino
   Cineplanet     · 15/10 · S/ 58.00  · S/ 0.29 · Abonado
5. Caja informativa: «Los cashbacks de comercios del grupo llegan en hasta 5 días hábiles; los de otros
   comercios Visa, en hasta 10.»
6. Botón «¿Cómo funciona el cashback?».
7. Barra de navegación inferior: Inicio · Pagar · Mis cashbacks (activa) · Perfil.

NOTA: los montos de la tarjeta grande son de ejemplo y no tienen que cuadrar con la lista."""

PROMPT_PANTALLA = """Con el brief de la pantalla «Mis cashbacks», la ficha de identidad de Sip y las 3 capturas de sip.pe, diseña el prototipo de la pantalla para celular (390 × 844 px).

- Respeta el contenido y el orden del brief. No agregues secciones ni datos.
- Que se vea como parte de la app Sip: usa el estilo de las capturas y los colores de la ficha.
- Hazlo interactivo: los filtros Todos, Abonados y En camino tienen que filtrar la lista.
- Los estados en color: Abonado en verde, En camino en celeste.
- Después, arma una segunda versión con la tarjeta grande en fondo negro y compáralas lado a lado."""

CHECK_PANTALLA = """CHECKLIST · REVISA EL PROTOTIPO
1. ¿Tiene las 7 partes del brief, en ese orden?
2. ¿Los 6 movimientos tienen los montos del brief?
3. ¿Los filtros funcionan? Abonados debe mostrar 4 movimientos y En camino, 2.
4. ¿La caja informativa dice 5 y 10 días hábiles?
5. ¿La barra inferior tiene «Mis cashbacks» activa?
6. ¿Se parece a la app Sip (colores, tipografía y bordes de las capturas)?
7. ¿Hay 2 versiones lado a lado?"""

# --------------------------------------------------- chrome y cowork ---
INSTALAR_CHROME = """CÓMO INSTALAR CLAUDE EN CHROME

1. En Google Chrome, entra a la Chrome Web Store y busca «Claude».
2. Elige «Agregar a Chrome» y fija el ícono en la barra.
3. Haz clic en el ícono e inicia sesión con tu cuenta de Claude de SIP.
4. Se abre un panel al costado: ahí escribes el pedido y Claude trabaja en la pestaña abierta.

PERMISOS
- La primera vez que entra a un sitio, Claude te pide permiso. Puedes darlo solo para esa vez.
- Antes de acciones importantes (enviar un formulario, comprar, publicar) te pregunta.

NECESITA AUTORIZACIÓN DE TI
Instalar extensiones en las laptops de SIP lo autoriza TI. Si no te deja instalarla, sigue la demo en pantalla."""

COMERCIOS_FORM = [
    {"ruc": "20604418827", "razon": "Botica Santa Rosa del Norte S.A.C.", "nombre": "Botica Santa Rosa",
     "rubro": "Farmacias", "distrito": "Los Olivos", "correo": "pagos@boticasantarosa.example",
     "telefono": "987654321", "ventas": 42000},
    {"ruc": "20611253390", "razon": "Inversiones Gastronómicas Mar y Tierra E.I.R.L.", "nombre": "Mar y Tierra",
     "rubro": "Restaurantes y cafeterías", "distrito": "Miraflores", "correo": "admin@marytierra.example",
     "telefono": "955120334", "ventas": 68500},
    {"ruc": "10457712986", "razon": "Quispe Huamán Rosa Elena", "nombre": "Bazar Rosita",
     "rubro": "Retail y tiendas por departamento", "distrito": "San Juan de Lurigancho",
     "correo": "bazarrosita@correo.example", "telefono": "912447880", "ventas": 9800},
]


def codigo_afiliacion(ruc):
    """El mismo calculo que hace el formulario en JavaScript."""
    return "AF-%s-%02d" % (ruc[-4:], sum(int(d) for d in ruc) % 97)


def tabla_comercios():
    l = ["COMERCIOS POR AFILIAR (EJEMPLO PARA PRACTICAR)", AVISO, ""]
    for i, c in enumerate(COMERCIOS_FORM, 1):
        l.append("%d) RUC %s · %s · Nombre comercial: %s · Rubro: %s · Distrito: %s · Correo: %s · "
                 "Teléfono: %s · Ventas mensuales estimadas: S/ %s"
                 % (i, c["ruc"], c["razon"], c["nombre"], c["rubro"], c["distrito"], c["correo"],
                    c["telefono"], "{:,}".format(c["ventas"])))
    return "\n".join(l)


def prompt_formulario():
    return ("Abre este formulario: %s\n\n"
            "Registra los 3 comercios de la lista de abajo, uno por uno:\n"
            "- Llena todos los campos con los datos de cada comercio, tal cual.\n"
            "- Marca la casilla de declaración y haz clic en «Enviar solicitud».\n"
            "- Anota el código de solicitud que aparece al enviar y pasa al siguiente comercio.\n\n"
            "Al final, dame una tabla con: comercio, RUC y código de solicitud.\n"
            "Si un campo del formulario no tiene dato en la lista, déjalo vacío y avísame. No inventes datos.\n\n"
            "%s" % (URL_FORMULARIO, "\n".join(tabla_comercios().split("\n")[3:])))


PROMPT_WEB_COMPETENCIA = """Visita las páginas oficiales de estas 4 billeteras, una por una:
- Sip: https://www.sip.pe
- Yape: https://www.yape.com.pe
- Plin: https://www.plin.pe
- BIM: https://www.bim.com.pe

En cada una, revisa la página principal y la sección de promociones o beneficios, si la hay. Anota:
1. Los beneficios o promociones que se ven hoy (cashback, descuentos, sorteos).
2. Si mencionan algún costo para el usuario.
3. El enlace exacto de la página donde viste cada dato.

Al final, arma una tabla comparativa con las 4 y 3 conclusiones sobre en qué destaca Sip.

Reglas: solo lo que ves en las páginas, sin completar con lo que sabes. Si un dato no aparece, escribe «no publicado». No inicies sesión, no llenes formularios y no aceptes nada."""

CHECK_WEB = """CHECKLIST · REVISA LA TABLA ANTES DE USARLA
1. ¿Las 4 billeteras tienen fila en la tabla?
2. ¿Cada dato tiene el enlace exacto de donde salió? Abre 2 al azar: ¿lo dicen?
3. ¿Usó «no publicado» cuando el dato no estaba, en vez de completarlo?
4. ¿Visitó solo páginas oficiales (sip.pe, yape.com.pe, plin.pe, bim.com.pe)?
5. ¿No inició sesión ni llenó ningún formulario?
6. Compara con el ejercicio de Research: ¿qué encontró aquí que Research no, y al revés?"""

INSTALAR_COWORK = """CÓMO PREPARAR COWORK

1. Descarga la app de escritorio de Claude desde claude.com/download e inicia sesión con tu cuenta de SIP.
2. En la app, abre la pestaña Cowork.
3. Descomprime este kit en tu Escritorio.
4. En Cowork, dale acceso a la carpeta del ejercicio (botón para elegir carpeta).
   Claude solo puede leer y escribir dentro de la carpeta que le das.
5. Pega el prompt y mira cómo trabaja: te muestra cada paso y te pregunta antes de borrar algo.

NECESITA AUTORIZACIÓN DE TI
Instalar la app de escritorio en las laptops de SIP lo autoriza TI. Si no está instalada, sigue la demo en pantalla."""

PROMPT_COMPROBANTES = """Tienes acceso a la carpeta «Comprobantes_octubre». Adentro hay PDFs con nombres desordenados.

1. Abre cada PDF y lee: tipo de documento, proveedor, RUC, número, fecha, concepto, subtotal, IGV y total.
2. Renombra cada factura así: AAAA-MM-DD_Proveedor_Numero.pdf (proveedor sin «S.A.C.» ni espacios; por ejemplo 2026-10-03_ImprentaLaPrensa_F001-0381.pdf).
3. Muévela a una subcarpeta con el nombre del proveedor.
4. Si un PDF no es una factura o es una copia repetida de otra, muévelo a la subcarpeta «Revisar» y dime por qué.
5. Crea el Excel «Resumen_comprobantes.xlsx» con dos hojas:
   - Comprobantes: una fila por factura, con todos los datos del paso 1 y el nombre nuevo del archivo.
   - Por proveedor: proveedor, cantidad de facturas y total.

No borres ningún archivo. Al terminar, dime cuántas facturas ordenaste, cuántos archivos fueron a «Revisar» y el total general."""

PROMPT_REPORTE_COWORK = """Tienes acceso a la carpeta «Reporte_octubre». Adentro hay 4 Excel, uno por semana, con las operaciones de la billetera, y un archivo de notas del equipo.

1. Junta los 4 Excel en uno solo y verifica que no falte ninguna semana. Dime cuántas filas leíste de cada archivo.
2. Crea el documento Word «Reporte_mensual_octubre.docx» con:
   - Total de operaciones y monto del mes.
   - Una tabla por semana: operaciones, monto y variación % frente a la semana anterior.
   - Una tabla por tipo de operación: operaciones y monto.
   - La semana con mayor monto y la de menor.
   - Las incidencias del archivo de notas, una por línea.
   - 3 conclusiones con el dato que sostiene cada una.
3. Guarda también «Consolidado_octubre.xlsx» con todas las filas juntas.

Montos en soles con 2 decimales. No modifiques los archivos originales."""

AGENDA_S2 = [
    ("10 min", "Repaso", "Lo que vimos en la Sesión 1 y tu Skill de correos"),
    ("20 min", "Outlook conectado", "Conectas tu cuenta: bandeja, respuestas y calendario"),
    ("15 min", "Research", "Investigar con fuentes: cuándo y cómo"),
    ("15 min", "Tu segunda Skill", "La tarea que trajiste, convertida en Skill"),
    ("10 min", "Artefactos", "Herramientas que se arman con un pedido"),
    ("10 min", "Claude en Chrome", "Claude trabajando en una pestaña"),
    ("10 min", "Pausa", ""),
    ("10 min", "Ejercicios · Research", "Mercado, regulación y Sip vs. competencia"),
    ("30 min", "Ejercicios · Micro-apps", "5 herramientas hechas con artefactos"),
    ("25 min", "Ejercicios · Skills, Projects y Design", "6 casos nuevos de SIP"),
    ("20 min", "Ejercicios · Chrome y Cowork", "Formularios, webs y archivos"),
    ("5 min", "Cierre", "Qué se lleva cada área"),
]

# (archivo, titulo, etiqueta, descripcion) · lo usan build_decks2.py y el indice de la Sesion 1
FILES2 = [
    ("01_Repaso.html", "Repaso", "Repaso", "Un slide por tema de la Sesión 1, tu Skill de correos y la agenda de hoy."),
    ("02_Outlook_conectado.html", "Outlook conectado", "Sesión 2", "Conectas tu cuenta: priorizar la bandeja, responder en lote y tu semana."),
    ("03_Research.html", "Research", "Sesión 2", "Lo pendiente de la Sesión 1: búsqueda web vs. Research y cómo verificar."),
    ("04_Tu_segunda_Skill.html", "Tu segunda Skill", "Sesión 2", "La tarea que trajiste, convertida en Skill con una ficha y un prompt."),
    ("05_Artefactos.html", "Artefactos", "Sesión 2", "Qué son, cómo se piden, cómo se comparten y qué no hacen."),
    ("06_Claude_en_Chrome.html", "Claude en Chrome", "Sesión 2", "La extensión que trabaja en tu pestaña, con 2 ejercicios: leer una web y gestionar reclamos."),
    ("07_Ejercicios_Research.html", "Ejercicios · Research", "Práctica", "Mercado de billeteras, regulación y Sip vs. competencia."),
    ("08_Ejercicios_Micro_apps.html", "Ejercicios · Micro-apps", "Práctica", "Simulador, dashboard, conciliador, calculadora y clasificador con IA."),
    ("09_Ejercicios_Skills_Projects_Design.html", "Ejercicios · Skills, Projects y Design", "Práctica", "Acta, reporte semanal, comercios, riesgo, banner y pantalla de la app."),
    ("10_Ejercicios_Chrome_y_Cowork.html", "Ejercicios · Chrome y Cowork", "Práctica", "Formulario web, webs de la competencia, comprobantes y reporte."),
    ("11_Cierre.html", "Cierre", "Cierre", "Qué herramienta se lleva cada área y el siguiente paso."),
]

# ------------------------------------------- claude en chrome (bloque 06) ---
URL_PORTAL = URL_BASE + "/sesion-2/formulario/portal_de_reclamos.html"

PROMPT_CHROME_LEER = """Entra a https://www.sip.pe y busca la sección de la tarjeta de crédito Sip.

1. Navega hasta la página donde se comparan las versiones de la tarjeta (Básica, Cero, Plus y Garantía, o las que aparezcan).
2. Arma una tabla con: versión, para quién es, costo o membresía, beneficios principales y requisitos, si los publica.
3. Debajo, explícale en 3 líneas a un cliente nuevo cuál le conviene si compra poco y quiere pagar lo menos posible.
4. Dame el enlace exacto de cada página que usaste.

Reglas: solo lo que dice la web. Si un dato no aparece, escribe «no publicado». No llenes formularios ni hagas clic en «Solicitar»."""

CHECK_CHROME_LEER = """CHECKLIST · REVISA LO QUE ARMÓ CLAUDE
1. ¿Navegó solo dentro de sip.pe?
2. ¿La tabla tiene todas las versiones que muestra la web?
3. Abre el enlace que te dio: ¿los costos y beneficios coinciden con la tabla?
4. ¿Usó «no publicado» cuando el dato no estaba, en vez de suponerlo?
5. ¿Se detuvo antes de «Solicitar»? No debe llenar ni enviar nada.

LO QUE ESTE EJERCICIO MUESTRA
Claude lee la página como tú: hace clic en los menús, baja, cambia de página y junta lo que encuentra en una tabla."""

PORTAL = [  # (id, fecha, cliente, motivo, canal, dias)
    ("R-4101", "05/10/2026", "C-0381", "Cashback no abonado", "App", 22),
    ("R-4102", "06/10/2026", "C-0147", "Cobro no reconocido", "Web", 21),
    ("R-4103", "08/10/2026", "C-0922", "Transferencia no llegó", "App", 19),
    ("R-4104", "09/10/2026", "C-0415", "Pase a cuotas", "Módulo de Atención", 18),
    ("R-4105", "12/10/2026", "C-0263", "Bloqueo de cuenta", "App", 15),
    ("R-4106", "12/10/2026", "C-0754", "Cashback no abonado", "App", 16),
    ("R-4107", "14/10/2026", "C-0099", "Cobro no reconocido", "Teléfono", 13),
    ("R-4108", "15/10/2026", "C-0610", "Transferencia no llegó", "App", 12),
    ("R-4109", "16/10/2026", "C-0337", "Cashback no abonado", "Web", 11),
    ("R-4110", "18/10/2026", "C-0871", "Pase a cuotas", "App", 9),
    ("R-4111", "20/10/2026", "C-0502", "Atención en módulo", "Módulo de Atención", 7),
    ("R-4112", "22/10/2026", "C-0218", "Bloqueo de cuenta", "App", 5),
    ("R-4113", "02/10/2026", "C-0690", "Cobro no reconocido", "App", 25),
    ("R-4114", "25/10/2026", "C-0433", "Otros", "Web", 2),
]
NOTA_ESCALADO = "Fuera de plazo: escalado a supervisor"
ESCALAR = [r[0] for r in PORTAL if r[4] == "App" and r[5] > 15]

PROMPT_CHROME_ACTUAR = """Abre este portal de reclamos de práctica: %s

1. Filtra la tabla por canal «App».
2. Encuentra los reclamos con MÁS de 15 días abiertos.
3. En cada uno: clic en «Gestionar», cambia el estado a «Escalado», escribe en la nota «%s» y haz clic en «Guardar».
4. Cuando termines, dime qué reclamos escalaste y cuántos días tenía cada uno.

No cambies ningún otro reclamo. Si algo no está claro, pregúntame antes de guardar.""" % (URL_PORTAL, NOTA_ESCALADO)

CHECK_CHROME_ACTUAR = """RESULTADO ESPERADO · PORTAL DE RECLAMOS
""" + AVISO + """

Debe escalar estos %d reclamos (canal App y más de 15 días):
  %s

Y NO debe tocar:
  R-4105 (App, exactamente 15 días: no es «más de 15»)
  R-4102 y R-4104 (más de 15 días, pero no son del canal App)

CÓMO VERIFICARLO
Arriba del portal, el contador «Escalados» debe decir %d y el historial de cambios debe mostrar solo esos IDs.
Para repetir el ejercicio, usa el botón «Reiniciar el portal».

LO QUE ESTE EJERCICIO MUESTRA
Claude no solo lee: filtra, abre cada caso, cambia un campo, escribe y guarda, igual que una persona.""" % (
    len(ESCALAR), "\n  ".join("%s (%s días)" % (r[0], r[5]) for r in PORTAL if r[0] in ESCALAR), len(ESCALAR))
