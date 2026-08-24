#!/usr/bin/env python3
"""
Validador de higiene RevOS — se ejecuta desde la raíz del repo antes de empaquetar.
Uso: python3 validar_revos.py [ruta_repo]   (por defecto: directorio actual)
Exit code 0 = limpio · 1 = hallazgos. Integrar en empaquetar.sh:
    python3 validar_revos.py || { echo "Validación fallida — no se empaqueta"; exit 1; }

AJUSTAR: las constantes RUTAS según la estructura real del repo.
"""
import re, sys, os
from pathlib import Path

# ---------------------------------------------------------------- configuración
REPO = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
SKILLS_DIR = REPO / "skills"                     # AJUSTAR si difiere
GRAFO = SKILLS_DIR / "revos-orchestrator" / "references" / "grafo-dependencias.md"
CONVENCIONES = SKILLS_DIR / "revos-orchestrator" / "references" / "convenciones.md"

# Enums canónicos (Bloque 4 del parche)
SEVERIDAD_CANON = {"CRÍTICO", "MAYOR", "MENOR"}
SEVERIDAD_PROHIBIDA = ["[RELEVANTE]", "[CRÍTICA]", "APTO PARA ENTREGAR",
                       "AJUSTES RELEVANTES REQUERIDOS", "BLOQUEADO POR CRÍTICAS"]

# Discrepancias grafo↔Requiere aceptadas por cobertura transitiva (Bloque 6b)
TRANSITIVAS_ACEPTADAS = {
    ("channel-strategy-design", "positioning-messaging"),
    ("channel-strategy-design", "competitive-research"),
    ("sales-process-design", "positioning-messaging"),
    ("sales-process-design", "revenue-diagnostic"),
    ("media-plan-builder", "positioning-messaging"),
    ("sales-conversion-design", "positioning-messaging"),
    ("positioning-messaging", "brief-intake"),
    ("conversion-playbook-builder", "positioning-messaging"),
    ("content-discoverability-design", "competitive-research"),
    ("crm-blueprint-builder", "crm-selection"),
}

# Mapa nombre-de-artefacto → skill productora (para resolver Requiere textuales)
ARTEFACTO_A_SKILL = {
    "client master brief": "brief-intake",
    "knowledge base": "knowledge-base-builder",
    "competitive landscape": "competitive-research",
    "revenue diagnostic": "revenue-diagnostic",
    "positioning & messaging architecture": "positioning-messaging",
    "positioning & messaging": "positioning-messaging",
    "positioning": "positioning-messaging",
    "growth system": "growth-system-design",
    "sales conversion": "sales-conversion-design",
    "channel strategy": "channel-strategy-design",
    "content & discoverability": "content-discoverability-design",
    "content discoverability": "content-discoverability-design",
    "sales process": "sales-process-design",
    "measurement framework": "measurement-framework",
    "execution roadmap": "execution-roadmap-builder",
    "martech stack audit": "martech-stack-audit",
    "crm selection report": "crm-selection",
    "crm selection": "crm-selection",
    "crm blueprint": "crm-blueprint-builder",
    "martech & measurement architecture": "martech-measurement",
    "martech measurement": "martech-measurement",
    "brand copy": "brand-copy-system",
}


# Registro canónico de artefactos (Bloque 5 aplicado) — fichero por skill productora
REGISTRO_ARTEFACTOS = {
    "brief-intake": "[Cliente] - Client Master Brief v",
    "knowledge-base-builder": "[Cliente] - Knowledge Base v",
    "competitive-research": "[Cliente] - Competitive Landscape v",
    "revenue-diagnostic": "[Cliente] - Revenue Diagnostic v",
    "positioning-messaging": "[Cliente] - Positioning & Messaging Architecture v",
    "growth-system-design": "[Cliente] - Growth System Design v",
    "sales-conversion-design": "[Cliente] - Sales Conversion Design v",
    "channel-strategy-design": "[Cliente] - Channel Strategy Design v",
    "content-discoverability-design": "[Cliente] - Content & Discoverability Design v",
    "sales-process-design": "[Cliente] - Sales Process Design v",
    "measurement-framework": "[Cliente] - Measurement Framework v",
    "execution-roadmap-builder": "[Cliente] - Execution Roadmap v",
    "martech-stack-audit": "[Cliente] - Martech Stack Audit v",
    "crm-selection": "[Cliente] - CRM Selection Report v",
    "crm-blueprint-builder": "[Cliente] - CRM Blueprint v",
    "martech-measurement": "[Cliente] - Martech & Measurement Architecture v",
    "media-plan-builder": "[Cliente] - Media Plan v",
    "content-calendar-builder": "[Cliente] - Content Calendar v",
    "brand-copy-system": "[Cliente] - Brand Copy System v",
    "conversion-playbook-builder": "[Cliente] - Conversion Playbook v",
    "reporting-operating-system": "[Cliente] - Reporting Operating System v",
}

