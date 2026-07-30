# RevOS v4 — Auditoría terminológica y análisis de mejoras

Fecha: 30/07/2026 · Fuentes: Master Doc v1.1, Blueprint v3, Workflow v3, Timeline HTML, las 24 skills RevOS instaladas y sesiones recientes (Kokolski, Barkibu, gtm-planner).

---

## PARTE 1 — Auditoría de inconsistencias

### 1.1 Marketing Studio
Cero menciones en los 4 documentos y en las 24 skills. Limpio.

### 1.2 PYMEs B2B (scope a ampliar)
| Dónde | Qué dice |
|---|---|
| Master Doc, tabla ICP | "CEO/Founder de **PYME mediana** B2B o industrial, facturación >1M€" |
| Timeline HTML (detalle revenue-diagnostic) | "más impactante que un Word para **pymes industriales**" |
| Timeline HTML (detalle sales-conversion-design) | "Crítico para **pymes industriales** donde el handoff…" |
| Skill `crm-selection` (línea 61) | "**PYME B2B** con marketing ligero y equipo pequeño: HubSpot…" |

Ampliar el scope no es solo sustituir la palabra: arrastra decisiones de negocio — el umbral ">1M€", el claim "sin acceso fácil a talento senior de marketing" (falso en mid-market), el pricing (3.500€/7.300€ y 150€/h quedan cortos para empresas grandes) y la heurística de crm-selection (HubSpot por defecto no aplica a mid-market con Salesforce). Marcar como decisión estratégica, no como buscar/reemplazar.

### 1.3 Término prohibido "Gate"
17 menciones en documentos + 1 en skills:
- Master Doc: "Gate de validación" ×2 (diagnostic-checkpoint, propósito).
- Blueprint (Matriz): "Gate de validación" en diagnostic-checkpoint y design-checkpoint.
- Timeline HTML: "Gate cliente" (leyenda), "Gate ✓" ×2, y textos en el JS de detalle.
- Skill `diagnostic-checkpoint`: 1 uso ("gate de validación").

Nota: el sistema ya usa "checkpoint" como término asentado (diagnostic-checkpoint, design-checkpoint, final checkpoint). Sugerencia: consolidar en "checkpoint" / "hito de validación" en lugar de introducir "Peaje", que connota coste/fricción en castellano. Decisión tuya; ambas son un reemplazo mecánico.

### 1.4 Término prohibido "Cuello" (a secas)
El Master Doc usa correctamente "cuellos de botella". El problema está en las skills:
| Skill | Usos de "cuello/cuellos" sin "de botella" |
|---|---|
| `revenue-diagnostic` | ~15 (títulos "Cuello #1/#2/#3", "los cuellos", "cuellos priorizados"…) |
| `execution-roadmap-builder` | 5 ("cuellos del diagnóstico", columna "Cuello del diagnóstico") |
| `growth-system-design` | 3 |
| `positioning-messaging` | 2 |
| `system-qa` | 1 |
| `knowledge-base-builder` | 1 |

### 1.5 Otras inconsistencias detectadas (no pedidas, relevantes)
1. **"Core v1 / Core v2"** en el Timeline HTML (29 menciones) vs. "Essentials / Complete" en el resto. Nomenclatura antigua.
2. **"Deployment"** como nombre de la fase 3 en el Workflow xlsx vs. "Activation" en todo lo demás. Y el Master Doc §4 define las fases como "Diagnostic, Design y **Opcionales**" — tampoco coincide.
3. **Versionado incoherente entre documentos canónicos**: el archivo se llama "Master Doc v1.1 160426" pero la portada dice "Versión 1.0 · Abril 2025" (¿2026?). Blueprint y Workflow van por "v3". No hay esquema común — irónico siendo una de tus mejoras.
4. **Typo "XSLX"** ×6 en el Workflow.
5. **Desajuste de inventario**: la tabla de skills del Master Doc omite `design-checkpoint` y `revos-orchestrator`, que sí existen en el Blueprint. El Timeline dice "27 skills". Además `revos-orchestrator` está definido en el Blueprint pero **no existe como skill instalada** — hueco que la mejora de plugins resuelve.
6. **Contradicción de formato de salida**: Master Doc dice "Markdown por defecto, DOCX solo si se pide"; el Blueprint asigna DOCX por skill como formato del entregable. Tu mejora de elección de output la resuelve — hay que reescribir ambos.
7. **Naming actual con guiones bajos dictado por las propias skills**: ~20 skills instruyen guardar como `[empresa]_skill_v1.md`. Choca frontalmente con tu nueva regla de naming.
8. **Operativa pre-Cowork**: el Master Doc §5 gira en torno a "Projects de claude.ai" y prompts de arranque por conversación. Con la migración a Cowork + plugins, toda la sección 5 queda obsoleta.
9. Portada del Master Doc duplica el subtítulo ("Sistema de revenue…" / "Revenue systems…").

