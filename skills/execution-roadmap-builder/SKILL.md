---
name: execution-roadmap-builder
description: >
  Usar cuando el consultor necesite priorizar y convertir todo el sistema diseñado (posicionamiento, growth,
  sales conversion y si aplica los Complete) en un roadmap ejecutable: iniciativas priorizadas, secuencia
  trimestral, dependencias, responsables, hitos. Cierra la fase de Design y prepara la Activation. Activar
  siempre después de los skills de Design — en Essentials después de sales-conversion-design, en Complete
  después de measurement-framework. También activar si el consultor pide "construye el roadmap", "plan de
  ejecución", "priorización de iniciativas" o "cronograma del sistema".
---

# Execution Roadmap Builder

## Propósito

Este skill produce el Execution Roadmap: el artefacto que convierte todo lo diseñado en el sistema RevOS en un plan ejecutable con iniciativas priorizadas, secuenciadas, con responsables y con hitos medibles.

Es la pieza que hace que el sistema deje de ser "un diseño bonito" y se convierta en algo operable. Un sistema sin roadmap es un sistema de papel. Un roadmap sin sistema es un plan de tareas sin estrategia. Aquí se unen.

El entregable final es doble: un XLSX operativo (que puede vivir, actualizarse y usarse para seguimiento) y un PPTX ejecutivo (que comunica el plan a dirección y stakeholders). Este skill produce el contenido validado en Markdown, incluida la especificación de estructura de ambos ficheros; los ficheros finales maquetados los genera `/revos:entrega` según la preferencia de output registrada en fase 0.

## Posición en el pipeline

**Requiere:** Revenue Diagnostic, Positioning & Messaging, Growth System Design, Sales Conversion Design. Si se está ejecutando Complete: + Channel Strategy, Content Discoverability, Sales Process, Measurement Framework.

**Produce:** Execution Roadmap v1 en Markdown, con especificación de estructura del XLSX operativo (tablero) y del PPTX ejecutivo para `/revos:entrega`.

**Siguiente skill:** diagnostic-checkpoint (checkpoint de cierre de Design con el cliente). Tras validación, se avanza a Activation en tier Complete, o se cierra el alcance en tier Essentials.

## Principios de ejecución

**Priorización con criterio explícito.** Las iniciativas se priorizan por dos ejes principales: (1) impacto sobre los cuellos de botella del diagnóstico, (2) esfuerzo relativo de implementación. Se añade un tercer criterio cualitativo: dependencias bloqueantes.

**Trimestres, no meses ni semanas.** El roadmap opera en unidades de trimestre — demasiado granular (semanas) descarrila con cualquier cambio; demasiado grueso (años) es irrelevante. Q1, Q2, Q3, Q4 son las unidades.

**Cada iniciativa tiene dueño.** No iniciativa sin owner. El owner es una persona (o rol) nominal, no "el equipo de marketing". Si no se sabe quién, se marca [DUEÑO POR DEFINIR] — no se asume.

**Hitos medibles, no actividades.** Cada iniciativa tiene un hito de cierre verificable. "Lanzar campaña" no es hito. "Primeras 50 reuniones agendadas desde la campaña" sí.

**Dependencias visibles.** Si la iniciativa B depende de que termine la A, se hace explícito. El roadmap muestra las dependencias, no solo las fechas.

**Secuenciación realista.** Q1 no puede tener 20 iniciativas grandes. La capacidad del equipo limita. El roadmap respeta esa capacidad, no la ignora.

**Lenguaje.** Castellano. Registro ejecutivo directo. Los nombres de iniciativas son frases de resultado, no de actividad. "Activar motor inbound SEO" es actividad; "Generar primeras 20 reuniones desde inbound SEO" es resultado.

**Convenciones v4:** cada [FALTA DATO] se clasifica al detectarse como bloqueante (impide una decisión de este entregable) o no bloqueante. Presupuesto máximo: 2 ciclos de revisión por entregable. Agotado el presupuesto, los [FALTA DATO] no bloqueantes se convierten en [ASUNCIÓN: valor asumido + criterio] y el sistema avanza; solo los bloqueantes detienen y se escalan al cliente de inmediato. Los datos extraídos de CRM conectado se marcan [DATO CRM: fuente, fecha]. Referencia completa: skills/revos-orchestrator/references/convenciones.md del plugin revos.

## Proceso

**Paso 1 — Inventario de iniciativas candidatas.**
Revisa todos los outputs de Design. Por cada skill, extrae las iniciativas implícitas o explícitas. Típicamente emergen entre 20 y 40 iniciativas candidatas — esto se reducirá por priorización.

