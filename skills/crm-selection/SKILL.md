---
name: crm-selection
description: >
  Usar cuando el cliente no tenga CRM o tenga un CRM inadecuado y el consultor necesite
  recomendar la opción más apropiada antes de ejecutar crm-blueprint-builder. Compara
  HubSpot, Salesforce, Pipedrive, Zoho y otras alternativas según los requisitos reales
  derivados del sistema diseñado — no por preferencia del consultor. Activar como skill
  opcional de Activation, siempre antes de crm-blueprint-builder si el CRM está por decidir.
  También activar si el consultor pide "qué CRM elegir", "comparativa de CRMs", "selección
  de CRM" o "recomendación de plataforma comercial".
---

# CRM Selection

## Propósito

Este skill produce una recomendación argumentada de CRM para el cliente: qué plataforma elegir, por qué esa y no otra, con qué configuración mínima, a qué coste real y con qué riesgos. Compara las alternativas viables (no todas las del mercado) usando una matriz de scoring ponderada por los requisitos específicos que surgen del sistema diseñado — volumen de pipeline, complejidad del proceso comercial, necesidad de marketing automation integrado, equipo técnico disponible, presupuesto.

No es un catálogo de CRMs ni una review comparativa neutral. Es una decisión con nombre y apellidos: "para este cliente, este CRM, por estas razones."

## Posición en el pipeline

**Requiere:** Sales Process Design (etapas del pipeline, criterios de cualificación, volumen estimado de oportunidades), Growth System Design (si hay marketing automation en el plan), Martech Stack Audit (herramientas existentes que deben integrarse).

**Produce:** CRM Selection Report v1 en Markdown (contenido validado). Los ficheros finales maquetados (DOCX + matriz XLSX de scoring comparativo) los genera `/revos:entrega` según la preferencia de output registrada en fase 0.

**Siguiente skill:** `crm-blueprint-builder` — con el CRM ya seleccionado, se procede a la especificación detallada de configuración.

## Principios de ejecución

**Requisitos antes que producto.** Primero se definen los requisitos (qué tiene que hacer el CRM para este cliente), después se evalúan las opciones. Nunca al revés. Empezar por "HubSpot vs Salesforce" es empezar mal.

**Web search obligatorio para pricing y features actuales.** El pricing de los CRMs cambia cada pocos meses. Los tiers se reconfiguran. Las features migran entre planes. Toda afirmación sobre precio o funcionalidad se verifica con web search antes de incluirla. Si no se puede verificar, se marca [FALTA BENCHMARK].

**Tres finalistas, no diez.** La matriz compara 3 finalistas reales. Más de tres dispersa la decisión; menos de tres no es comparación. Si se mencionan más plataformas, es como contexto de descarte rápido, no como finalistas.

**Criterios ponderados por negocio, no genéricos.** Los pesos de la matriz se derivan del contexto del cliente. Un cliente con 50 oportunidades al mes no pondera igual "escalabilidad" que uno con 2.000. Un cliente sin equipo técnico pondera "simplicidad de setup" por encima de "potencia de customización".

**Coste total, no solo licencias.** El TCO incluye licencias + implementación + formación + integraciones + coste de migración + coste de cambio posterior si falla. Un CRM "barato" en licencia puede ser caro en implementación o en cambio.

**Riesgos explícitos.** Toda recomendación viene con los 2-3 riesgos principales de esa elección. No hay CRM perfecto para nadie. Ocultar los riesgos hace parecer sólida una recomendación que no lo es.

**Decisión, no menú.** El skill termina con una recomendación única con nombre y plan. Matrices sin decisión final son informes, no recomendaciones.

Convenciones v4.3 — **Doctrina de avance**: un [FALTA DATO] es no bloqueante por defecto; solo bloquea si cumple un criterio de la definición cerrada (inversión de tesis · irreversibilidad ante el cliente · imposibilidad material), y la carga de la prueba es del bloqueo. En primera pasada, si la fuente del dato no estará disponible antes del checkpoint, escribe directamente [ASUNCIÓN: valor + criterio falsable] — un v1 con asunciones declaradas es un entregable válido. Máximo 3 preguntas abiertas al consultor por entregable, escaladas agrupadas al cierre del paso, nunca una a una en mitad de la producción. **Lenguaje calibrado**: la asertividad es del entregable, no de la conversación; las conclusiones mayores declaran su confianza (alta: dato medido/CRM · media: declarado por el cliente · baja: inferencia), las consecuencias se formulan condicionadas — nunca proféticas — y el contraste retórico ("No es X. Es Y.") solo es admisible con evidencia de ambos lados. **Precondición**: antes de producir, lee `00 Sistema/[Cliente] - Registro` y detente si falta fase 0, si hay una intervención sin tramitar por /revos:cambio con presupuesto agotado, o si el cierre de fase anterior exigía un system-qa aún no APTO. **Resumen para el consultor**: enumera lo relevante — nunca recuentos totales. Mecánica completa (dos contadores, propagación en lote, disposición de huecos, etiquetas): skills/revos-orchestrator/references/convenciones.md del plugin revos.

