# Requirement Template - Web & API Applications

Use one copy of this template for each atomic requirement.

Replace bracketed placeholders when authoring a requirement. Use `N/A` only when a field has been evaluated and is not applicable. Use `TO BE DECIDED` when the answer is unresolved.

Uppercase normative terms use BCP 14 semantics as defined by RFC 2119 and RFC 8174. Prefer `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY`. Split compound behavior into separate requirements.

## Metadata

- **ID**: [REQ-MODULE-###, e.g., REQ-AUTH-001]
- **Title**: [Concise requirement name]
- **Version**: [Semantic version, e.g., 1.0.0]
- **Status**: [Draft | In Review | Approved | Implemented | Verified | Deprecated]
- **Owner**: [Person or team responsible for the requirement]
- **Author**: [Name]
- **Last Updated**: [ISO 8601 date: YYYY-MM-DD]
- **Priority**: [Critical | High | Medium | Low]
- **Requirement Type**: [Functional | Security | Privacy | Compliance | Performance | Reliability | Operational]
- **Source / Parent**: [Source requirement IDs, stakeholder decision, threat-model decision, legal obligation, issue, or other origin]

## Requirement

- **Statement**: [One atomic, unambiguous, and independently testable statement describing what the system MUST, MUST NOT, SHOULD, SHOULD NOT, or MAY do.]
- **Rationale**: [Business, user, regulatory, architectural, privacy, or threat-driven reason for the requirement. Do not introduce additional required behavior here.]
- **Assumptions**: [Assumptions on which the requirement depends, or `None`.]
- **Out of Scope**: [Behavior that is explicitly excluded from this requirement, or `None`.]
- **Design Traceability**: [Relevant `DESIGN.md` section or decision, or `N/A`. Do not invent missing design decisions.]
- **Architecture Traceability**: [Relevant `ARCHITECTURE.md` component, boundary, data flow, or dependency rule.]
- **Security Traceability**: [Relevant `SECURITY.md` rule IDs, or `N/A`.]

## Scope

- **Applies To**: [Web Client | Server-Side Application | API | Background Processing | External Integration | Multiple]
- **Components**: [Affected logical components using the names defined in `ARCHITECTURE.md`]
- **Interfaces / Operations**: [Affected pages, workflows, API operations, events, or commands]
- **Actors**: [Affected users, roles, service identities, administrators, or external systems]
- **Preconditions**: [State that MUST exist before the behavior occurs, or `None`]
- **Data Classification**: [Public | Internal | Confidential | Restricted | Multiple | N/A]
- **Personal or Regulated Data**: [None | Personal Data | Sensitive Personal Data | Payment Account Data | Health Data | Financial Data | Other]
- **Jurisdiction / Regulatory Scope**: [Established jurisdiction or regulatory scope, `N/A`, or `TO BE DECIDED`]

## Security Context

- **Security Objectives**: [Confidentiality | Integrity | Availability | Authenticity | Authorization | Accountability | Privacy | Safety | Multiple | N/A]
- **Control Layers**: [Architecture | Authentication | Authorization | Session Management | Input Validation | Business-Rule Validation | Output Encoding | Sanitization | Data Protection | Logging and Monitoring | Availability | Supply Chain | Other]
- **Threat References**: [Versioned threat references such as CWE, CAPEC, STRIDE, or an OWASP Top 10:2025 category; use `N/A` when no threat mapping applies]
- **Abuse / Misuse Case**: [What an attacker, unauthorized actor, or compromised dependency may attempt, or `N/A`]
- **Trust Boundary**: [Boundary at which untrusted data, identity assertions, commands, or responses enter a more trusted component]
- **Untrusted Inputs or Assertions**: [Inputs, identity claims, authorization context, external responses, files, events, or other data that MUST NOT be trusted without verification]
- **Authoritative Enforcement Point**: [Server-side component or other trusted boundary responsible for enforcing the requirement]
- **Independent Verification**: [Validation or authorization performed independently of the originating client, actor, or external system]
- **Zero Trust Relevance**: [Specific NIST SP 800-207 resource-access principle or section, or `N/A`. Do not use Zero Trust as a synonym for input validation.]

## Standards Alignment

Only include mappings verified against the cited version of the standard. Do not guess control identifiers.

Use `N/A` when a standard has been evaluated and does not apply. Use `TO BE DECIDED` when applicability or mapping has not yet been assessed.

- **OWASP ASVS 5.0.0**: [Versioned requirement ID, e.g., `v5.0.0-1.2.5`, or `N/A`]
- **OWASP AISVS 1.0**: [Requirement ID when an AI-enabled component is involved, or `N/A`]
- **NIST SP 800-53 Rev. 5**: [Control or control-enhancement ID and the catalog release used, or `N/A`]
- **NIST SP 800-207**: [Specific Zero Trust tenet or section when applicable, or `N/A`]
- **Regulatory**: [Applicable regulation, exact version or effective date, and specific requirement or section; otherwise `N/A` or `TO BE DECIDED`]
- **Other**: [Versioned RFC, ISO/IEC standard, industry standard, or organizational policy and exact section, or `N/A`]
- **Mapping Basis**: [Brief explanation of why each listed mapping applies]

## Acceptance Criteria

Each acceptance criterion MUST:

- describe one observable pass/fail outcome
- be independently testable
- remain within the behavior defined by the requirement
- identify relevant preconditions, action, and expected result
- avoid introducing new product behavior

Use Given/When/Then or an equally explicit pass/fail form.

1. **AC-01 — Expected behavior**: Given [valid preconditions], when [actor or system action], then [observable expected result].
2. **AC-02 — Boundary or failure behavior**: Given [boundary condition, invalid input, unauthorized action, or dependency failure], when [action occurs], then [safe and observable result with no unauthorized state change or sensitive side effect].
3. **AC-03 — Prohibited behavior**: Given [relevant preconditions], when [action occurs], then [behavior or outcome that MUST NOT occur].
4. **AC-04 — Additional criterion**: [Add only when needed. Remove when not applicable.]

## Failure Behavior

- **On Invalid Input**: [Protocol-appropriate rejection behavior, error classification, and confirmation that no protected state change or sensitive side effect occurs]
- **On Authentication Failure**: [Expected response and disclosure behavior, or `N/A`]
- **On Authorization Failure**: [Deny the operation; define response behavior and whether resource existence may be disclosed, or `N/A`]
- **On Security-Decision Failure**: [Deny by default unless an explicit, documented risk decision permits another behavior]
- **On External Dependency Failure**: [Timeout, retry, circuit-breaker, idempotency, or degradation behavior, or `N/A`]
- **On System Error**: [Rollback, consistency, recovery, and safe error-response behavior; internal state and sensitive data MUST NOT be disclosed]
- **Logging / Audit**: [Events and fields to record, correlation mechanism, redaction requirements, and prohibited data]
- **Alerting**: [Alert condition, threshold, severity, and destination, or `N/A`]

## Test Strategy

- **Unit Tests**: [Business rules, validation rules, authorization decisions, transformations, and error paths testable in isolation]
- **Integration Tests**: [Cross-component, persistence, identity, external integration, or trust-boundary behavior]
- **Security Tests**: [Applicable negative tests, abuse cases, authorization tests, fuzzing classes, SAST rules, DAST targets, or manual review items]
- **Compliance Tests / Evidence**: [Automated or manual evidence required for an applicable obligation, or `N/A`]
- **Acceptance-Criteria Traceability**: [Test identifier or test suite covering each `AC-*` criterion]
- **Coverage Target**: [Project-defined target. All security-critical decisions and error paths MUST include positive and negative test coverage.]
- **Required Test Environment**: [Fixtures, identities, roles, dependency simulators, configuration, or test data required]

## Dependencies

- **Upstream Requirements**: [Requirement IDs that MUST be satisfied first, or `None`]
- **Downstream Requirements**: [Requirement IDs that depend on this requirement, or `None`]
- **External Dependencies**: [Third-party services, identity providers, APIs, cryptographic services, hardware services, or `None`]
- **Dependency Assumptions**: [Security, availability, data-integrity, or contractual assumptions made about external dependencies]
- **Failure Impact**: [Effect of an unavailable, compromised, slow, or malformed dependency response]

## Implementation Notes

- **Constraints**: [Mandatory technology, compatibility, latency, availability, migration, legal, or deadline constraints]
- **Prohibited Approaches**: [Explicit anti-patterns, such as relying solely on client-side enforcement or logging credentials, tokens, or sensitive raw data]
- **Implementation Guidance**: [Non-normative guidance that does not add or alter required behavior]
- **AI Development Guidance**: [Applicable prompt-library files, repository instructions, secure-coding rules, and mandatory human-review gates, or `N/A`]
- **Required Human Review**: [Security, privacy, architecture, legal, product, or domain reviewers required before approval or release]
- **Open Decisions**: [Unresolved decisions that prevent approval or implementation, or `None`]
