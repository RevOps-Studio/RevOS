---
name: sales-conversion-design
description: >
  Usar cuando el consultor necesite diseñar el sistema de conversión entre marketing y comercial: handoff,
  SLAs, cualificación, routing, seguimiento, roles y responsabilidades. Es el puente entre el motor de
  demanda y el proceso comercial. Activar siempre después de growth-system-design y antes de
  execution-roadmap-builder. También activar si el consultor pide "diseña el handoff", "cómo se convierten
  los leads", "proceso entre marketing y ventas" o "cualificación y enrutamiento".
---

# Sales Conversion Design

## Propósito

Este skill diseña el sistema de conversión entre marketing y comercial: cómo un lead generado por el motor de demanda se transforma en una oportunidad comercial cualificada, quién hace qué en cada momento, con qué criterios y en qué plazos.

Es la pieza que resuelve una de las patologías más comunes de las empresas B2B: marketing genera leads que ventas no trabaja, ventas se queja de la calidad, marketing acusa a ventas de no seguir, y nadie tiene visibilidad de lo que realmente pasa entre la captura y la primera reunión. Este skill cierra ese hueco con reglas explícitas.

## Posición en el pipeline

**Requiere:** Growth System Design v1 (obligatorio), Positioning & Messaging, Revenue Diagnostic.

**Produce:** Sales Conversion Design v1 en Markdown. Documento que define handoff, SLAs, cualificación, y alimenta el execution-roadmap-builder y el sales-process-design.

**Siguiente skill:** execution-roadmap-builder (prioriza y calendariza todo el sistema diseñado).

## Principios de ejecución

**Sistema, no acuerdo.** El handoff entre marketing y comercial no es un acuerdo entre dos equipos — es un sistema con reglas, SLAs, escalados y visibilidad compartida. Si solo es un acuerdo, se rompe al primer mes.

**Cualificación con criterios explícitos.** Los criterios de cualificación (MQL, SQL, SAL u otra nomenclatura) tienen que estar articulados en términos verificables — no "encaja con el ICP" sino "empresa entre X y Y empleados, sector Z, posición W del decisor".

**Tiempos medibles.** Todos los handoffs tienen SLA de tiempo. Un lead caliente recibido por marketing el viernes a las 18:00 no puede estar sin contactar hasta el lunes. Los SLAs están en horas, no en "lo antes posible".

**Roles claros.** Cada etapa del proceso de conversión tiene un dueño nominal. Si no hay dueño, no hay proceso. Si dos personas son dueñas, nadie es dueño.

**Visibilidad compartida.** Marketing y comercial trabajan sobre la misma vista de datos. No dos dashboards. No dos definiciones de "lead cualificado". Una sola fuente de verdad.

**Realismo dado el equipo actual.** El sistema propuesto tiene que funcionar con el equipo actual. Si requiere roles que no existen, se explicita como dependencia — no se asume.

**Lenguaje.** Castellano. Registro ejecutivo directo. Vocabulario: lead, cualificación, handoff, pipeline, oportunidad, SLA, routing, lifecycle, MQL, SQL. Evitar: "nutrir al lead", "calentar pipelines", "alineación", "sinergias comercial-marketing".

