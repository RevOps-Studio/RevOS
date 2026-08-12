---
name: conversion-playbook-builder
description: >
  Usar cuando el consultor necesite producir el playbook táctico de conversión del equipo comercial:
  guiones de llamada, estructuras de reunión, objeciones frecuentes y respuestas, plantillas de email,
  checklist por etapa del pipeline, plantillas de propuesta. Activar como skill opcional de Activation
  tras sales-process-design. También activar si el consultor pide "playbook comercial", "guion de ventas",
  "plantillas de venta" o "conversión táctica".
---

# Conversion Playbook Builder

## Propósito

Este skill produce el playbook operativo del equipo comercial: el manual táctico que cualquier SDR o AE puede consultar para saber qué decir, qué preguntar, cómo responder a objeciones, qué enviar y cuándo. Cubre: guión de llamada de descubrimiento, estructura de demo/reunión, librería de objeciones, plantillas de email por etapa, checklist por etapa del pipeline, plantillas de propuesta.

No rediseña el proceso comercial (eso es `sales-process-design`). Convierte el proceso en tácticas ejecutables por personas concretas.

## Posición en el pipeline

**Requiere:** Sales Process Design, Positioning & Messaging. Recomendado: Brand Copy System, Sales Conversion Design.

**Produce:** Conversion Playbook v1 en Markdown validado. El fichero final maquetado (DOCX formal) lo genera `/revos:entrega` según la preferencia de output registrada en fase 0.

**Siguiente skill:** Ninguno obligatorio (skill opcional).

## Principios de ejecución

**Derivado del proceso, no paralelo.** Cada pieza del playbook corresponde a una etapa del sales-process-design. No hay tácticas huérfanas.

**Guiones como estructura, no como script literal.** El guion de llamada da la estructura (apertura → descubrimiento → diagnóstico → siguiente paso) y los "musts" de información a extraer. No es un texto para recitar palabra por palabra — eso degrada la conversación.

**Objeciones reales del cliente.** La librería de objeciones se construye con las objeciones reales que el equipo ha escuchado, no con objeciones genéricas del sector. Si el intake no las recoge, se marca [FALTA DATO] y se pide.

**Respuestas probadas > respuestas elegantes.** Para cada objeción, la respuesta propuesta es breve, estructurada (reconocer + reframe + evidencia) y pensada para escuchar después. Respuestas largas son discursos, no conversaciones.

**Plantillas de email con variables.** Las plantillas tienen variables claras ({{nombre}}, {{empresa}}, {{dolor_detectado}}, {{caso_sector}}) para que la personalización sea rápida pero real.

**Checklists binarios por etapa.** Antes de pasar de una etapa a la siguiente, el comercial ejecuta un checklist binario: todo lo que tiene que estar documentado y confirmado. Sin el checklist completo no se avanza.

**Adaptabilidad por segmento.** Si hay ICPs distintos con mensajes distintos, el playbook tiene variantes por segmento, no una versión media que no sirve para ninguno.

**Convenciones v4.1 — **Precondición**: antes de producir, lee `00 Sistema/[Cliente] - Registro` y detente si falta fase 0, si el presupuesto de revisión de este entregable está agotado sin cambio tramitado por /revos:cambio, o si el cierre de fase anterior exigía un system-qa aún no APTO. **Etiquetado**: cada [FALTA DATO] se clasifica al detectarse como bloqueante (impide una decisión de este entregable) o no bloqueante. **Presupuesto**: 2 ciclos de revisión de calidad por entregable — solo consumen ciclo los cambios nacidos del juicio sobre lo escrito; las incorporaciones de información nueva (aportada por cliente o consultor, o medida por el sistema) no consumen ciclo y generan versión y entrada en el Backlog si el entregable ya está registrado. Agotado el presupuesto, los [FALTA DATO] no bloqueantes se convierten en [ASUNCIÓN: valor asumido + criterio falsable] y el sistema avanza; solo los bloqueantes detienen y se escalan de inmediato. **Resumen para el consultor**: enumera los bloqueantes y lo relevante — nunca recuentos totales (el recuento es chequeo mecánico de system-qa sobre el documento terminado). **Cierre**: todo [FALTA DATO] heredado sale con disposición explícita — resuelto, reasignado a la primera skill no ejecutada que lo necesite, o declinado con motivo. Datos de CRM conectado: [DATO CRM: fuente, fecha]. Referencia completa: skills/revos-orchestrator/references/convenciones.md del plugin revos.

