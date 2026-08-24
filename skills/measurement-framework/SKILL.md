---
name: measurement-framework
description: >
  Usar cuando el consultor necesite definir la arquitectura de medición del cliente: qué métricas se miden,
  con qué fuente, con qué frecuencia, quién las mira y qué decisión desbloquean. Activar al final del tier
  Design Complete, después de sales-process-design y antes de entrar en Activation. También activar si el
  consultor pide "qué medir", "KPIs", "framework de métricas", "dashboard" o "north star metric".
---

# Measurement Framework

## Propósito

Este skill produce el framework de medición del cliente: qué métricas se miden, con qué fuente de dato, con qué definición operativa, con qué frecuencia, quién las mira y qué decisión desbloquean. No es un dashboard estético — es la lista ejecutable de lo que el equipo de RevOps va a instrumentar y mantener.

Es lo que convierte "queremos medir el impacto de marketing" en "medimos pipeline influido por marketing como suma de oportunidades creadas con al menos un touch de marketing en los 90 días previos al cambio de etapa a SQL, fuente CRM + MAP, frecuencia semanal, responsable Head of RevOps, decisión: reasignación mensual de presupuesto por canal."

## Posición en el pipeline

**Requiere:** Revenue Diagnostic, Growth System Design, Sales Conversion Design, Channel Strategy, Content & Discoverability, Sales Process Design.

**Produce:** Measurement Framework v1 en Markdown, incluyendo la especificación de estructura de la matriz operativa XLSX para `/revos:entrega`. Alimenta crm-blueprint-builder, martech-measurement y reporting-operating-system.

**Siguiente skill:** `execution-roadmap-builder` — cierra Design convirtiendo todos los blueprints en roadmap. Activation no empieza hasta que el checkpoint de Design está validado.

## Principios de ejecución

**Cada métrica desbloquea una decisión.** Una métrica que no mueve ninguna decisión no pertenece al framework. La pregunta de chequeo es siempre: "si este número cambia mucho, ¿qué hacemos diferente?". Si no hay respuesta, se elimina.

**Definición operativa antes que nombre bonito.** "Engagement" no es una métrica. "Número de visitantes únicos al mes con ≥3 páginas y ≥2 minutos de sesión, fuente GA4" sí lo es. Toda métrica tiene fórmula, fuente y ventana temporal explícitas.

**Pocas métricas por rol.** Cada rol (CMO, CRO, CEO, SDR Lead, equipo completo) mira entre 5 y 10 métricas. Más es ruido. El framework selecciona para cada rol.

**North Star única.** El cliente tiene una única North Star Metric — la que refleja creación de valor real. Tres North Stars es no tener ninguna. La North Star se elige con criterio, no por voto.

**Métricas de entrada vs. de salida.** Se distingue leading indicators (métricas de actividad que predicen resultado) de lagging indicators (métricas de resultado). El framework equilibra ambas — solo lagging es demasiado tarde, solo leading es cortoplacismo.

**Cadencia proporcional al ciclo.** Métricas de actividad diaria se miran diariamente. Métricas de pipeline mensualmente. Métricas estratégicas trimestralmente. No todo se revisa semanalmente — es ruido.

**Fuente única de verdad.** Cada métrica tiene una y solo una fuente oficial. Si dos sistemas dan valores distintos, se resuelve cuál manda — no se mira el promedio.

Convenciones v4.3 — **Doctrina de avance**: un [FALTA DATO] es no bloqueante por defecto; solo bloquea si cumple un criterio de la definición cerrada (inversión de tesis · irreversibilidad ante el cliente · imposibilidad material), y la carga de la prueba es del bloqueo. En primera pasada, si la fuente del dato no estará disponible antes del checkpoint, escribe directamente [ASUNCIÓN: valor + criterio falsable] — un v1 con asunciones declaradas es un entregable válido. Máximo 3 preguntas abiertas al consultor por entregable, escaladas agrupadas al cierre del paso, nunca una a una en mitad de la producción. **Lenguaje calibrado**: la asertividad es del entregable, no de la conversación; las conclusiones mayores declaran su confianza (alta: dato medido/CRM · media: declarado por el cliente · baja: inferencia), las consecuencias se formulan condicionadas — nunca proféticas — y el contraste retórico ("No es X. Es Y.") solo es admisible con evidencia de ambos lados. **Precondición**: antes de producir, lee `00 Sistema/[Cliente] - Registro` y detente si falta fase 0, si hay una intervención sin tramitar por /revos:cambio con presupuesto agotado, o si el cierre de fase anterior exigía un system-qa aún no APTO. **Resumen para el consultor**: enumera lo relevante — nunca recuentos totales. Mecánica completa (dos contadores, propagación en lote, disposición de huecos, etiquetas): skills/revos-orchestrator/references/convenciones.md del plugin revos.

