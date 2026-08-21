from pathlib import Path

from aido_wl_ref.package import validate_package


ROOT = Path(__file__).resolve().parents[1]


def test_public_package_has_no_full_canonical_spec():
    assert not (ROOT / "WL1.2.0.md").exists()


def test_public_package_has_no_license_file():
    assert not (ROOT / "LICENSE").exists()


def test_package_validator_passes():
    assert validate_package(ROOT) == []
