# ARCHITECTURE.md

### Required Architecture Inputs

- **Requirements source:** REQUIREMENTS.md
- **Design source:** DESIGN.md
- **System purpose:** A fitness web application delivering science-based, admin-curated exercise and diet plans, allowing subscribers to customize those plans into private copies, and tracking their progress over time. Access requires a paid subscription. (REQUIREMENTS.md, Project purpose)
- **Primary use cases:** Register and authenticate; subscribe; browse and select an exercise or diet plan; customize a plan into a personal copy; log workouts, food intake, weight, and measurements; view progress over time; admin authors, cites, verifies, and publishes plans; consultant accesses an engaged subscriber's data. (REQUIREMENTS.md, Core workflows; FR-11.x)
- **Target users / actors:** Subscriber; Fitness consultant / helper (paid option); Admin. (REQUIREMENTS.md, Primary users / actors)
- **Runtime environment:** Web application, responsive across current desktop and mobile browsers (FR-1.1, FR-1.2). No native client.
- **Server framework:** Node.js (architecture notes). Specific server framework within Node.js: TO BE DECIDED.
- **Client framework:** Vue.js (architecture notes).
- **API style and integration model:** REST over HTTPS between browser client and server (architecture notes). No external integrations — the system is self-contained (REQUIREMENTS.md, External integrations; FR-9.8).
- **Authentication and session model:** Email + password with optional user-enabled MFA for subscribers; passkey required for admin and consultant accounts (architecture notes; FR-2.2, FR-2.3, FR-2.5, FR-2.6, FR-2.8, FR-2.9). Session transport, lifetime, and revocation mechanics: TO BE DECIDED.
- **Data model expectations:** Relational (RDBMS) (architecture notes). Entities from REQUIREMENTS.md: user account; subscription; consultant engagement; exercise plan and diet plan (each with cited sources and verification record); user plan copy; workout log entry; food log entry; body weight entry; body measurement entry; consent record; audit entry. Specific engine, schema, and migration strategy: TO BE DECIDED.
- **Deployment model:** Terraform-managed infrastructure on AWS (architecture notes). Specific services, topology, and environments: TO BE DECIDED.
- **Scale expectations:** Global (architecture notes). Concrete load, latency, availability, and data-residency targets: UNKNOWN. Note that global reach interacts with GDPR/CCPA and US health-law obligations (REQUIREMENTS.md, Regulatory constraints; OQ-3) — residency implications are TO BE DECIDED.
- **Security expectations:** Defined in SECURITY.md, including the initial document-based threat model (2026-07-31), which added trust boundaries 4 and 5 below.

### Initial Architecture (Provisional)

Four boundaries: the browser client, the server-side REST application, relational persistence, and identity/session handling within the server. There is no external-integration boundary and no message broker, because the system is specified as self-contained and must not transmit health data externally (FR-9.8). No background-processing boundary is asserted; whether data export and account deletion run synchronously or asynchronously is an open decision below.

All business rules are enforced server-side. The client renders and validates for usability only; it is never the authority for authorization, entitlement, or data validity.

- **Browser Client (Vue.js)**
  - **Responsibility:** Render all user-facing views and forms; issue REST calls; present plan content and citations; present progress history; enforce the interaction and accessibility conventions in DESIGN.md — visible focus indicators, keyboard operability, inline field-level error presentation with focus moved to the first invalid field, color-independent status signalling, responsive reflow with no loss of function on mobile (FR-1.2), reduced-motion handling, and 200%-zoom/320px reflow. Performs client-side input validation for immediate feedback only.
  - **Inputs:** User interaction; REST responses including validation errors, authorization failures, and entitlement failures.
  - **Outputs:** REST requests; rendered UI; accessible status and error announcements.
  - **Data owned or accessed:** Owns no durable data. Holds transient view state and session credentials as issued by Identity and Session Handling.
  - **Open decisions:** Whether progress history renders as charts, tables, or both (REQUIREMENTS.md OQ-7; DESIGN.md OQ-4). Presentation of citations and verification status (DESIGN.md OQ-5). Presentation and acknowledgement flow for the medical disclaimer (FR-9.6; DESIGN.md OQ-6). Client-side rendering/routing strategy: TO BE DECIDED. Offline capability is out of scope (REQUIREMENTS.md OQ-14).

