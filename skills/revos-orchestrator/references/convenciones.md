## Convenciones transversales RevOS v4.2

Aplican a todos los skills, comandos y agentes del plugin. Cualquier output que las incumpla es no conforme.

Cambios v4.1 respecto a v4: precondición obligatoria, dos contadores de ciclos, resúmenes sin recuentos, disposición de huecos al cierre, doble condición de checkpoint y partición del State Log en Registro + Estado. Evidencia: "RevOS v4 - Aprendizajes del piloto Diagnostic" (docs/).

Cambios v4.2 respecto a v4.1: extensión de la regla de resúmenes sin recuentos a Complete y opcionales, corrección de dependencias del grafo, y concepto nuevo de recolección y captura (ver el apartado correspondiente). Histórico completo en CHANGELOG.md de la raíz del plugin.

## Precondición de producción (F10-lite)

Antes de producir, toda skill lee `00 Sistema/[Cliente] - Registro` y se detiene si: (a) no existe (falta fase 0), (b) el presupuesto de revisión del entregable está agotado y hay una intervención sin tramitar por `/revos:cambio`, o (c) el cierre de la fase anterior exigía un system-qa que no está en veredicto APTO (o con sus críticos/mayores de bloqueo tramitados). La detención se comunica al consultor con la vía de desbloqueo.

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

## Etiquetado

| Etiqueta | Uso | Ciclo de vida |
|----------|-----|---------------|
| [FALTA DATO: descripción] | Información insuficiente para decidir con criterio. Clasificar siempre: bloqueante o no bloqueante. | Transitorio. Al cierre de cada skill, todo hueco heredado sale con disposición: **resuelto** / **reasignado** (a la primera skill NO ejecutada que lo necesite) / **declinado** (con motivo) |
| [ASUNCIÓN: valor + criterio falsable] | Sustituye a un [FALTA DATO] no bloqueante al agotar revisiones, o se escribe directamente si la calibración de brief-intake lo indica. El criterio falsable es irrenunciable: una asunción refutada rápido es el sistema operando. | Estable — se valida o corrige en checkpoint |
| [HIPÓTESIS] | Inferencia estratégica no respaldada por datos explícitos. | Validar con cliente |
| [CONTRADICCIÓN DETECTADA: descripción] | Conflicto entre fuentes o secciones. | Resolver antes de continuar |
| [DATO CRM: fuente, fecha] | Dato extraído de un CRM conectado. Cuando el dato es un agregado de una ventana temporal (conversión, ciclo medio, win rate), la forma canónica añade el periodo: [DATO CRM: fuente, periodo, fecha]. Un agregado sin ventana declarada no es interpretable. | Permanente (procedencia) |
| [DATO MEDIDO: herramienta, fecha] | Dato medido por conectores de research (Ahrefs, Similarweb…). Toda divergencia con lo declarado por el cliente es material de observaciones. | Permanente (procedencia) |
| [DATO NO FIABLE] | Dato de fuente conectada inconsistente. Tratar como [FALTA DATO]. | Transitorio |

## Recolección y material de captura (v4.2)

No todo lo que entra al sistema es un entregable. Se distinguen tres cosas:

| Naturaleza | Dónde vive | Versión | Registro | Ciclos |
|---|---|---|---|---|
| **Entregable** — contenido con argumento propio que el cliente recibe | `01 Entregables` | Sí, `v[N]` | Fila en Ejecución con versión y contadores | Consume presupuesto |
| **Material de captura** — lo que el cliente declara, en sus palabras, antes de interpretarse (formulario de intake, notas de discovery, transcripciones) | `02 Anexos` | No | Fila en Ejecución con entregable `— (material en 02 Anexos)`, sin versión ni contadores | No consume |
| **Recolección temprana** — datos medibles por terceros o inventariables que se recogen cuando es posible, no cuando toca evaluarlos | `02 Anexos` | No | Igual que captura | No consume |

Reglas:

