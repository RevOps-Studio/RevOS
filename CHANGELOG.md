# CHANGELOG — plugin revos

Histórico de cambios del plugin y de los documentos canónicos de RevOS. **Ninguna modificación del plugin se considera aplicada hasta que tiene entrada aquí.**

Convención de tipo, la misma que el sistema aplica a los entregables de cliente:
**Cosmético** (nada depende de ello) · **Dato** (algo depende del valor, no del argumento) · **Concepto** (el argumento cambia).

Fuentes únicas, para que no haya duda de dónde se edita qué:

| Materia | Fuente única | Vistas derivadas |
|---|---|---|
| Dependencias entre nodos | `skills/revos-orchestrator/references/grafo-dependencias.md` | Blueprint, hoja "Flujo dependencias" · Timeline · Workflow |
| Convenciones transversales | `skills/revos-orchestrator/references/convenciones.md` | Bloque esencial "Convenciones v4.x" + puntero en cada SKILL.md · Master Doc §6 |
| Mapa de conectores | `skills/revos-orchestrator/references/conectores.md` | Blueprint, hoja "Arquitectura plugin" · `.mcp.json` (solo nivel 1) |
| Sistema visual | `skills/entrega/references/sistema-visual.md` | Plantilla HTML · plantillas Office |
| Método de cada nodo | El `SKILL.md` correspondiente | Blueprint, hoja "Matriz RevOS" (columna Propósito) |
| Versión y estado del plugin | `.claude-plugin/plugin.json` | `README.md` (línea de Estado y nota de versiones) · entrada más reciente de este CHANGELOG |

**Descripción del manifiesto (v4.4).** `description` de `plugin.json` tiene un límite de **500 caracteres** en la instalación. Lleva la descripción del sistema más la nota de **la versión vigente únicamente**: las notas de versiones anteriores se retiran al publicar, porque su sitio es este CHANGELOG. El check F7 del validador lo hace cumplir y avisa cuando queda poco margen.

---

## [4.4.0] — 31/08/2026

Rescate del programa v5 hacia 4.3.1, adjudicado entrada a entrada contra el baseline congelado (ZIP SHA-256 `3c5594da…0ba1`) y no contra el expediente de v5. Dos lecturas ordenan la versión. La primera: de los cuatro `METHOD_CHANGE` que el programa presentaba como correcciones al método, **uno corrige el plugin y tres corrigen a v5** o afinan algo que ya estaba bien — la disciplina epistémica ([ASUNCIÓN] con criterio falsable, [DATO MEDIDO], confianza declarada por conclusión, la sección "lo que NO es el problema") ya era de la metodología; v5 no la añadió, la convirtió en schema. La segunda, aplicada al propio rescate: **el programa v5 fue en buena medida sobreingeniería de algo que no estaba roto**, y el mismo test hay que pasarlo a lo que vuelve. De las siete piezas del expediente inicial, entran las cuatro con daño observado; tres se descartan por añadir gobierno sin defecto que lo justifique, y una de las descartadas hacía redundantes 20 ediciones.

Decisión de rumbo: el rescate entra **dentro del contrato actual de QA**. La capa de juicio de calidad (MC-002, rúbrica de dimensiones puntuadas, separación QA estructural/sustantiva de ADR-009) queda aplazada, con criterio de reapertura declarado: cuando un entregable pase el QA de coherencia y falle ante el cliente por calidad, o cuando haga falta responder *qué conclusiones se caen si esta asunción resulta falsa* sin que alguien lea el documento entero.

### El método deja de recomendar alcance

- **Retirada de la recomendación de alcance en los tres sitios donde vivía**: `revenue-diagnostic` §7.3 *Alcance sugerido* y su punto en el Resumen para el consultor, y `diagnostic-checkpoint` §8.2 *Alcance recomendado*. Essentials/Complete se firma en pre-venta: el sistema recomendando lo ya contratado produce una recomendación que no puede no confirmarse, y el diagnóstico real entregado a cliente lo exhibe — *«Alcance recomendado: Complete»* con sección propia. **El sesgo no lo pone el modelo: lo pone la plantilla.** En `diagnostic-checkpoint` la sección se reconvierte en lo único que conservaba valor y no es recomendación de alcance: la **retirada** de activaciones opcionales que el diagnóstico deja sin objeto — ahorro para el cliente, no ampliación. Guardia mecánica: F9. *Concepto.*

### Autoría de los juicios

