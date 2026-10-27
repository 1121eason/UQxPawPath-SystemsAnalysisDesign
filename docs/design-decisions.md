# Design decisions and trade-offs

[Back to portfolio](../README.md) · [Requirements](requirements.md) · [Model gallery](model-gallery.md)

## 1. Separate assessment completion from eligibility

The intake activity forks into health, ownership and behaviour assessments. Joining those paths means each has recorded an outcome. It does not mean every outcome permits listing. Treatment, hold and suitability checks remain explicit gates after the join.

**Trace:** FUS2.AC4–AC6; FUS3.AC3–AC6; FUS4.AC4–AC5 → AD1 / SD1 / State / Class.

**Trade-off:** parallel work can represent independent assessments, but the combined decision needs authoritative current outcomes. A future implementation must define stale-result handling and transaction boundaries. A UML join alone cannot enforce those data rules.

## 2. Model Adopted and Released separately

The agreement and payment paths converge before finalisation. The animal becomes Adopted, then receives the final medical check. A health concern pauses physical release while retaining the existing adoption. A subsequent passed check enables release and follow-up scheduling.

**Trace:** FUS6.AC4–AC6; FUS7.AC1–AC6 → AD2 / SD2 / State / AdoptionRecord.

**Trade-off:** separating these events adds lifecycle states and fields, but prevents a financial or administrative event from being treated as proof of current medical fitness. Cancellation or refund rules for a prolonged pause remain to be designed.

## 3. Make urgent care an explicit clinical decision

`MedicalRecord.urgentTreatmentRequired` is a Boolean. A true value represents the veterinarian's judgement that delay risks immediate deterioration. The record requires a reason, treatment plan and later reassessment. PawPath records and applies the decision; clinical diagnosis remains with the veterinarian.

**Trace:** FUS2.AC3–AC6 → MedicalRecord, Veterinarian, treatment paths in AD1 and SD1.

**Trade-off:** an explicit flag makes a blocking condition visible, but clinical workflow, concurrent updates and who may clear it must be governed. The revised requirement restricts clearance of the flag to a veterinarian after reassessment.

## 4. Represent exceptions and recovery

Incomplete application data loops back for correction. Unsatisfactory suitability checks and unsuccessful meetings record the outcome and restore availability. Treatment and final health checks loop until the release condition is satisfied. Repeated finalisation requests must not create another placement.

**Trace:** FUS5.AC2–AC6; FUS6.AC3 and AC6; FUS7.AC3–AC4; NFUS6.AC1–AC3.

**Trade-off:** explicit exception paths improve reviewability but increase diagram density. The repository preserves native full exports alongside enlarged reading panels. Production design still needs retry limits, notification failure handling and competing-application rules.

## 5. Keep persistent state distinct from work activities

The Animal state machine represents enduring conditions such as Under Assessment, Available for Adoption, Application In Progress, Adopted and Release Paused. It uses events and guards for transitions, with entry/exit behaviour controlling listing visibility.

**Trace:** FUS1.AC6; FUS4.AC5–AC6; FUS6.AC6; FUS7.AC3–AC5 → State / Animal / AdoptionRecord.

**Trade-off:** a single primary state is understandable, while medical, ownership and behaviour flags retain independent facts. A production model should reconcile all combinations and define handling of contradictory or out-of-order events.

## 6. Specify quality in testable terms

The non-functional stories state actors, timing, workload, percentile response targets, access restrictions, recovery objectives, audit fields and accessibility checks. For example, a two-second p95 search target has a stated internal-user load; duplicate finalisation must return the existing record.

**Trace:** NFUS1–NFUS7, especially NFUS3.AC1 / AC6, NFUS4.AC5 and NFUS6.AC2.

**Trade-off:** measurable targets support supplier and acceptance discussions, but require business agreement and representative tests. They are proposed requirements, with no performance or compliance result claimed.

## Review questions before implementation

The native tool results establish a bounded technical check. Manual review should still examine crowded class multiplicity labels, connector routing, actor-to-role alignment and consistency between the 11-state lifecycle and concurrent application handling. The supplied `.eapx` is preserved in the private archive; public diagram exports have not been silently repaired.
