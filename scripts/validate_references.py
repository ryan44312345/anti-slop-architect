"""Check the reference catalog, historical IDs and source URL syntax."""
from collections import Counter
from pathlib import Path
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
ID = r"L\d+-[A-Z]+-\d{2}"
HEADING = re.compile(rf"^#### ({ID}) — (.+)$", re.M)
CATEGORIES = dict(zip(
    "HERO NARR FEAT SHOW PROOF CONV NAV SPEC".split(),
    "heroes narrative-about features-process showcase-media social-proof conversion-closing navigation-chrome special-modules".split(),
))
FIELDS = (
    "Requisitos de Mídia e Copy", "Ordem obrigatória do DOM",
    "Comportamento em largura estreita", "Comportamento em desktop",
    "Invariantes vs. Adaptáveis", "Animações & Interações observadas",
    "Regras Anti-Slop específicas daquela seção", "Direção de arte e aplicação",
)
TAGS = (
    "[Mídia: Tipográfico/Foto-Adaptável/Foto-Crítica]",
    "[Scroll: Estático/Sticky]",
    "[Fundo: Escuro/Claro/Adaptável]",
)


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def main():
    refs = ROOT / "references"
    cards = {}
    for prefix, stem in CATEGORIES.items():
        name = f"{stem}.md"
        text = (refs / name).read_text()
        headings = list(HEADING.finditer(text))
        for i, heading in enumerate(headings):
            key, title = heading.groups()
            stop = headings[i + 1].start() if i + 1 < len(headings) else len(text)
            body = text[heading.end():stop]
            require(key not in cards, f"ID duplicado: {key}")
            require(key.split("-")[1] == prefix, f"Categoria incorreta: {key}")
            require(f"`{key}`" in body and f"`{name}`" in body, f"Metadados: {key}")
            require(not re.search(r"\bundefined\b", body), f"Campo corrompido: {key}")
            fields = dict(re.findall(r"^##### (.+)\n([\s\S]*?)(?=^##### |\Z)", body, re.M))
            require(all(fields.get(field, "").strip() for field in FIELDS), f"Campo vazio: {key}")
            source = re.search(r"\*\*Fonte\*\* — \[([^\]]+)\]\(([^)]+)\)", body)
            require(source, f"Fonte ausente: {key}")
            url = urlsplit(source[2])
            require(url.scheme == "https" and url.hostname and "." in url.hostname, f"URL inválida: {key}")
            cards[key] = (name, title, source[1])

    original = Counter(key for file in (ROOT / "raw-audits").glob("lote-*.md")
                       for key, _ in HEADING.findall(file.read_text()))
    require(all(count == 1 for count in original.values()), "IDs repetidos no histórico")
    require(original.keys() <= cards.keys(), "IDs históricos ausentes")
    seen = set()
    for line in (refs / "INDEX.md").read_text().splitlines():
        if line.startswith("## "):
            category = line[3:]
        match = re.match(rf"^- \*\*({ID}) \| (.+?)\*\*", line)
        if not match:
            continue
        key, title = match.groups()
        require(key in cards and key not in seen, f"ID inesperado ou repetido no índice: {key}")
        name, expected_title, site = cards[key]
        require((category, title) == (name, expected_title) and f"(Fonte: {site})" in line,
                f"Índice diverge da ficha: {key}")
        for tag in TAGS:
            label, options = tag[1:-1].split(": ")
            values = re.findall(rf"\[{label}: ([^\]]+)\]", line)
            require(len(values) == 1 and values[0] in options.split("/"), f"Tag {label}: {key}")
        require("**Composição:**" in line and "**Seleção:**" in line, f"Curadoria ausente: {key}")
        seen.add(key)
    require(seen == cards.keys(), "Fichas ausentes no índice")
    totals = Counter(key.split("-")[0] for key in original)
    print(" | ".join(f"{lot}: {n}" for lot, n in sorted(totals.items())))
    print(f"Histórico: {len(original)} | Fichas: {len(cards)} | Índice: {len(seen)}")


if __name__ == "__main__":
    main()
