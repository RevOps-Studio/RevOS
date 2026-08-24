---
name: exec-deliverables
description: >
  Usar cuando el consultor necesite consolidar todo el trabajo realizado en el sistema RevOS en los
  entregables ejecutivos finales: Executive Summary, Board Deck y Handover Document. Activar como último
  skill del proyecto, tras cerrar toda la fase Activation. También activar si el consultor pide
  "entregables finales", "presentación ejecutiva", "handover", "cierre del proyecto" o "board deck".
---

# Executive Deliverables

## Propósito

Este skill produce los entregables ejecutivos finales del proyecto RevOS, pensados para tres audiencias distintas:

1. **Executive Summary** — documento de 8-15 páginas para el C-level del cliente y su Board (fichero final en DOCX).
2. **Board Deck** — presentación de 20-30 slides para la sesión de cierre con dirección (fichero final en PPTX).
3. **Handover Document** — documento operativo para el equipo que va a ejecutar el sistema en el día a día (fichero final en DOCX).

Este skill produce el contenido validado de los tres entregables en Markdown; los ficheros finales maquetados los genera `/revos:entrega` según la preferencia de output registrada en fase 0.

No genera contenido nuevo: sintetiza y consolida lo producido en los skills previos con un nivel de edición, diseño y narrativa superior, calibrado para decisores.

## Posición en el pipeline

**Requiere:** Todos los outputs de Design + Activation validados (especialmente Revenue Diagnostic, Growth System Design, Sales Conversion Design, Execution Roadmap, Channel Strategy Design, Sales Process Design, Measurement Framework, CRM Blueprint, Martech & Measurement Architecture).

**Produce:** Contenido validado en Markdown de los tres entregables: Executive Summary, Board Deck y Handover Document. Los ficheros finales (PPTX + 2 DOCX) los genera `/revos:entrega`.

**Siguiente skill:** `diagnostic-checkpoint`, parametrizada como checkpoint ejecutivo final (nodo virtual `activation-checkpoint` del grafo). El proyecto se cierra tras la validación del cliente en ese checkpoint y la entrega final vía `/revos:entrega`.

## Principios de ejecución

**Consolida, no inventa.** Cada afirmación de los entregables finales está respaldada por algún skill previo. Si algo no está en ningún output anterior, no debería aparecer aquí — o se identifica como gap a resolver antes del cierre.

**Narrativa orientada a decisión.** El Board Deck no es un catálogo de lo hecho. Es un argumento: dónde estábamos, qué descubrimos, qué proponemos, qué pasa si se ejecuta, qué decisiones hay que tomar. El consultor cuenta una historia ejecutiva.

**Tres audiencias, tres tonos.** El Executive Summary es denso y argumentado (leído en soledad). El Board Deck es visual y sintético (presentado en sala). El Handover es operativo y detallado (consultado en la operativa). No se pueden confundir.

**Números que mueven decisiones.** Las cifras del cliente (baseline, proyección, inversión, ritmo) tienen que aparecer de forma prominente. Con hipótesis declaradas y rangos cuando sea responsable hacerlo así.

**Una sola historia.** Los tres documentos cuentan la misma historia con distinto nivel de detalle. No hay contradicciones entre ellos. Antes de entregar, se hace una pasada de coherencia cruzada.

**Calidad visual.** Formato profesional. Portada, tabla de contenidos, numeración de páginas, separadores claros, tablas legibles. El cliente tiene que poder compartir estos entregables con su Board sin avergonzarse.

