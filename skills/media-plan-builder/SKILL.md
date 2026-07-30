---
name: media-plan-builder
description: >
  Usar cuando el consultor necesite producir un plan de medios táctico a partir de la estrategia de canales:
  inversión por canal por mes, formatos, audiencias, creatividades esperadas, KPIs y cadencias de optimización.
  Activar como skill opcional de Activation, tras channel-strategy-design. También activar si el consultor
  pide "plan de medios", "media plan", "inversión publicitaria" o "plan de paid".
---

# Media Plan Builder

## Propósito

Este skill produce el plan de medios táctico del cliente en formato ejecutable: inversión mensual por canal, formatos por canal, audiencias segmentadas, creatividades esperadas (número y tipo, no redacción), KPIs objetivo, cadencias de optimización y escenarios de sensibilidad. Convierte la estrategia de canales en un plan operable por un equipo de media o una agencia.

No redacta copy ni diseña creatividades (eso es `brand-copy-system` + trabajo creativo). No sustituye el plan estratégico de canales — lo aterriza a tácticas de media.

## Posición en el pipeline

**Requiere:** Channel Strategy Design, Positioning & Messaging. Recomendado: Content & Discoverability Design, Brand Copy System.

**Produce:** Media Plan v1 en Markdown validado. El fichero final maquetado (XLSX operativo) lo genera `/revos:entrega` según la preferencia de output registrada en fase 0, siguiendo la especificación de estructura incluida en este skill.

**Siguiente skill:** Ninguno obligatorio (skill opcional).

## Principios de ejecución

**Inversión proporcional a la función.** Cada canal pagado recibe inversión según su peso en el mix y su función en el funnel. No se reparte por igual ni por disponibilidad de creatividad.

**Audiencias que corresponden al ICP.** La segmentación de audiencias en cada plataforma se deriva del ICP (no de lo que la plataforma sugiere por defecto). Primer principio: fit con ICP, segundo: volumen.

**Formatos por canal con criterio.** LinkedIn no es Meta no es Google Ads. Cada canal tiene formatos que funcionan mejor para B2B según etapa. El plan especifica formato por campaña.

**Cadencias de optimización.** Se define cada cuánto se revisan los KPIs de cada campaña y qué decisiones se toman. Sin cadencia, el media plan se ejecuta a ciegas.

**Ramp-up realista.** No se asume velocidad de crucero desde el día 1. Primer mes: aprendizaje + configuración. Segundo: optimización inicial. Tercero: escalado si los KPIs lo permiten.

**Trípode de control.** Cada campaña se monitoriza con (1) KPI de entrega (impresiones, CPM, CTR), (2) KPI de respuesta (CPC, leads, conversiones) y (3) KPI de negocio (CAC, pipeline generado).

**Benchmarks con fuente.** Cualquier CPM, CPC, CTR o CVR usado como referencia va con fuente. Si no hay fuente verificable, [FALTA BENCHMARK].

**Convenciones v4:** cada [FALTA DATO] se clasifica al detectarse como bloqueante (impide una decisión de este entregable) o no bloqueante. Presupuesto máximo: 2 ciclos de revisión por entregable. Agotado el presupuesto, los [FALTA DATO] no bloqueantes se convierten en [ASUNCIÓN: valor asumido + criterio] y el sistema avanza; solo los bloqueantes detienen y se escalan al cliente de inmediato. Los datos extraídos de CRM conectado se marcan [DATO CRM: fuente, fecha]. Referencia completa: skills/revos-orchestrator/references/convenciones.md del plugin revos.

**Lenguaje.** Castellano. Registro ejecutivo operativo. Vocabulario: CPM, CPC, CTR, CVR, frecuencia, audiencia, lookalike, retargeting, fatiga creativa, ROAS, CAC. Evitar: "campañas virales", "performance puro" sin brand.

## Proceso

**Paso 1 — Lectura de inputs.**
Channel Strategy (qué canales, peso, función), Positioning (ICP, mensajes), Growth System (qué motores alimenta cada canal), Measurement Framework (KPIs oficiales).

**Paso 2 — Selección de canales pagados.**
De la channel strategy, selecciona los que son pagados (total o parcialmente). Típicamente: LinkedIn Ads, Google Ads (búsqueda + performance max si aplica), Meta Ads si el ICP lo justifica, ABM tools si hay ABM en el plan, retargeting cross-canal.

**Paso 3 — Diseño de audiencias por canal.**
Para cada canal, define 2-4 audiencias derivadas del ICP: core (match exacto ICP), adyacentes, retargeting de intención, lookalike si aplica. Para cada una: tamaño estimado, criterios exactos de segmentación.

