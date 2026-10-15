# -*- coding: utf-8 -*-
"""
Contenido de la Sesion 1 de SIP: casos por herramienta, prompts y textos de los kits.
Regla de los casos: por herramienta hay 3; los dos primeros los hace el facilitador (DEMO)
y el tercero se hace EN CONJUNTO. Todos tienen su material descargable.
Datos de negocio FICTICIOS: no son condiciones, clientes ni cifras reales de Sip.
"""

AVISO = ("DATOS FICTICIOS: creados para practicar. No son condiciones, clientes, cifras ni "
         "políticas reales de Sip.")

# ------------------------------------------------------------------ skills ---
SKILL_RECLAMOS = {
    "slug": "respuesta-a-reclamos",
    "desc": ("Redacta la respuesta a un reclamo o consulta de un cliente de Sip con la estructura y el tono "
             "de atención al cliente. Úsala cuando pegan un reclamo y piden responderlo."),
    "cuerpo": """# Respuesta a reclamos · Sip

Redactas la respuesta a un reclamo de un cliente de la billetera Sip.

## Pasos
1. Lee el reclamo e identifica: producto (tarjeta, billetera, cashback, transferencia), qué pasó, qué pide el cliente y desde qué canal escribió.
2. Si falta un dato clave (fecha, monto, número de operación), dilo al inicio en una línea: «Falta: ...».
3. Redacta la respuesta con esta estructura:
   - Saludo con el nombre del cliente.
   - Reconocimiento del problema en una frase, sin culpar al cliente.
   - Qué revisamos o vamos a revisar.
   - Solución o siguiente paso concreto.
   - Plazo: «te responderemos en un plazo máximo de [plazo que defina el área]».
   - Canal para seguir en contacto: app Sip o Módulos de Atención Sip.
4. Cierra con una línea de firma: «Equipo de Atención al Cliente · Sip».

## Tono
Cercano, claro y breve: máximo 150 palabras. Tutea al cliente. Sin tecnicismos ni jerga bancaria.

## Reglas
- Nunca prometas una devolución, un abono o una anulación que no esté validada: di que se está revisando.
- Nunca pidas claves, CVV, códigos de verificación ni datos completos de la tarjeta.
- Si el reclamo menciona fraude o un cobro no reconocido, recomienda bloquear la tarjeta desde la app.
- Si no puedes responder con la información que tienes, dilo y propone el siguiente paso.
""",
}
SKILL_CAMPANA = {
    "slug": "copies-de-campana",
    "desc": ("Convierte el brief de una campaña de Sip en los copies de cada canal (push, correo, redes y "
             "banner de la app) con la voz de Sip. Úsala cuando pegan un brief y piden los textos."),
    "cuerpo": """# Copies de campaña · Sip

Conviertes un brief de campaña en los textos de cada canal.

## Pasos
1. Del brief, extrae: beneficio, condición principal, vigencia, público y llamado a la acción.
2. Si falta la vigencia o la condición principal, pregúntala antes de escribir.
3. Entrega, en este orden:
   - Push: 2 opciones de máximo 90 caracteres.
   - Correo: asunto (máximo 50 caracteres) y cuerpo de 3 líneas.
   - Post para redes: 1 texto de máximo 280 caracteres.
   - Banner de la app: título de máximo 6 palabras y subtítulo de máximo 10.
4. Al final, la línea de condiciones: «Válido del [inicio] al [fin]. Aplican términos y condiciones en sip.pe».

## Voz de Sip
Cercana, optimista y directa. Habla de plata que vuelve: «te devolvemos plata», «tu compra te devuelve».
Frases cortas. Sin exceso de signos de exclamación (máximo uno por texto).

## Reglas
- No prometas un porcentaje o monto distinto al del brief.
- No inventes comercios, fechas ni condiciones.
- Nada de lenguaje de urgencia falsa («¡últimas horas!») si el brief no lo dice.
""",
}
SKILL_ACTAS = {
    "slug": "acta-de-reunion",
    "desc": ("Convierte notas desordenadas de una reunión del equipo de Sip en un acta con acuerdos, "
             "responsables y fechas. Úsala cuando pegan notas o una transcripción y piden el acta."),
    "cuerpo": """# Acta de reunión · Sip

Conviertes notas o una transcripción en un acta estándar.

## Formato del acta
ACTA DE REUNIÓN
- Fecha y hora:
- Asistentes:
- Objetivo de la reunión: (una línea)

TEMAS TRATADOS
1. Tema: resumen en 2 líneas.

ACUERDOS
| N° | Acuerdo | Responsable | Fecha límite |

PENDIENTES Y RIESGOS
- ...

PRÓXIMA REUNIÓN: fecha o «por definir».

## Reglas
- Un acuerdo sin responsable o sin fecha se marca como «Responsable: por definir» o «Fecha: por definir». No los inventes.
- No agregues temas que no estén en las notas.
- Las cifras se copian tal cual vienen en las notas.
- Máximo una página.
""",
}