**Lenguaje.** Castellano. Registro ejecutivo directo. Vocabulario: CRM, pipeline, deals, contactos, workflows, automations, integraciones, TCO, implementación, roadmap de adopción. Evitar: "solución de CRM", "ecosistema CRM", "experiencia cliente 360", "journey del cliente".

## Proceso

**Paso 1 — Lectura del sistema diseñado.**
Sales-process-design (etapas, criterios, volumen, complejidad), growth-system-design (motores activos, necesidad de marketing automation), sales-conversion-design (handoff, SLAs, routing), martech-stack-audit (herramientas existentes que deben integrarse — email, calendario, facturación, soporte). Extrae requisitos funcionales específicos.

**Paso 2 — Recopilación de restricciones del cliente.**
Presupuesto disponible (licencia anual + implementación), número de usuarios actual y a 24 meses, capacidad técnica interna (¿hay alguien que pueda administrar un CRM?), idioma obligatorio (español nativo vs. aceptable en inglés), restricciones de datos (ubicación de servidores, GDPR, sector regulado). Si falta información crítica, marca [FALTA DATO] y solicita.

**Paso 3 — Lista de requisitos ponderados.**
Convierte el contexto en 10-15 requisitos concretos con peso (Alta / Media / Baja). Ejemplos: "Gestión de pipeline multi-etapa con criterios binarios — Alta", "Marketing automation integrado para nurturing — Media", "Integración nativa con Google Workspace — Alta", "Reporting avanzado y custom dashboards — Media". El peso se justifica, no se asigna al azar.

**Paso 4 — Selección de finalistas.**
Filtra el universo de CRMs a tres finalistas basándote en los requisitos. Ejemplos típicos por perfil:
- Empresa B2B con marketing ligero y equipo comercial pequeño: HubSpot Starter/Pro, Pipedrive, Zoho CRM
- B2B con marketing automation central: HubSpot Pro/Enterprise, Salesforce + Pardot, Zoho One
- B2B enterprise con procesos complejos: Salesforce Sales Cloud, Microsoft Dynamics, HubSpot Enterprise
- Empresa B2B con venta consultiva larga: Pipedrive, HubSpot Pro, Salesforce SMB

Justifica por qué estos tres y no otros. Los descartados quedan mencionados con una frase de descarte.

**Paso 5 — Verificación de pricing y features con web search.**
Para cada finalista: pricing actual por plan, features clave en cada plan, límites (contactos, deals, workflows, usuarios), coste de add-ons relevantes, coste típico de implementación (partner certificado o interno). Marca [FALTA BENCHMARK] si no se obtienen datos actualizados.

**Paso 6 — Matriz de scoring.**
Diseña la matriz con: requisitos en filas, finalistas en columnas, score 1-5 por celda, peso del requisito, score ponderado calculado. Fila final con total ponderado. El XLSX editable final (pesos editables, scores editables, total ponderado recalculado automáticamente, para que el consultor pueda modificar pesos y ver impacto) lo genera `/revos:entrega` siguiendo esta especificación de estructura.

**Paso 7 — Narrativa de recomendación.**
Prosa ejecutiva (3-5 párrafos) que explica la decisión: por qué este CRM gana, en qué plan concreto, qué requisitos cubre mejor que los otros, dónde tiene el riesgo principal, qué pasa si el cliente crece. No es "el ganador es X porque tiene mejor score" — es "para este cliente, en este momento, con este equipo, X es la decisión porque [razones de negocio]."

**Paso 8 — Plan de implementación orientativo.**
Fases (discovery → configuración → datos → formación → go-live), duración estimada, roles necesarios (admin, sponsor interno, partner externo si aplica), coste orientativo de implementación, hitos de adopción post go-live (30/60/90 días).

**Paso 9 — Riesgos y plan B.**
2-3 riesgos principales de la recomendación con mitigación. Plan B: ¿cuál sería la segunda opción si la primera se descarta por razón imprevista? Breve, ejecutable.

**Paso 10 — Especificación de estructura para /revos:entrega.**
Documenta en el output la estructura de los entregables finales: DOCX con la narrativa completa + matriz resumen, y XLSX con la matriz de scoring editable (pesos editables, scores editables, total ponderado recalculado automáticamente). Este skill no produce los ficheros finales: los genera `/revos:entrega` según la preferencia de output registrada en fase 0.

