# CLAUDE.md

Canonical agent instructions for this repository.

## Specifications

These are normative. Read them before proposing or writing anything, and follow them directly rather than re-deriving their content.

@REQUIREMENTS.md
@ARCHITECTURE.md
@SECURITY.md
@DESIGN.md

`REQUIREMENT_TEMPLATE.md` is not imported — it is the authoring format for new requirements (see Issues below).

## Repository state

No application code exists. The repository contains specifications only. Anything about how the system is built, tested, deployed, or run is unwritten, not undiscovered.

- **Language, package manager, build tooling:** TO BE DECIDED
- **Node.js server framework:** TO BE DECIDED (ARCHITECTURE.md fixes Node.js; the framework within it is open)
- **RDBMS engine and migration tooling:** TO BE DECIDED
- **Test framework and runner commands:** TO BE DECIDED
- **Lint and format tooling:** TO BE DECIDED
- **CI platform and pipeline:** TO BE DECIDED (SECURITY.md SQ-7)
- **Local development and run instructions:** TO BE DECIDED
- **Directory layout:** TO BE DECIDED

Do not invent, assume, or silently pick any of the above. When work requires one, state that it is undecided and ask. When one is decided, replace the placeholder here in the same change that introduces it.

## Working rules

- **Specs precede code.** A behavior that is not in REQUIREMENTS.md, ARCHITECTURE.md, SECURITY.md, or DESIGN.md is not agreed. Propose a spec change first; do not encode an unspecified behavior in code and call it settled.
- **Do not resolve open questions unilaterally.** REQUIREMENTS.md OQ-*, DESIGN.md OQ-*, SECURITY.md SQ-*, and every `TO BE DECIDED` / `UNKNOWN` marker are open. Surface them; let the user decide. Never quietly close one by writing code that depends on one answer.
- **Preserve the markers.** `TO BE DECIDED` and `UNKNOWN` are deliberate. Do not replace either with a plausible-sounding value.
- **Trace every change.** Any non-trivial implementation change must name the requirement, architecture, security, and design identifiers it satisfies. If nothing traces, the change is out of scope.
- **Report gaps rather than closing them.** If a requested change cannot be made without deciding something open, do the parts that are unblocked, and say explicitly what was left and which open item blocks it.

## GitHub issues

Every new GitHub issue MUST follow `REQUIREMENT_TEMPLATE.md`, so that each issue is a structured, testable requirement — metadata, atomic normative statement, scope, security context, standards alignment, acceptance criteria, failure behavior, test strategy, dependencies, and implementation notes.

- Use `N/A` only for a field evaluated and found inapplicable; use `TO BE DECIDED` for one that is unresolved. Never leave a bracketed placeholder in a filed issue.
- Split compound behavior across separate issues. One issue is one atomic requirement.
- Do not invent standards mappings or control identifiers. An unverified mapping is `TO BE DECIDED`.

## Branch and change workflow

- Default branch is `main`. History to date is squash-merged pull requests.
- Do not commit or push unless asked. If asked while on `main`, branch first.
- Everything else about the workflow — branch naming, PR template, required reviewers, merge strategy, release process: TO BE DECIDED.
