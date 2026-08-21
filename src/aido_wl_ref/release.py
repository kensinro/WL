from __future__ import annotations

import json
from pathlib import Path


ALLOWED_GITHUB = {"NOT_YET_VERIFIED", "LIVE_VERIFIED"}
ALLOWED_IMMUTABLE = {"NOT_YET_CREATED", "LIVE_VERIFIED"}
ALLOWED_CANONICAL = {"IDENTIFIED_NOT_PUBLIC", "PUBLIC_PROOF_BOUNDARY_VERIFIED"}
ALLOWED_LICENSE = {"NO_PUBLIC_REUSE_LICENSE", "LICENSE_GRANTED"}
ALLOWED_ZENODO = {"NOT_YET_VERIFIED", "LIVE_VERIFIED"}
ALLOWED_DOI = {"NOT_YET_VERIFIED", "LIVE_VERIFIED"}


def load_release_status(root: str | Path) -> dict:
    root = Path(root)
    return json.loads((root / "RELEASE_STATUS.json").read_text(encoding="utf-8"))


def validate_release_truth(root: str | Path) -> list[str]:
    root = Path(root)
    status = load_release_status(root)
    issues: list[str] = []

    if status.get("package_version") != "0.1.1":
        issues.append("package_version must equal 0.1.1")
    if status.get("release_tier") != "MINIMUM_PUBLIC_PROOF":
        issues.append("release_tier must equal MINIMUM_PUBLIC_PROOF")
    if status.get("github_repository_status") not in ALLOWED_GITHUB:
        issues.append("unrecognized GitHub repository status")
    if status.get("immutable_release_status") not in ALLOWED_IMMUTABLE:
        issues.append("unrecognized immutable release status")
    if status.get("canonical_spec_status") not in ALLOWED_CANONICAL:
        issues.append("canonical specification boundary not resolved")
    if status.get("license_status") not in ALLOWED_LICENSE:
        issues.append("license boundary not resolved")
    if status.get("zenodo_status") not in ALLOWED_ZENODO:
        issues.append("unrecognized Zenodo status")
    if status.get("doi_status") not in ALLOWED_DOI:
        issues.append("unrecognized DOI status")
    if status.get("scientific_claim_status") != "BOUNDED_INTERNAL_VALIDATION":
        issues.append("scientific claim ceiling mismatch")
    if status.get("full_private_implementation_included") is not False:
        issues.append("full private implementation must not be included")

    # No backdating / impossible state checks.
    if status.get("immutable_release_status") == "LIVE_VERIFIED" and status.get("github_repository_status") != "LIVE_VERIFIED":
        issues.append("immutable release cannot be verified before live GitHub verification")
    if status.get("doi_status") == "LIVE_VERIFIED" and status.get("zenodo_status") != "LIVE_VERIFIED":
        issues.append("DOI cannot be verified before archive verification")

    return issues


def local_release_candidate_gate(root: str | Path) -> list[str]:
    root = Path(root)
    issues = validate_release_truth(root)

    required = [
        "CANONICAL_SPEC_BOUNDARY.md",
        "PUBLIC_PRIVATE_RELEASE_BOUNDARY.md",
        "LICENSE_BOUNDARY.md",
        "REPRODUCIBILITY.md",
        "MANUSCRIPT_RELEASE_CROSSWALK.md",
        "data/frozen_evidence.json",
    ]
    for rel in required:
        if not (root / rel).exists():
            issues.append(f"required release-boundary artifact missing: {rel}")

    # Local candidate readiness does NOT require live GitHub, immutable release,
    # Zenodo, or DOI verification. Those are downstream states.
    return issues
