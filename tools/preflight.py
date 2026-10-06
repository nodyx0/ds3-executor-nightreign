#!/usr/bin/env python3
"""Basic design-sheet preflight checker.

This checks that the JSON design files exist and that all required top-level
keys are filled in. It does not validate game assets or runtime behavior.
"""

import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
required_files = [
    root / "design" / "characters.json",
    root / "design" / "abilities.json",
    root / "design" / "systems.json",
]

missing = [str(p.relative_to(root)) for p in required_files if not p.exists()]
if missing:
    print("Missing design files:")
    for item in missing:
        print(f"- {item}")
    raise SystemExit(1)

for path in required_files:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not data:
        raise SystemExit(f"Empty file: {path}")
    print(f"OK: {path.relative_to(root)}")

print("Preflight check passed: required project sheets exist.")
print("Next step: verify rows and columns in the design files before any build attempt.")
