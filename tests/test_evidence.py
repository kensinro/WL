from pathlib import Path
import copy

from aido_wl_ref.evidence import load_evidence, validate_frozen_evidence


ROOT = Path(__file__).resolve().parents[1]


def test_frozen_evidence_passes():
    data = load_evidence(ROOT / "data" / "frozen_evidence.json")
    assert validate_frozen_evidence(data) == []


def test_case2_denominator_tampering_is_detected():
    data = load_evidence(ROOT / "data" / "frozen_evidence.json")
    data = copy.deepcopy(data)
    data["intervention"]["case2"]["directional_judgments"] = 12
    issues = validate_frozen_evidence(data)
    assert any("directional denominator" in x for x in issues)


def test_case3_exclusion_reason_tampering_is_detected():
    data = load_evidence(ROOT / "data" / "frozen_evidence.json")
    data = copy.deepcopy(data)
    data["intervention"]["case3"]["excluded_failure_type"] = "PREFERENCE"
    issues = validate_frozen_evidence(data)
    assert any("exclusion reason" in x for x in issues)


def test_hold_is_preserved_in_witness_denominator():
    data = load_evidence(ROOT / "data" / "frozen_evidence.json")
    data = copy.deepcopy(data)
    data["executable_governance"]["witness_1"]["hold"] = 0
    issues = validate_frozen_evidence(data)
    assert any("witness_1" in x for x in issues)


def test_overclaim_flags_are_detected():
    data = load_evidence(ROOT / "data" / "frozen_evidence.json")
    data = copy.deepcopy(data)
    data["scientific_claim_boundary"]["software_pass_equals_scientific_correctness"] = True
    issues = validate_frozen_evidence(data)
    assert any("scientific correctness" in x for x in issues)
