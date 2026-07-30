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
- **Hablas con comandos, no con skills.** `/revos:fase-0` para arrancar, `/revos:status` en cada sesión, `/revos:cambio` para toda corrección, `/revos:entrega` para maquetar. Las skills trabajan por debajo.
- **El State Log es la memoria.** Si algo no está registrado, para el sistema no existe.
- **Nada se edita a mano.** Entregables producidos → siempre por `/revos:cambio`; versiones antiguas → siempre a `04 Archivo` (lo hace el flujo, no tú).

### 2. Chequeo del entorno
Verifica y reporta:
- Carpeta de trabajo conectada en Cowork (si no, pídela).
- Conectores CRM autorizados (HubSpot/Pipedrive) — opcionales; explica qué aportan (datos reales del funnel con [DATO CRM]) y qué exigen (solo lectura + cláusula de confidencialidad con el cliente).
- Skills de formato disponibles (docx/xlsx/pptx) para la vía Office de `/revos:entrega`.

### 3. El ciclo de vida de un proyecto (con el Timeline delante)
Resume: fase 0 → Diagnostic → checkpoint → Design → checkpoint → Activation → entrega ejecutiva. Recalca los tres momentos que más errores evitan:
- **Fase 0 es innegociable** — sin State Log no hay orquestador.
- **Checkpoints**: nunca se celebran con cambios pendientes en el backlog; siempre incluyen las asunciones vigentes.
- **2 ciclos de revisión por entregable** — después, [FALTA DATO] no bloqueante pasa a [ASUNCIÓN] y se avanza. La búsqueda del dato perfecto es el freno número uno del sistema anterior.

### 4. Ofrecer ensayo en seco
Propón un dry-run con cliente ficticio: fase 0 + client-intake-form + brief-intake con datos inventados, en una carpeta "Ensayo". 20 minutos, sin riesgo, y el consultor ve el sistema entero funcionando (State Log, naming, etiquetas). Al terminar, la carpeta de ensayo se borra — no es un proyecto.

### 5. Cierre
Deja al consultor con la chuleta:

| Momento | Comando |
|---|---|
| Nuevo proyecto | `/revos:fase-0` |
| Empezar cada sesión | `/revos:status` |
| Ejecutar fases | `/revos:diagnostic` · `/revos:design` · `/revos:activation` |
| Preparar validación con cliente | `/revos:checkpoint` |
| Cualquier corrección | `/revos:cambio` |
| Fichero final para cliente | `/revos:entrega` |
| Cierre de fase | `/revos:qa` |

## Modo 2 — Corrección de rumbo (proactivo)

Si detectas cualquiera de estos patrones durante un proyecto, interviene con suavidad, nombra el riesgo y redirige al comando correcto:

| Patrón detectado | Riesgo | Redirección |
|---|---|---|
| Invocar una skill de producción directamente sin fase 0 / State Log | Entregables huérfanos, sin trazabilidad | `/revos:fase-0` primero |
| Editar a mano un entregable registrado | Incoherencia descendente silenciosa — la causa nº1 de errores | `/revos:cambio` |
| Pedir "una revisión más" con los 2 ciclos consumidos | Parálisis por dato perfecto | Convertir a [ASUNCIÓN] o clasificar como bloqueante y escalar |
| Querer celebrar checkpoint con backlog pendiente | Validar sobre contenido inestable | Resolver el backlog primero |
| Guardar ficheros con guiones bajos o fuera de carpeta | Rompe convención y State Log | Naming `[Cliente] - X v[N]` en su carpeta |
| Maquetar contenido sin validar | El cliente recibe borradores | Validar → registrar → `/revos:entrega` |

## Lo que NO hacer
- No convertir el setup en un volcado de documentación: máximo un concepto por interacción.
- No ejecutar fase 0 real durante el onboarding sin confirmación (el ensayo en seco usa carpeta "Ensayo").
- No repetir el onboarding completo a quien ya usa el sistema — para eso está el Modo 2.
