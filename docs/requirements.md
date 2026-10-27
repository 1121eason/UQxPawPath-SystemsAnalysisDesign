# Requirements catalogue

[Back to portfolio](../README.md)

The following story and criterion text is extracted from sections 1 and 2 of the supplied revised report. Wording is preserved; this public edition omits the cover, student identifiers and teaching materials. [Machine-readable JSON](../analysis/requirements.json) · [84-criterion CSV](../analysis/acceptance-criteria.csv).

All entries are specifications. Quality thresholds require stakeholder confirmation and implementation testing.

## Functional requirements

### FUS1 Create Animal Intake Record

AS A Shelter Staff Member, I WANT to record complete intake information, SO THAT I identify each animal throughout shelter care.

- **FUS1.AC1** Require species, approximate age, sex, coat markings, arrival circumstances and intake timestamp before completing intake.
- **FUS1.AC2** Capture arrival source and surrenderer contact details or transferring officer name, council and contact details, as applicable.
- **FUS1.AC3** For council transfers, require paperwork attachments or an explicit not applicable reason before assessments are enabled.
- **FUS1.AC4** Generate a unique shelterId; reject duplicate identifiers without creating another animal record.
- **FUS1.AC5** Require at least one identification photograph linked to the intake record before completion.
- **FUS1.AC6** Completed intake sets Under Assessment and enables independent health, ownership and behaviour assessments.

### FUS2 Assess Animal Health and Manage Treatment

AS A Veterinarian, I WANT to document examination and treatment decisions, SO THAT I establish medical fitness before public adoption.

- **FUS2.AC1** Save animal reference, examinedAt, veterinarian, body condition, dental health, coat and skin condition, and injury findings.
- **FUS2.AC2** Record species-specific screening results; document blood or faecal samples as collected, pending, negative, positive or not required.
- **FUS2.AC3** Require urgentTreatmentRequired Boolean; true means the veterinarian judges delay risks immediate deterioration, with urgentTreatmentReason recorded.
- **FUS2.AC4** Urgent cases require treatmentPlan and immediate-care recording; unresolved treatment blocks clearance and public listing.
- **FUS2.AC5** Record dated treatment, monitoring, treatmentOutcome and reassessment findings in the same MedicalRecord linked to the animal.
- **FUS2.AC6** Only a veterinarian can clear the urgent flag after reassessment; recovery returns the animal to combined fitness review.

### FUS3 Determine Ownership and Behavioural Suitability

AS A Shelter Staff Member, I WANT to record ownership and temperament outcomes, SO THAT I prevent unlawful or unsuitable public listing.

- **FUS3.AC1** Record microchip detection; require microchipNumber when detected and retain the registry lookup outcome.
- **FUS3.AC2** For identified owners, store contact attempts, holdJurisdiction and holdUntil using the applicable statutory period.
- **FUS3.AC3** Before holdUntil, block clearance; verified reclamation records return to owner and closes the intake without listing.
- **FUS3.AC4** Record responses to handling, animals, food and unfamiliar people, with assessor, assessment date and suitabilityResult.
- **FUS3.AC5** An unsuitable result requires behaviour referral and reassessment; permanent unsuitability closes the public-adoption pathway.
- **FUS3.AC6** Combined fitness review requires three completed assessments; listing additionally requires ownership clear, suitable behaviour and medical fitness.

### FUS4 Prepare Animal for Public Adoption

AS A Veterinarian, I WANT to complete preparation and authorise clearance, SO THAT I make eligible animals available for adoption.

- **FUS4.AC1** Record species-appropriate vaccination type, administration date and boosterDueDate; reject missing or chronologically inconsistent dates.
- **FUS4.AC2** Record desexingStatus as completed or scheduled; a scheduled procedure requires a date and identified shelter policy permitting listing.
- **FUS4.AC3** Vaccination and desexing preparation proceed independently; both must satisfy policy before medical clearance.
- **FUS4.AC4** Clearance records veterinarian and sign-off time; unresolved treatment, ownership hold or unsuitable temperament blocks authorisation.
- **FUS4.AC5** Only cleared animals can change from Under Assessment to Available for Adoption; failed transitions retain the previous status.
- **FUS4.AC6** Publish approved photographs, temperament notes and medical summary only; owner, applicant and raw clinical records remain private.

### FUS5 Assess Adoption Application

AS A Shelter Staff Member, I WANT to assess each complete adoption application, SO THAT I select suitable applicants for a meet-and-greet.

