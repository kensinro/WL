from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from aido_wl_ref.manifest import build_manifest


def main():
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT
    text = build_manifest(root)
    (root / "MANIFEST.sha256").write_text(text, encoding="utf-8", newline="\n")
    print(f"MANIFEST_WRITTEN: {root / 'MANIFEST.sha256'}")


if __name__ == "__main__":
    main()
