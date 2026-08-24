---
name: martech-stack-audit
description: >
  Usar cuando el consultor necesite auditar el stack tecnológico actual del cliente (CRM, MAP, analítica,
  herramientas de ventas, contenido, etc.): qué tiene, cómo lo usa, qué solapa, qué falta, qué brechas
  bloquean el sistema diseñado. Activar al inicio del tier Activation Complete, antes de crm-blueprint-builder.
  También activar si el consultor pide "auditar el stack", "revisar herramientas actuales" o "detectar brechas
  tecnológicas".
---

# Martech Stack Audit

## Propósito

Este skill produce una auditoría operativa del stack actual del cliente: qué herramientas tiene, para qué las usa, qué nivel de uso/saturación, qué integra con qué, dónde hay solapes redundantes, qué falta para soportar el sistema diseñado en Design.

No es una comparativa de vendors ni una lista genérica de "herramientas recomendadas". Es un diagnóstico del stack real, contrastado con los requerimientos derivados del growth system, sales process, channel strategy, content strategy y measurement framework.

## Posición en el pipeline

**Requiere:** Measurement Framework + todos los outputs de Design Essentials (Positioning, Growth System, Sales Conversion, Execution Roadmap). El criterio de evaluación de este audit *es* el sistema diseñado: sin Design cerrado no hay con qué medir el fit de una herramienta.

**Consume, si existe:** la recolección temprana del stack producida en `knowledge-base-builder` (inventario, costes, flujos de datos, higiene del CRM) y guardada en `02 Anexos`. Compruébalo antes de pedir nada al cliente.

**Produce:** Martech Stack Audit v1 en Markdown. Alimenta crm-blueprint-builder, crm-selection (si procede) y martech-measurement.

**Siguiente skill:** `crm-selection` si el vendor está por decidir y el módulo está contratado; si no, `crm-blueprint-builder`.

## Principios de ejecución

**Stack al servicio del sistema.** El diagnóstico del stack no es absoluto — es relativo al sistema diseñado. Una herramienta puede estar bien usada para un objetivo pasado y ser inservible para los nuevos. El juicio se hace contra los requerimientos nuevos.

**Uso real > suscripción contratada.** Muchas herramientas están contratadas y no usadas (o usadas al 10%). El audit distingue entre lo contratado y lo operativo.

**Integraciones primero.** En B2B la mayoría de fugas tecnológicas están en las integraciones (CRM ↔ MAP, CRM ↔ analítica, formularios ↔ CRM), no en las herramientas individuales. El audit examina los flujos de datos con la misma seriedad que las herramientas.

**Coste total ≠ licencias.** El coste real de una herramienta incluye licencias + horas de operación + coste de oportunidad de lo que no se hace por tenerla mal configurada. Se estiman los tres.

**Recomendación tripartita.** Para cada herramienta: mantener / renegociar / sustituir — con argumento. Nunca "depende".

**Stack mínimo funcional.** La recomendación final apunta a un stack tan simple como sea posible para soportar el sistema — no más. Añadir herramientas sin necesidad es deuda operativa.

Convenciones v4.3 — **Doctrina de avance**: un [FALTA DATO] es no bloqueante por defecto; solo bloquea si cumple un criterio de la definición cerrada (inversión de tesis · irreversibilidad ante el cliente · imposibilidad material), y la carga de la prueba es del bloqueo. En primera pasada, si la fuente del dato no estará disponible antes del checkpoint, escribe directamente [ASUNCIÓN: valor + criterio falsable] — un v1 con asunciones declaradas es un entregable válido. Máximo 3 preguntas abiertas al consultor por entregable, escaladas agrupadas al cierre del paso, nunca una a una en mitad de la producción. **Lenguaje calibrado**: la asertividad es del entregable, no de la conversación; las conclusiones mayores declaran su confianza (alta: dato medido/CRM · media: declarado por el cliente · baja: inferencia), las consecuencias se formulan condicionadas — nunca proféticas — y el contraste retórico ("No es X. Es Y.") solo es admisible con evidencia de ambos lados. **Precondición**: antes de producir, lee `00 Sistema/[Cliente] - Registro` y detente si falta fase 0, si hay una intervención sin tramitar por /revos:cambio con presupuesto agotado, o si el cierre de fase anterior exigía un system-qa aún no APTO. **Resumen para el consultor**: enumera lo relevante — nunca recuentos totales. Mecánica completa (dos contadores, propagación en lote, disposición de huecos, etiquetas): skills/revos-orchestrator/references/convenciones.md del plugin revos.

**Lenguaje.** Castellano. Registro ejecutivo directo. Vocabulario: stack, integración, flujo de datos, saturación de uso, licenciamiento, TCO (total cost of ownership), brecha. Evitar: "ecosistema martech", "transformación digital", "stack de clase mundial".

## Proceso

