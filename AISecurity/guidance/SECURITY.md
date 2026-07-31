# SECURITY.md

### Required Security Inputs

- **Requirements source:** REQUIREMENTS.md
- **Design source:** DESIGN.md
- **Architecture source:** ARCHITECTURE.md
- **System purpose:** Subscription-based fitness web application delivering admin-curated, citation-verified exercise and diet plans, subscriber-owned plan customizations, and progress logging (REQUIREMENTS.md, Project purpose).
- **Application profile:** Consumer fitness web application handling self-reported health data.
- **Users / actors / roles:** `subscriber`, `consultant` (fitness consultant/helper, paid option), `admin` (REQUIREMENTS.md FR-2.7, FR-10.1, FR-11.x). Exactly one role per account.
- **Public interfaces and trust boundaries:** One public interface — the browser-facing HTTPS surface of the REST API Application, consumed by the Vue.js Browser Client. Trust boundaries per ARCHITECTURE.md: (1) Browser Client → REST API Application; (2) unauthenticated → authenticated at Identity and Session Handling; (3) REST API Application → Relational Persistence. No separately consumable third-party public API is defined; whether the REST surface is ever published for external consumers is TO BE DECIDED.
- **Sensitive or regulated data:** Health data — body weight, body measurements, workout performance, food intake, and the plans a subscriber follows — plus account credentials, passkey registrations, MFA enrolment state, consent records, subscription and consultant-engagement state, and audit entries (REQUIREMENTS.md, Business objects; security notes: "This is health care data"). All of it is treated as sensitive.
- **External integrations:** None currently. The system is self-contained and MUST NOT transmit health data externally (REQUIREMENTS.md FR-9.8). Security notes say "none YET", so future integrations are anticipated but unspecified — TO BE DECIDED.
- **Authentication model:** Email + password with optional user-enabled MFA for subscribers; passkeys REQUIRED for `admin` and `consultant` accounts (REQUIREMENTS.md FR-2.2, FR-2.3, FR-2.5, FR-2.6, FR-2.8, FR-2.9). Password policy, MFA factors, and account/MFA recovery flows are UNKNOWN (REQUIREMENTS.md OQ-8, OQ-9).
- **Authorization model:** ABAC with capability-based access control (security notes). This refines, and does not replace, the role and ownership rules in REQUIREMENTS.md (FR-2.7, FR-7.4, FR-9.1, FR-10.1, FR-11.2, FR-11.3). Attribute schema, policy language, and policy combination algorithm are TO BE DECIDED.
- **Session model:** JWT (security notes). ARCHITECTURE.md left session transport, lifetime, and revocation TO BE DECIDED; the notes fix the token format only. Token lifetimes, refresh strategy, storage location, and revocation mechanism are TO BE DECIDED — see SQ-2, since FR-2.4 (logout) requires effective session termination.
- **Deployment and CI/CD model:** Terraform-managed infrastructure on AWS (ARCHITECTURE.md; security notes). CI/CD platform, pipeline design, environment topology, and AWS services are UNKNOWN.
- **Applicable privacy or regulatory obligations:** Security notes state US federal and US state law. REQUIREMENTS.md additionally asserts GDPR and CCPA data-subject rights and HIPAA obligations, and sets scale expectations to "global". These are not consistent — see SQ-1. Confirmed and in scope regardless of resolution, because REQUIREMENTS.md mandates them as behavior: explicit consent before health-data collection (FR-9.2), data export (FR-9.3), deletion (FR-9.4), correction (FR-9.5), medical disclaimer (FR-9.6), and health-data audit logging (FR-9.7). Specific statutory obligations beyond those behaviors: TO BE DECIDED.
- **Security assurance target:** OWASP ASVS 5.0.0 Level 3 (security notes). This is a stated target, not a conformance claim; no verification has been performed.
- **Security verification reference:** OWASP ASVS 5.0.0.
- **Threat model status:** Initial document-based threat model completed 2026-07-31 — see the Threat Model section below. STRIDE applied per trust boundary and LINDDUN applied to health-data flows, over the four specification documents only (no implementation exists). Single-perspective (security analyst); cross-functional validation, ownership, and refresh cadence are TO BE DECIDED — see SQ-9.

### Selected Security References and Prompt Imports

Local prompt library located at `/Users/jmanico/Dropbox/github/platform/context/prompts/code security/`. Files below were read; rules were synthesized, not copied.

| ID | Title | Path or URL | Purpose |
|---|---|---|---|
| `REF-PROMPT-NODE` | Secure Node.js Developer | `/Users/jmanico/Dropbox/github/platform/context/prompts/code security/Backend Frameworks/NodeJS/00 Secure Node.js Developer/PROMPT.md` | Server-side runtime hardening: prototype pollution, code execution, input validation, error handling, logging |
| `REF-PROMPT-VUE` | Secure VueJS Developer | `/Users/jmanico/Dropbox/github/platform/context/prompts/code security/Client Side Frameworks/VueJS/00 Secure VueJS Developer/PROMPT.md` | Browser rendering safety: auto-escaping, `v-html` policy, URL validation, client storage |
| `REF-PROMPT-JWT` | Secure JWT Developer | `/Users/jmanico/Dropbox/github/platform/context/prompts/code security/Web and API Security/09 Secure JWT Developer/PROMPT.md` | Token issuance, algorithm enforcement, claim validation, revocation, key management |
| `REF-PROMPT-API` | Secure API Developer | `/Users/jmanico/Dropbox/github/platform/context/prompts/code security/Web and API Security/06 Secure API Developer/PROMPT.md` | REST endpoint authN/authZ, BOLA prevention, mass assignment, response hygiene, rate limiting |
| `REF-PROMPT-ABAC` | ABAC Architect | `/Users/jmanico/Dropbox/github/platform/context/prompts/code security/Authorization/02 ABAC Architect/PROMPT.md` | PDP/PEP/PIP separation, attribute trust levels, policy combination, policy testing |
| `REF-PROMPT-QUALITY` | Secure Code Quality Engineer | `/Users/jmanico/Dropbox/github/platform/context/prompts/code security/Code Quality/00 General Code Quality Prompts/PROMPT.md` | Complexity limits, fail-closed error discipline, centralized validation, auditable security-critical code paths |
| `REF-PROMPT-TF-AWS` | Secure Terraform AWS Developer | `/Users/jmanico/Dropbox/github/platform/context/prompts/code security/Infrastructure/Terraform/01 Secure Terraform AWS Developer/PROMPT.md` | IAM least privilege, encryption at rest and in transit, network tiering, Terraform state protection |

Public references selected as authoritative defaults for the identified stack. These were selected, not retrieved; no claim is made that their contents were read in this session.

| ID | Title and version | URL |
|---|---|---|
| `REF-ASVS-5` | OWASP ASVS 5.0.0 | `https://github.com/OWASP/ASVS/releases/tag/v5.0.0_release` |
| `REF-PC-2024` | OWASP Top 10 Proactive Controls 2024 | `https://top10proactive.owasp.org/archive/2024/the-top-10/` |
| `REF-API-2023` | OWASP API Security Top 10 2023 | `https://owasp.org/API-Security/editions/2023/en/0x11-t10/` |
| `REF-REST` | OWASP REST Security Cheat Sheet | `https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html` |
| `REF-AUTH` | OWASP Authentication Cheat Sheet | `https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html` |
| `REF-SESSION` | OWASP Session Management Cheat Sheet | `https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html` |
| `REF-XSS` | OWASP XSS Prevention Cheat Sheet | `https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html` |
| `REF-INPUT` | OWASP Input Validation Cheat Sheet | `https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html` |
| `REF-SECRETS` | OWASP Secrets Management Cheat Sheet | `https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html` |
| `REF-LOG` | OWASP Logging Cheat Sheet | `https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html` |
| `REF-ERROR` | OWASP Error Handling Cheat Sheet | `https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html` |
| `REF-63B` | NIST SP 800-63B-4 | `https://pages.nist.gov/800-63-4/sp800-63b.html` |
| `REF-PASSKEY` | FIDO Alliance Passkeys | `https://fidoalliance.org/passkeys/` |
| `REF-WEBAUTHN` | W3C Web Authentication | `https://www.w3.org/TR/webauthn/` |
| `REF-SSDF` | NIST SSDF 1.1 (SP 800-218) | `https://csrc.nist.gov/pubs/sp/800/218/final` |
| `REF-CICD` | OWASP CI/CD Security Cheat Sheet | `https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html` |
| `REF-SUPPLY` | OWASP Software Supply Chain Security Cheat Sheet | `https://cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html` |
| `REF-IAC` | OWASP Infrastructure as Code Security Cheat Sheet | `https://cheatsheetseries.owasp.org/cheatsheets/Infrastructure_as_Code_Security_Cheat_Sheet.html` |
| `REF-DEPS` | OWASP Vulnerable Dependency Management Cheat Sheet | `https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html` |

