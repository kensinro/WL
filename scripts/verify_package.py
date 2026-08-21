from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from aido_wl_ref.evidence import load_evidence, validate_frozen_evidence
from aido_wl_ref.manifest import verify_manifest
from aido_wl_ref.package import validate_package
from aido_wl_ref.release import local_release_candidate_gate


def report(label: str, issues: list[str]) -> bool:
    if issues:
        print(f"{label}: HOLD")
        for issue in issues:
            print(f"- {issue}")
        return False
    print(f"{label}: PASS")
    return True


def main():
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT

    evidence_issues = validate_frozen_evidence(
        load_evidence(root / "data" / "frozen_evidence.json")
    )
    evidence_ok = report("EVIDENCE_CHECK", evidence_issues)

    manifest_ok, manifest_issues = verify_manifest(root)
    report("MANIFEST_CHECK", [] if manifest_ok else manifest_issues)

    release_issues = local_release_candidate_gate(root)
    release_ok = report("LOCAL_RELEASE_CANDIDATE", release_issues)

    package_issues = validate_package(root)
    package_ok = report("PACKAGE_CHECK", package_issues)

    if evidence_ok and manifest_ok and release_ok and package_ok:
        print("OVERALL: PASS")
        return 0
    print("OVERALL: HOLD")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
