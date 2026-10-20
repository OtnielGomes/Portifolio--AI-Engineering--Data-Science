from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAT = re.compile(r'(?:src="|!\[[^\]]*\]\()([^)"\s]+)')


def main() -> None:
    files = list(ROOT.glob("README*.md")) + list((ROOT / "projects").glob("*.md"))
    missing: list[tuple[str, str]] = []
    for file in files:
        text = file.read_text(encoding="utf-8")
        base = file.parent
        for match in PAT.finditer(text):
            path = match.group(1)
            if not re.search(r"\.(png|jpe?g|gif|webp)$", path, re.I):
                continue
            if not (base / path).resolve().exists():
                missing.append((str(file.relative_to(ROOT)), path))
    if missing:
        for rel, path in missing:
            print(f"MISSING {rel}: {path}")
        raise SystemExit(1)
    print("All image paths OK")


if __name__ == "__main__":
    main()
