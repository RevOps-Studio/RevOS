# Sistema visual RevOS — tokens y componentes

Fuente de verdad del diseño de entregables. Un solo lugar: cambiar aquí propaga a todos los entregables futuros.

## Tokens

| Token | Valor | Uso |
|---|---|---|
| --fondo | #F6F4F0 | Fondo general (crema de marca, theme-color de rev-ops.studio) |
| --tinta | #1C1B1A | Texto principal |
| --tinta-suave | #6B6862 | Texto secundario, notas |
| --acento | #C129A1 | Acento de marca — CTA, hitos, elementos activos. (confirmado por Carlos, 30/07/2026) |
| --ok | #3E7C4F | Estados positivos, checkpoints validados |
| --alerta | #B3822D | [ASUNCIÓN], [HIPÓTESIS], avisos |
| --critico | #A03A2E | [FALTA DATO] bloqueante, cuellos de botella críticos |
| --linea | #DDD8CF | Bordes, separadores |
| --panel | #FFFFFF | Tarjetas y paneles sobre el fondo crema |

Tipografía: serif editorial para títulos (Georgia/'Times New Roman' como fallback web-safe), sans para cuerpo y datos (system-ui). Jerarquía: h1 32px · h2 24px con kicker superior tipo "— Sección" · cuerpo 16px/1.6.

## Componentes (HTML)

- **Portada de entregable**: cliente, nombre del entregable, versión, fecha, fase y tier. Franja de acento.
- **Kicker + título de sección**: replica el patrón editorial de la web ("— El problema" / título).
- **Etiquetas vivas**: pills con color — [ASUNCIÓN] alerta · [HIPÓTESIS] alerta con borde · [FALTA DATO] crítico · [DATO CRM] tinta-suave con icono de base de datos · [DATO MEDIDO] tinta-suave con icono de gráfico. Los dos últimos son procedencia, no aviso: se renderizan discretos. Su función es que el cliente vea de un vistazo qué afirmación es verificable por terceros — que es el argumento comercial del diagnóstico.
- **Funnel con gaps** (revenue-diagnostic): barras horizontales por etapa, ancho proporcional al volumen, gap resaltado en crítico con la tasa de conversión perdida.
- **Matriz impacto × esfuerzo** (roadmap): cuadrantes con las iniciativas como fichas.
- **Tabla viva**: cabecera fija, filas cebradas con --linea, orden por columna si el entregable lo pide.
- **Bloque checkpoint**: hallazgo → implicación → decisión propuesta, con casilla de validación visual.

## Equivalencias Office

| Elemento HTML | DOCX | XLSX | PPTX |
|---|---|---|---|
| Tokens de color | Estilos de título/párrafo con la paleta | Cabeceras con --acento, formatos condicionales alerta/crítico | Master con fondo crema y acentos |
| Etiquetas vivas | Texto resaltado con color de la etiqueta | Celda con relleno del color | Pill en esquina del slide |
| Funnel/matriz | Imagen o tabla equivalente | Hoja dedicada con datos + gráfico | Slide dedicado |

Regla general: el mismo contenido, la misma jerarquía y los mismos colores en los tres formatos. La preferencia de fase 0 decide el contenedor, no el diseño.
