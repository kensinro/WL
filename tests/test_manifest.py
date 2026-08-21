from pathlib import Path

from aido_wl_ref.manifest import build_manifest, verify_manifest


ROOT = Path(__file__).resolve().parents[1]


def test_manifest_verifies():
    ok, issues = verify_manifest(ROOT)
    assert ok, issues


def test_manifest_detects_tampering(tmp_path):
    (tmp_path / "a.txt").write_text("A", encoding="utf-8")
    (tmp_path / "MANIFEST.sha256").write_text(build_manifest(tmp_path), encoding="utf-8")
    (tmp_path / "a.txt").write_text("B", encoding="utf-8")
    ok, issues = verify_manifest(tmp_path)
    assert not ok
    assert any("hash mismatch" in x for x in issues)


def test_manifest_detects_unmanifested_file(tmp_path):
    (tmp_path / "a.txt").write_text("A", encoding="utf-8")
    (tmp_path / "MANIFEST.sha256").write_text(build_manifest(tmp_path), encoding="utf-8")
    (tmp_path / "b.txt").write_text("B", encoding="utf-8")
    ok, issues = verify_manifest(tmp_path)
    assert not ok
    assert any("unmanifested file" in x for x in issues)
