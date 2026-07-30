---
name: diagnostic-checkpoint
description: >
  Usar cuando el consultor necesite producir el material de checkpoint con el cliente para validar una fase
  completa del sistema (Diagnostic, Design Essentials, Design Complete o Activation) antes de continuar.
  Es el hito de validación que garantiza alineación con el cliente antes de seguir generando entregables.
  Activar al final de cada fase. También activar si el consultor pide "prepara el checkpoint", "material para
  la reunión de validación", "presentación del diagnóstico" o "dossier de cierre de fase".
---

# Diagnostic Checkpoint

## Propósito

Este skill produce el material de checkpoint: la presentación y documento que el consultor lleva a la reunión de validación con el cliente al cierre de una fase. No es un resumen de lo hecho — es un instrumento de decisión. El cliente tiene que salir de esa reunión con claridad sobre (a) qué hemos encontrado, (b) qué implica, (c) qué decisiones hay que tomar para continuar.

El entregable tiene dos formatos complementarios: un artefacto HTML presentable (para conducir la reunión) y un documento formal extenso (para que quede constancia escrita y que el cliente pueda compartir internamente). Este skill produce el contenido validado en Markdown y la especificación de ambos formatos; la materialización final la genera `/revos:entrega` según la preferencia de output registrada en fase 0.

Aunque se llama "diagnostic-checkpoint" por consistencia con el nombre original del sistema, funciona para cualquier fase: Diagnostic, Design o Activation. Se adapta según la fase que se está cerrando.

## Posición en el pipeline

**Requiere:** todos los outputs de la fase que se está cerrando. Por defecto, el checkpoint de Diagnostic requiere brief, knowledge base, competitive research y revenue diagnostic.

**Produce:** Checkpoint [Fase] v1 — contenido validado en Markdown, con la especificación del artefacto HTML de presentación y del documento formal extenso (la materialización la genera `/revos:entrega`).

**Siguiente skill:** el primer skill de la siguiente fase, tras validación del cliente. Si el cliente no valida, vuelta atrás al skill correspondiente para ajustar.

## Principios de ejecución

**Checkpoint = instrumento de decisión.** Todo el material está diseñado para que el cliente tome decisiones, no para que admire el trabajo. Cada sección debe terminar con algo que el cliente tenga que confirmar, validar o decidir.

**Densidad calibrada.** El artefacto HTML es ligero — lo que se muestra en reunión. El documento formal es denso — lo que queda después. Ambos cuentan la misma historia, con distinto nivel de detalle.

**Preguntas explícitas al cliente.** Cada checkpoint termina con 3-7 preguntas concretas que el cliente tiene que responder para continuar. No preguntas abiertas — preguntas de decisión.

**Honestidad con vacíos e hipótesis.** El checkpoint no esconde los [FALTA DATO] ni las [HIPÓTESIS]. Al contrario, las hace visibles como las decisiones que requieren input del cliente. Esto genera confianza, no duda.

**Convenciones v4:** cada [FALTA DATO] se clasifica al detectarse como bloqueante (impide una decisión de este entregable) o no bloqueante. Presupuesto máximo: 2 ciclos de revisión por entregable. Agotado el presupuesto, los [FALTA DATO] no bloqueantes se convierten en [ASUNCIÓN: valor asumido + criterio] y el sistema avanza; solo los bloqueantes detienen y se escalan al cliente de inmediato. Los datos extraídos de CRM conectado se marcan [DATO CRM: fuente, fecha]. Referencia completa: skills/revos-orchestrator/references/convenciones.md del plugin revos.

**Lenguaje.** Castellano. Registro ejecutivo directo. El cliente es el destinatario directo, así que el tono es el de una conversación de dirección, no el de un informe interno.

## Proceso

**Paso 1 — Identificar la fase en curso.**
Confirma con el consultor (o infiere del contexto) qué fase se está cerrando: Diagnostic, Design (Essentials/Complete) o Activation. El template se adapta según la fase.