`REF-PASSKEY` and `REF-WEBAUTHN` are included because passkeys are explicitly selected for `admin` and `consultant` accounts (FR-2.8), not by default.

### Threat Model

**Conducted:** 2026-07-31. **Method:** Document and Architecture Absorption (prompt 06 of the threat-modeling suite) over REQUIREMENTS.md, ARCHITECTURE.md, SECURITY.md, and DESIGN.md, with STRIDE applied per trust boundary and LINDDUN applied to the health-data flows. No repository reconnaissance was possible (no implementation exists) and no cross-functional interview was held. **Perspective coverage:** single analyst, security-engineering perspective only — product, legal/privacy, and operations validation is outstanding and required by the methodology before the model is considered complete.

**Scope and limits.** The model covers the documented system, not imagined code. Threats that depend on an unresolved decision (session transport, revocation mechanism, deployment topology, consultant capabilities) are recorded as CONDITIONAL on the open question that resolves them, not assumed one way. It MUST be revisited when SQ-1, SQ-2, SQ-4, and SQ-7 resolve, and again once implementation exists (repository reconnaissance, prompt 05).

**Adversary actors considered:**

| Actor | Position | Notes |
|---|---|---|
| Anonymous internet attacker | Outside boundary 1 | Credential attacks, enumeration, DoS, injection |
| Malicious subscriber | Authenticated, `subscriber` role | Horizontal attacks on other subscribers' data (BOLA), entitlement bypass |
| Malicious or compromised consultant | Authenticated, `consultant` role | Over-access beyond engagement scope, residual access after engagement ends |
| Compromised admin account | Authenticated, `admin` role | Content poisoning of published plans, bulk access to plan library; admin has no documented access to subscriber health data — ASSUMPTION: admin capabilities are limited to plan and account administration, which REQUIREMENTS.md does not fully define |
| Malicious or careless operator / insider | Below the application layer | Direct persistence, backup, log, and Terraform-state access; controls UNKNOWN (SQ-13) |
| Compromised CI/CD identity or dependency | Build/deploy path | Malicious deploy, IaC tamper, supply-chain injection (SQ-7 platform UNKNOWN) |

**Trust boundaries.** ARCHITECTURE.md's three boundaries, plus two the threat model identifies that the architecture did not previously name: **(4)** the CI/CD-and-IaC-to-production boundary (a compromised pipeline or Terraform state rewrites the system itself), and **(5)** the operational/human-access boundary below the application (operators, support staff, and anyone holding persistence or backup credentials reach health data without traversing the REST API's enforcement point). ARCHITECTURE.md has been updated to carry all five.

**Threat inventory.** Severity is qualitative (H/M/L), judged pre-implementation against health-data impact. Status meanings — MITIGATED BY RULE: an existing or new rule in this document covers it (implementation and verification still pending); CONDITIONAL: mitigation depends on an unresolved decision, tracked by the named open question; GAP: no covering rule or requirement existed before this model — the named artifact was added to close or track it.

| ID | Threat | Class | Target / boundary | Sev | Coverage | Status |
|---|---|---|---|---|---|---|
| TM-S-1 | Credential stuffing / password spraying against subscriber login | S | Identity, boundary 2 | H | SEC-AUTHN-3, SEC-AUTHN-6 | CONDITIONAL — thresholds undecided (SQ-3) |
| TM-S-2 | Account/MFA recovery flow used to bypass MFA or passkey | S | Identity, boundary 2 | H | SEC-AUTHN-2 (recovery paths), SEC-AUTHN-6 | CONDITIONAL — recovery flows UNKNOWN (REQUIREMENTS OQ-8) |
| TM-S-3 | Registration with an email the registrant does not control — health data bound to a third party's identity, recovery hijack | S/L | Identity, boundary 2 | M | None previously | GAP → SEC-AUTHN-8; REQUIREMENTS OQ-15 |
| TM-S-4 | Privileged-account bootstrap: first passkey enrolment path for `admin`/`consultant` unspecified and attackable | S | Identity | H | SEC-AUTHN-2, SEC-AUTHN-7 | CONDITIONAL — provisioning UNKNOWN (SQ-12) |
| TM-S-5 | Theft and replay of a JWT (XSS, transport, shared device) | S | Boundary 1 | H | SEC-SESSION-1, SEC-SESSION-2, SEC-SESSION-5 | CONDITIONAL — transport, lifetime, revocation undecided (SQ-2) |
| TM-S-6 | CSRF against state-changing operations if tokens ride in cookies | S/T | Boundary 1 | M | SEC-HTTP-4 | CONDITIONAL — on SEC-SESSION-5 outcome (SQ-2) |
| TM-T-1 | Tampered client payloads: forged roles, foreign owner IDs, mass assignment of server-controlled fields | T/E | Boundary 1 | H | SEC-TB-1, SEC-INPUT-1, SEC-INPUT-3 | MITIGATED BY RULE |
| TM-T-2 | SQL injection through any input-bearing endpoint | T | Boundary 3 | H | SEC-INPUT-5 | MITIGATED BY RULE |
| TM-T-3 | JWT signature/algorithm confusion (`alg: none`, key confusion, claim omission) | T/S | Boundary 2 | H | SEC-SESSION-1, SEC-SESSION-2 | MITIGATED BY RULE |
| TM-T-4 | Stored XSS via admin-authored plan content, citation URLs, or subscriber-entered fields | T | Browser Client | H | SEC-RENDER-1, SEC-RENDER-2, SEC-RENDER-3, SEC-HTTP-2 | MITIGATED BY RULE — CSP directives still TO BE DECIDED |
| TM-T-5 | Compromised admin publishes harmful exercise/diet content; author and verifier may be the same account (no dual control) | T (safety) | Plan library | H | FR-4.4, FR-4.5 gate exists but is single-admin | GAP → REQUIREMENTS OQ-16 (dual-control verification); FR-10.2 / SEC-LOG-6 for accountability |
| TM-T-6 | CI/CD or Terraform-state compromise deploys attacker-controlled code or infrastructure | T/E | Boundary 4 | H | SEC-CICD-1–4, SEC-SECRET-3 | CONDITIONAL — platform and topology UNKNOWN (SQ-7) |
| TM-T-7 | Malicious or vulnerable dependency enters the build | T/E | Boundary 4 | H | DEP-1–DEP-8, SEC-CICD-4 | MITIGATED BY RULE |
| TM-T-8 | Prototype pollution / unsafe dynamic evaluation in the Node.js runtime | T/E | REST API Application | M | SEC-INPUT-6 | MITIGATED BY RULE |
| TM-R-1 | Admin plan lifecycle actions (create, edit, publish, unpublish) unaudited — only verification was recorded, so a hostile admin action is repudiable | R | Plan library | M | FR-4.5 only | GAP → REQUIREMENTS FR-10.2; SEC-LOG-6 |
| TM-R-2 | Audit entries alterable below the application (DB credential holder, operator); SEC-LOG-2 binds the application only | R/T | Boundary 5 | M | SEC-LOG-2 (app layer) | GAP → SEC-LOG-7; SQ-8, SQ-13 |
| TM-I-1 | BOLA/IDOR: subscriber A reads or mutates subscriber B's plan copies, logs, or export | I/T | REST API | H | SEC-AUTHZ-1, SEC-AUTHZ-2, SEC-DATA-3 | MITIGATED BY RULE |
| TM-I-2 | Consultant retains access after engagement ends via still-valid JWT | I | REST API | H | SEC-AUTHZ-3, SEC-SESSION-4 | CONDITIONAL — revocation mechanism undecided (SQ-2) |
| TM-I-3 | Excessive data exposure / bulk retrieval of subscriber records through any role | I | REST API | H | SEC-DATA-5 | MITIGATED BY RULE |
| TM-I-4 | Account-existence enumeration via response content or timing | I/L | Identity | L | SEC-AUTHN-3 | MITIGATED BY RULE |
| TM-I-5 | Health data leaks into logs, error responses, or external analytics/monitoring | I | All outbound paths | H | SEC-TB-3, SEC-LOG-3, SEC-ERR-1 | MITIGATED BY RULE |
| TM-I-6 | Backups, replicas, snapshots hold unencrypted or over-retained health data | I | Persistence | H | SEC-DATA-1, SEC-DATA-4 | CONDITIONAL — deletion mechanics and backup handling undecided (SQ-5) |
| TM-I-7 | Data export (FR-9.3) as an exfiltration channel; an asynchronously generated export artifact is a new health-data store with no stated controls | I | REST API; artifact storage | H | SEC-DATA-3 | GAP → SEC-DATA-6; conditional on ARCHITECTURE.md sync/async decision |
| TM-I-8 | Operator or support staff reads production health data directly; no rule constrained human access below the application | I | Boundary 5 | H | None previously | GAP → SEC-OPS-1; SQ-13 |
| TM-I-9 | Health data residue in browser storage, cache, or history on shared devices | I | Browser Client | M | SEC-SESSION-5, SEC-RENDER-4, SEC-HTTP-2 | MITIGATED BY RULE |
| TM-D-1 | Resource exhaustion on the public surface, amplified by expensive endpoints (export, history aggregation) | D | Boundary 1 | M | SEC-HTTP-5 | CONDITIONAL — limits undecided (SQ-3) |
| TM-D-2 | Targeted victim lockout: attacker triggers failed-auth lockout against a chosen account | D | Identity | M | None — lockout behavior itself creates the risk | CONDITIONAL — lockout design undecided (OQ-8, SQ-3); design MUST NOT allow third-party-triggered permanent lockout |
| TM-E-1 | Privilege escalation via role change or account-provisioning flows | E | Identity; REST API | H | SEC-INPUT-3 (request path) | CONDITIONAL — provisioning and role lifecycle UNKNOWN (SQ-12) |
| TM-E-2 | Authorization policy gap or fail-open evaluation grants unintended access | E | REST API | H | SEC-AUTHZ-5, SEC-AUTHZ-6, SEC-AUTHZ-7 | MITIGATED BY RULE — policy design still open (SQ-4) |
| TM-E-3 | Consultant capability creep: capabilities undefined, so scope of consultant write access cannot be bounded | E | REST API | M | SEC-AUTHZ-3 bounds *who*, not *what* | CONDITIONAL — REQUIREMENTS OQ-12 |
| TM-E-4 | Subscription entitlement bypass: whatever mechanism flips a subscription "active" is an unguarded target while undefined | E | REST API | M | SEC-AUTHZ-8 | CONDITIONAL — REQUIREMENTS OQ-1 |
| TM-P-1 | Identifiability: health data is linked to real identity by design; deletion may not de-identify backups and derived copies | L/I (LINDDUN) | Persistence | H | SEC-DATA-4 | CONDITIONAL — SQ-5 |
| TM-P-2 | Unawareness: consent is captured (FR-9.2) but no path existed to withdraw it short of account deletion | U (LINDDUN) | REST API | M | None previously | GAP → REQUIREMENTS FR-9.9 |
| TM-P-3 | Non-compliance: governing privacy regimes unresolved; no incident-response or breach-notification process defined | Nc (LINDDUN) | System-wide | H | — | CONDITIONAL — SQ-1, SQ-11 |
| TM-P-4 | The health-data audit trail is itself sensitive personal data with undefined retention and access control | I/Nc | Audit storage | M | SEC-LOG-5 | CONDITIONAL — SQ-8 |

