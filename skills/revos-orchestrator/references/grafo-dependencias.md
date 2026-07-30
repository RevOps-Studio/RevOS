# Grafo de dependencias RevOS v4

Fuente canónica: Blueprint v4 (hoja "Flujo dependencias"). Orden = secuencia cronológica de referencia; las dependencias son la verdad, no el orden.

| # | Nodo | Fase | Tier | Modelo | Depende de |
|---|------|------|------|--------|------------|
| 0 | fase-0 | Fase 0 | Todos | Sonnet | — (punto de entrada del proyecto) |
| 1 | client-intake-form | Diagnostic | Essentials | Sonnet | fase-0 |
| 2 | brief-intake | Diagnostic | Essentials | Sonnet | client-intake-form |
| 3 | knowledge-base-builder | Diagnostic | Essentials | Opus | brief-intake |
| 4 | competitive-research | Diagnostic | Essentials | Sonnet | brief-intake · knowledge-base-builder |
| 5 | revenue-diagnostic | Diagnostic | Essentials | Opus | brief-intake · knowledge-base-builder · competitive-research |
| 6 | diagnostic-checkpoint | Diagnostic | Essentials | Sonnet | revenue-diagnostic [CHECKPOINT CLIENTE] |
| 7 | positioning-messaging | Design | Essentials | Opus | revenue-diagnostic · competitive-research · knowledge-base-builder |
| 8 | growth-system-design | Design | Essentials | Opus | positioning-messaging · revenue-diagnostic |
| 9 | sales-conversion-design | Design | Essentials | Sonnet | revenue-diagnostic · growth-system-design |
| 10 | channel-strategy-design | Design | Complete | Sonnet | growth-system-design |
| 11 | content-discoverability-design | Design | Complete | Sonnet | positioning-messaging · growth-system-design |
| 12 | sales-process-design | Design | Complete | Sonnet | sales-conversion-design |
| 13 | measurement-framework | Design | Complete | Sonnet | revenue-diagnostic · sales-conversion-design · growth-system-design |
| 14 | execution-roadmap-builder | Design | Essentials/Complete | Opus | todos los blueprints Design del tier contratado |
| 15 | design-checkpoint | Design | Complete | Sonnet | execution-roadmap-builder [CHECKPOINT CLIENTE] |
| 16 | brand-copy-system | Design | Opcional | Sonnet | positioning-messaging |
| 17 | martech-stack-audit | Activation | Complete | Sonnet | brief-intake |
| 18 | crm-selection | Activation | Opcional | Sonnet | sales-process-design |
| 19 | crm-blueprint-builder | Activation | Complete | Sonnet | crm-selection (si aplica) · sales-process-design · sales-conversion-design |
| 20 | martech-measurement | Activation | Complete | Sonnet | martech-stack-audit · measurement-framework · crm-blueprint-builder |
| 21 | media-plan-builder | Activation | Opcional | Sonnet | channel-strategy-design |
| 22 | content-calendar-builder | Activation | Opcional | Sonnet | content-discoverability-design |
| 23 | conversion-playbook-builder | Activation | Opcional | Sonnet | sales-process-design · brand-copy-system |
| 24 | reporting-operating-system | Activation | Opcional | Sonnet | measurement-framework |
| 25 | exec-deliverables | Activation | Complete | Opus | execution-roadmap-builder · design-checkpoint · system-qa |
| 26 | system-qa | Transversal | Todos | Opus | se ejecuta al cierre de cada fase y bajo demanda tras propagaciones |

## Reglas de secuencia

- Los nodos de checkpoint (diagnostic-checkpoint, design-checkpoint, final checkpoint) los materializa una única skill: diagnostic-checkpoint, parametrizada por fase. No existe skill separada design-checkpoint.

- Complete contiene Essentials. Los opcionales requieren Complete.
- En Essentials, la fase Design termina en execution-roadmap-builder + checkpoint; no existen los nodos Complete.
- system-qa es obligatorio al cierre de cada fase (Diagnostic, Design, Activation) y antes de exec-deliverables.
- Ningún checkpoint se celebra con cambios "pendientes" en el backlog.

## Descendencia (para propagación)

Para calcular los descendientes de un nodo, sigue las dependencias en sentido inverso de forma transitiva. Los casos que más propagación generan:
- brief-intake → prácticamente todo el sistema.
- revenue-diagnostic → todo Design y Activation.
- positioning-messaging → growth, content, brand-copy y todos sus descendientes.
- measurement-framework → martech-measurement · reporting-operating-system.