- **El *Resumen para el consultor* no se traslada al fichero maquetado** (`entrega`, paso 4 y "Lo que NO hacer"; `convenciones.md` §Resúmenes). Hallazgo no previsto por el mapeo inverso: `entrega` no mencionaba la sección en ningún punto de su proceso y `convenciones.md` asumía lo contrario — *«una cifra … que un cliente con criterio comprueba»*. Verificado: **las 21 notas numéricas del sistema viven todas dentro de ese bloque**, entre 4 y 6 líneas bajo su cabecera; ninguna está en el cuerpo de un entregable. Una sola exclusión en el render las saca del documento del cliente. Es la corrección de R-015 en su forma económica: la nota del productor deja de heredar autoridad ante el cliente porque deja de llegarle, no porque se reetiquete en veinte ficheros. *Concepto.*
- **Postura de revisión en `system-qa`**, trasladada al dominio que el baseline sí tiene: la unidad no es la dimensión puntuada de v5 —que 4.x no tiene, y cuya introducción sería MC-002 por la puerta de atrás— sino **el cruce de la matriz de verificación**. Por cada cruce se construye primero el argumento más fuerte de que los documentos se contradicen; sólo si no se sostiene, el cruce se declara limpio. Entra como principio, sin obligación de reporte por cruce: el experimento controlado que la avala medía juicio de calidad con rúbrica, no coherencia, y no hay caso registrado de `system-qa` dando por coherente algo que no lo era — el principio cuesta una inserción y no infla ningún informe; la obligación de reporte habría crecido al cuadrado con el número de documentos para prevenir un fallo no observado. *Concepto.*

### Doctrina de fuentes

- **Un resumen generado por modelo no es fuente admisible de evidencia** (`convenciones.md` §Recolección, regla 5; mención en `brief-intake` y `knowledge-base-builder`). Origen: un digest de reunión atribuyó al cliente un producto que era del consultor, y tres de sus cifras no cuadraban contra el cuestionario. Es el único agujero de la versión que es **de hoy**: los notetakers automáticos ya están dentro del flujo real y el baseline no nombraba esa clase de fuente en ningún sitio. Punto de inserción corregido respecto al mapeo: §Recolección ya nombraba las transcripciones como material de captura, así que la regla va a la fuente única y no a dos doctrinas locales que se desincronizarían. Sin etiqueta nueva: la regla se ejecuta entera con [ASUNCIÓN] + criterio falsable, y añadir un enum obligaría a enseñárselo al chequeo de etiquetas vivas para una función ya cubierta. *Concepto.*
- **El checkpoint declara de qué se alimentó la fase** (`diagnostic-checkpoint` §2): una línea por entrada — *producido en esta fase*, nombrando la herramienta que lo midió / *aportado por el cliente* / *dado por provisto sin producir*, con motivo. En 4.x no es corrección sino refuerzo: el `Requiere … (todos obligatorios)` de `revenue-diagnostic` ya estaba bien, y es **más estricto que lo que v5 relajó** al convertirlo en `consumes` satisfacible por provisión — el hard stop del engagement de v5 fue deuda del porte, no del plugin. Lo que faltaba era que quedara escrito ante el cliente, porque es el contraste que hace visible el valor de la fase. *Concepto.*

### Plantillas

- **Ningún template afirma un hecho del proyecto** (`system-qa` §2, inventario de outputs auditados). Cuatro filas terminadas en `| ✓ |` le decían al modelo que los outputs estaban presentes, cuando el paso 1 del propio método es enumerar los existentes y los que faltan: el template pre-rellenaba la respuesta a su propia pregunta. En 4.x el `SKILL.md` **es** el prompt. Sustituidas por una fila de ejemplo con marcador sin resolver. Barrido confirmado: era la única aparición de ✓/✔ en las 31 skills, así que la corrección es puntual y **no se acompaña de doctrina ni de check mecánico** — un defecto de instancia única no justifica ninguno de los dos. *Dato.*

### Instrumentación

