# Convenciones transversales RevOS v4

Aplican a todos los skills, comandos y agentes del plugin. Cualquier output que las incumpla es no conforme.

## Terminología

| Usar | Nunca usar |
|------|-----------|
| checkpoint, hito de validación | Gate, peaje |
| cuellos de botella, problemas, fricciones | "cuello/cuellos" a secas |
| empresas B2B (sin calificativo de tamaño ni sector) | pyme, PYME, industrial, mediana/pequeña/gran empresa como scope |
| Essentials / Complete | Core v1 / Core v2 |
| Activation | Deployment |
| XLSX | XSLX |

Lenguaje de negocio, no de agencia: prohibidos "estrategia 360", "activación de marca", "ecosistema digital". Castellano, registro ejecutivo directo.

## Naming de ficheros

`[Cliente] - [Entregable] v[N].[ext]` — espacios y guion medio. Sin guiones bajos en ningún fichero del proyecto.
Ejemplos: `Kokolski - Revenue Diagnostic v1.docx` · `Kokolski - State Log v1.md`

## Etiquetado

| Etiqueta | Uso | Ciclo de vida |
|----------|-----|---------------|
| [FALTA DATO: descripción] | Información insuficiente para decidir con criterio. Clasificar siempre como bloqueante o no bloqueante. | Transitorio — máximo 2 ciclos de revisión |
| [ASUNCIÓN: valor + criterio] | Sustituye a un [FALTA DATO] no bloqueante agotado el presupuesto de revisiones. | Estable — se valida o corrige en checkpoint |
| [HIPÓTESIS] | Inferencia estratégica no respaldada por datos explícitos. | Validar con cliente |
| [CONTRADICCIÓN DETECTADA: descripción] | Conflicto entre fuentes o secciones. | Resolver antes de continuar |
| [DATO CRM: fuente, fecha] | Dato extraído de un CRM conectado. | Permanente (procedencia) |
| [DATO NO FIABLE] | Dato de CRM inconsistente. Tratar como [FALTA DATO]. | Transitorio |

## Régimen de revisiones

Máximo 2 ciclos de revisión por entregable. Al agotarse: [FALTA DATO] no bloqueante → [ASUNCIÓN], y el sistema avanza. Solo los bloqueantes detienen; se escalan al cliente de inmediato. Los checkpoints incluyen sección fija "Asunciones vigentes".

## Esquema de versionado

| Tipo | Definición | Acción | Versión | Backlog |
|------|-----------|--------|---------|---------|
| Cosmético | Nada depende de ello | Editar | Sin cambio | Opcional |
| Dato | Algo depende del valor, no del argumento | Editar | Sin cambio | Obligatorio, con lista de ficheros afectados y estado |
| Concepto | El argumento cambia | Reescribir | v1 → v2 | Obligatorio |

Reglas duras: un cambio de Concepto archiva la versión anterior en `04 Archivo` antes de reescribir · ningún checkpoint con cambios "pendientes" · la propagación la evalúa el orquestador y la aprueba el consultor.

## Formato de contenido

Los skills producen contenido validado en Markdown dentro de `01 Entregables`. El fichero final (HTML u Office, según la preferencia registrada en fase 0) lo genera `/revos:entrega` (bloque 5 — pendiente de construcción).
