---
name: competitive-research
description: >
  Usar cuando el consultor necesite generar inteligencia competitiva y de categoría para el cliente: análisis
  de competidores directos e indirectos, dinámicas de categoría, posicionamientos del mercado, gaps detectados.
  Activar siempre después de knowledge-base-builder y antes de revenue-diagnostic. También activar si el
  consultor pide "análisis competitivo de [cliente]", "mapa de categoría", "benchmark competitivo" o "cómo se
  posicionan los competidores de [cliente]".
---

# Competitive Research

## Propósito

Este skill produce el análisis competitivo y de categoría para el cliente RevOS. No es una lista de competidores — es una lectura estratégica del mercado en el que el cliente opera: quién compite, cómo se posiciona cada uno, qué categorías narrativas existen, qué gaps aprovechables hay.

El propósito no es describir el mercado en abstracto — es articular las decisiones de posicionamiento que el cliente tendrá que tomar en el skill de positioning-messaging. Un análisis competitivo que no informa decisiones de posicionamiento es relleno.

## Posición en el pipeline

**Requiere:** Knowledge Base v1 del cliente (obligatorio) · acceso a web search y deep research recomendado.

**Produce:** Competitive Landscape v1 en Markdown estructurado con mapa de categoría, análisis de 3-5 competidores prioritarios, oportunidades de posicionamiento detectadas.

**Siguiente skill:** revenue-diagnostic (cierra el diagnóstico integrando cliente + competencia).

## Principios de ejecución

**Priorizar sobre completitud.** No se trata de analizar a todos los competidores posibles — se trata de analizar los 3-5 que realmente importan para las decisiones del cliente. Mejor 4 competidores analizados en profundidad que 12 listados superficialmente.

**Jerarquía de competidores.** Distingue tres capas: (1) competidores directos — mismo producto/servicio, mismo ICP; (2) competidores de categoría — distinto producto pero mismo job to be done; (3) alternativas no-competitivas — lo que el cliente compraría si no existiera esta categoría (ej. contratar internamente, no hacer nada, hacerlo a mano).

**Posicionamiento, no features.** El análisis no es una tabla comparativa de funcionalidades. Es una lectura de cómo cada competidor se posiciona: qué promete, a quién, con qué tono, qué categoría narrativa ocupa.

**Gaps, no huecos.** Un gap real es una posición de mercado defendible y deseable que nadie ocupa hoy. No todo hueco es un gap — hay huecos vacíos por buenas razones. Marca los gaps con [GAP] y los huecos cuestionables con [HIPÓTESIS DE GAP].

**Fuentes verificables.** Todo lo que se afirme de un competidor debe poder trazarse a una fuente pública (web, LinkedIn, prensa, case study). Cita brevemente las fuentes. Si es información declarada por el cliente sobre el competidor, márcala como [FUENTE: cliente].

**Convenciones v4.1 — **Precondición**: antes de producir, lee `00 Sistema/[Cliente] - Registro` y detente si falta fase 0, si el presupuesto de revisión de este entregable está agotado sin cambio tramitado por /revos:cambio, o si el cierre de fase anterior exigía un system-qa aún no APTO. **Etiquetado**: cada [FALTA DATO] se clasifica al detectarse como bloqueante (impide una decisión de este entregable) o no bloqueante. **Presupuesto**: 2 ciclos de revisión de calidad por entregable — solo consumen ciclo los cambios nacidos del juicio sobre lo escrito; las incorporaciones de información nueva (aportada por cliente o consultor, o medida por el sistema) no consumen ciclo y generan versión y entrada en el Backlog si el entregable ya está registrado. Agotado el presupuesto, los [FALTA DATO] no bloqueantes se convierten en [ASUNCIÓN: valor asumido + criterio falsable] y el sistema avanza; solo los bloqueantes detienen y se escalan de inmediato. **Resumen para el consultor**: enumera los bloqueantes y lo relevante — nunca recuentos totales (el recuento es chequeo mecánico de system-qa sobre el documento terminado). **Cierre**: todo [FALTA DATO] heredado sale con disposición explícita — resuelto, reasignado a la primera skill no ejecutada que lo necesite, o declinado con motivo. Datos de CRM conectado: [DATO CRM: fuente, fecha]. Referencia completa: skills/revos-orchestrator/references/convenciones.md del plugin revos.

