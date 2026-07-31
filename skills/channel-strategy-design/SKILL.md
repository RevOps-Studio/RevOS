---
name: channel-strategy-design
description: >
  Usar cuando el consultor necesite recomendar el mix de canales adecuado para el cliente dentro del tier
  Complete: qué canales activar, con qué peso, con qué función en el funnel, con qué inversión orientativa.
  Activar dentro del tier Complete, después de execution-roadmap-builder y antes de
  content-discoverability-design. También activar si el consultor pide "diseño de canales", "mix de canales",
  "en qué canales invertir" o "estrategia de canales".
---

# Channel Strategy Design

## Propósito

Este skill produce la estrategia de canales del cliente: qué canales activar, en qué orden, con qué peso relativo, con qué función en el funnel y con qué inversión orientativa. Es la bajada táctica de los motores de demanda diseñados en growth-system-design.

Es el documento que convierte "motor inbound SEO" en "LinkedIn orgánico + blog + newsletter + SEO técnico, con estos pesos y esta lógica". Es el que convierte "outbound ABM" en "LinkedIn outreach + email personalizado + eventos verticales".

## Posición en el pipeline

**Requiere:** Growth System Design, Positioning & Messaging, Competitive Landscape. Recomendado: Execution Roadmap.

**Produce:** Channel Strategy Design v1 en Markdown. Alimenta content-discoverability-design, media-plan-builder y content-calendar-builder.

**Siguiente skill:** content-discoverability-design (diseño de contenido y SEO/GEO dentro de la estrategia de canales).

## Principios de ejecución

**Canales al servicio del sistema.** Los canales no se eligen por moda ni por disponibilidad — se eligen por su contribución al funnel diseñado. Cada canal tiene una función clara: awareness, consideración, captura, activación, reactivación.

**Pocos canales bien operados.** Mejor 4 canales operados con profundidad que 10 canales operados superficialmente. La profundidad gana a la dispersión en B2B. El mix propuesto típicamente tiene entre 3 y 6 canales activos.

**Benchmarks con fuente.** Cuando se propongan volúmenes, CPMs, CPCs, CTRs, conversiones — usar benchmarks del sector encontrados vía web search, no inventar. Cada benchmark cita fuente. Si no hay benchmark disponible, marcar [FALTA BENCHMARK].

**Calibración al presupuesto.** El mix propuesto tiene que encajar en el rango de presupuesto del cliente. Si el presupuesto no permite el mix ideal, se explicitan los trade-offs: qué se sacrifica y por qué.

**Madurez progresiva.** No todos los canales se activan a la vez. Se define cuáles son "fase 1" (Q1), "fase 2" (Q2) y "horizonte" (H2). Esto respeta la capacidad del equipo y evita que nada funcione bien.

**Orgánico vs. pagado declarado.** Para cada canal se especifica la proporción orgánica vs. pagada y la lógica de esa proporción. No se asume que "orgánico" o "pagado" es mejor — depende del canal, el sector y la madurez.

**Convenciones v4.1 — **Precondición**: antes de producir, lee `00 Sistema/[Cliente] - Registro` y detente si falta fase 0, si el presupuesto de revisión de este entregable está agotado sin cambio tramitado por /revos:cambio, o si el cierre de fase anterior exigía un system-qa aún no APTO. **Etiquetado**: cada [FALTA DATO] se clasifica al detectarse como bloqueante (impide una decisión de este entregable) o no bloqueante. **Presupuesto**: 2 ciclos de revisión de calidad por entregable — solo consumen ciclo los cambios nacidos del juicio sobre lo escrito; las incorporaciones de información nueva (aportada por cliente o consultor, o medida por el sistema) no consumen ciclo y generan versión y entrada en el Backlog si el entregable ya está registrado. Agotado el presupuesto, los [FALTA DATO] no bloqueantes se convierten en [ASUNCIÓN: valor asumido + criterio falsable] y el sistema avanza; solo los bloqueantes detienen y se escalan de inmediato. **Resumen para el consultor**: enumera los bloqueantes y lo relevante — nunca recuentos totales (el recuento es chequeo mecánico de system-qa sobre el documento terminado). **Cierre**: todo [FALTA DATO] heredado sale con disposición explícita — resuelto, reasignado a la primera skill no ejecutada que lo necesite, o declinado con motivo. Datos de CRM conectado: [DATO CRM: fuente, fecha]. Referencia completa: skills/revos-orchestrator/references/convenciones.md del plugin revos.