**Paso 2 — Agrupación por objetivo.**
Agrupa las iniciativas por objetivos mayores: activar motor X, implementar handoff Y, rediseñar web, instalar CRM, etc. Esta agrupación reduce redundancias.

**Paso 3 — Evaluación impacto × esfuerzo.**
Para cada iniciativa, evalúa impacto sobre los problemas del diagnóstico (A/M/B) y esfuerzo de implementación (A/M/B). Añade una nota de dependencias si las tiene.

**Paso 4 — Priorización y criba.**
Selecciona las iniciativas que entran en roadmap (típicamente 15-25 para 12 meses). Descarta las de bajo impacto y alto esfuerzo. Segundo plano para las de impacto medio.

**Paso 5 — Secuenciación temporal.**
Asigna cada iniciativa a un trimestre. Respeta dependencias: nada va a Q1 si depende de algo de Q2. Respeta capacidad: si Q1 ya tiene 5 iniciativas grandes, una sexta va a Q2.

**Paso 6 — Asignación de dueños.**
Por cada iniciativa, asigna dueño nominal. Si el cliente no tiene el rol, se marca como dependencia (ej. "requiere contratar/asignar RevOps parcial").

**Paso 7 — Definición de hitos.**
Por cada iniciativa, un hito de cierre medible. No dos ni tres — uno. Si necesita dos hitos, probablemente son dos iniciativas.

**Paso 8 — Especificación del XLSX operativo.**
Estructura la especificación del XLSX con las hojas: Summary, Initiatives, Quarterly View, Dependencies, Owners. Cada hoja con su función.

**Paso 9 — Especificación del PPTX ejecutivo.**
Versión narrativa del roadmap para dirección: slide de tesis, slide por trimestre, slide de requerimientos, slide de riesgos. Máximo 10 slides.

**Paso 10 — Revisión de coherencia.**
Verifica: ¿el roadmap prioriza lo que el diagnóstico identificó como crítico? ¿los trimestres son realistas dada la capacidad? ¿hay hitos que permiten detectar desviaciones temprano?

## Template de output

El entregable final principal es el XLSX. Este skill produce en Markdown el contenido del roadmap y la especificación de estructura de los ficheros finales, que sirve como descripción de entregables para `/revos:entrega`.

---

# Execution Roadmap — [NOMBRE EMPRESA]
*RevOS Design · Versión 1.0 · [Fecha]*

---

## 1. Sumario ejecutivo
*[Máximo 250 palabras. Tesis del roadmap, número de iniciativas, distribución por trimestre, las 3 iniciativas más críticas del Q1.]*

---

## 2. Principios de priorización aplicados

### 2.1 Criterio principal
[Qué guía la priorización — típicamente resolver los cuellos de botella del diagnóstico, empezando por los de máximo impacto × menor esfuerzo]

### 2.2 Criterios secundarios
[Dependencias, capacidad del equipo, restricciones de presupuesto]

### 2.3 Lo que se deja fuera y por qué
[Iniciativas descartadas o aplazadas con explicación breve]

---

## 3. Estructura del XLSX — Especificación de estructura para /revos:entrega

### 3.1 Hoja "Summary"
**Contenido:** KPIs globales del roadmap, distribución de iniciativas por trimestre y por dueño, indicadores de progreso.

### 3.2 Hoja "Initiatives"
**Contenido:** Listado completo de iniciativas con columnas:

| Columna | Descripción |
|---------|-------------|
| ID | Código único (INI-001, INI-002...) |
| Iniciativa | Nombre de la iniciativa — frase de resultado |
| Descripción | 1-2 líneas de qué resuelve |
| Área | Posicionamiento / Demanda / Conversión / Comercial / Stack / Medición |
| Origen | A qué skill/output del diseño responde |
| Cuello de botella del diagnóstico | Qué cuello de botella específico aborda |
| Impacto | A / M / B |
| Esfuerzo | A / M / B |
| Trimestre | Q1 / Q2 / Q3 / Q4 |
| Dueño | Nombre o rol |
| Dependencias | IDs de iniciativas de las que depende |
| Hito de cierre | Resultado verificable que confirma que se ha completado |
| Estado | Por defecto "No iniciada" |
| Notas | Contexto adicional |

### 3.3 Hoja "Quarterly View"
**Contenido:** Vista por trimestre — qué se activa en cada uno, qué hitos se esperan al cierre.

### 3.4 Hoja "Dependencies"
**Contenido:** Mapa de dependencias — tabla o matriz que muestra qué depende de qué.

