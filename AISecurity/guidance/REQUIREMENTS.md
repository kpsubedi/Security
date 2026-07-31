# Required Requirement Inputs

- **Project purpose:** A fitness web application that delivers science-based, admin-curated exercise and diet plans, lets users customize those plans, and tracks their progress over time. Access requires a paid subscription.
- **Primary users / actors:** Subscriber (registered end user who follows plans and logs progress); Fitness consultant / helper (available to subscribers as a paid option); Admin (authors, cites, verifies, and publishes plan content)
- **Core workflows:** Register and authenticate; subscribe; browse and select an exercise or diet plan; customize a plan into a personal copy; log workouts, food intake, weight, and measurements; view progress over time; admin authors and verifies plans
- **Business objects / data entities:** User account; subscription; exercise plan (with cited sources); diet plan (meals, calorie/macro targets, cited sources); user plan copy (customized); workout log entry; food log entry; body weight entry; body measurement entry
- **External integrations:** None — the system is self-contained
- **Authentication / roles:** Account required. Subscribers authenticate with standard consumer authentication: email + password minimum, with optional user-enabled MFA. Admins and fitness consultants MUST authenticate with a passkey. Roles: subscriber, consultant, admin
- **Regulatory or privacy constraints:** US health-related laws apply to user health data, including HIPAA obligations; GDPR and CCPA data-subject rights apply; a medical disclaimer stating the content is not medical advice must be shown

# Functional Requirements

### Delivery Channel

- **FR-1.1** The system MUST be delivered as a web application accessible through current desktop and mobile web browsers.
- **FR-1.2** The system MUST present a usable, responsive layout at both desktop and mobile viewport sizes, with no loss of function or content on mobile.

### Accounts and Authentication

- **FR-2.1** The system MUST require a user account for all plan, customization, and progress functionality, and MUST deny unauthenticated access to those functions.
- **FR-2.2** The system MUST allow a user to register an account with an email address and a password.
- **FR-2.3** The system MUST allow a registered user to authenticate with email and password, and MUST reject invalid credentials without revealing which factor was wrong.
- **FR-2.4** The system MUST allow a user to end their session (log out).
- **FR-2.5** The system MUST allow a user to enable and disable multi-factor authentication on their own account. MFA MUST be optional, not required.
- **FR-2.6** When MFA is enabled for an account, the system MUST require a successful second factor before granting an authenticated session.
- **FR-2.7** The system MUST assign every account exactly one of the roles `subscriber`, `consultant`, or `admin`.
- **FR-2.8** The system MUST require passkey authentication for accounts with the `admin` or `consultant` role, and MUST NOT allow those accounts to authenticate with a password alone.
- **FR-2.9** The system MUST allow an `admin` or `consultant` account to register a passkey and to register a replacement passkey.

### Subscription and Access Control

- **FR-3.1** The system MUST require an active subscription for a subscriber to access exercise plans, diet plans, customization, and progress tracking.
- **FR-3.2** The system MUST deny plan and progress-tracking access to authenticated users without an active subscription, and MUST tell them a subscription is required.
- **FR-3.3** The system MUST allow a user to view their current subscription status.
- **FR-3.4** The system MUST retain a user's existing progress records and plan customizations when their subscription lapses, and MUST restore access to them when the subscription becomes active again.

### Plan Library and Content Verification

- **FR-4.1** The system MUST provide a library of exercise plans and diet plans authored by admins.
- **FR-4.2** The system MUST NOT allow subscribers to author plans, submit plans for publication, or share plans with other users.
- **FR-4.3** The system MUST allow an admin to create, edit, publish, and unpublish plans.
- **FR-4.4** The system MUST require every plan to carry at least one citation to a peer-reviewed source before it can be published, and MUST block publication of a plan with no citation.
- **FR-4.5** The system MUST require explicit admin verification of a plan before publication, and MUST record which admin verified it and when.
- **FR-4.6** The system MUST display a plan's citations to the user when the plan is viewed.
- **FR-4.7** The system MUST show only published plans to subscribers.

### Exercise Plans

- **FR-5.1** The system MUST allow a subscriber to browse published exercise plans and view a plan's full contents, including its exercises and prescribed sets and repetitions.
- **FR-5.2** The system MUST allow a subscriber to select an exercise plan to follow.

### Diet Plans

- **FR-6.1** The system MUST allow a subscriber to browse published diet plans and view a plan's full contents.
- **FR-6.2** Each diet plan MUST specify its meals and its daily calorie and macronutrient targets.
- **FR-6.3** The system MUST allow a subscriber to select a diet plan to follow.

### Plan Customization

- **FR-7.1** The system MUST allow a subscriber to customize a published exercise or diet plan by editing its contents.
- **FR-7.2** The system MUST save a customization as a private copy owned by that subscriber, and MUST NOT modify the published plan.
- **FR-7.3** The system MUST persist a subscriber's customized plans across sessions and MUST make them retrievable by that subscriber.
- **FR-7.4** The system MUST NOT allow a subscriber to view or modify another subscriber's customized plans.
- **FR-7.5** The system MUST preserve an existing customized copy unchanged when the published plan it was derived from is later edited or unpublished.

### Progress Tracking