CARPETA_ONEDRIVE = "SIP - Conciliacion cashback"

SKILL_CONCILIACION = {
    "slug": "conciliacion-de-cashback",
    "desc": ("Concilia el cashback de Sip: abre en OneDrive los dos archivos de la carpeta «SIP - Conciliacion "
             "cashback» (compras elegibles y cashback abonado), los cruza por ID de compra y entrega las diferencias. "
             "Úsala cuando piden conciliar o revisar el cashback abonado."),
    "cuerpo": """# Conciliación de cashback · Sip

Cruzas las compras que debían recibir cashback contra el cashback que realmente se abonó.

## Pasos
1. Con el conector de Microsoft 365, busca en OneDrive la carpeta «SIP - Conciliacion cashback» y abre sus dos archivos:
   - Compras_elegibles_cashback_*.xlsx (lo que se debía abonar)
   - Cashback_abonado_*.xlsx (lo que se abonó)
   Si no encuentras la carpeta o alguno de los archivos, avisa y no sigas.
2. Confirma cuántas filas leíste en cada archivo y el rango de fechas.
3. Cruza los dos archivos por «ID compra» y clasifica cada diferencia:
   - Compra sin abono: está en compras elegibles y no en abonos.
   - Monto distinto: el abonado no coincide con el cashback esperado.
   - Abono duplicado: el mismo ID aparece más de una vez en abonos.
   - Abono sin compra: está en abonos y no en compras elegibles.
4. Entrega, en este orden:
   - Resumen: total esperado, total abonado y diferencia (S/).
   - Una tabla por tipo de diferencia: ID compra, fecha, comercio, esperado, abonado y diferencia.
   - Tres acciones sugeridas para el equipo de operaciones.

## Reglas
- No modifiques los archivos: solo los lees.
- Montos en soles con dos decimales.
- Si un dato no está en los archivos, escribe «no disponible»: no lo estimes.
""",
}

SKILL_COMUNICADO = {
    "slug": "comunicado-de-mantenimiento",
    "desc": ("Genera el comunicado a clientes de Sip por un mantenimiento programado de la app, siempre con el mismo "
             "formato: solo cambian la fecha, el horario, los servicios afectados y el canal alternativo. Úsala cuando "
             "piden el comunicado de mantenimiento."),
    "cuerpo": """# Comunicado de mantenimiento programado · Sip

Generas siempre el mismo documento. Solo cambian los CAMPOS.

## Campos (pregunta los que falten, en una sola pregunta)
- FECHA del mantenimiento
- HORA DE INICIO y HORA DE FIN
- SERVICIOS AFECTADOS (por ejemplo: transferencias, pago con QR, pago de servicios)
- CANAL ALTERNATIVO (por ejemplo: tarjeta de débito Sip en tiendas, Módulos de Atención Sip)
- FECHA DE EMISIÓN

## Texto fijo (no lo cambies)
TÍTULO: Mantenimiento programado de la app Sip

Hola,

Para seguir mejorando tu experiencia, el [FECHA] realizaremos un mantenimiento programado de la app Sip
entre las [HORA DE INICIO] y las [HORA DE FIN].

Durante ese horario no estarán disponibles: [SERVICIOS AFECTADOS].

Mientras tanto, puedes usar: [CANAL ALTERNATIVO].

Tu dinero y tus datos están seguros. Al terminar el mantenimiento, todo funcionará con normalidad.

Gracias por tu comprensión.
Equipo Sip
[FECHA DE EMISIÓN]

## Entrega
1. Un documento Word (.docx) con el título en negrita y el texto fijo con los campos completos.
2. Debajo, en el chat, el mismo texto para copiarlo en un correo.

## Reglas
- No cambies ni una palabra del texto fijo.
- No inventes campos: si falta uno, pregúntalo.
- El horario siempre en formato de 24 horas (por ejemplo, 23:00).
""",
}