**Paso 1 — Inventario completo del stack actual.**
Primero comprueba si existe recolección temprana del stack en `02 Anexos` (la produce `knowledge-base-builder`). Si existe: úsala como base, verifica que su fecha sigue siendo válida y complétala solo en lo que falte. Si no existe, constrúyela ahora a partir del intake, brief y documentación aportada. En ningún caso vuelvas a pedir al cliente datos que ya están recogidos. Lista todas las herramientas. Para cada una: categoría (CRM, MAP, analítica, SEO, ABM, telefonía, reuniones, contenido, diseño, gestión, ops, finanzas), plan contratado, número de licencias, coste mensual, fecha de renovación si se conoce, responsable interno. Si falta información, [FALTA DATO].

**Paso 2 — Datos reales de CRM (condicional).** Si el Registro del proyecto registra un CRM conectado, lanza el agente crm-analyst del plugin: además del funnel, sus hallazgos de higiene (deals sin actividad, fechas vencidas, campos vacíos, duplicados) son evidencia directa para este audit. Incorpóralos con etiqueta [DATO CRM: fuente, fecha].

**Paso 3 — Mapeo de uso real.**
Para cada herramienta: qué se hace con ella realmente, quién la usa, con qué frecuencia, nivel de saturación (% de funcionalidades usadas), integraciones activas. Muchas veces el dato es estimativo — señálalo con [HIPÓTESIS].

**Paso 4 — Mapeo de flujos de datos.**
Diagrama de los flujos: dónde entra el dato, por dónde pasa, dónde termina. Identifica puntos de rotura, duplicaciones, sistemas que no hablan entre sí.

**Paso 5 — Requerimientos derivados del sistema diseñado.**
Lista qué requerimientos tecnológicos impone el sistema: qué tiene que poder hacer el CRM para soportar el sales process diseñado, qué integraciones hace falta para el measurement framework, qué herramientas de contenido para el content plan, etc.

**Paso 6 — Diagnóstico por herramienta.**
Para cada herramienta existente: fit con el sistema nuevo (alto / medio / bajo), nivel de aprovechamiento actual, integraciones críticas funcionando o rotas, coste vs. valor. Recomendación: mantener / renegociar / sustituir.

**Paso 7 — Detección de brechas.**
Qué necesita el sistema diseñado que no está cubierto por el stack actual. Prioriza por criticidad: bloqueante / necesario / deseable.

**Paso 8 — Detección de solapes.**
Dos herramientas haciendo lo mismo. Propón consolidación donde aplique.

**Paso 9 — Estimación de TCO y movimientos.**
Coste actual del stack, coste propuesto, impacto en caja en los primeros 6-12 meses.

**Paso 10 — Revisión de coherencia.**
¿Todas las herramientas están diagnosticadas? ¿Las brechas se corresponden con lo que el sistema necesita? ¿La recomendación es operativa — el equipo puede ejecutar el cambio con realismo?

## Template de output

Produce el output siguiendo exactamente esta estructura.

---

# Martech Stack Audit — [NOMBRE EMPRESA]
*RevOS Activation Complete · Versión 1.0 · [Fecha]*

---

## 1. Sumario ejecutivo
*[Máximo 250 palabras. Tamaño del stack actual, coste mensual, brechas bloqueantes, solapes detectados, propuesta de consolidación, impacto económico orientativo.]*

---

## 2. Alcance del audit

### 2.1 Fuentes utilizadas
[Intake, brief, entrevistas, documentación, acceso directo a herramientas, datos de CRM conectado — [DATO CRM: fuente, fecha] si aplica]

### 2.2 Limitaciones
[Qué información falta o está parcial — [FALTA DATO]]

### 2.3 Sistema de referencia (requerimientos)
[Síntesis breve de los requerimientos que impone el sistema diseñado en Design]

---

## 3. Inventario del stack actual

### 3.1 Vista global
| Categoría | Herramienta | Plan | Licencias | Coste/mes | Renovación | Responsable |
|-----------|-------------|------|-----------|-----------|------------|-------------|
| CRM | [Nombre] | [Plan] | [N] | [€] | [Fecha] | [Rol] |
| MAP | [...] | [...] | [...] | [...] | [...] | [...] |
| Analítica | [...] | | | | | |
| SEO | [...] | | | | | |
| ABM / Outreach | [...] | | | | | |
| Reuniones / Scheduling | [...] | | | | | |
| Telefonía / Video | [...] | | | | | |
| Contenido / Diseño | [...] | | | | | |
| Gestión / Ops | [...] | | | | | |

### 3.2 Coste total actual del stack
[Suma mensual + anual. Distribución por categoría.]

---

## 4. Uso real de cada herramienta

### 4.1 Herramienta 1 — [Nombre]
**Categoría:** [CRM / MAP / ...]
**Uso real:** [Qué se hace con ella]
**Usuarios activos:** [N de los N licenciados]
**Frecuencia de uso:** [Diaria / Semanal / Puntual]
**Saturación de funcionalidades:** [% estimado — marcar [HIPÓTESIS] si procede]
**Integraciones activas:** [Lista]
**Problemas detectados:** [Errores, fricciones, dolores reportados — hallazgos de higiene con [DATO CRM: fuente, fecha] si el CRM está conectado]