**Convenciones v4.1 — **Precondición**: antes de producir, lee `00 Sistema/[Cliente] - Registro` y detente si falta fase 0, si el presupuesto de revisión de este entregable está agotado sin cambio tramitado por /revos:cambio, o si el cierre de fase anterior exigía un system-qa aún no APTO. **Etiquetado**: cada [FALTA DATO] se clasifica al detectarse como bloqueante (impide una decisión de este entregable) o no bloqueante. **Presupuesto**: 2 ciclos de revisión de calidad por entregable — solo consumen ciclo los cambios nacidos del juicio sobre lo escrito; las incorporaciones de información nueva (aportada por cliente o consultor, o medida por el sistema) no consumen ciclo y generan versión y entrada en el Backlog si el entregable ya está registrado. Agotado el presupuesto, los [FALTA DATO] no bloqueantes se convierten en [ASUNCIÓN: valor asumido + criterio falsable] y el sistema avanza; solo los bloqueantes detienen y se escalan de inmediato. **Resumen para el consultor**: enumera los bloqueantes y lo relevante — nunca recuentos totales (el recuento es chequeo mecánico de system-qa sobre el documento terminado). **Cierre**: todo [FALTA DATO] heredado sale con disposición explícita — resuelto, reasignado a la primera skill no ejecutada que lo necesite, o declinado con motivo. Datos de CRM conectado: [DATO CRM: fuente, fecha]. Referencia completa: skills/revos-orchestrator/references/convenciones.md del plugin revos.

## Proceso

**Paso 1 — Análisis del estado actual.**
Revisa knowledge base y diagnostic: cómo se pasan hoy los leads de marketing a comercial (si es que se pasan), qué criterios se usan, quién hace qué, dónde se pierden. Este es el baseline.

**Paso 2 — Mapeo del flujo ideal.**
Dibuja el flujo desde que un lead entra al sistema (output del motor de demanda) hasta que se convierte en oportunidad cualificada en pipeline. Cada nodo es una etapa con dueño y criterio.

**Paso 3 — Definición de estados del lead.**
Define los estados del lifecycle con precisión: por ejemplo Subscriber → Lead → MQL → SAL → SQL → Oportunidad. Para cada estado: definición verificable, criterios de entrada, criterios de salida, dueño.

**Paso 4 — Diseño de cualificación.**
Define los criterios de cualificación en cada nivel. Distingue entre cualificación de fit (¿coincide con ICP?) y cualificación de intent (¿muestra señales de compra?). Establece modelo de scoring si aplica.

**Paso 5 — SLAs y routing.**
Define SLAs por cada handoff: cuánto tiempo tiene cada etapa. Define routing: qué lead va a qué comercial según criterio (territorio, vertical, tamaño, idioma).

**Paso 6 — Bucles y recuperación.**
Diseña los bucles: qué pasa con un lead que marketing pasa pero comercial descarta (¿vuelve a nurturing?). Qué pasa con un lead que no avanza en N días. Qué pasa con leads dormidos.

**Paso 7 — Instrumentación mínima.**
Lista qué necesita el stack del cliente para que este sistema sea visible y medible. No es el stack completo — es el mínimo que permite operar el sistema.

**Paso 8 — Revisión de coherencia.**
Verifica: ¿los criterios de cualificación son coherentes con el ICP del positioning? ¿el volumen esperado del growth system es absorbible por el equipo comercial declarado? ¿los SLAs son realistas dada la capacidad del equipo?

## Template de output

Produce el output siguiendo exactamente esta estructura.

---

# Sales Conversion Design — [NOMBRE EMPRESA]
*RevOS Design · Versión 1.0 · [Fecha]*

---

## 1. Sumario ejecutivo
*[Máximo 250 palabras. Estado actual del handoff, diseño propuesto en una frase, decisiones clave requeridas, condiciones para que funcione.]*

---

## 2. Estado actual del handoff
[Descripción breve y honesta de cómo se pasan hoy los leads — qué funciona, qué no, dónde se pierden. Basado en el diagnóstico.]

---

## 3. Estados del lifecycle

### 3.1 Definición de estados
*[Listado de los estados que un prospecto atraviesa, desde captura hasta oportunidad cualificada.]*

**Subscriber / Lead frío**
- Definición: [Criterio verificable]
- Criterio de entrada: [Qué lo ubica aquí]
- Criterio de salida: [Qué lo mueve al siguiente estado]
- Dueño: [Marketing / Comercial / Automatizado]

**MQL (Marketing Qualified Lead)**
- Definición: [Criterio]
- Criterio de entrada: [Qué combinación de fit + intent lo convierte en MQL]
- Criterio de salida: [Qué lo mueve a SAL o a descarte]
- Dueño: [Marketing]

