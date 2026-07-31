---
name: status
description: Estado del proyecto RevOS y next best action. Punto de entrada de cada sesión de trabajo sobre un proyecto en curso. Usar cuando el consultor pregunte "por dónde vamos", "estado del proyecto", "qué toca ahora", "next best action" o al retomar un proyecto tras días sin actividad.
---

# Status — estado y siguiente paso

Devuelve una foto fiel del proyecto y la next best action. Solo lectura: este skill no modifica nada.

## Proceso

### 1. Localizar el estado
Lee `00 Sistema/[Cliente] - Registro v[N].md` (histórico inmutable), `[Cliente] - Estado v[N].md` (vistas de trabajo) y `[Cliente] - Backlog de cambios v[N].md`. Si no existen, el proyecto no ha pasado por fase 0: indícalo y ofrece ejecutar `fase-0`. No inventes estado. Si el Estado está desactualizado respecto al Registro (skills cerradas después de su última regeneración), señálalo: debe regenerarlo el orquestador antes de fiarse de sus vistas.

### 2. Contrastar con el grafo
Carga `skills/revos-orchestrator/references/grafo-dependencias.md` (desde la raíz del plugin) y aplica las reglas del orquestador (`skills/revos-orchestrator/SKILL.md`): nodos completados vs. nodos desbloqueados según el tier contratado.

### 3. Detectar bloqueos (en este orden de prioridad)
1. Cambios del backlog en estado "pendiente" → bloquean el avance.
2. Doble condición de checkpoint: backlog sin cambios abiertos Y último system-qa de la fase en veredicto APTO (consulta la tabla de veredictos del Registro). Sin QA ejecutado, no hay checkpoint.
3. Checkpoint de fase sin celebrar → bloquea la fase siguiente.
4. [FALTA DATO] bloqueantes abiertos → escalar al cliente de inmediato.
5. Entregables que agotaron sus 2 ciclos de revisión de calidad con [FALTA DATO] sin convertir a [ASUNCIÓN] → señalar la conversión pendiente. (Las incorporaciones de información no consumen ciclo.)
6. Huecos vivos del Estado con destinataria ya ejecutada → reasignación pendiente del orquestador.

### 4. Informe
Presenta, en este orden y sin relleno:
- **Proyecto**: cliente, tier, output elegido, conectores.
- **Fase actual** y entregables producidos (con versión y ciclos consumidos por contador (calidad / incorporaciones)).
- **Asunciones vigentes** (las pendientes de validar en el próximo checkpoint).
- **Cambios pendientes** de propagar, si los hay.
- **Next best action**: skill siguiente + inputs que requiere + huecos que arrastrará.

### 5. Cierre
Ofrece ejecutar la next best action. No la ejecutes sin confirmación explícita del consultor.

## Lo que NO hacer
- No modificar Registro, Estado ni backlog (eso es del orquestador y del flujo de cambios).
- No proponer saltarse un checkpoint o un bloqueo del backlog para "ir más rápido".
