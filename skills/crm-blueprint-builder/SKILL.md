---
name: crm-blueprint-builder
description: >
  Usar cuando el consultor necesite producir la especificación completa del CRM del cliente: objetos,
  campos obligatorios, pipelines, etapas, automatizaciones, reglas de asignación, reportes estándar y
  permisos. Activar dentro del tier Activation Complete, después de martech-stack-audit. También activar
  si el consultor pide "configurar el CRM", "especificación del CRM", "blueprint del CRM" o "setup de HubSpot/Salesforce/Pipedrive".
---

# CRM Blueprint Builder

## Propósito

Este skill produce la especificación operativa completa del CRM del cliente, lista para ser implementada por un administrador o un partner. Cubre: arquitectura de objetos (contactos, cuentas, oportunidades, productos), campos obligatorios y opcionales, pipelines y etapas, automatizaciones, reglas de asignación, reportes estándar, permisos por rol.

Es el documento que convierte el sales-process-design en algo ejecutable dentro de HubSpot, Salesforce, Pipedrive o el CRM que se haya elegido. Es agnóstico de vendor en la arquitectura, pero se puede aterrizar a uno concreto si el cliente ya lo tiene decidido.

## Posición en el pipeline

**Requiere:** Sales Process Design, Martech Stack Audit, Measurement Framework. Recomendado: CRM Selection si todavía no hay decisión de vendor.

**Produce:** CRM Blueprint v1 en Markdown (contenido validado). El fichero final maquetado (DOCX formal + XLSX de campos y pipelines) lo genera `/revos:entrega` según la preferencia de output registrada en fase 0. Alimenta martech-measurement y reporting-operating-system.

**Siguiente skill:** martech-measurement.

## Principios de ejecución

**El CRM es la implementación del sales process, no al revés.** Si el sales process dice que hay 5 etapas con estos criterios, el CRM tiene 5 etapas con esos criterios exactos. No se inventa pipeline porque "el CRM viene con otro por defecto".

**Campos con propósito.** Cada campo existe porque desbloquea un reporte, una automatización o una cualificación. Campos "por si acaso" no existen — son ruido que el equipo dejará de rellenar. Lista corta y obligatoria mejor que lista larga y opcional.

**Obligatoriedad escalonada.** No todos los campos son obligatorios desde el minuto uno. Se define qué campo es obligatorio en qué etapa (ej. "presupuesto confirmado" se hace obligatorio al pasar a etapa 3, no antes).

**Automatización al servicio del proceso.** Se automatiza lo repetitivo sin juicio (asignación round-robin, creación de tareas estándar, envío de resúmenes). No se automatiza lo que requiere criterio humano (cualificar, descualificar, cambiar fecha de cierre).

**Reportes antes que campos.** Parte de "qué reporte necesitamos" y diseña los campos hacia atrás. Así nada sobra y nada falta.

**Permisos por rol, no por persona.** Roles estandarizados con permisos bien definidos. No configuraciones ad-hoc por persona — inmantenible.

**Limpieza desde el diseño.** Reglas de deduplicación, validación de datos, enriquecimiento automático. Un CRM sucio pierde valor cada trimestre.

Convenciones v4.1 — **Precondición**: antes de producir, lee `00 Sistema/[Cliente] - Registro` y detente si falta fase 0, si el presupuesto de revisión de este entregable está agotado sin cambio tramitado por /revos:cambio, o si el cierre de fase anterior exigía un system-qa aún no APTO. **Etiquetado**: cada [FALTA DATO] se clasifica al detectarse como bloqueante (impide una decisión de este entregable) o no bloqueante. **Presupuesto**: 2 ciclos de revisión de calidad por entregable — solo consumen ciclo los cambios nacidos del juicio sobre lo escrito; las incorporaciones de información nueva (aportada por cliente o consultor, o medida por el sistema) no consumen ciclo y generan versión y entrada en el Backlog si el entregable ya está registrado. Agotado el presupuesto, los [FALTA DATO] no bloqueantes se convierten en [ASUNCIÓN: valor asumido + criterio falsable] y el sistema avanza; solo los bloqueantes detienen y se escalan de inmediato. **Resumen para el consultor**: enumera los bloqueantes y lo relevante — nunca recuentos totales (el recuento es chequeo mecánico de system-qa sobre el documento terminado). **Cierre**: todo [FALTA DATO] heredado sale con disposición explícita — resuelto, reasignado a la primera skill no ejecutada que lo necesite, o declinado con motivo. Datos de CRM conectado: [DATO CRM: fuente, fecha]. Referencia completa: skills/revos-orchestrator/references/convenciones.md del plugin revos.

**Lenguaje.** Castellano. Registro ejecutivo directo. Vocabulario: objeto, campo, pipeline, etapa, automatización, workflow, regla de asignación, enriquecimiento, deduplicación, permisos, role-based access. Evitar: "CRM 360", "visión única del cliente" como frase hecha.

## Proceso

**Paso 1 — Lectura integrada.**
Revisa sales-process-design (etapas, criterios, cadencias, roles), measurement-framework (qué métricas hay que alimentar desde CRM), martech-stack-audit (vendor actual, brechas), positioning (ICP para definir segmentaciones).

