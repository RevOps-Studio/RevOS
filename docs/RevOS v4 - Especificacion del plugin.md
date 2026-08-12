# RevOS v4 — Especificación del plugin

Versión 1.0 · 30/07/2026 · Documento de diseño para la reescritura única (paso 3)
Plugin interno de RevOps Studio. No destinado al Directorio.

> **DOCUMENTO HISTÓRICO DE DISEÑO — NO ES REFERENCIA VIGENTE.**
> Refleja el diseño previo al piloto de Kokolski. Superado en:
> · §1 — `.mcp.json` declara los conectores de nivel 1 de research y ficheros (Ahrefs, Similarweb, Drive, Notion, Dropbox), no CRMs. El mapa vigente es `references/conectores.md`.
> · §1 — el plugin tiene 27 nodos + skills de control, no 26 skills. Versión real: 4.2.0.
> · §2, §4 y §6 — el State Log único se partió en Registro (inmutable) + Estado (regenerado). Ver F7.
> · §6 — el presupuesto de revisión son dos contadores separados, no uno. Ver F3.
> · §5 — la precondición de checkpoint es doble (backlog + veredicto de QA). Ver F4.
> Referencia vigente: `references/convenciones.md` (v4.2), `references/grafo-dependencias.md` (v4.2) y `CHANGELOG.md`.

---

## 0. Log de decisiones que gobiernan esta spec

| # | Decisión | Valor acordado |
|---|---|---|
| D1 | Plataforma | Claude/Cowork como stack único. Revisión si >4 proyectos simultáneos o necesidad de ejecución desatendida. |
| D2 | Arquitectura | Plugin único "revos", con comandos por fase. |
| D3 | Scope de cliente | "Empresas B2B" — deliberadamente abierto. Sin "pyme", "industrial", ni calificativo de tamaño. |
| D4 | Término validación | "Checkpoint" (nunca "Gate"). |
| D5 | Término diagnóstico | "Cuellos de botella" o "problemas" (nunca "cuello" a secas como sustantivo del sistema). |
| D6 | Naming de ficheros | `Cliente - Entregable v1.ext` (espacios y guion medio, sin guiones bajos). |
| D7 | Output de entregables | El consultor elige por proyecto en fase 0: HTML u Office. La maquetación de entregables se incorpora como parte del Design. |
| D8 | Revisiones | Máximo 2 ciclos por entregable; después [FALTA DATO] no bloqueante → [ASUNCIÓN]. |
| D9 | Versionado | Esquema Cosmético / Dato / Concepto. Propagación descendente: la decide el orquestador. |
| D10 | Conectores | CRM en intake (lectura), opcional. ERP en iteración posterior. |
| D11 | Reescritura | Una sola pasada v4 de skills + documentos canónicos, después piloto (candidato: Kokolski). |

---

## 1. Estructura del plugin

```
revos/
  .claude-plugin/plugin.json      → name: revos · version: 4.0.0
  commands/
    fase-0.md                     → arranque de proyecto
    status.md                     → estado y next best action (orquestador)
    diagnostic.md                 → fase 1 orquestada
    design.md                     → fase 2 orquestada
    activation.md                 → fase 3 orquestada
    checkpoint.md                 → prepara el checkpoint de la fase en curso
    cambio.md                     → registra un cambio y gestiona versión + propagación
    entrega.md                    → produce el entregable final maquetado (HTML u Office)
    qa.md                         → system-qa transversal
  agents/
    competitive-researcher.md     → research autónomo multi-fuente
    crm-analyst.md                → extracción de datos de CRM conectado
    system-qa.md                  → coherencia transversal (read-only)
    deliverable-designer.md       → maquetación de entregables
  skills/                         → las 26 skills v4 (24 actuales + client-intake-form + revos-orchestrator)
  .mcp.json                       → conectores opcionales: HubSpot · Salesforce · Pipedrive
```

Principio de reparto: las **skills** contienen el conocimiento metodológico (qué es un buen positioning, cómo se estructura un diagnóstico). Los **comandos** contienen la operativa (qué skill toca ahora, con qué inputs, qué validar). Los **agentes** ejecutan trabajo autónomo pesado o de verificación. El consultor deja de invocar skills sueltas: habla con comandos.

---

## 2. El orquestador