---

## PARTE 2 — Análisis y jerarquización de las 9 mejoras

Criterio: primero las que condicionan a las demás (arquitectura), luego las que cambian el método, al final las de superficie. Según tu propio esquema de la imagen: casi todo lo del Nivel 1-2 es cambio de **Concepto** (reescribir, v1→v2, backlog obligatorio); el Nivel 3 es **Dato/Cosmético** (editar).

### NIVEL 1 — Estructurales (decidir y diseñar primero)

**1. Stack tecnológico: ¿Claude/Cowork o Google Cloud/n8n?** *(tu mejora 9 — va primero porque es la decisión madre)*
Un proyecto RevOS es: documentos que entran, documentos que salen, 17–62 horas, un consultor, cliente único por vez. Eso vive cómodamente entero en Claude/Cowork: skills, plugins, conectores MCP para CRM/ERP, scheduled tasks para cadencias, carpetas locales para el filesystem del proyecto. n8n/GCP aportarían valor solo con: (a) automatización desatendida multi-cliente (pipelines que corren solos), (b) volumen que exija paralelización, o (c) productización SaaS del sistema. Hoy no se da ninguna. **Recomendación: quedarse en Cowork como plataforma única para v4 y fijar triggers de revisión** (p.ej. >4 proyectos simultáneos o necesidad de ejecución sin humano). Evita mantener dos stacks mientras el cuello de botella real es metodológico, no de infraestructura.

**2. De skills sueltas a plugin(s) interno(s)** *(tu mejora 1 — la más profunda)*
Es la mejora paraguas: casi todas las demás acaban viviendo dentro del plugin, por lo que conviene **una sola reescritura v4 de las skills, no dos pasadas**. Diseño natural:
- **Un único plugin "RevOS"** (no tres por fase): las dependencias entre fases son fuertes y el estado del proyecto es uno. Comandos por fase dentro del plugin.
- **Orquestador**: el `revos-orchestrator` ya especificado en el Blueprint v3 (state log, next best action, routing) y nunca implementado pasa a ser el cerebro del plugin. Es la pieza donde se codifican: fase 0, límite de revisiones, esquema de versiones y elección de output.
- **Comandos**: `/revos:fase-0`, `/revos:diagnostic`, `/revos:checkpoint`, `/revos:qa`, `/revos:status`…
- **Agentes**: los candidatos claros son research competitivo (paralelo, autónomo), system-qa (read-only, transversal) y un agente de extracción CRM/ERP. Espejo de lo que ya hiciste en gtm-planner (market-researcher, plan-qa, materials-analyst) — ese plugin es tu plantilla validada.
- **Conectores predeterminados**: ver mejora 3.
Riesgo principal: sobre-ingeniería. Mitigación: empaquetar lo que ya funciona + las mejoras de esta lista, sin añadir funcionalidad nueva no pedida.

**3. Conexión CRM/ERP en intake** *(tu mejora 8)*
Sí, contemplarla — es la mejora con más impacto sobre la calidad del dato de todo el sistema descendente y reduce directamente los [FALTA DATO] (conecta con la mejora 5). Cowork ya soporta conectores MCP de HubSpot, Salesforce, Pipedrive, etc. Implementación: `client-intake-form`/`brief-intake` y `martech-stack-audit` ganan un paso condicional "si hay CRM conectado, extraer funnel real (volúmenes, conversión por etapa, ciclo, ticket) con procedencia marcada [DATO CRM]"; el plugin declara los conectores como opcionales. Cautelas: acceso de solo lectura, acuerdo de confidencialidad con el cliente, y regla explícita de que dato de CRM sucio se marca como [DATO NO FIABLE], no se toma como verdad. ERP: dejarlo para una segunda iteración — el valor inmediato está en el CRM.

### NIVEL 2 — Metodológicos (cambian el proceso)