**Lenguaje.** Castellano. Registro ejecutivo operativo — lenguaje que el comercial usa en su día a día. Vocabulario: descubrimiento, diagnóstico, objeción, propuesta, next step, discovery, demo, closing. Evitar: jerga de gurú de ventas, fraseología artificial.

## Proceso

**Paso 1 — Lectura del proceso y mensajes.**
Sales-process-design (etapas, criterios, cadencias), positioning (mensajes, pilares), sales-conversion-design (qué dispara una reunión), brand-copy-system (tono si existe).

**Paso 2 — Recopilación de objeciones reales.**
Del intake, del brief, de entrevistas comerciales si las hay. Lista todas las objeciones realmente escuchadas. Si faltan, [FALTA DATO] y solicítalas al consultor.

**Paso 3 — Guion de llamada de descubrimiento.**
Estructura clara: apertura (contexto + permiso), descubrimiento (preguntas abiertas sobre situación y problemas), diagnóstico (confirmación de dolor + implicaciones), conclusión (siguiente paso específico). Con ejemplos de formulación.

**Paso 4 — Estructura de demo / reunión de producto.**
No es una demo de producto — es una sesión de "problema → solución". Orden: resumen del descubrimiento, propuesta de solución, cómo funciona (producto), prueba (cliente similar), preguntas, siguiente paso.

**Paso 5 — Librería de objeciones.**
Para cada objeción: estructura de respuesta (reconocer + reframe + evidencia + pregunta que devuelve al diálogo). Organizadas por categoría: precio, timing, autoridad, alternativa, estatus quo.

**Paso 6 — Plantillas de email por etapa del pipeline.**
Al menos una plantilla por cada etapa donde el email sea crítico: cold outreach, seguimiento post-descubrimiento, envío de propuesta, cierre, reactivación de dormidas. Con variables claras.

**Paso 7 — Checklist por etapa.**
Derivado exactamente de los criterios binarios del sales-process-design: qué tiene que estar documentado antes de mover a la siguiente etapa.

**Paso 8 — Plantilla de propuesta.**
Estructura: contexto del cliente + problemas identificados + solución propuesta + plan de entrega + inversión + próximos pasos. No es un catálogo de producto.

**Paso 9 — Guía de discovery questions.**
Banco de 40-80 preguntas abiertas clasificadas por categoría (situación, dolor, impacto, criterios de decisión, proceso de compra). El comercial elige según la conversación.

**Paso 10 — Revisión de coherencia.**
¿Cada etapa del proceso tiene sus tácticas? ¿Las objeciones son reales? ¿Las plantillas respetan el tono de voz? ¿Los checklists son exactamente los criterios de sales-process-design?

## Template de output

Produce el output siguiendo exactamente esta estructura.

---

# Conversion Playbook — [NOMBRE EMPRESA]
*RevOS Activation · Versión 1.0 · [Fecha]*

---

## 1. Sumario ejecutivo
*[Máximo 200 palabras. Alcance del playbook, etapas cubiertas, nº de plantillas, nº de objeciones documentadas, cómo usar el documento.]*

---

## 2. Cómo usar este playbook

### 2.1 A quién va dirigido
[SDRs, AEs, Managers]

### 2.2 Cómo consultarlo
[Por etapa del pipeline / por tipo de situación / por tipo de pieza]

### 2.3 Mantenimiento
[Quién actualiza, con qué cadencia, cómo se añaden nuevas objeciones]