**Lenguaje.** Castellano. Registro ejecutivo directo. Vocabulario: métrica, KPI, North Star, leading, lagging, fuente, definición operativa, cadencia, umbral, decisión. Evitar: "datos accionables" vacío, "data-driven" sin concreción, "dashboard 360".

## Proceso

**Paso 1 — Lectura integrada de outputs previos.**
Revisa objetivos del cliente (revenue-diagnostic), motores de demanda activados (growth-system), etapas del pipeline (sales-process), canales (channel-strategy), contenidos (content-discoverability). El framework cubre lo que este sistema activa, no más.

**Paso 2 — Definición de la North Star Metric.**
Propón una única North Star que refleje creación de valor real para el cliente. Normalmente es algo del tipo "ARR nuevo cualificado" o "pipeline generado del ICP core" — no "leads totales".

**Paso 3 — Árbol de métricas desde la North Star hacia abajo.**
Descompón la North Star en las 2-4 métricas que la determinan. Descompón cada una en sus 2-4 drivers. Para por arriba en nivel 2-3 de profundidad — más es ruido.

**Paso 4 — Clasificación por dimensión.**
Organiza el árbol en dimensiones: adquisición (canales, contenidos), conversión (funnel, pipeline), retención y expansión (clientes existentes), eficiencia (CAC, LTV, ROI por canal). Típicamente 4-6 dimensiones.

**Paso 5 — Definición operativa por métrica.**
Para cada métrica: fórmula exacta, fuente de dato (sistema), ventana temporal, cadencia de medición, responsable del cálculo, responsable de la revisión, umbral de alerta.

**Paso 6 — Mapa por rol.**
Qué métricas mira cada rol: CEO (3-5), CRO/Dirección de Revenue (5-8), CMO (5-8), Head of RevOps (10-15), Equipo comercial individual (3-5).

**Paso 7 — Conexión con decisiones.**
Para cada métrica: qué decisión desbloquea si sube / si baja / si se estanca. Si no hay decisión asociada, se elimina la métrica.

**Paso 8 — Especificación de estructura para /revos:entrega.**
Documenta en el output la especificación de la matriz operativa XLSX que generará `/revos:entrega` según la preferencia de output registrada en fase 0, con las siguientes hojas: (1) Inventario de métricas, (2) Vista por rol, (3) North Star y árbol, (4) Umbrales y alertas. Este skill no produce el fichero final — produce el contenido validado en Markdown y esta especificación.

**Paso 9 — Revisión de coherencia.**
¿Cada métrica tiene fórmula, fuente, cadencia y decisión? ¿La North Star es única? ¿Hay equilibrio leading/lagging? ¿El stack actual permite medir todo esto — o hay gaps para martech-stack-audit?

## Template de output

Produce el output siguiendo exactamente esta estructura.

---

# Measurement Framework — [NOMBRE EMPRESA]
*RevOS Design Complete · Versión 1.0 · [Fecha]*

---

## 1. Sumario ejecutivo
*[Máximo 250 palabras. North Star elegida, número total de métricas, mapa por rol, gaps de medición detectados, prioridad de instrumentación.]*

---

## 2. North Star Metric

### 2.1 North Star elegida
**Nombre:** [Métrica]
**Definición operativa:** [Fórmula exacta]
**Fuente:** [Sistema de origen]
**Ventana temporal:** [Diaria / Semanal / Mensual / Trimestral]
**Responsable:** [Rol]

### 2.2 Por qué esta y no otra
[Argumento de selección — por qué refleja creación de valor real y no vanity]

### 2.3 Valor actual y objetivo
[Línea base actual, objetivo a 12 meses, ritmo esperado]

---

## 3. Árbol de métricas

### 3.1 Nivel 1 — drivers directos de la North Star
[2-4 métricas que la determinan]

### 3.2 Nivel 2 — drivers de los drivers
[Desglose de cada métrica de nivel 1 en sus 2-4 inputs]

### 3.3 Visualización del árbol
[Diagrama textual o tabla jerárquica]

---

## 4. Inventario por dimensión