**Paso 4 — Formatos y creatividades por campaña.**
Formato principal (ej. single image ad, video corto, documento, lead gen form, search ad). Número de variaciones creativas por campaña para evitar fatiga. Rotación.

**Paso 5 — Inversión mensual por canal y campaña.**
Partiendo del rango definido en channel strategy. Detalla la inversión mensual a 6-12 meses con fase de ramp-up. Justifica cada partida.

**Paso 6 — KPIs objetivo por campaña.**
Trípode de control por campaña: entrega, respuesta, negocio. Benchmarks citados con fuente. Objetivos realistas según madurez.

**Paso 7 — Cadencia de optimización.**
Quincenal los primeros 60 días, mensual después. Qué se revisa, qué decisiones se toman, cuándo se pausa o se escala una campaña.

**Paso 8 — Escenarios de sensibilidad.**
Escenario base. Escenario -30% (presupuesto recortado: qué se mantiene, qué se pausa). Escenario +30% (presupuesto ampliado: dónde se invierte lo adicional y con qué lógica).

**Paso 9 — Especificación de estructura para /revos:entrega.**
Completa la especificación de estructura del XLSX operativo (ver sección 11 del template): inversión mensual por canal/campaña, audiencias por canal, KPIs objetivo, escenarios, benchmarks referencia. Este skill no genera el fichero — lo genera `/revos:entrega` a partir de esta especificación.

**Paso 10 — Revisión de coherencia.**
¿Inversión coherente con channel strategy? ¿Audiencias coherentes con ICP? ¿KPIs coherentes con measurement framework? ¿Hay realismo operativo (agencia o equipo interno capaz de ejecutarlo)?

## Template de output

Produce el output siguiendo exactamente esta estructura.

---

# Media Plan — [NOMBRE EMPRESA]
*RevOS Activation · Versión 1.0 · [Fecha]*

---

## 1. Sumario ejecutivo
*[Máximo 200 palabras. Inversión total prevista, número de canales, audiencias principales, KPI principal, escenarios contemplados.]*

---

## 2. Contexto

### 2.1 Origen de las decisiones
[Channel strategy, positioning, measurement framework — síntesis del input]

### 2.2 Canales pagados seleccionados
[Lista con peso relativo]

### 2.3 Horizonte temporal del plan
[Típicamente 6-12 meses]

---

## 3. Audiencias

### 3.1 Audiencia núcleo — ICP core
**Criterios:** [Rol, tamaño empresa, sector, geografía, tecnologías, etc.]
**Plataformas donde se construye:** [LinkedIn, Google, Meta, ABM]
**Volumen estimado:** [Con fuente si es posible]
**Uso principal:** [Awareness, demand gen, retargeting]

### 3.2 Audiencias adyacentes
[Para expansión de alcance manteniendo fit]

### 3.3 Audiencias de retargeting
[Visitantes web cualificados, engagers de contenido, audiencias de CRM]

### 3.4 Audiencias lookalike si aplica
[Por cuál se construyen, semejanza]

---

## 4. Canales y campañas

### 4.1 Canal — [Nombre canal 1, ej. LinkedIn Ads]
**Función principal:** [Awareness / Demand Gen / Captura / Retargeting]
**Audiencias utilizadas:** [Lista]
**Formatos principales:** [Single image, video, documento, lead gen]
**Campañas:**

| Campaña | Objetivo | Audiencia | Formato | Creatividades | Inversión/mes |
|---------|----------|-----------|---------|---------------|---------------|
| [Nombre] | [Lead gen ICP core] | [Audiencia A] | [Documento + lead gen] | 3 variantes | €X |

**KPIs objetivo:**
- Entrega: CPM esperado €X-Y (fuente: [...])
- Respuesta: CTR esperado X-Y% (fuente: [...])
- Negocio: CPL esperado €X-Y

**Riesgos de canal:** [Fatiga creativa, ajustes de targeting, competencia]

### 4.2 Canal — [Google Ads]
[Misma estructura]

### 4.3 Canal — [Meta Ads si aplica]
[Misma estructura]

### 4.4 Canal — [ABM si aplica]
[Misma estructura]

### 4.5 Retargeting cross-canal
[Plan específico de retargeting integrado]

---

## 5. Distribución de inversión

### 5.1 Inversión mensual por canal
| Canal | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 |
|-------|----|----|----|----|----|----|----|----|----|-----|-----|-----|
| [Canal 1] | €X | €X | €X | ... |

