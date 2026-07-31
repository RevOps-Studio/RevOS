---
name: brand-copy-system
description: >
  Usar cuando el consultor necesite sistematizar el copy del cliente para ser consistente con el positioning
  a través de todos los canales: tono de voz, estructura de mensajes por etapa/canal, frases aprobadas y
  prohibidas, guía de titulares/CTAs. Activar como skill opcional de Activation cuando el cliente necesite
  asegurar coherencia de mensaje a escala (varios redactores, agencias externas, o equipo grande). También
  activar si el consultor pide "tono de voz", "guía de estilo", "sistema de copy" o "mensajes consistentes".
---

# Brand Copy System

## Propósito

Este skill produce el sistema de copy del cliente: una guía operativa que permite que cualquier persona (interna o externa) redacte pieza por pieza manteniendo consistencia con el posicionamiento, el tono de voz y los mensajes estratégicos. Cubre: tono de voz, estructura recomendada por tipo de pieza, glosario, frases aprobadas y prohibidas, guía de titulares y CTAs, ejemplos buenos y malos.

No es un libro de estilo creativo ni una guía gráfica. Es el sistema que permite que el positioning se exprese sin degradarse cada vez que alguien escribe una landing, un email o un anuncio.

## Posición en el pipeline

**Requiere:** Positioning & Messaging validado. Recomendado: Content & Discoverability Design, Channel Strategy Design.

**Produce:** Brand Copy System v1 en Markdown. El documento formal para compartir con agencias, freelances y equipo lo genera `/revos:entrega` según la preferencia de output registrada en fase 0.

**Siguiente skill:** Ninguno obligatorio (es skill opcional).

## Principios de ejecución

**El copy al servicio del posicionamiento.** Tono, mensajes y palabras se derivan del positioning — no son ejercicios creativos independientes. Un sistema de copy bueno hace visible el posicionamiento en cada pieza.

**Reglas sobre gusto personal.** Decisiones de estilo explícitas reducen discusiones subjetivas. "Usamos voz activa, no pasiva" es una regla. "Preferimos que suene dinámico" no lo es.

**Frases aprobadas y prohibidas.** Lista explícita de formulaciones bendecidas y formulaciones vetadas. Ejemplo prohibido: "transformamos tu negocio". Ejemplo aprobado para un cliente concreto: "asumimos objetivos comerciales contigo".

**Ejemplos > reglas abstractas.** Para cada regla, al menos un ejemplo bueno y uno malo. Las reglas sin ejemplos se interpretan de 5 formas distintas.

**Estructura por tipo de pieza.** La estructura de un email outbound es distinta de la de una landing page. El sistema define plantillas de estructura para los tipos de pieza más frecuentes.

**Titulares y CTAs priorizados.** En B2B el titular y el CTA determinan la mayor parte de la conversión. El sistema les dedica sección propia.

**Convenciones v4.1 — **Precondición**: antes de producir, lee `00 Sistema/[Cliente] - Registro` y detente si falta fase 0, si el presupuesto de revisión de este entregable está agotado sin cambio tramitado por /revos:cambio, o si el cierre de fase anterior exigía un system-qa aún no APTO. **Etiquetado**: cada [FALTA DATO] se clasifica al detectarse como bloqueante (impide una decisión de este entregable) o no bloqueante. **Presupuesto**: 2 ciclos de revisión de calidad por entregable — solo consumen ciclo los cambios nacidos del juicio sobre lo escrito; las incorporaciones de información nueva (aportada por cliente o consultor, o medida por el sistema) no consumen ciclo y generan versión y entrada en el Backlog si el entregable ya está registrado. Agotado el presupuesto, los [FALTA DATO] no bloqueantes se convierten en [ASUNCIÓN: valor asumido + criterio falsable] y el sistema avanza; solo los bloqueantes detienen y se escalan de inmediato. **Resumen para el consultor**: enumera los bloqueantes y lo relevante — nunca recuentos totales (el recuento es chequeo mecánico de system-qa sobre el documento terminado). **Cierre**: todo [FALTA DATO] heredado sale con disposición explícita — resuelto, reasignado a la primera skill no ejecutada que lo necesite, o declinado con motivo. Datos de CRM conectado: [DATO CRM: fuente, fecha]. Referencia completa: skills/revos-orchestrator/references/convenciones.md del plugin revos.

**Lenguaje.** Castellano (u otros idiomas del cliente con adaptación). Registro ejecutivo directo en la guía. Vocabulario: tono, voz, mensaje, pilar, CTA, titular, micro-copy, glosario. Evitar: "alma de marca", "brand mantra" si no aporta, "storytelling" vacío.

## Proceso

**Paso 1 — Extracción del positioning.**
Relee el positioning: categoría, promesa, pilares de mensaje, tagline. Todo lo que sigue deriva de aquí.

