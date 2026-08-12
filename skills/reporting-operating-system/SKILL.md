---
name: reporting-operating-system
description: >
  Usar cuando el consultor necesite diseñar la cadencia operativa de reporting y revisión
  del cliente: qué reportes se producen, para quién, con qué frecuencia, con qué formato,
  qué reunión los revisa y qué decisión desbloquea cada uno. Es el skill que convierte el
  measurement-framework (qué medir) en un sistema de reuniones, dashboards y rituales de
  gestión del revenue. Activar como skill opcional de Activation, siempre después de
  measurement-framework y martech-measurement. También activar si el consultor pide
  "cadencia de reporting", "ritmo operativo", "reuniones de revenue", "governance",
  "sistema de reporting" o "rituales de gestión".
---

# Reporting Operating System

## Propósito

Este skill diseña el sistema operativo de reporting del cliente: el conjunto de reuniones, dashboards y rituales que convierten las métricas del measurement-framework en decisiones repetibles. Define qué se mira cada semana, cada mes y cada trimestre, quién lo mira, en qué formato, con qué estructura de reunión y qué se decide al final. Cierra el ciclo: sin un sistema de reporting, las métricas son datos que nadie revisa.

No es un dashboard bonito. Es la arquitectura de reuniones y reportes que obliga al equipo a mirar el pipeline, el funnel y el motor de revenue con regularidad y a tomar decisiones con base en lo que ven.

## Posición en el pipeline

**Requiere:** Measurement Framework (métricas, fuentes, dueños), Martech Measurement (arquitectura técnica que alimenta los datos), Sales Process Design (estructura del pipeline), Execution Roadmap (iniciativas que hay que reportar).

**Produce:** Reporting Operating System v1 en Markdown validado. Los ficheros finales maquetados (DOCX + calendario operativo XLSX con reuniones, agendas, participantes y entregables) los genera `/revos:entrega` según la preferencia de output registrada en fase 0, siguiendo la especificación de estructura incluida en este skill.

**Siguiente skill:** `system-qa` (cierre de Activation) y después `exec-deliverables`, que consolida este sistema de reporting en el Handover.

## Principios de ejecución

**Decisión antes que dato.** Cada reporte existe para habilitar una decisión concreta. Si un reporte no lleva a ninguna decisión, se elimina. No se reportan métricas por completar un dashboard.

**Menos cadencias, más disciplina.** Pocas reuniones bien ejecutadas superan a muchas reuniones diluidas. El sistema típico: 1 semanal (operativa), 1 mensual (táctica), 1 trimestral (estratégica). Más de eso satura al equipo.

**Un dueño por reporte, un decisor por reunión.** Cada reporte tiene una persona que lo produce (dueño) y una persona que decide con él (decisor). Sin esos dos nombres, el reporte se muere por desuso.

**Formato estable, contenido vivo.** La estructura de cada reunión y cada reporte es siempre la misma. Lo que cambia son los números y las decisiones. Esto hace que el equipo sepa qué esperar y reduce la fricción semana a semana.

**Triage por excepciones, no por exhaustividad.** Las reuniones operativas no revisan todo el pipeline — revisan lo que se está moviendo fuera de lo esperado (deals estancados, etapas con tasa de conversión anómala, SLAs incumplidos). Revisar deal por deal cada semana mata el ritmo.

**Pre-work obligatorio.** Las reuniones se preparan antes. El reporte se comparte 24h antes. La reunión no es para descubrir los datos — es para interpretar y decidir sobre ellos.

**Actas cortas con decisiones.** Cada reunión termina con 3-5 decisiones documentadas (qué se decide, quién ejecuta, cuándo se revisa). Sin actas con decisiones, la cadencia se vuelve teatro.

**Métricas anti-vanidad.** Los reportes destacan métricas accionables (pipeline por etapa, velocidad, win rate, tiempo por etapa, cost per opportunity) por encima de métricas de vanidad (impresiones, visitas totales, followers).