**Paso 11 — Revisión de coherencia.**
¿Los requisitos derivan del sistema diseñado o son genéricos? ¿El CRM recomendado es compatible con el martech-stack-audit? ¿El pricing está verificado con web search? ¿La recomendación es una decisión o una lista de opciones? ¿Los riesgos son reales o cosméticos?

## Template de output

Produce el output siguiendo exactamente esta estructura.

---

# CRM Selection Report — [NOMBRE EMPRESA]
*RevOS Activation · Versión 1.0 · [Fecha]*

---

## 1. Recomendación ejecutiva
*[Máximo 200 palabras. CRM recomendado + plan específico + coste anual de licencias + duración e inversión de implementación + razón principal en una frase. Primer párrafo. El consultor tiene que poder leerlo y saber qué recomendar.]*

**CRM recomendado:** [Nombre + Plan específico]
**Inversión licencia anual:** [€/año]
**Inversión implementación:** [€ rango]
**Ventana de go-live:** [semanas]

---

## 2. Contexto y requisitos

### 2.1 Perfil del cliente relevante para la decisión
[3-4 párrafos: tipo de negocio, volumen comercial, complejidad del proceso, equipo, restricciones críticas]

### 2.2 Requisitos ponderados
| # | Requisito | Peso | Justificación |
|---|-----------|------|---------------|
| 1 | [Requisito] | Alta | [Por qué tiene este peso en este cliente] |
| 2 | [Requisito] | Alta | [...] |
| 3 | [Requisito] | Media | [...] |
| ... | ... | ... | ... |

### 2.3 Restricciones no negociables
- Presupuesto máximo de licencia: [€/año]
- Nº de usuarios a 12 meses: [X] · a 24 meses: [Y]
- Integraciones obligatorias: [Lista]
- Idioma: [español obligatorio / inglés aceptable]
- Otras: [GDPR, sector regulado, ubicación servidores, etc.]

---

## 3. Universo de opciones y descarte

### 3.1 CRMs evaluados y descartados
| CRM | Razón de descarte |
|-----|-------------------|
| [CRM] | [Frase de descarte — precio fuera de rango, feature bloqueante, etc.] |
| [CRM] | [...] |

### 3.2 Finalistas
**Finalista 1:** [Nombre + Plan]
**Finalista 2:** [Nombre + Plan]
**Finalista 3:** [Nombre + Plan]

---

## 4. Matriz comparativa

*[Ver especificación de estructura para /revos:entrega — el XLSX editable lo genera /revos:entrega. Aquí resumen visual de los totales ponderados.]*

| Criterio | Peso | [Finalista 1] | [Finalista 2] | [Finalista 3] |
|----------|------|---------------|---------------|---------------|
| [Requisito 1] | Alta | 5 | 4 | 3 |
| [Requisito 2] | Alta | 4 | 5 | 3 |
| [Requisito 3] | Media | 3 | 4 | 5 |
| ... | ... | ... | ... | ... |
| **Total ponderado** | | **[Score]** | **[Score]** | **[Score]** |

---

## 5. Análisis de cada finalista

### 5.1 [Finalista 1 — Recomendado]
**Fortalezas en el contexto del cliente:**
- [Fortaleza concreta, no genérica]
- [Fortaleza concreta]
- [Fortaleza concreta]

**Debilidades:**
- [Debilidad concreta]
- [Debilidad concreta]

**Pricing aplicable:**
- Plan: [nombre]
- Coste por usuario/mes: [€] · [FALTA BENCHMARK si no verificado]
- Coste anual para [N] usuarios: [€]
- Add-ons necesarios: [Lista con coste]
- Coste de implementación orientativo: [€ rango]

**TCO año 1:** [€]
**TCO año 2:** [€]

### 5.2 [Finalista 2]
[Misma estructura]

### 5.3 [Finalista 3]
[Misma estructura]

---

## 6. Recomendación razonada

### 6.1 Por qué [Finalista 1]
*[3-5 párrafos de narrativa ejecutiva. No es "tiene mejor score" — es por qué encaja con este cliente concreto, qué problema resuelve mejor que los otros, cómo se comporta cuando el cliente crezca, dónde tiene el riesgo.]*

### 6.2 Por qué no [Finalista 2]
*[1-2 párrafos. Qué hace bien, por qué no gana en este caso concreto.]*

### 6.3 Por qué no [Finalista 3]
*[1-2 párrafos]*

### 6.4 Escenarios en los que la decisión cambiaría
- Si [condición] → [Finalista alternativo]
- Si [condición] → [Finalista alternativo]

