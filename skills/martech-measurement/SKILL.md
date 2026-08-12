---
name: martech-measurement
description: >
  Usar cuando el consultor necesite definir la arquitectura tecnológica objetivo para medición integrada:
  cómo se conectan CRM + MAP + analítica + herramientas de venta para alimentar el measurement framework
  de forma fiable, con atribución, con data hygiene y con reporting automatizado. Activar dentro del tier
  Activation Complete, después de crm-blueprint-builder. También activar si el consultor pide
  "arquitectura de medición", "integraciones para reporting", "atribución" o "data layer".
---

# Martech & Measurement Architecture

## Propósito

Este skill produce la arquitectura tecnológica objetivo que hace posible medir lo definido en el measurement framework. Cubre: integraciones críticas entre CRM, MAP, analítica web y herramientas de ventas; modelo de atribución; reglas de tracking; flujos de datos hacia reporting; gobernanza del dato.

Es el puente entre la aspiración del measurement framework ("quiero medir pipeline influido por contenido") y la realidad operativa ("con qué UTMs, qué evento registramos en GA4, qué propiedad en HubSpot y qué regla de atribución").

## Posición en el pipeline

**Requiere:** Measurement Framework, Martech Stack Audit, CRM Blueprint.

**Produce:** Martech & Measurement Architecture v1 en Markdown + diagramas textuales de flujos. Alimenta reporting-operating-system y exec-deliverables.

**Siguiente skill:** los opcionales de Activation contratados, si los hay (`media-plan-builder`, `content-calendar-builder`, `conversion-playbook-builder`, `reporting-operating-system`); después `system-qa` — QA de cierre de Activation, obligatorio — y finalmente `exec-deliverables`.

## Principios de ejecución

**Atribución con criterio declarado.** No existe el modelo de atribución perfecto. Se elige uno (first-touch, last-touch, multi-touch lineal, W-shape, data-driven) con criterio argumentado y se documenta. Las decisiones se toman consistentemente con ese modelo.

**UTMs gobernadas.** El tracking de campañas exige convenciones estrictas de UTMs (source, medium, campaign, content, term) con tabla maestra que gobierna qué valores son válidos. Sin esto, todo reporting de canales miente.

**Fuente única de verdad por métrica.** Para cada métrica del measurement framework, se asigna una y solo una fuente oficial. Los conflictos entre sistemas se resuelven definiendo jerarquía.

**Integraciones con dueño.** Cada integración crítica tiene un responsable que la mantiene y un proceso de verificación (al menos mensual) de que sigue funcionando. Las integraciones rotas son la primera causa de decisiones equivocadas.

**Data hygiene continua.** El sistema no se configura una vez y ya está. Se define cadencia de limpieza, auditoría y validación. Sin esto, el dato se degrada trimestre a trimestre.

**Reporting automatizado antes que manual.** Cualquier reporte que se hace más de dos veces al mes se automatiza. El equipo no debería copiar datos a mano en presentaciones.

**Privacidad y consentimiento by design.** GDPR, consentimiento de cookies, retención de datos personales — se diseña desde el inicio, no como parche.

Convenciones v4.1 — **Precondición**: antes de producir, lee `00 Sistema/[Cliente] - Registro` y detente si falta fase 0, si el presupuesto de revisión de este entregable está agotado sin cambio tramitado por /revos:cambio, o si el cierre de fase anterior exigía un system-qa aún no APTO. **Etiquetado**: cada [FALTA DATO] se clasifica al detectarse como bloqueante (impide una decisión de este entregable) o no bloqueante. **Presupuesto**: 2 ciclos de revisión de calidad por entregable — solo consumen ciclo los cambios nacidos del juicio sobre lo escrito; las incorporaciones de información nueva (aportada por cliente o consultor, o medida por el sistema) no consumen ciclo y generan versión y entrada en el Backlog si el entregable ya está registrado. Agotado el presupuesto, los [FALTA DATO] no bloqueantes se convierten en [ASUNCIÓN: valor asumido + criterio falsable] y el sistema avanza; solo los bloqueantes detienen y se escalan de inmediato. **Resumen para el consultor**: enumera los bloqueantes y lo relevante — nunca recuentos totales (el recuento es chequeo mecánico de system-qa sobre el documento terminado). **Cierre**: todo [FALTA DATO] heredado sale con disposición explícita — resuelto, reasignado a la primera skill no ejecutada que lo necesite, o declinado con motivo. Datos de CRM conectado: [DATO CRM: fuente, fecha]. Referencia completa: skills/revos-orchestrator/references/convenciones.md del plugin revos.

**Lenguaje.** Castellano. Registro ejecutivo directo. Vocabulario: atribución, UTM, tracking, data layer, consentimiento, API, webhook, source of truth, data governance, data warehouse (si aplica). Evitar: "data-driven" sin concreción, "360 view", "inteligencia artificial" como palabra de relleno.

