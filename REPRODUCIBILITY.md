# Reproducibility

This package provides a bounded public reproduction of the manuscript-facing evidence record and release-governance checks.

## Environment

- Python 3.10+
- no network access required for the local checks
- no private AIDO-WL artifacts required

## Reproduce

From the repository root:

```bash
python -m pip install -e .
python -m pytest -q
python scripts/verify_package.py .
```

To regenerate the manifest after an authorized repository change:

```bash
python scripts/build_manifest.py .
python scripts/verify_package.py .
```

## What is reproduced

The validator checks the frozen values in `data/frozen_evidence.json`, including:

- three cases and E5 = 3/3 PASS;
- Case 2 denominator logic;
- Case 3 protocol-valid evaluator logic;
- source / built-package / demonstration counts;
- witness PASS + HOLD denominator preservation;
- adversarial detection denominators.

## What is not reproduced here

This minimum public package does not contain:

- the full internal Writing Layer specification;
- complete historical prompts, sessions, or private development records;
- private implementation-sensitive modules;
- unpublished or restricted evidence;
- a claim that software validation establishes scientific correctness.

The manuscript and Supplementary Information remain the authoritative scientific interpretation surfaces.
