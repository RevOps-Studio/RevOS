# RevOS v4 — Aprendizajes del primer piloto de Diagnostic
*Backlog de mejora para v5 · 31 de julio de 2026 · Documento interno de producto*

**Base de evidencia:** ejecución completa de la fase Diagnostic de Kokolski el 30-31/07/2026. Cinco skills ejecutadas (`fase-0`, `brief-intake`, `knowledge-base-builder`, `competitive-research`, `revenue-diagnostic`), un flujo de cambio tramitado, un `system-qa` de cierre de fase con veredicto APTO CON RESERVAS (1 crítico, 9 mayores, 18 menores), dos agentes de research en paralelo y ~2.290 unidades de Ahrefs consumidas.

**Nota de ubicación:** este fichero vive en la raíz de la carpeta del proyecto y no dentro de las cinco carpetas de fase 0, porque no es un entregable de Kokolski. Conviene moverlo a la carpeta de producto de RevOps Studio.

---

## 1. Veredicto contra los cuatro objetivos de la v4

| Objetivo | Resultado | Lectura |
|---|---|---|
| **Reducir inconsistencias** | Mejor, con una regresión | `/revos:cambio` y `system-qa` cazan las incoherencias descendentes, que era el fallo nº1 de la v3. Pero la v4 **genera una clase nueva**: los recuentos numéricos obligatorios en los resúmenes fallaron en 3 de 3 documentos largos |
| **Reducir faltan datos** | Claramente mejor | 16 pendientes al inicio, la fase cierra con **un solo bloqueante vivo**. El régimen de asunciones es el mayor acierto del rediseño |
| **Flexibilidad y agilidad** | Mejor en huecos, rígido en el sitio equivocado | El presupuesto de 2 ciclos es lo único inflexible del sistema y está aplicado a la dimensión que no toca |
| **Eficiencia** | Mejor en delegación, con retrabajo evitable | Cuatro entregables y un QA en una sesión. Pero las tablas de asunciones se reescribieron tres veces por aplicar el régimen después de escribir, no al escribir |

**Conclusión global:** la v4 resuelve el problema que se propuso resolver. Los defectos detectados son de **instrumentación del método**, no de diseño del método. Ninguno exige repensar el sistema; todos son arreglos localizados.

---

## 2. Aciertos que hay que conservar

Se listan primero para que una refactorización de v5 no los rompa por accidente.

**El campo de *criterio* en las asunciones es lo que las hace funcionar.** A8 se falsó en una hora precisamente porque estaba escrita de forma falsable. Una asunción refutada rápido no es un fallo: es el sistema operando. Si en v5 se simplifica la plantilla de asunciones, el criterio es lo último que puede desaparecer.

**`/revos:cambio` demostró su razón de ser en el único caso real que hubo.** La corrección de A8 retiraba una conclusión cuantitativa —contribución mediana del 69 %, una cuenta en pérdida— y el QA verificó que solo sobrevive en `04 Archivo`. Sin ese flujo, esa conclusión se habría filtrado a los tres entregables posteriores.

**El `system-qa` de cierre de fase se pagó solo en el primer run.** Encontró un hallazgo crítico que el operador había creado y no podía ver. La delegación en agente independiente —no autorrevisión— es parte del acierto y conviene hacerla obligatoria, no recomendada.

**La separación entre contenido validado en Markdown y fichero final vía `/revos:entrega`.** Evitó maquetar un artefacto cuya especificación era internamente incoherente. Estuvimos a una instrucción de hacerlo.

**La delegación en agentes de research.** Dos investigadores en paralelo, ~305k tokens con fuentes citadas, sin consumir el hilo principal.

---

## 3. Arreglos priorizados

| ID | Arreglo | Coste | Retorno | Evidencia del piloto |
|---|---|---|---|---|
| **F1** | Quitar los recuentos numéricos de las plantillas de resumen | Muy bajo | Muy alto | Falló en 3 de 3 documentos largos |
| **F2** | Paso de disposición de huecos al cierre de cada skill | Muy bajo | Alto | 6 elementos huérfanos o con destinatario caducado (M8) |
| **F3** | Separar el contador de revisión del de incorporación de información | Bajo | Alto | Presupuesto agotado sin una sola revisión de calidad |
| **F4** | El gating del checkpoint debe referenciar el veredicto del QA | Muy bajo | Alto | Backlog limpio y bloqueantes en el QA |
| **F5** | Paso de medición de activos en `knowledge-base-builder` | Medio | Muy alto | Produjo el mejor hallazgo de toda la fase, fuera de proceso |
| **F6** | Calibrar la tratabilidad de la capa económica al inicio de `brief-intake` | Medio | Alto | Tres reescrituras de la tabla de asunciones |
| **F7** | Partir el State Log en registro y vistas de trabajo | Medio-alto | Alto | Es el fichero menos fiable del proyecto y el que monta el checkpoint |
| **F8** | Chequeos mecánicos explícitos en el checklist de `system-qa` | Bajo | Medio | El agente los hizo por iniciativa propia, no por instrucción |
| **F9** | Validación de la especificación de artefactos antes de `/revos:entrega` | Bajo | Medio | §9 del diagnóstico no estaba lista (m11) |
| **F10** | Evaluar forzado real de precondiciones | Alto | A decidir | El operador estuvo a punto de saltarse la disciplina dos veces |