**Convenciones v4.1 — **Precondición**: antes de producir, lee `00 Sistema/[Cliente] - Registro` y detente si falta fase 0, si el presupuesto de revisión de este entregable está agotado sin cambio tramitado por /revos:cambio, o si el cierre de fase anterior exigía un system-qa aún no APTO. **Etiquetado**: cada [FALTA DATO] se clasifica al detectarse como bloqueante (impide una decisión de este entregable) o no bloqueante. **Presupuesto**: 2 ciclos de revisión de calidad por entregable — solo consumen ciclo los cambios nacidos del juicio sobre lo escrito; las incorporaciones de información nueva (aportada por cliente o consultor, o medida por el sistema) no consumen ciclo y generan versión y entrada en el Backlog si el entregable ya está registrado. Agotado el presupuesto, los [FALTA DATO] no bloqueantes se convierten en [ASUNCIÓN: valor asumido + criterio falsable] y el sistema avanza; solo los bloqueantes detienen y se escalan de inmediato. **Resumen para el consultor**: enumera los bloqueantes y lo relevante — nunca recuentos totales (el recuento es chequeo mecánico de system-qa sobre el documento terminado). **Cierre**: todo [FALTA DATO] heredado sale con disposición explícita — resuelto, reasignado a la primera skill no ejecutada que lo necesite, o declinado con motivo. Datos de CRM conectado: [DATO CRM: fuente, fecha]. Referencia completa: skills/revos-orchestrator/references/convenciones.md del plugin revos.

**Lenguaje.** Castellano. Registro ejecutivo operativo. Vocabulario: reporting, cadencia, pipeline review, forecast, weekly, MBR (monthly business review), QBR (quarterly business review), pre-read, agenda, actas, decisiones, dueño, decisor. Evitar: "sesión de alineamiento", "check-in", "sync", "touchpoint" (en castellano), "visibilidad 360".

## Proceso

**Paso 1 — Lectura del sistema.**
Measurement-framework (métricas, fuentes, dueños, frecuencia), martech-measurement (dashboards disponibles, automatización del reporting), sales-process-design (etapas, criterios, volumen esperado), execution-roadmap (iniciativas en curso que hay que reportar). Extrae qué métricas son accionables a qué frecuencia.

**Paso 2 — Mapa de decisiones a habilitar.**
Lista las decisiones recurrentes que tiene que tomar cada rol: CEO (¿vamos a cumplir el año?), CRO/Director Comercial (¿el pipeline cubre el forecast del trimestre?), Marketing (¿los motores de demanda están generando oportunidades cualificadas?), Management Comercial (¿qué deals están en riesgo esta semana?), SDR/AE (¿en qué deals tengo que trabajar hoy?). Cada decisión → una cadencia que la habilita.

**Paso 3 — Diseño de la cadencia semanal.**
Pipeline review operativa del equipo comercial. Duración 45-60 min. Estructura típica: forecast vs. actual, deals en etapa final (movimientos), deals estancados >N días, SLAs de marketing→ventas, acciones de la semana. Participantes: director comercial + AEs + SDR lead. Pre-read: dashboard de pipeline 24h antes.

**Paso 4 — Diseño de la cadencia mensual.**
Monthly Business Review (MBR). Duración 90 min. Estructura: resultados mes (pipeline generado, cerrado, velocidad, win rate), funnel completo (MQL→SAL→SQL→cerrado), motores de demanda (qué funciona y qué no), iniciativas en curso del roadmap, decisiones del mes. Participantes: dirección + marketing + comercial. Pre-read: reporte MBR 48h antes.

**Paso 5 — Diseño de la cadencia trimestral.**
Quarterly Business Review (QBR). Duración 3h con pausas. Estructura: resultados Q vs plan, revisión de ICP y posicionamiento (¿seguimos vendiendo a quien dijimos?), revisión del motor (¿el sistema está funcionando como fue diseñado?), priorización del próximo Q, ajustes al roadmap. Participantes: C-level + heads de funciones. Pre-read: dossier QBR 1 semana antes.