**Lenguaje.** Castellano. Registro ejecutivo directo. Vocabulario: canal, mix, función en funnel, peso, CPL, CPA, CTR, conversión, fatiga creativa, frecuencia. Evitar: "estrategia 360", "ecosistema de canales", "full funnel mágico".

## Proceso

**Paso 1 — Leer outputs previos con foco en canales.**
Revisa el growth system design — qué motores fueron seleccionados. Revisa el positioning — qué categoría y qué ICP. Revisa el competitive — qué canales usan los competidores y cómo. Esto delimita el universo.

**Paso 2 — Inventario de canales candidatos.**
Lista canales candidatos organizados por función: awareness (eventos, medios, LinkedIn thought leadership, PR), consideración (contenido propio, webinars, comunidad), captura (search, landings, lead magnets), activación (email, retargeting), reactivación (nurturing, sequences).

**Paso 3 — Benchmarks via web search.**
Para los canales priorizados, busca benchmarks actualizados del sector del cliente: CPLs típicos, conversiones, volúmenes esperables. Cita fuente en cada benchmark. Si es demasiado específico para encontrar datos públicos, [FALTA BENCHMARK].

**Paso 4 — Evaluación de cada canal candidato.**
Para cada candidato relevante: fit con ICP, fit con posicionamiento, viabilidad operativa del cliente, benchmarks esperables, tiempo hasta primer resultado, inversión mínima razonable.

**Paso 5 — Selección del mix.**
Elige 3-6 canales que juntos cubran las funciones necesarias del funnel. Define peso relativo (alto/medio/bajo) por canal.

**Paso 6 — Diseño por canal.**
Para cada canal seleccionado: función en el funnel, mensajes dominantes (del positioning), formato principal, frecuencia, inversión orientativa, KPIs de salud, tiempo hasta primer resultado.

**Paso 7 — Secuenciación.**
Define qué canales se activan en cada fase. Identifica dependencias entre canales (ej. LinkedIn orgánico antes de paid).

**Paso 8 — Revisión de coherencia.**
Verifica: ¿el mix cubre todas las funciones que el growth system necesita? ¿el presupuesto y el equipo del cliente pueden operar esto? ¿los canales son coherentes con el posicionamiento? ¿las inversiones están calibradas a los benchmarks?

## Template de output

Produce el output siguiendo exactamente esta estructura.

---

# Channel Strategy Design — [NOMBRE EMPRESA]
*RevOS Design Complete · Versión 1.0 · [Fecha]*

---

## 1. Sumario ejecutivo
*[Máximo 250 palabras. Mix propuesto, número de canales, fases de activación, inversión total orientativa, lo que el mix resuelve vs. lo que deja para más adelante.]*

---

## 2. Contexto estratégico

### 2.1 Motores de demanda que alimenta este mix
[Lista de los motores del growth-system-design y cómo se conectan con los canales propuestos]

### 2.2 Restricciones operativas consideradas
[Presupuesto, equipo, tiempo, capacidad de producción de contenido — lo que condiciona el diseño del mix]

### 2.3 Referencias competitivas
[Qué canales usan los competidores relevantes — y en qué se diferencia el mix propuesto]

---

## 3. Principios del mix

### 3.1 Principio 1 — [Nombre]
[Principio que guía el diseño — ej. "profundidad sobre amplitud", "orgánico primero, paid para amplificar lo que funciona"]

### 3.2 Principio 2 — [Nombre]
### 3.3 Principio 3 — [Nombre]

---

## 4. Mix propuesto

### 4.1 Vista general del mix

| Canal | Función | Peso | Fase | Orgánico / Pagado |
|-------|---------|------|------|-------------------|
| [Canal 1] | [Awareness/Consideración/...] | Alto/Medio/Bajo | Q1/Q2/H2 | [Proporción] |
| [Canal 2] | [...] | [...] | [...] | [...] |

### 4.2 Cobertura del funnel
[Qué función cubre cada canal en el funnel — permite ver si hay huecos o solapes]

---

## 5. Diseño detallado por canal

