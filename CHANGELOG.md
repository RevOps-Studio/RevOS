# CHANGELOG — plugin revos

Histórico de cambios del plugin y de los documentos canónicos de RevOS. **Ninguna modificación del plugin se considera aplicada hasta que tiene entrada aquí.**

Convención de tipo, la misma que el sistema aplica a los entregables de cliente:
**Cosmético** (nada depende de ello) · **Dato** (algo depende del valor, no del argumento) · **Concepto** (el argumento cambia).

Fuentes únicas, para que no haya duda de dónde se edita qué:

| Materia | Fuente única | Vistas derivadas |
|---|---|---|
| Dependencias entre nodos | `skills/revos-orchestrator/references/grafo-dependencias.md` | Blueprint, hoja "Flujo dependencias" · Timeline · Workflow |
| Convenciones transversales | `skills/revos-orchestrator/references/convenciones.md` | Bloque "Convenciones v4.x" replicado en cada SKILL.md · Master Doc §6 |
| Mapa de conectores | `skills/revos-orchestrator/references/conectores.md` | Blueprint, hoja "Arquitectura plugin" · `.mcp.json` (solo nivel 1) |
| Sistema visual | `skills/entrega/references/sistema-visual.md` | Plantilla HTML · plantillas Office |
| Método de cada nodo | El `SKILL.md` correspondiente | Blueprint, hoja "Matriz RevOS" (columna Propósito) |

---

## [4.2.0] — 12/08/2026

Auditoría de coherencia interna del plugin, cruzando las 34 skills con el grafo, las convenciones y el Blueprint. Ningún hallazgo venía de un proyecto de cliente: todos son de instrumentación.

### Estructural

- **Jerarquía de fuentes declarada.** `grafo-dependencias.md` y la hoja "Flujo dependencias" del Blueprint se declaraban mutuamente como fuente canónica. Circularidad resuelta: **el markdown es la fuente** (es lo que el orquestador lee en ejecución), el Blueprint es vista derivada y se regenera desde él. *Concepto.*
- **CHANGELOG.md creado.** Hasta hoy el plugin no registraba sus propios cambios — un sistema cuyo valor es la trazabilidad de los entregables no la tenía sobre sí mismo. *Concepto.*
- **`RevOS - Blueprint v4.xlsx` → `v5`**, regenerado con las correcciones de dependencias y el bloque de conectores actualizado a dos niveles. *Concepto.*
- **`RevOS v4 - Especificacion del plugin.md` marcado como documento histórico de diseño**, con la lista de los cinco puntos en que ha quedado superado por v4.1. No se corrige: se señaliza. *Cosmético.*

### Navegación (skills-only)

- **Decisión de arquitectura: no se construye `commands/`.** La Especificación planificó nueve comandos y el Blueprint los documenta, pero la carpeta nunca existió: `/revos:diagnostic`, `/revos:design` y `/revos:activation` no existen en ninguna forma, y `checkpoint` y `qa` viven bajo otro nombre. La consecuencia real es que la secuenciación por tier no tenía dónde vivir y se apoyaba en los punteros de cada skill. Se asume el modelo skills-only: la secuencia la calcula el orquestador y los punteros se parametrizan. `status` + grafo cubren lo que iban a cubrir los comandos de fase; construirlos queda como decisión abierta para cuando haya varios proyectos en paralelo. *Concepto.*
- **Punteros parametrizados por tier** en `sales-conversion-design` (Essentials → roadmap · Complete → channel-strategy) y corregido el de `measurement-framework`, que mandaba a Activation saltándose el roadmap y el checkpoint de Design: siguiendo punteros, un Complete cerraba Design sin roadmap ni validación. *Concepto.*
- **`system-qa` insertado en la cadena** de `revenue-diagnostic`, `execution-roadmap-builder`, `martech-measurement` y `reporting-operating-system`. Ningún puntero lo mencionaba, aunque las convenciones lo exigen antes de todo checkpoint desde v4.1. *Concepto.*
- **Opcionales de Activation reconectados**: `martech-measurement` apuntaba directo a `exec-deliverables` y dejaba `reporting-operating-system` fuera de la cadena. *Dato.*
- **`diagnostic-checkpoint`**: puntero de salida parametrizado por fase y tier, y la no-validación del cliente se enruta explícitamente por `cambio`. *Dato.*
- **`martech-stack-audit`**: puntero condicionado a si `crm-selection` está contratado. *Dato.*