**Resulting changes.** This model added: FR-9.9 and FR-10.2 plus OQ-15 and OQ-16 to REQUIREMENTS.md; trust boundaries 4 and 5 and traceability rows to ARCHITECTURE.md; and, in this document, rules SEC-AUTHN-8, SEC-DATA-6, SEC-LOG-6, SEC-LOG-7, SEC-OPS-1, open question SQ-13, and the rewrite of SQ-9. No previously documented statement was contradicted by the model; no conflict between the four source documents was found beyond the jurisdiction inconsistency already recorded as SQ-1.

### Provisional Security Rules

Rules marked **Confirmed** trace to an explicit statement in REQUIREMENTS.md, ARCHITECTURE.md, or the security notes. Rules marked **Provisional** are safe defaults for this profile and remain open to revision.

#### Trust Boundaries and Server-Side Enforcement

- **SEC-TB-1** (Confirmed) The REST API Application MUST re-derive every authorization, entitlement, ownership, and validation decision server-side, and MUST NOT accept any client-supplied identity, role, ownership, entitlement, or capability assertion as authoritative.
  - **Applies to:** Browser Client → REST API Application boundary; all operations
  - **Verification:** Integration tests replaying tampered client payloads (forged role, foreign owner ID, elevated capability) and asserting denial
  - **References:** `REF-ASVS-5`, `REF-API-2023`, `REF-PROMPT-API`
- **SEC-TB-2** (Confirmed) Relational Persistence MUST accept connections only from the REST API Application and Identity and Session Handling, and MUST NOT be reachable from the public network.
  - **Applies to:** REST API Application → Relational Persistence boundary
  - **Verification:** Network reachability test from outside the data tier; Terraform plan review of security groups and subnet placement
  - **References:** `REF-PROMPT-TF-AWS`, `REF-ASVS-5`
- **SEC-TB-3** (Confirmed) Health data MUST NOT be transmitted to any external service, including analytics, error-reporting, logging, or monitoring destinations outside the system boundary.
  - **Applies to:** All outbound paths; health data (FR-9.8)
  - **Verification:** Egress review of application and infrastructure configuration; test asserting no health field appears in any outbound payload
  - **References:** `REF-ASVS-5`, `REF-LOG`

#### Authentication

- **SEC-AUTHN-1** (Confirmed) All plan, customization, and progress operations MUST require an authenticated session; unauthenticated requests MUST be denied by default rather than allow-listed per endpoint.
  - **Applies to:** REST API Application; all non-public endpoints (FR-2.1)
  - **Verification:** Automated test enumerating every route unauthenticated and asserting denial; explicit review of any public route
  - **References:** `REF-ASVS-5`, `REF-AUTH`, `REF-PROMPT-API`
- **SEC-AUTHN-2** (Confirmed) `admin` and `consultant` accounts MUST authenticate with a passkey (WebAuthn), and MUST NOT be able to complete authentication with a password alone or fall back to a password-only path.
  - **Applies to:** Identity and Session Handling; privileged roles (FR-2.8, FR-2.9)
  - **Verification:** Test attempting password-only authentication for both privileged roles and asserting rejection, including on recovery paths
  - **References:** `REF-PASSKEY`, `REF-WEBAUTHN`, `REF-ASVS-5`
- **SEC-AUTHN-3** (Confirmed) Authentication failures MUST NOT reveal which factor was incorrect, and MUST NOT allow account existence to be inferred from response content, status, or timing.
  - **Applies to:** Identity and Session Handling; login, registration, recovery (FR-2.3)
  - **Verification:** Differential response and timing tests across known and unknown accounts
  - **References:** `REF-AUTH`, `REF-ASVS-5`
- **SEC-AUTHN-4** (Confirmed) When a subscriber has enabled MFA, a successful second factor MUST be required before any authenticated session is issued; a partially authenticated state MUST NOT grant access to any protected resource.
  - **Applies to:** Identity and Session Handling (FR-2.5, FR-2.6)
  - **Verification:** Test asserting that a first-factor-only context cannot call any protected endpoint
  - **References:** `REF-AUTH`, `REF-63B`, `REF-ASVS-5`
- **SEC-AUTHN-5** (Provisional) Passwords MUST be stored using a memory-hard password hashing function with per-credential salt; fast general-purpose hashes MUST NOT be used. Specific algorithm and parameters: TO BE DECIDED.
  - **Applies to:** Identity and Session Handling; credential storage
  - **Verification:** Code review of the credential storage path; test asserting stored values are not reversible digests of the input
  - **References:** `REF-PROMPT-NODE`, `REF-63B`, `REF-ASVS-5`
- **SEC-AUTHN-6** (Provisional) Authentication, MFA, passkey registration, and recovery endpoints MUST enforce anti-automation controls proportionate to credential-attack risk. Thresholds, lockout behavior, and recovery flows: TO BE DECIDED (REQUIREMENTS.md OQ-8, OQ-9; SQ-3).
  - **Applies to:** Identity and Session Handling
  - **Verification:** Burst-request test asserting throttled responses on each named endpoint
  - **References:** `REF-AUTH`, `REF-PROMPT-API`, `REF-ASVS-5`
- **SEC-AUTHN-7** (Provisional) Security-relevant account changes — password change, MFA enable/disable, passkey registration or replacement — MUST require re-authentication and MUST generate an audit entry.
  - **Applies to:** Identity and Session Handling (FR-2.5, FR-2.9)
  - **Verification:** Test asserting each change is refused without fresh authentication and produces an audit record
  - **References:** `REF-AUTH`, `REF-63B`, `REF-ASVS-5`

- **SEC-AUTHN-8** (Provisional) Control of a registered email address MUST be verified before the account can record health data or be relied upon in any account-recovery flow. Verification flow specifics (timing, token expiry, resend): TO BE DECIDED (REQUIREMENTS.md OQ-15).
  - **Applies to:** Identity and Session Handling; registration (threat TM-S-3)
  - **Verification:** Test attempting a health-data write on an account with an unverified email, asserting rejection
  - **References:** `REF-AUTH`, `REF-63B`, `REF-ASVS-5`