DATOS_COMUNICADO = """DATOS PARA PROBAR LA SKILL

PRUEBA 1 (completa)
Fecha: domingo 25 de octubre de 2026
Hora de inicio: 01:00 · Hora de fin: 05:00
Servicios afectados: transferencias y pago con QR
Canal alternativo: tarjeta de débito Sip en tiendas
Fecha de emisión: 20 de octubre de 2026

PRUEBA 2 (le falta un campo: la Skill debe preguntarlo)
Fecha: sábado 7 de noviembre de 2026
Hora de inicio: 23:00 · Hora de fin: no indicada
Servicios afectados: pago de servicios
Canal alternativo: Módulos de Atención Sip"""

COMO_SUBIR_ONEDRIVE = """CÓMO PREPARAR TU ONEDRIVE PARA ESTA SKILL
1. En tu OneDrive, crea una carpeta llamada exactamente: SIP - Conciliacion cashback
2. Sube ahí los dos Excel de la carpeta 1_Para_construir:
   - Compras_elegibles_cashback_Oct_2026.xlsx
   - Cashback_abonado_Oct_2026.xlsx
3. Verifica que el conector de Microsoft 365 esté activo en Claude.
4. Sube la Skill (.zip) y pide la conciliación con el prompt de Prompt_para_probar.txt.
Los dos archivos tienen diferencias a propósito: compara con Resultados_esperados.txt."""

RECLAMOS_PRUEBA = """RECLAMO 1 · App Sip
Hola, compré en plazaVea el 2 de octubre por S/ 186.40 pagando con mi tarjeta Sip y hasta hoy no me aparece el cashback del 1%. Ya pasó más de una semana. Me llamo Carla.

RECLAMO 2 · Módulo de Atención
Buenas tardes, en mi estado de cuenta aparece un cobro de S/ 349.90 de una tienda online que no reconozco. Yo no hice esa compra. Necesito que me devuelvan el dinero hoy mismo. Soy Jorge.

RECLAMO 3 · Correo
Hice una transferencia de S/ 500 a mi hermana desde la app y le dice que no le llegó. A mí ya me descontaron. ¿Qué pasó? Atentamente, Lucía."""

BRIEF_CAMPANA = """BRIEF · CAMPAÑA «NOVIEMBRE TE DEVUELVE»
Producto: Tarjeta de crédito y débito Sip.
Beneficio: 2% de cashback (en lugar del 1%) en compras en Inkafarma y Promart.
Vigencia: del 1 al 30 de noviembre de 2026.
Condición principal: pagar con tarjeta Sip; cashback máximo de S/ 40 por cliente en el mes.
Público: clientes Sip que compraron en Inkafarma o Promart en los últimos 3 meses.
Objetivo: aumentar la frecuencia de compra con tarjeta Sip en esos dos comercios.
Llamado a la acción: activar la campaña desde la app.
Canales: push, correo, redes y banner de la app."""

