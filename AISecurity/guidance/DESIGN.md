# DESIGN.md

## Required Design Inputs

- **Brand personality:** TO BE DECIDED
- **Primary audience:** Subscribers (registered end users who follow admin-curated exercise and diet plans and log workouts, food intake, weight, and measurements). Secondary audiences: fitness consultants / helpers engaged by subscribers as a paid option, and admins who author, cite, verify, and publish plan content.
- **Platform targets (web / mobile / both):** Web application, responsive across desktop and mobile browsers (REQUIREMENTS.md FR-1.1, FR-1.2). No native mobile app is in scope.
- **Light / dark mode:** TO BE DECIDED
- **Existing brand assets:** UNKNOWN

## Brand and Logo

**Product name:** UNKNOWN — REQUIREMENTS.md never names the product. The mark is therefore abstract and carries no wordmark or initial. A wordmark and lockup are **TO BE DECIDED** once the name exists; the mark below is designed to sit beside one later.

**Brand direction:** TO BE DECIDED. What the requirements do support, and what the mark reflects, is a product that is evidence-led (every plan carries verified peer-reviewed citations) and progress-oriented (logging and viewing change over time). The visual treatment is accordingly plain and clinical rather than motivational or high-energy — no expressive personality is asserted beyond what the requirements justify.

**Logo concept:** three ascending rounded bars inside a rounded square, with a separate dot above the tallest bar. The bars represent logged progress over time; the detached dot represents the plan's target the subscriber is working toward. It is geometric and abstract — no human figure, equipment, food, mascot, or medical imagery.

**Usage:**
- **Clear space:** on all sides, at least 25% of the mark's width (16px at the 64px default). Nothing else may enter that space.
- **Minimum display size:** 24×24px. The mark is drawn at a 64px reference size and holds at 24px; below that, bar separation degrades.
- **Backgrounds:** designed for light backgrounds (`background`, `surface`). The rounded square supplies its own contrast, so it may also be placed on mid-tone backgrounds. Placement on dark backgrounds is TO BE DECIDED with dark mode.
- **Incorrect usage:** do not recolor the mark outside the documented palette; do not stretch or scale it non-uniformly; do not rotate it; do not remove the rounded square and use the bars alone; do not add effects (shadow, glow, gradient, outline); do not place it on a busy photographic background; do not set it against a background that reduces contrast below 3:1.

## Color Palette

Restrained palette: one brand color, one accent used sparingly, and semantic colors for feedback. All contrast ratios below are against `background` (`#FFFFFF`) and against `surface` (`#F6F7F8`), both of which are near-white; every listed value meets or exceeds WCAG 2.2 AA for body text (4.5:1).

| Token | Hex | Role | Contrast on `#FFFFFF` |
|---|---|---|---|
| `primary` | `#0F766E` | Brand color; primary actions, active states, links | 5.40:1 |
| `secondary` | `#B45309` | Sparingly used accent for secondary emphasis | 5.02:1 |
| `background` | `#FFFFFF` | Page background | — |
| `surface` | `#F6F7F8` | Cards, panels, raised regions on the page background | — |
| `text` | `#14181A` | Body and heading text | 17.4:1 |
| `error` | `#B3261E` | Validation failures, destructive confirmation, error messages | 4.99:1 |
| `success` | `#1B6B3A` | Successful save, completed workout, confirmed action | 5.06:1 |

Rules:
- `text` on `background` and on `surface` is the only combination used for body copy.
- `primary`, `secondary`, `error`, and `success` are AA-safe as text on `background` and `surface`, and AA-safe as backgrounds under white text.
- Color is never the sole carrier of meaning — see Accessibility.
- Additional tints/shades are TO BE DECIDED; do not introduce new hues without extending this table.

**Colors used in `logo.svg`:**
- `#0F766E` — rounded square (`primary`)
- `#FFFFFF` — the three bars (`background`); 5.40:1 against the square
- `#5EEAD4` — goal dot; a light tint of `primary`, decorative only and never used for text

## Typography

Brand typography is **UNKNOWN**; the broader typographic direction is **TO BE DECIDED**. Until then, use the platform system font stack — it ships with every target browser, so it costs no download, renders natively at all sizes, and carries no licensing question.

- **Primary:** system UI stack — `system-ui`, then `-apple-system`, `Segoe UI`, `Roboto`, `Helvetica Neue`, `Arial`.
- **Fallback:** `sans-serif`.
- **Numeric data** (weights, measurements, sets/reps, calories, macros): render with tabular/lining figures so logged values align in columns and comparisons down a list read cleanly.

Type scale (1.25 ratio, 16px base):

| Step | Size | Typical use |
|---|---|---|
| xs | 12px | Metadata, citation attribution, timestamps |
| sm | 14px | Secondary text, helper text, table cells |
| base | 16px | Body copy; minimum for sustained reading |
| lg | 20px | Card and section titles |
| xl | 25px | Page titles |
| 2xl | 31px | Primary page heading |

- **Weights:** 400 (body), 500 (emphasis, labels, buttons), 700 (headings). No other weights.
- **Line height:** 1.5 for body, 1.25 for headings.
- Body text is never below 16px. Text is never justified.

