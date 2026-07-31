---
name: knowledge-base-builder
description: >
  Usar cuando el consultor necesite enriquecer y estructurar la base de conocimiento comercial, estratégica y
  operativa del cliente, partiendo del Client Master Brief y de materiales adicionales (decks, propuestas,
  informes, web, casos de cliente, entrevistas internas, notas). Activar siempre después de brief-intake y
  antes de competitive-research. También activar si el consultor pide "enriquece el brief", "construye la base
  de conocimiento", "profundiza en el cliente" o "consolida todo lo que sabemos de [cliente]".
---

# Knowledge Base Builder

## Propósito

Este skill produce la Knowledge Base del cliente: el documento consolidado que integra el Client Master Brief con toda la información adicional disponible (materiales del cliente, web, decks, casos, entrevistas internas). Es la "fuente única de verdad" que alimentará todos los skills de Design y Activation.

La diferencia con el brief es de profundidad y enriquecimiento: el brief captura lo declarado. La knowledge base integra, cruza fuentes, detecta patrones, identifica tensiones no declaradas y articula lo que la empresa sabe sobre sí misma pero no ha puesto en palabras.

## Posición en el pipeline

**Requiere:** Client Master Brief v1 (obligatorio) + todos los materiales del cliente disponibles en el proyecto (decks, propuestas, web, casos, entrevistas, informes internos).

**Produce:** Knowledge Base v1 en Markdown estructurado. Documento de referencia que se usa como input en todos los skills posteriores.

**Siguiente skill:** competitive-research (usa la knowledge base para contextualizar el análisis competitivo).

## Principios de ejecución

**Jerarquía de fuentes.** (1) Client Master Brief validado, (2) materiales internos del cliente (decks, propuestas, informes), (3) web y contenido público del cliente, (4) notas de entrevistas internas. Cuando haya contradicción entre fuentes, prevalece la más reciente y la más específica. Marca las contradicciones con [CONTRADICCIÓN DETECTADA].

**Integración, no copia.** No reproduzcas el brief literalmente. La knowledge base lo integra, lo enriquece y lo reorganiza. Toda información debe estar sintetizada con criterio propio — cruza datos de distintas fuentes y articula patrones.

**Detectar lo no dicho.** La parte más valiosa de la knowledge base es lo que el cliente no ha articulado explícitamente: tensiones entre lo que dice y lo que hace, supuestos implícitos sobre su mercado, creencias internas que condicionan decisiones. Identifícalo y márcalo como [OBSERVACIÓN] para diferenciarlo de los datos declarados.

**Vacíos y hipótesis.** Usa [FALTA DATO: descripción] cuando necesites información que no está en ningún material. Usa [HIPÓTESIS] para inferencias estratégicas que requieren validación. No inventes.

**Convenciones v4.1 — **Precondición**: antes de producir, lee `00 Sistema/[Cliente] - Registro` y detente si falta fase 0, si el presupuesto de revisión de este entregable está agotado sin cambio tramitado por /revos:cambio, o si el cierre de fase anterior exigía un system-qa aún no APTO. **Etiquetado**: cada [FALTA DATO] se clasifica al detectarse como bloqueante (impide una decisión de este entregable) o no bloqueante. **Presupuesto**: 2 ciclos de revisión de calidad por entregable — solo consumen ciclo los cambios nacidos del juicio sobre lo escrito; las incorporaciones de información nueva (aportada por cliente o consultor, o medida por el sistema) no consumen ciclo y generan versión y entrada en el Backlog si el entregable ya está registrado. Agotado el presupuesto, los [FALTA DATO] no bloqueantes se convierten en [ASUNCIÓN: valor asumido + criterio falsable] y el sistema avanza; solo los bloqueantes detienen y se escalan de inmediato. **Resumen para el consultor**: enumera los bloqueantes y lo relevante — nunca recuentos totales (el recuento es chequeo mecánico de system-qa sobre el documento terminado). **Cierre**: todo [FALTA DATO] heredado sale con disposición explícita — resuelto, reasignado a la primera skill no ejecutada que lo necesite, o declinado con motivo. Datos de CRM conectado: [DATO CRM: fuente, fecha]. Referencia completa: skills/revos-orchestrator/references/convenciones.md del plugin revos.