**Paso 6 — Definición de dashboards.**
Qué dashboards existen, quién los consume, en qué herramienta viven (CRM, Looker Studio, Power BI, Notion). Para cada uno: audiencia, métricas, fuente, frecuencia de actualización, dueño. Tres tipos típicos: operativo (diario, para el equipo), táctico (semanal/mensual, para management), estratégico (mensual/trimestral, para dirección).

**Paso 7 — Reporting automatizado vs. reporting manual.**
Qué se automatiza (extracción de métricas del CRM, actualización de dashboards, alertas por SLA incumplido) y qué es análisis manual (interpretación, decisiones, QBR). Los reportes operativos semanales deben ser 90% automatizados; los QBR son 80% análisis manual.

**Paso 8 — Especificación del calendario XLSX para /revos:entrega.**
Tabla operativa con columnas: Cadencia (semanal/mensual/Q), Reunión, Día recurrente, Duración, Participantes, Dueño del pre-read, Decisor, Pre-read entregado a, Dashboard fuente, Decisiones tipo que habilita. Permite al cliente ver todo el sistema en una página. Este skill no genera el fichero — lo genera `/revos:entrega` a partir de esta especificación.

**Paso 9 — Rituales de onboarding y salida.**
Primer día: qué dashboards debe mirar un nuevo AE/SDR, qué reuniones asiste. Mantenimiento: quién revisa trimestralmente si la cadencia sigue siendo adecuada, cuándo se añade/elimina una reunión.

**Paso 10 — Especificación de entregables para /revos:entrega.**
Define la especificación de estructura que usará `/revos:entrega` para los ficheros finales: DOCX con el sistema completo (narrativa + plantillas de agenda + estructura de actas); XLSX con el calendario operativo editable — una hoja con todas las cadencias, participantes, pre-reads y decisiones; una hoja con dashboards; una hoja con alertas; una hoja con checklist de implementación.

**Paso 11 — Revisión de coherencia.**
¿Cada reunión habilita una decisión específica? ¿Cada reporte tiene dueño y decisor? ¿Las métricas vienen del measurement-framework? ¿Los dashboards usan la arquitectura de martech-measurement? ¿El total de horas de reuniones semanales es razonable (<4h/semana para el equipo comercial)? ¿Hay plantillas de agenda reales, no abstractas?

## Template de output

Produce el output siguiendo exactamente esta estructura.

---

# Reporting Operating System — [NOMBRE EMPRESA]
*RevOS Activation · Versión 1.0 · [Fecha]*

---

## 1. Sumario ejecutivo
*[Máximo 200 palabras. Cadencias diseñadas, dashboards operativos, carga de reuniones total del equipo, decisiones principales habilitadas. El consultor tiene que poder leerlo y saber exactamente cómo queda el ritmo operativo.]*

---

## 2. Filosofía del sistema

### 2.1 Principios
- Un reporte = una decisión
- Pocas cadencias, bien ejecutadas
- Pre-work obligatorio
- Actas con decisiones, no minutas
- Triage por excepciones

### 2.2 Carga total de reuniones
| Rol | Horas/semana en reporting |
|-----|---------------------------|
| CEO | [X] |
| Director Comercial | [X] |
| Marketing Lead | [X] |
| AE (cada uno) | [X] |
| SDR (cada uno) | [X] |

---

## 3. Mapa de decisiones y cadencias

### 3.1 Decisiones recurrentes por rol
| Rol | Decisión recurrente | Cadencia que la habilita |
|-----|---------------------|--------------------------|
| CEO | ¿Vamos a cumplir el año? | QBR + MBR |
| Director Comercial | ¿El pipeline cubre el forecast Q? | Weekly + MBR |
| Marketing Lead | ¿Los motores están generando oportunidades cualificadas? | MBR |
| Director Comercial + AEs | ¿Qué deals están en riesgo esta semana? | Weekly Pipeline Review |
| AE | ¿En qué deals trabajo hoy? | Daily dashboard + Weekly |

