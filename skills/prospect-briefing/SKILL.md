---
name: prospect-briefing
description: |
  Generate personalized AI Transformation executive briefings for sales prospects, branded with Elixirr identity. Creates a professional 6-8 page PDF that applies Elixirr's AI transformation frameworks (Three Forces, Operating System, Failure Patterns, Augmented Professional, Maturity Model, Outcome-First Strategy) to a specific prospect's industry, company, and role.

  Default workflow: draft content as Markdown for user review and iteration, then generate the branded Elixirr PDF once content is approved.

  MANDATORY TRIGGERS: "generate a briefing", "create a briefing", "prospect briefing", "executive briefing", "AI briefing for", "briefing for [name]", "send [name] something", any request to create personalized sales collateral applying Elixirr's AI transformation frameworks.

  Required inputs: prospect name, title, company. Optional: seniority level, notes, context.
---

# Prospect Briefing Generator

## Workflow

### 1. Collect Prospect Details

Confirm these details (ask if missing):
- **Name** (full name)
- **Title** (full title, e.g. "Chief Executive Officer")
- **Company** (full company name)
- **Short title** (e.g. "CEO", "CTO", "VP Ops") — infer from title if not given
- **Notes** (optional — how they showed interest, what they care about, relationship history)

### 2. Research

Use web search to gather intelligence on three dimensions. Run searches in parallel.

**About the prospect**: Background, career, expertise, public talks/articles, leadership priorities.

**About the company**: What they do, market position, size, recent news, AI/digital strategy, competitors' AI activity, technology investments.

**About the industry + AI**: How AI impacts their industry. Key use cases, adoption rates, barriers. Find 3-5 specific data points.

### 3. Read References

Read these before writing:
- `../references/framework-core.md` — comprehensive framework overview
- `references/content-guide.md` — section-by-section writing guide and JSON format spec

### 4. Draft as Markdown

Write the full briefing as a Markdown file and save it to the user's workspace folder:
`<workspace>/AI Transformation Briefing - <Name> - <Company> [DRAFT].md`

Structure the Markdown to mirror the final PDF layout:

```markdown
# AI Transformation in [Industry]
**A strategic briefing for [Name], [Title], [Company]**
*Prepared by Adam Hofmann, Elixirr Partner — AI*

---

## The Forces Reshaping [Industry]
[Section 1 content — Three Forces applied to their industry]

## What This Means for [Company]
[Section 2 content — maturity placement + failure patterns]

## Leading Through the Shift
[Section 3 content — role-specific implications + Augmented Role table]

## Where I'd Focus First
[Section 4 content — 3 sequenced priorities with diagnostic questions]

## A Conversation Worth Having
[Section 5 content — closing + contact info]
```

**5 required sections** (see `references/content-guide.md` for detailed guidance):
1. **The Forces Reshaping [Industry]** — Three Forces applied to their industry
2. **What This Means for [Company]** — Maturity placement + failure patterns
3. **Leading Through the Shift** — Role-specific + Augmented [Role] table
4. **Where I'd Focus First** — 3 sequenced priorities with diagnostic questions
5. **A Conversation Worth Having** — Closing + signature

After saving, share the Markdown file link and tell the user to review it. Ask what they'd like to change. Iterate until they approve.

### 5. Convert Approved Content to PDF

Once the user approves the draft (e.g. "looks good", "generate the PDF", "send it"):

1. Convert the approved Markdown content into the JSON config format required by the PDF engine. Save to `/sessions/brave-fervent-ritchie/briefing_config.json`.

JSON structure:
```json
{
  "prospect": { "name": "", "title": "", "company": "", "short_title": "" },
  "cover": {
    "main_title_line1": "AI Transformation",
    "main_title_line2": "in [Industry]",
    "subtitle_line1": "A strategic briefing on ...",
    "subtitle_line2": "... your role as [short_title]."
  },
  "sections": [array of 5 sections with title, subtitle, and elements]
}
```

Element types: `intro`, `body`, `closing`, `heading`, `numbered` (number, title, body, optional accent:"gold"), `insight` (text, style:"warm"|"cool"), `table` (headers, rows, optional col_widths), `spacer`, `page_break`, `signature`, `hr`

2. Run the PDF generator:
```bash
cp <this_skill_dir>/scripts/generate_briefing.py /sessions/brave-fervent-ritchie/generate_briefing.py
python /sessions/brave-fervent-ritchie/generate_briefing.py \
  /sessions/brave-fervent-ritchie/briefing_config.json \
  "<workspace>/AI Transformation Briefing - <Name> - <Company>.pdf"
```

### 6. Verify

Render the first 2-3 pages as images with pypdfium2. Verify cover page branding, content flow, and layout. Fix and regenerate if needed.

### 7. Deliver

Share the PDF via link. Remove the draft Markdown file if the user no longer needs it.

## Key Principles

- Every paragraph must be specific to prospect's industry, company, or role
- Frame failure patterns as "worth watching for" not "you're failing at"
- Include at least 3 diagnostic questions the prospect can ask their own team
- The "Augmented [Role]" table is high-impact — tailor dimensions to their actual role
- The closing references the full Operating System (10 layers, 75 failure patterns) to create curiosity
- Target: 6-8 page PDF
