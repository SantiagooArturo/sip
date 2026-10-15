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