### 3.5 Hoja "Owners"
**Contenido:** Listado de dueños con su carga de iniciativas por trimestre. Permite ver sobrecargas.

---

## 4. Narrativa trimestral

### 4.1 Q1 — Tesis del trimestre
**Objetivo dominante:** [El objetivo central del trimestre en una frase]
**Iniciativas clave:** [Las 3-5 iniciativas que definen el trimestre]
**Hitos esperados al cierre:** [Qué debería estar demostrado al terminar Q1]
**Riesgos del trimestre:** [Qué puede descarrilar el plan]

### 4.2 Q2 — Tesis del trimestre
[Misma estructura]

### 4.3 Q3 — Tesis del trimestre
[Misma estructura]

### 4.4 Q4 — Tesis del trimestre
[Misma estructura]

---

## 5. Estructura del PPTX ejecutivo — Especificación de estructura para /revos:entrega

El PPTX tiene típicamente entre 8 y 10 slides:

1. **Tesis del roadmap** — una frase, sobre la página
2. **El punto de partida** — los cuellos de botella del diagnóstico que se abordan
3. **Principios de priorización** — cómo se decidió qué va primero
4. **Vista general del año** — distribución trimestral a alto nivel
5. **Q1 en detalle** — iniciativas, hitos, dueños
6. **Q2 en detalle** — iniciativas, hitos, dueños
7. **Q3-Q4 en alto nivel** — porque pueden ajustarse tras los aprendizajes del H1
8. **Requerimientos del plan** — equipo, stack, presupuesto, decisiones
9. **Principales riesgos y mitigaciones**
10. **Qué pedimos al cliente para empezar** — decisiones concretas para Q1

---

## 6. Requerimientos globales del plan

### 6.1 Equipo
[Qué roles necesita el plan — existentes, ampliaciones, nuevos]

### 6.2 Stack
[Qué piezas del stack requiere — con referencias a martech-stack-audit si existe]

### 6.3 Presupuesto orientativo
[Rangos por trimestre y total, con disclaimer de [HIPÓTESIS] si no hay datos firmes]

### 6.4 Decisiones del cliente
[Qué decisiones tiene que tomar el cliente antes de arrancar Q1]

---

## 7. Principales riesgos

### 7.1 Riesgos de ejecución
[Capacidad, rotación, curva de aprendizaje del equipo]

### 7.2 Riesgos externos
[Cambios de mercado, timing de competidores]

### 7.3 Riesgos de adopción interna
[Resistencia organizacional, cambios de prioridad del cliente]

---

## 8. Vacíos e hipótesis

**Información que falta:** [[FALTA DATO]]
**Hipótesis críticas:** [[HIPÓTESIS]]
**Decisiones abiertas:** [Decisiones del cliente]

---

## Entrega

Cuando el roadmap esté construido:

1. Presenta el Markdown completo como documento de estructura y narrativa, incluidas las especificaciones de estructura para `/revos:entrega`: el XLSX operativo con las 5 hojas descritas (con fórmulas básicas para totales y conteos por estado) y el PPTX ejecutivo de 8-10 slides (diseño sobrio, tipografía grande, jerarquía visual clara).
2. Añade al final una sección **"Resumen para el consultor"** con:
   - Número total de iniciativas y su distribución por trimestre
   - Top 3 iniciativas de Q1
   - Carga por dueño — alerta si alguien está sobrecargado
   - Dependencias críticas — iniciativas bloqueantes
   - Nivel de confianza en la ejecutabilidad del plan (1-5)
3. El contenido validado se guarda como `[Cliente] - Execution Roadmap v1.md` en `01 Entregables`. El orquestador lo registra en el State Log. Los ficheros finales XLSX y PPTX los genera `/revos:entrega` según la preferencia de output registrada en fase 0. Siguiente skill: `diagnostic-checkpoint` (prepara la validación con el cliente del cierre de Design).

## Lo que NO debes hacer

- No priorices por impacto únicamente — el esfuerzo importa igual.
- No crees un roadmap con 40 iniciativas activas — no se puede ejecutar.
- No asignes dueños por defecto como "marketing" o "ventas" — tiene que ser rol específico o persona.
- No pongas hitos que sean actividades ("lanzar la campaña") — tienen que ser resultados medibles.
- No ignores las dependencias entre iniciativas — es lo que hace que los roadmaps descarrilen en el Q2.
- No generes ficheros XLSX ni PPTX — este skill produce contenido validado en Markdown con su especificación de estructura; los ficheros finales maquetados los genera `/revos:entrega`.
- No avances al checkpoint sin confirmación del consultor.
