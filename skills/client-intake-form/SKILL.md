---
name: client-intake-form
description: Capturar la información inicial del cliente mediante formulario estructurado o entrevista guiada, antes de cualquier procesamiento. Primer skill de la fase Diagnostic de todo proyecto RevOS, inmediatamente después de fase 0. Activar si el consultor pide "captura el intake", "formulario de discovery", "entrevista inicial de [cliente]" o al arrancar Diagnostic sin información previa del cliente.
---

# Client Intake Form

Punto de entrada de información del sistema. Convierte la primera conversación con el cliente (o el formulario pre-discovery) en un registro estructurado y completo que brief-intake pueda procesar sin ambigüedad.

## Posición en el pipeline
- **Requiere:** fase 0 completada (State Log existente). Conversación con el cliente, formulario pre-discovery si existe, web del cliente y documentos aportados.
- **Produce:** formulario de discovery completado.
- **Siguiente skill:** brief-intake.

## Principios de ejecución

**Registrar, no interpretar.** Este skill captura lo que el cliente declara, con sus palabras. La interpretación y estructuración es de brief-intake. Si el cliente dice "no nos llegan leads buenos", eso se registra literal — no se traduce todavía a "problema de cualificación".

**Distinguir declarado de verificado.** Todo lo que venga del cliente es declarado. Lo verificable (web, materiales) se contrasta y se anota la fuente.

Convenciones v4: cada [FALTA DATO] se clasifica al detectarse como bloqueante (impide una decisión de este entregable) o no bloqueante. Presupuesto máximo: 2 ciclos de revisión por entregable. Agotado el presupuesto, los [FALTA DATO] no bloqueantes se convierten en [ASUNCIÓN: valor asumido + criterio] y el sistema avanza; solo los bloqueantes detienen y se escalan al cliente de inmediato. Los datos extraídos de CRM conectado se marcan [DATO CRM: fuente, fecha]. Referencia completa: skills/revos-orchestrator/references/convenciones.md del plugin revos.

## Proceso

### 1. Revisar lo disponible
Lee el State Log y el material ya presente en `02 Anexos` (formulario pre-discovery, notas, decks). Lista qué campos del formulario ya tienen respuesta para no preguntar dos veces.

### 2. Web del cliente
Lee la web del cliente (web fetch). Extrae: oferta visible, segmentos aparentes, claims actuales, señales de posicionamiento. Anótalo como fuente "web" — servirá para contrastar lo declarado.

### 3. Extracción de CRM (condicional)
Si el State Log registra un CRM conectado, lanza el agente crm-analyst del plugin: volúmenes por etapa, tasas de conversión, ciclo medio, ticket medio, win rate. Cada dato con etiqueta [DATO CRM: fuente, fecha]. Dato inconsistente → [DATO NO FIABLE], tratar como [FALTA DATO].

### 4. Entrevista guiada / formulario
Completa los campos pendientes con el cliente (o prepara el guion para que el consultor lo haga). Campos obligatorios:

| Bloque | Campos |
|---|---|
| Negocio | Sector, oferta/servicios, modelo de ingresos, facturación aproximada, años en mercado, nº empleados |
| Equipo | Estructura comercial y de marketing, roles, seniority, dependencia del founder en la venta |
| Objetivos | Objetivo comercial declarado, horizonte, crecimiento esperado |
| Retos declarados | Problemas percibidos, en palabras del cliente |
| Funnel actual | Cómo llegan los leads hoy, canales activos, proceso de venta descrito |
| Stack | CRM, herramientas de marketing, analítica, reporting |
| Restricciones | Presupuesto estimado, recursos, líneas rojas |

### 5. Contraste inicial
Señala discrepancias evidentes entre lo declarado y lo observado (web, CRM) con [CONTRADICCIÓN DETECTADA: descripción]. No las resuelvas — se resuelven con el cliente en brief-intake o en el checkpoint.

### 6. Entrega
El contenido validado se guarda como `[Cliente] - Client Intake v1.md` en `01 Entregables`. El orquestador lo registra en el State Log. Siguiente skill: brief-intake.
Cierra con el resumen para el consultor: campos completados, [FALTA DATO] (bloqueantes y no bloqueantes), contradicciones detectadas.

## Lo que NO hacer
- No interpretar ni diagnosticar — eso empieza en brief-intake.
- No rellenar campos con suposiciones: campo sin respuesta = [FALTA DATO] clasificado.
- No generar el fichero final maquetado: lo hace `/revos:entrega` según la preferencia de fase 0.