### 4.1 Dimensión Adquisición
| Métrica | Definición | Fuente | Ventana | Cadencia | Responsable | Decisión desbloqueada |
|---------|------------|--------|---------|----------|-------------|------------------------|
| [Métrica 1] | [Fórmula] | [Sistema] | [Tiempo] | [Freq] | [Rol] | [Qué decisión] |

### 4.2 Dimensión Conversión
[Misma estructura]

### 4.3 Dimensión Retención y Expansión
[Misma estructura]

### 4.4 Dimensión Eficiencia
[Misma estructura]

### 4.5 Dimensión Operación/Actividad
[Misma estructura]

---

## 5. Mapa por rol

### 5.1 Métricas del CEO / Founder
[3-5 métricas — solo lo estratégico]

### 5.2 Métricas del CRO / Head of Revenue
[5-8 métricas]

### 5.3 Métricas del CMO / Head of Marketing
[5-8 métricas]

### 5.4 Métricas del Head of RevOps
[10-15 métricas — el rol con visión operativa completa]

### 5.5 Métricas del comercial individual
[3-5 métricas — foco en actividad y pipeline propio]

---

## 6. Leading vs. lagging

### 6.1 Métricas leading priorizadas
[Las que predicen resultado con 30-90 días de antelación]

### 6.2 Métricas lagging priorizadas
[Las que confirman resultado a 60-180 días]

### 6.3 Equilibrio y lógica de uso
[Cómo se interpretan conjuntamente — leading para decidir, lagging para confirmar]

---

## 7. Umbrales y alertas

### 7.1 Umbrales por métrica crítica
[Verde / Ámbar / Rojo para las 10-15 métricas más estratégicas]

### 7.2 Lógica de alertas
[Cómo se activan, a quién se notifica, en qué cadencia]

---

## 8. Cadencias de revisión

### 8.1 Revisión diaria
[Qué se mira diariamente — típicamente actividad comercial]

### 8.2 Revisión semanal
[Pipeline, leads, conversiones por etapa]

### 8.3 Revisión mensual
[Resultados de negocio, canales, ROI]

### 8.4 Revisión trimestral
[North Star, árbol completo, ajuste de objetivos]

---

## 9. Brechas de medición detectadas

### 9.1 Métricas no instrumentables hoy
[Qué no se puede medir con el stack actual — input para martech-stack-audit]

### 9.2 Fuentes de dato poco fiables
[Dónde hay dudas sobre la calidad del dato — limpieza necesaria]

### 9.3 Prioridad de instrumentación
[Qué medir primero, qué puede esperar]

---

## 10. Especificación de estructura para /revos:entrega

El fichero final maquetado lo genera `/revos:entrega` según la preferencia de output registrada en fase 0. Especificación de la matriz operativa XLSX — `[Cliente] - Measurement Framework v1.xlsx` — con hojas:
1. Inventario completo de métricas
2. Vista por rol
3. North Star y árbol
4. Umbrales y alertas

---

## 11. Vacíos e hipótesis

**Información que falta:** [[FALTA DATO]]
**Hipótesis críticas:** [[HIPÓTESIS]]
**Decisiones abiertas del cliente:** [Decisiones sobre North Star, objetivos, roles]

---

## Entrega

Cuando el framework de medición esté completo:

1. Presenta el output en Markdown, incluyendo la especificación de estructura para `/revos:entrega`.
2. Añade al final una sección **"Resumen para el consultor"** con:
   - North Star elegida
   - Las métricas del framework, listadas por bloque — sin recuento total
   - Brechas de instrumentación más críticas
   - Nivel de confianza en el framework (1-5)
3. El contenido validado se guarda como `[Cliente] - Measurement Framework v1.md` en `01 Entregables`. El orquestador lo registra en el Registro. El XLSX final lo genera `/revos:entrega`. Siguiente skill: `execution-roadmap-builder` (cierre de Design). Activation arranca después del checkpoint de Design validado.

## Lo que NO debes hacer

- No propongas más de una North Star — por definición es una.
- No incluyas métricas sin decisión asociada — son ruido.
- No uses definiciones vagas ("engagement", "calidad de lead") — siempre fórmula operativa.
- No ignores la capacidad actual de medición — marca las brechas para martech-stack-audit.
- No asumas cadencias uniformes — cada métrica tiene la suya.
- No avances a martech-stack-audit sin confirmación del consultor.
- No generes el fichero XLSX final — eso corresponde a `/revos:entrega`; este skill entrega el contenido validado en Markdown y la especificación de estructura.