- **`scripts/validar_revos.py` — checks F7 y F8.** **F8**: ninguna skill recomienda alcance — guarda un cambio de Concepto que sí puede reintroducirse por deriva de redacción. **F7**: el manifiesto dentro de límites — `description` no excede 500 caracteres, con aviso a partir de 440 y comprobación de que `version` existe y de que el JSON es parseable. Los dos verificados en negativo: reintroducir §7.3 dispara F8; una descripción de 608 caracteres dispara F7 como error y una de 460 como aviso de margen. *Concepto.*
- **La descripción del manifiesto pasa a llevar sólo la versión vigente.** La convención anterior acumulaba una nota por versión y la 4.4 la llevó a 602 caracteres, por encima del límite de 500 que impone la instalación — el fallo no es de esta versión, es del patrón: cada versión futura habría vuelto a romperlo. Retiradas las notas de 4.3 y 4.3.1, que ya viven en este CHANGELOG, y añadido el puntero explícito. Queda en 427 caracteres. F7 lo vigila. *Dato.*
- **Dos checks propuestos y descartados**, sin número asignado para no reservar hueco: el que vigilaría los ✓ afirmativos en plantillas —un defecto de instancia única en 31 skills— y el que vigilaría la autoría de la nota numérica, que queda sin objeto tras la exclusión del Resumen y además nació mal, porque su lista de exclusiones fallaba en el primer caso: `crm-selection` tiene la matriz de scoring 1-5 **y** su propia nota de autoevaluación.
- **El bloque esencial no sube de versión.** F5 no exige que la cadena suba: exige que sea **una sola** en todas las skills, y lo es (`Convenciones v4.3`). La cadena nombra la generación de doctrina, no la versión del plugin — el propio fichero ya contiene secciones marcadas (v4.2) y (v4.3.1) bajo esa cabecera. Subirla habría costado una edición atómica de 25 ficheros por cero cambio de comportamiento. Las reglas nuevas se marcan (v4.4) en su sección.
- **Estado del validador**: 0 errores, 22 avisos — idéntico al baseline, porque 4.4 no toca el grafo.

### Higiene detectada, no corregida

- La entrada 4.3.1 declara *«0 errores, 17 avisos»*. El baseline congelado mide **22** (19 transitivas + 3 fórmulas en prosa). La divergencia parece venir de que una misma dependencia transitiva emite un aviso por cada variante de nombre del artefacto (`positioning`, `positioning & messaging`, `positioning & messaging architecture`). No se corrige aquí: es deriva documental de 4.3.1 y no afecta al comportamiento. Candidata a 4.4.1, junto con la deduplicación de avisos por artefacto en el validador.

### Migración

Ningún cambio invalida entregables emitidos. Proyectos abiertos migran al reabrirse: el *Alcance sugerido* de un diagnóstico ya emitido entra por `/revos:cambio` como **Concepto**; los ficheros maquetados ya entregados con el Resumen para el consultor incluido no se corrigen retroactivamente — se anota en el Backlog. Ninguna nota de autoevaluación cambia de redacción, así que ningún entregable vigente queda desalineado con su skill.

---

## [4.3.1] — 24/08/2026

Parche de higiene derivado de la auditoría externa (Sol 5.6, 24/08/2026) sobre el ZIP v4.3.0, con verificación independiente hallazgo a hallazgo antes de aplicar. Ningún cambio de doctrina: solo coherencia e instrumentación.

### Coherencia

- **Grafo alineado con los `Requiere` reales de las skills** (`grafo-dependencias.md`, 6 nodos). measurement-framework (+channel-strategy, +content-discoverability, +sales-process), content-discoverability-design (channel-strategy sustituye a growth-system como arista directa), crm-selection (+martech-stack-audit, +growth-system condicional), reporting-operating-system (+martech-measurement, +sales-process, +execution-roadmap), conversion-playbook-builder (brand-copy-system pasa a recomendado — un opcional no contratado ya no bloquea otro opcional), exec-deliverables (+outputs de Activation del tier). Las dependencias cubiertas transitivamente (channel-strategy, sales-process, media-plan, sales-conversion, positioning) se documentan en el validador como lista blanca, no se añaden como aristas. *Concepto.*
- **Alias `/revos:qa` inexistente → `/revos:system-qa`** en `diagnostic-checkpoint` y `revos-orchestrator`. *Dato.*
- **Enums canónicos de QA declarados en `convenciones.md`**: severidad `[CRÍTICO] · [MAYOR] · [MENOR]`, veredicto `APTO · APTO CON RESERVAS · NO APTO`. Normalizados en `system-qa` (skill y agente); [RELEVANTE] y los veredictos de plantilla antiguos quedan retirados con tabla de correspondencia. *Concepto.*
- **`setup` desambiguado**: "hablas con las skills de control como si fueran comandos" (resuelve la contradicción con "skills-only") e incorpora la asunción en primera pasada de v4.3 a la regla de los 2 ciclos. *Dato.*
- **README**: taxonomía corregida — 31 skills ejecutables (24 producción + 7 control) que implementan 27 nodos del grafo. *Dato.*
- **CHANGELOG**: fila duplicada "Versión y estado del plugin" eliminada de la tabla de fuentes. *Cosmético.*

### Instrumentación