**Lenguaje.** Castellano. Registro ejecutivo directo. Evita la jerga comparativa blanda — "más moderno", "mejor experiencia", "más completo". Di exactamente qué diferencia hay y qué implica.

## Proceso

**Paso 1 — Identificar universo competitivo.**
Antes de buscar, articula qué tipo de competidores busca el cliente. Revisa la knowledge base: ¿a quién mencionan como competencia? ¿Qué categorías narrativas emergen? Si el cliente mencionó competidores, empieza por ellos.

**Paso 2 — Mapa inicial de 3 capas.**
Lista competidores en las 3 capas (directos, categoría, alternativas). Prioriza los 3-5 más relevantes para el cliente — no los más grandes del mercado, los más relevantes para las decisiones de este cliente concreto.

**Paso 3 — Research en profundidad de los priorizados.**
Para cada competidor priorizado, investiga: web principal (homepage, how it works, pricing si es público), posicionamiento declarado, ICP aparente, últimos posts/contenidos relevantes, menciones en prensa, casos de cliente. Usa web search activamente. En el plugin revos, la investigación pesada multi-fuente puede delegarse en el agente competitive-researcher, que devuelve hallazgos con citación de fuentes.

**Paso 4 — Análisis por competidor.**
Para cada uno, articula: categoría narrativa que ocupa, promesa central, ICP aparente, mecanismo de diferenciación, fortalezas visibles, vulnerabilidades observables.

**Paso 5 — Mapa de posicionamiento.**
Sintetiza: qué categorías narrativas existen en el mercado, qué ocupa cada competidor, dónde está el cliente actualmente (si es visible), dónde hay espacio libre defendible.

**Paso 6 — Recomendaciones para positioning.**
Articula 2-3 hipótesis de posicionamiento que el cliente debería evaluar en el siguiente skill. No son decisiones finales — son direcciones con argumento.

**Paso 7 — Revisión de coherencia.**
Antes de entregar: ¿los competidores priorizados son realmente los que mencionó el cliente como relevantes? ¿las recomendaciones de posicionamiento son viables dada la knowledge base del cliente? ¿hay algún competidor que ignoré por defecto y debería estar?

## Template de output

Produce el output siguiendo exactamente esta estructura.

---

# Competitive Landscape — [NOMBRE EMPRESA]
*RevOS Diagnostic · Versión 1.0 · [Fecha]*

---

## 1. Sumario ejecutivo
*[Máximo 250 palabras. Categoría(s) en las que opera el cliente, competidores más relevantes, tensión central del mercado, oportunidad de posicionamiento más clara que emerge del análisis.]*

---

## 2. Definición del mercado

### 2.1 Categoría(s) narrativa(s) existentes
[Qué categorías narrativas existen en este mercado — cómo se nombra este espacio en decks de competidores, prensa, analistas]

### 2.2 Job to be done
[Qué problema resuelve este mercado desde el punto de vista del comprador, más allá del producto]

### 2.3 Alternativas no-competitivas
[Qué haría el comprador si no existiera esta categoría — incluye "no hacer nada", "hacerlo internamente", etc.]

---

## 3. Mapa competitivo

### 3.1 Competidores directos
[Lista breve con nombre y una línea de descripción — los que venden lo mismo al mismo ICP]

### 3.2 Competidores de categoría
[Lista breve — distinto producto pero mismo job to be done]

### 3.3 Alternativas relevantes
[Opciones no-competitivas pero con cuota de atención del comprador]

---

## 4. Análisis detallado de competidores priorizados

### 4.1 [Competidor 1 — Nombre]
**Categoría narrativa que ocupa:** [Cómo se autodenomina, qué espacio narrativo reclama]
**Promesa central:** [Qué prometen en una frase]
**ICP aparente:** [A quién parecen estar vendiendo según su comunicación]
**Mecanismo de diferenciación:** [Qué afirman que los hace distintos]
**Fortalezas visibles:** [Qué hacen objetivamente bien — con evidencia]
**Vulnerabilidades observables:** [Qué gaps tienen que el cliente podría explotar]
**Fuentes:** [URLs principales consultadas]

### 4.2 [Competidor 2 — Nombre]
[Misma estructura]

