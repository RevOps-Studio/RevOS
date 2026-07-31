---
name: revenue-diagnostic
description: >
  Usar cuando el consultor necesite producir el diagnóstico de revenue end-to-end del cliente: identificar
  cuellos de botella en la cadena desde generación de demanda hasta cierre, priorizar problemas por impacto
  y esfuerzo, y articular la tesis central del diagnóstico. Activar siempre después de competitive-research
  y antes de diagnostic-checkpoint. También activar si el consultor pide "diagnóstico de [cliente]",
  "dónde se rompe el revenue", "qué tiene que arreglar [cliente]" o "diagnóstico final de la fase 1".
---

# Revenue Diagnostic

## Propósito

Este skill produce el Revenue Diagnostic: el documento que cierra la fase de diagnóstico con una lectura end-to-end de la cadena de revenue del cliente y una priorización clara de dónde están los cuellos de botella.

No es un inventario de problemas. Es una tesis. Tiene que responder con claridad tres preguntas: (1) ¿dónde se está rompiendo el revenue de esta empresa hoy?, (2) ¿cuál es el patrón causal — qué causa qué?, (3) ¿qué hay que intervenir primero y por qué?

Esta skill produce el contenido validado en Markdown. El fichero final (artefacto HTML interactivo del funnel para la presentación al cliente y/o documento formal con el análisis completo) lo genera `/revos:entrega` según la preferencia de output de fase 0, siguiendo la especificación de la sección 9.

## Posición en el pipeline

**Requiere:** Client Master Brief v1, Knowledge Base v1, Competitive Landscape v1 (todos obligatorios).

**Produce:** Revenue Diagnostic v1 — contenido validado en Markdown estructurado, incluyendo la especificación del artefacto HTML visual de la cadena de revenue con los cuellos de botella señalados. El fichero final lo genera `/revos:entrega` según la preferencia de output de fase 0.

**Siguiente skill:** diagnostic-checkpoint (validación con cliente antes de avanzar a Design).

## Principios de ejecución

**Tesis sobre inventario.** Todo diagnóstico tiene que terminar con una tesis clara en una frase: "El revenue de esta empresa se rompe principalmente en [punto] porque [causa]." Si no puedes articularlo, el diagnóstico no está terminado.

**Cadena end-to-end.** El diagnóstico no analiza marketing y ventas por separado. Analiza la cadena completa: visibilidad → demanda → captura → cualificación → oportunidad → propuesta → cierre → onboarding. Los cuellos de botella aparecen en las uniones, no dentro de cada función.

**Evidencia sobre opinión.** Cada diagnóstico debe estar sustentado por evidencia del brief, knowledge base o competitive research. Cuando sea inferencia, márcala [HIPÓTESIS]. Cuando falte información para diagnosticar un tramo, [FALTA DATO: descripción del dato que haría falta].

**Priorizar con criterio explícito.** La priorización usa dos ejes: impacto (cuánto revenue desbloquea) y esfuerzo (cuánto cuesta intervenir). Marca cada problema identificado con un score Impacto (A/M/B) × Esfuerzo (A/M/B). No uses escalas numéricas falsas — son juicios cualitativos, que se vean como tales.

**Lenguaje.** Castellano. Registro ejecutivo directo. Di "aquí se está rompiendo", "aquí se está perdiendo", "este es el cuello de botella". Evita "podría ser conveniente", "sería interesante explorar" — el diagnóstico es asertivo, no sugerente.

Convenciones v4.1 — **Precondición**: antes de producir, lee `00 Sistema/[Cliente] - Registro` y detente si falta fase 0, si el presupuesto de revisión de este entregable está agotado sin cambio tramitado por /revos:cambio, o si el cierre de fase anterior exigía un system-qa aún no APTO. **Etiquetado**: cada [FALTA DATO] se clasifica al detectarse como bloqueante (impide una decisión de este entregable) o no bloqueante. **Presupuesto**: 2 ciclos de revisión de calidad por entregable — solo consumen ciclo los cambios nacidos del juicio sobre lo escrito; las incorporaciones de información nueva (aportada por cliente o consultor, o medida por el sistema) no consumen ciclo y generan versión y entrada en el Backlog si el entregable ya está registrado. Agotado el presupuesto, los [FALTA DATO] no bloqueantes se convierten en [ASUNCIÓN: valor asumido + criterio falsable] y el sistema avanza; solo los bloqueantes detienen y se escalan de inmediato. **Resumen para el consultor**: enumera los bloqueantes y lo relevante — nunca recuentos totales (el recuento es chequeo mecánico de system-qa sobre el documento terminado). **Cierre**: todo [FALTA DATO] heredado sale con disposición explícita — resuelto, reasignado a la primera skill no ejecutada que lo necesite, o declinado con motivo. Datos de CRM conectado: [DATO CRM: fuente, fecha]. Referencia completa: skills/revos-orchestrator/references/convenciones.md del plugin revos.

