---
name: content-discoverability-design
description: >
  Usar cuando el consultor necesite diseñar la arquitectura de contenidos y descubribilidad del cliente:
  qué contenidos producir, para qué etapa del funnel, para qué búsqueda/intención, con qué optimización
  SEO tradicional y qué lógica de GEO (generative engine optimization) para ser recuperado por LLMs.
  Activar dentro del tier Complete, después de channel-strategy-design y antes de sales-process-design.
  También activar si el consultor pide "arquitectura de contenidos", "SEO", "GEO", "posicionamiento en buscadores"
  o "plan de contenidos estratégico".
---

# Content & Discoverability Design

## Propósito

Este skill produce la arquitectura de contenidos y la lógica de descubribilidad del cliente: qué contenidos producir, con qué intención de búsqueda conectan, cómo se organizan en pilares y clusters, cómo se optimizan para buscadores tradicionales (SEO) y cómo se preparan para ser citados por motores generativos (GEO).

No es un calendario editorial (eso es content-calendar-builder). Es el mapa estratégico: qué temas dominan, qué preguntas respondemos, qué clusters construimos, qué piezas son el pilar y cuáles el soporte.

## Posición en el pipeline

**Requiere:** Channel Strategy Design, Positioning & Messaging, Competitive Landscape.

**Produce:** Content & Discoverability Design v1 en Markdown. Alimenta content-calendar-builder, brand-copy-system y sales-conversion-design (lead magnets).

**Siguiente skill:** sales-process-design.

## Principios de ejecución

**Contenidos al servicio del funnel.** Cada contenido tiene una función: atraer (TOFU), educar (MOFU), convertir (BOFU) o retener. No se produce contenido por producir — se produce para resolver una pregunta concreta del ICP en un momento concreto.

**Pilares y clusters.** La arquitectura se organiza en 3-5 pilares temáticos. Cada pilar tiene un contenido pilar (exhaustivo, perenne) y clusters de contenidos satélite que lo soportan y enlazan internamente. Esto es lo que construye autoridad temática para SEO y para GEO.

**Intención sobre volumen.** Keywords de alto volumen con baja intención B2B valen poco. Priorizar siempre intención comercial clara sobre búsquedas masivas genéricas. Una keyword con 200 búsquedas/mes pero intención transaccional B2B vale más que 5.000 búsquedas informacionales.

**GEO como capa añadida.** Los contenidos optimizados para SEO tradicional no son automáticamente recuperables por LLMs. GEO requiere: estructura clara, afirmaciones con fuente, datos concretos, definiciones directas, ejemplos verificables. Diseñar ambos en paralelo desde el principio.

**Evidencia con fuente.** Todo dato, benchmark, keyword o SERP referenciado viene con fuente accesible. Si no hay fuente, [FALTA EVIDENCIA].

**Convenciones v4.1 — **Precondición**: antes de producir, lee `00 Sistema/[Cliente] - Registro` y detente si falta fase 0, si el presupuesto de revisión de este entregable está agotado sin cambio tramitado por /revos:cambio, o si el cierre de fase anterior exigía un system-qa aún no APTO. **Etiquetado**: cada [FALTA DATO] se clasifica al detectarse como bloqueante (impide una decisión de este entregable) o no bloqueante. **Presupuesto**: 2 ciclos de revisión de calidad por entregable — solo consumen ciclo los cambios nacidos del juicio sobre lo escrito; las incorporaciones de información nueva (aportada por cliente o consultor, o medida por el sistema) no consumen ciclo y generan versión y entrada en el Backlog si el entregable ya está registrado. Agotado el presupuesto, los [FALTA DATO] no bloqueantes se convierten en [ASUNCIÓN: valor asumido + criterio falsable] y el sistema avanza; solo los bloqueantes detienen y se escalan de inmediato. **Resumen para el consultor**: enumera los bloqueantes y lo relevante — nunca recuentos totales (el recuento es chequeo mecánico de system-qa sobre el documento terminado). **Cierre**: todo [FALTA DATO] heredado sale con disposición explícita — resuelto, reasignado a la primera skill no ejecutada que lo necesite, o declinado con motivo. Datos de CRM conectado: [DATO CRM: fuente, fecha]. Referencia completa: skills/revos-orchestrator/references/convenciones.md del plugin revos.

