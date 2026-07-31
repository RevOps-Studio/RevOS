---
name: brief-intake
description: >
  Usar cuando el consultor necesite convertir información inicial del cliente
  (formulario de intake completado, notas de la reunión exploratoria, web del
  cliente, decks o materiales aportados) en un Client Master Brief estructurado.
  Activar siempre como primer skill de Diagnostic en cualquier proyecto RevOS,
  antes de knowledge-base-builder o competitive-research. También activar si el
  consultor pide "procesar el intake", "generar el brief" o "arrancar el proyecto".
---

# Brief Intake

## Propósito

Este skill convierte información inicial dispersa del cliente en el Client
Master Brief — el documento base que alimenta todos los skills posteriores
del sistema RevOS.

Es el skill más importante del pipeline: su calidad determina la calidad de
todo lo que viene después. Un brief superficial produce un diagnóstico
superficial. Un brief con criterio produce un sistema con criterio.

## Posición en el pipeline

**Requiere:** formulario de intake completado (mínimo), notas de reunión,
web del cliente si está disponible, materiales existentes (decks, propuestas,
informes) si los hay. Dominios de las cuentas del cliente (sus clientes) y
de competidores directos — se piden como dato de intake, al mismo nivel que
la web propia.

**Produce:** Client Master Brief v1 en Markdown estructurado.

**Siguiente skill:** knowledge-base-builder (usa el brief como input principal).

---

## Principios de ejecución

**Prioridad de fuentes.** Cuando haya contradicción entre fuentes, usa esta
jerarquía: (1) formulario de intake firmado por el cliente, (2) notas de
reunión del consultor, (3) web y materiales públicos del cliente. Señala
cualquier contradicción con [CONTRADICCIÓN DETECTADA: descripción].

**Datos declarados vs inferencias.** Distingue siempre entre lo que el
cliente afirmó explícitamente y lo que se puede inferir. Marca las
inferencias con [HIPÓTESIS] para que el consultor pueda validarlas.

**Vacíos de información.** No inventes ni generalices para rellenar secciones
que no tienen datos reales. Usa [FALTA DATO: descripción de lo que necesitas]
y continúa con las secciones que sí puedes completar.

Convenciones v4.1 — **Precondición**: antes de producir, lee `00 Sistema/[Cliente] - Registro` y detente si falta fase 0, si el presupuesto de revisión de este entregable está agotado sin cambio tramitado por /revos:cambio, o si el cierre de fase anterior exigía un system-qa aún no APTO. **Etiquetado**: cada [FALTA DATO] se clasifica al detectarse como bloqueante (impide una decisión de este entregable) o no bloqueante. **Presupuesto**: 2 ciclos de revisión de calidad por entregable — solo consumen ciclo los cambios nacidos del juicio sobre lo escrito; las incorporaciones de información nueva (aportada por cliente o consultor, o medida por el sistema) no consumen ciclo y generan versión y entrada en el Backlog si el entregable ya está registrado. Agotado el presupuesto, los [FALTA DATO] no bloqueantes se convierten en [ASUNCIÓN: valor asumido + criterio falsable] y el sistema avanza; solo los bloqueantes detienen y se escalan de inmediato. **Resumen para el consultor**: enumera los bloqueantes y lo relevante — nunca recuentos totales (el recuento es chequeo mecánico de system-qa sobre el documento terminado). **Cierre**: todo [FALTA DATO] heredado sale con disposición explícita — resuelto, reasignado a la primera skill no ejecutada que lo necesite, o declinado con motivo. Datos de CRM conectado: [DATO CRM: fuente, fecha]. Referencia completa: skills/revos-orchestrator/references/convenciones.md del plugin revos.