**Paso 2 — Definición del tono de voz.**
Usa dimensiones calibradas (ej. formal↔cercano, técnico↔divulgativo, serio↔con humor, cauto↔directo). Posiciona al cliente en cada dimensión con argumento. Típicamente 4-6 dimensiones.

**Paso 3 — Glosario corporativo.**
Términos del sector que el cliente usa con significado propio; términos técnicos que sí se usan y cómo se escriben; siglas que se definen siempre o que ya no se definen; nombres propios de producto/metodología.

**Paso 4 — Frases aprobadas.**
Formulaciones canónicas para expresar los pilares. Una por pilar mínimo. Estas son las que el equipo puede usar literalmente.

**Paso 5 — Frases prohibidas.**
Formulaciones que el cliente ha decidido no usar: clichés del sector, expresiones de la competencia, palabras vacías que diluyen el posicionamiento.

**Paso 6 — Guía de titulares.**
Reglas: extensión, estructura (problema + promesa / promesa + mecanismo / pregunta + respuesta), uso de cifras, uso de nombres propios. Con 10-15 ejemplos buenos y 5 ejemplos malos.

**Paso 7 — Guía de CTAs.**
Reglas: verbos preferidos, verbos evitados, especificidad ("Agenda una reunión de 20 min" vs "Contáctanos"), longitud, colocación.

**Paso 8 — Estructuras por tipo de pieza.**
Plantilla de estructura (no plantilla de texto) para: landing page, email outbound, email nurturing, post LinkedIn, anuncio de búsqueda, anuncio social, whitepaper, caso de éxito.

**Paso 9 — Ejemplos completos de aplicación.**
1-2 ejemplos completos para cada tipo de pieza principal, mostrando el sistema aplicado.

**Paso 10 — Checklist de revisión.**
Lista corta (8-12 puntos) que cualquier redactor o revisor puede usar antes de publicar.

**Paso 11 — Cierre del contenido validado.**
El skill entrega el contenido completo en Markdown. El documento formal maquetado (para agencias, freelances y equipo) lo genera `/revos:entrega` según la preferencia de output registrada en fase 0 — no se produce aquí.

## Template de output

Produce el output siguiendo exactamente esta estructura.

---

# Brand Copy System — [NOMBRE EMPRESA]
*RevOS Activation · Versión 1.0 · [Fecha]*

---

## 1. Sumario ejecutivo
*[Máximo 200 palabras. Para qué sirve este documento, a quién va dirigido, cómo usarlo.]*

---

## 2. Anclaje en el posicionamiento

### 2.1 Categoría
[Recordatorio breve]

### 2.2 Promesa central
[Recordatorio breve]

### 2.3 Pilares de mensaje
[Recordatorio breve]

### 2.4 Tagline si existe
[Recordatorio breve]

---

## 3. Tono de voz

### 3.1 Dimensiones calibradas
| Dimensión | Polo A | Polo B | Posición [NOMBRE EMPRESA] |
|-----------|--------|--------|---------------------------|
| Registro | Formal | Cercano | [Ej. Cercano con rigor] |
| Tecnicismo | Técnico | Divulgativo | [Ej. Técnico para decisores] |
| Humor | Serio | Con humor | [Ej. Serio, humor solo puntual] |
| Asertividad | Cauto | Directo | [Ej. Directo sin agresividad] |
| ... | ... | ... | ... |

### 3.2 Ejemplo de voz correcta
[Pasaje de referencia]

### 3.3 Ejemplo de voz incorrecta
[Pasaje que se desvía — explicando por qué]

---

## 4. Glosario

### 4.1 Términos propios del sector
| Término | Definición operativa | Notas de uso |
|---------|---------------------|--------------|

### 4.2 Siglas
| Sigla | Significado | ¿Se define siempre? |
|-------|-------------|---------------------|

### 4.3 Nombres propios (producto, metodología)
| Nombre | Escritura correcta | Variantes vetadas |
|--------|-------------------|-------------------|

---

## 5. Frases aprobadas

### 5.1 Para el pilar 1 — [Nombre]
- "[Frase 1]"
- "[Frase 2]"
- "[Frase 3]"

### 5.2 Para el pilar 2 — [Nombre]
[Ídem]

### 5.3 Para el pilar 3 — [Nombre]
[Ídem]

### 5.4 Frases de apertura habituales
[Openers para emails, posts, landings]

### 5.5 Frases de cierre habituales
[Cierres coherentes con el tono]

---

## 6. Frases y términos prohibidos

### 6.1 Clichés del sector
[Lista con motivo de veto]

### 6.2 Expresiones de la competencia
[Lista — para diferenciación]

### 6.3 Palabras vacías
[Adjetivos que no aportan: "innovador", "disruptivo", "revolucionario", "líder", "experto", a menos que se cuantifique]