- **`scripts/validar_revos.py` nuevo**: valida frontmatter y nombres, alias inexistentes, grafo↔Requiere (con lista blanca de transitivas), enums fuera de canon y versiones divergentes. Estado actual: 0 errores, 17 avisos (transitivas documentadas + 3 fórmulas en prosa del grafo, candidatas a explicitar en v5). *Concepto.*
- **`empaquetar.sh`**: ejecuta el validador y aborta si falla; `mktemp -u` → `mktemp -d`; comprobación de integridad del ZIP. *Dato.*

### Decisiones cerradas (24/08/2026, mismo día — la entrada se amplía antes de distribuir)

- **Secuencia final de Activation resuelta — opción A.** Nuevo nodo virtual `activation-checkpoint` (26, RCAC005) tras `exec-deliverables`; system-qa renumerado a 27. Secuencia codificada: outputs Activation → system-qa → exec-deliverables → checkpoint ejecutivo final → correcciones vía /revos:cambio → /revos:entrega → cierre. `exec-deliverables` deja de declararse terminal; `diagnostic-checkpoint` materializa el checkpoint final. El grafo pasa a 28 nodos (26 reales + 2 virtuales). *Concepto.*
- **Registro canónico de artefactos — opción A (renombrado).** El nombre de producción es el canónico: fichero, Requiere y Registro se conforman a él. Tabla A01–A24 en `convenciones.md`. Renombrados 10 artefactos (los 8 de la auditoría + 2 no detectados por ella: Reporting Operating System y Sales Process Design) + Handover Document. Formas cortas en los Requiere normalizadas en 13 skills. Validador ampliado con check F6 (guardado conforme al registro). Migración: proyectos con nombres antiguos migran al reabrirse como cambio Cosmético; proyectos nuevos usan el canon desde fase 0. *Concepto.*
- **Vistas derivadas regeneradas desde las fuentes v4.3.1**: Master Doc v3 (reposicionado como vista derivada — las fuentes canónicas son los ficheros del plugin; incorpora doctrina v4.3, skills-only, Registro/Estado, enums, 28 nodos, y nota de re-estimación pendiente en pricing), Blueprint v6 (sin capa de comandos; matriz de 28 nodos con IDs; conectores a dos niveles), Workflow v5 (secuencia por /revos:status, naming canónico, reglas v4.3.1), Timeline v3 (28 nodos, activation-checkpoint, generado desde el grafo). Versiones anteriores en `docs/archivo/` con nota de no-uso. *Concepto.*
- **Nota histórica**: la entrada 4.2.0 menciona 34 skills; es correcto — entre 4.2 y 4.3 se retiraron 3 skills. No se corrige.

---

## [4.3.0] — 24/08/2026

Parche de usabilidad tras dos iteraciones reales de proyecto. Diagnóstico de origen: tres síntomas convergentes — "lucha" por avanzar en el arranque (frentes abiertos que se tratan como bloqueos), conclusiones categóricas y dramáticas, y backlog que crece más rápido de lo que se resuelve. Causa raíz común: diseño defensivo pensado para modelos con menos juicio, ejecutado por modelos que sobre-cumplen cada raíl. Responde parcialmente a la decisión abierta "¿modo ligero?" registrada en 4.2.0: reduce el peso del gobierno sin crear un perfil separado.

### Doctrina de avance

- **Definición cerrada de bloqueante.** La definición anterior ("impide una decisión de este entregable") era circular y dejaba la clasificación al criterio expansivo del modelo. Sustituida por tres criterios cerrados — inversión de tesis · irreversibilidad ante el cliente · imposibilidad material — con **no bloqueante por defecto** y carga de la prueba en el bloqueo. *Concepto.*
- **Asunción de primera pasada (generalización de F6).** La conversión [FALTA DATO] → [ASUNCIÓN] operaba solo al agotar el presupuesto de revisión — un mecanismo de fin de vida, no un default. En el arranque (primera pasada de brief, KB, diagnostic) los huecos se acumulaban abiertos: ahí nacía la "lucha". Ahora: si la fuente del dato no estará disponible antes del checkpoint, se asume directamente con criterio falsable. [FALTA DATO] queda reservado a lo que cliente o consultor sí pueden responder antes del checkpoint. Es el patrón de la calibración económica de brief-intake (F6), generalizado. *Concepto.*
- **Tope de preguntas y escalado agrupado.** Máximo 3 preguntas abiertas al consultor por entregable; los bloqueantes se escalan agrupados al cierre del paso, nunca uno a uno en mitad de la producción. Sustituye el "escalarlo de inmediato" del orquestador. *Concepto.*
- Precedente interno: F3 (v4.1) corrigió que "el sistema penalizaba exactamente la conducta que quiere fomentar" en los ciclos. Esta doctrina corrige el mismo patrón un nivel más arriba, y matiza el F10-lite que el propio registro de v4.1 señaló como "el cambio de comportamiento más consecuente de la v4" implementado contra la evaluación original ("coste alto, contrario a la agilidad buscada").