#### Session Management (JWT)

Applies because JWTs are explicitly selected in the security notes.

- **SEC-SESSION-1** (Confirmed) The server MUST verify token signatures before reading any claim, MUST enforce a server-side allow-list of accepted algorithms, and MUST reject `alg: none` and any algorithm outside that list.
  - **Applies to:** Identity and Session Handling; every authenticated request
  - **Verification:** Tests submitting `alg: none`, algorithm-confusion, and tampered-payload tokens and asserting rejection
  - **References:** `REF-PROMPT-JWT`, `REF-ASVS-5`
- **SEC-SESSION-2** (Confirmed) The server MUST validate `exp`, `iss`, and `aud` on every token and MUST reject tokens missing any required claim rather than applying a default.
  - **Applies to:** Identity and Session Handling
  - **Verification:** Tests per claim: absent, expired, and mismatched values all rejected
  - **References:** `REF-PROMPT-JWT`, `REF-SESSION`, `REF-ASVS-5`
- **SEC-SESSION-3** (Confirmed) Logout MUST render the session unusable for subsequent requests. Because a signed JWT is self-contained, a revocation mechanism MUST exist. Mechanism and token lifetimes: TO BE DECIDED (SQ-2).
  - **Applies to:** Identity and Session Handling (FR-2.4)
  - **Verification:** Test capturing a token, logging out, and asserting the captured token is refused
  - **References:** `REF-PROMPT-JWT`, `REF-SESSION`, `REF-ASVS-5`
- **SEC-SESSION-4** (Confirmed) Revocation of authorization state — role change, subscription lapse, or ended consultant engagement — MUST take effect for the affected actor without waiting for natural token expiry.
  - **Applies to:** REST API Application; Identity and Session Handling (FR-3.1, FR-11.3)
  - **Verification:** Test ending a consultant engagement and asserting the consultant's existing token no longer grants access to that subscriber's data
  - **References:** `REF-PROMPT-JWT`, `REF-PROMPT-ABAC`, `REF-ASVS-5`
- **SEC-SESSION-5** (Provisional) Tokens MUST NOT be stored in `localStorage` or `sessionStorage`, MUST NOT appear in URLs, query strings, or browser history, and MUST be transmitted only over TLS. Preferred storage is an `HttpOnly`, `Secure`, `SameSite` cookie; final transport decision is TO BE DECIDED and determines whether SEC-HTTP-4 applies.
  - **Applies to:** Browser Client; Browser Client → REST API Application boundary
  - **Verification:** Client code review plus runtime inspection of storage and request URLs
  - **References:** `REF-PROMPT-JWT`, `REF-PROMPT-VUE`, `REF-SESSION`
- **SEC-SESSION-6** (Confirmed) Token payloads MUST NOT contain health data, credentials, or sensitive personal data, since signed JWTs are not confidential.
  - **Applies to:** Identity and Session Handling
  - **Verification:** Decode issued tokens in tests and assert the claim set matches an approved allow-list
  - **References:** `REF-PROMPT-JWT`, `REF-ASVS-5`
- **SEC-SESSION-7** (Provisional) Token signing keys MUST be stored in a managed secret or key store, MUST support rotation via a key identifier, and MUST NOT appear in source, client bundles, container images, or Terraform state in plaintext. Specific key store, algorithm, and rotation period: TO BE DECIDED.
  - **Applies to:** Identity and Session Handling; deployment
  - **Verification:** Secret-scanning in CI; review that signing material resolves from the key store at runtime
  - **References:** `REF-PROMPT-JWT`, `REF-SECRETS`, `REF-PROMPT-TF-AWS`

#### Authorization (ABAC + Capabilities)

- **SEC-AUTHZ-1** (Confirmed) The REST API Application MUST verify that the authenticated actor is authorized for the requested operation and the specific target object before performing the operation, and MUST deny by default when no policy permits it.
  - **Applies to:** All protected read and state-changing operations (FR-9.1, FR-10.1)
  - **Verification:** Automated authorization tests over permitted and prohibited actor/object/operation combinations
  - **References:** `REF-ASVS-5`, `REF-API-2023`, `REF-PROMPT-ABAC`
- **SEC-AUTHZ-2** (Confirmed) Object-level authorization MUST be enforced on every operation that addresses a record by identifier. Queries MUST be constrained by the authorized owner or engagement scope rather than filtered after retrieval.
  - **Applies to:** User plan copies, workout/food/weight/measurement log entries, consent records (FR-7.4, FR-9.1)
  - **Verification:** BOLA/IDOR tests: authenticated subscriber A requesting subscriber B's object identifiers, asserting denial and no information disclosure
  - **References:** `REF-PROMPT-API`, `REF-API-2023`, `REF-ASVS-5`
- **SEC-AUTHZ-3** (Confirmed) Consultant access to a subscriber's plans or health data MUST be permitted only while an active engagement exists between that consultant and that subscriber, and MUST be denied immediately once the subscriber ends it.
  - **Applies to:** REST API Application; consultant role (FR-11.2, FR-11.3)
  - **Verification:** Tests covering no engagement, active engagement, and ended engagement; assert denial in the first and third
  - **References:** `REF-PROMPT-ABAC`, `REF-ASVS-5`
- **SEC-AUTHZ-4** (Confirmed) Plan authoring, editing, verification, publication, and unpublication MUST be restricted to `admin` accounts and denied to all others.
  - **Applies to:** REST API Application; plan library (FR-4.3, FR-10.1, FR-4.2)
  - **Verification:** Tests attempting each admin operation as subscriber and consultant, asserting denial
  - **References:** `REF-ASVS-5`, `REF-API-2023`
- **SEC-AUTHZ-5** (Confirmed) Authorization policy MUST be evaluated at a single enforcement point that all protected operations traverse; per-endpoint bespoke authorization logic MUST NOT be the primary control, and no protected operation may bypass the enforcement point.
  - **Applies to:** REST API Application (PEP/PDP separation)
  - **Verification:** Route inventory test asserting every protected route passes through the enforcement point
  - **References:** `REF-PROMPT-ABAC`, `REF-PC-2024`
- **SEC-AUTHZ-6** (Provisional) Every attribute used in an authorization decision MUST have a declared source and trust level. Attributes sourced from client input or unverified headers MUST NOT influence decisions. Attribute schema and policy language: TO BE DECIDED.
  - **Applies to:** Authorization policy inputs
  - **Verification:** Policy review against the attribute schema; test injecting attribute-shaped client input and asserting no decision change
  - **References:** `REF-PROMPT-ABAC`, `REF-ASVS-5`
- **SEC-AUTHZ-7** (Provisional) The policy combination algorithm MUST be deny-overrides, and a missing or unresolvable attribute MUST produce a denial rather than an error-open or permit.
  - **Applies to:** Authorization policy evaluation
  - **Verification:** Policy unit tests covering conflicting policies and absent attributes
  - **References:** `REF-PROMPT-ABAC`
- **SEC-AUTHZ-8** (Confirmed) Subscription entitlement MUST be enforced server-side as a condition of access to plans, customization, and progress tracking, and MUST be distinct from authentication. Lapsed entitlement MUST deny access while preserving the underlying records.
  - **Applies to:** REST API Application (FR-3.1, FR-3.2, FR-3.4)
  - **Verification:** Test transitioning a subscription to inactive, asserting denial plus intact records on reactivation
  - **References:** `REF-ASVS-5`, `REF-PROMPT-ABAC`

#### HTTP and REST API Boundary

- **SEC-HTTP-1** (Confirmed) All external HTTP traffic MUST use TLS. Plaintext HTTP MUST be rejected or redirected, and HSTS MUST be sent.
  - **Applies to:** Public browser-facing boundary
  - **Verification:** TLS configuration scan; test asserting plaintext requests are not served
  - **References:** `REF-REST`, `REF-ASVS-5`, `REF-PROMPT-API`
- **SEC-HTTP-2** (Provisional) Security response headers MUST be set on all responses, including a Content Security Policy that forbids inline and eval-based script execution, `X-Content-Type-Options: nosniff`, a restrictive referrer policy, and `Cache-Control: no-store` on responses containing health or personal data. Exact CSP directives: TO BE DECIDED.
  - **Applies to:** REST API Application responses; Browser Client rendering surface
  - **Verification:** Automated header assertions per response class; CSP violation reporting in a pre-production environment
  - **References:** `REF-PROMPT-VUE`, `REF-XSS`, `REF-PROMPT-NODE`
