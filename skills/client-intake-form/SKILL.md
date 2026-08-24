---
name: client-intake-form
description: Capturar la información inicial del cliente mediante formulario estructurado o entrevista guiada, antes de cualquier procesamiento. Primer skill de la fase Diagnostic de todo proyecto RevOS, inmediatamente después de fase 0. Activar si el consultor pide "captura el intake", "formulario de discovery", "entrevista inicial de [cliente]" o al arrancar Diagnostic sin información previa del cliente.
---

# Client Intake Form

Punto de entrada de información del sistema. Convierte la primera conversación con el cliente (o el formulario pre-discovery) en un registro estructurado y completo que brief-intake pueda procesar sin ambigüedad.

## Posición en el pipeline
- **Requiere:** fase 0 completada (Registro existente). Conversación con el cliente, formulario pre-discovery si existe, web del cliente y documentos aportados.
- **Produce:** material de captura — formulario de discovery completado en `02 Anexos`. No es un entregable de cliente: no lleva versión ni consume presupuesto de revisión.
- **Siguiente skill:** brief-intake.

## Principios de ejecución

**Registrar, no interpretar.** Este skill captura lo que el cliente declara, con sus palabras. La interpretación y estructuración es de brief-intake. Si el cliente dice "no nos llegan leads buenos", eso se registra literal — no se traduce todavía a "problema de cualificación".

**Distinguir declarado de verificado.** Todo lo que venga del cliente es declarado. Lo verificable (web, materiales) se contrasta y se anota la fuente.

Convenciones v4.3 — **Doctrina de avance**: un [FALTA DATO] es no bloqueante por defecto; solo bloquea si cumple un criterio de la definición cerrada (inversión de tesis · irreversibilidad ante el cliente · imposibilidad material), y la carga de la prueba es del bloqueo. En primera pasada, si la fuente del dato no estará disponible antes del checkpoint, escribe directamente [ASUNCIÓN: valor + criterio falsable] — un v1 con asunciones declaradas es un entregable válido. Máximo 3 preguntas abiertas al consultor por entregable, escaladas agrupadas al cierre del paso, nunca una a una en mitad de la producción. **Lenguaje calibrado**: la asertividad es del entregable, no de la conversación; las conclusiones mayores declaran su confianza (alta: dato medido/CRM · media: declarado por el cliente · baja: inferencia), las consecuencias se formulan condicionadas — nunca proféticas — y el contraste retórico ("No es X. Es Y.") solo es admisible con evidencia de ambos lados. **Precondición**: antes de producir, lee `00 Sistema/[Cliente] - Registro` y detente si falta fase 0, si hay una intervención sin tramitar por /revos:cambio con presupuesto agotado, o si el cierre de fase anterior exigía un system-qa aún no APTO. **Resumen para el consultor**: enumera lo relevante — nunca recuentos totales. Mecánica completa (dos contadores, propagación en lote, disposición de huecos, etiquetas): skills/revos-orchestrator/references/convenciones.md del plugin revos.

## Proceso

### 1. Revisar lo disponible
Lee el Registro y el material ya presente en `02 Anexos` (formulario pre-discovery, notas, decks). Lista qué campos del formulario ya tienen respuesta para no preguntar dos veces.

### 2. Web del cliente
Lee la web del cliente (web fetch). Extrae: oferta visible, segmentos aparentes, claims actuales, señales de posicionamiento. Anótalo como fuente "web" — servirá para contrastar lo declarado.

### 3. Extracción de CRM (condicional)
Si el Registro registra un CRM conectado, lanza el agente crm-analyst del plugin: volúmenes por etapa, tasas de conversión, ciclo medio, ticket medio, win rate. Cada dato con etiqueta [DATO CRM: fuente, fecha]. Dato inconsistente → [DATO NO FIABLE], tratar como [FALTA DATO].

### 4. Entrevista guiada / formulario
Completa los campos pendientes con el cliente (o prepara el guion para que el consultor lo haga). Campos obligatorios:

| Bloque | Campos |
|---|---|
| Negocio | Sector, oferta/servicios, modelo de ingresos, facturación aproximada, años en mercado, nº empleados |
| Equipo | Estructura comercial y de marketing, roles, seniority, dependencia del founder en la venta |
| Objetivos | Objetivo comercial declarado, horizonte, crecimiento esperado |
| Retos declarados | Problemas percibidos, en palabras del cliente |
| Funnel actual | Cómo llegan los leads hoy, canales activos, proceso de venta descrito |
| Dominios de cuentas | Los dominios web de clientes actuales representativos y de competidores directos (input de la medición de activos) |
| Stack | CRM, herramientas de marketing, analítica, reporting |
| Restricciones | Presupuesto estimado, recursos, líneas rojas |

### 5. Contraste inicial
Señala discrepancias evidentes entre lo declarado y lo observado (web, CRM) con [CONTRADICCIÓN DETECTADA: descripción]. No las resuelvas — se resuelven con el cliente en brief-intake o en el checkpoint.

### 6. Entrega
El formulario se guarda como `[Cliente] - Client Intake.md` en `02 Anexos` — es material de captura, no un entregable: sin sufijo de versión y sin presupuesto de revisión (ver "Recolección y material de captura" en convenciones). El orquestador añade su fila a la tabla de Ejecución del Registro con entregable `— (material en 02 Anexos)`, para que la trazabilidad no se pierda. Si el cliente aporta o corrige datos después, se actualiza el fichero directamente: no hay versión que archivar ni ciclo que consumir. Siguiente skill: brief-intake.

## Lo que NO hacer
- No interpretar ni diagnosticar — eso empieza en brief-intake.
- No rellenar campos con suposiciones: campo sin respuesta = [FALTA DATO] clasificado.
- No generar el fichero final maquetado: lo hace `/revos:entrega` según la preferencia de fase 0.
