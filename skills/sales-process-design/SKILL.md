---
name: sales-process-design
description: >
  Usar cuando el consultor necesite diseñar el proceso comercial operativo del cliente: etapas del pipeline,
  criterios de avance entre etapas, definiciones MQL/SAL/SQL, playbook comercial básico, reglas de forecasting,
  cadencia comercial y gestión de pipeline. Activar dentro del tier Complete, después de sales-conversion-design
  y content-discoverability-design. También activar si el consultor pide "diseño del proceso comercial",
  "etapas del pipeline", "playbook comercial" o "proceso de venta".
---

# Sales Process Design

## Propósito

Este skill produce el proceso comercial operativo del cliente: qué etapas tiene el pipeline, qué define avanzar de una a la siguiente, qué se hace en cada etapa, cómo se pronostica el cierre, qué actividades son obligatorias, qué cadencia se aplica a cada tipo de oportunidad.

Es el documento que traduce el diseño de conversión (qué pasa para que un contacto llegue a reunión) en un proceso replicable de equipo comercial. Es la base operativa sobre la que después se configura el CRM.

## Posición en el pipeline

**Requiere:** Sales Conversion Design, Positioning & Messaging, Revenue Diagnostic (para entender el punto de partida comercial real).

**Produce:** Sales Process Design v1 en Markdown. Alimenta crm-blueprint-builder, measurement-framework y conversion-playbook-builder.

**Siguiente skill:** measurement-framework.

## Principios de ejecución

**Proceso al servicio del ciclo de venta real.** Las etapas del pipeline tienen que reflejar cómo el cliente realmente compra, no un modelo teórico genérico. Un ciclo consultivo de 9 meses con 4 decisores no tiene el mismo pipeline que un ciclo transaccional de 30 días.

**Definiciones binarias.** Cada etapa tiene un criterio de entrada y un criterio de salida binarios: se cumplen o no se cumplen. "Interesado" no es un criterio. "Ha confirmado un presupuesto disponible ≥X y una fecha orientativa de decisión" sí lo es. Esto es lo que elimina la subjetividad del comercial y lo que hace fiable el forecast.

**Pocas etapas, bien definidas.** Entre 4 y 7 etapas en el pipeline típico B2B. Más etapas crean fricción operativa sin ganancia de información. Menos etapas dejan huecos de gestión.

**MQL / SAL / SQL con criterios explícitos.** El handoff entre marketing y ventas es donde se pierde más pipeline. MQL (criterio de marketing), SAL (aceptado por ventas), SQL (cualificado por ventas) son conceptos operativos, no etiquetas. Cada transición tiene un criterio escrito y un SLA.

**Cadencia proporcional al valor.** No todas las oportunidades reciben el mismo esfuerzo. Se define cadencia por tipo de oportunidad (ICP core vs. secundario, ticket alto vs. medio).

**Forecasting con probabilidades asignadas.** Cada etapa del pipeline lleva una probabilidad orientativa de cierre. El forecast se construye a partir del pipeline ponderado, con reglas claras para mover fechas y cantidades.

**Convenciones v4:** cada [FALTA DATO] se clasifica al detectarse como bloqueante (impide una decisión de este entregable) o no bloqueante. Presupuesto máximo: 2 ciclos de revisión por entregable. Agotado el presupuesto, los [FALTA DATO] no bloqueantes se convierten en [ASUNCIÓN: valor asumido + criterio] y el sistema avanza; solo los bloqueantes detienen y se escalan al cliente de inmediato. Los datos extraídos de CRM conectado se marcan [DATO CRM: fuente, fecha]. Referencia completa: skills/revos-orchestrator/references/convenciones.md del plugin revos.

**Lenguaje.** Castellano. Registro ejecutivo directo. Vocabulario: pipeline, etapa, criterio de avance, MQL, SAL, SQL, cadencia, forecast, probabilidad ponderada, SLA, BANT/MEDDIC/MEDDPICC (si se usa). Evitar: "embudo mágico", "funnel 360", "hunter/farmer" como cliché.

## Proceso

**Paso 1 — Lectura del contexto comercial actual.**
Revisa revenue-diagnostic (cómo vende hoy), sales-conversion-design (qué se ha definido como conversión), positioning (qué ICP y qué mensajes). Identifica ciclo de venta medio, número de decisores medio, ticket medio, principales objeciones.

**Paso 2 — Mapeo del recorrido de compra del ICP.**
Desde el lado del comprador: cómo detecta el problema, cómo evalúa soluciones, quién entra en el proceso, qué decide cada decisor, qué desbloquea cada decisión. Esto es lo que define las etapas.