### 6.4 Errores frecuentes detectados
[Formulaciones que el equipo usa por inercia y hay que corregir]

---

## 7. Guía de titulares

### 7.1 Reglas
- Extensión recomendada: [X-Y caracteres / palabras]
- Estructura preferida: [Problema + promesa / Mecanismo claro / Cifra concreta]
- Uso de cifras: [Reglas]
- Uso de interrogación: [Cuándo sí, cuándo no]

### 7.2 Ejemplos buenos
[10-15 titulares modelo]

### 7.3 Ejemplos malos con corrección
[5 titulares con por qué están mal y cómo se corrigen]

---

## 8. Guía de CTAs

### 8.1 Reglas
- Verbos preferidos: [Lista]
- Verbos a evitar: [Lista]
- Especificidad: [Ej. incluir duración, formato, compromiso]
- Longitud: [X-Y palabras]

### 8.2 CTAs modelo por etapa del funnel
| Etapa | CTA modelo | Por qué |
|-------|------------|---------|
| TOFU | "Descarga el informe sobre [tema]" | Bajo compromiso, valor explícito |
| MOFU | "Ver la comparativa [A vs B]" | Señal de intención |
| BOFU | "Agenda una reunión de 20 min" | Compromiso, expectativa clara |

---

## 9. Estructuras por tipo de pieza

### 9.1 Landing page
**Orden recomendado:**
1. Titular (promesa clara)
2. Sub-titular (audiencia + mecanismo)
3. Prueba social breve
4. Bloque 1 — problema
5. Bloque 2 — solución
6. Bloque 3 — prueba (caso, cifra)
7. Bloque 4 — FAQ breve
8. CTA principal

**Reglas específicas:** [...]

### 9.2 Email outbound
**Orden recomendado:**
1. Asunto con gancho + contexto (≤50 caracteres)
2. Personalización específica (no genérica)
3. Problema reconocido del ICP
4. Mecanismo diferencial
5. CTA mínimo (no "demo", sí "15 min para validar si aplica")

**Reglas específicas:** [...]

### 9.3 Email nurturing
[Ídem]

### 9.4 Post LinkedIn
[Ídem]

### 9.5 Anuncio de búsqueda (SEM)
[Ídem]

### 9.6 Anuncio social
[Ídem]

### 9.7 Whitepaper / informe
[Ídem]

### 9.8 Caso de éxito
[Ídem]

---

## 10. Ejemplos completos de aplicación

### 10.1 Ejemplo de landing page
[Una landing modelo de 1 página completa]

### 10.2 Ejemplo de email outbound
[Un email modelo]

### 10.3 Ejemplo de post LinkedIn
[Un post modelo]

*[Entre 4 y 6 ejemplos completos.]*

---

## 11. Checklist de revisión pre-publicación

- [ ] ¿El titular expresa un pilar del posicionamiento?
- [ ] ¿El tono encaja en las dimensiones definidas?
- [ ] ¿Alguna frase prohibida se ha colado?
- [ ] ¿El CTA es específico y coherente con la etapa?
- [ ] ¿El texto usa voz activa mayoritariamente?
- [ ] ¿Las siglas están definidas la primera vez (si aplica)?
- [ ] ¿Las cifras llevan fuente si se presentan como hecho?
- [ ] ¿No hay adjetivos vacíos?
- [ ] ¿El mecanismo diferencial aparece con claridad?
- [ ] ¿El contenido respeta la extensión recomendada?

---

## 12. Vacíos e hipótesis

**Información que falta:** [[FALTA DATO]]
**Hipótesis críticas:** [[HIPÓTESIS]]
**Decisiones abiertas del cliente:** [Tono exacto, extensión de vetos, uso de humor]

---

## Entrega

Cuando el sistema de copy esté completo:

1. Presenta el output completo en Markdown.
2. Añade al final una sección **"Resumen para el consultor"** con:
   - Nº de dimensiones de tono calibradas
   - Nº de frases aprobadas y prohibidas
   - Tipos de pieza cubiertos
   - Nivel de confianza en el sistema (1-5)
3. El contenido validado se guarda como `[Cliente] - Brand Copy System v1.md` en `01 Entregables`. El orquestador lo registra en el Registro. El documento formal maquetado lo genera `/revos:entrega` según la preferencia de output registrada en fase 0. Siguiente skill: ninguno obligatorio (es skill opcional).

## Lo que NO debes hacer

- No inventes tono o mensajes que no se deriven del positioning.
- No redactes reglas sin ejemplos — inservibles.
- No copies clichés del sector — justamente es lo que el sistema tiene que evitar.
- No mezcles guía gráfica con guía de copy — son documentos distintos.
- No generes el documento formal maquetado — eso corresponde a `/revos:entrega`; este skill entrega el contenido validado en Markdown.
