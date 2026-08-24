---
name: setup
description: Guía de arranque y uso correcto del plugin revos. Usar justo después de instalar el plugin, cuando el consultor pida "setup", "cómo se usa revos", "guíame", "configura el plugin", "¿por dónde empiezo?", o cuando detectes que está usando el sistema de forma incorrecta (invocando skills sueltas, editando entregables a mano, saltándose fase 0 o checkpoints).
---

# Setup — guía de uso del plugin revos

Doble función: onboarding tras la instalación y corrección de rumbo cuando el sistema se está usando mal. Tono: guía práctica, no manual — enseña haciendo.

## Modo 1 — Onboarding (primera vez o a petición)

Recorre estos pasos en conversación, sin volcar todo de golpe:

### 1. El modelo mental (30 segundos)
Explica la regla de oro del sistema en tres frases:
- **Hablas con las skills de control como si fueran comandos.** `/revos:fase-0` para arrancar, `/revos:status` en cada sesión, `/revos:cambio` para toda corrección, `/revos:entrega` para maquetar. No existe una capa de comandos separada: son skills con interfaz de invocación directa. Las skills de producción trabajan por debajo, orquestadas por `status`.
- **El Registro es la memoria.** Si algo no está registrado, para el sistema no existe.
- **Nada se edita a mano.** Entregables producidos → siempre por `/revos:cambio`; versiones antiguas → siempre a `04 Archivo` (lo hace el flujo, no tú).

### 2. Chequeo del entorno
Verifica y reporta:
- Carpeta de trabajo conectada en Cowork (si no, pídela).
- Conectores de nivel 1 autorizados (Ahrefs, Similarweb, Drive, Notion, Dropbox — vienen con el plugin) y comprensión del nivel 2: el CRM del cliente y demás se activan por proyecto según el mapa `skills/revos-orchestrator/references/conectores.md`. Si hay CRM: solo lectura + cláusula de confidencialidad.
- Skills de formato disponibles (docx/xlsx/pptx) para la vía Office de `/revos:entrega`.

### 3. El ciclo de vida de un proyecto (con el Timeline delante)
Resume: fase 0 → Diagnostic → checkpoint → Design → checkpoint → Activation → entrega ejecutiva. Recalca los tres momentos que más errores evitan:
- **Fase 0 es innegociable** — sin Registro no hay orquestador.
- **Checkpoints**: nunca se celebran con cambios pendientes en el backlog; siempre incluyen las asunciones vigentes.
- **Asunciones en primera pasada + 2 ciclos de revisión.** Si en primera pasada ya se sabe que la fuente del dato no estará disponible antes del checkpoint, se escribe directamente [ASUNCIÓN: valor + criterio falsable] — no se espera. Para el resto, tras 2 ciclos de revisión, un [FALTA DATO] no bloqueante pasa a [ASUNCIÓN] y se avanza. La búsqueda del dato perfecto es el freno número uno del sistema anterior.

### 4. Ofrecer ensayo en seco
Propón un dry-run con cliente ficticio: fase 0 + client-intake-form + brief-intake con datos inventados, en una carpeta "Ensayo". 20 minutos, sin riesgo, y el consultor ve el sistema entero funcionando (Registro, naming, etiquetas). Al terminar, la carpeta de ensayo se borra — no es un proyecto.

### 5. Cierre
Deja al consultor con la chuleta:

| Momento | Skill que invocas |
|---|---|
| Nuevo proyecto | `fase-0` |
| Empezar cada sesión | `status` — te dice qué toca y con qué inputs |
| Ejecutar la fase | La skill que `status` indique, una a una, confirmando entre pasos |
| Cierre de fase (obligatorio antes del checkpoint) | `system-qa` |
| Preparar validación con cliente | `diagnostic-checkpoint` — sirve para las tres fases, parametrizado |
| Cualquier corrección sobre algo ya producido | `cambio` |
| Fichero final para cliente | `entrega` |

No hay comandos de fase ni una capa de comandos como tal: el sistema es skills-only (las skills de control se invocan con interfaz de comando) y la secuencia la calcula `status` contra el grafo. Si echas de menos lanzar una fase entera de un tirón, es una decisión de producto pendiente, no una función que estés usando mal.

## Modo 2 — Corrección de rumbo (proactivo)

Si detectas cualquiera de estos patrones durante un proyecto, interviene con suavidad, nombra el riesgo y redirige al comando correcto:

| Patrón detectado | Riesgo | Redirección |
|---|---|---|
| Invocar una skill de producción directamente sin fase 0 / Registro | Entregables huérfanos, sin trazabilidad | `/revos:fase-0` primero |
| Editar a mano un entregable registrado | Incoherencia descendente silenciosa — la causa nº1 de errores | `/revos:cambio` |
| Pedir "una revisión más" con los 2 ciclos consumidos | Parálisis por dato perfecto | Convertir a [ASUNCIÓN] o clasificar como bloqueante y escalar |
| Querer celebrar checkpoint con backlog pendiente | Validar sobre contenido inestable | Resolver el backlog primero |
| Guardar ficheros con guiones bajos o fuera de carpeta | Rompe convención y Registro | Naming `[Cliente] - X v[N]` en su carpeta |
| Maquetar contenido sin validar | El cliente recibe borradores | Validar → registrar → `/revos:entrega` |

## Lo que NO hacer
- No convertir el setup en un volcado de documentación: máximo un concepto por interacción.
- No ejecutar fase 0 real durante el onboarding sin confirmación (el ensayo en seco usa carpeta "Ensayo").
- No repetir el onboarding completo a quien ya usa el sistema — para eso está el Modo 2.
