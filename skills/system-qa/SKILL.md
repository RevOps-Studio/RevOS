---
name: system-qa
description: >
  Usar cuando el consultor necesite verificar la coherencia transversal entre todos los outputs del sistema
  RevOS producidos hasta ese momento. Es un skill transversal — se ejecuta al final de cada ciclo completo
  de fases (al cerrar Diagnostic, Design o Activation) y antes de entregar al cliente. También activar si el
  consultor pide "revisa la coherencia del sistema", "QA transversal", "verifica que todo encaja" o "auditoría
  de los entregables".
---

# System QA

## Propósito

Este skill ejecuta una auditoría de coherencia transversal sobre todos los outputs del sistema RevOS producidos hasta el momento. No genera contenido nuevo — verifica que los outputs existentes cuenten la misma historia, usen el mismo vocabulario, prioricen los mismos problemas y apunten a las mismas soluciones.

Es el skill que garantiza que el sistema funciona como sistema, no como colección de documentos. Sin este QA, los skills pueden producir outputs técnicamente correctos pero incoherentes entre sí — un ICP en el brief distinto al del positioning-messaging, una tesis de diagnóstico que no se refleja en el roadmap, un stack propuesto que contradice la auditoría.

## Posición en el pipeline

**Requiere:** todos los outputs generados hasta el momento en el proyecto (cualquier combinación de brief, knowledge base, competitive, diagnostic, positioning, growth-system, sales-conversion, roadmap, channels, content, sales-process, measurement, stack audit, CRM, martech, exec deliverables).

**Produce:** QA Report v[N] en Markdown — documento interno del consultor con coherencias verificadas, incoherencias detectadas y acciones correctivas recomendadas.

**Siguiente skill:** depende del resultado del QA. Si es limpio, continuar con el siguiente skill programado. Si hay incoherencias, volver a los skills afectados para corregir.

## Principios de ejecución

**Verificar coherencia, no juzgar calidad.** Este QA no evalúa si un output está bien o mal hecho — evalúa si es coherente con los demás. Un brief puede tener calidad 3/5 pero estar perfectamente coherente con el diagnóstico — eso pasa el QA.

**Niveles de coherencia.** Hay tres niveles: (1) coherencia de datos (mismo ticket, mismo ciclo, mismos segmentos mencionados en distintos documentos), (2) coherencia de vocabulario (mismas categorías narrativas, mismo nombre para los mismos elementos), (3) coherencia de tesis (diagnóstico, diseño y roadmap apuntan a lo mismo).

**Matrices de verificación.** El QA opera con matrices: pares de documentos que deben ser coherentes entre sí. No es una revisión lineal — es un cruce sistemático.

**Severidad clasificada.** Las incoherencias detectadas se clasifican en tres niveles: **[CRÍTICA]** — impide continuar hasta resolverla; **[RELEVANTE]** — conviene resolver antes de entregar al cliente; **[MENOR]** — conviene ajustar en próxima iteración pero no bloquea.

Convenciones v4.3 — **Doctrina de avance**: un [FALTA DATO] es no bloqueante por defecto; solo bloquea si cumple un criterio de la definición cerrada (inversión de tesis · irreversibilidad ante el cliente · imposibilidad material), y la carga de la prueba es del bloqueo. En primera pasada, si la fuente del dato no estará disponible antes del checkpoint, escribe directamente [ASUNCIÓN: valor + criterio falsable] — un v1 con asunciones declaradas es un entregable válido. Máximo 3 preguntas abiertas al consultor por entregable, escaladas agrupadas al cierre del paso, nunca una a una en mitad de la producción. **Lenguaje calibrado**: la asertividad es del entregable, no de la conversación; las conclusiones mayores declaran su confianza (alta: dato medido/CRM · media: declarado por el cliente · baja: inferencia), las consecuencias se formulan condicionadas — nunca proféticas — y el contraste retórico ("No es X. Es Y.") solo es admisible con evidencia de ambos lados. **Precondición**: antes de producir, lee `00 Sistema/[Cliente] - Registro` y detente si falta fase 0, si hay una intervención sin tramitar por /revos:cambio con presupuesto agotado, o si el cierre de fase anterior exigía un system-qa aún no APTO. **Resumen para el consultor**: enumera lo relevante — nunca recuentos totales. Mecánica completa (dos contadores, propagación en lote, disposición de huecos, etiquetas): skills/revos-orchestrator/references/convenciones.md del plugin revos.

