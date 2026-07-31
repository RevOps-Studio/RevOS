# Ejemplos de clasificación de cambios

| Caso real típico | Tipo | Por qué |
|---|---|---|
| Corregir el nombre de un competidor mal escrito en el Competitive Landscape | Cosmético | Nada depende de la grafía |
| El cliente corrige el ticket medio de 8.000€ a 15.000€ | Dato… o Concepto | Si los cuellos de botella del diagnóstico y el roadmap se sostienen con el nuevo valor → Dato (editar valor, backlog con descendientes "pendiente de editar"). Si el nuevo ticket cambia la economía de canales o la priorización → Concepto (v-bump del diagnóstico y cascada) |
| El cliente descarta el segmento secundario tras el diagnostic-checkpoint | Concepto | El argumento de positioning, growth y roadmap cambia. v2 del Knowledge Base Pack y evaluación de toda la descendencia |
| Cambiar la fecha del checkpoint en el resumen ejecutivo | Cosmético | — |
| El CRM real tiene 4 etapas, no las 6 asumidas en [ASUNCIÓN] | Dato o Concepto según afecte al Commercial Conversion Blueprint | Entra por cambio al validarse la asunción; no consume ciclo de revisión |
| system-qa detecta que el ICP del brief y el del positioning no coinciden | Concepto en el documento equivocado | Resolver la [CONTRADICCIÓN DETECTADA] con el cliente primero; después v-bump del documento incorrecto |

# Ejemplo de plan de propagación (formato de presentación al consultor)

Cambio: ticket medio 8.000€ → 15.000€ en `Kokolski - Client Master Brief v1.md` · Tipo: Dato

| Fichero descendiente | ¿Usó el valor como input de decisión? | Acción propuesta |
|---|---|---|
| Kokolski - Knowledge Base Pack v1 | Sí (economics del ICP) | Pendiente de editar |
| Kokolski - Revenue Diagnostic v1 | Sí (dimensionado del problema de conversión) | Pendiente de editar |
| Kokolski - Competitive Landscape v1 | No | Sin impacto |
| Kokolski - Positioning & Messaging v1 | No (el argumento no usa el ticket) | Sin impacto |

¿Apruebas este plan? Tras tu OK edito los dos ficheros, actualizo backlog y Registro.