---

## 4. Detalle de los arreglos

### F1 · Quitar los recuentos numéricos de las plantillas de resumen

**Problema.** Cada entregable largo debe declarar en su "Resumen para el consultor" cuántos [FALTA DATO], [HIPÓTESIS] y [CONTRADICCIÓN DETECTADA] contiene. Esos números se escriben una vez y el cuerpo del documento sigue cambiando después. **El sistema pide una cifra que no permite calcular.**

**Evidencia.** En la Knowledge Base: 13 hipótesis reales, declaradas como 9 en una sección y como 11 en otra. 18 observaciones declaradas como 20. "Tres hechos nuevos" que eran cuatro. En el Brief: "cinco asunciones" con ocho tabuladas, y un reparto de "8 + 8" de los dieciséis pendientes cuando el reparto real era 9 + 5 + 2. Falló en los tres documentos largos.

**Por qué importa más de lo que parece.** No cambian ninguna conclusión, pero son exactamente los números que un fundador con criterio técnico comprueba mientras lees el documento delante de él. El coste no es analítico, es de credibilidad — en un sistema cuyo valor es el rigor.

**Arreglo.** En las plantillas de `brief-intake`, `knowledge-base-builder`, `competitive-research`, `revenue-diagnostic` y `exec-deliverables`, sustituir *"Número de [FALTA DATO] encontrados (bloqueantes y no bloqueantes)"* por *"Los [FALTA DATO] bloqueantes, listados. Los no bloqueantes, sin recuento."* Mismo tratamiento para hipótesis y contradicciones: **enumerar lo que importa, no contar el total.** El recuento, si se quiere, pasa a ser un paso mecánico de `system-qa`, que sí lee el documento terminado.

### F2 · Paso de disposición de huecos al cierre de cada skill

**Problema.** Los huecos se asignan a "la primera skill que lo necesita", pero ninguna skill tiene la obligación de cerrar los que hereda. Cuando esa skill se ejecuta y no lo resuelve, el puntero se queda apuntando a una skill cerrada.

**Evidencia.** `competitive-research` tenía asignados la identificación del decisor real y los dominios de las cuentas. Se ejecutó y no resolvió ninguno: uno por decisión expresa de alcance del consultor, otro en silencio. El State Log quedó con tres punteros hacia skills ya ejecutadas y seis elementos vivos sin destinatario.

**Arreglo.** Añadir a la sección "Entrega" de cada SKILL.md de producción:

> Antes de cerrar, revisa los [FALTA DATO] que el State Log asignaba a esta skill. Cada uno sale con una disposición explícita: **resuelto** (con el dato), **reasignado** (a la primera skill *no ejecutada* que lo necesita) o **declinado** (con motivo). Un hueco heredado no puede quedar sin disposición.

Y en `revos-orchestrator`: la regla de asignación pasa de "primera skill que lo necesita" a **"primera skill no ejecutada que lo necesita"**, recalculada en cada cierre.

### F3 · Separar el contador de revisión del de incorporación de información

**Problema.** El presupuesto de 2 ciclos cuenta **intervenciones**, no **información**. Cualquier toque al entregable consume ciclo, con independencia de su naturaleza.

**Evidencia.** Los dos ciclos de `brief-intake` se consumieron en: (1) una **decisión de método** del consultor —convertir la capa económica en asunciones funcionales—, y (2) la **incorporación de ocho datos nuevos** que el consultor aportó. Ninguno fue una revisión de calidad del entregable. El presupuesto se agotó antes de la primera revisión real, y una corrección legítima posterior tuvo que quemar una versión completa vía `/revos:cambio`.

**El efecto perverso, dicho claro:** el sistema penalizó exactamente la conducta que quiere fomentar, que es que el consultor aporte más datos. Un consultor que aprenda la regla aportará los datos más tarde y peor.

**Arreglo.** Dos contadores en las convenciones:

- **Ciclos de revisión de calidad: 2.** Se consumen solo cuando el cambio nace del juicio del operador sobre el entregable — reescribir, reordenar, afinar, corregir criterio. Agotados, los no bloqueantes pasan a [ASUNCIÓN] y el sistema avanza. Igual que hoy.
- **Incorporaciones de información: ilimitadas.** Datos nuevos aportados por el cliente o el consultor, o medidos por el sistema. No consumen presupuesto. Generan versión y entrada en el Backlog si el entregable ya estaba registrado.