### Lenguaje calibrado

- Sección nueva en convenciones, **reconciliada** con la asertividad prescrita en revenue-diagnostic (que se mantiene, acotada): la asertividad es del entregable, no de la conversación. Tres límites: confianza declarada en conclusiones mayores (alta: medido/CRM · media: declarado · baja: inferencia), consecuencias condicionadas — nunca proféticas —, y contraste retórico ("No es X. Es Y.") solo con evidencia de ambos lados. *Concepto.*
- **revenue-diagnostic**: lenguaje acotado ("asertivo en sus tesis y calibrado en sus fundamentos"), campo de confianza en la tesis y en cada cuello de botella del template, y limpieza del propio patrón retórico en el texto de la skill — el estilo de las instrucciones contagia el estilo del output. *Dato.*
- **system-qa (skill y agente)**: chequeo mecánico nuevo — conclusiones sin confianza declarada, profecías y contraste retórico sin evidencia son hallazgos clasificables. *Dato.*

### Propagación en lote

- Los cambios de **Dato** se ejecutan en el origen y entran al backlog como "pendiente de evaluar"; su propagación se evalúa **en lote** en el siguiente cierre de skill o pre-checkpoint, lo que llegue antes. Los Dato en lote **no bloquean la next best action** — solo la bloquean los Concepto pendientes y los bloqueantes abiertos. La incoherencia transitoria origen/descendientes es un coste aceptado que cazan el lote y el chequeo de coherencia de datos de system-qa. La doble condición de checkpoint no cambia: backlog limpio (incluido el lote evaluado) y QA APTO. Corrige el multiplicador del atasco: cada dato nuevo bloqueaba la NBA hasta tramitarse individualmente — el sistema penalizaba aportar información. *Concepto.*
- Ficheros tocados en la misma pasada para evitar la edición parcial: convenciones, orquestador (reglas de bloqueo, cierre de skill con paso de lote, régimen), status (detección de bloqueos e informe), cambio (paso 4 bifurcado), plantilla de backlog (estados). *Concepto.*

### Bloque esencial + puntero (adelanto del Track 1 de v5)

- El bloque "Convenciones v4.1" replicado íntegro en 25 skills (con dos variantes tipográficas divergentes) se sustituye por un **bloque esencial** — la doctrina de comportamiento en un párrafo — más puntero a `convenciones.md` para la mecánica. La doctrina viaja siempre en contexto; la mecánica vive en un solo sitio. Corrige de paso la divergencia ya instalada: bloques etiquetados v4.1 conviviendo con convenciones centrales v4.2. *Concepto.*

### Fuera de alcance deliberado

- El aflojamiento estructural de templates y tests mecánicos (paradigma mapa/territorio, menos raíles de procedimiento y más criterios de aceptación) **no entra en este parche**: su radio de propagación alcanza a entrega y system-qa, y pertenece al plan de sprints v5.
- Los pendientes de punteros por tier e inserción de /revos:qa registrados en 4.2.0 para esta versión siguen bloqueados por la revisión de commands/ y agents/: pasan a 4.4.0.
- La decisión "¿modo ligero?" sigue abierta: esta versión reduce el peso del gobierno para todos los tiers; un perfil Essentials reducido explícito queda por decidir.

### Validación pendiente

- Prueba de territorio: próxima sesión real (Kokolski) con las tareas que hoy generan fricción. Criterios de éxito: arranque de skill sin interrogatorio previo (≤3 preguntas), entregables v1 con asunciones en lugar de huecos abiertos, backlog estable entre cierres, y ausencia de profecías y contrastes retóricos sin evidencia en los outputs.

---

## [4.2.0] — 12/08/2026

Auditoría de coherencia interna del plugin, cruzando las 34 skills con el grafo, las convenciones y el Blueprint. Ningún hallazgo venía de un proyecto de cliente: todos son de instrumentación.

### Estructural

