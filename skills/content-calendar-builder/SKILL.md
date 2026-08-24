---
name: content-calendar-builder
description: >
  Usar cuando el consultor necesite producir el calendario editorial operativo del cliente: qué contenido,
  en qué fecha, por quién, en qué canal, con qué formato, con qué CTA, derivado del plan de arquitectura
  de contenidos. Activar como skill opcional de Activation tras content-discoverability-design. También
  activar si el consultor pide "calendario editorial", "content calendar", "plan editorial" o "planificación
  de contenidos".
---

# Content Calendar Builder

## Propósito

Este skill produce el calendario editorial operativo del cliente: la planificación mensual y trimestral de contenidos a producir y publicar, derivada de la arquitectura de contenidos (`content-discoverability-design`). Cubre: fecha de publicación, fecha de producción, canal, formato, tema, pilar al que pertenece, responsable de producción, responsable de revisión, CTA, KPIs.

No decide qué contenidos producir — eso ya está decidido en la arquitectura. Este skill aterriza esa decisión estratégica a un calendario ejecutable.

## Posición en el pipeline

**Requiere:** Content & Discoverability Design. Recomendado: Channel Strategy Design, Brand Copy System.

**Produce:** Content Calendar v1 en Markdown validado. El fichero final maquetado (XLSX operativo) lo genera `/revos:entrega` según la preferencia de output registrada en fase 0, siguiendo la especificación de estructura incluida en este skill.

**Siguiente skill:** Ninguno obligatorio (skill opcional).

## Principios de ejecución

**Cadencia realista, no aspiracional.** El calendario refleja la capacidad real de producción del cliente, no lo que "molaría" tener. Mejor 4 piezas mensuales consistentes que 12 planificadas y 3 publicadas.

**Pilares balanceados.** Cada mes debe cubrir los pilares temáticos de forma equilibrada. Se evita concentrar todo el peso en un pilar y olvidar los demás.

**Funnel balanceado.** Cada mes mezcla TOFU, MOFU y BOFU en la proporción definida por el plan estratégico. Solo TOFU = tráfico sin conversión. Solo BOFU = sin nuevo público.

**Fechas de producción antes que de publicación.** Para cada pieza se define la fecha de publicación, pero también la cadena de fechas hacia atrás: brief, borrador, revisión, diseño, aprobación. Sin eso el calendario se rompe en la primera pieza compleja.

**Responsables unívocos.** Cada pieza tiene un único responsable de producción y un único responsable de revisión. "Lo hace el equipo" no es un responsable.

**Canal primario y adaptaciones.** Cada pieza tiene un canal primario (ej. blog), pero también sus adaptaciones (LinkedIn post, newsletter, email nurturing). El calendario contempla todas.

**KPI esperado por pieza.** Cada pieza tiene un KPI orientativo (tráfico esperado, leads esperados, alcance esperado). Para tener contrafáctico.

**Reutilización explícita.** Pieza pilar → clusters. Informe largo → posts. Webinar → resúmenes + clips. Se planifica la reutilización desde el día 1, no como ocurrencia.

Convenciones v4.3 — **Doctrina de avance**: un [FALTA DATO] es no bloqueante por defecto; solo bloquea si cumple un criterio de la definición cerrada (inversión de tesis · irreversibilidad ante el cliente · imposibilidad material), y la carga de la prueba es del bloqueo. En primera pasada, si la fuente del dato no estará disponible antes del checkpoint, escribe directamente [ASUNCIÓN: valor + criterio falsable] — un v1 con asunciones declaradas es un entregable válido. Máximo 3 preguntas abiertas al consultor por entregable, escaladas agrupadas al cierre del paso, nunca una a una en mitad de la producción. **Lenguaje calibrado**: la asertividad es del entregable, no de la conversación; las conclusiones mayores declaran su confianza (alta: dato medido/CRM · media: declarado por el cliente · baja: inferencia), las consecuencias se formulan condicionadas — nunca proféticas — y el contraste retórico ("No es X. Es Y.") solo es admisible con evidencia de ambos lados. **Precondición**: antes de producir, lee `00 Sistema/[Cliente] - Registro` y detente si falta fase 0, si hay una intervención sin tramitar por /revos:cambio con presupuesto agotado, o si el cierre de fase anterior exigía un system-qa aún no APTO. **Resumen para el consultor**: enumera lo relevante — nunca recuentos totales. Mecánica completa (dos contadores, propagación en lote, disposición de huecos, etiquetas): skills/revos-orchestrator/references/convenciones.md del plugin revos.

