---
name: client-pov
description: |
  Create client-specific points of view, proposal sections, and strategic recommendations using Elixirr's AI transformation frameworks. Researches a client's industry, company, and situation, then generates a tailored document demonstrating how Elixirr would approach their AI transformation. Use when anyone mentions "POV", "point of view", "proposal", "recommendation for [client]", "how would we approach", "what would we recommend", "client-specific", or any request to create strategic content tailored to a specific organization.
---

# Client POV Generator

## Workflow

### 1. Collect Context

Gather the essentials (ask if missing):
- **Company name** (legal name)
- **Industry** (what sector, primary business)
- **Known challenges** (what you know about their AI transformation challenges, competitive pressures, or strategic goals)
- **Engagement context** (RFP, pitch meeting, kickoff, deeper engagement planning?)
- **Desired output format** (short POV 2-3 pages, full POV 5-8 pages, proposal section, or full proposal?)
- **Stakeholder list** (who's this for? CEO, CTO, CFO, board?)

### 2. Read Core References

Read these frameworks before starting research:
- `../references/framework-core.md` (Three Forces, 10-Layer OS, Maturity Model)
- `../references/failure-patterns.md` (75 failure patterns organized by domain)
- `../references/solution-design.md` (AI-native solution design methodology)
- `../references/value-proposition.md` (positioning, differentiators, buyer personas)

These set your thinking foundation. You'll apply them specifically to this client.

### 3. Research the Client

Run web searches in parallel across these dimensions:

**Company intelligence**:
- Recent press releases, news articles, earnings calls (if public)
- AI initiatives, digital transformation announcements, technology partnerships
- Job postings and hiring trends (signals of transformation direction)
- Leadership statements, investor presentations, strategic priorities
- Website, product updates, market positioning

**Technology signals**:
- Tech stack (what platforms, cloud providers, data infrastructure are visible?)
- Recent vendor relationships or partnerships
- Acquisition activity (what companies have they bought? Signals of capability gaps)
- Open positions (what roles are they hiring? Signals of skill gaps)

**Industry context**:
- How AI is impacting their specific industry
- Competitor AI activity and announcements
- Regulatory or market shifts affecting AI adoption
- Customer expectations driving AI investment

**Leadership insights** (if known):
- Background, previous experiences, known priorities
- Public speeches, articles, LinkedIn activity
- Career trajectory (signals of what they value)

Compile 5-7 specific data points or signals to ground your assessment.

### 4. Assess Maturity Level

Based on the research signals, place the client on the maturity curve:
- **Exploring**: Early-stage, learning, no live systems or pilots yet
- **Piloting**: Live pilots, some experiments, but not scaled
- **Scaling**: Moving pilots to production, facing coordination challenges
- **Operating**: AI systems embedded, iterating for optimization, building internal capability

Most enterprises are in Piloting or early Scaling. Document your hypothesis and the evidence.

### 5. Identify Applicable Failure Patterns

From the 75 failure patterns, identify 3-5 most likely to apply based on:
- Their industry and competitive dynamics
- Their maturity level
- Their visible organizational structure and strategy
- The challenges implied by research signals

Don't list all patterns. Surface the specific ones most relevant to their situation. These become diagnostic anchors in the POV.

### 6. Map Recommended Approach

Using the 10-Layer Operating System, identify which layers need focus for this client:
- **Layer 1-2** (Vision & Leadership): Strategic clarity, leadership signal
- **Layer 3-5** (Execution): Ways of working, delivery capability, risk management
- **Layer 6** (Infrastructure): Data, platforms, governance
- **Layer 7** (Delivery): Project methodology, partner model
- **Layer 8** (Operations): Sustained performance, continuous improvement
- **Layer 9** (Human Transformation): Capability building, identity shifts
- **Layer 10** (Outcomes): Measurement, value realization

Sequence 3-5 priority layers based on their maturity and situation. What must come first?

### 7. Draft as Markdown

Create a document in the user's workspace:
`<workspace>/Client POV - [Company] - [DRAFT].md`

Choose the structure based on requested format:

#### For Short POV (2-3 pages):
```markdown
# AI Transformation Opportunity: [Company]
**Strategic Perspective** | Prepared for [Stakeholder Title] | [Date]

---

## The Opportunity
[Opening: Why now? What's at stake? 2-3 paragraphs]

## Where [Company] Stands
[Maturity assessment, failure patterns to watch, current strengths. 2-3 paragraphs]

## How We'd Approach It
[3 sequenced priorities with explanation. Each priority maps to OS layers. 2-3 paragraphs]

## Next Steps
[How to explore deeper. Suggested engagement. 1 paragraph]
```

#### For Full POV (5-8 pages):
```markdown
# AI Transformation Strategy: [Company]
**Point of View** | Prepared for [Stakeholder Title] | [Date]

---

## Executive Summary
[One-page distillation: opportunity, maturity assessment, recommended approach, expected outcomes]

## Industry Context
[Three Forces applied to their industry. Why now? What's changing? 2-3 pages]

## [Company] Assessment
[Maturity placement with evidence. Failure patterns to watch. Organizational strengths to build on. 2-3 pages]

## Recommended Approach
[Detailed sequence of priorities mapped to OS layers. Why this sequence? Interdependencies. 2-3 pages]

## Engagement Framework
[What Elixirr would do. Phased approach. Team, timeline, deliverables. 1-2 pages]

## Expected Outcomes
[Measurable results by phase. Value targets. Success metrics. 1 page]
```

#### For Proposal Section:
[Modular section for insertion into RFP response. 2-4 pages. Focus on: Approach, Methodology, Sequencing, Team Model, Timeline, Success Metrics]

### Key Principles for Each Format:

1. **Opening positions the inflection point**: Why now? What changes if they act vs. wait?
2. **Diagnosis before prescription**: Show you understand their specific situation before recommending approach
3. **Failure patterns frame risks**: Name the patterns most relevant to them. Frame as diagnostic, not judgmental.
4. **Sequencing is specific**: Not "do all layers" — prioritize based on their maturity and situation
5. **Outcomes are measurable**: Targets by phase, metrics, business impact
6. **Frameworks are invisible**: Use the thinking, never cite the frameworks by name
7. **Evidence-based**: Every claim backed by research or known facts about their situation
8. **Perspective, not pitch**: This is thinking, not a sales document. Help them see their situation differently

### 8. Iterate with User

Share the draft. Ask:
- "Does this assessment feel right based on what you know?"
- "What's missing or inaccurate?"
- "What would sharpen the recommended approach?"
- "Any failure patterns we should add or remove?"

Refine until the user approves.

### 9. Convert to Delivery Format

Once approved:
- **If for PDF delivery**: Convert Markdown to .docx, format with client logo space if needed
- **If for RFP insertion**: Extract proposal section, integrate into RFP response template
- **If for presentation**: Convert to slide outline with speaker notes

Share the final file with placement guidance.

## POV Assessment Template

Before drafting, fill this in to clarify your thinking:

```
CLIENT: [Company]
INDUSTRY: [Sector]
MATURITY: [Exploring/Piloting/Scaling/Operating]
EVIDENCE: [2-3 signals supporting maturity assessment]

FAILURE PATTERNS (top 3-5):
1. [Pattern name] — [why relevant to this client]
2. [Pattern name] — [why relevant to this client]
3. [Pattern name] — [why relevant to this client]

PRIORITY OS LAYERS (sequenced):
1. Layer X — [why this first?]
2. Layer Y — [builds on Layer X because...]
3. Layer Z — [enables sustainable value]

KEY INSIGHT TO SURFACE:
[One idea that reframes their situation]

MEASURABLE OUTCOMES:
- By Phase 1: [specific, measurable target]
- By Phase 2: [specific, measurable target]
- By Phase 3: [specific, measurable target]
```

## Key Principles

- **Never generic**: Every sentence should be specific to this client's industry, size, maturity, or situation
- **Diagnosis first**: Spend more space on assessment than on recommendations
- **Frameworks are invisible**: You're thinking out loud, not citing. The reader learns by implication.
- **Failure patterns as diagnostic lens**: These show you understand the risks specific to their situation
- **Sequencing matters**: Explain WHY each priority comes before the next
- **Outcomes are measurable**: Not "improved efficiency" but "25% faster decision cycles on AI model deployment"
- **Respect their expertise**: You're adding a lens, not telling them how to run their company
