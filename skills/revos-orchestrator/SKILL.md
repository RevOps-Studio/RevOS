---
name: revos-orchestrator
description: Cerebro del sistema RevOS. Usar cuando haya que decidir el siguiente paso de un proyecto RevOS, evaluar el impacto de un cambio en entregables descendentes (propagación), aplicar el régimen de revisiones y asunciones, o mantener el State Log. Lo invocan los skills fase-0, status y cambio; también activar si el consultor pide "qué toca ahora", "evalúa la propagación", "actualiza el state log" o "next best action".
---

# RevOS Orchestrator

Función: mantener la coherencia del sistema RevOS de principio a fin del proyecto. Este skill contiene las reglas; no produce entregables de cliente.

## Fuentes de verdad

1. `references/grafo-dependencias.md` — los 27 nodos del sistema con sus dependencias, fase, tier y modelo recomendado.
2. `references/convenciones.md` — terminología, naming, etiquetado, régimen de revisiones y esquema de versionado.
3. `00 Sistema/[Cliente] - State Log v1.md` en la carpeta del proyecto — el estado real.

Lee siempre el State Log antes de decidir nada. Si no existe, el proyecto no ha pasado por fase 0: indícalo y detente.

## Decidir el siguiente paso (next best action)

1. Lee del State Log: tier contratado, entregables producidos con versión y estado, asunciones vigentes, cambios pendientes en el backlog.
2. Consulta el grafo: identifica los nodos cuyos prerequisitos están completos y validados.
3. Aplica las reglas de bloqueo, en este orden:
   - Cambios del backlog en estado "pendiente" → la next best action es resolverlos, no avanzar.
   - Checkpoint de fase sin celebrar → la next best action es el checkpoint.
   - [FALTA DATO] bloqueante abierto → escalarlo al cliente de inmediato; no esperar al checkpoint.
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
5. Tras la aprobación, actualiza backlog y State Log, y mueve las versiones sustituidas a `04 Archivo`.

## Régimen de revisiones y asunciones

- Cada entregable tiene presupuesto de 2 ciclos de revisión. Registra cada ciclo consumido en el State Log.
- Al agotarse el presupuesto: cada [FALTA DATO] no bloqueante se convierte en [ASUNCIÓN: valor asumido + criterio], se registra en el State Log, y el sistema avanza.
- Solo un [FALTA DATO] bloqueante (impide una decisión del entregable) puede detener el avance.
- Toda asunción corregida por el cliente entra como cambio (Dato o Concepto según afecte) y pasa por la evaluación de propagación.

## Lo que NO hace el orquestador

- No produce contenido de entregables.
- No avanza fases ni propaga cambios sin confirmación del consultor.
- No modifica ficheros de `01 Entregables` — solo State Log, backlog y `04 Archivo`.