### Agentes alineados a v4.2

Los cuatro agentes seguían en vocabulario v4.0, hablando del **State Log** que F7 partió en Registro + Estado hace una versión.

- **`system-qa`**: los chequeos mecánicos de F8 estaban en el `SKILL.md` y no en el agente — y el agente es quien ejecuta. Es la observación del piloto repitiéndose ("los hizo por iniciativa propia, no por instrucción"), aplicada al fichero equivocado. Añadidos como sección obligatoria: recuentos contra contenido real, resúmenes que declaran totales, punteros caducados, supervivencia de contenido archivado, techo de 12 hallazgos y desfase Registro/Estado. Añadida la forma exacta del veredicto que espera el Registro. *Concepto.*
- **`crm-analyst`**: Registro en lugar de State Log; sus hallazgos de higiene se declaran recolección temprana para `martech-stack-audit` cuando se ejecuta en Diagnostic. *Dato.*
- **`competitive-researcher`**: distinción entre fuente web (URL) y dato de conector ([DATO MEDIDO]); su informe se declara recolección. *Dato.*
- **`deliverable-designer`** y **sistema visual**: `[DATO MEDIDO]` era una etiqueta huérfana — existía en convenciones y en el paso 4 de `knowledge-base-builder` desde F5, pero no tenía pill ni la conocía el maquetador. Lo que F5 creó no había llegado a la capa que lo renderiza. *Dato.*
- **`[DATO CRM]`**: admitido el periodo como extensión canónica para agregados temporales, resolviendo la divergencia entre el agente (tres campos) y la convención (dos) sin tocar el bloque replicado en 27 skills. *Dato.*

### Documentación

- **`README.md` reescrito.** Se declaraba en `v4.0.0-alpha.7` con los bloques 6-7 pendientes, cuando los documentos canónicos existen y el piloto se ejecutó. Ahora declara la arquitectura skills-only, el inventario real y la tabla de fuentes únicas. *Dato.*
- **Chuleta de `setup` corregida.** Enseñaba nueve comandos de los que tres no existen y dos tienen otro nombre — en el fichero de onboarding. *Dato.*

### Dependencias del grafo

- **Nodo 19 `crm-blueprint-builder`**: añadidas `measurement-framework` y `martech-stack-audit`, retirada `sales-conversion-design` (llega transitivamente vía `sales-process-design`). El paso 1 de la skill lee los dos documentos que el grafo no declaraba, de modo que el orquestador podía desbloquear el blueprint antes de que existieran y el paso 7 habría diseñado reportes contra un measurement framework inexistente. *Concepto.*
- **Nodo 17 `martech-stack-audit`**: dependencia corregida de `brief-intake` a `Design Essentials del tier · measurement-framework`, con consumo declarado de la recolección temprana. El grafo describía cuándo puede empezar el trabajo; la skill, cuándo puede cerrarse el entregable. *Concepto.*
- **Nodo 15 `design-checkpoint`**: tier corregido de `Complete` a `Essentials / Complete`. Las reglas de secuencia ya decían que Essentials cierra Design con checkpoint. *Dato.*
- **`channel-strategy-design`**: retirada la recomendación de usar el Execution Roadmap como input — el roadmap (nodo 14) depende de este nodo (10). Dependencia circular. *Dato.*

### Concepto nuevo: recolección y captura