## Proceso

**Paso 1 — Lectura consolidada.**
Lee brief, knowledge base y competitive research como un único corpus. Identifica mentalmente la cadena de revenue de este cliente concreto: cómo llega un lead, cómo se convierte, cuánto tiempo tarda, qué pasa al final.

**Paso 2 — Datos reales de CRM (condicional).**
Si el Registro del proyecto registra un CRM conectado, lanza el agente crm-analyst del plugin para cuantificar el funnel real: volúmenes por etapa, tasas de conversión, ciclo medio, ticket medio, win rate y antigüedad del pipeline. Usa estos datos como base cuantitativa del diagnóstico, marcados [DATO CRM: fuente, fecha]. Un dato inconsistente se marca [DATO NO FIABLE] y se trata como [FALTA DATO]; la suciedad del CRM es en sí misma un hallazgo del diagnóstico.

**Paso 3 — Mapeo de la cadena.**
Dibuja mentalmente (o en texto) la cadena end-to-end con las 7-8 etapas típicas. Para cada etapa, anota: qué sabemos del estado actual, qué métricas hay si las hay, qué problemas se intuyen.

**Paso 4 — Identificación de cuellos de botella.**
Recorre la cadena buscando: (a) puntos donde el volumen cae drásticamente, (b) puntos donde no hay visibilidad de lo que pasa, (c) puntos que dependen exclusivamente del founder, (d) puntos donde la experiencia es inconsistente entre clientes.

**Paso 5 — Análisis causal.**
Para cada cuello de botella identificado, articula la cadena causal: ¿qué lo causa? ¿qué otras fricciones están relacionadas? Muchos "cuellos de botella" son síntomas — busca la causa raíz.

**Paso 6 — Priorización.**
Evalúa cada problema por impacto y esfuerzo. Identifica los 2-3 de máximo impacto y menor esfuerzo (quick wins estratégicos) y los 1-2 de máximo impacto que requieren esfuerzo grande (inversiones estructurales).

**Paso 7 — Articulación de la tesis.**
Escribe en una frase la tesis central del diagnóstico. Si ocupa más de dos líneas, no está afilada todavía — reformula.

**Paso 8 — Especificación del artefacto HTML.**
Especifica la visualización de la cadena de revenue con los cuellos de botella resaltados, según la sección 9 del template. El artefacto lo generará `/revos:entrega`; tu trabajo aquí es dejar la especificación completa. Debe ser legible en presentación al cliente — colores claros para lo que funciona, marcadores visibles para los cuellos de botella, leyenda clara.

**Paso 9 — Revisión de coherencia.**
Verifica: ¿la tesis está soportada por la evidencia en el documento? ¿las prioridades son coherentes con las restricciones del cliente (presupuesto, equipo, tiempo)? ¿el diagnóstico apunta a lo que Design y Activation van a poder resolver?

## Template de output

Produce el output siguiendo exactamente esta estructura.

---

# Revenue Diagnostic — [NOMBRE EMPRESA]
*RevOS Diagnostic · Versión 1.0 · [Fecha]*

---

## 1. Tesis del diagnóstico
*[Una frase de máximo dos líneas. La lectura central del diagnóstico articulada con asertividad. "El revenue de [empresa] se rompe principalmente en [punto] porque [causa], lo que explica [síntoma visible]."]*

---

## 2. Sumario ejecutivo
*[Máximo 300 palabras. Contexto del diagnóstico, principales cuellos de botella detectados, prioridades de intervención, recomendación de alcance para la fase de Design.]*

---

## 3. La cadena de revenue hoy

### 3.1 Diagrama narrativo de la cadena actual
[Descripción end-to-end de cómo funciona el revenue hoy — desde que alguien descubre la empresa hasta que firma. En prosa, fase a fase. Este apartado debe poder leerlo el cliente y reconocerse.]

### 3.2 Estado por etapa
*[Para cada etapa de la cadena, un párrafo con: qué pasa hoy, qué sabemos, qué métricas hay, qué síntomas observamos.]*

**Visibilidad y descubrimiento**
[Descripción]

**Generación de demanda**
[Descripción]

**Captura y conversión inicial**
[Descripción]

**Cualificación**
[Descripción]

**Desarrollo de oportunidad**
[Descripción]

**Propuesta y negociación**
[Descripción]

**Cierre**
[Descripción]

**Onboarding y expansión**
[Descripción — si aplica al modelo del cliente]

---

## 4. Cuellos de botella identificados

### 4.1 Cuello de botella #1 — [Nombre descriptivo]
**Dónde:** [Etapa de la cadena afectada]
**Qué pasa:** [Descripción del problema concreto]
**Por qué pasa:** [Análisis causal — qué lo origina]
**Impacto:** [Qué le está costando al cliente hoy — revenue no capturado, tiempo perdido, oportunidades pasadas]
**Evidencia:** [Qué fuentes del brief/knowledge base soportan este diagnóstico]
**Impacto × Esfuerzo:** [A/M/B × A/M/B]

