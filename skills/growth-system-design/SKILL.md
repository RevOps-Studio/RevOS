---
name: growth-system-design
description: >
  Usar cuando el consultor necesite diseñar el sistema de generación de demanda full funnel del cliente:
  motores de demanda, tácticas por etapa del funnel, secuencia de activación, modelo de funcionamiento.
  Activar siempre después de positioning-messaging y antes de sales-conversion-design. También activar si
  el consultor pide "diseña el sistema de demanda", "cómo se genera demanda en [cliente]", "motor de
  adquisición" o "arquitectura de growth".
---

# Growth System Design

## Propósito

Este skill diseña el sistema de generación de demanda full funnel del cliente. No es un plan de marketing ni una lista de tácticas — es la arquitectura del motor: qué motores generan demanda, cómo se articulan entre sí, qué función cumple cada uno en el funnel completo, qué capacidades se necesitan para operarlo.

El objetivo es que el cliente termine con un sistema predecible de generación de demanda que no dependa del founder ni de la suerte de un mes puntual. Un sistema que pueda explicarse en una página y pueda operarse por un equipo.

## Posición en el pipeline

**Requiere:** Revenue Diagnostic validado, Positioning & Messaging Architecture v1.

**Produce:** Growth System Design v1 en Markdown. Documento que define el motor de demanda y alimenta channel-strategy-design, content-discoverability-design y media-plan-builder.

**Siguiente skill:** sales-conversion-design (cómo se convierte lo que genera este sistema).

## Principios de ejecución

**Motores, no tácticas.** Un motor de demanda es un mecanismo repetible con inputs, outputs y lógica de funcionamiento. Una táctica es una acción puntual. El sistema se compone de motores, no de tácticas sueltas. Típicamente 3-5 motores — no más.

**Funnel completo, no silos.** El diseño cubre el funnel entero: awareness → consideración → conversión inicial → cualificación → oportunidad. Si un motor solo cubre una etapa, hay que explicitar qué alimenta al siguiente.

**Coherencia con posicionamiento.** Todo motor debe ser coherente con la arquitectura de posicionamiento. Si el posicionamiento eligió ser "especialista en X", los motores no pueden ser de mass-market indiferenciado. La consistencia está primero.

**Realismo operacional.** Cada motor tiene requisitos de equipo, presupuesto, tiempo, herramientas. El diseño incluye esos requisitos explícitamente. Un motor que no se puede operar con el equipo y presupuesto del cliente es un motor imaginario.

**Priorización explícita.** Los motores se priorizan en dos ejes: velocidad hasta primer resultado × impacto potencial. Se distingue entre motores de Q1 (empezar ya), Q2 (siguientes 3 meses) y horizonte largo (6-12 meses).

**Lenguaje.** Castellano. Registro ejecutivo directo. El vocabulario correcto: demanda, motor, funnel, awareness, consideración, conversión, cualificación, pipeline, coste de adquisición. Evita "embudo mágico", "growth hacking", "viralidad", "estrategia omnicanal".

**Convenciones v4.1 — **Precondición**: antes de producir, lee `00 Sistema/[Cliente] - Registro` y detente si falta fase 0, si el presupuesto de revisión de este entregable está agotado sin cambio tramitado por /revos:cambio, o si el cierre de fase anterior exigía un system-qa aún no APTO. **Etiquetado**: cada [FALTA DATO] se clasifica al detectarse como bloqueante (impide una decisión de este entregable) o no bloqueante. **Presupuesto**: 2 ciclos de revisión de calidad por entregable — solo consumen ciclo los cambios nacidos del juicio sobre lo escrito; las incorporaciones de información nueva (aportada por cliente o consultor, o medida por el sistema) no consumen ciclo y generan versión y entrada en el Backlog si el entregable ya está registrado. Agotado el presupuesto, los [FALTA DATO] no bloqueantes se convierten en [ASUNCIÓN: valor asumido + criterio falsable] y el sistema avanza; solo los bloqueantes detienen y se escalan de inmediato. **Resumen para el consultor**: enumera los bloqueantes y lo relevante — nunca recuentos totales (el recuento es chequeo mecánico de system-qa sobre el documento terminado). **Cierre**: todo [FALTA DATO] heredado sale con disposición explícita — resuelto, reasignado a la primera skill no ejecutada que lo necesite, o declinado con motivo. Datos de CRM conectado: [DATO CRM: fuente, fecha]. Referencia completa: skills/revos-orchestrator/references/convenciones.md del plugin revos.

