# Design System — Agent Instructions

This skill describes the visual language for a **minimal portfolio** aesthetic — the same look used at https://minimal-xi.vercel.app/. Every page, component, and layout you produce in this project MUST follow these rules. The system favours typography, whitespace, and one strong call-to-action over decoration.

The rules in this file are **technology-agnostic**. They describe *what* to render and *why* — not which framework, library, utility classes, or rendering technology to use. Implement them in whatever stack the project happens to use.

## Style

A quiet, typography-driven personal portfolio. Warm off-white canvas, near-black ink, a single ultra-bold display headline, supporting copy in soft 60% ink, and one solid dark CTA. A subtle diagonal crosshatch in the background provides texture without competing with content.

Think: independent designer / engineer profile site. Calm, confident, generous whitespace, no ornament.

## Non-Negotiable Aesthetic Rules

These rules apply to **every screen** you build in this project. If a request would break them, push back or adapt — never invent a different style.

1. **Two colours only for layout.** Background `#F4F4F1` (warm cream), ink `#0C0C09` (warm near-black). Anything else (status, accent) is opt-in and used sparingly inside small components, never on hero surfaces.
2. **Soft hierarchy through opacity.** Secondary copy is always the ink colour at **60% opacity**. Do not introduce a separate gray text token for body copy.
3. **One display headline per view.** The hero `h1` is the visual anchor: display family at weight **900 (black)**, tight letter-spacing (-0.025em), and a responsive scale of **32px → 40px → 60px** across mobile / tablet / desktop. Never apply this scale to anything that is not the page's primary headline. Never exceed 60px.
4. **One primary CTA per view.** Solid `#0C0C09` background, cream label, 6px corner radius, **24px horizontal × 12px vertical padding** (Base size), body family at 16px and weight 600. Hover lowers the background to 90% opacity, active to 80%. No gradient, no glint, no shadow on the button.
5. **Centered, narrow content column.** Hero / landing content lives inside a single 672 px column, centered both axes, on a full-viewport-height wrapper. Inner content is centre-aligned and stacked vertically.
6. **Always render the crosshatch background.** A non-interactive layer underneath the content carrying two repeating diagonal-line gradients at +45° and -45°, colour `rgba(12, 12, 9, 0.03)`, 1 px lines, 32 px grid. This is the project's signature texture — include it on every full-page route.
7. **Flat, almost shadowless.** Only the avatar disc carries a small shadow. No card elevations, no glints, no blur, no neumorphism. Borders are 1 px (or 4 px for the avatar disc) — never thicker.
8. **Sans-serif everywhere.** **Inter** for display headings, **Open Sans** for body and UI labels, **Inconsolata** for code. Do not introduce a serif or a script.
9. **Generous vertical rhythm.** 24 px from avatar to `h1`, 32 px from `h1` to lead paragraph, 64 px from paragraph to CTA. Never crowd.
10. **No dark-mode swap.** This palette is intentionally light only. Do not author dark-mode overrides — if dark variants exist in dependent libraries, override them back to the cream / ink pair.

## Portfolio Page Pattern (use as the default scaffold)

Every new page in this project should start from this scaffold and only add what's strictly necessary. The structure is described in plain terms — implement it in whatever templating language the project uses.

```
PAGE WRAPPER
  - full viewport height
  - background: surface (cream)
  - text colour: text (ink)
  - relative positioning so the background layer can sit beneath
  - content centred horizontally and vertically
  - outer padding: 16 px on mobile, 32 px from the small breakpoint up

  CROSSHATCH BACKGROUND LAYER
    - sits behind everything (lowest stacking order)
    - covers the full wrapper
    - non-interactive (does not catch clicks)
    - background: two repeating diagonal-line gradients at +45° and -45°,
      colour rgba(12,12,9,0.03), 1 px lines, 32 px grid spacing

  MAIN CONTENT COLUMN
    - max width 672 px, centred
    - vertical flow, centre-aligned text and items
    - sits above the crosshatch (higher stacking order)

      AVATAR DISC
        - 208 × 208 px, fully rounded
        - 4 px solid border in disc-border
        - inner background: white
        - small shadow
        - 24 px below it: the headline

      HERO HEADLINE (h1)
        - display family, weight 900, tight letter-spacing
        - colour: primary
        - size: 32px mobile / 40px tablet / 60px desktop
        - 32 px below it: the lead paragraph

      LEAD PARAGRAPH
        - body family, weight 400
        - colour: text at 60% opacity
        - relaxed line-height (~1.625)
        - size: 18 px mobile / 20 px tablet / 24 px desktop
        - 64 px below it: the CTA

      PRIMARY CTA
        - solid dark CTA per buttons.md
```

If a page needs more sections (works grid, about, contact), each new section must:

- Sit on the same cream surface (no alternating section bands).
- Stay inside a centred column no wider than 768 px for prose, 1024 px for grids.
- Separate from the previous section with at least 96 px of vertical padding, never with a visible divider unless the divider is a single 1 px hairline at `text/10`.

## Before Writing Any Code

1. **Read the foundation modules first.** For any UI work, read at minimum: `colors.md`, `typography.md`, `layout.md`, `buttons.md`. For component work, also read the matching component file.
2. **Re-read this SKILL.md every time** you start a new page — the non-negotiable rules above are how this project stays consistent.

## Critical Implementation Notes

- **Tokens are agnostic.** Names like `primary`, `surface`, `text` describe roles, not framework classes. Map them to whatever styling layer the project uses — for example, declare CSS custom properties such as `--color-primary: #0C0C09`, `--color-surface: #F4F4F1`, `--color-text: #0C0C09`, `--font-display: "Inter", sans-serif`, `--font-sans: "Open Sans", sans-serif` — and consume those tokens in components.
- **Cross-reference modules.** A button inside a card must satisfy both `cards.md` AND `buttons.md`.
- **Use semantic HTML.** Proper heading order (`h1`→`h6`), `<button>` for actions, `<a>` for navigation, `aria-label` on icon-only controls, alt text on every image.
- **Typography page types:** Read `typography.md` page-type rules. Dashboard and e-commerce app surfaces use compact headings (max 28px, prefer 24px). Only e-commerce storefront heroes may use full display scale.
- **Button padding:** Use standard sizes from `buttons.md` — normal padding only, no oversized custom dimensions.
- **Every interactive element needs hover, focus-visible, and disabled states** as defined in the matching module.

## Module Index

### Foundation (read first for any UI work)
- [colors.md](colors.md) — the cream / ink palette plus the small set of accent tokens
- [typography.md](typography.md) — Inter display, Open Sans body, hero scale
- [layout.md](layout.md) — hero scaffold, spacing rhythm, crosshatch background
- [radius.md](radius.md) — radius scale (very small)
- [shadows.md](shadows.md) — elevation tokens (mostly unused)
- [borders.md](borders.md) — border widths (1 px default, 4 px on avatar)

### Components
- [buttons.md](buttons.md) — primary solid CTA + minimal secondary / ghost
- [button-group.md](button-group.md) — grouped buttons
- [cards.md](cards.md) — flat hairline cards
- [inputs.md](inputs.md) — single-line minimal inputs
- [alerts.md](alerts.md) — inline minimal alerts
- [badges.md](badges.md) — small uppercase badges
- [lists.md](lists.md) — list components
- [avatars.md](avatars.md) — large bordered profile disc + small variants
- [icon-shapes.md](icon-shapes.md) — icon containers

### Complex Components
- [accordion.md](accordion.md) — accordion variants
- [dropdown.md](dropdown.md) — dropdown menus
- [modals.md](modals.md) — modal dialogs
- [tabs.md](tabs.md) — tab navigation
- [tables.md](tables.md) — table structure
- [pagination.md](pagination.md) — pagination components
- [sidebars.md](sidebars.md) — sidebar navigation
- [radios-checkboxes-toggle.md](radios-checkboxes-toggle.md) — selection controls
- [tooltips-popovers.md](tooltips-popovers.md) — tooltips and popovers
- [content.md](content.md) — grid system, responsiveness