### 4.2 Herramienta 2 — [Nombre]
[Misma estructura]

*[Una por cada herramienta del inventario.]*

---

## 5. Flujos de datos

### 5.1 Flujo de leads (web → CRM)
[De dónde sale, qué pasos atraviesa, dónde termina, con qué enriquecimiento. Puntos de rotura.]

### 5.2 Flujo de actividad comercial (CRM → MAP / Analítica)
[Ídem]

### 5.3 Flujo de facturación / cliente (CRM → ERP / Finanzas)
[Ídem]

### 5.4 Flujo de medición (fuentes → reporting)
[De dónde se nutre el reporting actual y dónde rompe]

### 5.5 Diagrama global de flujos
[Representación textual o listada de las conexiones y roturas]

---

## 6. Requerimientos del sistema nuevo

### 6.1 Requerimientos CRM
[Campos, pipelines, reportes, automatizaciones — derivado de sales-process-design]

### 6.2 Requerimientos MAP / Marketing
[Segmentación, nurturing, puntuación — derivado de growth-system y channel-strategy]

### 6.3 Requerimientos de analítica y medición
[Derivados de measurement-framework]

### 6.4 Requerimientos de producción de contenido
[Derivados de content-discoverability]

### 6.5 Requerimientos comerciales operativos
[Telefonía, secuenciación, reuniones — derivados de sales-process]

---

## 7. Diagnóstico por herramienta

### 7.1 Tabla de diagnóstico
| Herramienta | Fit con sistema | Aprovechamiento | Integraciones | Coste vs. valor | Recomendación |
|-------------|-----------------|-----------------|---------------|-----------------|---------------|
| [Nombre] | Alto/Medio/Bajo | % | OK/Parcial/Roto | OK/Alto | Mantener/Renegociar/Sustituir |

### 7.2 Argumentos por herramienta
[Explicación de cada recomendación — una herramienta por párrafo]

---

## 8. Brechas detectadas

### 8.1 Brechas bloqueantes
[Lo que el sistema necesita y no está cubierto — bloquea ejecución]

### 8.2 Brechas necesarias
[Lo que hace falta pero puede esperar un trimestre]

### 8.3 Brechas deseables
[Mejoras de productividad no críticas]

---

## 9. Solapes detectados

[Herramientas que hacen lo mismo o parte de lo mismo. Propuesta de consolidación.]

---

## 10. Propuesta de stack objetivo

### 10.1 Stack recomendado
| Categoría | Herramienta propuesta | Acción | Coste/mes estimado |
|-----------|----------------------|--------|---------------------|
| CRM | [Actual/Nueva] | Mantener/Actualizar/Cambiar | [€] |
| ... |

### 10.2 Coste total propuesto
[Suma mensual + anual. Diferencia vs. stack actual.]

### 10.3 Secuencia de cambios
[Qué se hace primero, qué después, en qué meses, con qué dependencias]

---

## 11. Riesgos e impacto operativo

### 11.1 Riesgos de migración
[Lo que puede romperse durante los cambios]

### 11.2 Impacto en el equipo
[Qué capacitación, qué tiempo, qué recursos hacen falta]

### 11.3 Mitigaciones recomendadas
[Pilotos, rollouts por fases, backups de datos]

---

## 12. Vacíos e hipótesis

**Información que falta:** [[FALTA DATO]]
**Hipótesis críticas:** [[HIPÓTESIS]]
**Decisiones abiertas del cliente:** [Presupuesto disponible para cambios, tolerancia al riesgo, ventanas de migración]

---

## Entrega

Cuando el audit esté completo:

1. Presenta el output completo en Markdown.
2. Añade al final una sección **"Resumen para el consultor"** con:
   - Las herramientas del stack actual, listadas por categoría, con el coste mensual total
   - Las brechas bloqueantes, listadas — sin recuento
   - Las herramientas a sustituir, listadas con su motivo
   - Ahorro/coste neto orientativo del stack objetivo
   - Nivel de confianza en el diagnóstico (1-5)
3. El contenido validado se guarda como `[Cliente] - Martech Stack Audit v1.md` en `01 Entregables`. El orquestador lo registra en el Registro. Siguiente skill: `crm-selection` si el vendor está por decidir y el módulo está contratado; si no, `crm-blueprint-builder`.

## Lo que NO debes hacer

- No juzgues herramientas en abstracto — siempre contra los requerimientos del sistema nuevo.
- No recomiendes vendors específicos sin criterio — si hay que cambiar CRM, el skill `crm-selection` se encarga.
- No confundas suscripción con uso — separa siempre lo contratado de lo operativo.
- No añadas herramientas al stack solo porque "sería mejor tenerlas" — principio de stack mínimo funcional.
- No ignores las integraciones — suelen ser la raíz del problema.
- No avances a crm-blueprint-builder sin confirmación del consultor.