- **Apartado nuevo en convenciones**: distinción entre entregable, material de captura y recolección temprana, con su ubicación, versionado, registro y efecto sobre el presupuesto de ciclos.
- **`knowledge-base-builder`**: el paso 4 (medición de activos, F5) incorpora la recolección temprana del stack — inventario, costes, flujos de datos e higiene del CRM. La suciedad del CRM pasa a ser evidencia del diagnóstico en lugar de una nota para cuatro meses más tarde.
- **`martech-stack-audit`**: paso 1 comprueba y consume la recolección si existe, en lugar de volver a pedir al cliente datos ya recogidos.
- **`client-intake-form`**: su output pasa de `01 Entregables` con versión a `02 Anexos` sin versión, como material de captura. Deja de consumir presupuesto de revisión, que es lo que hacía hasta ahora sobre un formulario que solo registra lo que el cliente declara. La fila en la tabla de Ejecución del Registro se conserva para no perder trazabilidad.
- **Plantilla de Estado**: sección nueva "Recolección pendiente". Material en `02 Anexos` que nadie referencia es material que se pierde; se vigila desde el Estado, no desde la memoria del consultor.
*Todo el bloque: Concepto.*

### Resúmenes sin recuentos (extensión de F1)

F1 se aplicó en v4.1 al alcance que fijó el documento de aprendizajes: `brief-intake`, `knowledge-base-builder`, `competitive-research`, `revenue-diagnostic` y `exec-deliverables` — los cinco documentos largos que fallaron en el piloto. Las skills de Complete y opcionales nunca se revisaron porque el piloto solo recorrió Diagnostic, mientras la convención estaba escrita como regla transversal. Ocho skills pedían recuentos que la convención prohíbe y que el chequeo mecánico de `system-qa` marca como hallazgo.

Corregidas: `brand-copy-system`, `content-calendar-builder`, `content-discoverability-design`, `conversion-playbook-builder`, `martech-measurement`, `martech-stack-audit`, `media-plan-builder`, `reporting-operating-system`. *Dato.*

Criterio aplicado, ahora explícito: F1 prohíbe **declarar cuántos elementos contiene el propio documento**, porque el cuerpo sigue cambiando después de escribir el resumen. No prohíbe cifras de negocio calculadas (coste mensual del stack, inversión a 12 meses, carga en horas, TCO, scoring). Por eso `crm-selection` no se tocó.

### Pendiente para 4.3.0