---

## 3. Guion de llamada de descubrimiento

### 3.1 Objetivos de la llamada
[Confirmar ICP, identificar dolor, cualificar BANT/MEDDIC, agendar siguiente paso]

### 3.2 Estructura
**Apertura (2-3 min):**
- Contexto de cómo llegaste al contacto
- Agradecimiento y permiso para avanzar
- Pregunta de arranque

**Descubrimiento (15-20 min):**
- Preguntas sobre situación actual
- Preguntas sobre problemas/ineficiencias
- Preguntas sobre impacto del problema

**Diagnóstico (5-10 min):**
- Confirmación del dolor
- Implicaciones del no-cambio

**Conclusión (3-5 min):**
- Siguiente paso propuesto
- Cierre

### 3.3 Frases modelo por bloque
[Para cada bloque, 2-3 formulaciones modelo con tono del cliente]

### 3.4 Errores a evitar
[Hablar demasiado, vender antes de cualificar, no tomar notas, no confirmar next step]

---

## 4. Banco de discovery questions

### 4.1 Preguntas de situación actual
[15-20 preguntas]

### 4.2 Preguntas sobre dolor/ineficiencia
[10-15 preguntas]

### 4.3 Preguntas sobre impacto (emocional, económico)
[10-15 preguntas]

### 4.4 Preguntas sobre criterios de decisión
[10-15 preguntas]

### 4.5 Preguntas sobre proceso de compra
[10-15 preguntas]

---

## 5. Estructura de demo / reunión de producto

### 5.1 Objetivos
[Confirmar fit, demostrar valor, identificar decisores adicionales, definir prueba/piloto]

### 5.2 Orden recomendado (45-60 min)
1. Resumen del descubrimiento (5 min)
2. Propuesta de solución adaptada (10 min)
3. Demo centrada en los 2-3 dolores principales (15-20 min)
4. Prueba — cliente de referencia similar (5 min)
5. Preguntas + objeciones (10 min)
6. Siguiente paso definido (5 min)

### 5.3 Cómo adaptar según audiencia
- Solo decisor técnico: más peso a demo
- Solo decisor económico: más peso a caso + inversión
- Comité (técnico + económico): equilibrio

### 5.4 Errores a evitar
[Demo rígida, no adaptar al descubrimiento, no reservar tiempo a preguntas]

---

## 6. Librería de objeciones

### 6.1 Objeciones de precio
**Objeción:** "Es caro comparado con X."
**Respuesta modelo:**
- Reconocer: "Entiendo la comparación con X."
- Reframe: "La diferencia principal es [mecanismo diferencial], que en tu caso significa [impacto concreto]."
- Evidencia: "Un cliente muy similar a ti tardó Y meses en recuperar la diferencia gracias a Z."
- Pregunta: "¿Qué tendría que ver que te haga sentir que la diferencia está justificada?"

**Objeción:** "Ahora no hay presupuesto."
**Respuesta modelo:** [...]

**Objeción:** "¿Podéis hacer un descuento?"
**Respuesta modelo:** [...]

### 6.2 Objeciones de timing
[3-5 objeciones con respuesta modelo]

### 6.3 Objeciones de autoridad
[3-5 objeciones]

### 6.4 Objeciones de alternativa (competencia o hacerlo internamente)
[3-5 objeciones]

### 6.5 Objeciones de estatus quo
[3-5 objeciones — "ya tenemos algo que funciona"]

---

## 7. Plantillas de email por etapa

### 7.1 Cold outreach — primer contacto
**Asunto:** [Plantilla con variable]
**Cuerpo:** [Plantilla con variables y lógica de personalización]
**CTA:** [...]

### 7.2 Seguimiento post-descubrimiento
[Plantilla]

### 7.3 Envío de propuesta
[Plantilla]

### 7.4 Seguimiento de propuesta sin respuesta
[Plantilla]