**Lenguaje.** Castellano. Registro ejecutivo directo. Vocabulario: keyword, intención, SERP, pilar, cluster, topical authority, snippet, GEO, LLM citation. Evitar: "content is king", "ecosistema de contenidos", "storytelling mágico".

## Proceso

**Paso 1 — Lectura estratégica.**
Revisa positioning (categoría, mensajes, ICP), channel strategy (qué canales consumen qué contenido) y competitive (qué contenidos dominan hoy la categoría y quién lo hace).

**Paso 2 — Keyword research estructurado via web search.**
Busca keywords y preguntas reales relacionadas con los problemas del ICP y la categoría. Clasifica por intención (informacional / comparativa / transaccional) y por etapa del funnel. Cita fuente de volumen/dificultad siempre que sea posible. Marca [FALTA EVIDENCIA] cuando la fuente no sea verificable.

**Paso 3 — Análisis SERP de keywords clave.**
Para las keywords más estratégicas, revisa qué tipo de contenido domina la SERP: artículos largos, comparativas, herramientas, vídeos, listados. Esto define el formato que hay que producir.

**Paso 4 — Definición de pilares temáticos.**
Propón 3-5 pilares que cubran el territorio estratégico del posicionamiento. Cada pilar es un gran tema del que el cliente quiere ser referente.

**Paso 5 — Diseño de clusters por pilar.**
Para cada pilar, define: contenido pilar (1 pieza exhaustiva), 5-10 contenidos cluster que lo soportan, lógica de enlazado interno entre ellos.

**Paso 6 — Capa GEO.**
Para cada pilar, especifica cómo se estructura el contenido para ser citable por LLMs: preguntas-respuesta explícitas, definiciones en la intro, datos con fuente, ejemplos nombrados, sin adornos innecesarios.

**Paso 7 — Mapeo a etapas del funnel.**
Clasifica cada contenido propuesto por etapa del funnel (TOFU/MOFU/BOFU) y por canal principal de distribución. Esto conecta con channel strategy y con sales-conversion-design.

**Paso 8 — Priorización y fase 1.**
Propón qué 10-15 contenidos deben producirse en los primeros 90 días y por qué. El resto queda como backlog priorizado para los siguientes trimestres.

**Paso 9 — Revisión de coherencia.**
Verifica: ¿los pilares reflejan el posicionamiento? ¿el mix de intenciones cubre todo el funnel? ¿hay equilibrio TOFU/MOFU/BOFU? ¿la capacidad de producción del cliente permite el ritmo propuesto?

## Template de output

Produce el output siguiendo exactamente esta estructura.

---

# Content & Discoverability Design — [NOMBRE EMPRESA]
*RevOS Design Complete · Versión 1.0 · [Fecha]*

---

## 1. Sumario ejecutivo
*[Máximo 250 palabras. Pilares temáticos, número de contenidos propuestos, lógica SEO+GEO, prioridad de los primeros 90 días.]*

---

## 2. Contexto estratégico

### 2.1 Conexión con el posicionamiento
[Cómo los pilares temáticos aterrizan la categoría y los mensajes del positioning]

### 2.2 Conexión con channel strategy
[Qué canales distribuyen qué contenidos y con qué lógica]

### 2.3 Referencias competitivas
[Qué contenidos dominan hoy la categoría, quién lo hace, qué espacio queda libre]

---

## 3. Investigación de keywords e intenciones

### 3.1 Metodología
[Fuentes utilizadas, alcance, limitaciones]

### 3.2 Keywords priorizadas
| Keyword | Intención | Volumen (fuente) | Dificultad (fuente) | Etapa funnel | Pilar asociado |
|---------|-----------|------------------|---------------------|--------------|----------------|
| [kw 1]  | [Info/Comp/Trans] | [número + fuente] | [número + fuente] | [TOFU/MOFU/BOFU] | [Pilar X] |

### 3.3 Preguntas reales del ICP detectadas
[Preguntas literales que hace el ICP — People Also Ask, foros, entrevistas, Reddit, LinkedIn]

### 3.4 Análisis SERP de keywords clave
[Para las 5-10 más estratégicas: qué tipo de contenido domina, qué formato hay que producir, qué huecos hay]

---

## 4. Arquitectura temática

### 4.1 Pilar 1 — [Nombre]
**Tesis del pilar:** [En una frase, qué territorio de autoridad reclama]
**Conexión con el posicionamiento:** [Referencia al pilar de mensaje correspondiente]
**Contenido pilar (piedra angular):** [Título, formato, extensión orientativa]
**Contenidos cluster:** [Lista de 5-10 satélites, con título y formato]
**Lógica de enlazado interno:** [Cómo se enlazan entre sí y hacia el pilar]
**Keywords principales cubiertas:** [Lista]