**Operativa v4 de la verificación.** En el plugin revos, la verificación puede delegarse en el agente system-qa (solo lectura). El informe se guarda en `03 QA` como `[Cliente] - System QA [Fase] v1.md`. Las correcciones derivadas NUNCA se aplican directamente: entran una a una por el flujo `/revos:cambio`, que clasifica, versiona y evalúa propagación.

**Ejecución parcial v4.** Además del cierre de cada fase, se ejecuta system-qa parcial (solo el subconjunto afectado) cuando el orquestador lo recomienda tras una propagación en cascada de 2+ entregables.

**Verificación adicional v4:** cruzar las [ASUNCIÓN] vigentes del Registro con los entregables — ninguna asunción corregida en checkpoint puede seguir operando como vigente en un documento posterior.

**Lenguaje.** Castellano. Registro técnico interno — este documento es para el consultor, no para el cliente. Puede ser denso.

## Proceso

**Paso 1 — Inventario de outputs disponibles.**
Enumera todos los outputs del sistema existentes en el proyecto. Identifica qué fase cubren y cuáles están pendientes.

**Paso 2 — Extracción de datos clave por output.**
Para cada output, extrae los "datos ancla" que deben ser consistentes: ICP declarado, segmentos, ticket medio, ciclo de venta, cuellos de botella identificados, tesis principal, vocabulario diferencial.

**Paso 3 — Matriz de verificación.**
Cruza cada output con cada otro output relevante. Por ejemplo: ICP del brief vs. ICP del positioning; cuellos de botella del diagnóstico vs. prioridades del roadmap; stack propuesto en martech vs. stack en CRM blueprint.

**Paso 4 — Detección de incoherencias.**
Por cada cruce, identifica incoherencias. No solo "discrepancias obvias" — también inconsistencias sutiles (mismo concepto con dos nombres, secuencia cronológica imposible, prioridad dicha en un lugar y contradicha en otro).

**Paso 5 — Clasificación por severidad.**
Clasifica cada incoherencia en [CRÍTICA], [RELEVANTE] o [MENOR] según el criterio:
- [CRÍTICA]: la incoherencia invalida la lógica del sistema o confundiría al cliente
- [RELEVANTE]: la incoherencia se notaría si el cliente lee dos documentos seguidos
- [MENOR]: la incoherencia es detectable pero no compromete la experiencia

**Paso 6 — Articulación de acciones correctivas.**
Para cada incoherencia, define la acción correctiva concreta: qué output hay que ajustar, qué cambiar exactamente, en qué skill o edición manual. Las correcciones NUNCA se aplican directamente desde este skill: entran una a una por el flujo `/revos:cambio`, que clasifica, versiona y evalúa propagación.

**Paso 7 — Verificación de asunciones vigentes.**
Cruza las [ASUNCIÓN] vigentes del Registro con los entregables — ninguna asunción corregida en checkpoint puede seguir operando como vigente en un documento posterior. Si se detecta, es una incoherencia clasificable por severidad.

