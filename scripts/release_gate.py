from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from aido_wl_ref.package import validate_package
from aido_wl_ref.release import local_release_candidate_gate


def main():
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT

    package_issues = validate_package(root)
    release_issues = local_release_candidate_gate(root)

    if package_issues:
        print("PACKAGE_ACCEPTANCE: HOLD")
        for issue in package_issues:
            print(f"- {issue}")
    else:
        print("PACKAGE_ACCEPTANCE: PASS")

    if release_issues:
        print("LOCAL_RELEASE_CANDIDATE: HOLD")
        for issue in release_issues:
            print(f"- {issue}")
    else:
        print("LOCAL_RELEASE_CANDIDATE: PASS")

    return 0 if not package_issues and not release_issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