Convenciones v4.3 — **Doctrina de avance**: un [FALTA DATO] es no bloqueante por defecto; solo bloquea si cumple un criterio de la definición cerrada (inversión de tesis · irreversibilidad ante el cliente · imposibilidad material), y la carga de la prueba es del bloqueo. En primera pasada, si la fuente del dato no estará disponible antes del checkpoint, escribe directamente [ASUNCIÓN: valor + criterio falsable] — un v1 con asunciones declaradas es un entregable válido. Máximo 3 preguntas abiertas al consultor por entregable, escaladas agrupadas al cierre del paso, nunca una a una en mitad de la producción. **Lenguaje calibrado**: la asertividad es del entregable, no de la conversación; las conclusiones mayores declaran su confianza (alta: dato medido/CRM · media: declarado por el cliente · baja: inferencia), las consecuencias se formulan condicionadas — nunca proféticas — y el contraste retórico ("No es X. Es Y.") solo es admisible con evidencia de ambos lados. **Precondición**: antes de producir, lee `00 Sistema/[Cliente] - Registro` y detente si falta fase 0, si hay una intervención sin tramitar por /revos:cambio con presupuesto agotado, o si el cierre de fase anterior exigía un system-qa aún no APTO. **Resumen para el consultor**: enumera lo relevante — nunca recuentos totales. Mecánica completa (dos contadores, propagación en lote, disposición de huecos, etiquetas): skills/revos-orchestrator/references/convenciones.md del plugin revos.

**Lenguaje.** Castellano. Registro ejecutivo. En Board Deck, frases cortas y cifras. En Executive Summary, párrafos argumentados. En Handover, lista operativa y accionable. Evitar: jerga de consultoría genérica, ambigüedad estratégica, adjetivos huecos.

## Proceso

**Paso 1 — Inventario de outputs previos validados.**
Lista todos los entregables producidos en el proyecto. Verifica que están validados por el consultor. Si hay algún gap importante, advertir antes de empezar.

**Paso 2 — Definición de la narrativa maestra.**
En 1 párrafo: cuál es la historia del proyecto. De dónde partió el cliente, qué descubrimos, qué hemos diseñado, qué se espera como resultado, qué decisiones siguen abiertas. Esta narrativa guía los tres entregables.

**Paso 3 — Redacción del contenido del Board Deck.**
20-30 slides siguiendo la estructura narrativa, redactadas en Markdown conforme a la especificación de estructura de abajo. El PPTX final lo genera `/revos:entrega`.

**Paso 4 — Redacción del Executive Summary.**
8-15 páginas argumentadas, redactadas en Markdown conforme a la especificación de estructura de abajo. El DOCX final lo genera `/revos:entrega`.

**Paso 5 — Redacción del Handover Document.**
Documento operativo redactado en Markdown conforme a la especificación de estructura de abajo. Qué hay que hacer, por quién, con qué cadencia, con qué soporte, dónde buscar cada decisión documentada. El DOCX final lo genera `/revos:entrega`.

**Paso 6 — Pasada de coherencia cruzada.**
Verifica: ¿los tres documentos cuentan la misma historia? ¿las cifras coinciden? ¿las hipótesis están declaradas igual? ¿los próximos pasos coinciden?

**Paso 7 — Pasada de QA editorial.**
Tipos, puntuación, consistencia terminológica, siglas definidas la primera vez, cifras con unidades, tablas legibles.

**Paso 8 — Consolidación y entrega.**
Presenta el contenido validado de los tres entregables en Markdown, listo para registro y para la maquetación final vía `/revos:entrega`.

## Especificación de estructura para /revos:entrega — Board Deck (PPTX) — 20-30 slides

**Portada** — nombre del proyecto, cliente, fecha, versión.

**1. Resumen en 60 segundos** — una slide con 3-5 bullets: punto de partida, diagnóstico, propuesta, resultado esperado.

**2-3. Punto de partida** — baseline: revenue actual, pipeline, CAC, ciclo de venta, canales, equipo. Con datos.

**4-5. Hallazgos del diagnóstico** — 3-5 hallazgos críticos del Revenue Diagnostic, con evidencia.

**6. Posicionamiento propuesto** — categoría, promesa central, pilares.

**7-8. Sistema de Revenue propuesto** — motores de demanda, visualización simple.

**9-10. Proceso comercial propuesto** — pipeline con etapas, conversiones esperadas.

**11-12. Estrategia de canales** — mix, pesos, secuenciación.

**13. Arquitectura de medición** — North Star + métricas críticas.

**14. Roadmap de ejecución** — fases Q1/Q2/H2 con hitos.

**15. Inversión requerida** — por trimestre, por categoría (tecnología, contenido, media, equipo).

**16-17. Resultado esperado** — proyección a 12 meses con hipótesis declaradas y rangos.

**18. Gobernanza** — cadencia, responsables, checkpoints.