**Chequeos mecánicos obligatorios.**
Como parte del proceso — no opcionales — ejecuta siempre estas verificaciones mecánicas:
- **Recuentos y afirmaciones cuantitativas:** contrasta cada recuento y afirmación cuantitativa de cada documento contra su contenido real (si un resumen dice "tres hechos", cuenta los hechos). Los resúmenes no deben declarar totales (F1) — si los declaran, es hallazgo.
- **Punteros caducados:** huecos del `[Cliente] - Estado` asignados a skills ya ejecutadas.
- **Supervivencia de contenido retirado:** nada archivado en `04 Archivo` por un cambio de Concepto puede seguir operando en entregables vigentes.
- **Asunciones:** ninguna [ASUNCIÓN] corregida o refutada en checkpoint puede seguir citada como vigente; toda asunción del censo del Registro debe tener criterio falsable.
- **Coherencia interna del Estado:** sin hallazgos duplicados con estados opuestos, techo de 12 hallazgos respetado.
- **Lenguaje calibrado (v4.3):** conclusiones mayores (tesis, priorización, causa raíz) sin confianza declarada; consecuencias formuladas como profecías en lugar de condicionadas; contraste retórico ("No es X. Es Y." y variantes) usado como énfasis sin evidencia de ambos lados en el documento. Cada caso es hallazgo clasificable por severidad.

**Paso 8 — Verificación de completitud.**
Comprueba que no faltan outputs esperados para la fase en curso. Si la fase está cerrada pero falta algún output, [FALTA OUTPUT: descripción].

## Template de output

Produce el output siguiendo exactamente esta estructura.

---

# QA Report — [NOMBRE EMPRESA]
*RevOS · Ciclo [N] · [Fecha] · Documento interno del consultor*

---

## 1. Resumen ejecutivo del QA

**Fase auditada:** [Diagnostic / Design Essentials / Design Complete / Activation / Completo]
**Outputs revisados:** [Número total de outputs auditados]
**Incoherencias detectadas:** [N críticas / N relevantes / N menores]
**Veredicto:** **[APTO PARA ENTREGAR / AJUSTES RELEVANTES REQUERIDOS / BLOQUEADO POR CRÍTICAS]**
**Acción inmediata recomendada:** [Frase concreta]

---

## 2. Inventario de outputs auditados

| # | Output | Versión | Estado |
|---|--------|---------|--------|
| 1 | Client Master Brief | v1 | ✓ |
| 2 | Knowledge Base | v1 | ✓ |
| 3 | Competitive Landscape | v1 | ✓ |
| 4 | Revenue Diagnostic | v1 | ✓ |
| [...] | [...] | [...] | [...] |

**Outputs esperados ausentes:** [[FALTA OUTPUT] si aplica]

---

## 3. Matriz de verificación

### 3.1 Coherencia de datos
*[Para cada dato ancla, listado de dónde aparece y si es consistente.]*

**ICP declarado**
- Brief: [valor]
- Knowledge Base: [valor]
- Positioning: [valor si existe]
- Growth System: [valor si existe]
- **Coherencia:** [Consistente / [INCOHERENCIA: descripción] · severidad]

**Ticket medio**
- [Matriz similar]

**Ciclo de venta**
- [Matriz similar]

**Segmentos objetivo**
- [Matriz similar]

**Cuellos de botella identificados**
- [Matriz similar]

*[Otros datos ancla según la fase auditada]*

---

### 3.2 Coherencia de vocabulario
*[Verificación de que mismos conceptos se llaman igual en todos los documentos.]*

| Concepto | Nombre canónico | Variantes detectadas | Severidad |
|----------|-----------------|----------------------|-----------|
| [Concepto 1] | [Nombre usado oficialmente] | [Variantes incoherentes] | [Severidad] |

---

### 3.3 Coherencia de tesis
*[Verificación de que diagnóstico, diseño y roadmap apuntan a lo mismo.]*

**Tesis del diagnóstico:** [Frase del revenue-diagnostic]
**Apunta el diseño a esta tesis?** [Sí / No / Parcialmente — con explicación]
**Apunta el roadmap a priorizar según esta tesis?** [Sí / No / Parcialmente — con explicación]

---

### 3.4 Asunciones vigentes vs. entregables
*[Cruce de las [ASUNCIÓN] vigentes del Registro con los entregables. Ninguna asunción corregida en checkpoint puede seguir operando como vigente en un documento posterior.]*