**Lenguaje.** Castellano. Registro ejecutivo directo. El vocabulario correcto: revenue, pipeline, posicionamiento, ciclo de venta, cualificación, GTM, categoría, segmentos, ticket medio, ACV, CAC, LTV, pipeline velocity.

**Longitud.** La knowledge base es el documento más largo del Diagnostic. Típicamente 15-25 páginas. No por rellenar — por contenido real. Si con los materiales disponibles no llegas a 10 páginas con criterio, el problema es de inputs, no de output: dilo al consultor.

## Proceso

**Paso 1 — Inventario exhaustivo de inputs.**
Antes de escribir, enumera todos los materiales disponibles del proyecto: brief, decks, web, casos, propuestas, informes, notas. Para cada uno, anota mentalmente qué tipo de información aporta. Si solo tienes el brief y nada más, avisa al consultor — la knowledge base quedará limitada.

**Paso 2 — Lectura transversal con foco en tensiones.**
Lee todos los materiales buscando específicamente: (a) afirmaciones contradictorias entre fuentes, (b) términos que el cliente usa repetidamente (pueden ser pistas de posicionamiento), (c) supuestos implícitos no declarados, (d) descripciones de clientes reales que difieren del ICP declarado.

**Paso 3 — Mapa de fuentes por sección.**
Antes de redactar, mapea qué fuente alimenta cada sección del template. Esto asegura que no se pierde información y que cada sección tiene sustento real.

**Paso 4 — Medición de activos (F5).**
Con los conectores activos del proyecto (Ahrefs, Similarweb y los de nivel 2 que declare el Registro), mide el dominio del cliente y, si están disponibles, los dominios de sus clientes y de sus competidores directos. Como mínimo: autoridad de dominio, keywords orgánicas, tráfico orgánico, histórico de 12-18 meses, perfil de enlaces y citaciones en motores generativos (Brand Radar). Marca cada cifra como [DATO MEDIDO: herramienta, fecha]. Contrasta lo medido con lo que el cliente declara: toda divergencia es material de la sección de observaciones. Un diagnóstico construido sobre lo medible por terceros vale más que uno construido sobre lo que el cliente cuenta.

**Paso 5 — Redacción integrada.**
Sigue el template al pie de la letra. En cada sección, integra fuentes — no las yuxtapongas. Si una sección solo tiene una fuente, indícalo con [FUENTE ÚNICA] al final de la sección.

**Paso 6 — Sección de observaciones estratégicas.**
Después de completar el template, dedica tiempo a la sección "Observaciones y señales" — es la más valiosa del documento. Aquí es donde el valor se crea: patrones, tensiones, creencias implícitas, brechas entre discurso y práctica.

**Paso 7 — Revisión de coherencia.**
Antes de entregar, verifica:
- ¿El ICP declarado es coherente con los casos reales descritos?
- ¿La propuesta de valor articulada coincide con cómo se presenta la empresa en su web?
- ¿Las capacidades descritas son consistentes con el tamaño y madurez del equipo?
- ¿Las métricas declaradas (ticket, ciclo, tasa cierre) son internamente coherentes?
Si detectas incoherencias, márcalas con [CONTRADICCIÓN DETECTADA] en la sección correspondiente.

## Template de output

Produce el output siguiendo exactamente esta estructura. No añadas secciones. Si una sección no tiene información, déjala con [FALTA DATO: descripción].

---

# Knowledge Base — [NOMBRE EMPRESA]
*RevOS Diagnostic · Versión 1.0 · [Fecha]*
*Documento consolidado · Fuente única de verdad para los siguientes skills*

---

