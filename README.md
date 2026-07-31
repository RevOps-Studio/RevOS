# revos — plugin interno de RevOps Studio

Sistema RevOS v4: diagnóstico, diseño y activación de sistemas de revenue para empresas B2B, operado íntegramente en Claude/Cowork.

## Estado: v4.1.0 — piloto de Diagnostic completado

Incluido en este bloque:
- **fase-0** — arranque de proyecto: estructura de carpetas estándar, configuración (tier, output, idioma, conectores) e inicialización de Registro, Estado y Backlog de cambios.
- **status** — estado del proyecto y next best action; punto de entrada de cada sesión.
- **revos-orchestrator** — reglas del sistema: grafo de dependencias (27 nodos), propagación de cambios, régimen de revisiones/asunciones y convenciones transversales.
- **cambio** — puerta de entrada única de correcciones: clasificación Cosmético/Dato/Concepto, backlog, archivado en 04 Archivo y propagación aprobada por el consultor.

Incluido además (bloque 3): las 6 skills de la fase Diagnostic (client-intake-form, brief-intake, knowledge-base-builder, competitive-research, revenue-diagnostic, diagnostic-checkpoint) reescritas a convenciones v4, los agentes competitive-researcher y crm-analyst, y el modelo de conectores en dos niveles: investigación y archivos (Ahrefs, Similarweb, Drive, Notion, Dropbox) en .mcp.json; CRM, transcripciones y ads activables por proyecto según el mapa del orquestador.

Incluido además (bloque 4): las 19 skills de Design, Activation y opcionales reescritas a convenciones v4, y el agente system-qa (verificación transversal en solo lectura).

Incluido además (bloque 5): skill `entrega` + agente deliverable-designer con el sistema visual RevOS (tokens de marca, plantilla HTML autocontenida, equivalencias DOCX/XLSX/PPTX). Acento de marca confirmado: #C129A1.

v4.1.0 incorpora los aprendizajes del primer piloto real (Kokolski, Diagnostic completo — ver docs/RevOS v4 - Aprendizajes del piloto Diagnostic.md): resúmenes que enumeran en lugar de contar (F1), disposición obligatoria de huecos al cierre de cada skill (F2), dos contadores de ciclos — la información nueva no consume revisiones (F3), doble condición de checkpoint con veredicto de QA (F4), paso de medición de activos con conectores en knowledge-base-builder (F5), calibración económica al inicio del brief (F6), partición del State Log en Registro inmutable + Estado regenerado (F7), chequeos mecánicos obligatorios en system-qa (F8), validación de especificación antes de maquetar (F9) y precondición de producción en todas las skills (F10-lite).

Pendiente: pilotos de Design y Activation; forzado determinista de precondiciones (decisión de producto para v5).

## Uso

0. `/revos:setup` tras instalar el plugin — onboarding guiado y corrección de rumbo.
1. `/revos:fase-0` al arrancar cada proyecto de cliente.
2. `/revos:status` al inicio de cada sesión de trabajo.
3. `/revos:cambio` para cualquier corrección sobre entregables ya producidos.

Referencia de diseño: "RevOS v4 - Especificacion del plugin.md".