NOTAS_REUNION = """notas comité semanal canales digitales - lun 12 oct
estuvieron: Andrea (producto), Martín (operaciones), Rocío (atención), Diego (marketing), Paola (TI)
- app: subió 18% las quejas por cashback no abonado en sept, rocío dice q la mayoría son compras en comercios Visa (0.5%) que tardan más en reflejarse
- martín: proceso de abono de cashback corre 2 veces por semana, se podría pasar a diario, paola revisa si TI puede y avisa el viernes 16
- diego: campaña noviembre (2% inkafarma y promart) lista, falta ok de legal para TyC. diego lo pide hoy
- andrea quiere un mensaje en la app explicando plazos del cashback, rocío arma el texto, para el 19
- pendiente: definir si el tope de S/40 se comunica en el push o solo en TyC - no se decidió
- prox reunion lunes 19"""

# ---------------------------------------------------------------- conectores ---
ACTIVAR_CONECTOR = """CÓMO ACTIVAR EL CONECTOR DE MICROSOFT 365 EN CLAUDE (NAVEGADOR)

1. En claude.ai, abre el menú de Configuración > Conectores.
2. Busca «Microsoft 365» y elige Conectar.
3. Inicia sesión con tu cuenta corporativa y revisa los permisos que pide.
4. En un chat nuevo, abre el menú de herramientas y verifica que el conector esté activo.

IMPORTANTE
- El conector lo habilita TI de SIP para la organización. Si no te aparece, todavía no está habilitado:
  en la Sesión 2 lo configuramos juntos.
- Claude solo ve lo que tu cuenta ya puede ver: tu correo, tu calendario y tus archivos.
- Revisa siempre antes de enviar: Claude prepara el borrador; enviarlo es decisión tuya."""

QUE_REVISAR_CONECTOR = """ANTES DE USAR LO QUE TE DEVUELVE CLAUDE
1. ¿Encontró el correo, la reunión o el archivo correcto? Pídele el asunto, la fecha y el remitente.
2. ¿Lo que resume está en el original? Abre el correo o el archivo y contrasta un dato.
3. ¿El borrador sale con tu nombre? Léelo completo antes de enviarlo.
4. ¿Hay datos de clientes? No los pegues en otros chats ni los reenvíes fuera de la empresa."""

PROMPT_HILO = """Busca en mi Outlook el hilo de correos más reciente sobre [tema, por ejemplo: campaña de noviembre].

1. Resúmelo en 5 viñetas: qué se pide, quién lo pide, fecha límite, qué se decidió y qué sigue pendiente.
2. Redacta un borrador de respuesta mío, cordial y de máximo 120 palabras, que confirme lo decidido y pregunte por lo pendiente.

No envíes nada: solo muéstrame el resumen y el borrador. Dime el asunto y la fecha del hilo que usaste."""

PROMPT_REUNION = """Revisa mi calendario de mañana.

Para cada reunión dame:
- Hora, asunto y con quién es.
- Los 2 correos más recientes que intercambié con esas personas y de qué tratan.
- Si hay documentos en mi OneDrive relacionados con el tema, el nombre y el enlace.
- 3 puntos que debería llevar preparados.

Si una reunión no tiene información relacionada, dilo en vez de suponer."""

PROMPT_ONEDRIVE = """Busca en mi OneDrive el documento más reciente sobre [tema, por ejemplo: procedimiento de reclamos].

1. Dime el nombre, la fecha de modificación y de qué trata en 3 líneas.
2. Responde esta pregunta usando solo ese documento: [tu pregunta].
3. Indica en qué sección o página está la respuesta.

Si no encuentras el documento o la respuesta no está ahí, dilo."""

# ------------------------------------------------------------------ projects ---
P1_INSTR = """Eres el asistente del equipo de Atención al Cliente de Sip, la billetera digital que te devuelve plata.

CÓMO RESPONDES
- Primero la respuesta, en lenguaje simple; después, si hace falta, el detalle.
- Usa solo la información de los documentos del Project. Si algo no está, dilo: «No tengo esa información en los documentos».
- Cuando cites una condición, di de qué documento la sacaste.
- Para respuestas a clientes: tutea, sé breve (máximo 120 palabras) y cierra con el siguiente paso.

LO QUE NO HACES
- No prometes devoluciones ni abonos que no estén validados.
- No pides ni guardas claves, CVV, códigos de verificación ni datos completos de tarjetas."""

