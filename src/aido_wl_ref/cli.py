from __future__ import annotations

import argparse
from pathlib import Path

from .evidence import load_evidence, validate_frozen_evidence
from .manifest import verify_manifest
from .package import validate_package
from .release import local_release_candidate_gate


def _print(label: str, issues: list[str]) -> int:
    if issues:
        print(f"{label}: HOLD")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(f"{label}: PASS")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(prog="aido-wl-ref")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_ev = sub.add_parser("evidence")
    p_ev.add_argument("path")

    p_pkg = sub.add_parser("package")
    p_pkg.add_argument("root", nargs="?", default=".")

    p_mf = sub.add_parser("manifest")
    p_mf.add_argument("root", nargs="?", default=".")

    p_rel = sub.add_parser("release")
    p_rel.add_argument("root", nargs="?", default=".")

    args = parser.parse_args()

    if args.cmd == "evidence":
        issues = validate_frozen_evidence(load_evidence(args.path))
        return _print("EVIDENCE_CHECK", issues)
    if args.cmd == "package":
        return _print("PACKAGE_CHECK", validate_package(args.root))
    if args.cmd == "manifest":
        ok, issues = verify_manifest(args.root)
        return _print("MANIFEST_CHECK", [] if ok else issues)
    if args.cmd == "release":
        return _print("LOCAL_RELEASE_CANDIDATE", local_release_candidate_gate(args.root))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