---

## Source file: `accordion.md`

# Accordion

> Dependencies: `colors.md`, `radius.md`, `borders.md`, `typography.md`

The default accordion is **Flush** — it disappears into the cream surface and reads as a list of expandable headings. Use the bordered wrapper variant only when the accordion sits inside a multi-section page and needs visual containment.

## Core Specs

- **Wrapper (bordered variant):** full width, 1 px border `text/10`, 6 px radius, corner-clipped on the first/last items
- **Item separator:** 1 px hairline `text/10` on every item except the last
- **No shadow** on any variant

## Trigger (button)

- Layout: horizontal flex, items vertically centred, spaced apart, full-width
- Padding: 16 px horizontal, 16 px vertical (20 px / 16 px when inside a bordered wrapper)
- Font: 16 px Open Sans, weight 500
- Color: `text`
- Background: `transparent`
- Hover: background `text` at 5% opacity
- Open state: background `text` at 5% opacity, weight lifts to 600
- Focus-visible: 2 px outline `primary`, 2 px offset
- Transition: `colors` 150 ms

## Panel (content)

- Padding: 16 px horizontal, 16 px vertical (20 px / 16 px in bordered variant)
- Background: `transparent`
- Top hairline: 1 px `text/10` (only inside the bordered variant)
- Font: 14 px Open Sans, `text/60`, line-height 1.625

## Chevron Icon

- Size: 16 × 16 px
- Color: `text/40`
- Closed: 0deg
- Open: 180deg
- Transition: `transform` 150 ms

## Variants

### Flush (default)
No outer border, no wrapper background. Items separated by 1 px `text/10` hairlines only. Use inside any container that already has its own background.

### Bordered (collapse)
A single shared bordered wrapper around all items. One panel open at a time.

### Always Open
Multiple panels can be open simultaneously. Same styling as Flush or Bordered.

## States | State | Trigger appearance | |---|---| | Closed | `text` text, transparent background | | Hover | background `text` at 5% opacity | | Open | background `text` at 5% opacity, weight 600 | | Focus | 2 px outline `primary`, 2 px offset | | Disabled | `text/30` text, cursor not-allowed, no hover |

## Prohibited

- No drop shadow.
- No coloured background on open items.
- No animation beyond the chevron rotation and a fade on the panel content.

---

## Source file: `alerts.md`

# Alerts

> Dependencies: `colors.md`, `radius.md`, `borders.md`

Alerts are inline status messages — quiet by default, never blocking, never tinted with saturated fills on hero surfaces.

## Core Specs

- **Padding:** 16 px
- **Radius:** 6 px
- **Border:** 1 px solid (variant-coloured)
- **Background:** `transparent` for the neutral variant; `*-soft` for status variants
- **Heading:** 14 px Open Sans, weight 600
- **Body:** 14 px Open Sans, weight 400, line-height 1.6
- **Icon (optional):** 16 × 16 px, sits at the top-left with a 12 px right margin, colour matches the variant text

## Variants

### Neutral (default)
- Background: `transparent`
- Border: 1 px `text/20`
- Text (heading + body): `text`

### Success
- Background: `success-soft`
- Border: 1 px `success`
- Text: `success` for heading, `text` at full strength for body

### Warning
- Background: `warning-soft`
- Border: 1 px `warning`
- Text: `warning` for heading, `text` for body

### Danger
- Background: `danger-soft`
- Border: 1 px `danger`
- Text: `danger` for heading, `text` for body

### Info
- Background: `info-soft`
- Border: 1 px `info`
- Text: `info` for heading, `text` for body

## Dismissible Alert

- Add a 16 × 16 px close button at the top-right, `text/40`, hover lifts to `text`. Wrapper `aria-label="Dismiss"`.

## Prohibited

- No drop shadow.
- No saturated solid backgrounds (no full red / green / amber fills).
- No alerts inside the hero block — keep status feedback inside forms or below-the-fold sections.

---

## Source file: `avatars.md`

# Avatars

> Dependencies: `colors.md`, `radius.md`, `shadows.md`, `borders.md`

The avatar is the **face of the portfolio** — it sits above the headline and is the second-largest element on the page after the hero `h1`. Treat it with care.

## Hero Avatar (the signature profile disc)

This is the only avatar variant that should appear in a hero section. | Property | Value | |---|---| | Width × Height | **208 × 208 px** | | Shape | | Border | **4 px solid `#101828`** | | Inner background | `#FFFFFF` — visible only if the photo doesn't fill | | Image fit | cover fit | | Shadow | | Margin-bottom | 24 px — to the hero `h1` |

The hero avatar is **always circular**. Never a rounded square, never a hexagon, never with a coloured border.

## Inline Avatars (for testimonials, comments, author bylines) | Size | Dimensions | Border | |---|---|---| | Small | 32 × 32 px | none | | Base | 40 × 40 px | none | | Large | 56 × 56 px | 1 px `text/10` (optional) |

All inline avatars are the default radius, cover fit, and use the same white fallback.

## Stacked Avatars

- Displayed in a row
- Each avatar: 32 × 32 px, the default radius, with a 2 px `surface`-coloured ring so they read as separate when overlapping
- Overlap: `-8 px` margin (`-ml-2`) on every avatar except the first
- A trailing "+N" counter uses the same dimensions, background `text` at 10% opacity, ink colour, 12 px Open Sans semibold

## Avatar with Text (author byline)

- Layout: inline flex, items vertically centred, 12 px gap
- Avatar: Base size (40 × 40 px), the default radius, cover fit
- Name: 14 px, weight 600, `text` colour
- Subtitle: 12 px, weight 400, `text/40`

## Prohibited

- No square avatars on hero surfaces.
- No coloured borders (no brand-coloured ring, no rainbow gradient).
- No drop shadow heavier than shadow-sm (see shadows.md).
- No animated/loaded ring spinners around the hero avatar.
- The hero avatar size (208 px) does not change — do not shrink it on smaller screens beyond what the centered layout already does.

---

## Source file: `badges.md`

# Badges

> Dependencies: `colors.md`, `radius.md`, `typography.md`

Badges in this design are tiny, restrained, mostly outline. They label things — they never compete with content.

## Core Specs

- **Border:** 1 px (`text/20` for neutral; matching status hue otherwise)
- **Background:** `transparent` (default) or status `*-soft` for status variants
- **Radius:** 4 px; pills (`9999px`) only for icon-only dots
- **Family:** Open Sans
- **Weight:** 500
- **Letter-spacing:** `0.06em` for uppercase variants

## Sizes | Size | Font size | Padding-x | Padding-y | Case | |---|---|---|---|---| | Default | 11 px | 8 px | 2 px | UPPERCASE, `0.08em` tracking | | Large | 13 px | 10 px | 4 px | Title Case |

The default badge is uppercase and small — that's the project's preferred treatment (think "DESIGNER · 2024").

## Variants

### Neutral (default — use this everywhere unless you mean status)
- Background: `transparent`
- Border: 1 px `text/20`
- Text: `text/60`

### Solid Ink (when more emphasis is needed)
- Background: `primary`
- Border: none
- Text: `surface`

### Status — Success
- Background: `success-soft`
- Border: 1 px `success`
- Text: `success`

### Status — Warning
- Background: `warning-soft`
- Border: 1 px `warning`
- Text: `warning`

### Status — Danger
- Background: `danger-soft`
- Border: 1 px `danger`
- Text: `danger`

### Status — Info
- Background: `info-soft`
- Border: 1 px `info`
- Text: `info`

## Pill / Dot Indicators

- **Dot only** (notification): 8 × 8 px, the default radius, status-coloured background, no border
- **Pill with text:** the default radius, padding 10 px / 4 px, otherwise same colours as the matching variant above

## Badges with Icons

- Icon: 12 × 12 px (default), 14 × 14 px (large)
- Gap: 4 px between icon and label
- Icon uses `currentColor`

## Dismissible Badge