P1_PRODUCTOS = """PRODUCTOS SIP (RESUMEN DE EJEMPLO PARA PRACTICAR)
Basado en la información pública de sip.pe. Las condiciones detalladas son de ejemplo.

BILLETERA SIP
- App para pagar con QR, transferir con el número de celular, pagar servicios y recargar el celular.
- Cashback: 1% en plazaVea, Inkafarma, Mass, Makro, Oechsle y Promart; 0.5% en comercios que acepten Visa.
- El cashback se ve en la app.

TARJETA DE CRÉDITO SIP
- Se solicita por la web o en Módulos de Atención Sip.
- Las compras disponibles se pueden pasar a cuotas desde la app, en línea o en los Módulos de Atención Sip.
- Versiones: Básica, Cero, Plus y Garantía.

TARJETA DE DÉBITO SIP
- Para comprar en línea y en tiendas con el saldo de la cuenta.

DEPÓSITO A PLAZO FIJO
- Ahorro a plazo con tasa fija. (Tasas y plazos: ejemplo, consultar el tarifario vigente.)

CANALES
- App Sip, sip.pe y Módulos de Atención Sip en tiendas del grupo."""

P1_FAQ = """PREGUNTAS FRECUENTES (EJEMPLO PARA PRACTICAR)

¿Cuándo se refleja el cashback?
Ejemplo: en comercios del grupo, hasta 5 días hábiles; en otros comercios Visa, hasta 10 días hábiles.

¿Puedo pasar a cuotas una compra ya hecha?
Sí, si la compra está disponible para pasar a cuotas. Se hace desde la app, en línea o en un Módulo de Atención Sip.

¿Qué hago si veo un cobro que no reconozco?
Bloquea la tarjeta desde la app y registra el reclamo en la app o en un Módulo de Atención Sip.

Hice una transferencia y no llegó, ¿qué hago?
Revisa en la app el estado de la operación y el número de destino. Si figura como realizada y no llegó, registra el reclamo con el número de operación.

¿Sip me pide mi clave por correo o teléfono?
Nunca. Sip no pide claves, CVV ni códigos de verificación por ningún canal."""

P1_GUIA = """GUÍA DE RESPUESTA AL CLIENTE (EJEMPLO)
Estructura: saludo con nombre · reconocimiento del problema · qué revisamos · siguiente paso · plazo · canal.
Plazo de respuesta a reclamos: el que defina el área (en este ejemplo, 15 días hábiles).
Tono: cercano, claro, sin jerga. Máximo 120 palabras.
Escalar al supervisor: montos mayores a S/ 1,000, casos de fraude o clientes que reclaman por tercera vez."""

P1_PRUEBAS = """PREGUNTAS PARA PROBAR EL PROJECT
1. Un cliente pregunta por qué su cashback de una compra en Promart no aparece. Respóndele.
2. ¿En qué comercios el cashback es de 1% y en cuáles de 0.5%?
3. Explícale a un cliente cómo pasar a cuotas una compra, en 3 pasos.
4. Un cliente dice que le cobraron S/ 1,250 por una compra que no hizo. ¿Qué le respondes y a quién se escala?
5. PRUEBA TRAMPA: ¿Cuál es la tasa exacta del depósito a plazo fijo a 12 meses?
   Lo correcto es que diga que ese dato no está en los documentos."""

P2_INSTR = """Eres el analista de datos del área de Canales Digitales de Sip.

Trabajas sobre el archivo de transacciones del mes que está en el Project.
- Antes de analizar, confirma cuántas filas leíste y el rango de fechas.
- Cifras en soles con dos decimales; porcentajes con un decimal.
- Cada cifra que des debe poder rastrearse a una columna del archivo.
- Si te piden algo que no está en el archivo, dilo.
- Formato por defecto: 5 viñetas máximo y una tabla si comparas más de tres cosas."""