### 5.2 Ramp-up justificado
[Por qué M1 es menor que M3: configuración, aprendizaje, validación]

### 5.3 Inversión total por trimestre
[Suma Q1, Q2, Q3, Q4]

### 5.4 Distribución funcional
[% en awareness, % en demand gen, % en captura, % en retargeting]

---

## 6. Benchmarks sectoriales de referencia

[Tabla con CPM, CPC, CTR, CVR de referencia por canal y formato, con fuente. Lo que no tenga fuente: [FALTA BENCHMARK].]

---

## 7. Cadencia de optimización

### 7.1 Primera fase (M1-M2) — aprendizaje
**Cadencia:** Quincenal
**Decisiones posibles:** Ajustar audiencias, rotar creatividades, corregir targeting
**Criterios para escalar:** CPL dentro de banda objetivo + CVR mínimo

### 7.2 Segunda fase (M3-M6) — optimización
**Cadencia:** Mensual
**Decisiones posibles:** Redistribuir inversión, pausar campañas no rentables, lanzar nuevos formatos

### 7.3 Tercera fase (M7-M12) — escalado
**Cadencia:** Mensual
**Decisiones posibles:** Escalar inversión en campañas ganadoras, explorar nuevas audiencias, nuevos canales

---

## 8. Escenarios de sensibilidad

### 8.1 Escenario base
[Lo descrito en secciones anteriores]

### 8.2 Escenario -30% presupuesto
**Qué se mantiene:** [Canales críticos, audiencia core]
**Qué se pausa:** [Canales menos maduros, audiencias adyacentes]
**Impacto esperado en KPIs:** [Pipeline proyectado ajustado]

### 8.3 Escenario +30% presupuesto
**Dónde se invierte adicional:** [Escalado de ganadores + exploración]
**Impacto esperado en KPIs:** [Pipeline proyectado ampliado]

---

## 9. Requerimientos operativos

### 9.1 Equipo/agencia requerida
[Roles o perfil de agencia para ejecutar el plan]

### 9.2 Activos creativos necesarios
[Número y tipo de creatividades por mes — input para producción]

### 9.3 Herramientas de gestión
[Ads managers, herramientas de tracking, conexión con CRM]

---

## 10. Reporting del plan

### 10.1 Reporting semanal
[Métricas básicas de entrega]

### 10.2 Reporting mensual
[Métricas completas con trípode de control]

### 10.3 Reporting trimestral
[Análisis de rendimiento + ajustes]

---

## 11. Especificación de estructura para /revos:entrega

**XLSX operativo:** `[Cliente] - Media Plan v1.xlsx` (lo genera `/revos:entrega` según la preferencia de output registrada en fase 0) con hojas:
1. Inversión mensual por canal/campaña
2. Audiencias por canal
3. KPIs objetivo por campaña
4. Benchmarks referencia
5. Escenarios de sensibilidad

---

## 12. Vacíos e hipótesis

**Información que falta:** [[FALTA DATO]]
**Benchmarks no disponibles:** [[FALTA BENCHMARK]]
**Hipótesis críticas:** [[HIPÓTESIS]]
**Decisiones abiertas del cliente:** [Presupuesto definitivo, agencia, ventanas de lanzamiento]

---

## Entrega

Cuando el media plan esté completo:

1. Presenta el output en Markdown.
2. Añade al final una sección **"Resumen para el consultor"** con:
   - Inversión total a 12 meses
   - Nº de canales activos
   - KPI principal y CPL esperado en banda
   - Escenarios contemplados
   - Nivel de confianza en el plan (1-5)
3. El contenido validado se guarda como `[Cliente] - Media Plan v1.md` en `01 Entregables`. El orquestador lo registra en el State Log.
4. El fichero final maquetado (XLSX operativo) lo genera `/revos:entrega` según la preferencia de output registrada en fase 0, siguiendo la especificación de estructura de la sección 11.

## Lo que NO debes hacer

- No propongas inversiones sin justificación por canal y campaña.
- No uses benchmarks sin fuente — [FALTA BENCHMARK] cuando no haya.
- No ignores la fase de ramp-up — asumir velocidad de crucero desde el día 1 es un error frecuente.
- No diseñes audiencias amplias sin criterio ICP — principio de fit sobre volumen.
- No entregues sin plantear al menos los dos escenarios de sensibilidad.
- No generes tú el fichero XLSX final — lo produce `/revos:entrega`; este skill entrega el contenido validado en Markdown y la especificación de estructura.
