#!/usr/bin/env python3
"""Create a release package scaffold for the DS3 Executor mod.

This script does not build a real game mod. It prepares a clean archive structure
so the actual DS3 runtime files can be placed into `mod/` and packaged in a
ready-to-upload release.
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
MOD_DIR = ROOT / "mod"
FILES_TO_INCLUDE = [
    ROOT / "README.md",
    ROOT / "melty.json",
]


def ensure_required_files() -> None:
    missing = [str(p.relative_to(ROOT)) for p in FILES_TO_INCLUDE if not p.exists()]
    if missing:
        raise FileNotFoundError(f"Missing required project files: {', '.join(missing)}")
    if not MOD_DIR.exists():
        raise FileNotFoundError(f"Missing mod directory: {MOD_DIR}")


def make_release_archive(version: str = "0.1.0-template") -> Path:
    ensure_required_files()
    DIST.mkdir(exist_ok=True)
    archive_path = DIST / f"executor-in-ds3-{version}.zip"
    if archive_path.exists():
        archive_path.unlink()

    # The actual mod payload is intentionally left as-is; this script packages the project
    # scaffolding so the build can be replaced later with the actual verified DS3 files.
    dest = ROOT / "_release_stub"
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir()

    # Copy project files into a staging folder
    for item in FILES_TO_INCLUDE:
        target = dest / item.name
        shutil.copy2(item, target)

    shutil.copytree(MOD_DIR, dest / "mod", dirs_exist_ok=True)

    shutil.make_archive(str(DIST / f"executor-in-ds3-{version}"), "zip", str(dest))
    shutil.rmtree(dest)
    return archive_path


if __name__ == "__main__":
    try:
        version = sys.argv[1] if len(sys.argv) > 1 else "0.1.0-template"
        archive = make_release_archive(version)
        print(f"Created release scaffold: {archive}")
        print("This is a placeholder package only. Add the real DS3 ModEngine2 files before publishing.")
    except Exception as exc:  # pragma: no cover
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
