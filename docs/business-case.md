# Business case and system scope

[Back to portfolio](../README.md)

## Business question

PawPath is a proposed animal shelter and adoption management system. Its central coordination problem is deciding when an animal is eligible to be listed, when an adoption is valid, and when the animal can physically leave. Different people provide evidence at different times, and a later health finding can change release eligibility.

The analysis covers two connected workflows: **animal intake to medical clearance** and **adoption application to placement**. It treats animal welfare, ownership clearance and placement validity as prerequisites that the system must represent explicitly.

## Roles and boundaries

| Role or participant | Responsibility in the design | Boundary |
| --- | --- | --- |
| Shelter staff | Intake records, ownership contact, application checks, agreements, payment confirmation, placement and release recording | Clinical authorisation belongs to a veterinarian |
| Veterinarian | Health assessments, urgency decisions, treatment, clearance, final checks and care instructions | PawPath stores and checks evidence; it does not diagnose animals |
| Trained staff | Temperament assessment, behavioural referral and reassessment | Permanent unsuitability closes the public-adoption pathway |
| Council animal control officer | Transfer details and supporting paperwork | Conditional involvement when intake is through council |
| Prospective adopter | Browse approved profiles, submit details, attend meetings, sign an agreement and submit payment | Access to their own application; public information is a restricted projection |
| National pet registry | Ownership lookup when a microchip is detected | Modelled as an external, read-only interaction |

The use case actor `ShelterPersonnel` generalises shared personnel responsibilities. The activity view gives trained behavioural work its own lane. These views use different levels of detail, so a production handoff would still need a final actor-to-role mapping.

## Scope and intended business value

| Business concern | Specified control | Intended value to validate |
| --- | --- | --- |
| Parallel assessments finish at different times | Join assessment completion, then evaluate eligibility conditions | Fewer premature listing decisions |
| A registered owner may reclaim an animal | Record jurisdiction and hold deadline; block listing while active | Traceable ownership decisions |
| A rejected or incompatible application ends | Record reason and notification; restore animal availability | Clear application outcomes and reusable availability |
| Agreement or payment is incomplete | Require both before finalisation | Consistent placement records |
| A new health issue appears after adoption | Pause release until the latest recheck passes | Safe physical handover without losing adoption history |

These are design intentions. The supplied package contains no observed reduction in handling time, unsafe releases or shelter operating costs.

## Assumptions requiring stakeholder confirmation

- Hold duration depends on jurisdiction; no fixed legal period is asserted here.
- Listing an animal with scheduled desexing requires an identified shelter policy.
- The activity report assumes one application reserves an animal. Competing applications, timeouts, withdrawals and concurrency need further specification before implementation.
- An external payment service supplies a confirmation reference and outcome; payment-network integration is outside the model detail.
- Medical, ownership and behaviour flags coexist beneath the primary Animal status.
- Follow-up timing follows the agreement. Performance, recovery and service-hour thresholds are proposed targets.

The project derives requirements from the supplied academic case. Stakeholder interviews, user research, real-shelter policy approval and deployed operation are not evidenced.
