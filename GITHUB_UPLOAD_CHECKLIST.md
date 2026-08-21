# GitHub Upload Checklist

Before upload:

- [ ] delete the old repository contents or create a clean repository
- [ ] upload the complete contents of this package without nesting the package folder inside another folder
- [ ] keep `.github/workflows/tests.yml`
- [ ] do not add private/internal specifications
- [ ] do not add a software license unless separately authorized
- [ ] run local tests and package verification
- [ ] confirm `MANIFEST.sha256`

After upload:

- [ ] confirm repository tree matches this package
- [ ] confirm GitHub Actions PASS
- [ ] update `RELEASE_STATUS.json` only after live verification
- [ ] regenerate `MANIFEST.sha256` after any authorized status-file change
- [ ] create an immutable tag/release only after the frozen commit passes
- [ ] archive to Zenodo only after GitHub release identity is frozen
- [ ] add DOI to metadata only after DOI resolves to the exact archived object

Do not backdate later GitHub/Zenodo PASS into the earlier frozen study record.