---

## 4. Cadencia semanal — Weekly Pipeline Review

### 4.1 Ficha
- **Duración:** 45-60 min
- **Día recurrente:** [Recomendado: lunes 10:00]
- **Participantes:** Director Comercial + AEs + SDR Lead
- **Dueño del pre-read:** Director Comercial (o CRM admin)
- **Decisor:** Director Comercial
- **Pre-read:** Dashboard de pipeline + listado de deals en etapa final, entregado 24h antes

### 4.2 Agenda tipo
1. Forecast de la semana vs. actual (5 min)
2. Deals en closing (movimientos, riesgos) (15 min)
3. Deals estancados >N días (revisión y acción) (10 min)
4. Top 5 deals del mes por AE (10 min)
5. Cumplimiento SLA marketing→ventas (5 min)
6. Acciones y bloqueos (10 min)

### 4.3 Métricas que se revisan
- Pipeline total por etapa
- Deals nuevos en la semana
- Deals cerrados (won/lost) con aprendizaje
- Velocidad por etapa
- Tasa de conversión entre etapas
- SLAs incumplidos

### 4.4 Decisiones tipo que habilita
- Qué deals escalar al Director
- Qué deals reactivar o descartar
- Qué AE necesita soporte esta semana
- Qué ajuste táctico hacer para cerrar el mes

### 4.5 Estructura de actas
| Campo | Contenido |
|-------|-----------|
| Decisiones | Máx. 5 |
| Acciones | Con dueño + fecha |
| Escalados | A qué reunión mensual |

---

## 5. Cadencia mensual — Monthly Business Review (MBR)

### 5.1 Ficha
- **Duración:** 90 min
- **Día recurrente:** [Recomendado: primer lunes del mes, 10:00]
- **Participantes:** CEO + Director Comercial + Marketing Lead + CRO (si aplica)
- **Dueño del pre-read:** Marketing Lead + Director Comercial (conjunto)
- **Decisor:** CEO
- **Pre-read:** Reporte MBR, entregado 48h antes

### 5.2 Agenda tipo
1. Resultados del mes vs. plan (15 min)
2. Funnel completo: MQL → SAL → SQL → Won (20 min)
3. Motores de demanda: performance y ajustes (20 min)
4. Iniciativas del roadmap: estado y bloqueos (15 min)
5. Forecast del próximo mes y trimestre (10 min)
6. Decisiones del mes (10 min)

### 5.3 Métricas que se revisan
- Pipeline generado en el mes (por motor de demanda)
- Pipeline cerrado ganado/perdido
- Ticket medio, ciclo de venta
- Win rate por segmento
- CAC por motor
- Performance de contenidos y canales
- SLAs agregados del mes
- Estado de iniciativas del roadmap

### 5.4 Decisiones tipo que habilita
- Reasignación de inversión entre motores
- Activación/desactivación de iniciativas
- Ajustes al pricing o al proceso comercial
- Necesidades de contratación

### 5.5 Estructura de pre-read
[Plantilla: qué secciones debe tener el documento MBR que se distribuye 48h antes]

---

## 6. Cadencia trimestral — Quarterly Business Review (QBR)

### 6.1 Ficha
- **Duración:** 3h (con pausa)
- **Cuándo:** Última semana del trimestre o primera del siguiente
- **Participantes:** C-level + Heads de Marketing, Ventas, Producto
- **Dueño del pre-read:** Director Comercial + Marketing Lead (conjunto)
- **Decisor:** CEO
- **Pre-read:** Dossier QBR, entregado 1 semana antes

### 6.2 Agenda tipo
1. Resultados Q vs. plan anual (25 min)
2. Revisión del ICP: ¿seguimos vendiendo a quien dijimos? (20 min)
3. Revisión del posicionamiento: ¿está aguantando en el mercado? (20 min)
4. Motor de revenue: ¿el sistema funciona como fue diseñado? (30 min)
5. Roadmap del próximo Q: prioridades y recursos (45 min)
6. Decisiones estratégicas (30 min)