**Lenguaje.** Castellano. Registro ejecutivo directo — el nivel de un informe
interno de dirección. Sin jerga de agencia ("estrategia 360", "activación de
marca", "ecosistema digital"). El vocabulario correcto: revenue, pipeline,
conversión, funnel, cualificación, ciclo de venta, ticket medio.

**Longitud.** Ajustada al contenido real. No rellenes. Si una sección tiene
tres puntos importantes, escribe tres puntos — no añadas un cuarto para que
"parezca completo".

---

## Proceso

Sigue estos pasos en orden antes de escribir ninguna sección del brief:

**Paso 1 — Inventario de inputs.**
Enumera mentalmente todos los materiales disponibles del proyecto:
formulario de intake, notas, web, decks, propuestas, informes. Si no hay
formulario de intake, detente y avisa al consultor antes de continuar.

**Calibración de la capa económica (antes de escribir).** Pregunta al
consultor: ¿la gestión financiera de este cliente es lo bastante formal
para producir cifras fiables si se piden? Si la respuesta es no, la capa
económica se escribe directamente con [ASUNCIÓN: valor + criterio falsable]
en lugar de [FALTA DATO], y el criterio se declara en el propio brief.
Esto evita producir un documento que haya que convertir acto seguido.

**Paso 2 — Primera lectura transversal.**
Lee todos los materiales sin escribir todavía. Identifica: qué está claro,
qué está en conflicto entre fuentes, qué falta. Esto evita empezar a escribir
con una imagen parcial del cliente.

**Paso 3 — Extracción de CRM (condicional).**
Si el Registro del proyecto registra un CRM conectado, lanza el agente
crm-analyst del plugin: extrae en solo lectura volúmenes por etapa, tasas de
conversión, ciclo medio, ticket medio y win rate. Incorpora cada dato con
etiqueta [DATO CRM: fuente, fecha]. Si un dato del CRM es inconsistente
(etapas vacías, fechas imposibles, duplicados masivos), márcalo
[DATO NO FIABLE] y trátalo como [FALTA DATO] — además es input relevante
para martech-stack-audit.

**Paso 4 — Mapa de vacíos.**
Antes de rellenar el template, haz una lista mental de qué secciones puedes
completar con datos reales y cuáles tendrán [FALTA DATO]. Esto calibra las
expectativas — un brief con 3 [FALTA DATO] honestos es mejor que uno con
10 secciones rellenas de generalidades.

**Paso 5 — Redacción del brief.**
Sigue el template de output al pie de la letra. No añadas secciones, no
elimines secciones aunque estén vacías — usa [FALTA DATO] si no tienes
la información.

**Paso 6 — Revisión de coherencia.**
Antes de entregar, verifica: ¿el ICP es coherente con el ciclo de venta
descrito? ¿el ticket medio tiene sentido con los segmentos identificados?
¿las restricciones del cliente son coherentes con su situación declarada?
Si detectas incoherencias, señálalas con [CONTRADICCIÓN DETECTADA].

---

## Template de output

Produce el output siguiendo exactamente esta estructura. No añadas secciones.
No elimines secciones aunque estén vacías — usa [FALTA DATO] si no tienes
la información.

---

# Client Master Brief — [NOMBRE EMPRESA]
*RevOS Diagnostic · Versión 1.0 · [Fecha]*

---

## 1. Contexto de negocio

**Sector y categoría:** [Sector, subsector, categoría de producto/servicio]
**Tamaño y madurez:** [Facturación aproximada, años en el mercado, nº empleados]
**Modelo de negocio:** [Cómo genera revenue: venta directa / canal / recurrente / proyectos]
**Momento actual:** [Situación en la que se encuentra la empresa hoy]
**Geografía:** [Mercados en los que opera actualmente y target]

---

## 2. Oferta y propuesta de valor actual

**Qué venden:** [Descripción de productos/servicios principales]
**A quién se lo venden:** [Resumen del cliente actual — no el ICP objetivo, el real]
**Por qué los eligen (según ellos):** [Razones de compra declaradas]
**Diferenciadores percibidos:** [Qué creen que los diferencia en el mercado]

> **Nota para el consultor:** si hay discrepancia entre la propuesta de valor
> declarada y los competidores identificados en el intake, señálalo aquí.

---

## 3. Segmentos objetivo e ICP

**Segmento primario:** [Descripción del cliente ideal — sector, tamaño, perfil]
**Perfil del decisor:** [Cargo, responsabilidades, preocupaciones principales]
**Perfil del influenciador:** [Quién más interviene en la decisión de compra]
**Señales de cualificación:** [Cómo saben que un lead puede convertirse en cliente]
**Segmentos secundarios:** [Si existen — con descripción breve]

---

## 4. Funnel actual y ciclo de venta

**Cómo llegan los leads hoy:** [Fuentes con estimación de % si la hay]
**Proceso de cualificación actual:** [Cómo deciden si un lead merece tiempo]
**Etapas del proceso comercial:** [Las fases por las que pasa una oportunidad]
**Ciclo medio de venta:** [Tiempo desde primer contacto hasta cierre]
**Tasa de cierre estimada:** [Si la conocen]
**Ticket medio:** [Rango de valor por cliente/contrato]

---

## 5. Stack y herramientas actuales

**CRM:** [Herramienta, nivel de uso, calidad del dato]
**Marketing:** [Herramientas de email, automatización, analytics, CMS]
**Reporting:** [Cómo miden resultados hoy]
**Otros:** [Cualquier herramienta relevante para el sistema de revenue]

---

## 6. Equipo de revenue

**Estructura comercial:** [Nº comerciales, perfiles, territorios o verticales]
**Estructura de marketing:** [Nº personas, perfiles, qué hace cada uno]
**Operaciones/RevOps:** [Si existe — quién gestiona CRM, datos, proceso]
**Dependencia del founder:** [En qué medida el founder participa en ventas activamente]

---

## 7. Objetivos declarados

**Objetivo principal:** [Lo que el cliente quiere conseguir con RevOS]
**Horizonte temporal:** [En cuánto tiempo esperan resultados]
**Métricas de éxito según el cliente:** [Cómo medirán que esto ha funcionado]

---

## 8. Restricciones conocidas

**Presupuesto:** [Rango aproximado si lo han compartido]
**Equipo:** [Limitaciones de capacidad interna]
**Tecnología:** [Restricciones de stack]
**Tiempo:** [Urgencias o plazos que condicionan el alcance]
**Otros:** [Restricciones políticas, de governance, etc.]

---

## 9. Vacíos e hipótesis

**Información que falta:** [Lista de [FALTA DATO] identificados]
**Hipótesis del consultor:** [Lista de [HIPÓTESIS] que requieren validación]
**Contradicciones detectadas:** [Lista de [CONTRADICCIÓN DETECTADA] si las hay]
**Preguntas para la siguiente sesión:** [Lo que el consultor debería preguntar
al cliente antes de continuar al siguiente skill]

---

## Entrega

Cuando el brief esté completo:

1. Presenta el output completo en Markdown.
2. Añade al final una sección **"Resumen para el consultor"** con:
   - Los [FALTA DATO] bloqueantes, listados uno a uno. Los no bloqueantes,
     sin recuento total.
   - Las [HIPÓTESIS] que requieren validación del cliente, listadas. Nunca
     declares totales: enumera lo que importa.
   - Tu evaluación de la calidad del intake (1-5) con una frase explicativa
   - Recomendación sobre si proceder al siguiente skill o recoger más información primero
3. El contenido validado se guarda como `[Cliente] - Brief Intake v1.md` en
   `01 Entregables`. El orquestador lo registra en el Registro.
   Siguiente skill: knowledge-base-builder.

## Lo que NO debes hacer

- No produzcas el fichero final maquetado (DOCX/XLSX/PPTX) — este skill
  produce contenido validado en Markdown; el fichero final lo genera
  `/revos:entrega` según la preferencia de output registrada en fase 0.
- No avances al siguiente skill sin confirmación explícita del consultor.
- No asumas información que no está en los materiales disponibles.
- No uses el mismo brief de otro cliente como referencia aunque sea del mismo
  sector. Cada brief parte de cero.