P2_DICCIONARIO = """DICCIONARIO DE DATOS · Transacciones_Septiembre_2026.xlsx
ID            identificador de la transacción (T-00001)
Fecha         fecha de la operación
Tipo          Pago QR · Compra con tarjeta · Transferencia · Pago de servicios · Recarga celular
Comercio      comercio donde se pagó (solo en Pago QR y Compra con tarjeta)
Grupo         «Grupo» si el comercio es del grupo (cashback 1%), «Visa» si es otro comercio (0.5%), «—» si no aplica
Canal         App o Web
Región        Lima, Norte, Sur, Centro u Oriente
Monto (S/)    monto de la operación en soles
Cashback (S/) monto devuelto al cliente
Cliente       segmento: Nuevo (menos de 3 meses) o Recurrente
No hay nombres, DNI ni números de tarjeta: el archivo ya viene anonimizado."""

P2_PRUEBAS = """PREGUNTAS PARA PROBAR EL PROJECT
1. ¿Cuántas transacciones y cuánto monto hubo en septiembre, por tipo de operación?
2. ¿Cuánto cashback se devolvió en total y qué 3 comercios generaron más cashback?
3. Compara el monto de clientes nuevos vs. recurrentes. ¿Qué te llama la atención?
4. ¿Qué región tuvo el mayor ticket promedio?
5. Escribe 3 conclusiones para el comité de canales, una línea cada una, con el dato que la sostiene."""

P3_INSTR = """Eres el asistente del equipo de Marketing y Comunicación de Sip.

- Usa la guía de voz para todo texto que escribas.
- Antes de proponer una campaña, revisa el calendario para no chocar con otra.
- Cuando evalúes una campaña, usa los resultados anteriores como referencia y di cuál.
- No inventes porcentajes, comercios ni fechas: si faltan, pregúntalos.
- Formato por defecto: viñetas cortas; textos de campaña siempre por canal."""

P3_VOZ = """GUÍA DE VOZ DE SIP (EJEMPLO PARA PRACTICAR)
Personalidad: cercana, optimista, práctica. Habla como un amigo que sabe de plata.
Mensaje central: «La billetera digital que te devuelve plata».
Sí: frases cortas, tuteo, beneficios concretos («te devolvemos 1%»).
No: tecnicismos, letras chicas escondidas, urgencia falsa, más de un signo de exclamación.
Colores de marca: celeste Sip #00B1FF, negro #1B1B1D y blanco."""

P3_CALENDARIO = """CALENDARIO DE CAMPAÑAS · CUARTO TRIMESTRE 2026 (EJEMPLO)
Octubre 1–31     «Octubre sipeado»: 1% cashback en el grupo + sorteo semanal en la app.
Noviembre 1–30   «Noviembre te devuelve»: 2% en Inkafarma y Promart (tope S/ 40).
Noviembre 27–30  Cyber: cuotas sin intereses en Oechsle (pendiente de confirmar).
Diciembre 1–24   Navidad: por definir.
Diciembre 26–31  Fin de año: por definir."""

P3_RESULTADOS = """RESULTADOS DE CAMPAÑAS ANTERIORES (EJEMPLO)
Campaña                    Mes        Clientes que activaron   Compras con Sip   Cashback pagado   Costo por compra
«Vuelta al cole» 2%        marzo      18,400                   41,200            S/ 96,300         S/ 2.34
«Día de la madre» 1.5%     mayo       22,900                   52,700            S/ 118,600        S/ 2.25
«Fiestas Patrias» 2%       julio      25,300                   49,900            S/ 131,700        S/ 2.64
«Octubre sipeado» 1%       octubre    en curso                 —                 —                 —"""