- **SEC-HTTP-3** (Provisional) Cross-origin access MUST NOT be enabled unless a documented cross-origin consumer exists. If enabled, allowed origins MUST be an explicit allow-list — never a wildcard, never origin reflection — and credentials MUST NOT be exposed to unlisted origins. Allowed origins: TO BE DECIDED.
  - **Applies to:** Public browser-facing boundary
  - **Verification:** Test asserting disallowed origins receive no permissive CORS headers
  - **References:** `REF-REST`, `REF-API-2023`
- **SEC-HTTP-4** (Conditional, Provisional) If session tokens are carried in cookies (ambient authority), state-changing requests MUST be protected against cross-site request forgery. If tokens are carried in an explicit `Authorization` header with no ambient credential, this rule does not apply. Applicability depends on SEC-SESSION-5.
  - **Applies to:** State-changing operations at the public boundary
  - **Verification:** Cross-origin state-change test asserting rejection without a valid anti-CSRF signal
  - **References:** `REF-SESSION`, `REF-ASVS-5`
- **SEC-HTTP-5** (Provisional) Request bodies MUST be size-limited, request handling MUST be time-bounded, and per-actor and per-endpoint rate limits MUST apply to authenticated operations. Specific limits: TO BE DECIDED (SQ-3).
  - **Applies to:** REST API Application
  - **Verification:** Oversized-payload and burst tests asserting rejection with a non-descriptive error
  - **References:** `REF-PROMPT-API`, `REF-PROMPT-NODE`, `REF-API-2023`
- **SEC-HTTP-6** (Provisional) Internal, debug, and diagnostic endpoints MUST NOT be exposed in production, and error responses MUST NOT vary in a way that discloses internal structure.
  - **Applies to:** REST API Application
  - **Verification:** Production route inventory review
  - **References:** `REF-PROMPT-API`, `REF-ERROR`

#### Input Validation and Business-Rule Validation

- **SEC-INPUT-1** (Confirmed) All untrusted input — request bodies, query parameters, path parameters, and headers — MUST be validated against an explicit allow-list schema at the REST API Application boundary, checking type, format, range, and length. Requests failing validation MUST be rejected, not coerced.
  - **Applies to:** Browser Client → REST API Application boundary
  - **Verification:** Schema-conformance tests plus fuzzing with malformed and out-of-range payloads
  - **References:** `REF-INPUT`, `REF-PROMPT-NODE`, `REF-PROMPT-API`, `REF-ASVS-5`
- **SEC-INPUT-2** (Confirmed) Log entries MUST be rejected when a required value is absent, non-numeric, or negative, and the response MUST identify the specific invalid field without disclosing internal state.
  - **Applies to:** Progress logging operations (FR-8.9)
  - **Verification:** Boundary tests per numeric field asserting rejection and correct field attribution
  - **References:** `REF-INPUT`, `REF-ASVS-5`
- **SEC-INPUT-3** (Confirmed) Write operations MUST bind only an explicit allow-list of client-assignable fields. Server-controlled fields — owner identity, role, subscription state, engagement state, publication status, verification record, audit fields — MUST NOT be settable from a request body.
  - **Applies to:** All create and update operations (FR-4.5, FR-7.2, FR-9.1)
  - **Verification:** Mass-assignment tests submitting privileged fields and asserting they are ignored
  - **References:** `REF-PROMPT-API`, `REF-API-2023`, `REF-ASVS-5`
- **SEC-INPUT-4** (Confirmed) Business rules MUST be enforced server-side as validation, not merely as UI affordance: a plan MUST NOT publish without at least one citation and an admin verification record; a customization MUST create a subscriber-owned copy without mutating the published plan; an existing copy MUST remain unchanged when its source plan is edited or unpublished.
  - **Applies to:** REST API Application (FR-4.4, FR-4.5, FR-7.2, FR-7.5)
  - **Verification:** Direct API tests bypassing the client for each rule, asserting rejection or non-mutation
  - **References:** `REF-PC-2024`, `REF-ASVS-5`
- **SEC-INPUT-5** (Confirmed) All database access MUST use parameterized queries or an equivalent mechanism that separates code from data; query text MUST NOT be assembled by concatenating untrusted input.
  - **Applies to:** REST API Application → Relational Persistence boundary
  - **Verification:** Static analysis for dynamic query construction; injection test suite over all input-bearing endpoints
  - **References:** `REF-PC-2024`, `REF-ASVS-5`
- **SEC-INPUT-6** (Provisional) Server-side JSON handling MUST neutralize prototype-polluting keys, and dynamic code evaluation over untrusted input MUST NOT be used.
  - **Applies to:** REST API Application (Node.js runtime)
  - **Verification:** Test submitting prototype-polluting payloads and asserting no global object mutation
  - **References:** `REF-PROMPT-NODE`

#### Output Encoding and Safe Rendering

- **SEC-RENDER-1** (Confirmed) The Browser Client MUST render all dynamic content through the framework's contextual auto-escaping. Raw HTML injection interfaces MUST NOT be used with server- or user-originated content, including plan content authored by admins.
  - **Applies to:** Browser Client; all rendered plan, citation, and log content
  - **Verification:** Lint rule forbidding raw HTML binding; stored-XSS test injecting markup through admin-authored plan fields and subscriber-entered fields
  - **References:** `REF-PROMPT-VUE`, `REF-XSS`, `REF-ASVS-5`
- **SEC-RENDER-2** (Confirmed) If rich-text plan content is ever required, it MUST be sanitized with a vetted HTML sanitizer before rendering, and custom sanitization MUST NOT be written. Whether rich text is needed at all: TO BE DECIDED.
  - **Applies to:** Browser Client; plan content
  - **Verification:** Test asserting known XSS vectors are neutralized by the sanitizer in the rendering path
  - **References:** `REF-PROMPT-VUE`, `REF-XSS`
- **SEC-RENDER-3** (Confirmed) URLs originating from data — notably plan citation links (FR-4.6) — MUST be parsed and scheme-checked before being bound to link or resource attributes; only explicitly permitted schemes may render, and script-bearing schemes MUST be rejected. External links MUST open without granting opener access to the application window.
  - **Applies to:** Browser Client; citation and any user- or admin-supplied URL
  - **Verification:** Test binding hostile scheme URLs and asserting they do not render as active links
  - **References:** `REF-PROMPT-VUE`, `REF-XSS`
- **SEC-RENDER-4** (Provisional) The Browser Client MUST NOT persist health data, personal data, or tokens in browser-local storage. Accessibility affordances required by DESIGN.md — error text, status announcements, focus management — MUST NOT expose data the actor is not authorized to see, and error text surfaced to assistive technology MUST follow SEC-ERR-1.
  - **Applies to:** Browser Client
  - **Verification:** Runtime storage inspection; review of error and status message content
  - **References:** `REF-PROMPT-VUE`, `REF-ERROR`

#### Data Protection and Privacy

- **SEC-DATA-1** (Confirmed) Health data MUST be encrypted in transit and at rest, including database storage, backups, and any snapshot or replica.
  - **Applies to:** Relational Persistence; all transport paths
  - **Verification:** Terraform review asserting encryption on storage, backup, and replica resources; TLS enforced on database connections
  - **References:** `REF-PROMPT-TF-AWS`, `REF-ASVS-5`
- **SEC-DATA-2** (Confirmed) The system MUST record explicit consent before any health data is collected, and MUST refuse to record health data absent that consent.
  - **Applies to:** REST API Application (FR-9.2)
  - **Verification:** Test attempting a log write without a consent record, asserting rejection
  - **References:** `REF-ASVS-5`
- **SEC-DATA-3** (Confirmed) Data export MUST return only the requesting actor's own data, MUST be authorized as a sensitive operation, and MUST NOT become a channel for reading another subscriber's records.
  - **Applies to:** REST API Application (FR-9.3)
  - **Verification:** Export tests as subscriber, consultant, and admin, asserting scope containment
  - **References:** `REF-API-2023`, `REF-ASVS-5`
- **SEC-DATA-4** (Confirmed) Account deletion MUST remove or irreversibly de-identify the user's personal and health data across primary storage, backups, and derived copies. Retention of audit entries required for accountability MUST be justified and MUST NOT retain health values. Deletion mechanics, backup handling, and completion deadline: TO BE DECIDED (REQUIREMENTS.md FR-9.4; SQ-5).
  - **Applies to:** Relational Persistence; REST API Application (FR-9.4)
  - **Verification:** Deletion test asserting no health record remains queryable through any interface
  - **References:** `REF-ASVS-5`
- **SEC-DATA-5** (Provisional) Health data MUST be collected and returned on a least-privilege basis: responses MUST return only fields the operation requires, and bulk retrieval of other subscribers' data MUST NOT be possible through any role.
  - **Applies to:** REST API Application responses
  - **Verification:** Response-shape assertions per endpoint; review for excessive data exposure
  - **References:** `REF-API-2023`, `REF-PROMPT-API`