## Proceso

**Paso 1 — Relectura integrada.**
Relee el revenue diagnostic (cuellos de botella en generación de demanda), el positioning (promesa y categoría) y el competitive (canales dominantes del sector). Identifica: dónde está hoy el cuello de botella de generación de demanda, qué motor resolvería ese problema prioritariamente.

**Paso 2 — Inventario de motores posibles.**
Lista los motores candidatos. Típicamente aparecen entre 6 y 10 candidatos: inbound SEO, referral sistemático, outbound ABM, partnerships, eventos propios, eventos de tercero, thought leadership, programa de contenido, paid sintético, community-led. No todos serán seleccionados.

**Paso 3 — Criba por fit.**
Para cada motor candidato, evalúa fit contra tres criterios: (a) coherencia con posicionamiento, (b) viabilidad operativa dada la capacidad del cliente, (c) velocidad hasta primer resultado. Descarta los que fallan alguno de los tres.

**Paso 4 — Selección de 3-5 motores finales.**
Elige 3-5 motores que juntos cubran el funnel completo. No 5 motores todos de awareness — distribución por etapa.

**Paso 5 — Diseño de cada motor.**
Para cada motor seleccionado, describe: (a) qué es, (b) cómo funciona operacionalmente, (c) qué etapa del funnel cubre, (d) qué input necesita, (e) qué output produce, (f) qué indicadores miden su salud, (g) qué capacidades/herramientas requiere, (h) tiempo hasta primer resultado.

**Paso 6 — Articulación del sistema integrado.**
Describe cómo encajan los motores entre sí — qué motor alimenta a cuál, dónde están las junturas, dónde puede haber pérdida de velocidad entre motores.

**Paso 7 — Priorización temporal.**
Define el orden de activación de los motores por trimestres: Q1, Q2, H2. No se activan todos a la vez.

**Paso 8 — Revisión de coherencia.**
Verifica: ¿el sistema resuelve los cuellos de botella del diagnóstico? ¿los motores son coherentes con el posicionamiento? ¿el equipo y presupuesto declarados pueden operar este sistema? ¿hay cobertura de funnel completo?

## Template de output

Produce el output siguiendo exactamente esta estructura.

---

# Growth System Design — [NOMBRE EMPRESA]
*RevOS Design · Versión 1.0 · [Fecha]*

---

## 1. Sumario ejecutivo
*[Máximo 250 palabras. Lectura integrada del sistema propuesto: N motores seleccionados, lógica de funcionamiento, secuencia de activación, requisitos principales.]*

---

## 2. Punto de partida

### 2.1 Cuellos de botella de generación de demanda detectados
[Del revenue diagnostic — qué no está funcionando hoy en generación de demanda]

### 2.2 Estado actual del funnel
[Descripción breve del funnel actual — dónde se capta, cómo se convierte, dónde se pierde]

### 2.3 Restricciones operativas declaradas
[Presupuesto, equipo, tiempo, stack — lo que condiciona el diseño]

---

## 3. Principios de diseño del sistema

### 3.1 Principio 1 — [Nombre]
[Principio que guía el diseño — ej. "predictibilidad sobre picos", "calidad del lead sobre volumen"]

### 3.2 Principio 2 — [Nombre]
[Segundo principio]

### 3.3 Principio 3 — [Nombre]
[Tercer principio, si aplica. Típicamente 2-3 principios.]

---

## 4. Arquitectura del sistema

### 4.1 Mapa de motores
[Lista de los 3-5 motores seleccionados con nombre y una línea de descripción cada uno]

### 4.2 Cobertura del funnel
[Tabla/descripción mostrando qué motor cubre qué etapa del funnel — awareness, consideración, conversión inicial, cualificación, oportunidad]

### 4.3 Lógica de integración
[Cómo se alimentan unos motores a otros — el sistema es un sistema, no motores paralelos]

---

## 5. Diseño detallado por motor