- **Punteros "Siguiente skill" (#1)**: están escritos como si el tier fuera siempre Essentials. `sales-conversion-design` apunta al roadmap (correcto solo en Essentials) y `measurement-framework` apunta a Activation, saltándose el roadmap (14) y el design-checkpoint (15). Siguiendo punteros, un proyecto Complete cierra Design sin roadmap ni validación.
- **Inserción de `/revos:qa` (#2)**: ningún puntero del sistema menciona el QA, aunque las convenciones lo exigen antes de todo checkpoint.
- **Opcionales de Activation (#7)**: `martech-measurement` apunta directo a `exec-deliverables`, dejando `reporting-operating-system` fuera de la cadena.
- Los tres son el mismo mecanismo y se editan de una pieza. Bloqueados hasta revisar `commands/` y `agents/`: la secuenciación por tier vive en `/revos:design`, y arreglar las skills sin leer el comando puede ser cosmético o contraproducente.
- **Decisión abierta**: ¿modo ligero? Para un Essentials pequeño, la maquinaria de gobierno completa (Registro + Estado + Backlog + QA + doble condición) puede pesar más que el entregable. Merece un perfil reducido explícito antes de que se improvise saltándose pasos.

---

## [4.1.0] — 31/07/2026 · registrada retroactivamente

Incorporación de los aprendizajes del primer piloto de Diagnostic (Kokolski, 30-31/07/2026). Evidencia: `docs/RevOS v4 - Aprendizajes del piloto Diagnostic.md`. Cinco skills ejecutadas, un flujo de cambio tramitado, un `system-qa` de cierre con veredicto APTO CON RESERVAS.

- **F1 · Resúmenes sin recuentos.** Los recuentos declarados fallaron en 3 de 3 documentos largos. Aplicado a los cinco documentos del alcance del piloto. *Dato.*
- **F2 · Disposición de huecos al cierre.** Todo `[FALTA DATO]` heredado sale de cada cierre como resuelto, reasignado o declinado. La regla de asignación pasa a "primera skill **no ejecutada** que lo necesita", recalculada en cada cierre. *Concepto.*
- **F3 · Dos contadores de ciclos.** Separación entre revisión de calidad (máximo 2) e incorporación de información (ilimitada). En el piloto, el presupuesto se agotó sin una sola revisión de calidad: el sistema penalizaba exactamente la conducta que quiere fomentar. *Concepto.*
- **F4 · Doble condición de checkpoint.** Backlog limpio **Y** último `system-qa` de la fase en APTO. En el piloto el backlog estaba limpio y los bloqueantes estaban en el informe de QA. *Concepto.*
- **F5 · Medición de activos en `knowledge-base-builder`.** El mejor hallazgo de la fase salió fuera de proceso. Etiqueta nueva `[DATO MEDIDO: herramienta, fecha]`. Los dominios de las cuentas del cliente pasan a ser dato de intake. *Concepto.*
- **F6 · Calibración de la capa económica al inicio de `brief-intake`.** Ahorra un ciclo completo y evita producir un documento que hay que convertir acto seguido. *Concepto.*
- **F7 · Partición del State Log** en `Registro` (inmutable, solo adición) y `Estado` (vistas de trabajo, regeneración completa en cada cierre). Era el fichero menos fiable del sistema y el que monta la agenda del checkpoint. Techo de 12 hallazgos con consolidación obligatoria. *Concepto.*
- **F8 · Chequeos mecánicos obligatorios en `system-qa`**: recuentos contra contenido real, punteros caducados, supervivencia de contenido archivado, asunciones corregidas que siguen operando, coherencia interna del Estado. *Dato.*
- **F9 · Validación de la especificación de artefactos antes de `/revos:entrega`**: estados declarados = estados usados, etiquetas = nombres de las secciones referenciadas, todo elemento marcado con entrada en la leyenda. *Dato.*
- **F10-lite · Precondición de producción — decisión de producto no registrada en su momento.** El documento de aprendizajes dejó F10 en "coste alto, contrario a la agilidad buscada, a evaluar para v5". La v4.1 lo implementó como precondición obligatoria en todas las skills de producción: leer el Registro y detenerse si falta fase 0, si el presupuesto está agotado sin cambio tramitado, o si el QA de la fase anterior no está APTO. **El sistema pasó de registrar a bloquear**, que es el cambio de comportamiento más consecuente de la v4, y no quedó constancia de cuándo ni por qué se decidió. Se registra aquí retroactivamente. *Concepto.*
- Etiquetas nuevas: `[DATO MEDIDO]`. Criterio falsable obligatorio en toda `[ASUNCIÓN]`.

## [4.0.0] — 30/07/2026 · registrada retroactivamente

Reescritura única de las skills y migración de operativa de Projects de claude.ai al plugin en Cowork. Decisiones D1-D11 en `docs/RevOS v4 - Especificacion del plugin.md`.

- Arquitectura de plugin único con comandos por fase, orquestador, cuatro agentes y conectores MCP.
- `fase-0` obligatoria con estructura estándar de cinco carpetas.
- `/revos:cambio` como puerta única de correcciones, con clasificación Cosmético/Dato/Concepto, archivado en `04 Archivo` y evaluación de propagación aprobada por el consultor.
- Separación entre contenido validado en Markdown y fichero final vía `/revos:entrega`.
- Naming `[Cliente] - [Entregable] v[N].[ext]`, sin guiones bajos.
- Terminología: checkpoint (no Gate), cuellos de botella, empresas B2B sin calificativo, Essentials/Complete, Activation.
- Skills nuevas: `client-intake-form`, `revos-orchestrator`.
- Documentos canónicos resultantes: Master Doc v2, Blueprint v4, Workflow v4, Timeline v2.