### 4.2 Pilar 2 — [Nombre]
[Misma estructura]

*[Entre 3 y 5 pilares.]*

---

## 5. Capa GEO — optimización para motores generativos

### 5.1 Principios GEO aplicados
[Cómo se estructura cada pieza: pregunta-respuesta directa en intro, definiciones explícitas, datos con fuente, ejemplos nombrados]

### 5.2 Checklist GEO por contenido
[Lista de verificación que cualquier contenido del plan debe cumplir para ser citable]

### 5.3 Piezas candidatas a citación
[Qué contenidos del plan son los candidatos más fuertes a ser citados por LLMs y por qué]

---

## 6. Mapeo al funnel

### 6.1 Contenidos TOFU
[Objetivo: atraer tráfico del ICP. Formato, canal, función.]

### 6.2 Contenidos MOFU
[Objetivo: educar al ICP sobre el problema y las soluciones. Formato, canal, función.]

### 6.3 Contenidos BOFU
[Objetivo: convertir intención en reunión/demo/prueba. Formato, canal, función.]

### 6.4 Contenidos de retención/expansión
[Contenidos dirigidos a clientes existentes si aplica]

---

## 7. Plan de los primeros 90 días

### 7.1 Contenidos a producir en Q1
[10-15 contenidos priorizados, con responsable y formato]

### 7.2 Criterio de priorización
[Por qué estos y no otros — típicamente: mayor impacto SEO/GEO, menor coste de producción, mayor conexión con BOFU]

### 7.3 Backlog priorizado para Q2 y Q3
[Siguiente tanda]

---

## 8. Requerimientos operativos

### 8.1 Capacidad de producción necesaria
[Cuántas piezas al mes, de qué tipo, con qué recursos internos y externos]

### 8.2 Roles y responsables
[Quién escribe, quién revisa, quién publica, quién optimiza]

### 8.3 Stack técnico mínimo
[CMS, herramienta SEO, herramienta de analítica, herramienta de tracking]

---

## 9. Métricas

### 9.1 Métricas SEO
[Posicionamiento en keywords objetivo, tráfico orgánico, CTR en SERP, backlinks]

### 9.2 Métricas GEO
[Citaciones en LLMs — cómo medirlo hoy, con sus limitaciones]

### 9.3 Métricas de negocio
[Leads capturados por contenido, pipeline influido por contenido, CAC por contenido]

---

## 10. Lo que este plan NO cubre

[Huecos conscientes: idiomas no incluidos, canales de contenido no abordados (vídeo, podcast), territorios temáticos adyacentes que quedan fuera.]

---

## 11. Vacíos e hipótesis

**Información que falta:** [[FALTA DATO]]
**Evidencia no disponible:** [[FALTA EVIDENCIA]]
**Hipótesis críticas:** [[HIPÓTESIS]]
**Decisiones abiertas del cliente:** [Decisiones requeridas sobre formatos, idiomas, volumen]

---

## Entrega

Cuando el diseño de contenidos y descubribilidad esté completo:

1. Presenta el output completo en Markdown.
2. Añade al final una sección **"Resumen para el consultor"** con:
   - Los pilares temáticos, listados por nombre — sin recuento
   - Total de contenidos propuestos en el plan completo y en los primeros 90 días
   - Mix TOFU/MOFU/BOFU estimado
   - Brechas de capacidad de producción detectadas
   - Nivel de confianza en la arquitectura (1-5)
3. El contenido validado se guarda como `[Cliente] - Content Discoverability v1.md` en `01 Entregables`. El orquestador lo registra en el Registro. Siguiente skill: `sales-process-design`.

## Lo que NO debes hacer

- No confundas este skill con un calendario editorial — no se definen fechas ni autores concretos aquí.
- No propongas pilares que no aterricen el posicionamiento — sería contenido huérfano.
- No inventes datos de keywords ni volúmenes — si no hay fuente verificable, [FALTA EVIDENCIA].
- No optimices solo para SEO ignorando GEO — es desperdiciar la mitad del tráfico futuro.
- No propongas volúmenes de producción incompatibles con la capacidad real del cliente.
- No avances a sales-process-design sin confirmación del consultor.
