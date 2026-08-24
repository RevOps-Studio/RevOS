---
name: cambio
description: Puerta de entrada única de correcciones y cambios en un proyecto RevOS en curso. Registra el cambio, lo clasifica (Cosmético/Dato/Concepto), versiona, archiva la versión anterior y lanza la evaluación de propagación del orquestador. Usar cuando el consultor o el cliente pidan corregir, ajustar, actualizar o reescribir cualquier entregable ya producido; también si el consultor dice "registra un cambio", "el cliente ha corregido X" o "hay que actualizar el dato Y".
---

# Cambio — gestión de cambios y versiones

Regla de oro: **ningún entregable ya producido se modifica fuera de este flujo.** Si el consultor pide editar directamente un fichero de `01 Entregables` que ya está en el Registro, ejecuta este skill primero. Es la pieza que evita las incoherencias y alucinaciones que generaban las idas y vueltas de Diagnostic y Design.

## Proceso

### 1. Capturar el cambio
Pregunta (o extrae de la petición) en una sola interacción:
- ¿Qué entregable cambia y qué versión está vigente? (verifícalo en el Registro)
- ¿Qué cambia exactamente? (el texto/valor/argumento concreto)
- ¿Origen del cambio? (corrección del cliente · corrección del consultor · asunción corregida en checkpoint · hallazgo de system-qa · dato nuevo aportado o medido)
- **Clasifica el origen para el contador (F3)**: ¿el cambio nace de *información nueva* (dato aportado por cliente/consultor o medido por el sistema) o de *juicio sobre lo escrito* (reescribir, reordenar, afinar, corregir criterio)? Información nueva → no consume ciclo de revisión. Juicio → consume. Si mezcla ambos, domina el juicio.

### 2. Clasificar
Aplica la tabla de versionado de `skills/revos-orchestrator/references/convenciones.md`:

| Pregunta de clasificación | Sí → |
|---|---|
| ¿Algún otro documento depende del **argumento** que cambia? ¿Cambia una conclusión, prioridad o decisión? | **Concepto** |
| ¿Algún documento depende del **valor** (cifra, nombre, fecha, dato) pero el argumento se sostiene? | **Dato** |
| ¿No depende nada de ello (estilo, redacción, formato)? | **Cosmético** |

En caso de duda entre Dato y Concepto, pregunta: ¿si este valor hubiera sido el correcto desde el principio, el documento habría llegado a la misma conclusión? Sí → Dato. No → Concepto.

Presenta la clasificación al consultor con su justificación en una frase. Él confirma o corrige.

### 3. Registrar en el backlog
Añade la fila a `00 Sistema/[Cliente] - Backlog de cambios v[N].md`:
fecha · entregable origen · tipo · descripción · ficheros afectados (se completa en el paso 4 o en el lote) · estado global: "abierto" (Concepto) o "pendiente de evaluar" (Dato — v4.3).
Cosmético: el registro es opcional — regístralo solo si el consultor lo pide o si afecta a un entregable ya entregado al cliente.

### 4. Evaluar propagación (Concepto: inmediata · Dato: en lote — v4.3)
**Concepto** — evaluación inmediata. Invoca el procedimiento de propagación del orquestador (`skills/revos-orchestrator/SKILL.md`):
1. Lista los descendientes del entregable según el grafo.
2. Evalúa impacto por descendiente: sin impacto · pendiente de editar · pendiente de reescribir.
3. Presenta el plan de propagación en tabla al consultor y **espera su aprobación**. Nada se propaga sin ella.
4. Registra el plan aprobado en la columna "ficheros afectados" del backlog, con el estado de cada fichero.

**Dato** — evaluación diferida en lote. El cambio se ejecuta en el entregable origen (paso 5) y entra al backlog como "pendiente de evaluar". Su propagación se evalúa en lote — todos los Dato acumulados en una sola pasada — en el siguiente cierre de skill o antes del checkpoint, lo que llegue antes; el lote lo ejecuta el orquestador con el mismo procedimiento y la misma aprobación del consultor. La incoherencia transitoria entre origen y descendientes es un coste aceptado: la caza el lote y, en última instancia, el chequeo de coherencia de datos de system-qa. Si el consultor pide evaluar un Dato ahora, se evalúa ahora.

### 5. Ejecutar el cambio
- **Cosmético / Dato**: edita el entregable vigente. La versión no cambia.
- **Concepto**: copia la versión vigente a `04 Archivo` **antes** de tocar nada; después reescribe como v[N+1] en `01 Entregables`. El naming sigue `[Cliente] - [Entregable] v[N+1].[ext]`.
- Ejecuta las propagaciones aprobadas en orden de dependencia (upstream antes que downstream). Cada descendiente reescrito por cascada sigue la misma regla de archivado.

### 6. Cerrar
- Añade al Registro: versiones nuevas, ciclo consumido en el contador que corresponda según el origen clasificado, asunciones afectadas. El orquestador regenera el Estado.
- Marca los ficheros del backlog como "resuelto" y el estado global como "cerrado" (o "propagado" si quedan descendientes pendientes para otra sesión). Un Dato diferido conserva "pendiente de evaluar" hasta que el lote del próximo cierre de skill o pre-checkpoint evalúe su propagación — solo entonces se cierra.
- Si hubo cascada de Concepto sobre 2+ entregables, recomienda `system-qa` parcial antes de continuar la fase.
- Recuerda si aplica: ningún checkpoint se celebra con cambios en estado "pendiente" ni con el lote de Dato sin evaluar. Entre cierres, un Dato "pendiente de evaluar" no bloquea la next best action (v4.3).

## Interacción con el régimen de revisiones (dos contadores)
- Un cambio de origen *juicio* consume 1 de los 2 ciclos de calidad del entregable origen. Regístralo en el contador de calidad del Registro.
- Un cambio de origen *información nueva* no consume ciclo: se registra en el contador de incorporaciones, genera versión si toca y entra al Backlog. Ilimitadas — aportar datos nunca se penaliza.
- Si el entregable ya consumió sus 2 ciclos de calidad, un cambio de juicio solo procede si es bloqueante o viene de un checkpoint; si no, anótalo en el backlog como "diferido a próximo checkpoint" y no lo ejecutes. Las incorporaciones de información proceden siempre.
- Una [ASUNCIÓN] corregida por el cliente entra siempre por este flujo (como Dato o Concepto según afecte) y no consume ciclo de revisión.

## Lo que NO hacer
- No editar entregables sin clasificar el cambio primero.
- No propagar sin aprobación explícita del consultor.
- No borrar versiones antiguas: siempre a `04 Archivo`.
- No usar este flujo para producir entregables nuevos (eso es de las fases).
