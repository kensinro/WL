from __future__ import annotations

import json
from pathlib import Path


def load_evidence(path: str | Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def validate_frozen_evidence(data: dict) -> list[str]:
    issues: list[str] = []

    intervention = data.get("intervention", {})
    if intervention.get("cases") != 3:
        issues.append("intervention cases must equal 3")

    e5 = intervention.get("e5_pass", {})
    if (e5.get("numerator"), e5.get("denominator")) != (3, 3):
        issues.append("E5 frozen result must equal 3/3 PASS")

    c2 = intervention.get("case2", {})
    if c2.get("e1_e4_total_judgments") != 16:
        issues.append("Case 2 E1-E4 total must equal 16")
    if c2.get("post", 0) + c2.get("pre", 0) + c2.get("tie", 0) != 16:
        issues.append("Case 2 POST+PRE+TIE must equal 16")
    if c2.get("post", 0) + c2.get("pre", 0) != c2.get("directional_judgments"):
        issues.append("Case 2 directional denominator must equal POST+PRE")
    pad = c2.get("post_among_directional", {})
    if (pad.get("numerator"), pad.get("denominator")) != (8, 11):
        issues.append("Case 2 POST among directional must equal 8/11")

    c3 = intervention.get("case3", {})
    if c3.get("protocol_valid_evaluators") != 3:
        issues.append("Case 3 protocol-valid evaluator denominator must equal 3")
    for key in ("overall_post", "e1_post", "e4_post"):
        obj = c3.get(key, {})
        if (obj.get("numerator"), obj.get("denominator")) != (3, 3):
            issues.append(f"Case 3 {key} must equal 3/3")
    for key in ("e2", "e3"):
        obj = c3.get(key, {})
        if obj.get("post") != 2 or obj.get("tie") != 1 or obj.get("denominator") != 3:
            issues.append(f"Case 3 {key} must equal POST 2/3 + TIE 1/3")
    if c3.get("excluded_evaluators") != 1:
        issues.append("Case 3 excluded evaluator count must equal 1")
    if c3.get("excluded_failure_type") != "SYSTEMATIC_A_B_LABEL_INVERSION":
        issues.append("Case 3 exclusion reason mismatch")

    exe = data.get("executable_governance", {})
    exact_pairs = {
        "source_regression": ("pass", 64, 64),
        "built_package_regression": ("pass", 64, 64),
        "demonstration_fixture": ("pass", 29, 29),
        "adversarial_challenge_1": ("detected", 7, 7),
        "adversarial_challenge_2": ("detected", 8, 8),
    }
    for key, (field, expected, total) in exact_pairs.items():
        obj = exe.get(key, {})
        if obj.get(field) != expected or obj.get("total") != total:
            issues.append(f"{key} frozen count mismatch")

    w1 = exe.get("witness_1", {})
    if (w1.get("pass"), w1.get("hold"), w1.get("total")) != (25, 4, 29):
        issues.append("witness_1 must equal 25 PASS + 4 HOLD = 29")
    if w1.get("pass", 0) + w1.get("hold", 0) != w1.get("total"):
        issues.append("witness_1 denominator mismatch")

    w2 = exe.get("witness_2", {})
    if (w2.get("pass"), w2.get("hold"), w2.get("total")) != (27, 2, 29):
        issues.append("witness_2 must equal 27 PASS + 2 HOLD = 29")
    if w2.get("pass", 0) + w2.get("hold", 0) != w2.get("total"):
        issues.append("witness_2 denominator mismatch")

    boundary = data.get("scientific_claim_boundary", {})
    if boundary.get("population_efficacy_claimed") is not False:
        issues.append("population efficacy must not be claimed")
    if boundary.get("universal_writing_superiority_claimed") is not False:
        issues.append("universal writing superiority must not be claimed")
    if boundary.get("software_pass_equals_scientific_correctness") is not False:
        issues.append("software PASS must not equal scientific correctness")

    return issues