## Proceso

**Paso 1 — Lectura de inputs.**
Measurement framework (qué hay que medir), CRM blueprint (dónde se almacena la verdad comercial), martech audit (qué tenemos hoy y qué gaps hay).

**Paso 2 — Mapeo métrica → fuente.**
Para cada métrica del measurement framework, asigna la fuente única que la produce. Si la métrica requiere combinar datos de dos sistemas, define cuál manda y cómo se enriquece.

**Paso 3 — Modelo de atribución.**
Elige el modelo. Argumenta por qué. Documenta ventanas de atribución (30/60/90 días) y cómo se tratan los solapes entre canales.

**Paso 4 — Gobernanza de UTMs.**
Diseña la tabla maestra de UTMs: valores válidos de source, medium, campaign; convenciones de nomenclatura; responsables de generar UTMs. Incluye ejemplos reales.

**Paso 5 — Eventos de tracking web.**
Lista los eventos críticos a trackear (envío de formulario, clic en CTA, descarga, visualización de pricing, etc.) con su parametrización y en qué sistema se registran.

**Paso 6 — Integraciones críticas.**
Documenta cada integración: sistemas origen/destino, tipo (API, webhook, iPaaS), frecuencia (tiempo real, horaria, diaria), dato que transfiere, dueño, proceso de verificación.

**Paso 7 — Flujos de datos hacia reporting.**
De cada sistema al reporting final: qué pasa directamente, qué pasa por herramienta intermedia (data warehouse, BI), qué transformaciones se aplican. Diagrama textual.

**Paso 8 — Consentimiento, privacidad y retención.**
Modelo de consent (banner, categorías), tratamiento de datos personales, retención por tipo de dato, proceso de ejercicio de derechos.

**Paso 9 — Data hygiene.**
Cadencia de limpieza, responsables, criterios de deduplicación, validación periódica de integraciones, monitorización de fallos.

**Paso 10 — Plan de implementación.**
Orden de configuración, dependencias, ventanas de pruebas, criterios de aceptación.

**Paso 11 — Revisión de coherencia.**
¿Cada métrica del framework tiene fuente asignada? ¿El modelo de atribución es coherente con el ciclo de venta? ¿Las integraciones críticas tienen dueño? ¿El consentimiento está contemplado?

## Template de output

Produce el output siguiendo exactamente esta estructura.

---

# Martech & Measurement Architecture — [NOMBRE EMPRESA]
*RevOS Activation Complete · Versión 1.0 · [Fecha]*

---

## 1. Sumario ejecutivo
*[Máximo 250 palabras. Modelo de atribución elegido, número de integraciones críticas, convenciones de UTM, gaps de tracking, dependencias de implementación.]*

---

## 2. Contexto

### 2.1 Alcance
[Qué cubre esta arquitectura y qué queda fuera]

### 2.2 Fuentes de referencia
[Measurement Framework, CRM Blueprint, Martech Audit]

### 2.3 Principios aplicados
[Síntesis de los principios de medición]

---

## 3. Modelo de atribución

### 3.1 Modelo elegido
[Ej. multi-touch lineal con crédito a first-touch y last-touch en mayor peso]

### 3.2 Justificación
[Por qué este modelo y no otro — según ciclo de venta, cantidad de touches, peso canales]

### 3.3 Ventanas de atribución
[30/60/90 días — por canal y por etapa]

### 3.4 Reglas de resolución de conflictos
[Qué hacer cuando dos canales reclaman la misma oportunidad]

### 3.5 Limitaciones del modelo
[Qué no captura — y cómo mitigarlo]

---

## 4. Fuente única de verdad por métrica

### 4.1 Tabla métrica → fuente
| Métrica | Fuente oficial | Integraciones que la alimentan | Quién manda si hay conflicto |
|---------|----------------|--------------------------------|------------------------------|
| [Métrica 1] | [Sistema] | [Lista] | [Sistema] |

### 4.2 Dependencias cruzadas
[Métricas que requieren combinación — cómo se resuelven]

---

## 5. Gobernanza de UTMs

### 5.1 Convenciones
**Formato:** [Ej. kebab-case minúsculas, sin tildes]
**Campos obligatorios:** source, medium, campaign
**Campos opcionales:** content, term

### 5.2 Tabla maestra de valores válidos
| Campo | Valores permitidos | Ejemplo |
|-------|-------------------|---------|
| source | linkedin, google, email, referral, direct, ... | linkedin |
| medium | organic, cpc, email, social, referral, ... | cpc |
| campaign | [formato: [tipo]-[tema]-[mes]] | paid-whitepaper-2026-04 |

### 5.3 Responsables de generación de UTMs
[Quién crea, quién aprueba, dónde se registran]

### 5.4 Validación continua
[Cómo se detectan UTMs mal puestos y se corrigen]

