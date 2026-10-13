# Manuscript ↔ Public Package Crosswalk

| Manuscript-facing object | Public artifact | Reproduction / check |
|---|---|---|
| Three-case frozen intervention summary | `data/frozen_evidence.json` | `aido-wl-ref evidence data/frozen_evidence.json` |
| E5 = 3/3 PASS | `data/frozen_evidence.json` | evidence validator |
| Case 2 directional denominator | `data/frozen_evidence.json` | evidence validator |
| Case 3 protocol-valid evaluator denominator | `data/frozen_evidence.json` | evidence validator |
| Executable-governance lineage | `data/frozen_evidence.json` | evidence validator |
| Public/private boundary | `PUBLIC_PRIVATE_RELEASE_BOUNDARY.md` | package validator |
| Canonical-spec boundary | `CANONICAL_SPEC_BOUNDARY.md` | package validator |
| No-public-reuse license boundary | `LICENSE_BOUNDARY.md` | release validator |
| Package integrity | `MANIFEST.sha256` | `aido-wl-ref manifest .` |

## Boundary

This crosswalk identifies public verification surfaces. It does not claim that every internal manuscript-production artifact is public.

## Later WL1.1 four-case manuscript (not this v0.1.1 release)

| Later manuscript claim | v0.1.1 public proof support | Status |
|---|---|---|
| Four frozen manuscript cases; E5 4/4 | Existing file covers a different three-case study, E5 3/3 | NOT REPRODUCED HERE |
| 56 union claim records, 51 comparison units | No 51-unit case-level source ledger in v0.1.1 | NOT REPRODUCED HERE |
| 46 STABLE / 5 POST BETTER / RP1 0/51 | Not computed or validated by current repository code | NOT REPRODUCED HERE |
| Old JAE submission versus October publisher-facing draft | Bounded private two-DOCX textual/structural comparison; no primary-data replay | DOCUMENT DRIFT ONLY |
| Independent scientific correctness, novelty or external model robustness | Outside the v0.1.1 code and manuscript-comparison scope | NOT ESTABLISHED |

See [WL1.1 public evidence boundary](WL11_MANUSCRIPT_STATUS_20261013.md). Do not overwrite the frozen three-case ledger with later-study figures.