## 1. Sumario ejecutivo
*[Máximo 250 palabras. Lo esencial del cliente en dos párrafos: qué hace, a quién, por qué es relevante hoy hablar de revenue, qué hipótesis central tenemos sobre dónde está el cuello de botella. Este sumario lo leerá todo consumidor posterior del documento.]*

---

## 2. Contexto estratégico

### 2.1 Identidad y trayectoria
[Origen de la empresa, evolución hasta hoy, hitos relevantes, fundadores activos o no]

### 2.2 Modelo de negocio
[Cómo genera revenue hoy con detalle — tipología de contratos, estructura de precios si es pública, mix de recurrente/no recurrente, dependencia de proyectos vs. plataforma]

### 2.3 Momento de mercado
[Dinámicas del sector que afectan al cliente hoy: consolidación, regulación, cambios tecnológicos, madurez de la categoría]

### 2.4 Posicionamiento declarado
[Cómo se posiciona la empresa públicamente — qué frases usa en su web, en sus decks, cómo se autodenomina]

---

## 3. Oferta y propuesta de valor

### 3.1 Cartera actual
[Descripción detallada de productos/servicios — qué son exactamente, a qué problema responden, cómo se entregan]

### 3.2 Modelo de pricing
[Estructura de precios, lógica de pricing, variabilidad por cliente, niveles o tiers si existen]

### 3.3 Propuesta de valor declarada vs. percibida
[Qué dice la empresa que ofrece vs. qué dicen los clientes que reciben — si hay material que permita contrastarlo]

### 3.4 Diferenciación real
[Tras cruzar fuentes: qué diferencia realmente a esta empresa en el mercado, más allá del discurso]

---

## 4. Clientes y segmentos

### 4.1 Base de clientes actual
[Descripción de la base — tamaños típicos, sectores, tipos de proyecto, geografía]

### 4.2 ICP objetivo declarado
[El cliente ideal según la empresa]

### 4.3 ICP real observado
[El cliente que efectivamente compra y se queda — si es distinto al declarado, [CONTRADICCIÓN DETECTADA]]

### 4.4 Casos de referencia
[Casos de cliente concretos mencionados — qué compraron, por qué, cuánto tiempo duró el ciclo, por qué eligieron a esta empresa]

### 4.5 Decisores e influenciadores
[Mapa de personas que intervienen en la decisión de compra — roles, preocupaciones, objeciones típicas]

---

## 5. Funnel y motor comercial

### 5.1 Fuentes de demanda
[De dónde vienen los clientes — con % si se puede estimar. Diferencia referidos/inbound/outbound/partners/eventos]

### 5.2 Proceso comercial actual
[Etapas del proceso desde primer contacto hasta cierre — descripción narrativa, no diagrama]

### 5.3 Cualificación
[Cómo se cualifica hoy — formal o informal, criterios usados, quién cualifica]

### 5.4 Métricas clave
[Ticket medio, ciclo de venta, tasa de cierre — con fuente y nivel de confianza]

### 5.5 Herramientas y stack
[CRM, automatización, email, analytics — uso real, no teórico]

---

## 6. Marketing y generación de demanda

### 6.1 Actividad actual
[Qué hace marketing hoy — canales, contenidos, frecuencia]

### 6.2 Posicionamiento y mensajes
[Cómo comunica la empresa — mensajes recurrentes, tono, canales]

### 6.3 Contenido y discoverability
[Qué contenido produce, para quién, con qué frecuencia, qué visibilidad tiene en buscadores/IA]

### 6.4 Dependencia de canales
[Sobre qué canal descansa la generación de demanda hoy — y qué pasaría si ese canal se rompe]

---

## 7. Equipo y capacidades

### 7.1 Estructura comercial
[Organigrama comercial — roles, responsabilidades, territorios, incentivos]

### 7.2 Estructura de marketing
[Organigrama de marketing si existe — roles, capacidades, experiencia]