**19. Riesgos principales y mitigaciones** — 3-5 riesgos críticos.

**20. Decisiones abiertas del Board** — lo que hay que decidir ahora.

**21. Próximos 30 días** — qué arranca ya.

**Apéndice (5-10 slides)** — detalle de CRM, martech, equipo, etc. Para consulta en la sesión si surgen preguntas.

## Especificación de estructura para /revos:entrega — Executive Summary (DOCX) — 8-15 páginas

**Portada · índice · resumen ejecutivo (1 página)**

**1. Contexto del proyecto** (1 página)
Objetivos, alcance, proceso seguido, participantes.

**2. Diagnóstico de partida** (2-3 páginas)
Baseline cuantitativa, hallazgos cualitativos, principales fugas de revenue, principales oportunidades. Referencia a Revenue Diagnostic.

**3. Estrategia propuesta** (3-4 páginas)
Posicionamiento, sistema de revenue, proceso comercial, canales, contenidos. Nivel de argumentación — no solo enunciado.

**4. Arquitectura de activación** (2 páginas)
CRM blueprint, martech, measurement, gobernanza.

**5. Plan y roadmap** (1-2 páginas)
Fases, hitos, dependencias, inversión.

**6. Proyección y sensibilidad** (1 página)
Resultado esperado con escenarios (conservador, central, optimista). Hipótesis declaradas.

**7. Riesgos y decisiones abiertas** (0.5-1 página)
Los principales — sin adornos.

**Cierre · firmas · versión**

## Especificación de estructura para /revos:entrega — Handover Document (DOCX)

**1. Qué está hecho y dónde está documentado**
Tabla de todos los entregables y ubicación en el proyecto / Drive / sistema del cliente.

**2. Qué tiene que pasar en los próximos 30 días**
Acciones concretas con responsable y fecha.

**3. Cadencias operativas**
Qué se hace diariamente / semanalmente / mensualmente / trimestralmente, por quién.

**4. Métricas operativas y cómo consultarlas**
Lista de dashboards / reportes / fuentes, con ruta de acceso.

**5. Proceso comercial operativo**
Resumen ejecutable del sales process: etapas, criterios, cadencias, framework de cualificación. (Síntesis del sales-process-design.)

**6. CRM — guía rápida del equipo**
Campos obligatorios por etapa, reportes clave, automatizaciones activas, a quién contactar si algo falla.

**7. Stack y herramientas**
Cada herramienta, para qué, con qué acceso, quién administra.

**8. Contactos de soporte**
Responsables internos por área, partners externos.

**9. Qué hacer cuando algo cambie**
Proceso para actualizar el sistema (nuevo ICP, nueva línea, nuevo canal): a quién avisar, qué documentar.

## Entrega

Cuando los tres entregables estén listos:

1. Presenta en chat el contenido completo en Markdown de los tres entregables, junto a un resumen con el índice de cada documento y los "3 mensajes que queremos que el Board recuerde".
2. El contenido validado se guarda como `[Cliente] - Executive Summary v1.md`, `[Cliente] - Board Deck v1.md` y `[Cliente] - Handover Document v1.md` en `01 Entregables`. El orquestador los registra en el Registro. Los ficheros finales maquetados (PPTX + 2 DOCX) los genera `/revos:entrega` según la preferencia de output registrada en fase 0.
3. Indica al consultor: "Te entrego el contenido de los tres documentos finales. Tómalo como base para tu sesión de cierre con el cliente. Confirma si quieres ajustes de tono, de énfasis o de diseño antes de generar los ficheros con `/revos:entrega`."

## Lo que NO debes hacer

- No inventes contenido nuevo — todo tiene que venir de skills anteriores.
- No mezcles audiencias — Board Deck ≠ Executive Summary ≠ Handover.
- No presentes cifras sin hipótesis declaradas.
- No uses jerga consultora vacía — en entregables ejecutivos el coste reputacional es alto.
- No generes tú los ficheros PPTX/DOCX finales — el skill produce contenido validado en Markdown; la maquetación corresponde a `/revos:entrega`.
- No entregues los tres documentos sin haber hecho pasada de coherencia cruzada entre ellos.