### 6.3 Métricas que se revisan
- Revenue cerrado Q vs plan
- Pipeline generado Q por canal/motor
- Evolución de métricas north star del measurement-framework
- Evolución de CAC, LTV, payback
- Cohortes de clientes (retención, expansión)
- Benchmarks del sector (si disponibles)

### 6.4 Decisiones tipo que habilita
- Cambios estratégicos de posicionamiento
- Entrada/salida de segmentos
- Reasignación significativa de presupuesto
- Nuevas contrataciones clave
- Ajuste del plan anual

### 6.5 Estructura del dossier QBR
[Plantilla: índice del documento que se distribuye 1 semana antes]

---

## 7. Dashboards operativos

### 7.1 Dashboard operativo — equipo comercial (diario)
- **Audiencia:** AEs, SDRs, Director Comercial
- **Herramienta:** [CRM nativo / Looker Studio / Power BI / según martech-measurement]
- **Métricas:** Pipeline personal, deals estancados, SLAs pendientes, actividad de la semana
- **Frecuencia de actualización:** Tiempo real / diaria
- **Dueño:** [Admin CRM]

### 7.2 Dashboard táctico — management (semanal/mensual)
- **Audiencia:** Director Comercial, Marketing Lead
- **Herramienta:** [...]
- **Métricas:** Funnel completo, velocidad, win rate, performance por motor, SLAs agregados
- **Frecuencia:** Semanal
- **Dueño:** [Persona]

### 7.3 Dashboard estratégico — dirección (mensual/Q)
- **Audiencia:** CEO, C-level
- **Herramienta:** [...]
- **Métricas:** Revenue, pipeline total, evolución north star metric, CAC/LTV
- **Frecuencia:** Mensual
- **Dueño:** [Persona]

---

## 8. Alertas automatizadas

### 8.1 Alertas comerciales
| Alerta | Umbral | Destinatario | Acción esperada |
|--------|--------|-------------|-----------------|
| Deal estancado >N días | [N] | AE + Director | Revisar y decidir reactivar/cerrar |
| SLA marketing→ventas incumplido | [X] horas | Director Comercial | Reasignar o contactar |
| Pipeline por debajo del umbral de forecast | [Y%] | Director Comercial | Plan de recuperación |

### 8.2 Alertas de marketing
| Alerta | Umbral | Destinatario | Acción esperada |
|--------|--------|-------------|-----------------|
| Caída de conversión landing/lead | [X%] | Marketing Lead | Revisar funnel |
| Caída de tráfico orgánico | [X%] | Marketing Lead | Diagnóstico SEO |
| CAC por encima del objetivo | [Y] | CRO + Marketing Lead | Reasignación |

---

## 9. Roles y responsabilidades (RACI resumido)

| Actividad | R (Responsable) | A (Aprueba) | C (Consultado) | I (Informado) |
|-----------|-----------------|-------------|----------------|---------------|
| Producir pre-read weekly | [Rol] | [Rol] | — | Equipo |
| Conducir weekly | [Rol] | — | — | Equipo |
| Producir pre-read MBR | [Rol] | [Rol] | [Rol] | Equipo |
| Conducir MBR | [Rol] | — | — | — |
| Producir dossier QBR | [Rol] | [Rol] | [Rol] | — |
| Mantener dashboards | [Rol] | [Rol] | — | — |

---

## 10. Onboarding al sistema

### 10.1 Primer día de un nuevo AE
- Dashboards a consultar diariamente
- Reuniones a las que asiste
- Qué reporte produce cada viernes

### 10.2 Primer día de un nuevo Director Comercial
- Dashboards que debe dominar
- Reuniones que lidera
- Pre-reads que debe producir

### 10.3 Revisión del sistema
- **Cuándo:** 1 vez al trimestre
- **Quién:** Director Comercial + CEO
- **Qué evalúa:** Si las cadencias están generando las decisiones que debían, si sobra/falta alguna reunión, si los dashboards siguen siendo los correctos

