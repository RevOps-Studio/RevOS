---
name: revos-orchestrator
description: Cerebro del sistema RevOS. Usar cuando haya que decidir el siguiente paso de un proyecto RevOS, evaluar el impacto de un cambio en entregables descendentes (propagación), aplicar el régimen de revisiones y asunciones, o mantener Registro y Estado. Lo invocan los skills fase-0, status y cambio; también activar si el consultor pide "qué toca ahora", "evalúa la propagación", "actualiza el registro" o "next best action".
---

# RevOS Orchestrator

Función: mantener la coherencia del sistema RevOS de principio a fin del proyecto. Este skill contiene las reglas; no produce entregables de cliente.

## Fuentes de verdad

1. `references/grafo-dependencias.md` — los 27 nodos del sistema con sus dependencias, fase, tier y modelo recomendado.
2. `references/convenciones.md` — terminología, naming, etiquetado, régimen de revisiones y esquema de versionado.
3. `00 Sistema/[Cliente] - Registro v[N].md` — histórico inmutable (solo adición) y `[Cliente] - Estado v[N].md` — vistas de trabajo que este orquestador regenera completas en cada cierre de skill.

Lee siempre el Registro antes de decidir nada. Si no existe, el proyecto no ha pasado por fase 0: indícalo y detente. El Estado nunca se edita por adición: se regenera desde el Registro y el cierre recién producido.

## Decidir el siguiente paso (next best action)

1. Lee del Registro: tier contratado, entregables producidos con versión, contadores de ciclos, asunciones vigentes, veredictos de QA; y del Backlog: cambios pendientes.
2. Consulta el grafo: identifica los nodos cuyos prerequisitos están completos y validados.
3. Aplica las reglas de bloqueo, en este orden:
   - Cambios de **Concepto** en estado "pendiente" → la next best action es resolverlos. Los **Dato** en "pendiente de evaluar" no bloquean: su propagación se evalúa en lote en el siguiente cierre de skill o antes del checkpoint, lo que llegue antes (v4.3).
   - Doble condición de checkpoint (F4): backlog sin cambios abiertos Y último system-qa de la fase con veredicto APTO (o críticos/mayores de bloqueo tramitados). Sin QA ejecutado no hay checkpoint; si falta, la next best action es /revos:qa.
   - Checkpoint de fase sin celebrar → la next best action es el checkpoint.
   - [FALTA DATO] bloqueante abierto (definición cerrada de la Doctrina de avance: inversión de tesis · irreversibilidad · imposibilidad material) → escalarlo agrupado con los demás bloqueantes al cierre del paso en curso; no esperar al checkpoint, pero tampoco interrumpir la producción uno a uno.
4. Devuelve: skill siguiente + inputs que requiere + huecos conocidos que arrastrará.
5. Nunca ejecutes el skill siguiente sin confirmación explícita del consultor.

## Evaluar propagación de un cambio

Cuando un entregable ya producido cambia:

1. Clasifica el cambio según la tabla de versionado de `references/convenciones.md` (Cosmético / Dato / Concepto).
2. Consulta el grafo y lista todos los entregables descendentes del nodo modificado.
3. Evalúa cada descendiente con una sola pregunta: ¿el cambio afecta a algo que este documento usó como input de una decisión?
   - No → márcalo "sin impacto" en el backlog. No se toca.
   - Sí, afecta a datos pero no al argumento → márcalo "pendiente de editar".
   - Sí, afecta al argumento → márcalo "pendiente de reescribir" (v-bump en cascada) y recomienda system-qa parcial antes de continuar la fase.
4. Presenta el plan de propagación completo al consultor (tabla: fichero → impacto → acción propuesta). No propagues nada sin su aprobación.
5. Tras la aprobación, actualiza backlog, añade al Registro y mueve las versiones sustituidas a `04 Archivo`.

## Cierre de skill — regeneración del Estado

En cada cierre de skill de producción:

1. **Añade al Registro** la fila de ejecución (entregable, versión, ciclos por contador, fecha).
2. **Lote de propagación (v4.3)**: si el backlog tiene cambios de Dato en "pendiente de evaluar", evalúa su propagación en una sola pasada (procedimiento de propagación de este skill) y presenta el plan conjunto al consultor. Nada se propaga sin su aprobación.
3. **Disposición de huecos (F2)**: verifica que cada [FALTA DATO] que el Estado asignaba a la skill cerrada sale con disposición explícita — resuelto (con el dato), reasignado o declinado (con motivo). La regla de asignación es "primera skill NO ejecutada que lo necesita", recalculada en este momento para todos los huecos vivos. Un puntero hacia una skill ya ejecutada es un defecto.
4. **Regenera el Estado completo**: huecos vivos con destinataria vigente, hallazgos (techo 12 — si se supera, consolida antes de añadir), lote de Dato pendiente de evaluar si queda alguno, agenda del próximo checkpoint (asunciones vigentes + bloqueantes + estado de la doble condición), siguiente paso.
5. El Estado anterior no se archiva (es una vista); el Registro nunca pierde filas.

## Régimen de revisiones y asunciones

- Dos contadores por entregable: **calidad** (máximo 2 — cambios nacidos del juicio sobre lo escrito) e **incorporaciones de información** (ilimitadas — datos nuevos aportados o medidos; no consumen presupuesto). El origen lo clasifica /revos:cambio. Registra ambos en el Registro.
- La conversión a [ASUNCIÓN] opera desde la primera pasada (Doctrina de avance, convenciones v4.3): si la fuente del dato no estará disponible antes del checkpoint, se asume directamente con criterio falsable. Al agotarse el presupuesto, los [FALTA DATO] no bloqueantes restantes se convierten igualmente en [ASUNCIÓN], se registran en el Registro, y el sistema avanza.
- Solo un [FALTA DATO] bloqueante según la definición cerrada de la Doctrina de avance puede detener el avance: no bloqueante por defecto, carga de la prueba en el bloqueo, máximo 3 preguntas abiertas al consultor por entregable, escalado agrupado al cierre del paso.
- Toda asunción corregida por el cliente entra como cambio (Dato o Concepto según afecte) y pasa por la evaluación de propagación.

## Lo que NO hace el orquestador

- No produce contenido de entregables.
- No avanza fases ni propaga cambios sin confirmación del consultor.
- No modifica ficheros de `01 Entregables` — solo Registro (adición), Estado (regeneración completa), backlog y `04 Archivo`.