### 5.1 Motor 1 — [Nombre]
**Qué es:** [Descripción en 2-3 líneas]
**Etapa del funnel que cubre:** [Awareness / Consideración / Conversión / Cualificación / Mixto]
**Cómo funciona operativamente:** [Descripción paso a paso del mecanismo]
**Input que necesita:** [Qué hace falta para que funcione — contenido, datos, equipo, presupuesto]
**Output que produce:** [Qué genera — leads, reuniones, pipeline, awareness medida por X]
**Indicadores de salud:** [Qué métricas permiten saber si funciona — 3-5 métricas]
**Capacidades y herramientas requeridas:** [Qué necesita el cliente en stack, equipo, skills]
**Tiempo hasta primer resultado:** [Estimación honesta]
**Escalabilidad:** [Cómo se escala si funciona]
**Riesgos principales:** [Qué podría hacer que no funcione]

### 5.2 Motor 2 — [Nombre]
[Misma estructura]

### 5.3 Motor 3 — [Nombre]
[Misma estructura]

*[Típicamente 3-5 motores. Menos, falta cobertura; más, falta priorización.]*

---

## 6. Integración entre motores

### 6.1 Flujo de prospectos entre motores
[Narrativa de cómo un prospecto viaja a través del sistema — qué motor lo descubre, qué motor lo nutre, qué motor lo convierte]

### 6.2 Puntos críticos del sistema
[Junturas entre motores donde puede haber pérdida — y cómo se mitigan]

### 6.3 Señales de salud del sistema global
[3-5 indicadores que miran al sistema completo, no motor a motor]

---

## 7. Secuencia de activación

### 7.1 Q1 — Arranque
**Motores a activar:** [Lista]
**Hitos esperados:** [Qué debería pasar para saber que el arranque va bien]
**Riesgos del trimestre:** [Qué puede salir mal]

### 7.2 Q2 — Expansión
**Motores a activar:** [Lista — los que se añaden a los de Q1]
**Hitos esperados:** [Qué debería haber cambiado]
**Riesgos del trimestre:** [Qué puede salir mal]

### 7.3 H2 — Consolidación y escalado
**Motores a activar:** [Lista]
**Hitos esperados:** [Qué debería estar demostrado para invertir más]
**Condiciones para escalar:** [Qué tiene que estar probado para aumentar inversión en motores concretos]

---

## 8. Requerimientos del sistema

### 8.1 Capacidades de equipo
[Qué personas/roles hacen falta para operar el sistema — y cuáles faltan en el equipo actual]

### 8.2 Stack y herramientas
[Qué herramientas requiere el sistema — con el stack actual vs. lo que falta]

### 8.3 Presupuesto orientativo
[Rangos de inversión por motor y total, con disclaimer de [HIPÓTESIS] si no hay datos firmes]

### 8.4 Dependencias organizacionales
[Qué tiene que pasar en la organización para que el sistema funcione — decisiones, nuevos procesos, cambios de rol]

---

## 9. Lo que este sistema NO resuelve

[Cuellos de botella del diagnóstico que este sistema no aborda — y que se resolverán en sales-conversion-design, sales-process-design u otros skills. Gestión de expectativas explícita.]

---

## 10. Vacíos e hipótesis

**Información que falta:** [[FALTA DATO]]
**Hipótesis críticas:** [[HIPÓTESIS]]
**Decisiones abiertas para el cliente:** [Decisiones que el diseño deja abiertas]

---

## Entrega

Cuando el sistema esté diseñado:

1. Presenta el output completo en Markdown.
2. Añade al final una sección **"Resumen para el consultor"** con:
   - Los motores seleccionados, listados por nombre — sin recuento
   - Cobertura del funnel — completa / con huecos / con solapes
   - Tiempo estimado hasta primer resultado del sistema completo
   - Las 2-3 decisiones del cliente que más condicionan el diseño
   - Nivel de confianza en que el cliente puede operar este sistema (1-5)
3. El contenido validado se guarda como `[Cliente] - Growth System Design v1.md` en `01 Entregables`. El orquestador lo registra en el Registro. Siguiente skill: `sales-conversion-design`.

## Lo que NO debes hacer

- No listes tácticas sueltas — diseña motores.
- No propongas más de 5 motores — no es priorización.
- No propongas motores que el cliente no puede operar con su equipo y presupuesto — es diseño de papel.
- No diseñes solo motores de awareness sin cobertura de cualificación — funnel incompleto.
- No uses jerga de growth hacking — el cliente es una empresa B2B seria.
- No generes el fichero final DOCX — este skill produce contenido validado en Markdown; el fichero final maquetado lo genera `/revos:entrega` según la preferencia de output registrada en fase 0.
- No avances a sales-conversion-design sin confirmación explícita del consultor.