1. La recolección temprana **no anticipa la skill que la consume**. Recoger el inventario del stack en Diagnostic no adelanta el `martech-stack-audit`: adelanta su materia prima. La evaluación sigue exigiendo el sistema diseñado.
2. Toda recolección lleva su etiqueta de procedencia y fecha ([DATO MEDIDO], [DATO CRM]) — un inventario sin fecha caduca en silencio.
3. La skill que consume recolección **comprueba si existe antes de pedirla de nuevo**. Pedir dos veces el mismo dato al cliente es el defecto que este concepto existe para evitar.
4. El Estado lista la recolección pendiente como categoría propia. Material en `02 Anexos` que nadie referencia es material que se pierde: es el riesgo que asume este concepto y por eso se vigila desde el Estado, no desde la memoria del consultor.

## Régimen de revisiones — dos contadores (F3)

- **Ciclos de revisión de calidad: máximo 2 por entregable.** Consumen ciclo solo los cambios nacidos del juicio del operador o consultor sobre lo escrito: reescribir, reordenar, afinar, corregir criterio. Agotados, los [FALTA DATO] no bloqueantes pasan a [ASUNCIÓN] y el sistema avanza.
- **Incorporaciones de información: ilimitadas.** Datos nuevos aportados por el cliente o el consultor, o medidos por el sistema. No consumen presupuesto. Si el entregable ya está registrado, generan versión y entrada en el Backlog.
- El origen lo clasifica `/revos:cambio` en su paso 1: si un cambio mezcla dato nuevo y juicio, domina el juicio (consume ciclo).
- Los checkpoints incluyen sección fija "Asunciones vigentes".

## Resúmenes sin recuentos (F1)

Los "Resumen para el consultor" **enumeran, no cuentan**: los [FALTA DATO] bloqueantes listados, las hipótesis que requieren validación listadas, las contradicciones listadas. Prohibido declarar totales ("hay 9 hipótesis") — es una cifra que el documento no permite mantener y que un cliente con criterio comprueba. El recuento es un chequeo mecánico de system-qa sobre el documento terminado.

## Esquema de versionado

| Tipo | Definición | Acción | Versión | Backlog |
|------|-----------|--------|---------|---------|
| Cosmético | Nada depende de ello | Editar | Sin cambio | Opcional |
| Dato | Algo depende del valor, no del argumento | Editar | Sin cambio | Obligatorio, con lista de ficheros afectados y estado |
| Concepto | El argumento cambia | Reescribir | v1 → v2 | Obligatorio |

Reglas duras: un cambio de Concepto archiva la versión anterior en `04 Archivo` antes de reescribir · la propagación la evalúa el orquestador y la aprueba el consultor · **doble condición de checkpoint (F4): backlog sin cambios abiertos Y último system-qa de la fase en veredicto APTO** (o críticos/mayores de bloqueo tramitados). Sin QA ejecutado no hay checkpoint.

## Registro y Estado (F7)

`00 Sistema` contiene dos ficheros, no uno:

- **`[Cliente] - Registro v[N].md`** — inmutable y acumulativo: configuración del proyecto, tabla de ejecución (skill, entregable, versión, ciclos consumidos por contador, fecha), censo de asunciones con historial de estado, veredictos de system-qa. **Crece por adición, nunca se reescribe.**
- **`[Cliente] - Estado v[N].md`** — vistas de trabajo: huecos vivos con disposición y skill destinataria (no ejecutada), hallazgos vigentes (techo: 12, con consolidación obligatoria al superarlo), agenda del próximo checkpoint, siguiente paso. **Se regenera completo en cada cierre de skill, nunca se edita por adición.** Lo regenera el orquestador.

## Formato de contenido

Los skills producen contenido validado en Markdown dentro de `01 Entregables`. El fichero final (HTML u Office, según la preferencia registrada en fase 0) lo genera `/revos:entrega`, previa validación de la especificación del artefacto (F9): estados declarados = estados usados, etiquetas = nombres de las secciones referenciadas, todo elemento marcado tiene entrada en la leyenda.