**Paso 2 — Inventario de outputs de la fase.**
Enumera todos los outputs producidos en la fase. Para el checkpoint de Diagnostic serán típicamente 4: brief, knowledge base, competitive, revenue diagnostic.

**Paso 3 — Extracción de lo esencial.**
Por cada output, extrae lo esencial: la tesis principal, los 2-3 insights más importantes, los vacíos críticos. No reproduzcas outputs — síntesis.

**Paso 4 — Identificación de decisiones.**
Articula las 3-7 decisiones que el cliente tiene que tomar para que la siguiente fase avance. Tienen que ser decisiones reales (elección entre opciones), no preguntas genéricas.

**Paso 5 — Construcción narrativa.**
Organiza el material como una narrativa, no como un índice. La historia tiene que fluir: contexto → hallazgos → implicaciones → decisiones.

**Paso 6 — Especificación del artefacto HTML presentable.**
Especifica el HTML como slides o secciones navegables. Pocos elementos por "slide", tipografía grande, jerarquía visual clara. Destinado a proyectarse en reunión. La materialización del artefacto la genera `/revos:entrega`.

**Paso 7 — Especificación del documento formal denso.**
El documento formal incluye todo lo que el HTML no puede incluir: argumentación extendida, evidencias, citas, referencias a los outputs originales. La materialización del documento la genera `/revos:entrega` según la preferencia de output registrada en fase 0.

## Template de output (Markdown base, adaptable)

Produce el output siguiendo exactamente esta estructura.

---

# Checkpoint [FASE] — [NOMBRE EMPRESA]
*RevOS · [Fase que se cierra] · [Fecha]*

---

## 1. Propósito de esta sesión
*[2-3 frases. Qué vamos a revisar hoy, qué decisiones tenemos que tomar para que RevOS continúe, cuánto tiempo aproximado.]*

---

## 2. Contexto y alcance
**Qué incluyó esta fase:** [Resumen del alcance — skills ejecutados, outputs producidos]
**Qué materiales del cliente hemos utilizado:** [Inputs consumidos]
**Cuándo empezamos y dónde estamos:** [Fechas, hitos cumplidos]

---

## 3. Los hallazgos
*[La sección central del checkpoint. Articulada como 3-5 hallazgos clave, cada uno con un nombre claro, descripción y evidencia. Estos hallazgos son los que el cliente tiene que validar antes de seguir.]*

### Hallazgo 1 — [Nombre]
**Qué hemos encontrado:** [Enunciado claro del hallazgo]
**Por qué es relevante:** [Qué implica para el revenue]
**Evidencia que lo sustenta:** [Qué datos/fuentes lo soportan]
**Qué necesitamos validar contigo:** [Lo que pedimos confirmación explícita al cliente]

### Hallazgo 2 — [Nombre]
[Misma estructura]

### Hallazgo 3 — [Nombre]
[Misma estructura]

*[Máximo 5 hallazgos. Menos es más — el cliente no puede procesar más de 5 hallazgos en una reunión.]*

---

## 4. La lectura integrada

### 4.1 Tesis central
[Una frase. La lectura que integra todos los hallazgos en una interpretación coherente. Para el checkpoint de Diagnostic, es la tesis del revenue-diagnostic. Para el de Design, es la tesis del sistema propuesto.]

### 4.2 Qué implica esto para el cliente
[Qué cambia en cómo el cliente piensa su revenue después de esta fase — expresado desde su perspectiva, no la nuestra]

### 4.3 Qué NO hemos encontrado
[Cosas que el cliente podría esperar y que no están. Gestión de expectativas explícita.]

---

## 5. Decisiones a tomar hoy

**Decisión 1 — [Título de la decisión]**
**Contexto:** [Por qué hace falta decidir esto]
**Opciones:** [2-3 opciones claras]
**Nuestra recomendación:** [Con argumento breve]
**Qué necesitamos de ti:** [Decisión concreta o plazo para decidir]