- **SEC-DATA-6** (Conditional, Provisional) If data export (FR-9.3) or account deletion (FR-9.4) executes asynchronously, any generated export artifact is health data at rest: it MUST be encrypted, retrievable only by the requesting actor, automatically expired after a bounded lifetime, and covered by account deletion. Applicability depends on the synchronous-vs-deferred decision in ARCHITECTURE.md (threat TM-I-7).
  - **Applies to:** REST API Application; any artifact storage introduced for export
  - **Verification:** Test asserting a second actor cannot retrieve an export artifact and that expired artifacts are inaccessible
  - **References:** `REF-API-2023`, `REF-ASVS-5`

#### Operational Access

- **SEC-OPS-1** (Provisional) Human access to production health data below the application layer — direct database access, backup restoration, support tooling — MUST be denied by default, granted only through a documented break-glass process with per-use justification, time-bound credentials, and an audit record. Specific mechanism and approver model: TO BE DECIDED (SQ-13; threat TM-I-8).
  - **Applies to:** Operational/human-access boundary (ARCHITECTURE.md trust boundary 5)
  - **Verification:** Review of production access paths asserting no standing human credential can read health data; break-glass drill producing the expected audit trail
  - **References:** `REF-PROMPT-TF-AWS`, `REF-LOG`, `REF-ASVS-5`

#### Secrets and Keys

- **SEC-SECRET-1** (Confirmed) Secrets — token signing keys, database credentials, and any future integration credentials — MUST NOT appear in source control, client bundles, logs, error responses, or container images.
  - **Applies to:** All components; CI/CD
  - **Verification:** Secret scanning in CI over history and build artifacts; client bundle inspection
  - **References:** `REF-SECRETS`, `REF-PROMPT-NODE`, `REF-PROMPT-VUE`
- **SEC-SECRET-2** (Provisional) Secrets MUST be resolved at runtime from a managed secret store and MUST support rotation without code change. Specific secret-management service: TO BE DECIDED (SQ-7).
  - **Applies to:** REST API Application; Identity and Session Handling; deployment
  - **Verification:** Configuration review asserting no secret is supplied as a plaintext committed value
  - **References:** `REF-SECRETS`, `REF-PROMPT-TF-AWS`
- **SEC-SECRET-3** (Confirmed) Terraform state MUST be treated as sensitive: encrypted, access-restricted, never publicly readable, and never committed to source control.
  - **Applies to:** Deployment
  - **Verification:** Review of state backend configuration and access policy
  - **References:** `REF-PROMPT-TF-AWS`, `REF-IAC`
- **SEC-SECRET-4** (Confirmed) All security-relevant randomness — tokens, identifiers used as capabilities, recovery values — MUST come from a cryptographically secure generator.
  - **Applies to:** REST API Application; Identity and Session Handling
  - **Verification:** Code review of every generation site
  - **References:** `REF-PROMPT-NODE`, `REF-ASVS-5`

#### Logging, Audit, and Error Handling

- **SEC-LOG-1** (Confirmed) Every access to, and modification of, a user's health data MUST produce an audit entry recording the acting account, the action, the affected subject, and the time — including consultant access.
  - **Applies to:** REST API Application (FR-9.7, FR-11.4)
  - **Verification:** Test asserting each health-data read and write path emits exactly one audit entry with the required fields
  - **References:** `REF-LOG`, `REF-ASVS-5`
- **SEC-LOG-2** (Confirmed) Audit entries MUST be append-only from the application's perspective; no role, including `admin`, may edit or delete them through the application.
  - **Applies to:** REST API Application; Relational Persistence
  - **Verification:** Test attempting audit mutation via every role and interface, asserting denial
  - **References:** `REF-LOG`, `REF-ASVS-5`
- **SEC-LOG-3** (Confirmed) Logs MUST NOT contain health values, credentials, tokens, or full personal records. Audit entries reference the data accessed; they do not copy it.
  - **Applies to:** All logging surfaces
  - **Verification:** Log-content assertions in tests; redaction configuration review
  - **References:** `REF-LOG`, `REF-PROMPT-NODE`, `REF-ASVS-5`
- **SEC-LOG-4** (Confirmed) Authentication successes and failures, authorization denials, and security-relevant account changes MUST be logged with enough context to detect attack patterns, without logging the credentials involved.
  - **Applies to:** Identity and Session Handling; REST API Application
  - **Verification:** Test asserting each event type produces a structured log record
  - **References:** `REF-LOG`, `REF-ASVS-5`
- **SEC-ERR-1** (Confirmed) Error responses MUST NOT expose stack traces, framework or database details, or internal identifiers. Responses carry a generic message plus a correlation identifier; full diagnostics remain server-side.
  - **Applies to:** REST API Application; Browser Client presentation
  - **Verification:** Fault-injection tests asserting response bodies contain no internal detail while the server log retains it
  - **References:** `REF-ERROR`, `REF-PROMPT-NODE`, `REF-PROMPT-API`
- **SEC-LOG-5** (Provisional) Log and audit retention periods, storage location, and access controls: TO BE DECIDED (SQ-8). Retention MUST be defined before production, since audit entries are themselves sensitive.
  - **Applies to:** Logging and audit storage
  - **Verification:** Documented retention policy exists and is enforced by configuration
  - **References:** `REF-LOG`
- **SEC-LOG-6** (Confirmed) Every admin plan lifecycle action — create, edit, verify, publish, unpublish — MUST produce an audit entry recording the acting admin, the action, the plan, and the time.
  - **Applies to:** REST API Application (FR-10.2; threats TM-R-1, TM-T-5)
  - **Verification:** Test asserting each admin plan operation emits exactly one audit entry with the required fields
  - **References:** `REF-LOG`, `REF-ASVS-5`
- **SEC-LOG-7** (Provisional) Audit storage MUST be tamper-evident against actors below the application layer, including holders of database or backup credentials; SEC-LOG-2 binds only the application. Mechanism (write-once storage, integrity chaining, or segregated log account): TO BE DECIDED (SQ-8, SQ-13; threat TM-R-2).
  - **Applies to:** Relational Persistence; audit storage; operational-access boundary
  - **Verification:** Attempted out-of-band modification of an audit record is detectable in review
  - **References:** `REF-LOG`, `REF-PROMPT-TF-AWS`

#### External Integrations

- **SEC-EXT-1** (Confirmed) No external integration currently exists. Any future integration MUST be introduced behind an internally defined interface owned by the REST API Application, MUST NOT propagate vendor-specific behavior into business logic, and MUST NOT carry health data across the boundary (FR-9.8) without an explicit documented change to REQUIREMENTS.md.
  - **Applies to:** Future external boundaries
  - **Verification:** Architecture review at the time any integration is proposed
  - **References:** `REF-ASVS-5`, `REF-PC-2024`
- **SEC-EXT-2** (Confirmed) Server-side requests to URLs derived from user or admin input — including citation URLs — MUST NOT be issued without an explicit allow-list. Citation URLs are rendered as links, never fetched server-side, unless a documented decision says otherwise.
  - **Applies to:** REST API Application (FR-4.4, FR-4.6)
  - **Verification:** Test asserting internal-network URLs supplied as citations are never requested by the server
  - **References:** `REF-ASVS-5`, `REF-PC-2024`

#### CI/CD, Deployment, and Infrastructure

- **SEC-CICD-1** (Provisional) Build and deployment identities MUST follow least privilege, MUST use short-lived federated credentials rather than long-lived static keys, and MUST be scoped per environment. CI/CD platform: UNKNOWN (SQ-7).
  - **Applies to:** Deployment pipeline
  - **Verification:** Review of pipeline identity configuration and IAM policy scope
  - **References:** `REF-CICD`, `REF-SSDF`, `REF-PROMPT-TF-AWS`
- **SEC-CICD-2** (Confirmed) Infrastructure MUST be defined as code in Terraform and MUST be reviewed before apply; manual changes to production infrastructure MUST NOT bypass that review.
  - **Applies to:** Deployment (AWS)
  - **Verification:** Drift detection; change-history review
  - **References:** `REF-IAC`, `REF-PROMPT-TF-AWS`
- **SEC-CICD-3** (Provisional) IAM policies MUST avoid wildcard actions and resources; the data tier MUST reside in private network segments with no direct public ingress; storage MUST block public access by default.
  - **Applies to:** AWS infrastructure
  - **Verification:** Automated IaC policy scanning in the pipeline
  - **References:** `REF-PROMPT-TF-AWS`, `REF-IAC`