Actualizar el bloque de "Convenciones v4" que aparece replicado en todas las skills, y `references/convenciones.md`.

### F4 · El gating del checkpoint debe referenciar el veredicto del QA

**Problema.** La regla vigente es que un checkpoint no se celebra con cambios pendientes en el backlog. En este piloto el backlog estaba **limpio** —un cambio, propagado y cerrado— y los bloqueantes del checkpoint estaban en el informe de QA.

**Arreglo.** En `diagnostic-checkpoint` y en `revos-orchestrator`, la precondición pasa a ser doble: **backlog sin cambios abiertos Y último `system-qa` de la fase con veredicto APTO** (o con sus críticos y mayores de bloqueo ya tramitados). Sin QA ejecutado, no hay checkpoint.

### F5 · Paso de medición de activos en `knowledge-base-builder`

**Problema — y es el hueco de método más importante que ha salido.** Ninguna skill pregunta si el cliente tiene datos medibles que nadie ha mirado. `brief-intake` y `knowledge-base-builder` dicen "enriquece con los materiales disponibles", pero materiales significa decks, web, notas y transcripciones. **Ninguna dice: mide con los conectores que ya tienes.**

**Evidencia.** El hallazgo más valioso de toda la fase salió fuera de proceso. Medir `kokolski.com` reveló 355 dominios de referencia de spam que no constaban en ninguna fuente del cliente. Medir dos dominios de clientes que el consultor pasó casi de pasada reveló que **CREA había crecido un +243 % con 86 citaciones en motores generativos** — lo que reencuadró el problema de credibilidad de *veracidad* a *documentación*, y convirtió la afirmación de la web de un riesgo en un activo pendiente de documentar. En el mismo movimiento apareció el mayor riesgo de cartera no vigilado: Dini, 1.800 €/mes, −58 %.

**Nada de eso estaba en el proceso.** Es la diferencia entre un diagnóstico construido sobre lo que el cliente cuenta y uno construido sobre lo que es medible por terceros.

**Arreglo.** Nuevo paso en el proceso de `knowledge-base-builder`, antes de redactar:

> **Paso — Medición de activos.** Con los conectores activos del proyecto, mide el dominio del cliente y, si están disponibles, los dominios de sus clientes y de sus competidores directos. Como mínimo: autoridad, keywords, tráfico orgánico, histórico de 12-18 meses, perfil de enlaces y citaciones en motores generativos. Contrasta cada cifra medida con lo que el cliente declara. Toda divergencia entre lo declarado y lo medido es material de la sección de observaciones.

Y en `brief-intake`, en la lista de inputs: **pedir los dominios de las cuentas del cliente como dato de intake**, al mismo nivel que la web propia. En este piloto llegaron por casualidad en la cuarta interacción.

**Nota de coste.** El run completo consumió ~2.290 unidades de Ahrefs de un plan Lite de 100.000/mes. La medición no es el cuello de botella económico: pedir los dominios sí lo es.

### F6 · Calibrar la tratabilidad de la capa económica al inicio de `brief-intake`

**Problema.** El régimen de asunciones se aplicó **después** de producir un brief con dieciséis huecos, en lugar de al producirlo. Eso obligó a reescribir la tabla de asunciones tres veces: en el ciclo 1, en el ciclo 2 y en la corrección de A8.

**Arreglo.** Añadir al Paso 1 de `brief-intake` una pregunta de calibración explícita al consultor, antes de escribir:

> ¿La gestión financiera de este cliente es lo bastante formal para producir cifras fiables si se piden? Si la respuesta es no, la capa económica se escribe directamente con asunciones funcionales y no con [FALTA DATO], y se declara el criterio en el propio brief.

Ahorra un ciclo completo y evita producir un documento que hay que convertir acto seguido.

### F7 · Partir el State Log en registro y vistas de trabajo

**Problema.** El State Log hace siete trabajos a la vez: configuración de proyecto, registro de ejecución, censo de asunciones, tracker de huecos con punteros, repositorio de hallazgos estructurales, fuente de la agenda del checkpoint y puntero de siguiente paso. **Todo se acumula por adición y nada es una vista calculada.**

**Evidencia.** Es donde el QA encontró sus peores defectos. Dos hallazgos que se contradicen entre sí sobre si existe activo de prueba. Una tabla que dice "quedan tres" con nueve filas y una duplicada con estados opuestos. Tres punteros caducados. Una lista de hallazgos que llegó a 23 elementos numerados a mano. Y una instrucción que, seguida al pie de la letra, mandaba al cliente la lista equivocada de preguntas y dejaba sin preguntar el único bloqueante de la fase.

**Es el fichero desde el que se monta la agenda del checkpoint y el arranque de Design, y hoy es el elemento menos fiable del conjunto.**

