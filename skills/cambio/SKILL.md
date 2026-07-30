---
name: cambio
description: Puerta de entrada única de correcciones y cambios en un proyecto RevOS en curso. Registra el cambio, lo clasifica (Cosmético/Dato/Concepto), versiona, archiva la versión anterior y lanza la evaluación de propagación del orquestador. Usar cuando el consultor o el cliente pidan corregir, ajustar, actualizar o reescribir cualquier entregable ya producido; también si el consultor dice "registra un cambio", "el cliente ha corregido X" o "hay que actualizar el dato Y".
---

# Cambio — gestión de cambios y versiones

Regla de oro: **ningún entregable ya producido se modifica fuera de este flujo.** Si el consultor pide editar directamente un fichero de `01 Entregables` que ya está en el State Log, ejecuta este skill primero. Es la pieza que evita las incoherencias y alucinaciones que generaban las idas y vueltas de Diagnostic y Design.

## Proceso

### 1. Capturar el cambio
Pregunta (o extrae de la petición) en una sola interacción:
- ¿Qué entregable cambia y qué versión está vigente? (verifícalo en el State Log)
- ¿Qué cambia exactamente? (el texto/valor/argumento concreto)
- ¿Origen del cambio? (corrección del cliente · corrección del consultor · asunción corregida en checkpoint · hallazgo de system-qa)

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
fecha · entregable origen · tipo · descripción · ficheros afectados (se completa en el paso 4) · estado global "abierto".
Cosmético: el registro es opcional — regístralo solo si el consultor lo pide o si afecta a un entregable ya entregado al cliente.

### 4. Evaluar propagación (Dato y Concepto)
Invoca el procedimiento de propagación del orquestador (`skills/revos-orchestrator/SKILL.md`):
1. Lista los descendientes del entregable según el grafo.
2. Evalúa impacto por descendiente: sin impacto · pendiente de editar · pendiente de reescribir.
3. Presenta el plan de propagación en tabla al consultor y **espera su aprobación**. Nada se propaga sin ella.
4. Registra el plan aprobado en la columna "ficheros afectados" del backlog, con el estado de cada fichero.

### 5. Ejecutar el cambio
- **Cosmético / Dato**: edita el entregable vigente. La versión no cambia.
- **Concepto**: copia la versión vigente a `04 Archivo` **antes** de tocar nada; después reescribe como v[N+1] en `01 Entregables`. El naming sigue `[Cliente] - [Entregable] v[N+1].[ext]`.
- Ejecuta las propagaciones aprobadas en orden de dependencia (upstream antes que downstream). Cada descendiente reescrito por cascada sigue la misma regla de archivado.

### 6. Cerrar
- Actualiza el State Log: versiones nuevas, ciclos de revisión consumidos (+1 al entregable origen si el cambio nació de una revisión), asunciones afectadas.
- Marca los ficheros del backlog como "resuelto" y el estado global como "cerrado" (o "propagado" si quedan descendientes pendientes para otra sesión).
- Si hubo cascada de Concepto sobre 2+ entregables, recomienda `system-qa` parcial antes de continuar la fase.
- Recuerda si aplica: ningún checkpoint se celebra con cambios en estado "pendiente".

## Interacción con el régimen de revisiones
- Un cambio originado en revisión de cliente o consultor consume 1 de los 2 ciclos del entregable origen. Regístralo.
- Si el entregable ya consumió sus 2 ciclos, el cambio solo procede si es bloqueante o viene de un checkpoint; si no, anótalo en el backlog como "diferido a próximo checkpoint" y no lo ejecutes.
- Una [ASUNCIÓN] corregida por el cliente entra siempre por este flujo (como Dato o Concepto según afecte) y no consume ciclo de revisión.

## Lo que NO hacer
- No editar entregables sin clasificar el cambio primero.
- No propagar sin aprobación explícita del consultor.
- No borrar versiones antiguas: siempre a `04 Archivo`.
- No usar este flujo para producir entregables nuevos (eso es de las fases).