### 5.1 Canal 1 — [Nombre]
**Función en el funnel:** [Awareness / Consideración / Captura / Activación / Reactivación]
**Por qué este canal:** [Argumento de fit con ICP, posicionamiento y motor al que sirve]
**Formato principal:** [Qué tipo de contenido o pieza domina]
**Mensajes dominantes:** [Referencias a los pilares del positioning que se expresan en este canal]
**Orgánico vs. pagado:** [Proporción y lógica]
**Frecuencia:** [Con qué ritmo se opera]
**Inversión orientativa:** [Rango mensual — con [HIPÓTESIS] o [FALTA BENCHMARK] si procede]
**KPIs de salud:** [3-5 KPIs específicos del canal]
**Tiempo hasta primer resultado:** [Estimación realista]
**Benchmarks sectoriales de referencia:** [Datos + fuente]
**Riesgos principales:** [Qué puede hacer que no funcione]

### 5.2 Canal 2 — [Nombre]
[Misma estructura]

*[Entre 3 y 6 canales detallados.]*

---

## 6. Secuencia de activación

### 6.1 Fase 1 — Q1
**Canales activos:** [Lista]
**Prioridad del trimestre:** [Cuál es el canal que más importa en Q1 — típicamente uno o dos]
**Inversión del trimestre:** [Rango]
**Hitos al cierre:** [Señales de que los canales están funcionando]

### 6.2 Fase 2 — Q2
**Canales que se añaden:** [Lista]
**Prioridad del trimestre:** [Cuál pesa más]
**Inversión del trimestre:** [Rango]
**Hitos al cierre:** [Qué debería estar demostrado]

### 6.3 Horizonte — H2
**Canales adicionales a evaluar:** [Lista condicionada a lo aprendido en H1]
**Condiciones para activar cada uno:** [Qué tiene que demostrar H1 para justificar cada canal adicional]

---

## 7. Inversión orientativa

### 7.1 Distribución por canal
[Tabla con inversión orientativa mensual por canal — orgánico (inversión en horas/contenido) vs. pagado (media)]

### 7.2 Distribución temporal
[Cómo evoluciona la inversión mes a mes durante los primeros 6-9 meses]

### 7.3 Supuestos del cálculo
[Qué benchmarks se han usado — con fuentes — y qué supuestos están en juego]

---

## 8. Requerimientos operativos

### 8.1 Equipo y skills necesarios
[Qué roles/capacidades hacen falta para operar este mix — con alerta si el equipo actual no los tiene]

### 8.2 Stack y herramientas
[Qué herramientas hacen falta por canal — con referencia a martech-stack-audit si existe]

### 8.3 Proveedores externos recomendados si aplica
[Dónde tiene sentido tirar de agencia o freelance — sin nombres específicos salvo que el consultor los pida]

---

## 9. Métricas del mix global

### 9.1 Métricas de contribución por canal al funnel
[Qué porción del pipeline viene de cada canal — medido cómo]

### 9.2 Métricas de eficiencia por canal
[CPL, CPA, coste por reunión cualificada por canal]

### 9.3 Métricas de salud global del mix
[Dependencia de canal único, diversificación, fatiga creativa]

---

## 10. Lo que este mix NO resuelve

[Huecos del funnel que el mix no cubre — por restricciones o por priorización. Gestión de expectativas explícita.]

---

## 11. Vacíos e hipótesis

**Información que falta:** [[FALTA DATO]]
**Benchmarks no disponibles:** [[FALTA BENCHMARK]]
**Hipótesis críticas:** [[HIPÓTESIS]]
**Decisiones abiertas del cliente:** [Decisiones requeridas]

---

## Entrega

Cuando la estrategia de canales esté completa:

1. Presenta el output completo en Markdown.
2. Añade al final una sección **"Resumen para el consultor"** con:
   - Los canales seleccionados, listados por nombre y rol — sin recuento
   - Canal dominante de Q1
   - Inversión total orientativa del primer trimestre
   - Brechas de equipo/skill detectadas
   - Nivel de confianza en el mix (1-5)
3. El contenido validado se guarda como `[Cliente] - Channel Strategy v1.md` en `01 Entregables`. El orquestador lo registra en el Registro. Siguiente skill: `content-discoverability-design`.

## Lo que NO debes hacer

- No propongas más de 6 canales — dispersión.
- No inventes benchmarks — si no hay fuente verificable, [FALTA BENCHMARK].
- No propongas canales incompatibles con el posicionamiento (ej. canales de mass market para un posicionamiento premium especialista).
- No asumas capacidad de producción de contenido ilimitada — cada canal tiene un coste de operación.
- No ignores el competitive research al elegir canales — a veces el canal correcto es el que los competidores no están usando.
- No avances a content-discoverability-design sin confirmación del consultor.
