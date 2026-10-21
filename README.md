# SIP · Workshop de IA con Claude

Propuesta 2026-046 (Sip, billetera digital del grupo Intercorp · contacto Lucianna Moreno).
**Claude solo en el navegador (claude.ai): sin Cowork ni Claude in Chrome.**

## Sesión 1 · Fundamentos de IA y entornos de Claude (`sesion-1/`)
`index.html` + 11 decks (armados para 4 h; la sesión dura 3 h) + 16 kits en `materiales/`.
Por herramienta (Skills, Conectores, Projects, Research, Design) hay 3 casos: 1 y 2 demo del facilitador,
3 en conjunto. Cada slide con material tiene botón de descarga; cada prompt, Copiar y Descargar (.txt).

- **Reconstruir:** `cd sesion-1/build && python3 build_materiales.py && python3 build_decks.py && python3 build_index.py && python3 qa.py`
  (requiere openpyxl).
- Kits: LEEME.txt + 1_Para_construir + 2_Para_probar, todo en .txt. Las Skills van también como .zip con SKILL.md
  (formato que pide Claude para subirlas).
- Datos FICTICIOS (transacciones, reclamos, políticas, campañas). Resultados esperados en `build/esperados.json`.
- Diseño: base.css de Interbank (Figtree, paleta Interbank) + logo de Sip recoloreado a celeste #00B1FF.

## Sesión 2 · Taller práctico: Conectores, Skills y Artefactos (`sesion-2/`)
11 decks en el mismo índice (`sesion-1/index.html#s2`) + 22 kits en `sesion-2/materiales/`.
- **01** Repaso · **02–06** lo nuevo: Outlook conectado (3 ejercicios), Research (pendiente de la S1),
  Tu segunda Skill (1 ejercicio), Artefactos, Claude en Chrome · **07–10** ejercicios: Research (3),
  Micro-apps con artefactos (5), Skills/Projects/Design (6), Chrome y Cowork (4) · **11** Cierre.
- Cada ejercicio: slide de ficha (qué se logra, qué trae el kit, pasos, «sale bien si») + slide del prompt
  con Copiar y Descargar. Kit = LEEME.txt + 1_Para_construir (incluye Prompt.txt) + 2_Para_probar.
- Formulario de práctica para Claude en Chrome: `sesion-2/formulario/afiliacion_de_comercios.html`.
- **Reconstruir:** `cd sesion-2/build && python3 build_materiales2.py && python3 build_decks2.py && python3 qa2.py`
  y luego `cd ../../sesion-1/build && python3 build_index.py`. Usa el motor de `sesion-1/build/` (deck.py, qa.py).