- **FR-8.1** The system MUST allow a subscriber to log a body weight entry with a date.
- **FR-8.2** The system MUST allow a subscriber to log body measurement entries with a date. The specific measurement fields are TO BE DECIDED.
- **FR-8.3** The system MUST allow a subscriber to record completion of a workout from their plan, including sets, repetitions, and weight used per exercise.
- **FR-8.4** The system MUST allow a subscriber to log food intake and MUST attribute calories and macronutrients to each logged entry.
- **FR-8.5** The system MUST display logged calories and macronutrients for a given day against the targets of the subscriber's selected diet plan.
- **FR-8.6** The system MUST display a subscriber's logged history over time for body weight, body measurements, and workout performance.
- **FR-8.7** The system MUST allow a subscriber to edit and delete their own log entries.
- **FR-8.8** The system MUST allow a subscriber to log entries for a past date, not only the current date.
- **FR-8.9** The system MUST reject log entries with a non-numeric, negative, or absent required value and MUST report the specific invalid field to the user.

### Data Rights, Privacy, and Safety

- **FR-9.1** The system MUST scope every plan copy and log entry to its owning subscriber, and MUST NOT expose one subscriber's data to another subscriber.
- **FR-9.2** The system MUST obtain the user's explicit consent to collect and process their health data before any health data is recorded.
- **FR-9.3** The system MUST allow a user to export all of their own account, plan, and progress data in a machine-readable form.
- **FR-9.4** The system MUST allow a user to request deletion of their account and all associated personal and health data, and MUST complete the deletion. The completion deadline is TO BE DECIDED.
- **FR-9.5** The system MUST allow a user to view and correct the personal data held about them.
- **FR-9.6** The system MUST display a disclaimer stating that the plans and content are not medical advice, and MUST require the user to acknowledge it before they first use a plan.
- **FR-9.7** The system MUST record an audit entry for each access to or modification of a user's health data, capturing the acting account, the action, and the time.
- **FR-9.8** The system MUST NOT transmit user health data to any external service.
- **FR-9.9** The system MUST allow a user to withdraw their previously given consent to health-data collection, and MUST NOT record new health data for that user while consent is withdrawn. Existing records remain subject to FR-9.3–FR-9.5. *(Threat-model-derived: SECURITY.md TM-P-2.)*

### Fitness Consultants

- **FR-11.1** The system MUST offer subscribers access to a fitness consultant / helper as a paid option in addition to the base subscription.
- **FR-11.2** The system MUST NOT grant a consultant access to a subscriber's plans or health data unless that subscriber has an active paid consultant engagement with them.
- **FR-11.3** The system MUST allow a subscriber to end a consultant engagement, after which the system MUST revoke that consultant's access to the subscriber's data.
- **FR-11.4** The system MUST record an audit entry for each consultant access to a subscriber's health data, per FR-9.7.

### Administration

- **FR-10.1** The system MUST restrict plan authoring, verification, publication, and unpublication to accounts with the `admin` role, and MUST deny those actions to subscribers.
- **FR-10.2** The system MUST record an audit entry for every admin plan lifecycle action — create, edit, verify, publish, unpublish — capturing the acting admin, the action, the affected plan, and the time. *(Threat-model-derived: SECURITY.md TM-R-1, TM-T-5.)*

# Open Questions

- **OQ-1** Subscription-only access was chosen, but no payments integration is in scope and the system is specified as self-contained. How are subscriptions purchased, renewed, and cancelled, and what makes a subscription "active"? Without this, FR-3.1–FR-3.3 cannot be fully tested.
- **OQ-2** Is there a trial period, promotional access, or a free tier of any kind?
- **OQ-3** Which US health-related laws are in scope beyond HIPAA (e.g. state health-privacy laws, FTC Health Breach Notification Rule)? HIPAA itself binds only covered entities and their business associates — what is the covering relationship here, and does it require a BAA, breach-notification workflow, or access controls beyond FR-9.7?
- **OQ-4** Which body measurement fields must be supported (waist, chest, arms, hips, body-fat %), and are units configurable (metric vs. imperial)?
- **OQ-5** Food logging requires nutrition data, but no external nutrition database is in scope. Do subscribers enter calories and macros manually, or does the system ship its own food catalog, and who maintains it?
- **OQ-6** Can a subscriber follow more than one exercise plan and one diet plan at a time, or is it one active plan of each type?
- **OQ-7** What time period and granularity must progress history cover (per day, per week, all-time), and are charts required or is a list sufficient?
- **OQ-8** What password policy, account-recovery, and MFA-recovery flows apply? MFA is optional, but lockout behavior on lost second factor is unspecified.
- **OQ-9** Which MFA factors must be supported (authenticator app, SMS, email code, passkey)?
- **OQ-10** Is admin verification of a plan a one-time gate, or must a plan be re-verified after each edit?
- **OQ-11** Are accessibility conformance targets (e.g. WCAG 2.1 AA) in scope? None were selected.
- **OQ-12** What can a fitness consultant actually do — view a subscriber's plans and logs, edit their plans, message them, or something else? FR-11.x currently only bounds their access, not their capabilities.
- **OQ-13** How are consultants onboarded and vetted, are they platform staff or third parties, and how is the paid consultant option purchased (the same payments gap as OQ-1)?
- **OQ-14** Is offline use required for logging entries without a connection? Not selected, so assumed out of scope.
- **OQ-15** *(Threat-model-derived: SECURITY.md TM-S-3.)* What is the email-verification flow at registration — when verification occurs, token expiry, and resend behavior? SECURITY.md SEC-AUTHN-8 requires that control of the registered email be verified before health data is recorded or the address is used in recovery; the product flow is undecided.
- **OQ-16** *(Threat-model-derived: SECURITY.md TM-T-5.)* Should plan verification (FR-4.5) require an admin other than the plan's author (dual control)? A single compromised admin account can currently author, verify, and publish harmful exercise or diet content alone.