**SAL (Sales Accepted Lead)**
- Definición: [Criterio]
- Criterio de entrada: [Qué tiene que verificar comercial para aceptarlo]
- Criterio de salida: [Qué lo convierte en SQL o lo devuelve a marketing]
- Dueño: [Comercial — rol específico]

**SQL (Sales Qualified Lead)**
- Definición: [Criterio]
- Criterio de entrada: [Qué señales de intent + fit + timing califican]
- Criterio de salida: [Qué lo mueve a oportunidad]
- Dueño: [Comercial]

**Oportunidad**
- Definición: [Criterio]
- Criterio de entrada: [Propuesta comercial discutible, timing claro, BANT o equivalente]
- Dueño: [Comercial]

*[La nomenclatura puede adaptarse al cliente — lo importante es que haya estados definidos y verificables.]*

---

## 4. Cualificación

### 4.1 Criterios de fit
[Qué define que un lead encaja con el ICP — criterios verificables que tanto marketing como comercial pueden aplicar con consistencia]

### 4.2 Criterios de intent
[Qué señales indican que un lead está en el mercado — eventos, comportamientos, respuestas]

### 4.3 Modelo de scoring (si aplica)
[Si tiene sentido un modelo de scoring para el cliente, definirlo con criterios y umbrales. Si no tiene sentido para la escala del cliente, decirlo explícitamente.]

### 4.4 Criterios de descarte
[Qué hace que un lead sea descartado activamente — no pasado a nurturing, descartado]

---

## 5. SLAs de handoff

| Handoff | Qué pasa | SLA | Dueño del SLA |
|---------|----------|-----|---------------|
| MQL generado | Marketing notifica a comercial | Inmediato (automatizado) | Marketing |
| MQL → Primer contacto | Comercial contacta | < X horas hábiles | Comercial asignado |
| MQL → Aceptación/Rechazo | Comercial acepta como SAL o devuelve | < Y días hábiles | Comercial asignado |
| SAL → SQL | Comercial verifica BANT | < Z días hábiles | Comercial asignado |
| Lead devuelto | Marketing recoge y reactiva nurturing | < 48h | Marketing |

*[Los tiempos concretos los propone el skill dado el contexto — no son valores por defecto.]*

---

## 6. Routing

### 6.1 Criterios de asignación
[Cómo se decide qué comercial trabaja qué lead — territorio, vertical, tamaño, idioma, producto]

### 6.2 Reglas de round-robin o asignación directa
[Cuándo se usa round-robin y cuándo asignación directa a un comercial]

### 6.3 Reasignación
[Qué pasa si un comercial no responde en SLA, está de baja, o se considera que el lead encaja mejor con otro perfil]

---

## 7. Bucles y recuperación

### 7.1 Lead devuelto por comercial
[Qué pasa con un lead que comercial rechaza como SAL — vuelve a marketing, se etiqueta, entra en nurturing específico]

### 7.2 Lead estancado
[Qué pasa con un lead que no avanza después de N días en un estado — acciones automáticas, revisión manual, descarte]

### 7.3 Lead dormido
[Qué pasa con leads que cumplieron fit pero no intent — programa de nurturing de largo plazo con frecuencia y contenido específicos]

### 7.4 Lead reactivado
[Qué pasa con un lead que vuelve a mostrar intent después de meses — re-evaluación de fit, re-cualificación, re-asignación]

---

## 8. Roles y responsabilidades

### 8.1 Rol: Responsable de MQL (Marketing)
**Responsabilidades:** [Lista]
**KPIs:** [3-5 KPIs]

### 8.2 Rol: SDR / BDR / Inside Sales (si aplica)
**Responsabilidades:** [Lista]
**KPIs:** [3-5 KPIs]

### 8.3 Rol: Account Executive / Comercial senior
**Responsabilidades:** [Lista]
**KPIs:** [3-5 KPIs]