**Decisión 2 — [Título]**
[Misma estructura]

*[Máximo 7 decisiones. Típicamente 3-5. Si son más, el checkpoint no está bien priorizado.]*

---

## 6. Vacíos e hipótesis a resolver

### 6.1 Información que necesitamos del cliente
[Los [FALTA DATO] críticos para seguir — lista priorizada, indicando cuáles son bloqueantes]

### 6.2 Hipótesis que requieren validación
[Los [HIPÓTESIS] que hemos hecho y que pedimos confirmar o ajustar]

### 6.3 Contradicciones detectadas
[Si hay [CONTRADICCIÓN DETECTADA] sin resolver, listarlas aquí con claridad]

---

## 7. Asunciones vigentes
[Lista de todas las [ASUNCIÓN] del State Log con su valor asumido y criterio. El cliente valida o corrige cada una. Las corregidas entran por el flujo de cambio (`/revos:cambio`) como cambio de Dato o de Concepto según afecte.]

---

## 8. Siguiente fase

### 8.1 Qué pasa si validamos hoy
[Qué es lo primero que haremos tras la validación y en qué plazo]

### 8.2 Alcance recomendado
[Confirmación o ajuste del alcance (Essentials / Complete / Activaciones opcionales) dado lo aprendido]

### 8.3 Hitos de la siguiente fase
[Los 3-5 hitos de la siguiente fase, con fecha estimada]

---

## 9. Apéndices
*[Sección del documento formal, no del artefacto HTML]*
- **Anexo A:** Client Master Brief completo
- **Anexo B:** Knowledge Base completa
- **Anexo C:** Competitive Landscape completo
- **Anexo D:** Revenue Diagnostic completo
- **Anexo E:** Lista completa de fuentes consultadas

---

## Entrega y reglas de cierre

Cuando el checkpoint esté completo:

1. Presenta el Markdown completo como guion/base.
2. Incluye la especificación del artefacto HTML presentable — estructura navegable tipo slides, tipografía grande, jerarquía visual clara, colores sobrios, diseñado para proyectarse en reunión con el cliente. La materialización la genera `/revos:entrega` según la preferencia de output registrada en fase 0.
3. Incluye la especificación del documento formal con el contenido extendido y los apéndices. La materialización la genera `/revos:entrega`.
4. Añade al final una sección **"Resumen para el consultor"** con:
   - Fase que se está cerrando
   - Número de hallazgos y número de decisiones a tomar
   - La decisión más crítica para la continuidad del proyecto
   - Nivel de confianza en la validación (alta / media / baja) y por qué
   - Riesgos identificados para la reunión (temas sensibles, posibles desacuerdos)
5. Después de la reunión, actualiza este checkpoint con las decisiones validadas. El contenido validado se guarda como `[Cliente] - Checkpoint [Fase] Validado v1.md` en `01 Entregables`. El orquestador lo registra en el State Log. Siguiente skill: el primer skill de la siguiente fase, solo una vez recibida la validación del cliente.
6. Ningún checkpoint se celebra con cambios en estado pendiente en el Backlog de cambios.

## Lo que NO debes hacer

- No generes un checkpoint que sea un resumen neutro — el checkpoint empuja decisiones.
- No incluyas más de 5 hallazgos ni más de 7 decisiones — satura al cliente.
- No escondas [FALTA DATO] ni [HIPÓTESIS] para parecer más seguro — el cliente las tiene que ver.
- No cambies el orden de las secciones — el orden está diseñado para conducir la reunión.
- No uses el mismo checkpoint para dos fases distintas — cada fase requiere articular sus hallazgos y sus decisiones.
- No generes los ficheros finales maquetados (HTML, DOCX) — este skill produce contenido validado en Markdown con la especificación de ambos formatos; los ficheros finales los genera `/revos:entrega`.
- No avances al siguiente skill sin confirmación del consultor de que la reunión con el cliente se ha celebrado y ha sido validada.