**Arreglo.** Dos ficheros en `00 Sistema`:

- **`[Cliente] - Registro v[N].md`** — solo lo inmutable y acumulativo: configuración, tabla de ejecución, censo de asunciones con su historial de estado. Crece por adición y nunca se reescribe.
- **`[Cliente] - Estado v[N].md`** — solo vistas de trabajo, reescritas completas en cada cierre de skill: huecos vivos con dueño y regla de caducidad, hallazgos vigentes con límite duro, y siguiente paso. **Se regenera, no se edita.**

Con dos reglas nuevas: los hallazgos estructurales tienen un techo (12, con consolidación obligatoria al superarlo) y cada hueco lleva la skill no ejecutada que lo necesita, recalculada en cada cierre.

### F8 · Chequeos mecánicos explícitos en `system-qa`

El agente de QA verificó recuentos declarados contra contenido real, punteros caducados y supervivencia del análisis retirado por el cambio de A8. Lo hizo **porque el prompt del operador se lo pidió**, no porque estuviera en su checklist. Conviene que estén en el SKILL.md como verificaciones obligatorias, no dependientes de cómo se invoque.

### F9 · Validación de la especificación de artefactos antes de `/revos:entrega`

La §9 del Revenue Diagnostic declaraba tres estados y usaba cuatro, y sus etiquetas de etapa no coincidían con los nombres de la sección que decía reutilizar. Un checklist de tres líneas al final de la especificación —estados declarados = estados usados, etiquetas = nombres de la sección referenciada, cada elemento marcado tiene entrada en la leyenda— lo habría evitado.

### F10 · Evaluar forzado real de precondiciones

**Observación honesta del operador.** Estuve a punto de saltarme la disciplina dos veces: una editando un entregable en silencio después de haber anunciado que su presupuesto de ciclos estaba agotado. Lo detecté y lo tramité, pero **el sistema depende de que el operador recuerde reglas que no están forzadas en ninguna parte.** El State Log registra; no bloquea.

En un piloto con un operador atento, funciona. Con prisa, con un cliente esperando y con el proyecto en la interacción cuarenta, no es una apuesta que yo haría.

**A evaluar para v5:** un paso de precondición al inicio de cada skill de producción que lea el registro y se detenga si falta fase 0, si el presupuesto de revisión está agotado sin cambio tramitado, o si el último QA de la fase no está APTO. Coste alto y contrario a la agilidad que buscabais — de ahí que sea una decisión de producto y no una recomendación.

---

## 5. Un hallazgo de posicionamiento para RevOS, no para la v5

El valor de este Diagnostic vino de forma desproporcionada de **datos medidos por terceros**, no de lo que el cliente declaró. Las dos piezas centrales de la tesis —el caso CREA y la inexistencia de la categoría *Search Everywhere Optimization*— son verificables por cualquiera y no dependen de la palabra del cliente. Todo lo que el cliente declaró está en el intake y era insuficiente para llegar ahí.

Eso es un argumento comercial para RevOS que no está explotado: **un diagnóstico que le dice al cliente algo que no sabía sobre sí mismo, con evidencia que puede comprobar.** Es lo que separa un diagnóstico de una consultoría que reordena lo que el cliente ya contó. Merece estar en la propuesta comercial, y merece que F5 sea prioritario.

---

## 6. Qué no cambiaría

- El régimen de asunciones con criterio explícito, incluido su carácter falsable.
- `/revos:cambio` como puerta única, con clasificación, versionado, archivado y evaluación de propagación.
- `system-qa` al cierre de fase, delegado en agente independiente.
- La separación entre contenido validado y fichero maquetado.
- La delegación de research pesado en agentes con exigencia de citación.
- Los checkpoints como hito de validación con el cliente.

---

## 7. Resumen

**Cuatro arreglos de coste muy bajo cubren la mayor parte del retorno:** quitar los recuentos numéricos (F1), obligar a cada skill a cerrar los huecos que hereda (F2), separar los dos contadores de ciclos (F3) y hacer que el checkpoint dependa del veredicto del QA (F4). Se pueden aplicar en una tarde editando plantillas y las convenciones.

**Dos arreglos de coste medio valen más de lo que cuestan:** el paso de medición de activos (F5), que es el que produjo el mejor hallazgo de la fase y hoy no existe en el método, y la calibración económica al inicio del brief (F6).

**Uno es de fondo y conviene hacerlo antes de escalar a varios clientes en paralelo:** partir el State Log (F7). Mientras siga siendo un fichero que hace siete trabajos por acumulación, seguirá siendo el elemento menos fiable del sistema — y es el que gobierna los checkpoints.

**Y una decisión de producto que no es un arreglo:** si RevOS va a operarse con prisa, el sistema necesita forzar sus reglas en lugar de confiar en que se recuerden (F10).