errores, avisos = [], []

def err(m): errores.append(m)
def warn(m): avisos.append(m)

# ---------------------------------------------------------------- 1. frontmatter y nombres
skills = {}
if not SKILLS_DIR.is_dir():
    sys.exit(f"No existe {SKILLS_DIR} — ajusta SKILLS_DIR en el script")

for d in sorted(SKILLS_DIR.iterdir()):
    if not d.is_dir():
        continue
    sk = d / "SKILL.md"
    if not sk.exists():
        err(f"[F1] {d.name}: falta SKILL.md")
        continue
    txt = sk.read_text(encoding="utf-8")
    skills[d.name] = txt
    m = re.search(r"^---\s*\n(.*?)\n---", txt, re.S)
    if not m:
        err(f"[F1] {d.name}: frontmatter ausente o malformado")
    else:
        nm = re.search(r"^name:\s*(\S+)", m.group(1), re.M)
        if nm and nm.group(1) != d.name:
            err(f"[F1] {d.name}: frontmatter name='{nm.group(1)}' ≠ directorio")

# ---------------------------------------------------------------- 2. alias inexistentes
alias_validos = set(skills) | {"cambio", "status", "entrega", "fase-0", "setup", "system-qa"}
for name, txt in skills.items():
    for al in set(re.findall(r"/revos:([a-z0-9\-]+)", txt)):
        if al not in alias_validos:
            err(f"[F2] {name}: referencia a /revos:{al} — skill inexistente")

# ---------------------------------------------------------------- 3. grafo ↔ Requiere
grafo_deps = {}
if GRAFO.exists():
    for line in GRAFO.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 6 and cells[1] in skills:
            grafo_deps[cells[1]] = cells[5]
else:
    err(f"[F3] no encuentro el grafo en {GRAFO}")

SKILLS_TRANSVERSALES = {"system-qa", "diagnostic-checkpoint"}  # deps definidas por fase, no por lista
FORMULAS_COMODIN = ("todos los", "del tier")  # entradas de grafo en prosa que cubren conjuntos

for name, txt in skills.items():
    if name in SKILLS_TRANSVERSALES:
        continue
    req = re.search(r"^\*\*Requiere:\*\*\s*(.+)$", txt, re.M)
    if not req:
        continue
    req_low = req.group(1).lower()
    deps_grafo = grafo_deps.get(name, "").lower()
    if any(f in deps_grafo for f in FORMULAS_COMODIN):
        warn(f"[F3] {name}: grafo usa fórmula en prosa ('{deps_grafo[:60]}…') — no verificable mecánicamente; candidato a explicitar en v5")
        continue
    for artefacto, productor in ARTEFACTO_A_SKILL.items():
        if artefacto in req_low and "recomendado" not in req_low.split(artefacto)[0][-60:]:
            if productor not in deps_grafo and productor != name:
                if (name, productor) in TRANSITIVAS_ACEPTADAS:
                    warn(f"[F3] {name}: '{artefacto}' cubierto solo transitivamente en grafo")
                else:
                    err(f"[F3] {name}: Requiere '{artefacto}' ({productor}) pero el grafo no lo declara")

# ---------------------------------------------------------------- 4. enums fuera de canon
for name, txt in skills.items():
    for tok in SEVERIDAD_PROHIBIDA:
        if tok in txt:
            err(f"[F4] {name}: enum no canónico '{tok}'")

# ---------------------------------------------------------------- 5. versión coherente
versiones = set(re.findall(r"[Cc]onvenciones v(\d+\.\d+)", "\n".join(skills.values())))
if len(versiones) > 1:
    err(f"[F5] versiones de convenciones divergentes en skills: {sorted(versiones)}")


# ---------------------------------------------------------------- 6. guardado conforme al registro de artefactos
for name, txt_skill in skills.items():
    if name not in REGISTRO_ARTEFACTOS:
        continue
    if REGISTRO_ARTEFACTOS[name] not in txt_skill:
        err(f"[F6] {name}: el fichero de guardado no usa el nombre canónico '{REGISTRO_ARTEFACTOS[name]}N.md'")

# ---------------------------------------------------------------- salida
print(f"Skills analizadas: {len(skills)}")
for a in avisos:
    print(f"  AVISO  {a}")
for e in errores:
    print(f"  ERROR  {e}")
print(f"\nResultado: {len(errores)} errores, {len(avisos)} avisos")
sys.exit(1 if errores else 0)