- A close button sits inside the badge, 12 × 12 px, `text/40`
- Hover lifts it to `text`
- No background change on close-button hover (keep it quiet)

## Prohibited

- No saturated coloured-background badges (no solid red, blue, green) outside of `*-soft` status variants.
- No drop shadows.
- No badges larger than the Large size.
- No more than two badges grouped together — they will fight the headline.

---

## Source file: `borders.md`

# Borders

## Width Scale | Context | Width | |---|---| | Hairlines, dividers, card outlines, input outlines | **1 px** (default) | | Focus-visible outlines | 2 px (with 2 px offset) | | **Avatar disc** | **4 px** |

## Colour

- Default border colour: `text/10` (a 10 % opacity ink hairline). This is what you use for cards, inputs, dividers.
- Avatar disc border: `#101828` (`disc-border` token). Crisper than `text` to separate the photo from the cream surface.
- Focus outline: `primary` (`#0C0C09`).
- Status borders: the matching status colour (`success`, `danger`, `warning`, `info`) used inside small components only.

## Rules

- **Solid by default.** No dashed, dotted, or double borders anywhere except file dropzones (which may use 1 px dashed at `text/40`).
- **Never thicker than 1 px** on rectangular content (cards, inputs, dividers). The 4 px avatar border is the single exception and is unique to that component.
- **Never mix widths inside a single component.**
- **Border-radius and width move together.** A 1px card outline pairs with `card` (2px radius); buttons and modals pair with `radius-md` (6px); the 4px avatar pairs with `radius-full`.
- Dividers between sections: prefer whitespace; if a line is required, use a 1 px `text/10` rule that spans the full container width with no inner spacing.

---

## Source file: `button-group.md`

# Button Groups

> Dependencies: `buttons.md`, `colors.md`, `radius.md`, `borders.md`

Use button groups sparingly — they add density to a design that otherwise rewards space. They're appropriate for view-switchers and toolbar segments, not for hero CTAs.

## Core Specs

- **Wrapper:** inline flex, 6 px radius, 1 px border `text/10`
- **No shadow** on the wrapper (this design is flat)
- **Children overlap:** `-1px` left margin on every child except the first, so the shared border reads as one line
- **All inner buttons use the Secondary or Ghost variant from `buttons.md`** — never the solid Primary

## Anatomy

### Wrapper
- Display: inline flex
- Radius: 6 px
- Border: 1 px solid `text/10`
- Background: `transparent`

### First Button
- Inline-start corners: 6 px radius
- Inline-end corners: 0

### Middle Button(s)
- All four corners: 0

### Last Button
- Inline-start corners: 0
- Inline-end corners: 6 px radius

### All buttons except first
- `-1px` left margin

## States