`revos-orchestrator` estaba especificado en el Blueprint v3 (REVA-adjacente: state log, next best action, routing) y nunca se implementó. En v4 es el cerebro del plugin, repartido en dos piezas:

**Skill `revos-orchestrator`** — el conocimiento: grafo de dependencias completo (los 27 nodos del Blueprint), reglas de secuencia por tier, reglas de propagación, formato del state log.

**Comando `/revos:status`** — la operativa: lee `00 Sistema/Cliente - State Log.md`, contrasta con el grafo, y devuelve: fase y skill actual, entregables producidos con su versión, asunciones vigentes, cambios pendientes de propagar, y next best action.

### State log (vive en 00 Sistema)

| Campo | Contenido |
|---|---|
| Proyecto | Cliente, tier contratado, fecha inicio, preferencia de output, conectores activos |
| Ejecutado | Skill → entregable → versión → fecha → ciclos de revisión consumidos |
| Asunciones | Lista viva de [ASUNCIÓN] con estado (vigente / validada / corregida) |
| Backlog de cambios | Ver §5 |
| Próximo paso | Skill siguiente + inputs requeridos + huecos conocidos |

### Propagación descendente (D9)

Cuando un entregable upstream cambia, el orquestador decide — no hay regla mecánica. Su criterio, codificado en la skill:

1. Clasifica el cambio (Cosmético / Dato / Concepto) según la tabla de §5.
2. Consulta el grafo de dependencias y lista los entregables descendentes.
3. Evalúa cada descendiente: ¿el cambio afecta a algo que este documento usó como input de decisión?
   - No → lo marca "sin impacto" en el backlog y no se toca.
   - Sí, afecta a datos → marca "pendiente de editar" (cambio Dato en cascada).
   - Sí, afecta al argumento → marca "pendiente de reescribir" (v-bump en cascada) y recomienda system-qa parcial antes de continuar.
4. Presenta el plan de propagación al consultor para aprobación. Nunca propaga sin confirmación.

Esto blinda la coherencia sin convertir cada corrección menor en una reescritura del sistema.

---

## 3. Comandos

| Comando | Qué hace | Sustituye a |
|---|---|---|
| `/revos:fase-0` | Ver §4. Crea la estructura del proyecto y fija las preferencias. | Nada — es nuevo, obligatorio |
| `/revos:status` | Estado + next best action. Punto de entrada de cada sesión de trabajo. | Prompts de arranque del Master Doc §5 |
| `/revos:diagnostic` | Orquesta la fase 1: intake → brief → knowledge base → competitive (agente) → diagnóstico → checkpoint. Para entre skills para validación del consultor. | Ejecutar 6 skills a mano |
| `/revos:design` | Orquesta la fase 2 según tier (Essentials o Complete). | Ejecutar 4–9 skills a mano |
| `/revos:activation` | Orquesta la fase 3 + opcionales contratados. | Ejecutar 4–10 skills a mano |
| `/revos:checkpoint` | Prepara el material del checkpoint de la fase en curso, incluida la sección fija "asunciones vigentes". | diagnostic/design-checkpoint invocadas a mano |
| `/revos:cambio` | Registra un cambio: pregunta qué cambió, clasifica (Cosmético/Dato/Concepto), actualiza backlog, versiona, archiva la versión anterior en `04 Archivo`, y lanza la evaluación de propagación del orquestador. | Nada — hoy es la fuente de errores |
| `/revos:entrega` | Toma el contenido validado y produce el fichero final maquetado según la preferencia de output del proyecto (agente deliverable-designer). | Instrucciones de guardado dispersas en cada skill |
| `/revos:qa` | Lanza el agente system-qa sobre todo lo producido. Obligatorio al cierre de cada fase; parcial bajo demanda tras propagaciones. | Skill system-qa a mano |

Los comandos de fase nunca avanzan al siguiente skill sin confirmación explícita del consultor (principio conservado del Master Doc).

---

## 4. Fase 0 — `/revos:fase-0`

Pasos del comando:

1. Pide o confirma la carpeta del proyecto en Cowork.
2. Crea la estructura:

```
[Cliente]/
  00 Sistema/       → State Log · Backlog de cambios · Estructura del proyecto
  01 Entregables/
  02 Anexos/        → material del cliente, research bruto, transcripciones
  03 QA/            → informes de system-qa
  04 Archivo/       → versiones antiguas (movidas por /revos:cambio, nunca a mano)
```

