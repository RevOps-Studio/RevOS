# revos — plugin interno de RevOps Studio

Sistema RevOS v4: diagnóstico, diseño y activación de sistemas de revenue para empresas B2B, operado íntegramente en Claude/Cowork.

## Estado: bloques 1-6 de 7 (v4.0.0-alpha.7)

Incluido en este bloque:
- **fase-0** — arranque de proyecto: estructura de carpetas estándar, configuración (tier, output, idioma, conectores) e inicialización de State Log y Backlog de cambios.
- **status** — estado del proyecto y next best action; punto de entrada de cada sesión.
- **revos-orchestrator** — reglas del sistema: grafo de dependencias (27 nodos), propagación de cambios, régimen de revisiones/asunciones y convenciones transversales.
- **cambio** — puerta de entrada única de correcciones: clasificación Cosmético/Dato/Concepto, backlog, archivado en 04 Archivo y propagación aprobada por el consultor.

Incluido además (bloque 3): las 6 skills de la fase Diagnostic (client-intake-form, brief-intake, knowledge-base-builder, competitive-research, revenue-diagnostic, diagnostic-checkpoint) reescritas a convenciones v4, los agentes competitive-researcher y crm-analyst, y el modelo de conectores en dos niveles: investigación y archivos (Ahrefs, Similarweb, Drive, Notion, Dropbox) en .mcp.json; CRM, transcripciones y ads activables por proyecto según el mapa del orquestador.

Incluido además (bloque 4): las 19 skills de Design, Activation y opcionales reescritas a convenciones v4, y el agente system-qa (verificación transversal en solo lectura).

Incluido además (bloque 5): skill `entrega` + agente deliverable-designer con el sistema visual RevOS (tokens de marca, plantilla HTML autocontenida, equivalencias DOCX/XLSX/PPTX). Acento de marca confirmado: #C129A1.

Pendiente (bloques 6-7): documentos canónicos v4 (Master Doc v2, Blueprint v4, Workflow v4, Timeline v2) y piloto con cliente real.

## Uso

0. `/revos:setup` tras instalar el plugin — onboarding guiado y corrección de rumbo.
1. `/revos:fase-0` al arrancar cada proyecto de cliente.
2. `/revos:status` al inicio de cada sesión de trabajo.
3. `/revos:cambio` para cualquier corrección sobre entregables ya producidos.

Referencia de diseño: "RevOS v4 - Especificacion del plugin.md".