- **Jerarquía de fuentes declarada.** `grafo-dependencias.md` y la hoja "Flujo dependencias" del Blueprint se declaraban mutuamente como fuente canónica. Circularidad resuelta: **el markdown es la fuente** (es lo que el orquestador lee en ejecución), el Blueprint es vista derivada y se regenera desde él. *Concepto.*
- **CHANGELOG.md creado.** Hasta hoy el plugin no registraba sus propios cambios — un sistema cuyo valor es la trazabilidad de los entregables no la tenía sobre sí mismo. *Concepto.*
- **`RevOS - Blueprint v4.xlsx` → `v5`**, regenerado con las correcciones de dependencias y el bloque de conectores actualizado a dos niveles. *Concepto.*
- **`RevOS v4 - Especificacion del plugin.md` marcado como documento histórico de diseño**, con la lista de los cinco puntos en que ha quedado superado por v4.1. No se corrige: se señaliza. *Cosmético.*

### Navegación (skills-only)

- **Decisión de arquitectura: no se construye `commands/`.** La Especificación planificó nueve comandos y el Blueprint los documenta, pero la carpeta nunca existió: `/revos:diagnostic`, `/revos:design` y `/revos:activation` no existen en ninguna forma, y `checkpoint` y `qa` viven bajo otro nombre. La consecuencia real es que la secuenciación por tier no tenía dónde vivir y se apoyaba en los punteros de cada skill. Se asume el modelo skills-only: la secuencia la calcula el orquestador y los punteros se parametrizan. `status` + grafo cubren lo que iban a cubrir los comandos de fase; construirlos queda como decisión abierta para cuando haya varios proyectos en paralelo. *Concepto.*
- **Punteros parametrizados por tier** en `sales-conversion-design` (Essentials → roadmap · Complete → channel-strategy) y corregido el de `measurement-framework`, que mandaba a Activation saltándose el roadmap y el checkpoint de Design: siguiendo punteros, un Complete cerraba Design sin roadmap ni validación. *Concepto.*
- **`system-qa` insertado en la cadena** de `revenue-diagnostic`, `execution-roadmap-builder`, `martech-measurement` y `reporting-operating-system`. Ningún puntero lo mencionaba, aunque las convenciones lo exigen antes de todo checkpoint desde v4.1. *Concepto.*
- **Opcionales de Activation reconectados**: `martech-measurement` apuntaba directo a `exec-deliverables` y dejaba `reporting-operating-system` fuera de la cadena. *Dato.*
- **`diagnostic-checkpoint`**: puntero de salida parametrizado por fase y tier, y la no-validación del cliente se enruta explícitamente por `cambio`. *Dato.*
- **`martech-stack-audit`**: puntero condicionado a si `crm-selection` está contratado. *Dato.*

### Agentes alineados a v4.2

Los cuatro agentes seguían en vocabulario v4.0, hablando del **State Log** que F7 partió en Registro + Estado hace una versión.

- **`system-qa`**: los chequeos mecánicos de F8 estaban en el `SKILL.md` y no en el agente — y el agente es quien ejecuta. Es la observación del piloto repitiéndose ("los hizo por iniciativa propia, no por instrucción"), aplicada al fichero equivocado. Añadidos como sección obligatoria: recuentos contra contenido real, resúmenes que declaran totales, punteros caducados, supervivencia de contenido archivado, techo de 12 hallazgos y desfase Registro/Estado. Añadida la forma exacta del veredicto que espera el Registro. *Concepto.*
- **`crm-analyst`**: Registro en lugar de State Log; sus hallazgos de higiene se declaran recolección temprana para `martech-stack-audit` cuando se ejecuta en Diagnostic. *Dato.*
- **`competitive-researcher`**: distinción entre fuente web (URL) y dato de conector ([DATO MEDIDO]); su informe se declara recolección. *Dato.*
- **`deliverable-designer`** y **sistema visual**: `[DATO MEDIDO]` era una etiqueta huérfana — existía en convenciones y en el paso 4 de `knowledge-base-builder` desde F5, pero no tenía pill ni la conocía el maquetador. Lo que F5 creó no había llegado a la capa que lo renderiza. *Dato.*
- **`[DATO CRM]`**: admitido el periodo como extensión canónica para agregados temporales, resolviendo la divergencia entre el agente (tres campos) y la convención (dos) sin tocar el bloque replicado en 27 skills. *Dato.*

### Documentación

- **`README.md` reescrito.** Se declaraba en `v4.0.0-alpha.7` con los bloques 6-7 pendientes, cuando los documentos canónicos existen y el piloto se ejecutó. Ahora declara la arquitectura skills-only, el inventario real y la tabla de fuentes únicas. *Dato.*
- **Chuleta de `setup` corregida.** Enseñaba nueve comandos de los que tres no existen y dos tienen otro nombre — en el fichero de onboarding. *Dato.*

### Dependencias del grafo

