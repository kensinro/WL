import json
from pathlib import Path

from aido_wl_ref.release import validate_release_truth, local_release_candidate_gate


ROOT = Path(__file__).resolve().parents[1]


def test_current_local_release_state_is_truthful():
    assert validate_release_truth(ROOT) == []


def test_local_candidate_does_not_require_live_github_or_zenodo():
    assert local_release_candidate_gate(ROOT) == []


def test_no_backdating_rule_is_enforced(tmp_path):
    status = json.loads((ROOT / "RELEASE_STATUS.json").read_text(encoding="utf-8"))
    status["immutable_release_status"] = "LIVE_VERIFIED"
    status["github_repository_status"] = "NOT_YET_VERIFIED"
    (tmp_path / "RELEASE_STATUS.json").write_text(json.dumps(status), encoding="utf-8")
    issues = validate_release_truth(tmp_path)
    assert any("immutable release cannot be verified" in x for x in issues)


def test_doi_requires_archive_verification(tmp_path):
    status = json.loads((ROOT / "RELEASE_STATUS.json").read_text(encoding="utf-8"))
    status["doi_status"] = "LIVE_VERIFIED"
    status["zenodo_status"] = "NOT_YET_VERIFIED"
    (tmp_path / "RELEASE_STATUS.json").write_text(json.dumps(status), encoding="utf-8")
    issues = validate_release_truth(tmp_path)
    assert any("DOI cannot be verified" in x for x in issues)