**Lenguaje.** Castellano. Registro ejecutivo operativo. Vocabulario: calendario, cadencia, pilar, cluster, CTA, gating, reutilización, adaptación. Evitar: "content machine", "always-on" como cliché.

## Proceso

**Paso 1 — Extracción del plan estratégico.**
Lee content-discoverability-design: pilares, piezas priorizadas para Q1, backlog priorizado, formatos, canales asociados.

**Paso 2 — Calibración de capacidad.**
Confirma con el cliente (o hereda del intake): capacidad real de producción mensual en cada formato (artículos, vídeos, webinars, posts, informes). Esto fija la cadencia.

**Paso 3 — Diseño del calendario mensual para Q1.**
Para cada mes del primer trimestre: lista exacta de piezas, fechas de publicación, pilar al que pertenece, etapa del funnel, canal primario, formato, responsable.

**Paso 4 — Planificación hacia atrás de cada pieza.**
Desde la fecha de publicación: fecha límite de diseño, fecha límite de borrador final, fecha límite de primer borrador, fecha de brief. Típicamente: brief (D-21), borrador 1 (D-14), revisión (D-10), borrador final (D-7), diseño (D-3), publicación (D-0).

**Paso 5 — Adaptaciones y reutilización.**
Para cada pieza primaria: lista de adaptaciones (post LinkedIn, newsletter, etc.) con fechas y responsables. Piezas pilares alimentan a varios clusters; informes alimentan a series de posts; webinars alimentan a clips y resúmenes.

**Paso 6 — CTAs por pieza.**
CTA principal de cada pieza (vinculado a su etapa del funnel). CTAs secundarios si aplica. Guía del brand-copy-system cuando exista.

**Paso 7 — KPIs orientativos por pieza.**
Tráfico esperado, leads esperados, alcance esperado. Con margen realista.

**Paso 8 — Backlog Q2 y Q3.**
Lista de piezas planificadas para los siguientes trimestres, con fechas aproximadas. Menor nivel de detalle (se detalla mes a mes cuando llegue).

**Paso 9 — Calendario editorial integrado.**
Vista visual calendario: qué día cae qué pieza, qué canal, qué pilar. Útil para detectar concentraciones o huecos.

**Paso 10 — Especificación de estructura para /revos:entrega.**
Completa la especificación de estructura del XLSX operativo (ver sección 10 del template) con las hojas específicas. Este skill no genera el fichero — lo genera `/revos:entrega` a partir de esta especificación.

**Paso 11 — Revisión de coherencia.**
¿La cadencia cabe en la capacidad real? ¿Todos los pilares tienen cobertura? ¿Hay equilibrio TOFU/MOFU/BOFU? ¿Las adaptaciones están planificadas?

## Template de output

Produce el output siguiendo exactamente esta estructura.

---

# Content Calendar — [NOMBRE EMPRESA]
*RevOS Activation · Versión 1.0 · [Fecha]*

---

## 1. Sumario ejecutivo
*[Máximo 200 palabras. Cadencia mensual de piezas, cobertura de pilares, mix TOFU/MOFU/BOFU, equipo implicado.]*

---

## 2. Contexto

### 2.1 Arquitectura de contenidos de referencia
[Resumen breve: pilares, estrategia, prioridades Q1]

### 2.2 Capacidad de producción confirmada
[Por formato: artículos/mes, posts/mes, vídeos/mes, informes/trimestre, webinars/trimestre, etc.]

### 2.3 Equipo implicado y roles
[Quién escribe, quién revisa, quién aprueba, quién publica]

---

## 3. Calendario Q1 detallado

### 3.1 Mes 1
| Fecha pub | Pieza | Pilar | Etapa | Canal primario | Formato | Responsable prod | Responsable rev |
|-----------|-------|-------|-------|----------------|---------|------------------|-----------------|
| [DD/MM] | [Título] | [Pilar A] | TOFU | Blog | Artículo | [Persona] | [Persona] |
| [DD/MM] | [Título] | [Pilar B] | MOFU | LinkedIn | Post largo | [Persona] | [Persona] |
| ... |

### 3.2 Mes 2
[Misma estructura]

### 3.3 Mes 3
[Misma estructura]

### 3.4 Distribución Q1
| Concepto | Q1 |
|----------|-----|
| Total piezas | [N] |
| Pilar A | [N piezas (X%)] |
| Pilar B | [N piezas (X%)] |
| TOFU / MOFU / BOFU | [%/%/%] |
| Canal primario dominante | [Canal] |

---

## 4. Planificación de cada pieza (hacia atrás)

