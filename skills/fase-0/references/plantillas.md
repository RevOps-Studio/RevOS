# Plantillas de fase 0 (v4.1)

## Registro — `[Cliente] - Registro v1.md`
Inmutable y acumulativo: crece por adición, nunca se reescribe. Lo mantiene el orquestador.

```markdown
# [Cliente] — Registro
Creado: [fecha] · Solo adición. Las vistas de trabajo viven en [Cliente] - Estado.

## Configuración
| Campo | Valor |
|---|---|
| Cliente | |
| Tier contratado | Essentials / Complete / Complete + opcionales: […] |
| Fecha de inicio | |
| Preferencia de output | HTML / Office |
| Idioma | Castellano |
| Conectores nivel 2 activos | Ninguno / CRM: […] / Transcripciones: […] / Ads: […] |
| Dominios de cuentas del cliente | [lista — se piden en intake] |

## Ejecución
| Skill | Entregable | Versión | Fecha | Ciclos de calidad (máx. 2) | Incorporaciones de información | Estado |
|---|---|---|---|---|---|---|

## Censo de asunciones
| # | Asunción | Criterio falsable | Origen | Historial de estado (fecha → vigente/validada/corregida/refutada) |
|---|---|---|---|---|

## Veredictos de system-qa
| Fase | Fecha | Veredicto (APTO / APTO CON RESERVAS / NO APTO) | Críticos | Mayores | Informe |
|---|---|---|---|---|---|

## Checkpoints celebrados
| Checkpoint | Fecha | Resultado | Ajustes acordados |
|---|---|---|---|
```

## Estado — `[Cliente] - Estado v1.md`
Vistas de trabajo. **Se regenera completo en cada cierre de skill** (lo regenera el orquestador); nunca se edita por adición.

```markdown
# [Cliente] — Estado
Regenerado: [fecha, tras cierre de skill X]. Este fichero se reescribe entero; el histórico vive en el Registro.

## Huecos vivos
| # | [FALTA DATO] | Bloqueante | Skill destinataria (no ejecutada) | Disposición del último cierre |
|---|---|---|---|---|

## Recolección pendiente
| # | Qué recoger | Fuente / conector | Skill que lo consumirá | Estado |
|---|---|---|---|---|

## Hallazgos vigentes (techo: 12 — al superarlo, consolidar antes de añadir)
| # | Hallazgo | Fuente | Afecta a |
|---|---|---|---|

## Agenda del próximo checkpoint
- Asunciones a validar: [del censo del Registro, las vigentes]
- Bloqueantes a resolver con el cliente: [de huecos vivos]
- Precondición: backlog sin cambios abiertos + system-qa de fase APTO → [estado actual]

## Siguiente paso
- Skill: 
- Inputs requeridos: 
- Huecos que arrastrará: 
```

## Backlog de cambios — `[Cliente] - Backlog de cambios v1.md`

```markdown
# [Cliente] — Backlog de cambios
Un cambio por fila. Tipos: Cosmético / Dato / Concepto. Origen: juicio (consume ciclo) / información nueva (no consume).

| Fecha | Entregable origen | Tipo | Origen | Descripción | Ficheros afectados (con estado) | Estado global |
|---|---|---|---|---|---|---|
```