### 7.3 RevOps / Operaciones
[Si existe — quién gestiona CRM, datos, procesos transversales]

### 7.4 Dependencia del founder
[En qué actividades de revenue sigue participando el founder y por qué]

### 7.5 Gaps de capacidad
[Qué capacidades faltan en el equipo actual para ejecutar la estrategia declarada]

---

## 8. Objetivos, restricciones y contexto de decisión

### 8.1 Objetivos declarados
[Qué quiere conseguir el cliente con RevOS — expresado como resultado]

### 8.2 Criterios de éxito
[Cómo medirá el cliente que RevOS ha funcionado]

### 8.3 Restricciones duras
[Presupuesto, tiempo, tecnología, governance — lo que no se puede mover]

### 8.4 Restricciones blandas
[Preferencias, inercias organizacionales, sensibilidades políticas]

### 8.5 Apetito al cambio
[Qué dispuesta está la organización a cambiar — evaluación realista, no declarada]

---

## 9. Observaciones y señales
*[La sección más valiosa del documento. Aquí articulas lo que NO está dicho explícitamente en ninguna fuente pero emerge del cruce de todas.]*

### 9.1 Tensiones entre discurso y práctica
[[OBSERVACIÓN] Donde la empresa dice una cosa pero hace otra — sin juicio, como dato]

### 9.2 Supuestos implícitos
[[OBSERVACIÓN] Creencias sobre su mercado, sus clientes o su modelo que la empresa da por ciertas pero no ha examinado]

### 9.3 Patrones emergentes
[[OBSERVACIÓN] Patrones que se repiten en los datos cuando cruzas fuentes — en tipos de cliente, objeciones, fuentes de demanda]

### 9.4 Oportunidades no articuladas
[[HIPÓTESIS] Oportunidades que la empresa no ha verbalizado pero que son visibles desde fuera]

### 9.5 Riesgos no articulados
[[HIPÓTESIS] Riesgos que la empresa no está viendo o no está nombrando]

---

## 10. Vacíos, hipótesis y contradicciones

**Información que falta:** [Lista de [FALTA DATO] identificados]
**Hipótesis del consultor:** [Lista de [HIPÓTESIS] que requieren validación]
**Contradicciones detectadas:** [Lista de [CONTRADICCIÓN DETECTADA]]
**Preguntas para el cliente:** [Las 3-5 preguntas más importantes que el consultor debería resolver antes de continuar]

---

## Entrega

Cuando la knowledge base esté completa:

1. Presenta el output completo en Markdown.
2. Añade al final una sección **"Resumen para el consultor"** con:
   - Las fuentes utilizadas, listadas por tipo — sin recuento
   - Densidad de contenido (alta/media/baja) y por qué
   - Los [FALTA DATO] bloqueantes, las [HIPÓTESIS] pendientes de validación y las [CONTRADICCIÓN DETECTADA], listados uno a uno — sin recuentos totales.
   - Las 3 observaciones más valiosas de la sección 9
   - Tu evaluación de la profundidad alcanzada (1-5) con frase explicativa
   - Recomendación: proceder a competitive-research o volver a recoger información
3. El contenido validado se guarda como `[Cliente] - Knowledge Base v1.md` en `01 Entregables`. El orquestador lo registra en el Registro. Siguiente skill: competitive-research.

## Lo que NO debes hacer

- No reproduzcas el brief literalmente — la knowledge base lo integra y lo enriquece, no lo copia.
- No inventes información que no está en las fuentes, aunque "sería lógico" para el sector.
- No marques como [OBSERVACIÓN] algo que es simplemente un dato declarado por el cliente.
- No produzcas el fichero final maquetado (DOCX/XLSX/PPTX) — este skill produce contenido validado en Markdown; el fichero final lo genera `/revos:entrega` según la preferencia de output registrada en fase 0.
- No avances a competitive-research sin confirmación del consultor.
- No uses la knowledge base de otro cliente como referencia aunque sea del mismo sector.
