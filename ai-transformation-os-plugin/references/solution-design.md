# AI-Native Solution Design Reference
**Condensed Framework** | v1.0

---

## TABLE OF CONTENTS
1. [Four-Phase Methodology](#four-phase-methodology)
2. [Three-Level Problem Framework](#three-level-problem-framework)
3. [Eight AI Patterns](#eight-ai-patterns)
4. [Pattern Combinations](#pattern-combinations)
5. [Human-in-Loop Framework](#human-in-loop-framework)
6. [Trust-Building Progression](#trust-building-progression)
7. [Anti-Patterns to Avoid](#anti-patterns-to-avoid)

---

## FOUR-PHASE METHODOLOGY

### Phase 1: Discovery & Scoping
**Goal:** Identify the right problem at the right level

- Map stakeholders (IC → Manager → Executive)
- Define goal-level outcomes (not task-level)
- Validate scope: symptom check, breadth check, value check
- **Output:** Stakeholder map, goal definition, scope boundaries

**Key Questions:**
- "What are you trying to achieve?" (stated goal)
- "Why does this matter to business?" (business outcome)
- "Is this a time-save or value-unlock?"

---

### Phase 2: Workflow Analysis
**Goal:** Light-touch current state + deep ideal state design

**Current State (Light Touch):**
- High-level process walkthrough (not exhaustive)
- Data/system inventory (what exists, where)
- Pain points and friction
- Legacy task identification

**Ideal State (Deep):**
- **Inputs Required:** Structured data, unstructured content, tribal knowledge, real-time context, decisions
- **Outputs Desired:** Artifacts, decisions, actions, data
- **Context of Work:** Timing (real-time/sync/async/batch), interaction (solo/collaborative/handoff), interface (conversational/dashboard/embedded/ambient/API)

**Key Principle:** Design ideal state from first principles, don't just automate current broken process

---

### Phase 3: AI-Native Solution Design
**Goal:** Map new way of working using AI capabilities

**Step 1: Workflow Decomposition**
- Break goal into discrete steps
- Map inputs → process → outputs for each step
- Identify decision points (human vs. autonomous)
- Document data transformations and storage needs

**Step 2: AI Pattern Matching**
- Assign AI patterns to each workflow step (see pattern library)
- Note that one step may use multiple patterns in sequence

**Step 3: Human-in-Loop Design**
- Decide: Automate / Assist / Human-Only (see framework below)
- Map trust-building progression (Learning → Assisted → Autonomous)

**Step 4: Interface/Interaction Model**
- Choose interface: Chat, Dashboard, Embedded, Ambient, API
- Choose interaction: Synchronous (user waits), Asynchronous (background), Proactive (AI initiates)

---

### Phase 4: Delivery Strategy
**Goal:** Ship value progressively toward vision

**Future State Vision:** 1-2 paragraph narrative of ultimate system (12-month vision)

**Quick Win Identification:**
- High value (solves real pain, measurable impact)
- Low effort (minimal integration, existing data/systems, 1-2 weeks)
- De-risked (well-understood, clear success criteria, low political complexity)

**Sequencing & Roadmap:**
- Factor 1: Dependencies (what needs to exist first)
- Factor 2: Value delivery (standalone value first)
- Factor 3: Learning & iteration (prove pieces before combining)
- Factor 4: Trust building (start assisted, move autonomous)
- Factor 5: Technical complexity (momentum before hard stuff)

**Litmus Test:** Can we deliver measurable value in 2-4 weeks?

---

## THREE-LEVEL PROBLEM FRAMEWORK

| Level | What It Is | Who Cares | Value | AI Approach | Our Focus |
|-------|-----------|----------|-------|-------------|-----------|
| **Task** | Individual activities (find info, draft email, summarize notes) | Individual contributors | Time savings, reduced tedium | Point solutions, copilots | ❌ Usually not—handled by ChatGPT |
| **Goal** ⭐ | Measurable outcomes delivering business value (generate pipeline, write content, onboard customers) | Managers, team leads | Business impact, capability transformation | Integrated workflows, agents, end-to-end | ✅ **Anchor here** |
| **Business** | Strategic outcomes composed of multiple goals (hit revenue, reduce churn, accelerate product dev) | Executives, C-suite | Strategic transformation, differentiation | Multiple integrated goal solutions | ⚠️ Sometimes (understand to prioritize) |

**Translation Framework:**
- Task-level statement? Ask: "What larger goal does this serve?"
- Business outcome statement? Ask: "What specific goals drive this?"

---

## EIGHT AI PATTERNS

### 1. Summarization
**What:** Condenses long/complex content into concise key points
**When:** Meeting notes, call transcripts, research, long emails
**Input/Output:** Long-form text → condensed summary
**Strengths:** Fast, scalable, handles nuance
**Limitations:** May miss subtle details, quality depends on source, can hallucinate
**Example:** Summarize 1-hour call into 5 key points; distill 50-page report to 1-page brief

---

### 2. Generation
**What:** Creates new content from inputs (text, code, data)
**When:** Emails, proposals, reports, blog posts, code, personalized content at scale
**Input/Output:** Context + instructions + examples → new content
**Strengths:** Highly flexible, handles personalization, learns from examples
**Limitations:** Needs good inputs (GIGO), may need editing, can be verbose without constraints
**Example:** Draft personalized outreach email; generate product description; write test cases

---

### 3. Extraction
**What:** Pulls structured data from unstructured content
**When:** Parsing emails, PDFs, forms, invoices; extracting entities (names, dates, amounts)
**Input/Output:** Unstructured text/documents → structured data (JSON, database records)
**Strengths:** Handles messy/inconsistent formats, complex nested info, multiple doc types
**Limitations:** Accuracy depends on source quality, struggles with handwriting, needs clear schema
**Example:** Extract customer request from email; pull invoice details from PDF; parse resume

---

### 4. Classification
**What:** Categorizes or labels content based on rules/patterns
**When:** Routing (tickets, leads, emails), prioritization, tagging, filtering
**Input/Output:** Content + category definitions → category label + confidence score
**Strengths:** Fast, automatable, handles nuance, learns from examples
**Limitations:** Needs clear definitions, edge cases ambiguous, may need training data
**Example:** Route support ticket by type; tag sentiment; prioritize tasks

---

### 5. Reasoning
**What:** Analyzes information, evaluates options, makes judgment calls
**When:** Scoring (leads, content, risk), recommendations, decision support, diagnosis
**Input/Output:** Data + context + criteria + rules → score + recommendation + rationale
**Strengths:** Handles complex multi-factor decisions, explains reasoning, adapts to nuanced criteria
**Limitations:** Quality depends on criteria clarity, can be overconfident, needs validation for high-stakes
**Example:** Score leads by fit; recommend priority prospects; evaluate proposal win likelihood

---

### 6. Orchestration
**What:** Coordinates multi-step workflows, manages task sequences, calls tools/agents
**When:** Agentic systems, complex workflows (research → analyze → draft → review), tool-using agents
**Input/Output:** Goal + tools/capabilities available + context → completed multi-step task
**Strengths:** Handles complex end-to-end tasks, reduces human intervention, adapts to intermediate results
**Limitations:** More complex to build/debug, can fail at any step, needs clear goal + tool access
**Example:** Research agent (company name → web search → extract → summarize → save to CRM); automated lead qualification pipeline

---

### 7. Retrieval
**What:** Finds relevant information from knowledge base, database, document set
**When:** Q&A systems, context lookup, knowledge augmentation (RAG), research
**Input/Output:** Query/question/context need + knowledge base → relevant documents/passages/answers
**Strengths:** Grounded in real data (reduces hallucination), scales to large corpora, fast
**Limitations:** Quality depends on KB quality, may miss if query poorly worded, needs upfront indexing
**Example:** "What's our refund policy?"; find similar past proposals; pull relevant meeting notes

---

### 8. Transformation
**What:** Converts data/content from one format/structure to another
**When:** Data mapping (CRM → marketing automation), translation, reformatting, standardization
**Input/Output:** Source data + target format spec → transformed data
**Strengths:** Handles inconsistent/messy data, flexible, reduces manual entry
**Limitations:** Accuracy depends on rules clarity, may lose information, edge cases need validation
**Example:** Meeting notes → CRM fields; technical specs → customer benefits; spreadsheet → chart-ready

---

## PATTERN COMBINATIONS

### Research & Summarization
**Flow:** Retrieval → Extraction → Summarization
**Use:** Prospect research
- Retrieval: Search web for company news, LinkedIn, press releases
- Extraction: Pull key facts (funding, leadership, pain points)
- Summarization: Condense into 1-page brief

### Content Generation with Context
**Flow:** Retrieval → Generation
**Use:** Personalized email drafting
- Retrieval: Find past interactions, relevant product info
- Generation: Draft email using retrieved context

### Intelligent Routing
**Flow:** Extraction → Classification → Orchestration
**Use:** Support ticket management
- Extraction: Pull key details (issue type, customer tier)
- Classification: Categorize urgency, department
- Orchestration: Route to team, set priority, trigger notifications

### Decision Support
**Flow:** Retrieval → Reasoning → Generation
**Use:** Opportunity assessment
- Retrieval: Pull past wins/losses with similar profile
- Reasoning: Score this opportunity based on patterns
- Generation: Create recommendation memo with rationale

### End-to-End Automation
**Flow:** Orchestration (calling Retrieval, Extraction, Reasoning, Generation)
**Use:** Automated lead qualification
- Orchestration triggers nightly: retrieve new leads, extract company info, score fit, draft outreach, save, notify

---

## HUMAN-IN-LOOP FRAMEWORK

### Automate (AI Autonomous)
**When:**
- ✅ Task is routine and rules-based
- ✅ Input data reliable and structured
- ✅ Stakes are low (errors recoverable)
- ✅ Speed/scale critical

**Examples:** Data retrieval, formatting, scheduling, routing

---

### Assist (AI + Human)
**When:**
- ✅ Task requires subjective judgment
- ✅ Stakes are moderate (costly but not catastrophic)
- ✅ Trust still being built
- ✅ Context or nuance matters

**Examples:** Drafting content (AI drafts, human edits), scoring leads (AI scores, human reviews outliers), recommendations

---

### Human-Only
**When:**
- ✅ High-stakes decisions with significant consequences
- ✅ Requires deep relationship or political context
- ✅ Regulatory/compliance requirements
- ✅ Creativity or strategic vision needed

**Examples:** Final contract approval, hiring decisions, strategic pivots

---

## TRUST-BUILDING PROGRESSION

### Phase 1: Learning (Weeks 1-4)
- AI generates, human reviews everything
- Humans provide feedback, tune system
- **Goal:** Build trust, improve accuracy

### Phase 2: Assisted (Weeks 5-12)
- AI handles routine cases autonomously
- Human reviews edge cases and exceptions
- **Goal:** Scale efficiency while maintaining quality

### Phase 3: Autonomous (Week 13+)
- AI operates independently for most cases
- Human oversight via dashboards/metrics
- Human intervention only on escalations
- **Goal:** Maximum leverage, human focus on high-value work

**Note:** Not all workflows reach Phase 3. Some always require human judgment.

---

## ANTI-PATTERNS TO AVOID

| Anti-Pattern | Why It Fails | How to Avoid |
|--------------|-------------|-------------|
| **Automating broken processes** | Exhaustive current-state mapping enslaves you to bad process | Light-touch current state; design ideal from first principles |
| **Solving symptoms, not root problems** | Didn't ask "why" enough times | Use symptom check: "Why does this exist?" + "What would break?" |
| **Myopic scope** | Focused on one pain point without seeing full workflow | Use breadth check: "What before/after/adjacent?" |
| **Boiling the ocean** | Tried to solve everything at once | Anchor at goal-level, identify quick wins, sequence delivery |
| **Task-level solutions** | Talked to ICs, never translated up | Stakeholder mapping, translate task → goal with managers |
| **Over-engineering** | Designed for every edge case in v1 | Start simple, iterate based on real usage |
| **Low adoption** | Built without understanding context of work | Map interaction model, consider trust-building progression |
| **Generating without grounding** | Creating content without context/examples | Use Retrieval + Generation pattern |
| **Trusting without validation** | Auto-executing high-stakes AI outputs | Use human-in-loop for high-risk decisions |
| **Over-orchestrating early** | Complex multi-step workflows before individual steps proven | Start with single patterns, compose once validated |

---

## QUICK REFERENCE: PATTERN DECISION TREE

**"I need to make long content shorter"** → **Summarization**

**"I need to create something new"** → **Generation**

**"I need to pull specific data from messy content"** → **Extraction**

**"I need to categorize or label things"** → **Classification**

**"I need to score, evaluate, or recommend"** → **Reasoning**

**"I need to coordinate multiple steps"** → **Orchestration**

**"I need to find relevant information"** → **Retrieval**

**"I need to convert format or structure"** → **Transformation**

---

## KEY PRINCIPLES

1. **Outcome-first, not current-state-first**
2. **Design ideal state from first principles**
3. **Solve root problems, not symptoms**
4. **Right-sized scope (not myopic, not boiling the ocean)**
5. **Progressive delivery (quick wins → vision)**
6. **Human-in-loop where it matters (automate routine, assist judgment, human for high-stakes)**
7. **Identity matters as much as capability**
8. **Compressed feedback loops accelerate learning**
9. **Build at goal-level, anchor there**

---

**Use this reference during Phase 3: AI-Native Solution Design to match patterns to workflow steps and design interactions.**

**For detailed methodology:** See framework-core.md

**Version 1.0 | 2026-01-17**