### 8.4 Rol: RevOps / responsable del sistema (aunque sea a tiempo parcial)
**Responsabilidades:** [Mantener criterios, visibilidad de datos, SLAs, reporting]
**KPIs:** [3-5 KPIs]

*[Si algún rol no existe en el equipo actual, señalar como dependencia.]*

---

## 9. Instrumentación mínima

### 9.1 CRM
[Qué tiene que estar configurado en CRM para que el sistema sea visible — estados del lifecycle, campos de fit/intent, owner, timestamps de transición]

### 9.2 Automatización
[Qué automatizaciones son mínimas — notificaciones de handoff, alertas de SLA, nurturing básico]

### 9.3 Dashboards
[Qué 2-3 dashboards permiten operar el sistema — uno compartido de conversion funnel, uno de salud operativa]

### 9.4 Brechas detectadas en el stack actual
[Dónde el stack actual no soporta lo propuesto — con referencia al audit si existe, o como [FALTA DATO] si aún no se ha auditado]

---

## 10. Métricas clave del sistema

### 10.1 Métricas de conversión
[Tasas entre estados — MQL→SAL, SAL→SQL, SQL→Oportunidad, Oportunidad→Cierre]

### 10.2 Métricas de velocidad
[Tiempo medio en cada estado — alerta si el tiempo se alarga sistemáticamente]

### 10.3 Métricas de salud del sistema
[SLA cumplido %, leads devueltos %, leads sin contacto en SLA %, distribución por comercial]

### 10.4 Indicadores de alerta temprana
[Qué señales avisan de que el sistema se está rompiendo antes de que el pipeline lo refleje]

---

## 11. Implementación y adopción

### 11.1 Pre-requisitos antes de activar el sistema
[Qué tiene que estar listo antes de lanzar — configuración CRM, formación de equipo, definiciones acordadas]

### 11.2 Plan de adopción
[Cómo se introduce el sistema — en qué orden se activan las piezas, qué se mide en cada fase]

### 11.3 Riesgos de adopción
[Resistencias previsibles, puntos donde el sistema puede romperse, cómo mitigar]

---

## 12. Vacíos e hipótesis

**Información que falta:** [[FALTA DATO] — típicamente datos de conversión actual, capacidad real del equipo]
**Hipótesis críticas:** [[HIPÓTESIS]]
**Decisiones abiertas:** [Decisiones del cliente que bloquean implementación]

---

## Entrega

Cuando el diseño esté completo:

1. Presenta el output completo en Markdown.
2. Añade al final una sección **"Resumen para el consultor"** con:
   - Estados del lifecycle definidos (cuántos y cuáles)
   - SLAs más críticos (los 2-3 que determinan que el sistema funcione)
   - Roles requeridos y cuáles existen / faltan en el equipo actual
   - Brechas detectadas en el stack actual (alto nivel)
   - Nivel de confianza en que el equipo actual puede operar este sistema (1-5)
3. El contenido validado se guarda como `[Cliente] - Sales Conversion Design v1.md` en `01 Entregables`. El orquestador lo registra en el Registro. Siguiente skill: `execution-roadmap-builder`.

## Lo que NO debes hacer

- No definas estados del lifecycle sin criterios verificables — "el lead está caliente" no es un criterio.
- No propongas SLAs sin estimar la capacidad del equipo para cumplirlos.
- No diseñes un sistema que requiere RevOps full-time si el cliente declaró no tenerlo — hazlo explícito como dependencia.
- No ignores los leads dormidos — son la segunda fuente de pipeline más infravalorada en B2B.
- No propongas un scoring complejo para una empresa que maneja 100 leads al año — escalar el diseño al volumen.
- No generes el fichero final DOCX — este skill produce contenido validado en Markdown; el fichero final maquetado lo genera `/revos:entrega` según la preferencia de output registrada en fase 0.
- No avances a execution-roadmap-builder sin confirmación del consultor.
