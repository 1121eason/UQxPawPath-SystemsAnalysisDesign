# Requirement-to-model traceability

[Project overview](../README.md) · [Complete requirements](requirements.md)

The functional mapping combines the model coverage in Appendix A of the revised report with the principal supporting domain classes. It identifies intended coverage; it is not a formal proof that every model completely satisfies every criterion.

| Story | Principal model coverage | Principal classes | Acceptance gate |
| --- | --- | --- | --- |
| FUS1 | UC; AD1; SD1; CL | IntakeRecord; Animal | Complete intake and unique shelterId |
| FUS2 | AD1; SD1; SM; CL | MedicalRecord; Veterinarian | Explicit urgency; treatment resolution |
| FUS3 | AD1; SD1; SM; CL | IntakeRecord; BehaviourAssessment | All assessments complete; ownership clear; behaviour suitable |
| FUS4 | AD1; SD1; SM; CL | MedicalRecord; Animal | Vaccination and desexing policy met; authorised clearance |
| FUS5 | AD2; SD2; CL | AdoptionApplication; ProspectiveAdopter | Three satisfactory suitability checks |
| FUS6 | AD2; SD2; SM; CL | AdoptionApplication; AdoptionAgreement; AdoptionRecord | Compatible meeting; signed agreement; confirmed payment |
| FUS7 | AD2; SD2; SM; CL | Veterinarian; AdoptionRecord | Latest medical check passed before release; follow-up scheduled |

[Traceability dataset (CSV)](../analysis/traceability.csv).

## FUS7: final medical release traceability

1. **Requirement:** FUS7.AC4 blocks release until the latest check passes, even when payment or an earlier clearance is valid.
2. **Activity:** AD2 routes a failed final check through treatment and reassessment before physical release.
3. **Sequence:** SD2 records the check result, pauses release and repeats treatment/recheck interactions.
4. **State:** Adopted can move into Release Paused; passing a recheck permits resumption before release confirmation.
5. **Data:** AdoptionRecord includes `latestMedicalCheckPassed`, `releaseStatus`, `releasedAt`, `followUpMethod` and `followUpDueAt`.
6. **Specified acceptance scenario:** a release request follows an earlier passed check and a latest failed check. The expected result is a block. This scenario is specified, not executed in this repository.

## Non-functional coverage

The UML set principally describes functional behaviour and domain structure. It does not demonstrate implementation of non-functional controls. NFUS1–NFUS7 require additional security, performance, recovery, usability, data-integrity and accessibility testing. The [acceptance review scenarios](../analysis/acceptance-review-scenarios.csv) make a selected set of future checks concrete without marking them passed.