**Paso 3 — Diseño de etapas del pipeline.**
Propón 4-7 etapas. Para cada etapa: nombre, criterio de entrada, criterio de salida, actividades que ocurren, artefactos producidos, duración orientativa, tasa de conversión esperada a la siguiente.

**Paso 4 — Definiciones MQL / SAL / SQL.**
Criterios explícitos de cada transición. SLA de respuesta de ventas tras MQL. Proceso de devolución (ventas puede rechazar SAL y explicar por qué — para que marketing aprenda).

**Paso 5 — Diseño de cadencias.**
Por tipo de oportunidad: cuántos touches, en qué canales, con qué ritmo, hasta cuándo. Diferenciar inbound vs. outbound. Diferenciar ticket y fit.

**Paso 6 — Cualificación y descalificación.**
Framework de cualificación recomendado (BANT / MEDDIC / MEDDPICC / personalizado) y cómo se documenta. Criterios explícitos de descalificación — cuándo se cierra una oportunidad como "perdida no trabajada".

**Paso 7 — Forecasting.**
Probabilidad por etapa. Regla de avance de probabilidad. Regla de revisión de fechas y cantidades. Cadencia de revisión del forecast (semanal/mensual).

**Paso 8 — Roles y handoffs.**
Quién hace qué en cada etapa: SDR, AE, AM, preventa, legal. Cómo se transfieren oportunidades entre roles. Dónde quedan documentadas las conversaciones.

**Paso 9 — Revisión de coherencia.**
¿Las etapas reflejan el ciclo de compra real? ¿Los criterios son binarios? ¿Las probabilidades son calibrables? ¿El equipo actual puede operar esto?

## Template de output

Produce el output siguiendo exactamente esta estructura.

---

# Sales Process Design — [NOMBRE EMPRESA]
*RevOS Design Complete · Versión 1.0 · [Fecha]*

---

## 1. Sumario ejecutivo
*[Máximo 250 palabras. Número de etapas, definiciones MQL/SAL/SQL, duración media prevista del ciclo, principales cambios respecto al proceso actual.]*

---

## 2. Contexto comercial

### 2.1 Situación actual (Revenue Diagnostic)
[Resumen operativo: ciclo de venta actual, tasas de conversión actuales, principales fugas]

### 2.2 Ciclo de compra del ICP
[Cómo compra realmente el ICP: detonante, evaluación, decisores, criterios, plazos]

### 2.3 Framework de cualificación elegido
[BANT / MEDDIC / MEDDPICC / personalizado — y por qué este y no otro]

---

## 3. Definiciones operativas

### 3.1 MQL — Marketing Qualified Lead
**Criterio:** [Requisitos exactos para que marketing pase un lead a ventas]
**Fuente del dato:** [De dónde viene la información]
**Responsable de la clasificación:** [Quién marca un lead como MQL]

### 3.2 SAL — Sales Accepted Lead
**Criterio:** [Requisitos para que ventas acepte el MQL]
**SLA de respuesta:** [Tiempo máximo para aceptar o rechazar un MQL — típicamente ≤48h]
**Proceso de rechazo:** [Cómo se devuelve un MQL no aceptado, con motivo]

### 3.3 SQL — Sales Qualified Lead
**Criterio:** [Requisitos para que ventas califique un SAL como oportunidad activa]
**Campos mínimos que tienen que estar completos en CRM:** [Lista]

### 3.4 Oportunidad
**Criterio:** [Cuándo un SQL se convierte formalmente en oportunidad en pipeline]

---

## 4. Diseño del pipeline

### 4.1 Vista general de etapas
| # | Etapa | Criterio de entrada | Criterio de salida | Prob. cierre | Duración típica |
|---|-------|---------------------|--------------------|--------------:|-----------------|
| 1 | [Nombre] | [Criterio] | [Criterio] | 10% | [X días] |
| 2 | [Nombre] | [Criterio] | [Criterio] | 25% | [X días] |
| ... |

### 4.2 Detalle por etapa

#### Etapa 1 — [Nombre]
**Criterio de entrada:** [Binario]
**Criterio de salida:** [Binario]
**Actividades que ocurren:** [Lista ordenada]
**Artefactos producidos:** [Notas de llamada, demo, propuesta, etc.]
**Responsable:** [SDR / AE / AM]
**Duración típica:** [Días]
**Tasa de conversión esperada a la siguiente etapa:** [%]
**Señales de alerta (stalling):** [Cuándo dar por perdida]