- **Inactive button:** transparent background, `text/60` label
- **Hover:** background lifts to `text/5`, label to `text`
- **Selected / active:** background `text` (full ink), label `surface`
- **Focus-visible:** 2 px outline `primary`, 2 px offset (the entire group can lose its border-overlap during focus — that's fine)

## Rules

- Maximum **4 segments** in a group; beyond that, switch to a select.
- Icon-only buttons inside a group: 16 × 16 px icon, height matches text-button rows.
- Never mix sizes inside a single group.

---

## Source file: `buttons.md`

# Buttons

> Dependencies: `colors.md`, `radius.md`, `typography.md`

The minimal portfolio favours **one** strong button per view. The default is the solid dark CTA below — the same button used for "See My Works" on the live site.

## Core Specs (apply to every variant unless overridden)

- **Family:** Open Sans
- **Weight:** 600 (semibold)
- **Display:** inline flex, items vertically centred, content horizontally centred
- **Radius:** `6px` — the default. Pills (`9999px`) are allowed for icon-only round buttons.
- **Border:** none on the primary; 1px on secondary/ghost outlines.
- **Shadow:** **none.** Buttons in this system are flat — no glints, no inset highlights, no drop shadows.
- **Cursor:** `pointer`.
- **Transition:** `transition-colors` only (no transform, no scale).
- **Box sizing:** border-box.
- **Focus-visible:** `outline: 2px solid var(--color-primary); outline-offset: 2px`. No focus ring of any other colour.

## Sizes

Use **normal padding** from the scale below — aligned with other design systems. Never invent oversized hero padding (e.g. 40px × 24px or taller than ~48px total height) unless Extra large is explicitly required.

| Size | Font size | Horizontal padding | Vertical padding |
|---|---|---|---|
| Small | 14px | 16px | 8px |
| Base (default) | 16px | 24px | 12px |
| Large | 16px | 20px | 12px |
| Extra large | 16px | 24px | 14px |

Hero and page-level CTAs use **Base** or **Large** from this table — not custom dimensions.

## Variants

### Primary (the signature CTA — dark on cream)
- **Background:** `primary` (`#0C0C09`)
- **Text:** `surface` (`#F4F4F1`)
- **Border:** none
- **Hover:** background `primary` at 90% opacity
- **Active:** background `primary` at 80% opacity
- **Focus-visible:** 2px solid `primary` outline with 2px offset
- **Disabled:** background `primary` at 30% opacity, text `surface` at 70% opacity, cursor not-allowed

### Secondary (outline — used only when a Primary already exists in the same view)
- **Background:** `transparent`
- **Border:** `1px solid primary`
- **Text:** `primary`
- **Hover:** background `primary`, text `surface` (full ink fill)
- **Active:** background `primary` at 90% opacity, text `surface`
- **Focus-visible:** same as Primary
- **Shadow:** none, **no glint**

### Ghost (text-only, for tertiary navigation links)
- **Background:** `transparent`
- **Border:** none
- **Text:** `primary`
- **Underline:** 1px, `text/40` colour, on hover the underline becomes full `primary`
- **Hover:** no background change — the underline change is the entire hover affordance
- **Focus-visible:** outline-2 outline-offset-2 outline-primary
- **No shadow**

### Disabled (any variant)
- **Cursor:** `not-allowed`
- **Opacity:** 30% on the foreground colour
- **No hover, no focus ring change**

## Pairing Rules (per page)

- **One Primary maximum** per view. Two competing dark buttons breaks the design.
- A Secondary may sit next to a Primary in the same flex row, separated by 12–16px gap.
- Ghost buttons are used for navigation (`Home`, `About`, `Works`) — never as the primary action.

## Icons in Buttons

- Icon size: 16 × 16px (Base/Small) or 20 × 20px (Large)
- Spacing: `8px` gap between icon and label
- Icon stroke uses `currentColor` so it inherits the button's text colour
- Layout: inline flex, vertically centered

## Prohibited

- **No box-shadow, no inset glint, no gradient.** Flat fills only.
- **No coloured CTAs** (no green / red / brand-blue solid buttons on hero surfaces). Status actions live inside alerts/forms, not as page-level CTAs.
- **No transform or scale on hover** — only colour changes.
- **No rounded-full** on rectangular text buttons. Pills are reserved for icon-only round controls.
- **No uppercase** on button labels longer than two words.
- **No oversized padding** outside the Sizes table.

---

## Source file: `cards.md`

# Cards

> Dependencies: `colors.md`, `radius.md`, `borders.md`, `typography.md`

Cards in this design are **flat hairline frames** — no fill, no shadow, just a 1 px outline that lets the cream surface show through.

## Core Specs

- **Background:** `transparent` (the page `surface` shows through)
- **Border:** 1 px solid at `text/10`
- **Radius:** 2px — **every card uses 2px border radius only**
- **Shadow:** **none**
- **Padding:** 24px; 32px for feature/work cards

## Card Heading

- Family: Inter (display)
- Size: 18 px mobile, 20 px desktop
- Weight: 600
- Color: `primary`
- Margin-bottom: 8 px to subtitle / 16 px to body

## Card Subtitle / Meta

- 12 px Open Sans, weight 500, `text/40`
- Eyebrow style (uppercase, `0.12em` tracking) optional

## Card Body Copy

- 14 px Open Sans, weight 400, `text/60`, line-height 1.6

## States

### Static Card (non-interactive)
- Border: 1 px `text/10`
- No hover, no cursor change

### Interactive Card (link wraps the whole card)
- Same base styles
- Hover: border colour shifts to `text/30`, body text (any `text/60` content) lifts to `text` for 150 ms — that's the entire affordance
- Cursor: `pointer`
- Focus-visible: 2 px outline `primary`, 2 px offset

### Featured / Work-thumbnail Card
- Image fills the top of the card (full-bleed inside the radius), aspect ratio 4:3, cover fit
- Image radius matches container: **2px** on the top corners only
- Below the image: 24 px padding block with title (`h3` style) + 1-line description + small "View →" link (ghost button style)

## Layouts

- Single-column for testimonials / quotes (max width 768 px, centered)
- Two-column at `md`, three-column at `lg` for project grids — gap `32 px`
- Never more than 3 columns. Density isn't the goal of this design.

## Prohibited

- **No drop shadow.** Replace any "elevated card" instinct with whitespace and a hairline.
- **No filled background colour** (no light gray cards). The cream of the page must be visible inside the card.
- **No gradient borders, no animated borders.**
- **No badge clusters** stacked on the card. One small status pill maximum.

---

## Source file: `colors.md`

# Color Tokens

> The minimal portfolio palette is intentionally tiny: one warm cream, one warm near-black, and a few status hues. Light only — no dark-mode variants.

All values below are technology-agnostic; map them to whatever styling layer the project uses.

## Core Palette (used everywhere) | Token | Value | Role | |---|---|---| | `surface` | `#F4F4F1` | Page background, button-foreground on dark | | `primary` | `#0C0C09` | Headline ink, CTA background | | `text` | `#0C0C09` | Default body ink (same value as `primary`, kept distinct for semantics) | | `rgba(12, 12, 9, 0.6)` | Secondary copy — always express as "text at 60% opacity"; do not introduce a separate gray hex | | `rgba(12, 12, 9, 0.4)` | Captions, metadata | | `hairline` | `rgba(12, 12, 9, 0.10)` | Optional 1 px dividers | | `crosshatch` | `rgba(12, 12, 9, 0.03)` | The signature +45° / -45° background pattern |

## Bordered Disc (avatar) | Token | Value | |---|---| | `disc-border` | `#101828` (slightly cooler than ink for crispness on the cream) | | `disc-fill` | `#FFFFFF` |

## Interaction States (derived from `primary`) | State | Expression | |---|---| | Hover on dark CTA | `primary` at 90% opacity | | Active on dark CTA | `primary` at 80% opacity | | Focus ring | `primary` outline, 2 px, 2 px offset | | Disabled | `primary` at 30% opacity background, `surface` text |

## Status (use only inside small components — never on hero surfaces) | Token | Value | |---|---| | `success` | `#16A34A` | | `warning` | `#D97706` | | `danger` | `#DC2626` | | `info` | `#2563EB` |

Each status token is paired with a `*-soft` background derived as a 10% mix of the status colour into `surface`.

## Semantic Usage Rules

- **Page surface:** always `surface`. Never alternate section backgrounds.
- **Headlines (`h1`–`h3`):** `primary`.
- **Body paragraphs:** `text` at 60% opacity. Full-strength `text` is reserved for emphasised inline runs (`<strong>`).
- **Captions / metadata / timestamps:** `text` at 40% opacity.
- **Primary CTA:** `primary` background, `surface` label.
- **Links inline in copy:** `primary` ink, 1 px underline at `text/40`, hover removes the underline.
- **Dividers:** 1 px line at `hairline`. Avoid them when whitespace already separates content.
- **Status indicators:** use the status token for the icon / dot only; keep the surrounding surface cream.

## Prohibited

- No raw hex / rgb in component code — always go through tokens.
- No second gray ramp. Hierarchy is achieved by lowering the opacity of `text`, not by adding new grays.
- No gradients on text or surfaces.
- No saturated brand colours on large layout surfaces. The page must read as cream + ink first.
- No dark-mode overrides. This skill is light-mode only.
- No accent colour for body copy or navigation.

---

## Source file: `content.md`

# Content & Grid System

> Dependencies: `layout.md`, `typography.md`

## Containers | Type | Max width | Horizontal padding | |---|---|---| | Hero (single-column) | **672 px** | 16 px on mobile, 32 px from the small breakpoint up | | Long-form prose | 768 px | 16 px on mobile, 32 px from the small breakpoint up | | Works grid | 1024 px | 16 px on mobile, 32 px from the small breakpoint up | | Absolute outer cap | 1280 px | 16 px on mobile, 32 px from the small breakpoint up |

Centre everything horizontally. No full-bleed text — text always sits inside one of the four containers above.

## Vertical Padding | Breakpoint | Section padding | |---|---| | Mobile | 64 px | | Tablet (≥768 px) | 96 px | | Desktop (≥1024 px) | 128 px |

The hero section uses full viewport height and centres its content vertically — it does not follow the section padding scale.

## Grid System

Mobile-first. Default to one column; only escalate when content density actually requires it. | Context | Gap | |---|---| | Works grid (cards) | 32 px | | Two-column prose | 48 px | | Compact metadata rows | 16 px |

### Responsive Columns | Breakpoint | Default columns | Maximum | |---|---|---| | Mobile (default) | 1 | 1 | | Small (≥640 px) | 1 | 2 | | Medium (≥768 px) | 2 | 2 | | Large (≥1024 px) | 2 | 3 |

**Never more than 3 columns.** This design's density is intentionally low.

## Breakpoints | Name | Width | |---|---| | Small | 640 px | | Medium | 768 px | | Large | 1024 px | | Extra large | 1280 px | | 2x Extra large | 1536 px |

## Composition Order Inside a Section

1. Eyebrow (12 px uppercase, `text/60`, 0.12em tracking) — optional
2. `h2` headline
3. Lead paragraph (20 px, `text/60`)
4. Body paragraphs / lists / cards
5. Single CTA (Secondary or Ghost — never a second Primary on a non-hero section)

Items 1 → 2: 12 px gap. 2 → 3: 16 px gap. 3 → 4: 32 px gap.

## Lists

- Indent: 24 px from the surrounding container
- Vertical gap between items: 8 px
- Bullets: small disc, `text` at 40% opacity
- Numbered lists: ink colour for numerals, weight 600

## Body Copy Specifics

- Default paragraph: 16 px Open Sans, weight 400, `text` at 60% opacity, line-height 1.7
- Max measure: ~ 65 characters (rely on the 672 px / 768 px containers)
- Inline emphasis lifts to full `text` via `<strong>`

## Rules

- Mobile-first: design at 375 px first, then enhance.
- Layout shifts are column → row only. Never re-order content arbitrarily between breakpoints.
- Lists, paragraphs, and headings all stay on the cream surface — no inset content boxes.
- Do not add background images, illustrations, or hero photography behind text. Keep the cream + crosshatch as the only background.

---

## Source file: `dropdown.md`

# Dropdown

> Dependencies: `colors.md`, `radius.md`, `shadows.md`, `borders.md`, `inputs.md`

## Trigger

Use the Secondary or Ghost button variant from `buttons.md`. Add a chevron icon on the right.

### Chevron
- Size: 16 × 16 px
- Spacing: 6 px left margin from label
- Color: inherits from button text

## Menu Container

- **Background:** `surface` (`#F4F4F1`)
- **Border:** 1 px `text/10`
- **Radius:** 6 px
- **Shadow:** shadow-md (see shadows.md) (the only place besides modals/popovers where shadow is permitted)
- **Z-index:** elevated above all in-flow content
- **Padding:** 8 px
- **Min width:** matches the trigger; max width 320 px

## Menu Item

- Layout: horizontal flex, items vertically centred, 12 px gap, full-width
- Padding: 8 px horizontal, 8 px vertical
- Radius: 4 px
- Font: 14 px Open Sans, weight 500
- Color: `text`
- Hover background: `text/5`
- Active background: `text/10`
- Focus-visible: 2 px outline `primary`, inset
- Transition: `colors` 150 ms

## Variants

### With Divider
Insert a 1 px `text/10` rule between groups. Group label (eyebrow style: 11 px uppercase, `text/40`, 0.12em letter-spacing) sits 8 px above its group.

### With Header
Header padding: 12 px / 8 px, bottom hairline `text/10`. Name: 14 px Inter, weight 600, `text`. Email/meta: 12 px Open Sans, `text/40`, truncated.

### With Icons
Icon: 16 × 16 px, 8 px right of icon to label, `text/60` colour. Hover lifts the icon to `text` along with the label.

### With Checkbox / Radio
Use `radios-checkboxes-toggle.md` specs. The control sits to the left of the label.

### With Search
Top of the menu: a single input from `inputs.md` (size: small).

### Scrollable
Max height 240 px, vertical scroll, custom scrollbar uses `text/20`.

## States | State | Appearance | |---|---| | Trigger focused | 2 px outline `primary`, 2 px offset | | Item hover | background `text` at 5% opacity | | Item active / open | `text/10` background | | Item disabled | `text/30` text, cursor not-allowed, no hover |

## Prohibited

- No saturated brand-coloured menus or items.
- No drop shadow heavier than shadow-md (see shadows.md).
- No animation other than fade-in / out.

---

## Source file: `icon-shapes.md`

# Icon Shapes

> Dependencies: `colors.md`, `radius.md`

Icon containers (the round / square frames that hold a foreground icon) are used sparingly in this design — usually for feature-list bullets or social links. Default to the **Neutral** variant.

## Core Specs

- Box-sizing: border-box
- Icon perfectly centred
- Circle: the default radius
- Rounded square: 6 px for sizes MD/LG/XL; 4 px for XS/SM
- No shadow

## Sizes | Size | Container | Icon | |---|---|---| | XS | 24 × 24 px | 14 × 14 px | | SM | 32 × 32 px | 16 × 16 px | | MD (default) | 40 × 40 px | 20 × 20 px | | LG | 48 × 48 px | 24 × 24 px | | XL | 56 × 56 px | 28 × 28 px |

## Variants

### Neutral (default)
- Shape: circle
- Background: `transparent`
- Border: 1 px `text/10`
- Icon colour: `text/60`

### Solid Ink
- Shape: circle
- Background: `primary`
- Border: none
- Icon colour: `surface`

### Hairline (for inline social-link rows)
- Shape: circle
- Background: `transparent`
- Border: 1 px `text/20`
- Icon colour: `text`
- Hover: border `text`, no background change

### Status (success / warning / danger / info)
- Shape: circle
- Background: matching `*-soft`
- Border: 1 px matching status token
- Icon colour: matching status token

## Prohibited

- No drop shadows.
- No filled brand-coloured circles for non-status content.
- No mix of square and circle icon shapes within the same row/list.

---

## Source file: `inputs.md`

# Inputs

> Dependencies: `colors.md`, `radius.md`, `borders.md`, `typography.md`

Inputs match the rest of the system — flat, hairline-bordered, no fill.

## Core Specs

- **Display:** block, full-width inside its container
- **Background:** `transparent` (cream shows through)
- **Border:** 1 px solid `text/10`
- **Radius:** 4 px
- **Shadow:** **none**
- **Family:** Open Sans
- **Font size:** 16 px (prevents iOS zoom)
- **Color:** `text`
- **Placeholder color:** `text/40`
- **Padding:** 12 px horizontal, 10 px vertical
- **Transition:** 150 ms on border-color only

## Label

- Block, 14 px Open Sans, weight 500, `text` colour
- Margin-bottom: 8 px
- `htmlFor` always matches the input `id`

## Helper Text

- 12 px, `text/40`, sits 6 px below the input

## States

### Default
- Border: `text/10`

### Hover
- Border: `text/30`

### Focus-visible
- Outline: 2 px `primary`, 2 px offset (matches buttons — same focus ring across the whole system)
- Border colour stays at `text/30` underneath

### Filled
- Border: `text/30`

### Success
- Border: `success` (1 px)
- Helper text: `success`

### Error
- Border: `danger` (1 px)
- Helper text: `danger`

### Disabled
- Background: `text/5` (very faint cream wash)
- Border: `text/10`
- Text & placeholder: `text/30`
- Cursor: `not-allowed`

## Input with Icon

- Container is `relative`
- Icon: 16 × 16 px, `text/40`, absolutely positioned
- Leading icon: `left-3`, input adds `pl-10`
- Trailing icon: `right-3`, input adds `pr-10`

## Textarea

- Same specs as input
-  (128 px), resize `vertical` only
- Padding: 12 px

## Prohibited

- No filled grey input backgrounds.
- No coloured focus ring other than `primary`.
- No animated borders.
- No floating-label patterns — labels sit above the input.

---

## Source file: `layout.md`

# Layout & Spacing

> Dependencies: `colors.md`, `typography.md`

## Spacing Rhythm

Base unit: **4 px** (`--spacing`). Use multiples; the canonical scale for this skill is: | Step | Value | |---|---|---| | `xs` | 4 px | `1` | | `sm` | 8 px | `2` | | `md` | 16 px | `4` | | `lg` | 24 px | `6` | | `xl` | 32 px | `8` | | `2xl` | 64 px | `16` | | `3xl` | 96 px | `24` |

## Hero Spacing (the canonical rhythm of the landing page) | Gap | Value | |---|---| | Avatar → `h1` | 24 px | | `h1` → lead paragraph | 32 px | | Lead paragraph → CTA | 64 px | | Page outer padding | 16 px mobile, 32 px ≥ small |

These exact gaps are mandatory on any hero/landing surface — they are the "feel" of the project.

## Containers | Purpose | Max width | Notes | |---|---|---| | Hero / landing column | **672 px** | Default for any page-level main content | | Long-form prose | 768 px | About / case-study text | | Works grid | 1024 px | Project thumbnails, 2- or 3-column | | Absolute outer cap | 1280 px | Only for full-bleed gallery rows |

Every container is centered with horizontal padding . Never let content touch the viewport edge.

## Page Scaffold (use this on every full-page route)

This scaffold is the single source of truth — copy it, do not invent variations.

## Section Pattern (when more than the hero is needed)

When a page has follow-up sections (Works, About, Contact):

- **No alternating section backgrounds.** Every section sits on `surface`.
- **Vertical padding:** 96 px between sections, 128 px before the first follow-up section after a hero.
- **Section header pattern:** small uppercase eyebrow (12 px, `text/60`, 0.12em letter-spacing) → `h2` headline → 48 px gap → section content.
- **Section dividers** (if needed): a single 1 px hairline at `text/10`, full container width. Prefer pure whitespace over dividers.

## Background Treatment

- **Always** render the 45°/-45° crosshatch on full-page routes (see scaffold above).
- The crosshatch sits at z-index -10 with pointer-events none so it never interferes with interaction.
- **Never** stack additional textures, noise, blobs, gradient meshes, or images on top. The crosshatch is the only decorative layer this design uses.
- Hero photography (e.g. project thumbnails) lives **inside** content blocks, never as a section background.

## Motion & Animation

- **Default to none.** This is a quiet design — animation should be the exception, not the rule.
- When animating, use CSS transitions on `colors`, `opacity`, or `transform` only. 150 ms (`--default-transition-duration`) with the default cubic-bezier.
- One acceptable orchestrated moment per page-load: stagger the avatar → `h1` → paragraph → CTA fade-in with `40 ms` delay between elements. No more.
- Never animate the crosshatch background.
- Never use parallax, scroll-jacking, or auto-playing motion.

## Visual Depth

- The design is intentionally **flat**. Depth comes from typography weight contrast (900 vs 400) and from the 60 % opacity of body copy, not from shadows or gradients.
- Avatar gets shadow-sm (see shadows.md). Nothing else carries elevation.

## Must

- Hero rhythm: 24 / 32 / 64 px sequence between avatar / h1 / paragraph / CTA.
- Crosshatch background present on every full-page route.
- One Primary CTA per view, centered.
- Containers always centered, never full-bleed for text content.
- Mobile padding, scales to at small breakpoint and above.

---

## Source file: `lists.md`

# Lists

> Dependencies: `colors.md`, `typography.md`

## Core Specs

- **Item spacing:** 8 px vertical gap between items (12 px for prose lists with paragraph-length items)
- **Text:** `text/60`, 16 px Open Sans, line-height 1.7
- **Indent from container:** 24 px

## Bulleted Lists (`<ul>`)

- Bullet: small filled disc, `text/40` colour
- Custom bullets allowed (e.g. an em-dash for a more editorial feel) — must stay within the `text/40` colour and same size as the line height permits

## Numbered Lists (`<ol>`)

- Numerals: Open Sans, weight 600, `text` colour, 1 ch wider gutter than the list text

## List Icons (for feature checklists)

- Size: 16 × 16 px, no shrink
- Spacing: 8 px right margin between icon and text
- Active / featured icon: `text` (full ink)
- Neutral icon: `text/40`
- Status icon: matching status token (`success`, `danger`, etc.) — small dot to the left of the text

## Inactive / Completed Items

- Strikethrough on the text, colour stays at `text/40`

## Definition Lists (`<dl>`)

- Term (`<dt>`): 14 px Open Sans, weight 600, `text`
- Definition (`<dd>`): 14 px, `text/60`, indented 24 px from term

## Pattern

## Rules

- Never colour list text with brand or accent.
- Never use heavy bullet styles (filled squares, large discs).
- Keep nested lists shallow — two levels maximum.

---

## Source file: `modals.md`

# Modals

> Dependencies: `colors.md`, `radius.md`, `shadows.md`, `buttons.md`, `inputs.md`

Modals are the one place this design admits a real shadow — they need to feel as if they're floating above the page.

## Core Specs

### Overlay (Backdrop)
- Fixed, full-screen
- Z-index: 40
- Background: `rgba(12, 12, 9, 0.50)` (the ink colour at 50 % opacity, so the cream tint persists)
- Optional `backdrop-blur-sm`

### Content Container
- Background: `surface` (`#F4F4F1`)
- Radius: 6 px
- Shadow: shadow-lg (see shadows.md)
- Border: 1 px `text/10`
- Padding: 24 px
- Max width: 512 px (default), 640 px for form modals
- Centered both axes

## Anatomy

### Header
- Title: 18 px Inter, weight 600, `text` colour
- Optional bottom hairline: 1 px `text/10`, 16 px below the title
- Close button: Ghost button (16 × 16 px icon, `text/40`, hover `text`), positioned top-right

### Body
- Vertical padding: 24 px
- Vertical spacing between elements: 16 px
- Text: 14–16 px Open Sans, line-height 1.625, `text/60`

### Footer
- Top hairline: 1 px `text/10`, optional
- Padding-top: 24 px
- Layout: horizontal flex, items at trailing edge, 12 px gap
- Always one Primary action, optionally one Secondary or Ghost to the left

## Variants

### Default (information)
Header + body + footer with Primary / Secondary actions.

### Confirmation Pop-up
Centered text, optional 48 × 48 px icon at the top, no header divider, footer collapses into two stacked buttons on mobile.

### Form Modal
Body contains inputs from `inputs.md`. 16 px gap between fields. The submit Primary lives in the footer.

## Rules

- Backdrop is the only place where a near-black tint is allowed at large surface area.
- Content surface is always `surface` cream — never white.
- Use shadow-lg (see shadows.md) only here. Cards and dropdowns must not borrow it.
- Accessibility: `role="dialog"`, `aria-modal="true"`, focus trap, `Escape` closes.
- Close button must be present and reachable by keyboard.

---

## Source file: `pagination.md`

# Pagination

> Dependencies: `colors.md`, `radius.md`, `borders.md`, `typography.md`

## Container

- Layout: inline flex with `-1px` overlap between items so borders read as one continuous line
- Font: 14 px Open Sans, weight 500

## Pagination Item

- Layout: horizontal flex, items centred both axes
- Size: 36 × 36 px
- Color: `text/60`
- Background: `transparent`
- Border: 1 px `text/10`
- Hover: background `text` at 5% opacity, label lifts to `text`
- Transition: `colors` 150 ms
- Focus-visible: 2 px outline `primary`, inset

## Previous / Next Buttons

- Padding: 12 px horizontal, height 36 px
- Label "Previous" / "Next" with chevron (16 × 16 px, `currentColor`) on the leading/trailing side, 8 px gap
- First item: 6 px radius on inline-start corners
- Last item: 6 px radius on inline-end corners

## Active Page Item

- Background: `primary`
- Color: `surface`
- Border: 1 px `primary`
- Hover: stays `primary` (no change)

## Disabled (e.g. Prev on page 1)

- Color: `text/20`
- Cursor: `not-allowed`
- No hover

## Rules

- Display as inline flex with `-1px` child overlap.
- One active item only.
- Always include Previous and Next, even on the first/last page (disabled state).
- All items must be reachable by keyboard.

---

## Source file: `radios-checkboxes-toggle.md`

# Radios, Checkboxes & Toggles

> Dependencies: `colors.md`, `radius.md`, `borders.md`

All three controls use the same focus treatment as buttons (2 px `primary` outline, 2 px offset) so the system reads as one.

## Checkbox

- Size: 16 × 16 px
- Radius: 4 px
- Border: 1 px `text/30`
- Background: `transparent`
- Checked background: `primary`
- Checked check mark: `surface`, 1.5 px stroke
- Hover (unchecked): border `text`
- Focus-visible: 2 px outline `primary`, 2 px offset

### Disabled
- Border: `text/10`
- Background: `text/5`
- Check mark: `text/30`

## Radio

- Size: 16 × 16 px
- Radius: 9999 px (full)
- Border: 1 px `text/30`
- Background: `transparent`
- Checked: 1 px border `primary`, inner 8 × 8 px `primary` dot centered
- Hover (unchecked): border `text`
- Focus-visible: 2 px outline `primary`, 2 px offset

### Disabled
- Border: `text/10`
- Inner dot (if checked): `text/30`

Group all radios under the same `name` attribute.

## Toggle

### Track
- Size: 36 × 20 px
- Radius: 9999 px (full)
- Background: `text/15` (off), `primary` (on)
- Transition: `background-color` 150 ms
- Focus-visible (on the wrapper): 2 px outline `primary`, 2 px offset

### Thumb
- Size: 16 × 16 px
- Radius: 9999 px (full)
- Background: `surface`
- Position: 2 px from the leading edge (off), 2 px from the trailing edge (on)
- Transition: `transform` 150 ms

### Disabled
- Track: `text/5`
- Thumb: `text/20`
- Cursor: `not-allowed`

## Label Pattern

- All controls sit in a horizontal flex, items vertically centred, 8 px gap row with their label
- Label: 14 px Open Sans, weight 500, `text` colour
- Helper text below: 12 px Open Sans, `text/40`, 4 px below the label
- `id` of the control matches the `htmlFor` of the label

## Prohibited

- No coloured focus rings (no brand-blue, no green). All three controls share the `primary` outline.
- No animated check marks beyond the natural fade.
- No size variants larger than the defaults — the design is intentionally compact.

---

## Source file: `radius.md`

# Border Radius

| Token | Value | Default usage |
|---|---|---|
| `none` | 0px | Section dividers, full-bleed image edges |
| `card` | **2px** | **All cards** — every card and card-like container |
| `sm` | 4px | Inputs, badges, code blocks, small chips |
| `md` (default) | **6px** | Buttons, modals, dropdowns, tooltips |
| `full` | 9999px | Avatars, dot indicators, icon-only round buttons |

## Rules

- **Cards use 2px border radius only** — never 6px, 4px, or pill radius on cards
- **6px** applies to rectangular interactive controls (buttons, modals, popovers) — not cards
- Avatars and dot indicators are **always** `full`. No squircles, no rounded squares for profile imagery
- Never use 8px, 10px, 12px, 16px, or 20px radii — they pull the design toward shadcn/Material territory and break the minimal feel
- A single component must use one radius value. Card shells use `card` (2px); inner inset images inside a card match the card radius (2px)
- Do not apply button/modal radius (`md`) to cards

---

## Source file: `shadows.md`

# Shadows

This design is **flat by intent.** The only routinely-used shadow is shadow-sm (see shadows.md) on the avatar disc. Everything else should rely on whitespace, hairline borders, and typographic weight contrast for separation. | Token | CSS value | When (if ever) to use | |---|---|---| | `none` | — | Default for buttons, cards, sections, hero surfaces | | `0 1px 2px 0 rgb(0 0 0 / 0.05)` | Avatar disc only | | `0 4px 6px -1px rgb(0 0 0 / 0.08), 0 2px 4px -2px rgb(0 0 0 / 0.05)` | Floating menus (dropdown, popover) when they overlay content | | `0 10px 20px -8px rgb(0 0 0 / 0.10)` | Modal dialog overlay only |

## Rules

- **Buttons have no shadow.** Not the primary, not the secondary, never. No glints, no insets, no glows.
- **Cards have no shadow.** Use a 1 px hairline border at `text/10` instead.
- **Sections have no shadow.** Whitespace separates sections.
- **Avatar gets shadow-sm (see shadows.md)** — that's the only place the design admits elevation on first-paint surfaces.
- **Overlays** (dropdown, popover, modal) may use shadow-md (see shadows.md) / shadow-lg (see shadows.md) because they sit above content and need to read as floating. They are the only exception.
- Never stack multiple shadow tokens on one element.
- Never use coloured shadows.

---

## Source file: `sidebars.md`

# Sidebars

> Dependencies: `colors.md`, `radius.md`, `borders.md`, `typography.md`

Sidebars are uncommon in a minimal portfolio (most pages are single-column hero scaffolds). When one is needed — usually for a long case-study or dashboard-style admin view — keep it lean.

## Core Specs

- **Background:** `surface` (cream — the same as the page; the sidebar reads as a column, not a separate surface)
- **Right border** (for left-sidebar): 1 px `text/10`
- **Width:** 240 px desktop, 100 % mobile (slide-in)
- **Padding:** 12 px horizontal, 24 px vertical

## Anatomy

### Outer Container
- Hidden below `md` (768 px) breakpoint, replaced by a slide-in drawer with a hamburger trigger
- Trigger: ghost button, 24 × 24 px icon

### Inner Wrapper
- Full height, vertical scroll overflow
- Sticky if page is long: `position: sticky; top: 0`

### Section Header (eyebrow)
- 11 px Open Sans, weight 600, uppercase, 0.12em letter-spacing, `text/40`
- Margin-bottom: 8 px

### Navigation List
- Vertical spacing: 4 px between items

### Navigation Item
- Layout: horizontal flex, items vertically centred, 12 px gap, full-width
- Padding: 8 px horizontal, 8 px vertical
- Radius: 6 px
- Font: 14 px Open Sans, weight 500, `text/60`
- Hover: background `text` at 5% opacity, `text` text
- Transition: `colors` 150 ms
- Icon: 16 × 16 px, inherits text colour

### Active Item
- Background: `text/5`
- Text: `text`
- 2 px left ink bar (`primary` colour, full height of the item) sitting flush with the inline-start edge — this is the active indicator

### Separator
- 24 px top margin, 1 px hairline `text/10`, 16 px top padding before the next group

### Bottom CTA Card (optional)
- Padding: 16 px
- Border: 1 px `text/10`
- Radius: 6 px
- Background: transparent
- Contains a short label and a Secondary button

## Rules

- Sidebar background is the same cream as the page — separation comes from the 1 px hairline alone.
- Active state is text + a 2 px ink bar — never a saturated colour fill.
- Multi-level menus indent with 24 px additional left padding. Two levels max.
- Keyboard navigation: arrow keys to move, `Enter` to activate.

---

## Source file: `tables.md`

# Tables

> Dependencies: `colors.md`, `radius.md`, `borders.md`, `typography.md`

Tables are built from hairlines and whitespace — no zebra striping, no shadows, no rounded cell fills.

## Wrapper

- Horizontal scroll overflow on small screens
- Background: `transparent` (cream surface shows through)
- Radius: 6 px — applied to the wrapper, with overflow hidden so cell borders clip
- Border: 1 px `text/10`
- No shadow

## Table Element

- `width: 100%`, left-aligned (right-aligned for RTL)
- Font: 14 px Open Sans, `text/60`

## Table Head

- Font: 11 px Open Sans, weight 600, `text/60`, **uppercase**, 0.08em letter-spacing
- Background: `transparent`
- Bottom border: 1 px `text/10`
- Cell padding: 24 px horizontal, 12 px vertical

## Table Body

- Row background: `transparent`
- Row bottom hairline: 1 px `text/10` (omit on the last row to avoid doubling with the wrapper)
- Row hover: background `text` at 5% opacity (optional)
- Row header (`<th scope="row">`): weight 500, `text` colour, white-space nowrap
- Cell padding: 24 px horizontal, 16 px vertical

## Cell Content

- Numerics: tabular figures, right-aligned
- Status pills: small pill badges per `badges.md`
- Truncation: `text-ellipsis whitespace-nowrap` on cells with `max-width`

## Rules

- No zebra striping.
- No drop shadow.
- Last row: omit bottom hairline.
- Row header: always `scope="row"`.
- Sortable columns: chevron icon (12 × 12 px, `text/40`) right of header label, hover lifts label to `text`.
- All colours via tokens — no raw hex.

---

## Source file: `tabs.md`

# Tabs

> Dependencies: `colors.md`, `radius.md`, `borders.md`, `typography.md`

The default tab pattern in this design is the **Underline** variant — it sits flat against the surface and reads as type-first navigation.

## Core Specs

- **Typography:** 14 px Open Sans, weight 500
- **Default text colour:** `text/60`
- **Active text colour:** `text`
- **Transition:** `colors` 150 ms

## Variants

### 1. Underline (default — use this 95 % of the time)

**Wrapper:** bottom hairline `text/10`, full container width.

**Tab Item:**
- Padding: 16 px horizontal, 12 px vertical
- Bottom border: 2 px transparent
- Background: transparent | State | Appearance | |---|---| | Active | text `text`, bottom border `primary` | | Inactive | text `text/60`; hover → text `text` | | Disabled | text `text/30`, cursor not-allowed, no hover | | Focus-visible | 2 px outline `primary`, 2 px offset |

### 2. Pills (for compact toolbars only)

**Tab Item:**
- Padding: 12 px horizontal, 8 px vertical
- Radius: 6 px
- No shadow | State | Appearance | |---|---| | Active | `primary` background, `surface` text | | Inactive | `text/60`; hover → background `text` at 5% opacity, `text` text | | Disabled | `text/30`, cursor not-allowed |

### 3. Full-Width Segmented (for two- or three-option pickers)

Behaves like a button group:
- Wrapper: 1 px `text/10`, 6 px radius
- Items overlap with `-1px` left margin
- Active: `primary` background, `surface` text
- Inactive: transparent background, `text/60` text

## Tabs with Icons

- Icon: 16 × 16 px
- Spacing: 8 px right margin from icon to label
- Layout: inline flex, items vertically centred
- Icon inherits the tab's text colour

## Prohibited

- No coloured underline (no brand-blue/green underline). The active underline is always `primary` (ink).
- No more than 5 tabs in a single bar — switch to a dropdown instead.
- No shadow on any tab variant.

---

## Source file: `tooltips-popovers.md`

# Tooltips & Popovers

> Dependencies: `colors.md`, `radius.md`, `shadows.md`, `borders.md`

## Tooltips

### Core Specs
- Padding: 8 px horizontal, 6 px vertical
- Font: 12 px Open Sans, weight 500
- Radius: 4 px
- Shadow: shadow-sm (see shadows.md) (only here for tooltips)
- Transition: `opacity` 150 ms
- Max width: 240 px
- Pointer offset from anchor: 8 px

### Default (Dark — the only variant)
- Background: `primary` (`#0C0C09`)
- Text: `surface`
- Border: none

This design uses one tooltip variant. Don't introduce a "light" tooltip — it would compete with cards and dropdowns at the same elevation.

## Popovers

### Core Specs
- Background: `surface`
- Radius: 6 px
- Shadow: shadow-md (see shadows.md)
- Border: 1 px `text/10`
- Transition: `opacity` 150 ms
- Max width: 320 px

### Header / Title
- Padding: 12 px horizontal, 8 px vertical
- Background: `transparent`
- Bottom hairline: 1 px `text/10`
- Font: 14 px Inter, weight 600, `text`

### Body / Content
- Padding: 12 px horizontal, 12 px vertical
- Font: 14 px Open Sans, `text/60`, line-height 1.6

### Footer (optional)
- Padding-top: 12 px above a top hairline `text/10`
- Layout: horizontal flex, items at trailing edge, 8 px gap, contains a Secondary or Ghost button

## Arrows (optional)

- Size: 8 × 8 px rotated 45°
- Background must match the tooltip / popover background (`primary` for tooltips, `surface` for popovers)
- Border on popover arrow: 1 px `text/10` on the two visible edges
- Position via `clip-path` or `transform` to align with the anchor

## Rules

- Tooltips are always dark (`primary` ink). Popovers are always cream.
- Never both visible at once on the same anchor.
- Show on hover after a 200 ms delay; hide on mouse-leave with no delay.
- Keyboard: tooltips appear on focus, hide on blur and `Escape`.
- ARIA: `role="tooltip"`; popover triggers use `aria-haspopup="dialog"` and `aria-expanded`.

---

## Source file: `typography.md`

# Typography

> Dependencies: `colors.md`

Type does the heavy lifting in this design — colour and layout intentionally stay quiet so the words can lead.

## Font Stack

| Role | Family | CSS variable |
|---|---|---|
| Display (hero `h1`, large numerics) | **Inter** | `--font-display: var(--font-inter), ui-sans-serif, system-ui, sans-serif` |
| Body / UI (paragraphs, buttons, labels) | **Open Sans** | `--font-sans: var(--font-open-sans), ui-sans-serif, system-ui, sans-serif` |
| Code / mono | **Inconsolata** | `--font-mono: var(--font-inconsolata), ui-monospace, SFMono-Regular, monospace` |

All three are loaded via the project's standard web-font loading mechanism. Never introduce a serif, slab, or script. Never override the body default of Open Sans.

## Core Rules

- **Do not override heading sizes** with arbitrary `text-[…]` classes unless a page-type rule below explicitly allows it
- **Semantic HTML:** Use `h1`–`h6` in order, never skip levels

## Hero Headline (the project's signature)

The page-level `h1` always uses these settings — this is the visual anchor of the design.

| Property | Value |
|---|---|
| Font family | `--font-display` (Inter) |
| Font weight | **900 (black)** |
| Letter-spacing | `-0.025em` |
| Color | `primary` (`#0C0C09`) |
| Line-height | `1.1` |
| Margin-bottom | `32px` |

### Responsive size (hero `h1` only)

| Breakpoint | Size |
|---|---|
| Mobile (default) | **32px** |
| Tablet (≥768px) | **40px** |
| Desktop (≥1024px) | **60px** |

There is **only one** element on a page that uses the hero black weight at display scale. Do not inflate beyond 60px desktop.

## Heading Scale (everything else)

All sub-headings use Inter at weight 700 (bold), tight tracking, ink-coloured.

| Element | Mobile | Tablet (≥768px) | Desktop (≥1024px) | Line-height | Margin-bottom |
|---|---|---|---|---|---|
| `h2` | 28px | 36px | 44px | 1.15 | 24px |
| `h3` | 22px | 26px | 30px | 1.2 | 20px |
| `h4` | 20px | 22px | 24px | 1.25 | 16px |
| `h5` | 18px | 18px | 20px | 1.4 | 12px |
| `h6` | 14px (uppercase, `0.08em` tracking) | 14px | 14px | 1.4 | 8px |

Never reduce line-height below `1.1` for any heading. Never skip heading levels.

## Page-Type Heading Rules

### Dashboard pages

- Set `data-surface="dashboard"` on the root app shell (e.g. `<main>` or layout wrapper).
- **All headings** (`h1`–`h6`) must stay **compact: maximum 28px, preferably 24px**.
- Page title (`h1`): **24px** preferred.
- Section titles (`h2`): **22–24px**.
- Panel / card titles (`h3`–`h4`): **20–24px**.
- Never use display-scale marketing sizes in dashboard sidebars, tables, stats, or settings.

### E-commerce pages (app surfaces)

- Set `data-surface="ecommerce-app"` on the storefront layout root.
- **All headings outside the storefront hero** follow the same compact rule as dashboard: **max 28px, prefer 24px**.
- Product grid titles, category headers, cart, and footer sections: **20–24px**.
- Do not use oversized `text-[…]` utilities on e-commerce app headings.

### E-commerce storefront hero (exception)

- Only the **above-the-fold marketing hero** on an e-commerce landing page may use the full **Landing Heading Scale** (`h1` up to 60px desktop).
- Mark the hero wrapper with `data-section="storefront-hero"` inside `data-surface="ecommerce-app"`.
- Hero supporting copy stays at **20px** leading paragraph size; hero `h2` subheads max **44px** desktop.
- All sections below the hero revert to compact e-commerce heading rules.

## Paragraphs

### Hero / Lead Paragraph (the one directly under the hero `h1`)
- Family: `--font-sans` (Open Sans)
- Weight: 400
- Color: `text/60`
- Line-height: `1.625`
- Margin-bottom: `64px`
- Responsive size: **18px → 20px → 24px**
- Max line length: ≤ 60 characters (rely on container)

### Standard Body Paragraph
- Size: 16px
- Weight: 400
- Color: `text/60`
- Line-height: 1.7
- Max width: ~65 characters

### Small Supporting Copy
- Size: 14px
- Weight: 400
- Color: `text/40`
- Use for captions, timestamps, helper text, legal copy.

## UI Labels

| Context | Family | Size | Weight | Notes |
|---|---|---|---|---|
| Primary CTA label | Open Sans | 16px | 600 (semibold) | Cream colour on dark button |
| Secondary / ghost button label | Open Sans | 14px | 500 | Ink colour |
| Input label | Open Sans | 14px | 500 | Ink colour, 8px below sits the input |
| Caption / meta | Open Sans | 12–14px | 500 | `text/40` |
| Eyebrow / section kicker | Open Sans | 12px, uppercase, `0.12em` tracking | 600 | `text/60` |

Never apply paragraph line-height (1.7) to control labels.

## Links

- **Inline links in body copy:** ink colour, 1px underline at `text/40`, underline removed on hover.
- **Standalone CTA links:** ink colour, weight 500, underline always visible, hover shifts underline to full ink.
- Never colour links with brand or accent hues.

## Emphasis

- `<strong>` lifts inline copy from `text/60` back to full ink — that's the whole emphasis mechanism.
- `<em>` is for tone only.
- Set in ALL CAPS only for ≤ 24-character labels (eyebrows, button groups), with `0.08–0.12em` tracking, 12 or 14px.

## Prohibited

- No coloured text for paragraphs (status, brand, accent).
- No light weights below 400 — they vanish on the cream surface.
- No condensed or expanded variants of Inter / Open Sans.
- No drop-shadows on text.
- No two hero-scale headlines on the same page.
- No viewport-based or oversized display sizes (e.g. `text-[120px]`, `12vw`) on headings.