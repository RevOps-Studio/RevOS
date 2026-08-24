---
name: positioning-messaging
description: >
  Usar cuando el consultor necesite construir la arquitectura estratégica de posicionamiento y mensajes del
  cliente: categoría narrativa, promesa central, pilares de mensaje, value propositions por segmento,
  mensajes por etapa del funnel. Es el primer skill de la fase Design. Activar siempre después del
  diagnostic-checkpoint validado y antes de growth-system-design. También activar si el consultor pide
  "construye el posicionamiento de [cliente]", "arquitectura de mensajes", "mensaje central" o "cómo se
  posiciona [cliente] en su mercado".
---

# Positioning & Messaging

## Propósito

Este skill construye la arquitectura de posicionamiento y mensajes del cliente. Es la pieza estratégica que articula: qué categoría ocupa la empresa en el mercado, qué promete de forma diferencial, con qué pilares sostiene esa promesa, y cómo se traduce a mensajes concretos por segmento y por etapa del funnel.

No es copy — es la infraestructura sobre la que luego se construye el copy. Otros skills (brand-copy-system, content-calendar, media-plan) consumen este documento como input. Sin arquitectura de posicionamiento clara, cada canal acaba contando una historia distinta.

## Posición en el pipeline

**Requiere:** Client Master Brief, Knowledge Base, Competitive Landscape, Revenue Diagnostic — todos validados en el checkpoint de Diagnostic.

**Produce:** Positioning & Messaging Architecture v1 en Markdown. Documento de referencia que alimenta todos los skills posteriores de Design y Activation.

**Siguiente skill:** growth-system-design (usa el posicionamiento como motor narrativo del sistema de demanda).

## Principios de ejecución

**Categoría antes que producto.** El posicionamiento empieza por definir qué categoría ocupa la empresa. Un producto idéntico posicionado en dos categorías distintas vende a distintos compradores, compite con distintas alternativas y se vende a distinto precio. La elección de categoría es estratégica, no descriptiva.

**Promesa, no descripción.** La promesa central no describe lo que la empresa hace — articula lo que el cliente obtiene. "Ayudamos a equipos comerciales a cerrar más rápido" es descripción. "El cierre deja de depender de tu director comercial" es promesa.

**Diferenciación defendible.** Cada pilar de mensaje tiene que ser (a) relevante para el ICP, (b) diferenciado de los competidores identificados en el competitive research, (c) defendible con capacidades reales del cliente. Si un pilar no cumple los tres criterios, no es pilar — es ruido.

**Segmentación con intencionalidad.** Los mensajes por segmento no son variaciones cosméticas — son traducciones de la misma promesa central a los códigos de cada segmento. Si un segmento requiere un mensaje radicalmente distinto, probablemente no es un subsegmento — es un mercado distinto.

**Integridad con el diagnóstico.** El posicionamiento tiene que resolver (o al menos abordar) los cuellos de botella del diagnóstico relacionados con posicionamiento. Si el diagnóstico dijo "la empresa está indiferenciada en un mercado commodity", el posicionamiento no puede proponer la misma posición genérica.

**Lenguaje.** Castellano. Registro ejecutivo directo. Prohibido: "transformamos el negocio", "experiencia 360", "ecosistema", "soluciones integrales". Los mensajes deben sonar como los diría un operador, no una agencia.

Convenciones v4.3 — **Doctrina de avance**: un [FALTA DATO] es no bloqueante por defecto; solo bloquea si cumple un criterio de la definición cerrada (inversión de tesis · irreversibilidad ante el cliente · imposibilidad material), y la carga de la prueba es del bloqueo. En primera pasada, si la fuente del dato no estará disponible antes del checkpoint, escribe directamente [ASUNCIÓN: valor + criterio falsable] — un v1 con asunciones declaradas es un entregable válido. Máximo 3 preguntas abiertas al consultor por entregable, escaladas agrupadas al cierre del paso, nunca una a una en mitad de la producción. **Lenguaje calibrado**: la asertividad es del entregable, no de la conversación; las conclusiones mayores declaran su confianza (alta: dato medido/CRM · media: declarado por el cliente · baja: inferencia), las consecuencias se formulan condicionadas — nunca proféticas — y el contraste retórico ("No es X. Es Y.") solo es admisible con evidencia de ambos lados. **Precondición**: antes de producir, lee `00 Sistema/[Cliente] - Registro` y detente si falta fase 0, si hay una intervención sin tramitar por /revos:cambio con presupuesto agotado, o si el cierre de fase anterior exigía un system-qa aún no APTO. **Resumen para el consultor**: enumera lo relevante — nunca recuentos totales. Mecánica completa (dos contadores, propagación en lote, disposición de huecos, etiquetas): skills/revos-orchestrator/references/convenciones.md del plugin revos.