P3_PRUEBAS = """PEDIDOS PARA PROBAR EL PROJECT
1. Propón 3 ideas para la campaña de Navidad (1 al 24 de diciembre) que no choquen con el calendario.
2. Escribe 2 opciones de push para «Noviembre te devuelve», de máximo 90 caracteres.
3. ¿Qué campaña anterior tuvo el menor costo por compra y qué la diferenció?
4. PRUEBA TRAMPA: ¿Cuántos clientes activaron «Octubre sipeado»?
   Lo correcto es que diga que todavía está en curso y no hay dato."""

# ------------------------------------------------------------------ research ---
PROMPT_R1 = """Investiga el mercado de billeteras digitales en el Perú a 2026.

Quiero:
1. Las principales billeteras (por ejemplo Yape, Plin, Sip, BIM y otras) con: entidad detrás, usuarios reportados y su diferencial.
2. Los datos de adopción más recientes (SBS, BCRP o estudios de mercado).
3. Tres tendencias que estén cambiando el mercado.

Formato: resumen ejecutivo de una página, con una tabla de billeteras.
Reglas: fuente y fecha al lado de cada dato. Si un dato no lo encuentras, escribe «no encontrado». Al final, lista lo que no pudiste confirmar."""

PROMPT_R2 = """Investiga qué exige hoy la regulación peruana a una billetera digital como Sip.

Cubre:
1. Interoperabilidad de pagos (BCRP): qué se exige y desde cuándo.
2. Dinero electrónico y protección al usuario (SBS): obligaciones principales.
3. Atención de reclamos: plazos y canales que pide la norma.

Formato: tabla con norma, entidad, fecha, qué exige en una línea y enlace oficial.
Reglas: separa lo VIGENTE de lo que está EN CONSULTA o anunciado. Solo fuentes oficiales o medios reconocidos. Si no encuentras la fecha, dilo."""

PROMPT_R3 = """Compara los beneficios que ofrecen hoy las billeteras y tarjetas digitales en el Perú frente a Sip.

Para Sip, Yape, Plin, BIM y al menos 2 tarjetas de crédito digitales:
- Cashback o puntos (porcentaje y en qué comercios).
- Promociones vigentes este mes.
- Costo para el usuario (mantenimiento, comisiones).

Formato: tabla comparativa y 3 conclusiones sobre dónde Sip se diferencia y dónde está detrás.
Reglas: fuente y fecha en cada dato. Lo que no encuentres, «no encontrado». No completes con supuestos."""

CHECKLIST_RESEARCH = """CHECKLIST PARA VERIFICAR UNA INVESTIGACIÓN
1. ¿Cada dato tiene fuente y fecha? Lo que no tiene, no se usa.
2. Abre 2 enlaces al azar: ¿dicen lo que la IA dice que dicen?
3. ¿Las fechas son recientes? Un dato de 2023 puede ya no servir.
4. ¿Separó lo confirmado de lo anunciado o «no encontrado»?
5. ¿Las fuentes son oficiales (SBS, BCRP, la empresa) o medios reconocidos?
6. Antes de compartirlo: ¿lo firmarías con tu nombre?"""

# -------------------------------------------------------------------- design ---
IDENTIDAD = """IDENTIDAD VISUAL DE SIP PARA CLAUDE DESIGN (FICHA DE EJEMPLO)
Colores
- Principal: celeste Sip #00B1FF
- Texto y fondos oscuros: negro #1B1B1D
- Fondo: blanco #FFFFFF; celeste claro #DEF2FF para cajas
Tipografía: sans serif en negrita para títulos, regular para textos.
Estilo: limpio, fondos blancos, una idea por slide, cifras grandes.
Logo: arriba a la izquierda (súbelo como imagen si lo tienes).
No usar: colores de la competencia, gráficos 3D, fondos recargados, más de 3 colores por gráfico."""

