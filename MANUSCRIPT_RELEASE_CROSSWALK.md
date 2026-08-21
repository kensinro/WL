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
