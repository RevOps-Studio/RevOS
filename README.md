# revos — plugin interno de RevOps Studio

Sistema RevOS: diagnóstico, diseño y activación de sistemas de revenue para empresas B2B, operado íntegramente en Claude/Cowork.

## Estado: v4.3.0 · sistema completo, un piloto ejecutado

Arquitectura **skills-only**: 27 nodos de producción y 7 de control, sin capa de comandos. La secuenciación por tier vive en el grafo del orquestador; el punto de entrada de cada sesión es `status`.

- **Control** — `setup` (onboarding y corrección de rumbo) · `fase-0` (arranque: carpetas, configuración, Registro, Estado, Backlog) · `status` (estado y next best action) · `cambio` (puerta única de correcciones) · `entrega` (fichero final maquetado) · `system-qa` (coherencia transversal) · `revos-orchestrator` (reglas del sistema).
- **Diagnostic** — client-intake-form · brief-intake · knowledge-base-builder · competitive-research · revenue-diagnostic · diagnostic-checkpoint.
- **Design** — positioning-messaging · growth-system-design · sales-conversion-design · channel-strategy-design · content-discoverability-design · sales-process-design · measurement-framework · execution-roadmap-builder · brand-copy-system (opcional).
- **Activation** — martech-stack-audit · crm-selection (opcional) · crm-blueprint-builder · martech-measurement · media-plan-builder · content-calendar-builder · conversion-playbook-builder · reporting-operating-system (opcionales) · exec-deliverables.
- **Agentes** — competitive-researcher · crm-analyst · system-qa (solo lectura) · deliverable-designer.
- **Conectores** — nivel 1 en `.mcp.json` (Ahrefs, Similarweb, Drive, Notion, Dropbox); nivel 2 activable por proyecto (CRM, transcripciones, ads, SEO alternativo) según `skills/revos-orchestrator/references/conectores.md`.

Piloto ejecutado: fase Diagnostic completa con cliente real (07/2026). Sus aprendizajes están en `docs/` y produjeron las versiones 4.1 y 4.2. La 4.3 es un parche de usabilidad tras dos iteraciones reales: doctrina de avance (bloqueante con definición cerrada, asunción de primera pasada), lenguaje calibrado y propagación en lote para cambios de Dato. Histórico en `CHANGELOG.md`.

## Uso

1. `setup` tras instalar el plugin — onboarding guiado y corrección de rumbo.
2. `fase-0` al arrancar cada proyecto de cliente. Innegociable: sin Registro no hay orquestador.
3. `status` al inicio de cada sesión. Te dice qué toca, con qué inputs y qué huecos arrastra.
4. `cambio` para cualquier corrección sobre entregables ya producidos. Nada se edita a mano.
5. `system-qa` al cierre de cada fase, antes de preparar el checkpoint.
6. `entrega` para producir el fichero que recibe el cliente.

## Fuentes únicas

| Materia | Fichero |
|---|---|
| Dependencias entre nodos | `skills/revos-orchestrator/references/grafo-dependencias.md` |
| Convenciones transversales | `skills/revos-orchestrator/references/convenciones.md` |
| Mapa de conectores | `skills/revos-orchestrator/references/conectores.md` |
| Sistema visual | `skills/entrega/references/sistema-visual.md` |

El Blueprint, el Workflow y el Timeline son vistas derivadas: se regeneran desde estas fuentes, nunca al revés. Todo cambio del plugin se registra en `CHANGELOG.md`.

## Documentación interna

`docs/` no se empaqueta en el `.plugin` (ver `scripts/empaquetar.sh`). Contiene el Master Doc, la especificación de diseño histórica y los aprendizajes del piloto.