| Asunción | Estado en Registro | Documentos donde sigue operando | Severidad |
|----------|---------------------|---------------------------------|-----------|
| [ASUNCIÓN: ...] | [Vigente / Corregida en checkpoint] | [Lista] | [Severidad] |

---

## 4. Incoherencias detectadas

### 4.1 Incoherencias críticas
**[CRÍTICA #1]:** [Descripción precisa de la incoherencia]
- **Outputs afectados:** [Lista]
- **Qué dice cada uno:** [Citas exactas]
- **Acción correctiva:** [Qué hay que cambiar, dónde, en qué skill o ajuste manual — a tramitar vía `/revos:cambio`]

### 4.2 Incoherencias relevantes
**[RELEVANTE #1]:** [Misma estructura]

### 4.3 Incoherencias menores
**[MENOR #1]:** [Misma estructura]

---

## 5. Lagunas detectadas

**Información declarada en un output pero no usada en los siguientes:** [Lista]
**Hipótesis sin cerrar:** [[HIPÓTESIS] del diagnóstico o design que no se han validado y están bloqueando coherencia]
**Contradicciones arrastradas:** [[CONTRADICCIÓN DETECTADA] que vienen del diagnóstico y no se han resuelto]

---

## 6. Plan de resolución

### 6.1 Acciones antes de entregar al cliente
[Lista numerada de correcciones críticas y relevantes, con output/skill afectado y descripción. Cada corrección entra una a una por el flujo `/revos:cambio`.]

### 6.2 Acciones recomendadas para próxima iteración
[Correcciones menores que se pueden dejar para v2]

### 6.3 Skills que conviene re-ejecutar vs. ajustar manualmente
**Re-ejecutar:** [Skills donde el output está corrompido y vale más regenerar]
**Ajustar manualmente:** [Correcciones puntuales donde el consultor puede editar el documento directamente — siempre tramitadas por `/revos:cambio`]

---

## 7. Firma del QA

**Nivel de coherencia global del sistema:** [1-5]
**Riesgo de entregar al cliente en estado actual:** [Alto / Medio / Bajo]
**Recomendación final:** [Continuar / Corregir antes de continuar / Volver atrás N skills]

---

## Entrega

Cuando el QA Report esté completo:

1. Presenta el output completo en Markdown.
2. Añade al final una sección **"Resumen para el consultor"** con:
   - Veredicto en una frase
   - Top 3 acciones inmediatas que tiene que hacer el consultor
   - Tiempo estimado de corrección
3. Si hay [CRÍTICAS], resuélvelas antes de continuar. Si no hay [CRÍTICAS] pero sí [RELEVANTES], decide si ajustas antes de la próxima entrega al cliente o después.
4. El informe se guarda en `03 QA` como `[Cliente] - System QA [Fase] v1.md`. El orquestador lo registra en el Registro. Al cerrar, el veredicto (**APTO / APTO CON RESERVAS / NO APTO**, con nº de críticos y mayores) se añade a la tabla "Veredictos de system-qa" del Registro — es la entrada que gobierna la doble condición del checkpoint.
5. Las correcciones derivadas NUNCA se aplican directamente: entran una a una por el flujo `/revos:cambio`, que clasifica, versiona y evalúa propagación.

## Lo que NO debes hacer

- No generes contenido nuevo — este skill solo audita.
- No apliques correcciones directamente sobre los entregables — toda corrección entra por el flujo `/revos:cambio`.
- No evalúes la calidad subjetiva de los outputs — solo la coherencia entre ellos.
- No clasifiques todo como [CRÍTICA] — la clasificación tiene que discriminar de verdad.
- No hagas QA sobre outputs que aún no existen — audita solo lo disponible.
- No marques incoherencia sobre datos que están explícitamente marcados como [FALTA DATO], [ASUNCIÓN] o [HIPÓTESIS] en los outputs originales — eso es transparencia, no incoherencia.
- No entregues un QA Report que termine con "todo está bien" si no lo está — la función del skill es detectar, no tranquilizar.