- **Nodo 19 `crm-blueprint-builder`**: añadidas `measurement-framework` y `martech-stack-audit`, retirada `sales-conversion-design` (llega transitivamente vía `sales-process-design`). El paso 1 de la skill lee los dos documentos que el grafo no declaraba, de modo que el orquestador podía desbloquear el blueprint antes de que existieran y el paso 7 habría diseñado reportes contra un measurement framework inexistente. *Concepto.*
- **Nodo 17 `martech-stack-audit`**: dependencia corregida de `brief-intake` a `Design Essentials del tier · measurement-framework`, con consumo declarado de la recolección temprana. El grafo describía cuándo puede empezar el trabajo; la skill, cuándo puede cerrarse el entregable. *Concepto.*
- **Nodo 15 `design-checkpoint`**: tier corregido de `Complete` a `Essentials / Complete`. Las reglas de secuencia ya decían que Essentials cierra Design con checkpoint. *Dato.*
- **`channel-strategy-design`**: retirada la recomendación de usar el Execution Roadmap como input — el roadmap (nodo 14) depende de este nodo (10). Dependencia circular. *Dato.*

### Concepto nuevo: recolección y captura

- **Apartado nuevo en convenciones**: distinción entre entregable, material de captura y recolección temprana, con su ubicación, versionado, registro y efecto sobre el presupuesto de ciclos.
- **`knowledge-base-builder`**: el paso 4 (medición de activos, F5) incorpora la recolección temprana del stack — inventario, costes, flujos de datos e higiene del CRM. La suciedad del CRM pasa a ser evidencia del diagnóstico en lugar de una nota para cuatro meses más tarde.
- **`martech-stack-audit`**: paso 1 comprueba y consume la recolección si existe, en lugar de volver a pedir al cliente datos ya recogidos.
- **`client-intake-form`**: su output pasa de `01 Entregables` con versión a `02 Anexos` sin versión, como material de captura. Deja de consumir presupuesto de revisión, que es lo que hacía hasta ahora sobre un formulario que solo registra lo que el cliente declara. La fila en la tabla de Ejecución del Registro se conserva para no perder trazabilidad.
- **Plantilla de Estado**: sección nueva "Recolección pendiente". Material en `02 Anexos` que nadie referencia es material que se pierde; se vigila desde el Estado, no desde la memoria del consultor.
*Todo el bloque: Concepto.*

### Resúmenes sin recuentos (extensión de F1)

F1 se aplicó en v4.1 al alcance que fijó el documento de aprendizajes: `brief-intake`, `knowledge-base-builder`, `competitive-research`, `revenue-diagnostic` y `exec-deliverables` — los cinco documentos largos que fallaron en el piloto. Las skills de Complete y opcionales nunca se revisaron porque el piloto solo recorrió Diagnostic, mientras la convención estaba escrita como regla transversal. Ocho skills pedían recuentos que la convención prohíbe y que el chequeo mecánico de `system-qa` marca como hallazgo.

Corregidas: `brand-copy-system`, `content-calendar-builder`, `content-discoverability-design`, `conversion-playbook-builder`, `martech-measurement`, `martech-stack-audit`, `media-plan-builder`, `reporting-operating-system`. *Dato.*

Criterio aplicado, ahora explícito: F1 prohíbe **declarar cuántos elementos contiene el propio documento**, porque el cuerpo sigue cambiando después de escribir el resumen. No prohíbe cifras de negocio calculadas (coste mensual del stack, inversión a 12 meses, carga en horas, TCO, scoring). Por eso `crm-selection` no se tocó.

### Pendiente para 4.3.0