- **REST API Application (Node.js)**
  - **Responsibility:** Single server-side entry point and the sole authority for business rules. Authenticates every request via Identity and Session Handling; enforces role rules (FR-2.7, FR-10.1), subscription entitlement (FR-3.1, FR-3.2), owner scoping (FR-7.4, FR-9.1), and consultant engagement scoping (FR-11.2, FR-11.3) before any data access. Enforces publication gates (FR-4.4, FR-4.5, FR-4.7), copy-on-customize semantics (FR-7.2, FR-7.5), log-entry validation (FR-8.9), consent capture (FR-9.2), and audit writes on health-data access (FR-9.7, FR-11.4). Owns every business object described below.
  - **Inputs:** Authenticated REST requests from the Browser Client; persisted state.
  - **Outputs:** REST responses; validation and authorization errors carrying the specific failing field or reason so the client can present them per DESIGN.md; persistence reads and writes; audit entries.
  - **Data owned or accessed:** Owns user account, subscription, consultant engagement, exercise plan, diet plan, plan citations and verification records, user plan copy, workout log entry, food log entry, body weight entry, body measurement entry, consent record, and audit entry. Accesses all of them through Relational Persistence.
  - **Open decisions:** Internal module decomposition within the application (plan library, customization, progress logging, entitlement, privacy/data-rights, audit are distinct responsibilities but not necessarily separate deployables) — TO BE DECIDED. Whether data export (FR-9.3) and account deletion (FR-9.4) execute synchronously or as deferred work, which determines whether a background-processing boundary is needed at all — TO BE DECIDED. How subscription state becomes "active" given no payments integration is in scope (REQUIREMENTS.md OQ-1, OQ-13) — UNKNOWN. Source of nutrition data for food logging (REQUIREMENTS.md OQ-5) — UNKNOWN. Consultant capabilities beyond access scoping (REQUIREMENTS.md OQ-12) — UNKNOWN. Whether admin verification re-triggers on plan edit (REQUIREMENTS.md OQ-10) — TO BE DECIDED.

- **Identity and Session Handling**
  - **Responsibility:** Server-side registration, credential verification, MFA challenge for subscribers who enable it, passkey registration and verification for admin and consultant accounts, session establishment and termination, and role resolution supplied to the REST API Application for every request. Rejects invalid credentials without revealing which factor failed (FR-2.3).
  - **Inputs:** Registration, authentication, MFA, passkey, and logout requests; stored credential and passkey material.
  - **Outputs:** Authenticated session context including account identity and role; authentication failures; session termination.
  - **Data owned or accessed:** Owns credential material, MFA enrolment state, passkey registrations, and session state. Reads user account identity and role.
  - **Open decisions:** Whether this is a module of the Node.js application or a separately deployed service — TO BE DECIDED; either way it is a distinct trust boundary. Session transport and lifetime — TO BE DECIDED. Supported MFA factors (REQUIREMENTS.md OQ-9), password policy, and account/MFA recovery flows (OQ-8) — UNKNOWN. Credential storage and cryptographic controls are deferred to SECURITY.md.

- **Relational Persistence (RDBMS)**
  - **Responsibility:** Durable, transactionally consistent storage for all business objects. Enforces referential integrity and ownership relationships in schema. Must retain progress records and plan customizations across subscription lapse (FR-3.4) and preserve customized copies when their source plan changes (FR-7.5).
  - **Inputs:** Reads and writes issued exclusively by the REST API Application and Identity and Session Handling.
  - **Outputs:** Persisted state; integrity constraint violations.
  - **Data owned or accessed:** Stores all entities listed under Data model expectations. Stores no data that originates outside the system.
  - **Open decisions:** Engine, schema design, indexing, retention behavior for audit entries, and deletion mechanics satisfying FR-9.4 (hard delete vs. anonymization, and the completion deadline, both TO BE DECIDED in REQUIREMENTS.md) — TO BE DECIDED. Global-scale replication and data residency — TO BE DECIDED.