## Layout and Spacing

- **Spacing scale (4px base):** 4, 8, 12, 16, 24, 32, 48, 64. Use only these steps for margin, padding, and gaps.
- **Grid:** 12-column fluid grid on desktop, 4-column on mobile, with a 24px gutter (16px below the `md` breakpoint).
- **Content width:** max 1200px for application pages; max 72ch for long-form reading (plan descriptions, citations, the medical disclaimer).
- **Breakpoints:** `sm` 480px, `md` 768px, `lg` 1024px, `xl` 1280px. Single-column below `md`; multi-column at `md` and above.
- **Touch targets:** minimum 44×44px on all interactive elements at every breakpoint.
- Mobile layouts reflow rather than truncate — no function or content is dropped at small widths (FR-1.2).

## Components

**Buttons.** Three levels: primary (filled `primary`, white label) for the main action on a view; secondary (outlined, `primary` label) for alternatives; text/quiet for low-emphasis actions. One primary button per view. Destructive actions use `error` as the filled color and require explicit confirmation. Disabled buttons are visibly muted and remain non-interactive but readable; a button awaiting a response shows a busy state and blocks repeat submission.

**Inputs.** Every input has a persistent visible label — never a placeholder as the only label. Placeholders show format examples only. Numeric log entry fields (weight, measurements, sets, reps, calories, macros) show their unit adjacent to the field. Required fields are marked in the label, not by color. Inputs sit on `surface` with a visible border at rest; border strengthens to `primary` on focus.

**Links.** `primary` colored and underlined in body copy so they are distinguishable without relying on hue. Citation links on plan content are always visibly links, since the evidence behind a plan must be reachable by the reader.

**Focus states.** Every interactive element has a visible focus indicator: a 2px `primary` outline offset 2px from the element, meeting 3:1 against its background. Focus is never suppressed without an equivalent replacement, and focus order follows the visual reading order.

**Form feedback and errors.** Validation errors appear inline, adjacent to the field that failed, in `error`, paired with an icon and text — never color alone. The message names the specific problem and how to fix it, not a generic failure. Errors are programmatically associated with their field and announced to assistive technology. On submit failure, focus moves to the first invalid field. Success confirmation uses `success` with an icon and text, and is announced politely without stealing focus.

**Empty states.** Progress views begin with no data. An empty state states what will appear there and names the action that populates it.

## Accessibility

- **Target conformance:** WCAG 2.2 AA.
- **Contrast:** 4.5:1 for body text, 3:1 for large text (≥24px, or ≥19px bold), 3:1 for UI component boundaries, focus indicators, and meaningful graphics. Every documented palette pairing meets these; new pairings must be verified before use.
- **Color independence:** color never carries meaning alone. Errors, success, required fields, and status all pair color with text, icon, or shape.
- **Keyboard:** every function is operable by keyboard, in a logical order, with no traps. Focus is always visible (see Components) and is managed deliberately when content opens, closes, or replaces itself. A skip link precedes repeated navigation.
- **Structure:** correct heading hierarchy, landmark regions, labelled controls, and text alternatives for all non-decorative graphics. The logo is decorative wherever an adjacent text label already names the product.
- **Reduced motion:** honor `prefers-reduced-motion`. When set, remove non-essential transitions, parallax, and auto-playing motion; keep only instantaneous state changes or a plain opacity fade. No motion is required to understand or complete any task.
- **Zoom and reflow:** usable at 200% zoom and at a 320px-wide viewport without horizontal scrolling or loss of content.
- **Text sizing:** relative units throughout so user font-size preferences are respected.

## Open Questions

- **OQ-1** What is the product name? Without it there is no wordmark, no lockup, and no favicon/app-icon strategy — the mark is abstract by necessity.
- **OQ-2** What is the intended brand personality (clinical and precise vs. encouraging and motivational)? This drives tone, color warmth, imagery policy, and typographic direction, none of which the requirements determine.
- **OQ-3** Is dark mode in scope? It affects palette structure, the logo's dark-background variant, and surface elevation conventions.
- **OQ-4** How should progress data be visualized — charts, tables, or both? REQUIREMENTS.md OQ-7 leaves this open, and it is the largest unspecified area of the interface.
- **OQ-5** How are plan citations and admin verification surfaced in the UI (inline links, a sources panel, a verification badge)? The requirement to display them is firm (FR-4.5, FR-4.6); the presentation is not.
- **OQ-6** How is the medical disclaimer presented and acknowledged (interstitial, checkbox, persistent banner)? FR-9.6 requires acknowledgement before first plan use but does not specify the form.
- **OQ-7** Do consultants and admins get a distinct visual treatment or a separate interface region, and how does a subscriber see that a consultant has access to their data?
- **OQ-8** Are there localization, right-to-left, or unit-system (metric/imperial) requirements that affect layout and numeric formatting? REQUIREMENTS.md OQ-4 leaves units open.
- **OQ-9** What imagery policy applies — photography, illustration, or neither? Exercise plans may need demonstration visuals, which the requirements neither specify nor exclude.