### 4.2 Cuello de botella #2 — [Nombre descriptivo]
[Misma estructura]

### 4.3 Cuello de botella #3 — [Nombre descriptivo]
[Misma estructura]

*[Típicamente entre 3 y 6 cuellos de botella. Ni menos —el diagnóstico sería superficial— ni más — deja de ser priorización.]*

---

## 5. Patrón causal integrado

### 5.1 Cómo se relacionan los cuellos de botella entre sí
[Análisis de cómo los problemas identificados se encadenan o se refuerzan. Muchos problemas aparentes son síntomas del mismo problema raíz.]

### 5.2 Causa raíz
[La causa fundamental que, si se resolviera, mejoraría varias fricciones a la vez. Puede haber más de una — máximo dos.]

### 5.3 Lo que NO es el problema
[Problemas que el cliente cree tener pero que en realidad no lo son — importante para evitar invertir donde no toca. Con tacto pero con claridad.]

---

## 6. Priorización de intervención

### 6.1 Matriz impacto × esfuerzo
[Listado de los cuellos de botella priorizados en tres grupos:]

**Quick wins estratégicos (impacto alto × esfuerzo bajo-medio)**
[Lista con 1-3 intervenciones]

**Inversiones estructurales (impacto alto × esfuerzo alto)**
[Lista con 1-2 intervenciones]

**Segundo plano (impacto medio o esfuerzo muy alto)**
[Lista con lo que no es prioridad ahora y por qué]

### 6.2 Secuencia recomendada de intervención
[En qué orden conviene atacar los cuellos de botella — con argumento del por qué de esa secuencia]

---

## 7. Implicaciones para Design

### 7.1 Qué skills de Design son prioritarios dado el diagnóstico
[Ej. si el cuello de botella está en posicionamiento, priorizar positioning-messaging; si está en cualificación, priorizar sales-conversion-design]

### 7.2 Decisiones que el cliente tendrá que tomar en Design
[Las 3-5 decisiones estratégicas que emergen del diagnóstico y que Design tendrá que resolver]

### 7.3 Alcance sugerido
[Recomendación: Essentials es suficiente, o se recomienda Complete por [razón]]

---

## 8. Vacíos, hipótesis y dependencias

**Información que falta:** [[FALTA DATO] detectados durante el diagnóstico]
**Hipótesis del consultor:** [[HIPÓTESIS] que requieren validación]
**Contradicciones detectadas:** [[CONTRADICCIÓN DETECTADA] si las hay]
**Dependencias externas:** [Factores externos al diagnóstico que pueden invalidar conclusiones]

---

## 9. Artefacto visual de la cadena de revenue
*[Esta sección es la especificación de estructura del artefacto HTML interactivo del funnel, que genera `/revos:entrega` según la preferencia de output de fase 0. Debe incluir:]*

- Diagrama horizontal de la cadena de revenue del cliente (8 etapas)
- Marcadores visuales sobre los cuellos de botella identificados (color según severidad)
- Leyenda con nombre y severidad de cada cuello de botella
- Impacto × Esfuerzo visible para cada cuello de botella
- Versión presentable directamente al cliente
- Diseño limpio, tipografía legible en pantalla y proyección, colores sobrios (no infografía)

---

## Entrega

Cuando el diagnóstico esté completo:

1. Presenta el output completo en Markdown, incluyendo la especificación del artefacto visual (sección 9) que `/revos:entrega` usará para generar el fichero final según la preferencia de output de fase 0.
2. Añade al final una sección **"Resumen para el consultor"** con:
   - Tesis del diagnóstico en una frase
   - Los cuellos de botella identificados, listados, señalando el crítico — sin recuento total
   - Recomendación de alcance (Essentials / Complete)
   - Nivel de confianza en el diagnóstico (1-5) y qué haría falta para subirlo
   - Las 2-3 decisiones más importantes que el cliente debe confirmar en el checkpoint
3. El contenido validado se guarda como `[Cliente] - Revenue Diagnostic v1.md` en `01 Entregables`. El orquestador lo registra en el Registro. Siguiente skill: diagnostic-checkpoint.

## Lo que NO debes hacer

- No produzcas un diagnóstico sin tesis central — un diagnóstico sin tesis no es un diagnóstico.
- No diagnostiques marketing y ventas por separado — la cadena es una sola.
- No confundas síntoma con causa — si el cliente tiene "pocos leads", probablemente el problema real no es "generar más leads".
- No uses lenguaje blando ("podría haber oportunidad de mejorar") — el diagnóstico es asertivo.
- No priorices por lo que es fácil de implementar si no es lo que más impacto tiene.
- No generes el fichero final directamente — esta skill produce el contenido validado en Markdown; el artefacto HTML y/o documento los genera `/revos:entrega` según la preferencia de output de fase 0.
- No avances a diagnostic-checkpoint sin confirmación explícita del consultor.