**4. Límite de revisiones / gestión de [FALTA DATO]** *(tu mejora 5 — la de mayor criticidad operativa del nivel)*
Ataca la causa declarada nº1 de errores y freno. Propuesta concreta:
- Clasificar cada dato faltante como **bloqueante** (impide decidir) o **no bloqueante** (afina pero no cambia la decisión). Solo los bloqueantes justifican parar.
- **Máximo 2 ciclos de revisión por entregable**. Al agotarse, cada [FALTA DATO] no bloqueante se convierte en **[ASUNCIÓN]** documentada (valor asumido + fuente del criterio) y se registra en el backlog del proyecto.
- Los checkpoints con cliente incluyen una sección fija "asunciones vigentes" — el cliente las valida o las corrige, pero el sistema nunca se detiene por ellas.
Toca: System Prompt maestro, convenciones de etiquetado (§6 del Master Doc), todas las skills y ambos checkpoints. Es cambio de Concepto.

**5. Fase 0 — estructura de carpetas estándar** *(tu mejora 2)*
Sencilla, alto retorno, y es el sustrato físico del versionado y el backlog. Propuesta:
```
[Cliente]/
  00 Sistema/          → estructura del proyecto, backlog de cambios, state log, preferencia de output
  01 Entregables/
  02 Anexos/
  03 QA/
  04 Archivo/          → versiones antiguas
```
Se implementa como comando `/revos:fase-0` del plugin: crea carpetas, inicializa backlog y state log, y pregunta la preferencia de output (mejora 6). Pasa a ser fase obligatoria del Workflow y del Timeline.

**6. Esquema de versionado según tu tabla** *(tu mejora 7)*
El esquema (Cosmético → editar sin cambio, opcional en backlog · Dato → editar sin cambio, backlog obligatorio con ficheros afectados y estado · Concepto → reescribir v1→v2, backlog obligatorio) es sólido y encaja con la fase 0 (backlog vive en `00 Sistema`, versiones antiguas en `04 Archivo`). **El punto no trivial que falta definir: la propagación descendente.** Si un doc upstream pasa a v2 (cambio de Concepto), ¿qué pasa con los entregables que dependen de él? Propuesta: el orquestador consulta el grafo de dependencias del Blueprint y añade al backlog los ficheros descendentes con estado "pendiente de re-validar"; system-qa parcial antes de continuar. Sin esta regla, el esquema gestiona bien el documento cambiado pero no la coherencia del sistema — que es donde hoy se generan las alucinaciones.

### NIVEL 3 — Superficie (mecánicos, se ejecutan al reescribir)

**7. Elección de output HTML u Office** *(tu mejora 3)*
Preguntar **una vez por proyecto en fase 0** (no por entregable) y guardar la preferencia en `00 Sistema`; permitir override puntual. Resuelve de paso la contradicción actual Markdown-vs-DOCX (hallazgo 1.5.6). Cambio de Dato en las 24 skills (la línea de formato de salida) + Blueprint + Master Doc.

**8. Naming limpio sin guiones bajos** *(tu mejora 4)*
Definir la convención antes de tocar nada. Propuesta: `[Cliente] - [Entregable] v1.docx` (espacios y guion medio; legible para cliente) o `cliente-entregable-v1.docx` si prefieres compatibilidad estricta. Hay 21 skills que hoy dictan `[empresa]_skill_v1.md` — es un solo patrón repetido, reemplazo mecánico en la reescritura v4.

**9. Terminología** *(tu mejora 6 + scope pymes)*
Todo mapeado en la Parte 1. "Gate" y "Cuello": reemplazo mecánico en 4 documentos + 6 skills. "Pymes → empresas más grandes": requiere decisión previa de ICP y pricing (ver 1.2). Añadir a la misma pasada: Core v1/v2 → Essentials/Complete, Deployment → Activation, typo XSLX, y unificar el versionado de los propios documentos canónicos.

---

## Orden de ejecución propuesto

1. **Decidir** (sin producir nada): stack (quedarse en Cowork), término sustituto de Gate, convención de naming, nuevo ICP/scope de empresa.
2. **Diseñar el plugin RevOS v4**: arquitectura de orquestador + comandos + agentes + conectores, con las mejoras 3–7 como especificaciones internas.
3. **Reescribir una sola vez**: las 24 skills + Master Doc v2 + Blueprint v4, incorporando terminología, naming, etiquetado nuevo ([ASUNCIÓN]), formato de salida y fase 0. Según tu propio esquema: cambio de Concepto, v-bump y backlog completo.
4. **Pilotar** con un cliente real (Kokolski es candidato natural) antes de dar la v4 por canónica.