- **SEC-CICD-4** (Provisional) Security-relevant automated checks — dependency vulnerability scanning, secret scanning, IaC scanning, and the authorization test suite — MUST run in CI and MUST block merge on failure.
  - **Applies to:** CI pipeline
  - **Verification:** Pipeline configuration review; deliberate failing-case test
  - **References:** `REF-SSDF`, `REF-CICD`, `REF-DEPS`
- **SEC-CICD-5** (Provisional) Non-production environments MUST NOT contain real subscriber health data.
  - **Applies to:** Environment management
  - **Verification:** Data-provenance review of non-production datasets
  - **References:** `REF-SSDF`

### Requirement and Architecture Traceability

| Rule(s) | Requirements protected | Architecture component / boundary | Status |
|---|---|---|---|
| SEC-TB-1 | FR-2.1, FR-9.1, FR-10.1 | Browser Client → REST API Application | CONFIRMED |
| SEC-TB-2 | FR-9.1, FR-9.8 | REST API Application → Relational Persistence | CONFIRMED |
| SEC-TB-3, SEC-EXT-1 | FR-9.8 | System boundary (no external integration) | CONFIRMED |
| SEC-AUTHN-1 | FR-2.1 | REST API Application; Identity and Session Handling | CONFIRMED |
| SEC-AUTHN-2 | FR-2.8, FR-2.9 | Identity and Session Handling | CONFIRMED |
| SEC-AUTHN-3 | FR-2.3 | Identity and Session Handling | CONFIRMED |
| SEC-AUTHN-4 | FR-2.5, FR-2.6 | Identity and Session Handling | CONFIRMED |
| SEC-AUTHN-5 | FR-2.2, FR-2.3 | Identity and Session Handling | PROVISIONAL — algorithm and parameters undecided |
| SEC-AUTHN-6 | FR-2.3 | Identity and Session Handling | PARTIALLY DEFINED — thresholds and recovery flows undecided (OQ-8, OQ-9) |
| SEC-AUTHN-7 | FR-2.5, FR-2.9 | Identity and Session Handling | PROVISIONAL |
| SEC-SESSION-1, SEC-SESSION-2, SEC-SESSION-6 | FR-2.1, FR-2.3 | Identity and Session Handling | CONFIRMED |
| SEC-SESSION-3 | FR-2.4 | Identity and Session Handling | PARTIALLY DEFINED — revocation mechanism undecided (SQ-2) |
| SEC-SESSION-4 | FR-3.1, FR-11.3 | Identity and Session Handling; REST API Application | CONFIRMED |
| SEC-SESSION-5 | FR-2.4 | Browser Client | PROVISIONAL — token transport undecided |
| SEC-SESSION-7 | FR-2.1 | Identity and Session Handling; deployment | PROVISIONAL — key store undecided |
| SEC-AUTHZ-1, SEC-AUTHZ-2 | FR-7.4, FR-9.1 | REST API Application | CONFIRMED |
| SEC-AUTHZ-3 | FR-11.2, FR-11.3, FR-11.4 | REST API Application | CONFIRMED |
| SEC-AUTHZ-4 | FR-4.2, FR-4.3, FR-10.1 | REST API Application | CONFIRMED |
| SEC-AUTHZ-5 | FR-9.1, FR-10.1 | REST API Application | PROVISIONAL — enforcement-point design undecided |
| SEC-AUTHZ-6, SEC-AUTHZ-7 | FR-9.1, FR-11.2 | REST API Application | PROVISIONAL — attribute schema and policy language undecided |
| SEC-AUTHZ-8 | FR-3.1, FR-3.2, FR-3.4 | REST API Application | PARTIALLY DEFINED — subscription activation unspecified (REQUIREMENTS.md OQ-1) |
| SEC-HTTP-1 | FR-1.1, FR-9.8 | Public browser-facing boundary | CONFIRMED |
| SEC-HTTP-2 | FR-1.1, FR-1.2 | Browser Client; REST API Application | PROVISIONAL — CSP directives undecided |
| SEC-HTTP-3 | — | Public browser-facing boundary | TO BE DECIDED — no cross-origin consumer documented |
| SEC-HTTP-4 | FR-2.1 | Public browser-facing boundary | TO BE DECIDED — conditional on token transport (SEC-SESSION-5) |
| SEC-HTTP-5 | FR-2.3, FR-8.x | REST API Application | PROVISIONAL — limits undecided (SQ-3) |
| SEC-HTTP-6 | — | REST API Application | PROVISIONAL |
| SEC-INPUT-1 | FR-8.9 and all write paths | Browser Client → REST API Application | CONFIRMED |
| SEC-INPUT-2 | FR-8.9 | REST API Application | CONFIRMED |
| SEC-INPUT-3 | FR-4.5, FR-7.2, FR-9.1 | REST API Application | CONFIRMED |
| SEC-INPUT-4 | FR-4.4, FR-4.5, FR-7.2, FR-7.5 | REST API Application | CONFIRMED |
| SEC-INPUT-5 | FR-9.1 | REST API Application → Relational Persistence | CONFIRMED |
| SEC-INPUT-6 | — | REST API Application | PROVISIONAL |
| SEC-RENDER-1 | FR-4.6, FR-5.1, FR-6.1, FR-8.6 | Browser Client | CONFIRMED |
| SEC-RENDER-2 | FR-4.6 | Browser Client | TO BE DECIDED — rich-text requirement unknown |
| SEC-RENDER-3 | FR-4.6 | Browser Client | CONFIRMED |
| SEC-RENDER-4 | FR-9.1; DESIGN.md accessibility targets | Browser Client | PROVISIONAL |
| SEC-DATA-1 | FR-9.8 and all health data | Relational Persistence; transport | CONFIRMED |
| SEC-DATA-2 | FR-9.2 | REST API Application | CONFIRMED |
| SEC-DATA-3 | FR-9.3, FR-9.1 | REST API Application | CONFIRMED |
| SEC-DATA-4 | FR-9.4 | Relational Persistence; REST API Application | PARTIALLY DEFINED — mechanics and deadline undecided (SQ-5) |
| SEC-DATA-5 | FR-9.1 | REST API Application | PROVISIONAL |
| SEC-SECRET-1, SEC-SECRET-4 | FR-2.1 | All components | CONFIRMED |
| SEC-SECRET-2 | FR-2.1 | Deployment | PROVISIONAL — secret store undecided (SQ-7) |
| SEC-SECRET-3 | — | Deployment (Terraform) | CONFIRMED |
| SEC-LOG-1 | FR-9.7, FR-11.4 | REST API Application | CONFIRMED |
| SEC-LOG-2 | FR-9.7 | REST API Application; Relational Persistence | CONFIRMED |
| SEC-LOG-3 | FR-9.7, FR-9.8 | All logging surfaces | CONFIRMED |
| SEC-LOG-4 | FR-2.3 | Identity and Session Handling | CONFIRMED |
| SEC-LOG-5 | FR-9.7 | Logging and audit storage | TO BE DECIDED — retention undefined (SQ-8) |
| SEC-ERR-1 | FR-8.9; DESIGN.md error presentation | REST API Application; Browser Client | CONFIRMED |
| SEC-EXT-2 | FR-4.4, FR-4.6 | REST API Application | CONFIRMED |
| SEC-CICD-1 | — | Deployment pipeline | PARTIALLY DEFINED — CI/CD platform unknown (SQ-7) |
| SEC-CICD-2 | — | Deployment (Terraform on AWS) | CONFIRMED |
| SEC-CICD-3 | FR-9.1, FR-9.8 | AWS infrastructure | PROVISIONAL |
| SEC-CICD-4 | — | CI pipeline | PROVISIONAL |
| SEC-CICD-5 | FR-9.1, FR-9.8 | Environment management | PROVISIONAL |
| SEC-AUTHN-8 | FR-2.2, FR-9.1 | Identity and Session Handling | PROVISIONAL — verification flow undecided (REQUIREMENTS.md OQ-15) |
| SEC-DATA-6 | FR-9.3, FR-9.4 | REST API Application; artifact storage | TO BE DECIDED — conditional on sync/async export decision (ARCHITECTURE.md) |
| SEC-LOG-6 | FR-10.2 | REST API Application | CONFIRMED |
| SEC-LOG-7 | FR-9.7 | Relational Persistence; audit storage | PROVISIONAL — mechanism undecided (SQ-8, SQ-13) |
| SEC-OPS-1 | FR-9.1, FR-9.8 | Operational-access boundary (5) | PROVISIONAL — access model undecided (SQ-13) |
| DEP-1 … DEP-8 | — | All components | PROVISIONAL — no implementation and no dependencies exist yet |

### Dependency Security Rules

