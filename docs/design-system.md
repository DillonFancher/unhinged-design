# Design system

This kit recreates Dillon Fancher’s Agent Gateway **visual language**, not the application behind it. The name for the aesthetic is **neon-brutalist glassmorphism on a void**: a near-black violet field, saturated ambient light, translucent cards, brutal display type, and state communicated as colored light plus words.

## The theory

- **Void first.** `#050008` is black with a violet whisper, so the accents bloom instead of clipping against pure black.
- **Atmosphere before content.** Magenta, cyan, and acid-lime radial fields sit over a violet sweep. A 42px blueprint grid and 4px CRT scanlines add texture without becoming content.
- **Glass with a hairline.** Cards are translucent violet with an 18px blur and `saturate(1.25)`. Their border reads as a magenta → cyan → acid masked ring, not a heavy box outline.
- **Type is the loud part.** System sans is enough: uppercase, 850–950 weight, negative tracking, compressed line-height, and hard magenta/cyan text ghosts. Micro-labels reverse that recipe with small type and wide tracking.
- **Light is state.** A status has a word, glyph, border, tint, and matching glow. Color never does the entire accessibility job.
- **Charts stay disciplined.** Data uses the muted categorical palette (`--viz-cat-*`), not the brighter UI neons. “Other” uses `--viz-neutral` and italic muted text.

## Literal public recipe

The values below are the public visual source recipe. They are also present as copyable declarations in `css/unhinged.css`.

```css
:root {
  --void: #050008;
  --void-2: #0b0617;
  --ink: #f8edff;
  --muted: #b8a7c8;
  --acid: #d7ff2f;
  --hot: #ff2bd6;
  --plasma: #7c3cff;
  --cyan: #00f5ff;
  --ember: #ff7a18;
  --card: rgba(16, 8, 30, 0.78);
  --card-strong: rgba(31, 13, 52, 0.92);
  --card-border: rgba(255, 255, 255, 0.16);
  --success: #83ff6a; --success-bg: rgba(36, 255, 94, 0.14);
  --error: #ff5c8a; --error-bg: rgba(255, 43, 105, 0.16);
  --warning: #ffd166;
  --shadow: 0 28px 90px rgba(0, 0, 0, 0.5), 0 0 45px rgba(255, 43, 214, 0.1);
  --radius: 1.35rem;
}
```

The full token block adds the five muted chart categoricals and their glow partners, status colors, latency colors, chart surface, hairline, and neutral bucket. The deliberate distinction is teal `#00a9b0` for data versus electric cyan `#00f5ff` for UI; olive `#87a300` for data versus acid `#d7ff2f` for brand state.

```css
body {
  background:
    radial-gradient(circle at 12% 6%, rgba(255, 43, 214, 0.38), transparent 26rem),
    radial-gradient(circle at 82% 18%, rgba(0, 245, 255, 0.28), transparent 24rem),
    radial-gradient(circle at 48% 94%, rgba(215, 255, 47, 0.22), transparent 28rem),
    linear-gradient(135deg, #050008 0%, #12061f 46%, #030009 100%);
}

.ud-shell {
  width: min(1240px, calc(100% - 2rem));
  margin: 0 auto;
}
```

The fixed `body::before` layer uses 42px lines at `0.28` opacity and fades to transparent at 85%. The fixed `body::after` layer uses 4px scanlines at `0.14` opacity with `mix-blend-mode: screen`. Both are pointer-transparent and remain behind the shell.

```css
.ud-card {
  border: 1px solid var(--card-border);
  border-radius: var(--radius);
  background: linear-gradient(135deg, rgba(255,255,255,.08), transparent 32%), var(--card);
  box-shadow: var(--shadow);
  backdrop-filter: blur(18px) saturate(1.25);
}
```

The card’s `::before` is a 1px padded gradient ring at `0.46` opacity, removed from the content box with `mask-composite: exclude`; `::after` is a rotated 28° white sheen. A normal border and opaque-enough card remain in place as the fallback when masks or backdrop filters are unsupported.

Display headings use `clamp(3.1rem, 8vw, 7.6rem)`, `line-height: .76`, `letter-spacing: -.1em`, and this signature shadow:

```css
text-shadow: 5px 0 0 rgba(255,43,214,.9),
  -4px 0 0 rgba(0,245,255,.8), 0 0 42px rgba(255,255,255,.24);
```

A page gets one `.ud-label` acid eyebrow. Labels are `0.72rem`, weight `950`, uppercase, and tracked at `0.22em`. Body copy stays `--muted`. Buttons use the hot → plasma → cyan gradient; recessed inputs get an acid focus bloom; active range pills get an acid border and glow.

## Standalone adaptations

The source interface used application-specific dashboard markup, data, and chart runtime. This kit intentionally adapts that recipe for a portable static file:

- `.ud-*` namespacing keeps copied components from colliding with a host page. Baseline `html`, `body`, and focus rules establish the atmosphere and can be scoped by a host if needed.
- The gallery uses CSS bars and a conic-gradient donut, so there is no chart library, canvas, JSON island, backend, or network request.
- The optional `js/demo.js` only copies a clearly fictional markup snippet and reports success. Everything else works without JavaScript, including the native checkbox and semantic links.
- The source’s dense grid-table becomes a smaller horizontally scrollable CSS grid. The wrapper is keyboard-focusable and the mobile breakpoint hides only the share column, never the content.
- Every heading remains one text node. The RGB split is `text-shadow`, so assistive technology does not receive duplicated visual ghosts.
- `backdrop-filter`, masking, `color-mix()`, and blend modes are enhancements. Solid/translucent backgrounds, a regular border, and visible text remain the fallback. The stylesheet includes `-webkit-` mask/backdrop declarations for common browser variants.
- Motion follows the source timing scale (mostly 160ms), while `prefers-reduced-motion: reduce` removes transitions and animation duration. Focus rings are acid, 3px, and offset.
