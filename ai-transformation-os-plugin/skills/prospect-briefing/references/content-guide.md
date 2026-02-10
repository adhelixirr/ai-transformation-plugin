# Briefing Content Guide

## Document Structure

Every briefing follows a four-section narrowing funnel: **Industry → Company → Role → Action**. Each section builds credibility for the next.

## Section 1: The Forces Reshaping [Industry]

**Purpose**: Establish credibility by demonstrating deep understanding of why their specific industry faces a unique AI transformation challenge.

**Framework**: Three Forces (Pace × Breadth × Depth)

**Writing approach**:
- Open by addressing the prospect by first name and acknowledging their experience
- Apply each force specifically to their industry (not generic AI commentary)
- Include 1-2 industry-specific data points from research
- Close with the compound effect insight

**Tone**: Authoritative but not lecturing. You're sharing a lens, not teaching a class.

**Key elements**:
- `intro`: Personal opening connecting to prospect's background
- `body`: Why traditional playbooks break for this industry
- `heading`: "Three Forces Operating Simultaneously"
- 3x `numbered` points (PACE, BREADTH, DEPTH) — each applied to their industry
- `insight` (warm): The compound effect
- `heading`: "What This Means for [Industry] Specifically"
- 1-2 `body` paragraphs with industry data points

## Section 2: What This Means for [Company]

**Purpose**: Show you've done your homework on their specific organization. Place them on the maturity curve and flag relevant failure patterns.

**Framework**: Maturity Model + Failure Patterns

**Writing approach**:
- Open with a hypothesis about where they sit (Exploring → Piloting → Scaling → Operating) based on public signals
- Explain the Pilot-to-Scale gap (most companies are here)
- Select 4-5 failure patterns most relevant to their situation
- Frame patterns as "worth watching for" not "you're failing at"

**Tone**: Diagnostic, not judgmental. Frame as patterns seen across many organizations.

**Key elements**:
- `intro`: Maturity hypothesis with evidence from research
- `heading`: "The Pilot-to-Scale Gap" (or equivalent)
- 1-2 `body` paragraphs
- `heading`: "Patterns Worth Watching For" (or "Five Challenges Worth Examining")
- 4-5x `numbered` points — each a specific failure pattern applied to their situation
- `insight` (cool): Reframe that these are diagnostic markers, not inevitabilities

## Section 3: Leading Through the Shift

**Purpose**: Make it personal. Address what transformation requires of someone in their specific role. This is where the prospect feels "this is about ME."

**Framework**: Augmented Professional + Leadership Operating Model

**Writing approach**:
- Open by naming their unique position and why their background is an advantage
- The leadership signal: personal workflow redesign as the strongest predictor
- "The Augmented [Role]" — table showing current vs. augmented state across 4-5 dimensions relevant to their role
- Identity shift: how to guide their people through it

**Tone**: Personal, empathetic, forward-looking. Paint a vision they want to be part of.

**Key elements**:
- `intro`: Why their specific background is an advantage
- `heading`: "The Leadership Signal That Matters Most"
- 2-3 `body` paragraphs on personal workflow redesign
- `heading`: "The Augmented [Short Title]"
- `body`: Setup for the table
- `table`: 3 columns (Dimension, Current State, Augmented State), 4-5 rows relevant to their role
- `insight` (warm): Key identity shift insight
- `heading`: "Guiding Your Organization Through the Identity Shift"
- 2-3 `body` paragraphs on the Five Thresholds approach (honor → encounter → reimagine)

## Section 4: Where I'd Focus First

**Purpose**: Provide 3 concrete, sequenced priorities. Each one naturally leads to "...and I could help you do this."

**Framework**: Outcome-First Strategy + Operating System layers

**Writing approach**:
- Open with "If I were sitting in your chair..." framing
- 3 priorities, deliberately sequenced (each builds on the previous)
- Each priority: numbered point (gold accent) + 1-2 body paragraphs + insight box with diagnostic question
- Priorities should map to the most relevant Operating System layers for their situation

**Tone**: Practical, specific, actionable. Not abstract consulting-speak.

**Key elements**:
- `intro`: "If I were sitting in your chair" framing
- For each priority:
  - `numbered` (accent: "gold"): Priority title only (no body in the numbered point)
  - 1-2 `body` paragraphs explaining the priority
  - `insight` (cool): A diagnostic question they can ask themselves

## Section 5: A Conversation Worth Having (Closing)

**Purpose**: Soft CTA. Reference the broader framework as deeper work, invite a 30-minute conversation.

**Key elements**:
- 3x `closing` paragraphs:
  1. Restate the inflection point and their strong foundation
  2. Reference the full Operating System (10 layers, 75 failure patterns) as deeper work
  3. Invite a 30-minute conversation to explore which themes resonate
- `signature` element

## General Writing Principles

- **Use the prospect's first name** in the opening of Section 1 and the closing
- **Never be generic** — every paragraph should contain something specific to their industry, company, or role
- **Frame AI as "digital coworker, not software"** and adoption as "social contract renegotiation"
- **Avoid jargon** — write for a senior executive, not a technologist
- **Use em dashes (—) not hyphens** for asides
- **Use "smart quotes"** (" ") not straight quotes
- **Data points**: Include 3-5 industry-specific statistics from research
- **Diagnostic questions**: Include at least 3 questions the prospect can ask their own team
- **Length target**: The full JSON should produce a 6-8 page PDF

## JSON Config Template

The JSON must include:
```
{
  "prospect": { "name", "title", "company", "short_title" },
  "cover": { "main_title_line1", "main_title_line2", "subtitle_line1", "subtitle_line2" },
  "sections": [ array of 5 sections, each with "title", "subtitle", "elements" ]
}
```

Element types: `intro`, `body`, `closing`, `heading`, `numbered` (with number, title, body, optional accent:"gold"), `insight` (with text, style:"warm"|"cool"), `table` (with headers, rows, optional col_widths), `spacer`, `page_break`, `signature`, `hr`