PROMPT_D1 = """Con el archivo de transacciones de septiembre y la ficha de identidad de Sip, arma una presentación ejecutiva de 6 slides para el comité de Canales Digitales.

Que responda:
1. Cuánto se movió en el mes y por qué tipo de operación.
2. Cuánto cashback devolvimos y en qué comercios.
3. Nuevos vs. recurrentes.
4. Qué región destaca.
5. Tres conclusiones con el dato que las sostiene.

Una idea por slide, cifras grandes, colores de la ficha. No incluyas nada que no esté en el archivo."""

PROMPT_D2 = """Con el brief de la campaña «Noviembre te devuelve» y la ficha de identidad de Sip, arma un one-pager para enviar al equipo comercial.

Debe tener: el beneficio en grande, vigencia, comercios, condición y tope, a quién va dirigido, canales y un llamado a la acción.
Una sola página, colores de la ficha, nada que no esté en el brief."""

PROMPT_D3 = """Con el archivo de reclamos del tercer trimestre y la ficha de identidad de Sip, arma una presentación de 5 slides para la jefatura de Atención al Cliente.

Que muestre:
1. Total de reclamos por mes.
2. Los 3 motivos principales.
3. Tiempo promedio de respuesta por canal de ingreso.
4. Cuántos siguen en proceso.
5. Dos recomendaciones con el dato que las sostiene.

Una idea por slide, colores de la ficha. Solo datos del archivo."""

# ----------------------------------------------------------------- practica ---
PROMPT_SKILL_CORREOS = """Quiero crear una Skill que escriba correos con mi estilo.

Abajo te pego 5 correos que yo envié. Analízalos y detecta cómo escribo: saludo y despedida, largo de las frases, nivel de formalidad, palabras que repito, cómo pido las cosas, cómo cierro y mi firma.

Con eso crea la Skill «correos-con-mi-estilo»:
- Se usa cuando le paso un borrador rápido o una idea suelta de correo (por ejemplo: «dile a Ana que el reporte va el viernes»).
- Devuelve solo el correo final, con asunto y cuerpo, como yo lo habría escrito. Sin explicaciones ni variantes.
- Si falta un dato clave (a quién va, qué se pide, una fecha), lo deja entre corchetes en lugar de inventarlo.
- Imita mi estilo, no copia frases enteras de mis correos.

Al final, dame la Skill lista para guardar.

MIS 5 CORREOS
[Correo 1: pega el texto completo]
[Correo 2]
[Correo 3]
[Correo 4]
[Correo 5]"""

COMO_ELEGIR_CORREOS = """CÓMO ELEGIR TUS 5 CORREOS
1. En Outlook, entra a «Elementos enviados».
2. Elige 5 correos que escribiste tú (no reenvíos ni respuestas de una línea).
3. Que sean variados: a tu jefe, a un compañero, a otra área, uno que pide algo y uno que da una noticia.
4. Copia el texto completo de cada uno, con saludo y firma.
5. Aplica el semáforo: cambia nombres de clientes, DNI, montos de personas y todo dato confidencial por [CLIENTE], [MONTO], etc."""

BORRADORES_PRUEBA = """CÓMO PROBAR TU SKILL
Abre un chat nuevo y escribe solo el borrador, rápido y vago. Prueba estos tres:

1. avisale a mi jefe q el informe de octubre se retrasa un dia xq falta la data de finanzas
2. pedirle a ti q me habilite el acceso al sharepoint del equipo, urgente
3. agradecer al equipo de marketing por la campaña de noviembre, salio muy bien

Revisa en cada correo:
- ¿Suena a ti? ¿Saludas y te despides así?
- ¿Dejó entre corchetes lo que faltaba en vez de inventarlo?
- Si algo no te gusta, díselo en el chat y pídele que actualice la Skill."""

TAREA = [
    "Usa tu Skill de correos esta semana en correos reales y anota qué tuviste que corregir.",
    "Elige una tarea que repites siempre igual: será tu segunda Skill en la Sesión 2.",
    "Trae un Excel o reporte de tu área (anonimizado) para construir un artefacto.",
    "Confirma con TI si el conector de Microsoft 365 ya está habilitado en tu cuenta.",
]