**Trust boundaries.** Five: (1) between the Browser Client and the REST API Application — the client is untrusted, and all authorization and validation decisions are re-made server-side regardless of what the client sent; (2) between unauthenticated and authenticated request handling at Identity and Session Handling; (3) between the REST API Application and Relational Persistence, which accepts requests from no other origin; (4) between the CI/CD-and-IaC path and the production environment — the build and deploy pipeline can rewrite the system itself, so its identities and Terraform state are a distinct trust concern (SECURITY.md SEC-CICD-*, SEC-SECRET-3); (5) between the application and human operational access below it — operators and holders of persistence or backup credentials reach health data without traversing the REST API's enforcement point (SECURITY.md SEC-OPS-1, SEC-LOG-7, SQ-13). Boundaries 4 and 5 were identified by the 2026-07-31 threat model (SECURITY.md, Threat Model). There is no external-system boundary: health data does not leave the system (FR-9.8). Role separation (subscriber / consultant / admin) and consultant engagement scoping are enforced inside the REST API Application, not at the network edge.

**Primary data flows.**
1. *Authentication:* Client → Identity and Session Handling → credential/passkey verification → session context returned to client; subsequent requests carry it.
2. *Plan browse and view:* Client → REST API → entitlement and publication checks → Persistence → plan content with citations and verification record → Client.
3. *Customization:* Client → REST API → entitlement check → copy of published plan written as a subscriber-owned record; published plan untouched.
4. *Progress logging:* Client → REST API → consent check, owner scoping, field validation → log entry written → audit entry written.
5. *Progress viewing:* Client → REST API → owner scoping → aggregated log history, and for diet, logged intake compared against the selected plan's targets → Client.
6. *Admin publication:* Admin client → REST API → role check, citation-presence gate, verification record → plan published.
7. *Consultant access:* Consultant client → REST API → active-engagement check → scoped subscriber data → audit entry written.
8. *Data export and deletion:* Client → REST API → owner scoping and sensitive-operation authorization → export assembled or deletion executed → audit entry written. Synchronous vs. deferred execution remains TO BE DECIDED; if deferred, any generated export artifact is itself health data at rest and carries the controls in SECURITY.md SEC-DATA-6.

**Note on DESIGN.md:** DESIGN.md targets WCAG 2.2 AA, which resolves REQUIREMENTS.md OQ-11. The client boundary is therefore treated as having a firm accessibility target, not an open one.

### Requirement Traceability