## Proceso

**Paso 1 — Relectura estratégica del diagnóstico.**
Antes de diseñar nada, relee el revenue diagnostic y el competitive landscape. Identifica: qué categoría narrativa está disputada, qué gaps de posicionamiento se detectaron, qué fricciones del diagnóstico están vinculadas a posicionamiento.

**Paso 2 — Decisión de categoría.**
Articula 2-3 categorías narrativas candidatas en las que el cliente podría posicionarse. Evalúa cada una contra: tamaño del espacio, nivel de saturación (según competitive), fit con capacidades del cliente (según knowledge base), apelación al ICP. Elige una.

**Paso 3 — Construcción de la promesa central.**
Articula la promesa en una frase. Verifica: ¿es una promesa de resultado (no de actividad)? ¿es diferencial frente a los competidores? ¿es creíble dado lo que sabemos de las capacidades del cliente?

**Paso 4 — Definición de los pilares.**
Define 3-4 pilares de mensaje que sostengan la promesa. Cada pilar debe responder a "¿por qué deberíamos creerte esta promesa?". Los pilares son las razones para creer — no las funcionalidades.

**Paso 5 — Traducción a segmentos.**
Para cada segmento relevante (primario + 1-2 secundarios máximo), traduce la promesa y los pilares al lenguaje y las preocupaciones específicas. La esencia es la misma; la manifestación, distinta.

**Paso 6 — Mensajes por etapa del funnel.**
Articula el mensaje dominante en 3 etapas: (a) visibilidad/awareness — cómo se presenta la categoría; (b) consideración — qué argumentos empujan a la conversación; (c) decisión — qué mata objeciones y genera urgencia.

**Paso 7 — Banco de anti-mensajes.**
Identifica los mensajes que NO se deben usar: lo que dicen los competidores que no queremos replicar, formulaciones genéricas que diluyen, claims que no podemos defender.

**Paso 8 — Revisión de coherencia.**
Verifica: ¿la categoría elegida es coherente con el mapa competitivo? ¿la promesa es coherente con los casos de cliente reales de la knowledge base? ¿los pilares son demostrables con capacidades declaradas? ¿el mensaje de awareness es distinto al de decisión?

## Template de output

Produce el output siguiendo exactamente esta estructura.

---

# Arquitectura de Posicionamiento y Mensajes — [NOMBRE EMPRESA]
*RevOS Design · Versión 1.0 · [Fecha]*

---

## 1. Sumario ejecutivo
*[Máximo 250 palabras. Categoría elegida, promesa central en una frase, pilares principales, traducción a segmentos, implicaciones para los siguientes skills.]*

---

## 2. La decisión estratégica de categoría

### 2.1 Categorías candidatas evaluadas
*[Las 2-3 categorías narrativas que se consideraron, con evaluación breve de cada una]*

**Categoría A — [Nombre]**
- Tamaño del espacio: [Descripción]
- Saturación competitiva: [Descripción]
- Fit con capacidades del cliente: [Descripción]
- Apelación al ICP: [Descripción]

**Categoría B — [Nombre]**
[Misma estructura]

### 2.2 Categoría elegida
**[Nombre de la categoría]**

### 2.3 Argumentación
[Por qué esta categoría y no las otras — con argumento explícito que enlaza diagnóstico, competencia y capacidades]

### 2.4 Implicaciones de esta elección
[Qué significa operacionalmente haber elegido esta categoría — contra qué se compite, a quién se vende, qué alternativas se declaran obsoletas]

---

## 3. La promesa central

### 3.1 Formulación canónica
**[Frase de la promesa — una sola frase, idealmente bajo 15 palabras]**

### 3.2 Formulación alternativa
**[Formulación de respaldo — misma idea, registro levemente distinto para cuando la canónica no encaja en un contexto]**

### 3.3 Qué es y qué no es esta promesa
**Es:** [Lista breve de lo que sí afirma]
**No es:** [Lista breve de lo que NO afirma — importante para evitar expansión indiscriminada]

### 3.4 Prueba: ¿por qué el ICP debería creer esto?
[Argumento breve de credibilidad inicial — lo que permite que esta promesa no sea percibida como discurso vacío]

---

## 4. Los pilares de mensaje

### 4.1 Pilar 1 — [Nombre corto y accionable]
**Qué afirma:** [Frase clara]
**Por qué es creíble:** [Qué capacidades del cliente lo sustentan]
**Por qué es diferencial:** [Contra qué competidor/alternativa lo diferencia]
**Evidencia disponible:** [Casos, datos, referencias que lo prueban — o [FALTA EVIDENCIA]]

### 4.2 Pilar 2 — [Nombre]
[Misma estructura]