### 7.5 Cierre / decisión
[Plantilla]

### 7.6 Reactivación de cerrada perdida
[Plantilla — con ventana recomendada de X meses]

### 7.7 Reactivación de cliente dormido
[Plantilla]

### 7.8 Seguimiento tras referido interno
[Plantilla]

*[8-12 plantillas totales.]*

---

## 8. Checklists por etapa del pipeline

### 8.1 Checklist etapa [X] → etapa [X+1]
Antes de mover la oportunidad a la siguiente etapa, confirma:
- [ ] [Criterio 1 — binario]
- [ ] [Criterio 2 — binario]
- [ ] [Criterio 3 — binario]

### 8.2 Checklist de documentación por etapa
[Qué tiene que estar escrito en CRM]

### 8.3 Checklist de handoff SDR → AE
[Qué transferir, qué documentar]

---

## 9. Plantilla de propuesta

### 9.1 Estructura
1. Portada + resumen ejecutivo (1 página)
2. Contexto del cliente (1 página)
3. Problemas identificados (1-2 páginas)
4. Solución propuesta (2-3 páginas)
5. Plan de entrega (1-2 páginas)
6. Inversión y modelo (1 página)
7. Próximos pasos (0.5 página)

### 9.2 Reglas de redacción
- En "contexto del cliente", usar palabras del cliente (citadas del descubrimiento)
- En "problemas identificados", reflejar impacto en su negocio, no genérico
- En "solución", describir mecanismo + caso de cliente similar
- En "plan", calendario concreto, no placeholder

### 9.3 Duración de validez
[Típicamente 30 días]

---

## 10. Guía de cualificación según framework

### 10.1 Preguntas clave del framework elegido
[Si es MEDDIC: Metrics, Economic buyer, Decision criteria, Decision process, Identify pain, Champion. Preguntas prototipo por cada uno.]

### 10.2 Cómo documentar cada pilar en CRM
[Dónde se registra cada uno]

---

## 11. Señales de oportunidad estancada

[Lista de señales que indican que una oportunidad está muerta aunque aparente seguir viva. Con recomendación de acción — reactivación o cierre.]

---

## 12. Adaptación por segmento

### 12.1 Playbook ICP segmento A
[Qué cambia — objeciones específicas, mensajes prioritarios, duración de ciclo]

### 12.2 Playbook ICP segmento B
[Qué cambia]

---

## 13. Vacíos e hipótesis

**Información que falta:** [[FALTA DATO]] — especialmente objeciones reales del equipo
**Hipótesis críticas:** [[HIPÓTESIS]]
**Decisiones abiertas del cliente:** [Framework de cualificación final, ventanas de reactivación]

---

## Entrega

Cuando el playbook esté completo:

1. Presenta el output en Markdown.
2. Añade al final una sección **"Resumen para el consultor"** con:
   - Las objeciones cubiertas, listadas
   - Las plantillas de email incluidas, listadas por momento del ciclo
   - Las etapas del pipeline que quedan con checklist, listadas
   - Gaps (si hay [FALTA DATO] de objeciones reales)
   - Nivel de confianza en el playbook (1-5)
3. El contenido validado se guarda como `[Cliente] - Conversion Playbook v1.md` en `01 Entregables`. El orquestador lo registra en el Registro.
4. El fichero final maquetado (DOCX formal) lo genera `/revos:entrega` según la preferencia de output registrada en fase 0.

## Lo que NO debes hacer

- No inventes objeciones genéricas del sector — las reales del cliente son las que importan.
- No escribas guiones literales para recitar — estructura con frases modelo, no monólogos.
- No crees plantillas de email sin variables — terminan siendo spam genérico.
- No dupliques el sales-process-design — el playbook aterriza, no rediseña.
- No uses jerga de gurú de ventas — el equipo no la usa en la vida real.
- No generes tú el fichero DOCX final — lo produce `/revos:entrega`; este skill entrega el contenido validado en Markdown.
