---
name: entrega
description: Producir el fichero final maquetado de un entregable RevOS a partir del contenido validado en Markdown. Aplica la preferencia de output del proyecto (HTML u Office) y el sistema visual de RevOps Studio. Usar cuando el consultor diga "genera el entregable", "maqueta el diagnóstico", "prepara el fichero para el cliente" o al cerrar la validación de cualquier skill del sistema.
---

# Entrega — maquetación del fichero final

Único punto del sistema donde el contenido validado se convierte en fichero para el cliente. Las skills producen Markdown; este flujo produce lo que el cliente recibe.

## Prerequisitos

1. El contenido está validado y guardado en `01 Entregables` como `[Cliente] - [Entregable] v[N].md`, registrado en el Registro.
2. El Registro indica la preferencia de output del proyecto (fase 0): **HTML** u **Office**. Override puntual permitido si el consultor lo pide para este entregable.
3. Si el entregable no está en el Registro, no se maqueta: primero la skill correspondiente, después la entrega.

## Proceso

### 1. Localizar contenido y especificación
Lee el Markdown validado. Muchos entregables incluyen una sección "Especificación de estructura para /revos:entrega" (hojas de XLSX, secciones de PPTX, requisitos del artefacto HTML): esa especificación manda sobre cualquier decisión de estructura.

### 2. Determinar el formato
- Preferencia **Office**: el formato lo dicta la naturaleza del entregable según su especificación — DOCX (documentos narrativos), XLSX (documentos vivos con datos: roadmap, measurement, media plan, calendario, CRM spec), PPTX (checkpoints y exec-deliverables). Usa las skills docx/xlsx/pptx del entorno.
- Preferencia **HTML**: un único fichero autocontenido por entregable, con el sistema visual de `references/sistema-visual.md` y la plantilla `references/plantilla.html`. Los entregables con componente de datos (roadmap, measurement) incluyen tablas filtrables; el revenue-diagnostic incluye el funnel visual con gaps que exige su especificación.

### 3. Validar la especificación (F9)
Antes de lanzar la maquetación, verifica la especificación del artefacto con este checklist:
- Estados/categorías declarados = estados/categorías usados en el contenido (ni uno más).
- Etiquetas y nombres de etapa = nombres exactos de las secciones que la especificación dice reutilizar.
- Todo elemento marcado o codificado por color tiene entrada en la leyenda.
Si algo falla, la especificación vuelve a su skill vía `/revos:cambio` — no se maqueta una especificación incoherente.

### 4. Maquetar
Antes de maquetar, retira del contenido de origen la sección **"Resumen para el consultor"**. No se edita el Markdown validado: se excluye del render. Es sección interna — contiene la autoevaluación de quien produjo el documento y los huecos en curso.

Lanza el agente deliverable-designer con: ruta del Markdown validado, formato objetivo, especificación de estructura, y el sistema visual. Reglas que el agente debe respetar:
- Fidelidad total al contenido validado: la maquetación no reescribe, no resume, no "mejora" textos.
- Las etiquetas vivas ([ASUNCIÓN], [HIPÓTESIS], [FALTA DATO] bloqueantes) se renderizan visibles con su estilo propio — nunca se ocultan en el fichero del cliente sin decisión explícita del consultor.
- Naming: `[Cliente] - [Entregable] v[N].[ext]`, misma versión que el Markdown de origen.

### 5. Verificar y registrar
Revisa el fichero producido contra la especificación (secciones/hojas completas, sin texto truncado). Guarda en `01 Entregables`, junto al Markdown de origen. El orquestador registra el fichero final en el Registro.

### 6. Cambios posteriores
Si el contenido cambia después de maquetar, el cambio entra por `/revos:cambio` sobre el Markdown; la re-maquetación se repite desde aquí. Nunca se edita el fichero final directamente.

## Lo que NO hacer
- No trasladar el *Resumen para el consultor* al fichero maquetado. El render al cliente empieza y termina en el contenido del entregable.
- No maquetar contenido sin validar o sin registrar.
- No alterar el contenido durante la maquetación.
- No mezclar formatos en un mismo proyecto sin decisión explícita (la preferencia de fase 0 es la norma).