### 4.3 Pilar 3 — [Nombre]
[Misma estructura]

### 4.4 Pilar 4 — [Nombre, si aplica]
[Típicamente entre 3 y 4 pilares. Menos, el posicionamiento queda expuesto; más, se diluye.]

---

## 5. Traducción por segmento

### 5.1 Segmento primario — [Descripción del segmento]
**Lo que les quita el sueño:** [Preocupación central del decisor en este segmento]
**Cómo se formula la promesa para ellos:** [Promesa central adaptada a su lenguaje]
**Pilares con más peso:** [Cuáles de los 3-4 pilares tiran más en este segmento]
**Vocabulario específico:** [3-5 términos que resuenan en este segmento]

### 5.2 Segmento secundario 1 — [Descripción]
[Misma estructura]

### 5.3 Segmento secundario 2 — [Descripción — si aplica]
[Típicamente máximo 3 segmentos. Más segmentos = no hay segmentación.]

---

## 6. Mensajes por etapa del funnel

### 6.1 Visibilidad / Awareness
**Objetivo de la comunicación en esta etapa:** Generar reconocimiento de categoría y de marca
**Mensaje dominante:** [Frase]
**Formulaciones alternativas:** [2-3 variantes para distintos formatos]
**Qué evitar:** [Mensajes que son demasiado adelantados para esta etapa]

### 6.2 Consideración
**Objetivo:** Empujar a la conversación y diferenciarse de alternativas
**Mensaje dominante:** [Frase]
**Formulaciones alternativas:** [2-3 variantes]
**Qué evitar:** [Errores típicos en esta etapa]

### 6.3 Decisión
**Objetivo:** Matar objeciones, generar urgencia, cerrar
**Mensaje dominante:** [Frase]
**Formulaciones alternativas:** [2-3 variantes]
**Qué evitar:** [Errores típicos — ej. descuentos que devalúan posicionamiento]

---

## 7. Banco de anti-mensajes

### 7.1 Lo que NO decimos
[Lista de formulaciones explícitamente descartadas — genéricas, de agencia, demasiado amplias]

### 7.2 Lo que dicen los competidores que no replicamos
[Mensajes que usan competidores identificados en el competitive research y que sería un error imitar]

### 7.3 Claims que no podemos defender
[Afirmaciones que serían diferenciadoras pero que el cliente no puede sostener hoy — registrar para evitar que se cuelen por inercia]

---

## 8. Implicaciones operacionales

### 8.1 Para la web
[Qué debería cambiar en la web del cliente dado este posicionamiento — en titulares, no en diseño]

### 8.2 Para el pitch comercial
[Cómo debería cambiar la primera parte del pitch del equipo comercial]

### 8.3 Para contenido y thought leadership
[Qué tipos de contenido son consistentes con este posicionamiento — y cuáles no]

### 8.4 Para sales enablement
[Qué necesita el equipo comercial para poder defender este posicionamiento en sus conversaciones]

---

## 9. Vacíos e hipótesis

**Información que falta:** [[FALTA DATO] identificados]
**Hipótesis a validar con el cliente:** [[HIPÓTESIS]]
**Claims que requieren validación de evidencia:** [[FALTA EVIDENCIA] en pilares]
**Decisiones abiertas:** [Decisiones que el posicionamiento deja abiertas y que requerirán input del cliente]

---

## Entrega

Cuando la arquitectura esté completa:

1. Presenta el output completo en Markdown.
2. Añade al final una sección **"Resumen para el consultor"** con:
   - Categoría elegida en una frase
   - Promesa central en una frase
   - Los pilares y segmentos, listados por nombre — sin recuento
   - Nivel de confianza en la arquitectura (1-5)
   - Las 2-3 decisiones que el cliente tendría que validar antes de avanzar
   - Alerta sobre claims que requieren evidencia
3. El contenido validado se guarda como `[Cliente] - Positioning & Messaging v1.md` en `01 Entregables`. El orquestador lo registra en el Registro. Siguiente skill: `growth-system-design`.

## Lo que NO debes hacer

- No produzcas una promesa que sea descripción de lo que la empresa hace — debe ser resultado para el cliente.
- No propongas más de 4 pilares — más pilares = ningún pilar.
- No uses jerga de agencia ("transformación", "ecosistema", "holístico", "360", "journey integral").
- No propongas mensajes de awareness que se parezcan a los de decisión — son etapas con objetivos distintos.
- No ignores los competidores del competitive research — el posicionamiento se define frente a ellos.
- No generes el fichero final DOCX — este skill produce contenido validado en Markdown; el fichero final maquetado lo genera `/revos:entrega` según la preferencia de output registrada en fase 0.
- No avances a growth-system-design sin confirmación explícita del consultor.
