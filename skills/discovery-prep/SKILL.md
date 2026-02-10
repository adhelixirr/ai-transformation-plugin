---
name: discovery-prep
description: |
  Prepare for client or prospect meetings with research, hypotheses, and discovery questions grounded in Elixirr's AI transformation frameworks. Use when anyone mentions "call with", "meeting with", "prep me for", "discovery questions", "what should I ask", "meeting prep", "call prep", or any request to prepare for a conversation with a prospect or client about AI transformation.
---

# Discovery Prep Generator

## Workflow

### 1. Collect Meeting Context

Confirm these details (ask if missing):
- **Company name** (what organization)
- **Attendee names & titles** (who's on the call? What are their roles?)
- **Your attendees** (who's representing Elixirr?)
- **Meeting context** (first call, follow-up, specific topic, deep dive?)
- **Time allocated** (30 min, 60 min, 90 min? Shapes question count)
- **Known situation** (what you know about them already, any triggers for the conversation)

### 2. Read Core Frameworks

Read these before research:
- `../references/framework-core.md` (Three Forces, 10-Layer OS, Maturity Model)
- `../references/failure-patterns.md` (75 failure patterns — helps you recognize patterns they describe)

These set your thinking. You'll listen for evidence of maturity level and failure patterns during the call.

### 3. Research the Company & Attendees

Run web searches in parallel:

**About the company**:
- Recent news, press releases, earnings (if public)
- AI/digital initiatives, partnerships, acquisitions
- Market position, size, growth trajectory
- Leadership statements or strategic priorities
- Competitive positioning

**About the attendees** (if names are known):
- Background, career trajectory, previous roles
- LinkedIn profile, public speaking, articles
- Known expertise or priorities
- What their role typically cares about

**Industry context**:
- How AI is impacting their industry specifically
- Regulatory environment, customer expectations, competitive threats
- Adoption rates and barriers in their sector
- Vendor landscape (who else are they likely evaluating?)

Compile 5-7 specific facts or signals to ground your hypothesis.

### 4. Develop Hypotheses

Form preliminary hypotheses about:

**Maturity level**: Based on signals, where do they likely sit?
- **Exploring**: No live systems, early learning
- **Piloting**: Pilots running, not yet scaled
- **Scaling**: Moving pilots to production, facing coordination challenges
- **Operating**: Embedded systems, iterating, building capability

Document your hypothesis and the 2-3 signals supporting it.

**Failure patterns**: Based on industry, size, and maturity, which patterns are they most likely facing?
- Pick 3-5 from the 75 failure patterns
- Frame these as probing questions, not accusations

### 5. Generate Meeting Prep Document

Create a Markdown document and save to user's workspace:
`<workspace>/Meeting Prep - [Company] - [Date].md`

**Structure** (see detailed sections below):

```markdown
# Meeting Prep: [Company]
**Call with:** [Attendees] | **Date/Time:** [When] | **Duration:** [How long]

---

## Company Overview
[30-second summary of what they do, size, market position]

## Attendee Profiles
- [Name] ([Title]): [Background, likely priorities]
- [Name] ([Title]): [Background, likely priorities]

## Maturity Hypothesis
[Exploring/Piloting/Scaling/Operating] — Evidence: [signals]

## Likely Challenges (Failure Patterns)
1. [Pattern 1] — Why this matters for them
2. [Pattern 2] — Why this matters for them
3. [Pattern 3] — Why this matters for them

## Discovery Questions (organized by theme)

### Strategic Clarity (Understanding their vision & direction)
[6-8 questions]

### Current State & Pilots (What's happening right now)
[6-8 questions]

### Organizational Readiness (How equipped are they to scale)
[6-8 questions]

### Governance & Decision-Making (How do they make decisions, manage portfolio)
[6-8 questions]

### Value & Measurement (How they measure success)
[6-8 questions]

## Suggested Conversation Flow
[How to sequence the conversation for maximum insight]

## Key Insights to Share
[3 observations they might find valuable]

## Success Metrics for This Call
[What outcomes would make this call successful?]
```

### Section 6 Details: Attendee Profiles

For each attendee, include:
```
**[Name] — [Title]**
- Background: [Where they came from, key experience]
- Likely priorities: [What this role cares about]
- Success signals: [How to tell if they're engaged/interested]
- Question approach: [How to ask questions that resonate with this person]
```

### Section 7 Details: Failure Patterns

Select 3-5 patterns most relevant. For each:
```
**Pattern Name**
- Description: [What this pattern looks like]
- Why relevant to them: [Industry, size, or situation signals suggesting this is real]
- Probe approach: [How to ask about it conversationally]
- Red flag language: [What they might say that indicates this pattern]
```

### Section 8 Details: Discovery Questions

Organize by five themes. For each, write 6-8 questions:

#### Theme 1: Strategic Clarity (Layers 1-2: Vision & Leadership Signal)

Frame as genuine curiosity, not interrogation. Use "I'm curious about..." phrasing.

Sample questions:
- "How does your CEO think about AI's role in [company's] next 3-year strategy?"
- "If I asked your executive team to define what 'successful AI adoption' looks like, how aligned would they be?"
- "What are the top 2-3 business outcomes your organization is trying to achieve in the next 18 months?"
- "What's driving the urgency around AI now? What changes if you don't act?"
- "Who owns the decision on how to approach AI transformation — is it IT, business, or CEO-level?"

#### Theme 2: Current State & Pilots (Understanding what's happening)

These questions map to Layers 3-5 (execution readiness) and early signals of failure patterns.

Sample questions:
- "How many AI/ML initiatives are currently running? What's the range from smallest to largest?"
- "Of those initiatives, how many have moved from pilot to production?"
- "What's the biggest bottleneck preventing pilots from scaling?"
- "How would you describe the collaboration between your data/AI team and the business teams they support?"
- "What's been your biggest surprise (positive or negative) from the pilots you've run?"

#### Theme 3: Organizational Readiness (Can they scale? Do they have the capability?)

Maps to Layers 6-8 (infrastructure, operations, delivery model).

Sample questions:
- "How is AI responsibility distributed across your organization? Who owns it?"
- "What's your approach to governance — how do you make decisions about which initiatives to fund and how to resource them?"
- "How quickly can you onboard new tools or platforms? What's the typical approval cycle?"
- "How do teams currently collaborate across siloed functions (data, IT, business)?"
- "What's been your experience with partners or vendors on AI-related projects?"

#### Theme 4: Human & Capability Transformation (Are they building internal capability? Are they set up for sustained value?)

Maps to Layer 9 (human transformation, identity shift).

Sample questions:
- "How are you thinking about upskilling your current teams versus hiring new talent?"
- "What does 'AI capability' mean to your organization? What roles need to change?"
- "How is AI adoption affecting day-to-day workflows? Have roles had to redesign?"
- "What's your biggest concern about sustaining momentum on AI beyond initial pilots?"
- "How are you helping leaders understand their role in AI transformation?"

#### Theme 5: Value & Measurement (How do they measure success? Can they articulate ROI?)

Maps to Layer 10 (outcomes, measurement, value realization).

Sample questions:
- "How are you currently measuring the success of your AI initiatives?"
- "What would [initial value target] in value realization look like for you?"
- "How transparent is ROI on AI investments across your organization?"
- "If you had to point to one AI investment that delivered clear business value, what would it be?"
- "How do you communicate AI ROI to the board or executive team?"

### Section 9 Details: Suggested Conversation Flow

Map out a logical conversation arc:

```
**Opening (5 minutes)**
- Build rapport: Acknowledge their context (what you know about them/industry)
- Frame your intent: "I want to understand where you stand and what matters most"
- Set expectations: "I have some questions, but I'm most interested in your perspective"

**Section 1: Strategic Clarity (10-15 minutes)**
- Start with big picture: vision, strategy, outcomes
- Listen for: alignment, leadership signal, maturity clues
- Key insight to listen for: Can they articulate what success means?

**Section 2: Current State (10-15 minutes)**
- Move to what's happening now: pilots, initiatives, momentum
- Listen for: failure patterns, bottlenecks, real challenges
- Key insight to listen for: Where are they stuck? Where's the friction?

**Section 3: Organizational Capability (10 minutes)**
- Explore structure, governance, teamwork
- Listen for: silos, decision velocity, ability to scale
- Key insight to listen for: Can they organize themselves to scale?

**Section 4: Value & Outcomes (10 minutes)**
- Understand how they measure success
- Listen for: outcome clarity, measurement maturity
- Key insight to listen for: Are they measuring business impact or just activity?

**Closing (5-10 minutes)**
- Summarize: "Here's what I'm hearing..."
- Share insight: One observation that might be valuable
- Invite next: "What would be most useful to explore further?"
```

### Section 10 Details: Key Insights to Share

Identify 3 observations you could share if the conversation allows:

```
**Insight 1: [Reframe something they said]**
- What they're likely saying: [Their narrative]
- A different lens: [How Elixirr would reframe it]
- Why it matters: [The impact of this reframe]
- Conversation trigger: "I've noticed that when I ask [similar companies] this question..."

**Insight 2: [Diagnostic observation]**
[Same structure]

**Insight 3: [Forward-looking observation]**
[Same structure]
```

*Don't pitch these. Only surface them if the conversation opens naturally.*

### Section 11 Details: Success Metrics

Define what "success" means for this specific call:

```
- [ ] Confirmed/updated maturity level hypothesis
- [ ] Identified top 3 failure patterns they're likely facing
- [ ] Understood their definition of success
- [ ] Mapped who owns different decisions
- [ ] Scheduled next conversation
- [ ] Built rapport with [attendee names]
- [ ] Tested whether they're open to [your service/engagement]
```

## Key Principles

1. **Questions over pitch**: A great discovery call generates 80% listening, 20% talking on Elixirr's side.

2. **Conversational, not interrogative**: "I'm curious about..." not "Do you have...". Build rapport through genuine interest.

3. **Listen for patterns**: Framework knowledge (OS, failure patterns) helps you recognize what they're describing without them naming it.

4. **Acknowledge before you probe**: If they describe a situation, acknowledge the challenge before asking about it. Shows respect.

5. **Connect dots**: If they mention something in one answer that relates to another area, call it out: "That connects to what you said earlier about..."

6. **Know your hypotheses but stay flexible**: You have hypotheses. Data from the call might shift them. That's good.

7. **Leave space for silence**: After you ask a question, wait for their full answer. Silence is powerful.

8. **Take notes actively**: Show you're listening. Quote them back. "So if I'm hearing you right..."

## Pre-Call Checklist

Before the meeting:
- [ ] Read prep document
- [ ] Have web research (company, attendees) summarized
- [ ] Confirm attendee names/titles/roles
- [ ] Know your conversation flow
- [ ] Have 3 key insights identified
- [ ] Know what "success" looks like for this call
- [ ] Test tech setup (camera, audio, screen share if needed)
- [ ] Prepare to take notes (doc or notebook visible to you only)
- [ ] Know when/how you'll debrief with your Elixirr colleague

## Post-Call Debrief

After the call, capture:
- **Maturity confirmed/revised**: Where are they really?
- **Top 3-5 failure patterns observed**: What did you hear?
- **Decision makers**: Who decides? Who influences?
- **Timelines**: When do they need to decide/move?
- **Appetite for engagement**: Were they open/closed/testing?
- **Next steps**: What did you agree to?
- **Key insights**: What surprised you?
- **Follow-up actions**: What do you need to do?