- **FUS5.AC1** Require selected available animal, applicant contact, household, referee and adoption-reason details; missing fields prevent completed submission.
- **FUS5.AC2** Assign applicationId and preserve submissions; incomplete applications return for correction before suitability review.
- **FUS5.AC3** Record referenceCheckResult, contacted referee, date and supporting evidence; pending results cannot support approval.
- **FUS5.AC4** Record homeSuitabilityResult, tenure, yard security and landlord permission; not applicable decisions require a reason.
- **FUS5.AC5** Record petCompatibilityResult and species or temperament evidence; no existing pets is recorded explicitly with justification.
- **FUS5.AC6** All three satisfactory results permit progression; any unsatisfactory result requires rejection reason, applicant notification and available status restoration.

### FUS6 Finalise Adoption Placement

AS A Shelter Staff Member, I WANT to confirm compatibility and placement prerequisites, SO THAT I finalise a valid adoption.

- **FUS6.AC1** Schedule a meet-and-greet only after approval; store application reference, meetingAt and supervising staff.
- **FUS6.AC2** Record compatible or incompatible outcome with observations; an unrecorded outcome blocks finalisation.
- **FUS6.AC3** Incompatibility closes that application, records notification and restores the animal to Available for Adoption.
- **FUS6.AC4** Compatibility enables signed agreement and payment confirmation in parallel, linked to the same application.
- **FUS6.AC5** Require signature reference and successful payment reference; missing, failed or pending payment blocks finalisation.
- **FUS6.AC6** Finalisation creates one AdoptionRecord and sets Adopted before the final medical check; duplicate requests cannot create duplicate placements.

### FUS7 Complete Final Medical Release and Follow-Up

AS A Veterinarian, I WANT to confirm fitness and care requirements before release, SO THAT I support safe placement and follow-up.

- **FUS7.AC1** Record the final examination date, veterinarian and latestMedicalCheckPassed against the adopted animal.
- **FUS7.AC2** Record applicable care instructions, medication schedule and dietary advice; identify not applicable items explicitly.
- **FUS7.AC3** A failed check sets Release Paused; treatment and a new examination are required before release can resume.
- **FUS7.AC4** Release remains blocked until the latest check passes, regardless of an earlier clearance or successful payment.
- **FUS7.AC5** Staff confirm recipient and releasedAt only for a valid adoption with a passed current check.
- **FUS7.AC6** After release, require followUpMethod and followUpDueAt within the agreement period; retain completion outcome when follow-up occurs.


## Non-functional requirements

### NFUS1 Protect Role-Based Access

AS A Shelter Staff Member, I WANT to use authenticated role permissions, SO THAT I prevent unauthorised changes.

- **NFUS1.AC1** Each staff account has a unique identifier; passwords use salted one-way hashing and never appear in logs.
- **NFUS1.AC2** Staff manage intake and placement; veterinarians authorise clinical outcomes; applicants access only their own applications.
- **NFUS1.AC3** Direct unauthorised requests return no protected data and log actor, action, timestamp and denial outcome.
- **NFUS1.AC4** Five failed logins in 15 minutes lock the account for 15 minutes or until authorised administrator unlock.
- **NFUS1.AC5** Internal sessions expire after 15 inactive minutes; the next protected request requires authentication.
- **NFUS1.AC6** Permission changes take effect within five minutes, including existing sessions, and record administrator and timestamp.

### NFUS2 Preserve Personal and Sensitive Data Privacy

AS A Prospective Adopter, I WANT to protect my personal and household information, SO THAT I apply without unnecessary privacy exposure.

- **NFUS2.AC1** Use TLS 1.2 or later in transit and encrypted databases and backups; reject unencrypted protected-data requests.
- **NFUS2.AC2** Public responses and exports exclude owner contacts, microchip numbers, applications, payment details and raw medical notes.
- **NFUS2.AC3** Before application submission, display collection purpose and record privacy-notice version, acknowledgement and timestamp.
- **NFUS2.AC4** Veterinarians access release contacts and care needs; household and referee evidence remains staff-restricted.
- **NFUS2.AC5** Store payment reference and outcome only; never store card verification codes or full payment-card numbers.
- **NFUS2.AC6** Apply a management-approved retention schedule; delete or irreversibly de-identify expired personal data within 30 days, logging completion.

### NFUS3 Maintain Responsive Performance

AS A Shelter Staff Member, I WANT to receive prompt system responses, SO THAT I complete time-sensitive shelter work.