3. Pregunta y registra: tier contratado, preferencia de output (HTML u Office — D7), idioma del cliente, conectores CRM disponibles.
4. Inicializa `Cliente - State Log v1.md` y `Cliente - Backlog de cambios v1.md`.
5. Devuelve el next best action (normalmente `/revos:diagnostic`).

Naming en todo el proyecto: `Cliente - Entregable v1.ext` (D6). El comando valida que ningún fichero generado lleve guiones bajos.

---

## 5. Gestión de cambios y versiones — `/revos:cambio`

Tabla canónica (de tu esquema):

| Tipo | Definición | Acción | Versión | Backlog |
|---|---|---|---|---|
| **Cosmético** | Nada depende de ello | Editar | Sin cambio | Opcional |
| **Dato** | Algo depende del valor, no del argumento | Editar | Sin cambio | **Obligatorio, con lista de ficheros afectados y estado** |
| **Concepto** | El argumento cambia | **Reescribir** | **v1 → v2** | Obligatorio |

Formato del backlog (una fila por cambio):

| Fecha | Entregable | Tipo | Descripción | Ficheros afectados | Estado |
|---|---|---|---|---|---|
| — | — | Cosmético/Dato/Concepto | — | lista con estado individual: sin impacto / pendiente editar / pendiente reescribir / resuelto | abierto / propagado / cerrado |

Reglas duras:
- Un cambio de Concepto siempre archiva la versión anterior en `04 Archivo` antes de reescribir.
- Ningún checkpoint se celebra con cambios en estado "pendiente" en el backlog.
- La propagación la decide el orquestador y la aprueba el consultor (§2).

---

## 6. Límite de revisiones y régimen de asunciones (D8)

Convención transversal nueva, presente en el frontmatter de comportamiento de todas las skills:

1. Cada dato faltante se clasifica al detectarse: **bloqueante** (impide una decisión del entregable) o **no bloqueante** (afina pero no cambia la decisión).
2. Cada entregable tiene un presupuesto de **2 ciclos de revisión**. Un ciclo = una ronda de correcciones del consultor o del cliente.
3. Agotado el presupuesto: todo [FALTA DATO] no bloqueante se convierte en **[ASUNCIÓN: valor asumido + criterio]**, se registra en el state log y el sistema avanza. Solo los bloqueantes pueden parar el avance, y deben escalarse al cliente de inmediato, no esperar al checkpoint.
4. Los checkpoints incluyen sección fija "Asunciones vigentes" — el cliente valida o corrige. Una asunción corregida entra por `/revos:cambio` como cambio de Dato o de Concepto según afecte.

Etiquetado v4: [FALTA DATO] (transitorio, máx. 2 ciclos) · [ASUNCIÓN] (estable, validable) · [HIPÓTESIS] (inferencia estratégica) · [CONTRADICCIÓN DETECTADA] · [DATO CRM] (procedencia conector, §8).

---

## 7. Output y maquetación (D7)

- La preferencia se fija **una vez por proyecto** en fase 0: **HTML** (entregables interactivos con sistema visual propio) u **Office** (DOCX/XLSX/PPTX según la naturaleza de cada entregable, como dicta el Blueprint). Override puntual permitido por entregable.
- Las skills dejan de dictar formato de guardado; producen **contenido validado en Markdown** dentro de `01 Entregables`. La conversión al formato final la hace `/revos:entrega`.
- **Agente `deliverable-designer`** (la maquetación entra en Design): aplica el sistema visual RevOS — plantilla HTML con identidad del estudio (tipografía, paleta, componentes de funnel/roadmap reutilizables) o plantillas Office equivalentes. Un solo lugar donde vive el diseño; los 20+ entregables heredan.
- Esto resuelve la contradicción v3 (Master Doc decía "Markdown por defecto", Blueprint decía "DOCX por skill").

---

## 8. Conectores CRM en intake (D10)

