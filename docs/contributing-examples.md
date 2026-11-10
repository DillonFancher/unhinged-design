# Contributing examples

More examples are welcome. Send a small, public-safe specimen that teaches someone how to use the visual language; this is an intake guide, not a roadmap.

## Include

- A screenshot, short screen recording, or self-contained HTML/CSS snippet.
- What the example demonstrates: a card, form state, data display, responsive shell, empty state, or another concrete pattern.
- The intended viewport and what changes at narrow widths.
- At least one meaningful state: default, hover/focus, success, warning, error, loading, or empty.
- The keyboard path and accessible name/label for every interactive control. Include status words, not color-only indicators, and mention reduced-motion behavior.
- Any browser fallback needed for blur, masks, blend modes, or modern color functions.

## Sanitize before sending

Use fictional names, counts, URLs, identifiers, and copy. Remove private screenshots, customer or organizational names, personal information, source paths, credentials, tokens, service endpoints, internal hostnames, analytics exports, and operational details. Do not paste backend code or architecture documents: this repository is for the visual language only.

Keep examples dependency-free when possible. A local HTML file is ideal; if a runtime is genuinely needed, explain why and keep the visual specimen separable from it. Do not add a CDN, remote font, tracker, deployment configuration, or package solely to demonstrate the look.

## Small review checklist

- [ ] The example opens or renders from local assets without a network.
- [ ] Text remains readable against the void and glass.
- [ ] Focus is visible and the narrow layout does not require sideways page scrolling.
- [ ] Headings are single accessible strings, not duplicated glitch layers.
- [ ] Controls are real links, buttons, form inputs, or disclosure elements.
- [ ] The example identifies the author and confirms that its content is safe to publish.