**Paso 2 — Decisión de vendor si aplica.**
Si ya está decidido, se aterriza al vendor (HubSpot / Salesforce / Pipedrive / Zoho / otro). Si no, se trabaja agnóstico y se remite a `crm-selection`.

**Paso 3 — Arquitectura de objetos.**
Qué objetos se usan (Contacto, Cuenta, Oportunidad, Producto/LineItem, Ticket si aplica), relaciones entre ellos, lógica de duplicados.

**Paso 4 — Diseño de campos.**
Para cada objeto: campos mínimos necesarios. Distingue por campo: tipo (texto, número, lista, fecha, booleano), obligatoriedad y cuándo (siempre / en etapa X), fuente (manual, automático, enriquecimiento), quién lo puede editar.

**Paso 5 — Diseño de pipelines.**
Normalmente uno por línea de negocio. Etapas exactamente las de sales-process-design. Probabilidades por etapa. Campos obligatorios por etapa.

**Paso 6 — Automatizaciones.**
Lista operativa: disparador (trigger), condiciones, acciones, excepciones. Incluye asignación de leads (round-robin, territorio, ICP, etc.), creación de tareas, notificaciones, envío de emails transaccionales, cambios de etapa automáticos cuando proceda.

**Paso 7 — Reportes estándar.**
Qué reportes vive el equipo cada día/semana/mes. Derivados del measurement-framework. Diseño de cada uno: objeto base, filtros, agrupación, métricas.

**Paso 8 — Permisos por rol.**
Qué ve y qué edita cada rol: SDR, AE, AM, Manager, Dirección, Marketing, Finanzas, Admin.

**Paso 9 — Reglas de datos.**
Deduplicación, validación, enriquecimiento, limpieza periódica.

**Paso 10 — Plan de rollout.**
Fases de implementación: configuración básica → carga de datos → automatizaciones → reportes → capacitación → go-live.

**Paso 11 — Especificación de estructura para /revos:entrega.**
Documenta en el output la estructura de los entregables finales (DOCX formal + XLSX operativo con sus hojas), siguiendo la sección "Especificación de estructura para /revos:entrega" del template. Este skill no produce los ficheros finales: el DOCX y el XLSX maquetados los genera `/revos:entrega` según la preferencia de output registrada en fase 0.

**Paso 12 — Revisión de coherencia.**
¿Cada campo tiene propósito? ¿Cada etapa del pipeline refleja el sales process? ¿Los reportes alimentan el measurement framework? ¿Los permisos respetan la separación de roles?

## Template de output

Produce el output siguiendo exactamente esta estructura.

---

# CRM Blueprint — [NOMBRE EMPRESA]
*RevOS Activation Complete · Versión 1.0 · [Fecha]*

---

## 1. Sumario ejecutivo
*[Máximo 250 palabras. Vendor (si está definido), número de pipelines, número total de campos, número de automatizaciones, plan de rollout orientativo.]*

---

## 2. Contexto y alcance

### 2.1 Vendor seleccionado
[Nombre si está decidido, o "agnóstico pendiente de crm-selection"]

### 2.2 Fuentes de partida
[Sales Process, Measurement Framework, Martech Audit — qué se toma de cada uno]

### 2.3 Principios de diseño aplicados
[Síntesis de los principios — para que el admin los tenga presentes]

---

## 3. Arquitectura de objetos

### 3.1 Objetos utilizados
| Objeto | Uso | Objeto padre/relación |
|--------|-----|-----------------------|
| Contact | [Personas] | Account |
| Account | [Empresas] | — |
| Deal / Opportunity | [Oportunidades] | Account + Contact |
| Product / LineItem | [Productos en deal] | Deal |
| Ticket | [Soporte si aplica] | Account + Contact |

### 3.2 Relaciones y multiplicidades
[Uno a muchos, muchos a muchos, reglas de herencia]

---

## 4. Campos por objeto

### 4.1 Contact — campos
| Campo | Tipo | Obligatorio | Cuándo | Fuente | Editable por |
|-------|------|-------------|--------|--------|--------------|
| Nombre | Texto | Sí | Siempre | Manual | Todos |
| Email | Email | Sí | Siempre | Manual/Form | Todos |
| ... |

### 4.2 Account — campos
[Misma estructura]

### 4.3 Deal / Opportunity — campos
[Misma estructura, con los campos clave de cualificación: presupuesto, autoridad, timeline, etc.]

### 4.4 Product / LineItem — campos
[Misma estructura]

---

## 5. Pipelines

### 5.1 Pipeline 1 — [Nombre]
**Línea de negocio:** [Ej. nuevos clientes B2B]
**Etapas:** [Lista ordenada con probabilidad]
**Campos obligatorios por etapa:** [Tabla]
**Duración típica total:** [Días del sales-process]

### 5.2 Pipeline 2 — [Nombre]
[Misma estructura — ej. expansión, renovación]

---

## 6. Automatizaciones