### 4.3 [Competidor 3 — Nombre]
[Misma estructura]

*[Añadir hasta 5 máximo. Si son menos, menos — no rellenar.]*

---

## 5. Mapa de posicionamiento

### 5.1 Ejes de diferenciación presentes en el mercado
[Los 2-3 ejes sobre los que los competidores se diferencian — ej. generalista vs. especialista, tecnológico vs. consultivo, proceso vs. resultado]

### 5.2 Posiciones ocupadas
[Qué competidor ocupa qué posición en esos ejes — con una descripción narrativa, no un gráfico]

### 5.3 Posición actual del cliente
[Dónde está hoy el cliente en ese mapa — con honestidad, aunque el cliente crea estar en otro sitio]

### 5.4 Gaps detectados
**[GAP 1]:** [Posición defendible y deseable que nadie ocupa — con argumento de por qué sería viable]
**[GAP 2]:** [Otra posición si existe]
**[HIPÓTESIS DE GAP]:** [Posiciones que parecen libres pero pueden estar vacías por buenas razones — con la hipótesis del por qué]

---

## 6. Dinámicas de categoría

### 6.1 Tendencias relevantes
[Qué está cambiando en esta categoría — consolidación, nuevas entradas, cambios tecnológicos, cambios regulatorios]

### 6.2 Lenguaje emergente
[Nuevos términos, nuevas categorías narrativas que están apareciendo en el mercado]

### 6.3 Señales de saturación o desaturación
[Donde el mercado está saturado (muchos actores compitiendo por el mismo mensaje) y donde hay espacio de voz]

---

## 7. Recomendaciones para positioning

### 7.1 Hipótesis de posicionamiento para evaluar
**[HIPÓTESIS 1]:** [Primera dirección de posicionamiento — con argumento de por qué tiene sentido dado el análisis]
**[HIPÓTESIS 2]:** [Segunda dirección si aplica]
**[HIPÓTESIS 3]:** [Tercera si aplica — máximo 3]

### 7.2 Categorías narrativas a explorar
[Qué categorías narrativas tendría sentido que el cliente considere ocupar o crear]

### 7.3 Riesgos de posicionamiento
[Qué posicionamientos el cliente debería evitar y por qué]

---

## 8. Vacíos, hipótesis y limitaciones del análisis

**Información que no fue posible obtener:** [Competidores sobre los que hubo poca información pública — [FALTA DATO], clasificado como bloqueante o no bloqueante]
**Hipótesis que requieren validación del cliente:** [Lista de [HIPÓTESIS]]
**Limitaciones del análisis:** [Qué no se ha podido hacer y por qué]
**Siguientes research recomendados:** [Si hace falta deep research adicional para reforzar alguna sección. En el plugin revos, la investigación pesada multi-fuente puede delegarse en el agente competitive-researcher, que devuelve hallazgos con citación de fuentes.]

---

## Entrega

Cuando el análisis competitivo esté completo:

1. Presenta el output completo en Markdown.
2. Añade al final una sección **"Resumen para el consultor"** con:
   - Los competidores analizados en profundidad, listados — sin recuento
   - Los [GAP] detectados, listados, con el más importante resumido en una frase — sin recuento total.
   - Hipótesis de posicionamiento más prometedora
   - Fuentes principales consultadas (listado)
   - Tu evaluación de la robustez del análisis (1-5) con frase explicativa
3. El contenido validado se guarda como `[Cliente] - Competitive Research v1.md` en `01 Entregables`. El orquestador lo registra en el Registro. Siguiente skill: `revenue-diagnostic`.

## Lo que NO debes hacer

- No produzcas una tabla comparativa de features — eso no es análisis competitivo, es un formulario.
- No listes más de 5 competidores en análisis detallado aunque existan más — prioriza.
- No afirmes cosas sobre un competidor sin fuente pública o declaración del cliente. Si lo infieres, márcalo como [HIPÓTESIS].
- No uses juicios blandos ("son buenos en X", "son modernos") — di exactamente qué hacen y qué implica.
- No confundas un hueco de mercado con un gap aprovechable — hay huecos vacíos por buenas razones.
- No generes el fichero final maquetado (DOCX u otro formato) — este skill produce contenido validado en Markdown; el fichero final lo genera `/revos:entrega` según la preferencia de output registrada en fase 0.