- `.mcp.json` del plugin declara HubSpot, Salesforce y Pipedrive como conectores **opcionales**. Ninguno es requisito.
- Skills afectadas: `client-intake-form`, `brief-intake`, `revenue-diagnostic` y `martech-stack-audit` ganan un paso condicional: *"Si hay CRM conectado, lanza el agente crm-analyst"*.
- **Agente `crm-analyst`**: extrae en solo lectura volúmenes por etapa, tasas de conversión, ciclo medio, ticket medio, win rate y antigüedad del pipeline. Todo dato extraído se marca **[DATO CRM: fuente, fecha]**.
- Regla de higiene: si el dato del CRM es inconsistente (etapas vacías, fechas imposibles, duplicados masivos), se marca [DATO NO FIABLE] y se trata como [FALTA DATO] — un CRM sucio no es mejor que no tener CRM, y además es input para martech-stack-audit.
- Requisito comercial: incluir en la propuesta al cliente una cláusula de acceso de lectura y confidencialidad.
- ERP: fuera de v4.0. Hueco previsto en el diseño del agente para añadirlo sin reestructurar.

---

## 9. Agentes

| Agente | Modelo | Herramientas | Función |
|---|---|---|---|
| `competitive-researcher` | Sonnet | Web search, fetch | Landscape competitivo multi-fuente con citación. Espejo del market-researcher del gtm-planner. |
| `crm-analyst` | Sonnet | Conectores CRM (lectura) | §8. Extracción con procedencia. |
| `system-qa` | Opus | Read/Grep/Glob (read-only) | Coherencia transversal. Sin permisos de escritura — el informe va a `03 QA` y las correcciones entran por `/revos:cambio`. Espejo del plan-qa del gtm-planner. |
| `deliverable-designer` | Sonnet | Filesystem + skills docx/pptx/xlsx | §7. Maquetación final. |

La asignación Opus/Sonnet por skill de la "Arquitectura Claude" del Blueprint se conserva y se traslada al frontmatter de cada skill.

---

## 10. Cambios transversales en la reescritura de las 26 skills

Aplicar a todas en la misma pasada (por eso una sola reescritura — D11):

1. **Terminología**: checkpoint (no Gate) · cuellos de botella / problemas (no "cuello" a secas) · empresas B2B sin calificativo (D3) · Essentials/Complete (no Core v1/v2) · Activation (no Deployment) · corregir XSLX→XLSX.
2. **Naming**: eliminar todas las instrucciones `[empresa]_x_v1.md` (21 skills) → `Cliente - Entregable v1.ext`.
3. **Formato**: eliminar instrucciones de formato de salida → el contenido va a `01 Entregables` en Markdown; `/revos:entrega` decide el fichero final.
4. **Etiquetado**: añadir régimen de asunciones y límite de 2 revisiones (§6) y [DATO CRM].
5. **Posición en pipeline**: actualizar las referencias "guárdalo y súbelo al Project" (operativa claude.ai v3, obsoleta) → referencias al state log y a comandos.
6. **Skills nuevas**: `client-intake-form` (existía solo en el Blueprint) y `revos-orchestrator` (§2).

Documentos canónicos resultantes (cambio de Concepto → v-bump con backlog, según el propio esquema):
- Master Doc v2 (reescrito: secciones 4-6 cambian por completo; §5 "Projects de claude.ai" desaparece a favor del plugin)
- Blueprint v4 (columnas nuevas: comando responsable, agente asociado, conector)
- Workflow v4 y Timeline v2 (regenerados desde el Blueprint para que no vuelvan a divergir)

---

## 11. Plan de construcción

| Orden | Bloque | Contenido | Dependencia |
|---|---|---|---|
| 1 | Esqueleto | plugin.json, estructura de carpetas, `/revos:fase-0`, `/revos:status` + skill orchestrator con state log | — |
| 2 | Convenciones | `/revos:cambio` + backlog + régimen de asunciones documentado | 1 |
| 3 | Skills fase Diagnostic | 6 skills reescritas + competitive-researcher + crm-analyst | 2 |
| 4 | Skills Design + Activation + opcionales | 20 skills reescritas + system-qa agente | 2 |
| 5 | Entrega | deliverable-designer + plantillas HTML y Office + `/revos:entrega` | 3 |
| 6 | Docs canónicos | Master Doc v2, Blueprint v4, Workflow v4, Timeline v2 | 3–5 |
| 7 | Piloto | Proyecto real (Kokolski) con el plugin completo; los fallos entran como backlog v4.1 | 6 |

Los bloques 3 y 4 son paralelizables. El piloto (7) es el criterio de "canónico": ningún documento v4 se declara definitivo hasta pasar un proyecto real.
