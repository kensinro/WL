from __future__ import annotations

from pathlib import Path

from .evidence import load_evidence, validate_frozen_evidence
from .manifest import verify_manifest
from .release import local_release_candidate_gate


REQUIRED_PATHS = (
    "README.md",
    "REPRODUCIBILITY.md",
    "CODE_BOUNDARY.md",
    "PUBLIC_PRIVATE_RELEASE_BOUNDARY.md",
    "CANONICAL_SPEC_BOUNDARY.md",
    "LICENSE_BOUNDARY.md",
    "MANUSCRIPT_RELEASE_CROSSWALK.md",
    "RELEASE_STATUS.json",
    "CITATION.cff",
    ".zenodo.json",
    "pyproject.toml",
    "data/frozen_evidence.json",
    "src/aido_wl_ref",
    "tests",
    "scripts",
    ".github/workflows/tests.yml",
    "MANIFEST.sha256",
)


def validate_package(root: str | Path) -> list[str]:
    root = Path(root)
    issues: list[str] = []

    for rel in REQUIRED_PATHS:
        if not (root / rel).exists():
            issues.append(f"required path missing: {rel}")

    if (root / "data/frozen_evidence.json").exists():
        evidence = load_evidence(root / "data/frozen_evidence.json")
        issues.extend(validate_frozen_evidence(evidence))

    issues.extend(local_release_candidate_gate(root))

    ok, manifest_issues = verify_manifest(root)
    if not ok:
        issues.extend(manifest_issues)

    # Explicit leakage guard: full internal canonical spec must not appear here.
    forbidden_names = {
        "WL1.2.0.md",
        "WRITING_LAYER_V1.2.11_TABLE_NOTE_COMPLETENESS_FIRST_INTERPRETIVE_NECESSITY_GOVERNANCE_2026-08-21.md",
    }
    for name in forbidden_names:
        if (root / name).exists():
            issues.append(f"public-proof boundary violation: {name} must not be included")

    return issues
