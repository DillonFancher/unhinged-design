# Unhinged Design

A copy/paste design kit for Dillon Fancher’s **neon-brutalist glassmorphism on a void**: saturated light, glass hairlines, crushed display type, and enough attitude to keep a dashboard awake.

Open `index.html` directly from disk. There is no build, dependency, font download, server, or network request.

## Copy it in 30 seconds

1. Copy [`css/unhinged.css`](css/unhinged.css) into your project.
2. Add this in your page head:

   ```html
   <link rel="stylesheet" href="css/unhinged.css">
   ```

3. Put your page content in `<main class="ud-shell">` and apply `.ud-card`, `.ud-button`, `.ud-input`, `.ud-status`, and the other documented classes.
4. Copy only the markup you need from [`index.html`](index.html). The CSS is the reusable part; classes under the `ud-demo-*` prefix are gallery-only (the current demo only uses `ud-demo-message`).

Minimal card example:

```html
<link rel="stylesheet" href="css/unhinged.css">
<main class="ud-shell">
  <section class="ud-card" aria-labelledby="signal-title">
    <p class="ud-label">Signal / 01</p>
    <h1 id="signal-title" class="ud-heading">Make it glow</h1>
    <p class="ud-copy">Readable information with a little beautiful menace.</p>
    <a class="ud-button" href="/next">Continue</a>
  </section>
</main>
```

## Contents

- `index.html` — self-contained visual gallery with fictional data and small demo interactions.
- `css/unhinged.css` — zero-dependency, independently copyable tokens, background, glass, type, controls, status, data display, responsive rules, and reduced-motion support.
- `js/demo.js` — optional gallery-only copy/status behavior; the CSS and markup do not require JavaScript.
- `docs/design-system.md` — design theory, literal recipes, and the standalone adaptations made here.
- `docs/contributing-examples.md` — how to send future screenshots or snippets without sending private material.
- `.github/workflows/check.yml` and `scripts/check-static.py` — lightweight source checks only; no build or dependency install.

## Source and boundaries

The visual language is adapted from the author’s Agent Gateway interface: its void background, ambient glows, blueprint grid, glass cards, RGB-split headings, acid eyebrows, and categorical data colors. This kit exports that visual language only. It does **not** export the source application’s architecture, backend, services, data, endpoints, actors, or operational content; every example here is fictional.

This is an initial public design-kit release with room for more examples. A license has not been selected yet, so public visibility alone does not grant reuse permission. We will ask the owner about an MIT choice later.