### 4.1 Ejemplo de planificación — pieza clave del mes 1
| Hito | Fecha | Responsable |
|------|-------|-------------|
| Brief aprobado | D-21 | [Marketing Lead] |
| Primer borrador | D-14 | [Redactor] |
| Revisión editorial | D-10 | [Editor] |
| Borrador final | D-7 | [Redactor] |
| Diseño/maquetación | D-3 | [Diseñador] |
| Publicación | D-0 | [Marketing Ops] |

### 4.2 SLAs estándar por formato
[Artículo: 21 días. Post: 7 días. Informe: 60 días. Webinar: 45 días.]

### 4.3 Piezas con dependencias externas
[Las que requieren input de expertos, invitados, clientes — con buffer extra]

---

## 5. Adaptaciones y reutilización

### 5.1 Matriz de reutilización por pieza pilar
| Pieza pilar | Adaptaciones planificadas | Fechas | Responsable |
|-------------|---------------------------|--------|-------------|
| [Informe X] | 5 posts LinkedIn, 1 webinar, 3 emails nurturing | [Fechas] | [Persona] |

### 5.2 Calendario de adaptaciones
[Cómo se distribuyen las adaptaciones en el tiempo — típicamente a lo largo de 4-8 semanas tras la publicación]

---

## 6. CTAs por pieza

### 6.1 Regla general por etapa
- TOFU: CTA a suscripción o siguiente lectura
- MOFU: CTA a lead magnet o comparativa
- BOFU: CTA a demo/reunión/trial

### 6.2 CTAs específicos Q1
[Tabla o lista de CTAs por pieza del Q1]

---

## 7. KPIs orientativos por pieza

### 7.1 KPIs por tipo de pieza
| Formato | Tráfico esperado | Leads esperados | Alcance esperado |
|---------|------------------|-----------------|------------------|
| Artículo pilar | [X] | [Y] | [Z] |
| Post LinkedIn | — | — | [Alcance] |
| Informe | [Tráfico a landing] | [Downloads] | — |

### 7.2 Contrafáctico por pieza destacada Q1
[Las 5-10 piezas más importantes del Q1 con KPI objetivo individual]

---

## 8. Backlog priorizado Q2 y Q3

### 8.1 Q2
[Lista de piezas previstas con mes orientativo y pilar]

### 8.2 Q3
[Lista de piezas previstas]

### 8.3 Criterios de re-priorización
[Qué haría cambiar este backlog — señales de rendimiento, cambios de estrategia]

---

## 9. Gobernanza del calendario

### 9.1 Reunión editorial semanal
[Participantes, duración, agenda estándar]

### 9.2 Revisión mensual del calendario
[Qué se valida, qué se ajusta, qué se incorpora]

### 9.3 Reporting editorial
[Qué métricas se comparten al final de cada mes]

---

## 10. Especificación de estructura para /revos:entrega

**XLSX operativo:** `[Cliente] - Content Calendar v1.xlsx` (lo genera `/revos:entrega` según la preferencia de output registrada en fase 0) con hojas:
1. Calendario Q1 por pieza
2. Calendario mensual visual
3. Matriz de reutilización
4. KPIs por pieza
5. Backlog Q2-Q3

---

## 11. Vacíos e hipótesis

**Información que falta:** [[FALTA DATO]]
**Hipótesis críticas:** [[HIPÓTESIS]]
**Decisiones abiertas del cliente:** [Responsables definitivos, cadencia exacta, formatos a priorizar]

---

## Entrega

Cuando el calendario esté completo:

1. Presenta el output en Markdown.
2. Añade al final una sección **"Resumen para el consultor"** con:
   - Las piezas de Q1, listadas por mes y formato — sin recuento total
   - Cadencia mensual
   - Mix TOFU/MOFU/BOFU
   - Brechas de capacidad detectadas
   - Nivel de confianza en el calendario (1-5)
3. El contenido validado se guarda como `[Cliente] - Content Calendar v1.md` en `01 Entregables`. El orquestador lo registra en el Registro.
4. El fichero final maquetado (XLSX operativo) lo genera `/revos:entrega` según la preferencia de output registrada en fase 0, siguiendo la especificación de estructura de la sección 10.

## Lo que NO debes hacer

- No planifiques volúmenes que excedan la capacidad real del cliente — el calendario se rompe en el primer mes.
- No concentres un pilar en un mes y descuides los otros — principio de equilibrio.
- No omitas adaptaciones — la reutilización es donde está el retorno real.
- No planifiques piezas sin responsable o con responsable genérico.
- No confundas este skill con el diseño de contenidos — aquí ya está decidido qué hacer, solo se calendariza.
- No generes tú el fichero XLSX final — lo produce `/revos:entrega`; este skill entrega el contenido validado en Markdown y la especificación de estructura.