---

## 11. Checklist de implementación

| # | Acción | Dueño | Fecha objetivo | Estado |
|---|--------|-------|----------------|--------|
| 1 | Crear dashboard operativo comercial | [Rol] | [Fecha] | [ ] |
| 2 | Crear dashboard táctico management | [Rol] | [Fecha] | [ ] |
| 3 | Crear dashboard estratégico dirección | [Rol] | [Fecha] | [ ] |
| 4 | Configurar alertas automatizadas | [Rol] | [Fecha] | [ ] |
| 5 | Agendar weekly recurrente | [Rol] | [Fecha] | [ ] |
| 6 | Agendar MBR recurrente | [Rol] | [Fecha] | [ ] |
| 7 | Agendar primera QBR | [Rol] | [Fecha] | [ ] |
| 8 | Distribuir plantillas de agenda | [Rol] | [Fecha] | [ ] |
| 9 | Formación del equipo en el sistema | [Rol] | [Fecha] | [ ] |
| 10 | Primera revisión del sistema | [Rol] | [Fecha + 90 días] | [ ] |

---

## 12. Especificación de estructura para /revos:entrega

**DOCX formal:** `[Cliente] - Reporting OS v1.docx` (lo genera `/revos:entrega`) con el sistema completo: narrativa + plantillas de agenda + estructura de actas.

**XLSX operativo:** `[Cliente] - Reporting OS v1.xlsx` (lo genera `/revos:entrega`) con hojas:
1. Calendario operativo — todas las cadencias, participantes, pre-reads y decisiones (columnas: Cadencia, Reunión, Día recurrente, Duración, Participantes, Dueño del pre-read, Decisor, Pre-read entregado a, Dashboard fuente, Decisiones tipo que habilita)
2. Dashboards
3. Alertas
4. Checklist de implementación

---

## 13. Vacíos e hipótesis

**Información que falta:** [[FALTA DATO]]
**Hipótesis críticas:** [[HIPÓTESIS]] — cadencias ajustadas al tamaño del equipo, carga total de reporting
**Decisiones abiertas del cliente:** Herramienta de BI, quién administra dashboards, día recurrente de reuniones

---

## Entrega

Cuando el sistema esté completo:

1. Presenta el output en Markdown.
2. Añade al final una sección **"Resumen para el consultor"** con:
   - Las cadencias diseñadas, listadas por frecuencia — sin recuento
   - Carga total de reporting por rol (horas/semana)
   - Los dashboards operativos, listados por dueño — sin recuento
   - Gaps ([FALTA DATO] críticos)
   - Nivel de confianza en el sistema (1-5)
3. El contenido validado se guarda como `[Cliente] - Reporting OS v1.md` en `01 Entregables`. El orquestador lo registra en el Registro.
4. Los ficheros finales maquetados (DOCX + XLSX) los genera `/revos:entrega` según la preferencia de output registrada en fase 0, siguiendo la especificación de estructura de la sección 12.
5. Este skill cierra el ciclo de Activation — combínalo con `exec-deliverables` para el handover final.

## Lo que NO debes hacer

- No diseñes más de tres cadencias principales — saturar el calendario del equipo mata la disciplina.
- No definas reuniones sin decisión explícita asociada — son teatro operativo.
- No inventes métricas que no estén en el measurement-framework — el reporting deriva, no improvisa.
- No escribas agendas abstractas ("alineamiento", "revisión general") — agendas con tiempos y outputs concretos.
- No olvides el pre-read — una reunión sin pre-read es una reunión para descubrir datos, no para decidir.
- No uses jerga genérica de management ("sync", "touchpoint", "check-in") — el sistema habla el lenguaje del negocio.
- No dejes ningún reporte sin dueño y sin decisor — se muere en dos semanas.
- No generes tú los ficheros DOCX/XLSX finales — los produce `/revos:entrega`; este skill entrega el contenido validado en Markdown y la especificación de estructura.
