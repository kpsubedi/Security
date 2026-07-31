Create or replace `SECURITY.md` in the repository root. `SECURITY.md` should own the security
posture: threat model, security requirements, controls, trust-boundary enforcement.
Read in order: `REQUIREMENTS.md`, `DESIGN.md`, `ARCHITECTURE.md`, then the security notes below.
`REQUIREMENTS.md` is the source of truth for behavior, actors, workflows, data, integrations,
and privacy/regulatory constraints; `ARCHITECTURE.md` for components, trust boundaries, data
flows, external interfaces, and dependency direction; `DESIGN.md` for browser-facing behavior,
rendering surfaces, user input, and frontend interaction. Assume no implementation exists; do
not infer frameworks, auth mechanisms, databases, providers, CI/CD systems, or regulatory
obligations from nonexistent code. Do not ask clarifying questions.
Marker convention: use `UNKNOWN` for facts the input documents do not provide; use `TO BE
DECIDED` for decisions not yet made; label every unsupported inference `ASSUMPTION`. Never
invent values or present provisional defaults as confirmed requirements.
Security notes may add constraints but MUST NOT silently override `REQUIREMENTS.md` or
`ARCHITECTURE.md`; record material conflicts under `## Open Security Questions`.
## Security Notes
<<SECURITY_NOTES_OR_NONE>>
## Security Reference Selection
If a secure-coding prompt library exists in the execution environment: read only the prompt
files relevant to the identified architecture and stack, record the exact path and purpose of
each, never claim a prompt was imported unless actually located and read, and convert prompts
into concise project-specific rules rather than copying them. Otherwise use the applicable
references below.
### Authoritative Public Defaults
Select only those relevant:- OWASP ASVS 5.0.0: `https://github.com/OWASP/ASVS/releases/tag/v5.0.0_release`- OWASP Top 10 Proactive Controls 2024: `https://top10proactive.owasp.org/archive/2024/the-top
10/`- OWASP Cheat Sheet Series: `https://cheatsheetseries.owasp.org/`- OWASP API Security Top 10 2023: `https://owasp.org/API-Security/editions/2023/en/0x11-t10/`- OWASP REST Security Cheat Sheet:
`https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html`- OWASP Authentication Cheat Sheet:
`https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html`- OWASP Session Management Cheat Sheet:
`https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html`- OWASP XSS Prevention Cheat Sheet:
`https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
- OWASP Input Validation Cheat Sheet:
`https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html`- OWASP Secrets Management Cheat Sheet:
`https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html`- OWASP Logging Cheat Sheet:
`https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html`- OWASP Error Handling Cheat Sheet:
`https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html`- NIST SSDF 1.1: `https://csrc.nist.gov/pubs/sp/800/218/final`- OWASP CI/CD Security Cheat Sheet:
`https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html`- OWASP Software Supply Chain Security Cheat Sheet:
`https://cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html`- OWASP Infrastructure as Code Security Cheat Sheet:
`https://cheatsheetseries.owasp.org/cheatsheets/Infrastructure_as_Code_Security_Cheat_Sheet.html
`- OWASP Vulnerable Dependency Management Cheat Sheet:
`https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.htm
l`- NIST SP 800-63B-4 (when authentication assurance or authenticator lifecycle is relevant):
`https://pages.nist.gov/800-63-4/sp800-63b.html`- Only if passkeys are explicitly selected (never merely because the auth model is UNKNOWN):
FIDO Alliance Passkeys `https://fidoalliance.org/passkeys/` and W3C Web Authentication
`https://www.w3.org/TR/webauthn/`
### Reference Accuracy Rules- Record exact title, version, and URL or local path for every selected source; prefer version
pinned over mutable "latest" pages.- Never state a source was read if it could not be accessed; never invent titles, URLs,
guidance, or prompt files.- Never guess ASVS requirement identifiers. Use an identifier only if verified against ASVS
5.0.0, written in versioned form (`v5.0.0-1.2.5`); otherwise reference ASVS 5.0.0 generally.- Cite the most specific source actually used, not a general index.- Synthesize short project-specific rules; do not copy source material verbatim.
## Output
Output only the Markdown content of `SECURITY.md`, with exactly these sections:
### Required Security Inputs
Each field exactly once, derived from the input documents and security notes (`UNKNOWN` if
absent). Do not assume GDPR, HIPAA, PCI DSS, SOC 2, or any other compliance regime merely
because personal or sensitive data may exist; if jurisdiction is UNKNOWN, mark the obligation
`TO BE DECIDED` and add an open security question.- Requirements source: REQUIREMENTS.md- Design source: DESIGN.md- Architecture source: ARCHITECTURE.md- System purpose:- Application profile:- Users / actors / roles:- Public interfaces and trust boundaries
- Sensitive or regulated data:- External integrations:- Authentication model:- Authorization model:- Session model:- Deployment and CI/CD model:- Applicable privacy or regulatory obligations:- Security assurance target: TO BE DECIDED- Security verification reference: OWASP ASVS 5.0.0- Threat model status: TO BE DECIDED
If `ARCHITECTURE.md` identifies a web application but leaves the client/server integration model
unresolved: prioritize browser and HTTP boundary security, treat API style and exposure as `TO
BE DECIDED`, and do not invent a separately consumable public API.
### Selected Security References and Prompt Imports
List only sources and prompt files actually selected and used (inaccessible sources go under
placeholders instead). Stable IDs such as `REF-ASVS-5`, `REF-PC-2024`, `REF-API-2023`, `REF
REST`, `REF-AUTH`, `REF-SESSION`, `REF-XSS`, `REF-SSDF`, `REF-CICD`; exact paths for local
prompt files.
### Provisional Security Rules
A compact, project-specific rule set derived from the requirements, roles, workflows, data,
architecture boundaries, frontend behavior, integrations, and selected references. Rules MUST:- Be grouped by security capability with stable IDs (`SEC-HTTP-1`, `SEC-AUTHN-1`, `SEC-AUTHZ-1`,
`SEC-DATA-1`).- Use MUST / MUST NOT / SHOULD / MAY; one independently verifiable behavior per rule.- Identify the protected boundary, actor, operation, or data when known.- Distinguish confirmed requirements from provisional defaults; apply the marker convention.- Reference applicable `REF-*` IDs and include a concise verification method.- Trace to `REQUIREMENTS.md` and `ARCHITECTURE.md`.
Format:- **SEC-AUTHZ-1** The server-side application MUST verify that the authenticated actor is
authorized for the requested operation and target object before performing the operation.- **Applies to:** Protected state-changing operations- **Verification:** Automated authorization tests using permitted and prohibited actor/object
combinations- **References:** `REF-ASVS-5`, `REF-API-2023`
Include only categories relevant to the project (candidates: trust boundaries and server-side
enforcement, authentication, session management, authorization, HTTP/API boundaries, input
validation, business-rule validation, output encoding and safe rendering, data protection and
privacy, secrets and keys, logging and error handling, external integrations, CI/CD and
deployment, dependency and supply-chain security).
Apply safe durable defaults where the application profile supports them: server-side
authorization enforcement with deny-by-default; validation of untrusted data (format and
business meaning) at the trust boundary where it enters; context-appropriate output encoding and
no raw HTML/DOM injection interfaces; secrets kept out of source, client code, logs, and errors;
non-sensitive error responses with server-side diagnostics retained; TLS for external HTTP;
east privilege for service and deployment identities; no sensitive data in security or
diagnostic logs.
Express mechanism-dependent controls conditionally: CSRF defenses only when ambient authority
(cookie auth) applies; CORS only when cross-origin access is required; token-specific controls
only when bearer tokens/JWTs are selected; REST guidance only when the style is REST;
passkey/WebAuthn guidance only when passkeys are explicitly selected; IaC guidance only when
infrastructure is code-managed; cloud-provider guidance only when a provider is identified.
Do not invent: authentication factors, token formats, password rules, session timeouts,
cryptographic algorithms, rate limits, data- or log-retention periods, exact CSP directives,
allowed CORS origins, cloud services, secret-management or scanning products, or compliance
obligations. Mark each `TO BE DECIDED`.
### Requirement and Architecture Traceability
Map each security rule to the requirements and boundaries it protects, using exact requirement
IDs from `REQUIREMENTS.md` and exact component names from `ARCHITECTURE.md`. Status values:
`CONFIRMED`, `PROVISIONAL`, `PARTIALLY DEFINED`, `TO BE DECIDED`. A rule not yet mappable to a
documented requirement or boundary is `TO BE DECIDED`.
### Dependency Security Rules
Include these rules verbatim, referencing the applicable supply-chain sources selected earlier.
They are prospective rules for future implementation; do not claim any dependency has been
assessed when none exists.- **DEP-1** The project MUST NOT add a dependency when the standard library or a small amount of
straightforward, non-security-sensitive first-party code is safer and sufficient. The project
MUST NOT replace vetted cryptography, authentication, authorization, protocol parsing, output
encoding, HTML sanitization, or other security-critical functionality with custom code merely to
avoid a dependency.- **DEP-2** The project SHOULD prefer zero new dependencies. Every new dependency MUST be
justified in the pull request description, including its purpose and why existing code or
platform functionality is insufficient.- **DEP-3** A new dependency MUST show evidence of active maintenance through a stable release,
security response, or substantive maintainer activity within the previous 12 months. A mature
project with less frequent releases requires an explicit documented exception and evidence that
security reports are still handled.- **DEP-4** The project MUST use the latest stable release from the latest actively supported
major version unless a documented compatibility constraint requires another actively supported
major version. Deprecated, abandoned, end-of-life, or pre-release packages MUST NOT be
introduced into production.- **DEP-5** Before a dependency is added or updated, direct and transitive dependencies MUST be
checked for known vulnerabilities. A dependency with a known unpatched vulnerability applicable
to the intended use MUST NOT be introduced without explicit, time-bounded risk acceptance,
documented compensating controls, and a remediation plan.- **DEP-6** Dependency review MUST include the complete transitive dependency graph. A small
direct dependency with a disproportionately large, opaque, abandoned, or unvetted transitive
tree SHOULD be rejected.- **DEP-7** Production builds MUST resolve dependencies to exact versions through a committed
lockfile or equivalent ecosystem mechanism. Production and CI builds MUST use frozen or
reproducible dependency resolution and MUST NOT resolve floating versions at build or deployment
time.- **DEP-8** When multiple suitable libraries exist, the project SHOULD prefer the library with
the narrowest required scope, smallest dependency tree, active security response process, clear
provenance, and established security track record.
### Prompt Placeholders To Resolve
Include each placeholder exactly once. Status values: `RESOLVED`, `PARTIALLY RESOLVED`, `TO BE
DECIDED`, `NOT APPLICABLE`.- `{{CODE_QUALITY_PROMPT}}` — use a local code-quality prompt if actually found; otherwise
resolve to: low cyclomatic and cognitive complexity; small cohesive functions and modules;
separated presentation, business-rule, persistence, and integration concerns; explicit error
handling and trust-boundary transitions; no duplicated security-sensitive logic; testability
without hidden global state.- `{{API_SECURITY_PROMPT}}` — if an API exists: OWASP API Security Top 10 2023, plus the REST
cheat sheet only if the style is REST, or style-specific guidance for GraphQL/gRPC/WebSocket.
API exposure or style unresolved: `PARTIALLY RESOLVED` or `TO BE DECIDED`. No API boundary: `NOT
APPLICABLE`.- `{{BACKEND_FRAMEWORK_PROMPT}}` — resolve only when the backend framework and version are
explicitly identified, preferring in order: an applicable local prompt actually read, the
framework's official version-appropriate security documentation, an applicable OWASP framework
cheat sheet. Framework UNKNOWN: `TO BE DECIDED`. Never invent a framework or URL.- `{{FRONTEND_FRAMEWORK_PROMPT}}` — same resolution order for the frontend framework. For any
browser-rendered UI the XSS Prevention Cheat Sheet MAY serve as a framework-neutral rendering
baseline, but it does not resolve this placeholder. Framework UNKNOWN: `TO BE DECIDED`.- `{{AUTH_PROMPT}}` — if the auth and session model is identified: mechanism-specific standards
plus OWASP Authentication/Session Management guidance and NIST SP 800-63B-4 where assurance or
lifecycle guidance applies; add FIDO Passkeys and W3C WebAuthn only if passkeys are explicitly
selected. If the mechanism is UNKNOWN: choose no mechanism (no passwords, passkeys, OAuth, OIDC,
SAML, JWTs, or cookie sessions), mark `TO BE DECIDED`; general authentication references MAY
remain as provisional background.- `{{DEPLOYMENT_PROMPT}}` — always NIST SSDF 1.1 and the OWASP CI/CD Security Cheat Sheet, then
only guidance applicable to the documented deployment model (platform/provider, IaC, container,
orchestrator, CI-system-specific). Deployment model UNKNOWN: `PARTIALLY RESOLVED` with provider
specific guidance `TO BE DECIDED`. Never assume Terraform unless explicitly selected.
### Open Security Questions
Only unresolved questions that materially affect security behavior, architecture,
implementation, verification, or compliance, and that the input documents do not answer. Stable
IDs: `SQ-1`, `SQ-2`, ... Candidate topics: authentication and account recovery, authorization
policy and role boundaries, sensitive-data classification, privacy jurisdiction, session/token
model, public vs private API exposure, abuse prevention and resource limits, external
integration trust, secret storage, deployment and CI/CD platforms, assurance level,
logging/audit/retention obligations, incident response.
## Constraints
No invented features, architecture, frameworks, or vendors; no generic security essays, attack
tutorials, or exploit payloads; no file inventories, directory summaries, or implementation
code; no unsupported compliance claims, claims of ASVS conformance, or guessed ASVS identifiers;
no copied prompts or long quotations; no controls unrelated to the documented system. Keep the
document compact, concrete, testable, traceable, and optimized for AI context loading.
