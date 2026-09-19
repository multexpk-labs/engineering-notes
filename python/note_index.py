#!/usr/bin/env python3
"""List engineering notes by Markdown heading."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
for path in sorted(root.rglob("*.md")):
    if path.name == "README.md" and path.parent == root:
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    heading = next((m.group(1).strip() for m in re.finditer(r"^#\s+(.+)$", text, re.M)), path.stem)
    print(f"{path.relative_to(root)}\t{heading}")