### 6.1 Asignación de leads
**Trigger:** [Ej. nuevo contacto con formulario completado]
**Condiciones:** [ICP, país, sector, fuente]
**Acción:** [Asignar a propietario según regla — round robin, territorio, etc.]
**Excepciones:** [Cuándo no se automatiza]

### 6.2 Creación de tareas estándar
[Ídem]

### 6.3 Notificaciones
[Ídem — qué eventos notifican a qué personas]

### 6.4 Emails transaccionales
[Ídem — confirmaciones, recordatorios, etc.]

### 6.5 Cambios de etapa automáticos
[Ídem — solo cuando son incuestionables]

### 6.6 Lead scoring si aplica
[Modelo, variables, umbrales]

---

## 7. Reportes estándar

### 7.1 Reporte de pipeline
**Objetivo:** [Qué decisión desbloquea]
**Objeto base:** [Deal]
**Filtros:** [Abiertos, propietario, rango de fechas]
**Agrupación:** [Por etapa, por AE]
**Métricas:** [Cantidad, probabilidad ponderada, duración]

### 7.2 Reporte de velocidad de pipeline
[Ídem]

### 7.3 Reporte de actividad comercial
[Ídem]

### 7.4 Reporte de MQL → SQL → Cerrado
[Ídem]

### 7.5 Reporte de forecast
[Ídem]

### 7.6 Reporte de fuentes de lead
[Ídem]

*[Típicamente entre 6 y 10 reportes estándar.]*

---

## 8. Permisos por rol

| Rol | Ver todos los datos | Editar datos propios | Editar datos de equipo | Admin |
|-----|---------------------|----------------------|------------------------|-------|
| SDR | Sí (equipo) | Sí | No | No |
| AE | Sí (equipo) | Sí | No | No |
| Manager | Sí (equipo) | Sí | Sí | No |
| Dirección | Sí (global) | No | No | No |
| Marketing | Sí (lectura) | No | No | No |
| RevOps Admin | Sí (global) | Sí | Sí | Sí |

---

## 9. Calidad del dato

### 9.1 Deduplicación
[Reglas — email, dominio, nombre+empresa]

### 9.2 Validaciones al crear/editar
[Formato email, teléfono, país, dominio corporativo obligatorio]

### 9.3 Enriquecimiento automático
[Fuentes — Clearbit, Apollo, ZoomInfo si aplica]

### 9.4 Limpieza periódica
[Cadencia, criterios, responsable]

---

## 10. Plan de rollout

### 10.1 Fase 1 — configuración base (semanas 1-2)
[Objetos, campos, pipelines]

### 10.2 Fase 2 — datos (semanas 2-3)
[Carga, deduplicación, enriquecimiento]

### 10.3 Fase 3 — automatizaciones (semanas 3-4)
[Asignación, tareas, notificaciones]

### 10.4 Fase 4 — reportes (semana 4)
[Dashboards estándar]

### 10.5 Fase 5 — capacitación y go-live (semanas 4-5)
[Formación por rol, ventana de paralelo, corte definitivo]

---

## 11. Especificación de estructura para /revos:entrega

Los ficheros finales maquetados los genera `/revos:entrega` según la preferencia de output registrada en fase 0, con esta estructura:

**DOCX formal:** `[Cliente] - CRM Blueprint v1.docx` — para presentar a dirección o al partner implementador.

**XLSX operativo:** `[Cliente] - CRM Blueprint v1.xlsx` con hojas:
1. Campos por objeto
2. Pipelines y etapas
3. Automatizaciones
4. Reportes estándar
5. Permisos por rol

---

## 12. Vacíos e hipótesis

**Información que falta:** [[FALTA DATO]]
**Hipótesis críticas:** [[HIPÓTESIS]]
**Decisiones abiertas del cliente:** [Vendor si no está decidido, partners, ventanas de implementación]

---

## Entrega

Cuando el blueprint esté completo:

1. Presenta el output completo en Markdown.
2. Añade al final una sección **"Resumen para el consultor"** con:
   - Vendor (o agnóstico)
   - Los pipelines, listados por nombre — sin recuento
   - Los campos obligatorios, listados por objeto — sin recuento total
   - Las automatizaciones, listadas — sin recuento
   - Plan de rollout en semanas
   - Nivel de confianza en el blueprint (1-5)
3. El contenido validado se guarda como `[Cliente] - CRM Blueprint v1.md` en `01 Entregables`. El orquestador lo registra en el Registro. El DOCX y el XLSX finales los genera `/revos:entrega` según la preferencia de output registrada en fase 0. Siguiente skill: `martech-measurement`.

## Lo que NO debes hacer

- No incluyas campos sin propósito (sin reporte ni automatización que los use).
- No diseñes un pipeline distinto al del sales-process-design — es la misma fuente de verdad.
- No automatices nada que requiera criterio humano (cualificar, descalificar, cambiar fechas).
- No uses configuraciones ad-hoc por persona — permisos por rol siempre.
- No ignores la carga inicial de datos — suele ser lo que más frena el go-live.
- No generes tú los ficheros DOCX/XLSX finales — el skill produce contenido validado en Markdown; la maquetación corresponde a `/revos:entrega`.
- No avances a martech-measurement sin confirmación del consultor.
