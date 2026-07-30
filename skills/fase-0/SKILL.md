---
name: fase-0
description: Arranque obligatorio de todo proyecto RevOS. Crea la estructura estándar de carpetas del proyecto, registra tier, preferencia de output y conectores, e inicializa el State Log y el Backlog de cambios. Usar antes de producir ningún entregable. Activar si el consultor dice "arranca el proyecto de [cliente]", "fase 0", "nuevo proyecto RevOS" o "prepara las carpetas".
---

# Fase 0 — Arranque de proyecto RevOS

Ningún proyecto RevOS produce entregables sin pasar por aquí. Si el consultor pide ejecutar cualquier skill del sistema y no existe State Log en la carpeta del proyecto, redirige a este skill primero.

## Proceso

### 1. Carpeta del proyecto
Confirma la carpeta de trabajo en Cowork. Si no hay carpeta conectada, solicítala. El nombre del cliente se toma de la carpeta o se pregunta.

### 2. Estructura estándar
Crea exactamente esta estructura (no añadas ni renombres carpetas):

```
[Cliente]/
  00 Sistema/       → State Log · Backlog de cambios · configuración del proyecto
  01 Entregables/   → contenido validado en Markdown y ficheros finales
  02 Anexos/        → material del cliente, research bruto, transcripciones
  03 QA/            → informes de system-qa
  04 Archivo/       → versiones antiguas (las mueve el flujo de cambios, nunca a mano)
```

### 3. Configuración del proyecto
Pregunta al consultor, en una sola interacción:
1. **Tier contratado**: Essentials · Complete · Complete + opcionales (cuáles).
2. **Preferencia de output**: HTML u Office (DOCX/XLSX/PPTX). Una elección por proyecto; override puntual permitido por entregable.
3. **Idioma de los entregables** (por defecto castellano).
4. **Conectores del proyecto** — consulta el mapa `skills/revos-orchestrator/references/conectores.md`. Los de nivel 1 (Ahrefs, Similarweb, Drive, Notion, Dropbox) vienen con el plugin. Pregunta cuáles del nivel 2 aplican: CRM del cliente (HubSpot, Pipedrive, Zoho, Attio u otro), transcripciones (Fireflies/Gong/Granola), datos de ads (Supermetrics). Registra los activos en el State Log. Si hay CRM: acceso de solo lectura y cláusula de confidencialidad en la propuesta.

### 4. Inicialización
Crea en `00 Sistema/`, usando las plantillas de `references/plantillas.md`:
- `[Cliente] - State Log v1.md`
- `[Cliente] - Backlog de cambios v1.md`

### 5. Validación de naming
Todo fichero del proyecto sigue `[Cliente] - [Entregable] v[N].[ext]`. Sin guiones bajos. Verifica los ficheros recién creados antes de terminar.

### 6. Cierre
Resume al consultor: estructura creada, configuración registrada, y next best action (normalmente `client-intake-form` vía la fase Diagnostic). No ejecutes el siguiente skill sin confirmación.

## Lo que NO hacer
- No crear carpetas adicionales "por si acaso".
- No producir ningún entregable en fase 0.
- No omitir la pregunta de preferencia de output — condiciona toda la entrega posterior.
