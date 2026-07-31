# Mapa de conectores RevOS v4

Dos niveles. **Nivel 1** — declarados en el `.mcp.json` del plugin (disponibles siempre): investigación y acceso a archivos. **Nivel 2** — activables por proyecto desde el registro de conectores cuando fase-0 lo detecte; se registran en el Registro.

## Nivel 1 — en el plugin

| Conector | Skills que lo usan | Qué aporta |
|---|---|---|
| Ahrefs | competitive-research · content-discoverability-design · martech-measurement | SEO, keywords, backlinks, Brand Radar (GEO/AI search) |
| Similarweb | competitive-research · channel-strategy-design | Tráfico y mix de canales de competidores |
| Google Drive | knowledge-base-builder · brief-intake | Materiales del cliente compartidos por Drive |
| Notion | knowledge-base-builder | Documentación interna del cliente |
| Dropbox | knowledge-base-builder · brief-intake | Materiales del cliente compartidos por Dropbox |

## Nivel 2 — activables por proyecto

| Categoría | Opciones en el registro | Skills que los usan | Cuándo activar |
|---|---|---|---|
| CRM | HubSpot · Pipedrive · Zoho CRM · Attio | client-intake-form · brief-intake · revenue-diagnostic · martech-stack-audit (vía agente crm-analyst) | El cliente usa ese CRM y firma la cláusula de acceso de lectura. No hay MCP oficial de Salesforce: usar Supermetrics como vía de datos |
| Transcripciones | Fireflies · Gong · Granola | knowledge-base-builder (entrevistas internas) | Hay entrevistas grabadas del discovery |
| Datos de ads | Supermetrics (Google/Meta/LinkedIn Ads y 200+ fuentes) | media-plan-builder · measurement-framework · martech-stack-audit | Proyecto Complete con histórico de paid |
| SEO alternativo | Semrush | content-discoverability-design | El cliente ya trabaja con Semrush |

## Reglas

1. fase-0 pregunta qué conectores del nivel 2 aplican al proyecto y los registra en el Registro. La activación la hace el consultor desde el registro de conectores de Cowork.
2. El agente crm-analyst es agnóstico del CRM: opera contra el CRM que el Registro declare conectado, sea cual sea.
3. Todo dato externo lleva su etiqueta de procedencia: [DATO CRM: fuente, fecha] para CRM; citación de fuente para research.
4. No añadir conectores al `.mcp.json` del plugin sin criterio de uso intrínseco y transversal — cada conector declarado pide autorización en cada sesión.