| Requirement group | Responsible component / boundary | Status |
|---|---|---|
| FR-1.1, FR-1.2 (Delivery Channel) | Browser Client | SUPPORTED |
| FR-2.1–FR-2.9 (Accounts and Authentication) | Identity and Session Handling; REST API Application (FR-2.1 enforcement, FR-2.7 role assignment) | SUPPORTED |
| FR-3.1–FR-3.3 (Subscription entitlement) | REST API Application | PARTIALLY DEFINED — entitlement is enforced, but how a subscription becomes active is unspecified (REQUIREMENTS.md OQ-1) |
| FR-3.4 (Retention across lapse) | REST API Application; Relational Persistence | SUPPORTED |
| FR-4.1–FR-4.7 (Plan Library and Content Verification) | REST API Application; Relational Persistence; Browser Client (FR-4.6 display) | SUPPORTED |
| FR-5.1, FR-5.2 (Exercise Plans) | REST API Application; Browser Client | SUPPORTED |
| FR-6.1–FR-6.3 (Diet Plans) | REST API Application; Browser Client | SUPPORTED |
| FR-7.1–FR-7.5 (Plan Customization) | REST API Application; Relational Persistence | SUPPORTED |
| FR-8.1–FR-8.3, FR-8.6–FR-8.9 (Progress Tracking) | REST API Application; Relational Persistence; Browser Client (FR-8.6 presentation, FR-8.9 error display) | SUPPORTED |
| FR-8.4, FR-8.5 (Food logging and target comparison) | REST API Application; Browser Client | PARTIALLY DEFINED — no nutrition data source is defined (REQUIREMENTS.md OQ-5) |
| FR-9.1 (Owner scoping) | REST API Application | SUPPORTED |
| FR-9.2, FR-9.5, FR-9.6 (Consent, correction, disclaimer) | REST API Application; Browser Client | SUPPORTED |
| FR-9.3, FR-9.4 (Export and deletion) | REST API Application; Relational Persistence | PARTIALLY DEFINED — synchronous vs. deferred execution and deletion mechanics unresolved |
| FR-9.7 (Health-data audit) | REST API Application; Relational Persistence | SUPPORTED |
| FR-9.8 (No external transmission) | System boundary — no external integration exists by construction | SUPPORTED |
| FR-9.9 (Consent withdrawal) | REST API Application | SUPPORTED |
| FR-10.1 (Administration) | REST API Application | SUPPORTED |
| FR-10.2 (Admin plan-action audit) | REST API Application; Relational Persistence | SUPPORTED |
| FR-11.1 (Paid consultant option) | REST API Application | PARTIALLY DEFINED — the paid-option mechanism shares the unresolved payments gap (REQUIREMENTS.md OQ-13) |
| FR-11.2–FR-11.4 (Consultant scoping and audit) | REST API Application | SUPPORTED |

No functional requirement is currently without an assigned responsibility.

### Dependency Rules

- **DR-1** The Browser Client MUST depend on the REST API Application only, and only through its published REST interface. It MUST NOT reach Relational Persistence or Identity and Session Handling storage directly.
- **DR-2** No business rule may exist only in the Browser Client. Every authorization, entitlement, ownership, publication-gate, and validation rule MUST be enforced by the REST API Application, and client-side checks are duplicate convenience only. Server responses MUST carry enough structured detail (failing field, reason) for the client to present errors per DESIGN.md without re-deriving the rule.
- **DR-3** The REST API Application MUST NOT depend on the Browser Client, on client-supplied identity or role claims, or on client-supplied ownership assertions. Identity and role come from Identity and Session Handling; ownership comes from persisted state.
- **DR-4** Every business object has exactly one owning component — the REST API Application — and only that component may mutate it. Published plans are mutable only by admin-role operations; subscriber plan copies and log entries are mutable only by their owning subscriber, or by a consultant with an active engagement where capabilities permit (capabilities TO BE DECIDED, REQUIREMENTS.md OQ-12).
- **DR-5** Relational Persistence MUST be reachable only from the REST API Application and Identity and Session Handling. It MUST NOT initiate calls outward, and it MUST NOT be shared with any component outside this system.
- **DR-6** Dependencies MUST flow in one direction — Client → API → Identity/Persistence — with no cycles. Internal modules of the REST API Application MUST likewise depend across documented interfaces without cycles.
- **DR-7** Should any external service ever be introduced, it MUST be reached only through an internally defined interface owned by the REST API Application, and no vendor-specific type, error, identifier, or behavior may propagate past that interface. Health data MUST NOT cross such an interface (FR-9.8).
- **DR-8** No component may depend on an unresolved decision in a way that hard-codes it. Framework, database engine, session transport, and deployment choices MUST sit behind the component interfaces described above so that resolving them does not change component responsibilities or data flows.
- **DR-9** Audit entry writing (FR-9.7, FR-11.4) MUST be a dependency of every health-data access path within the REST API Application, not an optional caller responsibility that individual paths may omit.
