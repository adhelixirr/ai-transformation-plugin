# AI Adoption Failure Patterns Reference

**Version**: 1.0 | **Purpose**: Condensed diagnostic cheat sheet — 75 patterns across 10 domains

---

## TABLE OF CONTENTS

1. [Most Common High-Impact Failures](#most-common-high-impact-failures)
2. [All 75 Patterns by Domain](#all-75-patterns-by-domain)
3. [Root Cause Sequencing](#root-cause-sequencing)
4. [Pattern Selection by Client Situation](#pattern-selection-by-client-situation)

---

## MOST COMMON HIGH-IMPACT FAILURES

These six patterns show up in 80%+ of transformations. They're high-leverage because they're often invisible until too late.

**⭐ 1.3 No executive owner** → Everyone "supporting" AI, nobody accountable for outcomes.

**⭐ 2.2 Delegating understanding, not execution** → Leaders outsource sensemaking; work redesign never happens.

**⭐ 4.3 Ignoring identity threat** → AI attacks source of professional value; resistance shows as edge-case fixation and quality complaints.

**⭐ 7.1 PoC purgatory** → Lots of prototypes, few production systems; most AI initiatives die in the demo-to-workflow gap.

**⭐ 9.1 Assuming adoption will happen naturally** → "If we build it, they'll use it" is false, especially when AI changes professional identity.

**⭐ 10.1 Measuring the wrong things** → Tracking models built, PoCs shipped, prompts written—not decisions improved or capacity created.

---

## ALL 75 PATTERNS BY DOMAIN

**Domain 1 (8)**: 1.1 No business case | 1.2 AI as IT project | 1.3 No executive owner | 1.4 Not choosing where to win | 1.5 Unrealistic expectations | 1.6 Ignoring differentiation | 1.7 Cost-saving only | 1.8 Reversible adoption

**Domain 2 (12)**: 2.1 "Don't need to know how it works" | 2.2 Delegating understanding | 2.3 No personal operating model | 2.4 Can't distinguish hype | 2.5 "Use AI" without incentive change | 2.6 Public support, private skepticism | 2.7 No visible learning | 2.8 Blame for AI mistakes | 2.9 Delegating to training teams | 2.10 Avoiding decision redesign | 2.11 No workforce narrative | 2.12 Governance ≠ leadership

**Domain 3 (6)**: 3.1 Picking use cases that don't matter | 3.2 Starting with hardest problems | 3.3 Avoiding core workflows | 3.4 Forgetting the user | 3.5 No workflow-first design | 3.6 Not defining decision boundaries

**Domain 4 (7)**: 4.1 AI as assistant, not teammate | 4.2 Never redefining roles | 4.3 Ignoring identity threat | 4.4 De-skilling feeling | 4.5 No upgrade path | 4.6 Middle management compression | 4.7 Power shifts without acknowledgment

**Domain 5 (7)**: 5.1 Layering on legacy workflows | 5.2 No default behaviors | 5.3 No explicit handoffs | 5.4 Optimizing tasks not outcomes | 5.5 Hiding AI value in workflows | 5.6 No exception handling design | 5.7 No change control

**Domain 6 (12)**: 6.1 Data is "good enough" | 6.2 No data ownership | 6.3 No knowledge strategy | 6.4 Volume over relevance | 6.5 No feedback loops | 6.6 Tool-first decisions | 6.7 Over-customizing early | 6.8 Ignoring latency | 6.9 No evaluation framework | 6.10 No model drift plan | 6.11 No observability | 6.12 Under-investing integration

**Domain 7 (9)**: 7.1 PoC purgatory | 7.2 No product thinking | 7.3 Unclear build vs buy | 7.4 Single-team job | 7.5 No portfolio management | 7.6 AI as software not labor | 7.7 No AI onboarding | 7.8 No AI manager role | 7.9 No training data from real work

**Domain 8 (11)**: 8.1 Policy theater | 8.2 Blocking everything | 8.3 Allowing everything | 8.4 Not classifying data | 8.5 No human-in-loop design | 8.6 No auditability | 8.7 Ignoring IP/vendor terms | 8.8 No H vs AI authority clarity | 8.9 Ethics as PR | 8.10 Ignoring customer trust | 8.11 Not updating policies

**Domain 9 (19)**: 9.1 Adoption happens naturally | 9.2 No champions | 9.3 No output standards | 9.4 No escalation | 9.5 AI reduces load | 9.6 Effort→ambiguity | 9.7 No focus protection | 9.8 Speed=effectiveness | 9.9 Skepticism=rigor | 9.10 No error language | 9.11 Fear of replacement | 9.12 AI overselling | 9.13 Risk without authority | 9.14 No "why now" story | 9.15 Fear fills vacuum | 9.16 AI threatens meaning | 9.17 Same management | 9.18 No coaching model | 9.19 Speed is neutral

**Domain 10 (9)**: 10.1 Measuring wrong things | 10.2 No baseline | 10.3 Not tracking value | 10.4 No reinvestment plan | 10.5 Licenses without adoption | 10.6 Ignoring total cost | 10.7 Polish over insight | 10.8 Activity vs leverage | 10.9 Local optimization, global failure

**Vendor (4)**: V.1 Chasing shiny objects | V.2 Vendors define roadmap | V.3 No exit strategy | V.4 Not negotiating terms

---

## ROOT CAUSE SEQUENCING

**Key insight**: Failures in Domain 1 (Strategy) cause failures in all subsequent domains. Failures in Domain 2 (Leadership) cascade through Domains 3–10.

### Failure Propagation Chains

**Chain 1: Strategic Collapse**
- 1.1 (No business case) → 3.1 (Pick use cases that don't matter) → 7.1 (PoC purgatory) → 10.1 (Measure wrong things)

**Chain 2: Leadership Failure**
- 2.2 (Delegate understanding) → 4.2 (Never redefine roles) → 9.1 (Assume adoption happens naturally) → 9.15 (Fear narratives fill vacuum)

**Chain 3: Human Resistance**
- 4.3 (Ignore identity threat) → 9.6 (Replace effort with ambiguity) → 9.10 (No shared language for errors) → 9.13 (People absorb risk without authority)

**Intervention principle**: Fix failures upstream (Domains 1–2) first. Downstream interventions alone will never stick.

---

## ROOT CAUSE SEQUENCING

**Key insight**: Failures in Domain 1 cascade through all other domains. Domain 2 failures propagate to 3–10. Fix upstream first.

**Failure Chains**:
- **Strategic collapse**: 1.1 → 3.1 → 7.1 → 10.1
- **Leadership failure**: 2.2 → 4.2 → 9.1 → 9.15
- **Human resistance**: 4.3 → 9.6 → 9.10 → 9.13

---

## PATTERN SELECTION BY CLIENT SITUATION

Use this to pick which patterns to mention in specific client conversations.

### "We don't know where to start"
- **1.1** No clear business case
- **2.2** Delegating understanding
- **3.1** Picking use cases that don't matter
- **7.1** PoC purgatory

### "We're stuck in pilots"
- **7.1** PoC purgatory
- **1.3** No executive owner
- **7.5** No portfolio management
- **10.1** Measuring wrong things

### "Our people aren't adopting"
- **4.3** Ignoring identity threat
- **9.1** Assuming adoption happens naturally
- **9.6** Replacing effort with ambiguity
- **2.3** No personal operating model with AI (leaders not modeling)

### "Leadership says right things but nothing changes"
- **2.2** Delegating understanding
- **2.5** Saying "use AI" without changing incentives
- **2.6** Public support, private skepticism
- **2.12** Confusing governance with leadership

### "We have a strategy but can't execute"
- **4.2** Never redefining roles
- **5.1** Layering AI on legacy workflows
- **7.2** No product thinking
- **6.6** Tool-first decisions

### "We're measuring activity, not impact"
- **10.1** Measuring wrong things
- **10.2** No baseline before AI
- **10.4** No reinvestment plan
- **10.8** Measuring activity instead of leverage

---

**Line Count**: 285 lines | **Use Case**: Rapid diagnostics, client conversations, pattern-based interventions
