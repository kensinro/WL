# Code Boundary

This repository is a **reference implementation and public proof layer**.

Included code is intentionally limited to:

- frozen-evidence validation;
- public-package integrity checks;
- manifest generation/verification;
- release-state truth checks;
- command-line wrappers and tests.

It is not the complete internal Writing Layer implementation.

Absence of an internal module from this repository does not imply that the module does not exist. It means only that it is outside the authorized public proof boundary.

The public package must not be used to infer undocumented private capabilities.
