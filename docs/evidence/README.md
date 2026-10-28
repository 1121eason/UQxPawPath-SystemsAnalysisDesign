# Evidence, provenance and limitations

[Project overview](../../README.md)

## Current publication checks

On 28 October 2026, all **34 entries** in the supplied SHA-256 manifest matched the Desktop source package. The native model's current hash matched both model and validation-copy snapshot hashes recorded in the supplied JSON. The public PNGs and retained records are byte-identical copies; their mapping and hashes are in [provenance.json](provenance.json).

Native model SHA-256: `c1b168b4f2c3601d5f3b41263e480305b543a1da9f4735d330b93ad00d432310`.

`scripts/verify_portfolio.py` verifies the public manifest, image/record hashes, 14 story IDs, 84 criterion IDs and internal document links. It reads the supplied check record, but does not reproduce its database inspection or native EA run.

## Supplied historical evidence

| Evidence | What it records | Limit |
| --- | --- | --- |
| [Native export log](native-export-log.txt) | Final model opened; seven PNG and seven EMF exports completed at 00:00:18 on 28 October 2026 | Export success does not establish semantic correctness |
| [Report Only screenshot](screenshots/EA_Report_Only_No_Problems.png) | Six integrity checks selected; UML 2.0 Migration excluded; Checks Complete / No problems found | Bounded repository-integrity result |
| [UML completion](screenshots/EA_UML_Validation_Complete.png), [text result](uml-validation-result.txt) | Validation complete: 0 errors, 0 warnings | Applies to EA's enabled built-in rules on that snapshot |
| [Enabled rule groups](screenshots/EA_UML_Enabled_Rules.png) | All 12 listed groups checked | A configuration screenshot does not establish complete business-rule coverage |
| [Validation-copy hashes](validation-copy-hashes.json) | Recorded source and UQ-local validation snapshot hashes match | Current source hash rechecked; the validation snapshot itself is not distributed publicly |
| [Supplied static verification](supplied-verification.json) | 103 PASS entries, including persisted model data, references, diagram structure and AC counts | Historical results; not independently rerun during publication |

The static record additionally reports 98 table schemas, 244 index traversals and 2,552 readable rows. The native model is an Enterprise Architect Microsoft Access repository. These figures describe model storage, not an implemented PawPath application database.

The export log contains an earlier 23:56 start. The source validation README explains that the successful export round began at 23:58:32 after EA licensing loaded. The shared-folder UML attempt was cancelled; it is not used as pass evidence. Validation completed on a UQ-local copy instead.

## Validation scope and limitations

- Complete business-case semantics, visual layout quality and conformity to every teaching convention.
- Stakeholder agreement with assumptions, legal hold policy or proposed quality thresholds.
- Software implementation, integration, access-control enforcement, load tests, restoration, accessibility conformance and user acceptance.
- Operational savings, animal-welfare outcomes, a particular assessment grade or submission readiness.

The source contains crowded class multiplicity labels and dense connectors. These remain visible in the unmodified diagrams. Detailed review of the corresponding native model endpoints remains an implementation and academic-validation consideration.

## Source handling

Public: analysis documentation, extracted requirements, selected review scenarios, all 19 supplied diagram PNGs, three validation screenshots, and four original validation/export records. Private: native model, original reports and revision notes, full package metadata and the assignment brief. No student IDs, teaching PDFs, editable reports or native model binary are committed publicly.

Original report date: 11 September 2026. Revised report date: 27 October 2026. Native exports and completed validation evidence: 28 October 2026, Brisbane time. This repository uses the revised snapshot; no grade is inferred from it.