---

## 7. Plan de implementación orientativo

### 7.1 Fases y duración
| Fase | Duración | Entregable |
|------|----------|------------|
| Discovery y diseño detallado | [X semanas] | [Blueprint — es `crm-blueprint-builder`] |
| Configuración | [X semanas] | [Objetos, campos, pipeline configurados] |
| Migración de datos | [X semanas] | [Contactos y deals migrados] |
| Formación del equipo | [X semanas] | [Equipo operativo] |
| Go-live + estabilización | [X semanas] | [CRM operando] |
| **Total** | **[X semanas]** | |

### 7.2 Roles necesarios
- Sponsor interno: [Perfil]
- Admin CRM interno: [Perfil, dedicación]
- Partner externo: [Si aplica — perfil, nº de horas estimadas]
- Equipo comercial en formación: [Horas por persona]

### 7.3 Inversión total implementación
**Rango:** [€ - €] · [HIPÓTESIS] si no hay cotización

### 7.4 Hitos de adopción post go-live
- **30 días:** [Qué tiene que estar funcionando]
- **60 días:** [Qué tiene que estar funcionando]
- **90 días:** [Qué tiene que estar funcionando]

---

## 8. Riesgos y plan B

### 8.1 Riesgos principales de la recomendación
| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| [Riesgo concreto] | [Alta/Media/Baja] | [Alto/Medio/Bajo] | [Acción concreta] |
| [Riesgo concreto] | [...] | [...] | [...] |
| [Riesgo concreto] | [...] | [...] | [...] |

### 8.2 Plan B
**Si [Finalista 1] se descarta por razón imprevista:** Pasar a [Finalista 2] con estos ajustes: [breve].

---

## 9. Especificación de estructura para /revos:entrega

Los ficheros finales maquetados los genera `/revos:entrega` según la preferencia de output registrada en fase 0, con esta estructura:

**DOCX formal:** `[Cliente] - CRM Selection v1.docx` — narrativa completa del report + matriz resumen.

**XLSX de scoring:** `[Cliente] - CRM Selection v1.xlsx` — matriz de scoring editable: requisitos en filas, finalistas en columnas, score 1-5 por celda, peso del requisito editable, score ponderado calculado automáticamente, fila final con total ponderado recalculado al modificar pesos.

---

## 10. Vacíos e hipótesis

**Información que falta:** [[FALTA DATO]] — especialmente presupuesto real y nº de usuarios a 24 meses
**Benchmarks no verificados:** [[FALTA BENCHMARK]] — pricing de add-ons, coste típico de implementación
**Hipótesis críticas:** [[HIPÓTESIS]] — volumen de pipeline, cadencia de adopción

---

## 11. Decisión y próximos pasos

### 11.1 Decisión recomendada
[CRM + Plan + Coste anual + Ventana de implementación]

### 11.2 Próximos pasos inmediatos
1. Validación de la recomendación con el cliente
2. Solicitud de cotización formal a [proveedor] o partner certificado
3. Pasar a `crm-blueprint-builder` con el CRM seleccionado
4. Si hay dudas, ejecutar demo guiada con [Finalista 1] y [Finalista 2] antes de decidir

---

## Entrega

Cuando el report esté completo:

1. Presenta el output en Markdown.
2. Añade al final una sección **"Resumen para el consultor"** con:
   - CRM recomendado + plan
   - TCO año 1 orientativo
   - Finalistas descartados y por qué
   - Gaps ([FALTA DATO] / [FALTA BENCHMARK] críticos)
   - Nivel de confianza en la recomendación (1-5)
3. El contenido validado se guarda como `[Cliente] - CRM Selection v1.md` en `01 Entregables`. El orquestador lo registra en el Registro. El DOCX y el XLSX finales los genera `/revos:entrega` según la preferencia de output registrada en fase 0. Siguiente skill: `crm-blueprint-builder`.

## Lo que NO debes hacer

- No compares más de tres finalistas — la matriz se diluye y la decisión se difumina.
- No asignes pesos al azar — cada peso se justifica con el contexto del cliente.
- No afirmes pricing sin web search de verificación — el pricing de los CRMs cambia.
- No escondas los riesgos — toda elección tiene 2-3 riesgos reales.
- No termines con "depende del cliente" — el skill entrega una decisión, no un menú.
- No recomiendes el CRM que tú prefieres como consultor — recomiendas el que encaja con este cliente.
- No ignores el martech-stack-audit — la integración con herramientas existentes es criterio crítico.
- No generes tú los ficheros DOCX/XLSX finales — el skill produce contenido validado en Markdown; la maquetación corresponde a `/revos:entrega`.