- **DEP-1** The project MUST NOT add a dependency when the standard library or a small amount of straightforward, non-security-sensitive first-party code is safer and sufficient. The project MUST NOT replace vetted cryptography, authentication, authorization, protocol parsing, output encoding, HTML sanitization, or other security-critical functionality with custom code merely to avoid a dependency.
- **DEP-2** The project SHOULD prefer zero new dependencies. Every new dependency MUST be justified in the pull request description, including its purpose and why existing code or platform functionality is insufficient.
- **DEP-3** A new dependency MUST show evidence of active maintenance through a stable release, security response, or substantive maintainer activity within the previous 12 months. A mature project with less frequent releases requires an explicit documented exception and evidence that security reports are still handled.
- **DEP-4** The project MUST use the latest stable release from the latest actively supported major version unless a documented compatibility constraint requires another actively supported major version. Deprecated, abandoned, end-of-life, or pre-release packages MUST NOT be introduced into production.
- **DEP-5** Before a dependency is added or updated, direct and transitive dependencies MUST be checked for known vulnerabilities. A dependency with a known unpatched vulnerability applicable to the intended use MUST NOT be introduced without explicit, time-bounded risk acceptance, documented compensating controls, and a remediation plan.
- **DEP-6** Dependency review MUST include the complete transitive dependency graph. A small direct dependency with a disproportionately large, opaque, abandoned, or unvetted transitive tree SHOULD be rejected.
- **DEP-7** Production builds MUST resolve dependencies to exact versions through a committed lockfile or equivalent ecosystem mechanism. Production and CI builds MUST use frozen or reproducible dependency resolution and MUST NOT resolve floating versions at build or deployment time.
- **DEP-8** When multiple suitable libraries exist, the project SHOULD prefer the library with the narrowest required scope, smallest dependency tree, active security response process, clear provenance, and established security track record.

Applicable sources: `REF-SUPPLY`, `REF-DEPS`, `REF-SSDF`, `REF-PROMPT-NODE`, `REF-PROMPT-VUE`. No dependency has been assessed; no implementation exists.

### Prompt Placeholders To Resolve

| Placeholder | Status | Resolution |
|---|---|---|
| `{{CODE_QUALITY_PROMPT}}` | RESOLVED | `REF-PROMPT-QUALITY` — `/Users/jmanico/Dropbox/github/platform/context/prompts/code security/Code Quality/00 General Code Quality Prompts/PROMPT.md`, read and applied. Project-specific intent: security-critical operations (authentication, authorization policy evaluation, validation, encoding) isolated into single-purpose, descriptively named functions that are independently reviewable and testable; guard clauses and early returns in access-control paths so no nested condition produces an ambiguous authorization state; fail-closed semantics — an exception inside authorization logic denies (reinforces SEC-AUTHZ-7); silent exception swallowing in authN/authZ paths treated as a security defect; validation centralized rather than repeated per endpoint (SEC-AUTHZ-5, SEC-INPUT-1); immutable representation of roles, capabilities, and session attributes to avoid time-of-check-to-time-of-use gaps; presentation, business-rule, persistence, and integration concerns kept separate per ARCHITECTURE.md DR-2 and DR-4; named constants for security-relevant thresholds; testability without hidden global state. |
| `{{API_SECURITY_PROMPT}}` | RESOLVED | An API boundary exists and the style is REST (ARCHITECTURE.md). Applied: `REF-API-2023`, `REF-REST`, and `REF-PROMPT-API`. Public/external exposure of that REST surface remains TO BE DECIDED (SQ-6); rules here assume a first-party browser client only. |
| `{{BACKEND_FRAMEWORK_PROMPT}}` | RESOLVED | `REF-PROMPT-NODE` — `/Users/jmanico/Dropbox/github/platform/context/prompts/code security/Backend Frameworks/NodeJS/00 Secure Node.js Developer/PROMPT.md`, read and applied. The specific Node.js server framework is TO BE DECIDED, so framework-specific sub-prompts were not selected. |
| `{{FRONTEND_FRAMEWORK_PROMPT}}` | RESOLVED | `REF-PROMPT-VUE` — `/Users/jmanico/Dropbox/github/platform/context/prompts/code security/Client Side Frameworks/VueJS/00 Secure VueJS Developer/PROMPT.md`, read and applied. |
| `{{AUTH_PROMPT}}` | PARTIALLY RESOLVED | Mechanisms are identified, so mechanism-specific guidance applies: passkeys for privileged roles (`REF-PASSKEY`, `REF-WEBAUTHN`), passwords plus optional MFA for subscribers (`REF-AUTH`, `REF-63B`), JWT sessions (`REF-PROMPT-JWT`, `REF-SESSION`). Unresolved and therefore not specified: password policy, MFA factors, token lifetimes, revocation mechanism, and account/MFA recovery (SQ-2, SQ-3, REQUIREMENTS.md OQ-8, OQ-9). |
| `{{DEPLOYMENT_PROMPT}}` | PARTIALLY RESOLVED | `REF-SSDF` and `REF-CICD` always apply. Terraform and AWS are explicitly selected in ARCHITECTURE.md and the security notes, so `REF-PROMPT-TF-AWS` and `REF-IAC` apply. CI/CD platform, container/orchestrator usage, and specific AWS services are UNKNOWN — platform-specific guidance TO BE DECIDED (SQ-7). |

### Open Security Questions

- **SQ-1** Which privacy regimes actually govern this system? The security notes say US federal and state law; REQUIREMENTS.md asserts GDPR and CCPA rights plus HIPAA obligations and sets scale to "global". These are materially different control sets (HIPAA presupposes a covered-entity relationship that a direct-to-consumer fitness app usually lacks; GDPR presupposes EU data subjects). Until resolved, jurisdiction-specific obligations beyond the behaviors in FR-9.x remain TO BE DECIDED, and data-residency requirements cannot be set.
- **SQ-2** What is the full JWT session model — access token lifetime, refresh strategy, transport (cookie vs. header), and the revocation mechanism that makes logout (FR-2.4) and engagement termination (FR-11.3) effective? This determines whether CSRF defenses apply (SEC-HTTP-4) and whether SEC-SESSION-3 and SEC-SESSION-4 are satisfiable. The security notes fix the token format but not the model; ARCHITECTURE.md left it undecided.
- **SQ-3** What abuse-prevention thresholds apply — rate limits, lockout behavior, and anti-automation on authentication, export, and logging endpoints? No limits may be invented, and ASVS Level 3 will require them to be defined.
- **SQ-4** What is the concrete ABAC attribute schema, policy language, and enforcement architecture, and how do capabilities relate to the three fixed roles? The notes select ABAC plus capability-based access control, but REQUIREMENTS.md describes role- and ownership-based rules; the mapping between them is undefined, and consultant capabilities themselves are unspecified (REQUIREMENTS.md OQ-12).
- **SQ-5** What are the deletion mechanics for FR-9.4 — hard delete vs. de-identification, treatment of backups and replicas, what survives in audit entries, and the completion deadline?
- **SQ-6** Is the REST surface ever exposed to third-party consumers, or is it strictly a private backend for the first-party Vue client? This changes the API threat surface, versioning obligations, and CORS posture.
- **SQ-7** What are the CI/CD platform, secret-management service, and AWS service topology? Least-privilege deployment identities, secret resolution, and IaC scanning cannot be specified concretely without them.
- **SQ-8** What retention periods and access controls apply to audit entries and security logs? Audit records of health-data access are themselves sensitive, and retention interacts directly with SQ-1 and SQ-5.
- **SQ-9** The initial document-based threat model was produced 2026-07-31 (see Threat Model section) — single-perspective and pre-implementation. Who owns it, its refresh cadence, and its cross-functional validation (product, legal/privacy, operations) are TO BE DECIDED. It MUST be revisited when SQ-1, SQ-2, SQ-4, and SQ-7 resolve, and re-run against the repository once implementation exists, before any ASVS Level 3 conformance claim.
- **SQ-10** Is ASVS Level 3 the right target, and who verifies it? Level 3 is intended for the highest-risk applications and carries substantial verification cost. No conformance claim is made here, and no gap assessment against ASVS 5.0.0 has been performed.
- **SQ-11** What is the incident response and breach-notification process, including who is notified and within what window if health data is exposed? This is unaddressed by all input documents and is likely required by whichever regime SQ-1 resolves to.
- **SQ-12** How are `admin` and `consultant` accounts provisioned, vetted, and deprovisioned? Both hold elevated access to subscriber health data, and REQUIREMENTS.md OQ-13 leaves consultant onboarding open. The threat model adds: how is the *first* passkey for a privileged account enrolled, and how are role changes authorized (TM-S-4, TM-E-1)?
- **SQ-13** What is the operational human-access model for production health data — who can reach the database, backups, and logs below the application layer, under what break-glass process, and with what audit? No input document addressed access below the application (TM-I-8, TM-R-2; SEC-OPS-1, SEC-LOG-7).
