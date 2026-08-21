# AIDO-WL Reference Package

**Package version:** 0.1.0  
**Release tier:** Minimum Public Proof / Reference Package  
**Status:** local release candidate; public repository/archive state must be verified after upload

AIDO-WL is a human-governed, evidence-constrained Writing Layer for reconstructing scientific manuscripts around a protected scientific state.

This repository is deliberately **not** a full release of the internal Writing Layer specification or private development implementation. It contains only the minimum public artifacts needed to inspect the manuscript's bounded executable-governance claims and frozen evidence record.

## What this package does

The public reference package:

- validates the frozen evidence summary reported by the manuscript;
- checks denominator and state consistency for the three-case intervention;
- checks the executable-governance evidence lineage;
- preserves PASS / HOLD distinctions;
- validates the public/private release boundary;
- verifies a SHA-256 manifest;
- provides reproducible command-line checks and automated tests.

It does **not**:

- autonomously write or approve scientific manuscripts;
- establish scientific correctness from software PASS;
- publish the complete internal Writing Layer specification;
- expose the full private implementation;
- grant scientific authority to AI or software;
- claim universal writing improvement or population-level efficacy.

## Frozen manuscript-facing evidence represented here

The public evidence record contains:

- three intervention cases;
- E5 scientific-state invariance: 3/3 PASS;
- Case 2: 16 E1–E4 judgments = POST 8, PRE 3, TIE 5; 11 directional judgments; POST among directional = 8/11;
- Case 3: three protocol-valid evaluators; Overall POST 3/3; E1 POST 3/3; E2 POST 2/3 + TIE 1/3; E3 POST 2/3 + TIE 1/3; E4 POST 3/3; one excluded A/B label-inversion execution failure;
- executable-governance record: source regression 64/64 PASS, built-package regression 64/64 PASS, controlled demonstration 29/29 PASS, witness 1 = 25 PASS + 4 HOLD, adversarial challenge 1 = 7/7 detected, witness 2 = 27 PASS + 2 HOLD, adversarial challenge 2 = 8/8 detected.

These are frozen evidence objects. The package validates their internal consistency; it does not reinterpret them as population-level performance estimates.

## Quick start

Requires Python 3.10+.

```bash
python -m pip install -e .
python -m pytest -q
python scripts/verify_package.py .
```

Expected local disposition:

```text
EVIDENCE_CHECK: PASS
PACKAGE_CHECK: PASS
MANIFEST_CHECK: PASS
LOCAL_RELEASE_CANDIDATE: PASS
```

The GitHub/Zenodo/DOI states remain separate and must be updated only after live verification.

## CLI

```bash
aido-wl-ref evidence data/frozen_evidence.json
aido-wl-ref package .
aido-wl-ref manifest .
aido-wl-ref release .
```

## Public / private boundary

See:

- `PUBLIC_PRIVATE_RELEASE_BOUNDARY.md`
- `CANONICAL_SPEC_BOUNDARY.md`
- `LICENSE_BOUNDARY.md`

## Scientific authority boundary

Software PASS means only that a declared check behaved as specified under the tested inputs.

It does **not** establish scientific correctness, semantic truth, universal reproducibility, manuscript superiority, reader comprehension, journal acceptance, or autonomous scientific entitlement.

Final scientific interpretation and authorization remain Human-Governed.