- **Punteros "Siguiente skill" (#1)**: están escritos como si el tier fuera siempre Essentials. `sales-conversion-design` apunta al roadmap (correcto solo en Essentials) y `measurement-framework` apunta a Activation, saltándose el roadmap (14) y el design-checkpoint (15). Siguiendo punteros, un proyecto Complete cierra Design sin roadmap ni validación.
- **Inserción de `/revos:qa` (#2)**: ningún puntero del sistema menciona el QA, aunque las convenciones lo exigen antes de todo checkpoint.
- **Opcionales de Activation (#7)**: `martech-measurement` apunta directo a `exec-deliverables`, dejando `reporting-operating-system` fuera de la cadena.
- Los tres son el mismo mecanismo y se editan de una pieza. Bloqueados hasta revisar `commands/` y `agents/`: la secuenciación por tier vive en `/revos:design`, y arreglar las skills sin leer el comando puede ser cosmético o contraproducente.
- **Decisión abierta**: ¿modo ligero? Para un Essentials pequeño, la maquinaria de gobierno completa (Registro + Estado + Backlog + QA + doble condición) puede pesar más que el entregable. Merece un perfil reducido explícito antes de que se improvise saltándose pasos.

---

## [4.1.0] — 31/07/2026 · registrada retroactivamente

Incorporación de los aprendizajes del primer piloto de Diagnostic (Kokolski, 30-31/07/2026). Evidencia: `docs/RevOS v4 - Aprendizajes del piloto Diagnostic.md`. Cinco skills ejecutadas, un flujo de cambio tramitado, un `system-qa` de cierre con veredicto APTO CON RESERVAS.

- **F1 · Resúmenes sin recuentos.** Los recuentos declarados fallaron en 3 de 3 documentos largos. Aplicado a los cinco documentos del alcance del piloto. *Dato.*
- **F2 · Disposición de huecos al cierre.** Todo `[FALTA DATO]` heredado sale de cada cierre como resuelto, reasignado o declinado. La regla de asignación pasa a "primera skill **no ejecutada** que lo necesita", recalculada en cada cierre. *Concepto.*
- **F3 · Dos contadores de ciclos.** Separación entre revisión de calidad (máximo 2) e incorporación de información (ilimitada). En el piloto, el presupuesto se agotó sin una sola revisión de calidad: el sistema penalizaba exactamente la conducta que quiere fomentar. *Concepto.*
- **F4 · Doble condición de checkpoint.** Backlog limpio **Y** último `system-qa` de la fase en APTO. En el piloto el backlog estaba limpio y los bloqueantes estaban en el informe de QA. *Concepto.*
- **F5 · Medición de activos en `knowledge-base-builder`.** El mejor hallazgo de la fase salió fuera de proceso. Etiqueta nueva `[DATO MEDIDO: herramienta, fecha]`. Los dominios de las cuentas del cliente pasan a ser dato de intake. *Concepto.*
- **F6 · Calibración de la capa económica al inicio de `brief-intake`.** Ahorra un ciclo completo y evita producir un documento que hay que convertir acto seguido. *Concepto.*
- **F7 · Partición del State Log** en `Registro` (inmutable, solo adición) y `Estado` (vistas de trabajo, regeneración completa en cada cierre). Era el fichero menos fiable del sistema y el que monta la agenda del checkpoint. Techo de 12 hallazgos con consolidación obligatoria. *Concepto.*
- **F8 · Chequeos mecánicos obligatorios en `system-qa`**: recuentos contra contenido real, punteros caducados, supervivencia de contenido archivado, asunciones corregidas que siguen operando, coherencia interna del Estado. *Dato.*
- **F9 · Validación de la especificación de artefactos antes de `/revos:entrega`**: estados declarados = estados usados, etiquetas = nombres de las secciones referenciadas, todo elemento marcado con entrada en la leyenda. *Dato.*
- **F10-lite · Precondición de producción — decisión de producto no registrada en su momento.** El documento de aprendizajes dejó F10 en "coste alto, contrario a la agilidad buscada, a evaluar para v5". La v4.1 lo implementó como precondición obligatoria en todas las skills de producción: leer el Registro y detenerse si falta fase 0, si el presupuesto está agotado sin cambio tramitado, o si el QA de la fase anterior no está APTO. **El sistema pasó de registrar a bloquear**, que es el cambio de comportamiento más consecuente de la v4, y no quedó constancia de cuándo ni por qué se decidió. Se registra aquí retroactivamente. *Concepto.*
- Etiquetas nuevas: `[DATO MEDIDO]`. Criterio falsable obligatorio en toda `[ASUNCIÓN]`.

## [4.0.0] — 30/07/2026 · registrada retroactivamente

Reescritura única de las skills y migración de operativa de Projects de claude.ai al plugin en Cowork. Decisiones D1-D11 en `docs/RevOS v4 - Especificacion del plugin.md`.

- Arquitectura de plugin único con comandos por fase, orquestador, cuatro agentes y conectores MCP.
- `fase-0` obligatoria con estructura estándar de cinco carpetas.
- `/revos:cambio` como puerta única de correcciones, con clasificación Cosmético/Dato/Concepto, archivado en `04 Archivo` y evaluación de propagación aprobada por el consultor.
- Separación entre contenido validado en Markdown y fichero final vía `/revos:entrega`.
- Naming `[Cliente] - [Entregable] v[N].[ext]`, sin guiones bajos.
- Terminología: checkpoint (no Gate), cuellos de botella, empresas B2B sin calificativo, Essentials/Complete, Activation.
- Skills nuevas: `client-intake-form`, `revos-orchestrator`.
- Documentos canónicos resultantes: Master Doc v2, Blueprint v4, Workflow v4, Timeline v2.