---

## 6. Eventos de tracking web

### 6.1 Eventos críticos
| Evento | Descripción | Parámetros | Sistema de registro |
|--------|-------------|------------|---------------------|
| form_submit | Envío de formulario | form_id, form_name | GA4 + CRM + MAP |
| demo_request | CTA demo | page_path, button_id | GA4 + CRM |
| pricing_view | Ver página pricing | time_on_page | GA4 |
| ... |

### 6.2 Implementación técnica
[GTM, scripts, data layer, webhooks — nivel de detalle suficiente para que desarrollo lo implemente]

---

## 7. Integraciones críticas

### 7.1 CRM ↔ MAP
**Tipo:** [API nativa / iPaaS / webhook]
**Frecuencia:** [Tiempo real / cada X minutos]
**Dato que transfiere:** [Contactos, actividad, cambios de etapa]
**Dirección:** [Bidireccional / unidireccional]
**Dueño:** [Rol]
**Verificación:** [Proceso y cadencia]

### 7.2 Formulario web ↔ CRM
[Misma estructura]

### 7.3 Analítica ↔ CRM
[Misma estructura]

### 7.4 CRM ↔ Reporting / BI
[Misma estructura]

### 7.5 Otras integraciones
[Lista]

---

## 8. Flujo de datos hacia reporting

### 8.1 Diagrama de flujo
[Representación textual ordenada: origen → transformación → destino → uso]

### 8.2 Herramientas intermedias
[Data warehouse si existe, BI, herramienta de dashboard]

### 8.3 Transformaciones aplicadas
[Normalización de valores, enriquecimiento, cálculos]

### 8.4 Latencia total por métrica
[Cuánto tarda un dato en aparecer en el dashboard desde que ocurre el evento]

---

## 9. Privacidad, consentimiento y retención

### 9.1 Modelo de consentimiento
[Banner, categorías, granularidad, gestión del consentimiento, proveedor si aplica]

### 9.2 Datos personales gestionados
[Qué categorías, con qué finalidad, base legal]

### 9.3 Políticas de retención
[Por tipo de dato — contacto activo, contacto inactivo, oportunidad ganada/perdida, log de actividad]

### 9.4 Ejercicio de derechos
[Proceso para atender solicitudes de acceso/rectificación/supresión]

---

## 10. Data hygiene

### 10.1 Cadencia de limpieza
[Diaria, semanal, mensual, trimestral — qué se limpia en cada ciclo]

### 10.2 Responsables
[RevOps Admin, dueños de sistemas]

### 10.3 Criterios de deduplicación
[Ya definidos en CRM Blueprint — se heredan]

### 10.4 Monitorización de fallos de integración
[Alertas automáticas, revisión semanal, escalado]

---

## 11. Plan de implementación

### 11.1 Dependencias
[Qué tiene que estar antes de qué]

### 11.2 Fases
[Fase 1: UTMs y tracking web. Fase 2: integraciones CRM-MAP. Fase 3: reporting automático. Fase 4: BI avanzado.]

### 11.3 Criterios de aceptación por fase
[Qué se valida para dar por cerrada cada fase]

### 11.4 Calendario orientativo
[Semanas 1-2, 3-4, 5-8, 9-12]

---

## 12. Riesgos y mitigaciones

[Riesgos técnicos y organizativos: resistencia al cambio, calidad del dato histórico, dependencia de integraciones frágiles — con mitigaciones propuestas]

---

## 13. Vacíos e hipótesis

**Información que falta:** [[FALTA DATO]]
**Hipótesis críticas:** [[HIPÓTESIS]]
**Decisiones abiertas del cliente:** [Modelo de atribución, proveedor de consentimiento, ventanas de atribución]

---

## Entrega

Cuando la arquitectura de medición esté completa:

1. Presenta el output completo en Markdown.
2. Añade al final una sección **"Resumen para el consultor"** con:
   - Modelo de atribución elegido
   - Las integraciones críticas documentadas, listadas — sin recuento
   - Gaps bloqueantes de tracking
   - Fases de implementación y duración total orientativa
   - Nivel de confianza en la arquitectura (1-5)
3. El contenido validado se guarda como `[Cliente] - Martech Measurement v1.md` en `01 Entregables`. El orquestador lo registra en el Registro. Siguiente skill: los opcionales contratados si los hay; después `system-qa` (cierre de Activation) y `exec-deliverables`.

## Lo que NO debes hacer

- No propongas más de un modelo de atribución en paralelo — hay que elegir uno.
- No definas UTMs sin tabla maestra de valores — los UTMs libres terminan en caos.
- No documentes integraciones sin dueño ni proceso de verificación.
- No ignores privacidad y consentimiento — no es opcional en UE.
- No asumas que el dato actual está limpio — en la mayoría de casos no lo está.
- No avances a exec-deliverables sin confirmación del consultor.
