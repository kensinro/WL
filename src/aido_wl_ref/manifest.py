from __future__ import annotations

import hashlib
from pathlib import Path


DEFAULT_EXCLUDES = {
    "MANIFEST.sha256",
}

EXCLUDED_PARTS = {
    ".git",
    ".pytest_cache",
    "__pycache__",
    "build",
    "dist",
}


def _eligible(path: Path, root: Path) -> bool:
    rel = path.relative_to(root).as_posix()
    if rel in DEFAULT_EXCLUDES:
        return False
    if any(part in EXCLUDED_PARTS for part in path.relative_to(root).parts):
        return False
    if rel.endswith(".egg-info") or ".egg-info/" in rel:
        return False
    if rel.endswith(".pyc"):
        return False
    return path.is_file()


def iter_files(root: str | Path):
    root = Path(root)
    for path in sorted(root.rglob("*")):
        if _eligible(path, root):
            yield path


def sha256(path: str | Path) -> str:
    h = hashlib.sha256()
    with Path(path).open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def build_manifest(root: str | Path) -> str:
    root = Path(root)
    lines = []
    for path in iter_files(root):
        rel = path.relative_to(root).as_posix()
        lines.append(f"{sha256(path)}  {rel}")
    return "\n".join(lines) + "\n"


def verify_manifest(root: str | Path) -> tuple[bool, list[str]]:
    root = Path(root)
    manifest = root / "MANIFEST.sha256"
    if not manifest.exists():
        return False, ["MANIFEST.sha256 missing"]

    expected = {}
    for raw in manifest.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        digest, rel = raw.split("  ", 1)
        expected[rel] = digest

    actual = {}
    for path in iter_files(root):
        rel = path.relative_to(root).as_posix()
        actual[rel] = sha256(path)

    issues = []
    for rel in sorted(set(expected) - set(actual)):
        issues.append(f"manifest entry missing from package: {rel}")
    for rel in sorted(set(actual) - set(expected)):
        issues.append(f"unmanifested file: {rel}")
    for rel in sorted(set(actual) & set(expected)):
        if actual[rel] != expected[rel]:
            issues.append(f"hash mismatch: {rel}")

    return not issues, issues