#### Etapa 2 — [Nombre]
[Misma estructura]

*[Entre 4 y 7 etapas.]*

---

## 5. Cadencias comerciales

### 5.1 Cadencia inbound core ICP
**Número de touches:** [X]
**Canales:** [Email, llamada, LinkedIn, ...]
**Ritmo:** [Ej. 8 touches en 14 días]
**Mensajes clave:** [Temas dominantes de cada touch]

### 5.2 Cadencia outbound core ICP
[Misma estructura]

### 5.3 Cadencia ICP secundario / ticket menor
[Misma estructura, calibrada a menor inversión por oportunidad]

### 5.4 Reactivación de cerradas perdidas
[Cuándo y cómo se reactivan oportunidades perdidas — ventana de tiempo, criterio]

---

## 6. Forecasting

### 6.1 Probabilidades por etapa
[Tabla de probabilidades — las mismas del pipeline, consolidadas]

### 6.2 Reglas de ponderación
[Cómo se calcula el forecast ponderado — pipeline * probabilidad]

### 6.3 Revisión del forecast
**Cadencia:** [Semanal / Quincenal]
**Participantes:** [Quién participa]
**Criterios de revisión:** [Qué se mira, qué hace saltar alarmas]
**Movimientos permitidos:** [Cuándo se puede mover fecha o cantidad y con qué justificación]

---

## 7. Roles y handoffs

### 7.1 Roles en el proceso
| Rol | Responsabilidades | Etapas donde interviene |
|-----|-------------------|-------------------------|
| SDR | [...] | [1, 2] |
| AE | [...] | [3, 4, 5] |
| ... |

### 7.2 Handoffs críticos
[Transiciones de responsabilidad: Marketing → SDR, SDR → AE, AE → AM. Qué se transfiere, cómo se documenta, SLA.]

---

## 8. Criterios de descalificación

### 8.1 Descalificación temprana
[Cuándo cerrar una oportunidad sin trabajar — ahorra esfuerzo]

### 8.2 Descalificación en proceso
[Señales de oportunidad "stalled" y cuándo cerrarla como perdida]

### 8.3 Motivos de pérdida estandarizados
[Lista cerrada de motivos para poder analizar después]

---

## 9. Métricas del proceso

### 9.1 Salud del pipeline
[Coverage ratio, velocidad, conversión etapa a etapa, tamaño medio, ciclo medio]

### 9.2 Actividad comercial
[Volumen de touches, tasa de respuesta, reuniones agendadas, demos realizadas]

### 9.3 Forecast accuracy
[Desviación forecast vs. real — objetivo de error bajo]

---

## 10. Diferencias respecto al proceso actual

[Tabla de lo que cambia respecto a cómo vende hoy el cliente: etapas antes/después, criterios nuevos, cadencias nuevas]

---

## 11. Requerimientos operativos

### 11.1 Herramientas mínimas necesarias
[CRM, telefonía, secuenciador, herramienta de reuniones, etc.]

### 11.2 Capacitación necesaria
[Qué formación necesita el equipo para operar el proceso]

### 11.3 Calendario de puesta en marcha
[Propuesta de rollout en fases]

---

## 12. Vacíos e hipótesis

**Información que falta:** [[FALTA DATO]]
**Hipótesis críticas:** [[HIPÓTESIS]]
**Decisiones abiertas del cliente:** [Framework, asignación de territorios, roles]

---

## Entrega

Cuando el diseño del proceso comercial esté completo:

1. Presenta el output completo en Markdown.
2. Añade al final una sección **"Resumen para el consultor"** con:
   - Número de etapas del pipeline
   - Framework de cualificación seleccionado
   - Duración media prevista del ciclo
   - Principales cambios respecto al proceso actual
   - Nivel de confianza en el diseño (1-5)
3. El contenido validado se guarda como `[Cliente] - Sales Process v1.md` en `01 Entregables`. El orquestador lo registra en el State Log. Siguiente skill: `measurement-framework`.

## Lo que NO debes hacer

- No diseñes más de 7 etapas — complejidad innecesaria.
- No uses criterios subjetivos ("interesado", "cualificado") — siempre binarios y auditables.
- No copies un framework comercial sin adaptarlo al ICP y al ciclo real del cliente.
- No ignores el ciclo de venta actual — el proceso nuevo tiene que ser viable desde el primer día, no una utopía.
- No definas cadencias idénticas para todos los tipos de oportunidad — proporcionalidad al valor.
- No avances a measurement-framework sin confirmación del consultor.