- **NFUS3.AC1** Animal-search response time is at most two seconds at the 95th percentile with 50 active internal users.
- **NFUS3.AC2** Public listings become usable within three seconds at the 95th percentile with 100 concurrent visitors.
- **NFUS3.AC3** Valid intake, assessment and status updates confirm within two seconds at the 95th percentile.
- **NFUS3.AC4** A valid 10 MB photograph uploads and confirms within five seconds at the 95th percentile.
- **NFUS3.AC5** Valid application submission confirms within three seconds; retrying the same request returns the same applicationId.
- **NFUS3.AC6** A 30-minute mixed-load test uses 50 internal users, 100 visitors and 10,000 animals; server errors remain below 1%.

### NFUS4 Sustain Availability and Recoverability

AS A Shelter Staff Member, I WANT to retain dependable access and recovery, SO THAT I continue animal care after system failures.

- **NFUS4.AC1** Achieve 99.5% monthly availability, measured by successful one-minute probes, excluding approved announced maintenance.
- **NFUS4.AC2** Announce maintenance 48 hours ahead; schedule outside the proposed 08:00 to 18:00 shelter operating window.
- **NFUS4.AC3** Three consecutive failed probes trigger an alert to support within five minutes of the first failure.
- **NFUS4.AC4** Back up critical records every 15 minutes and take encrypted daily backups stored separately from production.
- **NFUS4.AC5** Recovery loses at most 15 minutes of committed data and restores critical service within four hours.
- **NFUS4.AC6** Quarterly restoration verifies identifiers, relationships and latest committed values across animal, medical, application, agreement and placement records.

### NFUS5 Support Usable and Error-Resistant Work

AS A Shelter Staff Member, I WANT to use clear consistent workflows, SO THAT I avoid welfare and placement errors.

- **NFUS5.AC1** After 60 minutes of training, each participant completes intake within five minutes without critical error.
- **NFUS5.AC2** Required fields are identified before submission; validation identifies the field, problem and corrective action.
- **NFUS5.AC3** Validation failures preserve all valid entries and attachments; users correct errors without re-entering unaffected information.
- **NFUS5.AC4** Rejection, adoption finalisation and release require a confirmation showing animal, application, previous status and proposed outcome.
- **NFUS5.AC5** Status labels match the domain model across forms, searches, dashboards and exports.
- **NFUS5.AC6** Five representative staff perform four core tasks each; at least 18 of 20 succeed unaided, with zero unsafe releases.

### NFUS6 Preserve Record Integrity and Auditability

AS A Shelter Staff Member, I WANT to retain consistent traceable records, SO THAT I trust welfare and placement decisions.

- **NFUS6.AC1** Intake and adoption finalisation commit all required related records atomically; injected failure leaves no partial transaction.
- **NFUS6.AC2** Unique constraints reject duplicate shelterId and applicationId; repeated finalisation returns the existing adoption record.
- **NFUS6.AC3** Updates include record version; stale submissions are rejected with a conflict message and retain unsaved user changes.
- **NFUS6.AC4** Critical changes log actor, UTC timestamp, record identifier, action and before-and-after values.
- **NFUS6.AC5** Ordinary users cannot change or delete audit entries; retention follows the approved audit schedule.
- **NFUS6.AC6** Daily checks report orphan records, invalid status transitions and released animals without passed checks within one hour; affected finalisation is blocked.

### NFUS7 Provide Accessible Public Services

AS A Prospective Adopter, I WANT to use accessible public listings and forms, SO THAT I browse and apply independently.

- **NFUS7.AC1** All public browse-and-apply pages satisfy WCAG 2.2 Level AA, checked manually and with automated tools (W3C, 2024).
- **NFUS7.AC2** Every interaction works by keyboard, with logical focus order, visible unobscured focus and no keyboard trap.
- **NFUS7.AC3** Controls expose accessible names; screen readers announce required fields, validation errors and submission outcomes.
- **NFUS7.AC4** Meaningful animal photographs have descriptive alternative text; decorative images are ignored by assistive technology.
- **NFUS7.AC5** Text contrast meets 4.5:1, or 3:1 for large text; 200% zoom preserves all content and functions.
- **NFUS7.AC6** Test current and previous Chrome, Edge and Safari releases, plus NVDA with Chrome and VoiceOver with Safari.

## Reading quality targets

For example, NFUS3 defines p95 response-time targets under a stated load; NFUS4 proposes 99.5% monthly availability, a 15-minute recovery point and four-hour restoration. These figures specify what a future solution should be tested against. No benchmark, recovery drill, accessibility audit or security control implementation is supplied.

NFUS7 names WCAG 2.2 AA as a proposed acceptance target. The standard is referenced in the source report; this portfolio does not claim audited compliance.
