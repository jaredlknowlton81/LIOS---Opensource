Purpose: Test whether multiple agents can collaboratively evolve a shared knowledge graph while preserving disagreement, provenance, decisions, and learning in a persistent Ledger.

1. Experiment

Question

Can multiple agents contribute to a shared graph without losing the history of how the graph evolved?

Hypothesis

A shared graph can represent the system’s current relational state, while a Ledger preserves the temporal history of agent observations, proposals, conflicts, decisions, and outcomes.

Participants

- [[Agent-Researcher]]
- [[Agent-Skeptic]]
- [[Agent-Reviewer]]

Shared Substrate

- [[Shared-Graph]]
- [[Ledger]]

  

2. Initial Graph

Create:

05-Graph/Shared-Graph.md

---

type: graph

version: 1

status: active

---

Entities

- [[Entity-A]]
- [[Entity-B]]

Known Relationships

Currently unknown.

Open Questions

- Are Entity-A and Entity-B related?
- If related, what type of relationship exists?
- What evidence supports the relationship?

  

3. Entity A

Create:

01-Entities/Entity-A.md

---

type: entity

entity_id: A

status: active

---

Entity A

A hypothetical entity used for testing the multi-agent graph.

Observations

No observations yet.

Relationships

None confirmed.

  

4. Entity B

Create:

01-Entities/Entity-B.md

---

type: entity

entity_id: B

status: active

---

Entity B

A hypothetical entity used for testing the multi-agent graph.

Observations

No observations yet.

Relationships

None confirmed.

  

5. Agent Researcher

Create:

04-Agents/Agent-Researcher.md

---

type: agent

agent_id: researcher

role: evidence-finder

authority: propose

writes_to:

  - proposed-changes

---

Mission

Find evidence that reveals relationships between entities.

Behavior

1. Read the relevant graph context.
2. Examine available evidence.
3. Identify possible relationships.
4. Assign confidence.
5. Create a proposed graph change.
6. Never silently modify the shared graph.

Output

A [[Graph-Change]] proposal containing:

- proposed relationship
- evidence
- reasoning
- confidence
- provenance

  

6. Agent Skeptic

Create:

04-Agents/Agent-Skeptic.md

---

type: agent

agent_id: skeptic

role: adversarial-reviewer

authority: challenge

writes_to:

  - proposed-changes

---

Mission

Search for contradictory evidence and alternative interpretations.

Behavior

1. Read the current graph.
2. Examine existing proposals.
3. Challenge unsupported relationships.
4. Identify missing evidence.
5. Propose alternatives when justified.
6. Preserve uncertainty rather than forcing a conclusion.

Output

A challenge or competing [[Graph-Change]].

  

7. Agent Reviewer

Create:

04-Agents/Agent-Reviewer.md

---

type: agent

agent_id: reviewer

role: governance

authority: approve

writes_to:

  - graph

  - ledger

---

Mission

Determine which proposed changes become part of shared state.

Review Criteria

1. Evidence quality
2. Provenance
3. Confidence
4. Contradictory evidence
5. Existing graph state
6. Ontology constraints

Possible Decisions

- ACCEPT
- REJECT
- MODIFY
- DEFER

Every decision must create a Ledger entry.

  

8. Graph Change

Create:

05-Graph/Proposed-Changes/CHANGE-001.md

---

type: graph-change

change_id: CHANGE-001

status: proposed

agent: "[[Agent-Researcher]]"

subject: "[[Entity-A]]"

object: "[[Entity-B]]"

relationship: related_to

confidence: 0.82

---

Proposed Change

Entity-A → related_to → Entity-B

Evidence

Describe the evidence supporting the relationship.

Reasoning

Explain why the evidence supports the proposed relationship.

Confidence

0.82

This number is illustrative only.

Provenance

Where did the evidence originate?

Review Status

PROPOSED

  

9. Challenge

Create:

05-Graph/Proposed-Changes/CHANGE-002.md

---

type: graph-change

change_id: CHANGE-002

status: proposed

agent: "[[Agent-Skeptic]]"

subject: "[[Entity-A]]"

object: "[[Entity-B]]"

relationship: disputed

confidence: 0.67

---

Challenge

The Skeptic disputes the proposed relationship.

Counter-Evidence

Describe evidence that weakens CHANGE-001.

Alternative Interpretation

Explain another possible interpretation.

Recommendation

- Reject
- Modify
- Gather more evidence

  

10. Conflict

Create:

05-Graph/Conflicts/CONFLICT-001.md

---

type: conflict

conflict_id: CONFLICT-001

status: open

participants:

  - "[[Agent-Researcher]]"

  - "[[Agent-Skeptic]]"

related_changes:

  - CHANGE-001

  - CHANGE-002

---

Conflict

Position A

Entity-A is related to Entity-B.

Position B

The evidence does not establish the relationship.

Question

What should the shared graph represent?

  

11. Review

The Reviewer examines:

CHANGE-001

CHANGE-002

CONFLICT-001

Shared-Graph

Then creates:

06-Ledger/Decisions/DECISION-001.md

---

type: decision

decision_id: DECISION-001

reviewer: "[[Agent-Reviewer]]"

conflict: "[[CONFLICT-001]]"

decision: MODIFY

---

Decision

MODIFY

The relationship is retained as a hypothesis rather than a confirmed fact.

New Graph State

Entity-A

    │

    └── possibly_related_to ──→ Entity-B

Reason

The evidence is suggestive but insufficient for a definitive relationship.

  

12. Merge

The Reviewer updates Shared-Graph.md.

Entity-A

    │

    └── possibly_related_to ──→ Entity-B

The graph now represents the current state.

The graph does not need to contain every rejected proposal.

The history remains in the Ledger.

  

13. Ledger Entry

Create:

06-Ledger/Events/LEDGER-001.md

---

type: ledger-event

ledger_id: LEDGER-001

timestamp: 2026-09-03

event_type: graph-update

actor: "[[Agent-Reviewer]]"

subject: "[[Entity-A]]"

object: "[[Entity-B]]"

decision: MODIFY

previous_state: unknown

new_state: possibly_related

related_changes:

  - CHANGE-001

  - CHANGE-002

related_decision: DECISION-001

---

Event

The shared graph was modified following conflicting proposals from two agents.

Sequence

1. Researcher proposed relationship.
2. Skeptic challenged relationship.
3. Conflict was identified.
4. Reviewer evaluated evidence.
5. Reviewer modified the proposed relationship.
6. Shared graph was updated.
7. Decision was recorded in the Ledger.

  

8. The Important Part — Learning

Create:

09-Feedback/Outcomes/OUTCOME-001.md

---

type: outcome

outcome_id: OUTCOME-001

related_decision: DECISION-001

---

Outcome

Later evidence becomes available.

New Evidence

Describe what happened.

Did the Decision Hold?

- Confirmed
- Partially confirmed
- Contradicted
- Still unresolved

Learning

What should the system change about future decisions?

  

15. The Complete Loop

           EXPERIENCE

                ↓

             CAPTURE

                ↓

          SHARED GRAPH

                ↓

        ┌───────┴───────┐

        ↓               ↓

   RESEARCHER        SKEPTIC

        ↓               ↓

   PROPOSAL A        PROPOSAL B

        └───────┬───────┘

                ↓

             CONFLICT

                ↓

             REVIEW

                ↓

          GOVERNED MERGE

                ↓

          SHARED GRAPH

                ↓

             LEDGER

                ↓

             ACTION

                ↓

            OUTCOME

                ↓

            LEARNING

                │

                └────────→ SHARED GRAPH

  

16. What This Prototype Tests

Test 1 — Shared State

Can multiple agents work against the same graph?

Test 2 — Agent Independence

Can agents maintain genuinely different interpretations?

Test 3 — Conflict

Can disagreement become an explicit object?

Test 4 — Governance

Can proposed changes be reviewed before becoming shared state?

Test 5 — Provenance

Can we determine why a relationship exists?

Test 6 — Temporal Memory

Can we reconstruct how the graph changed?

Test 7 — Learning

Can later outcomes change future reasoning?

  

17. The Architectural Insight

The prototype gives us four distinct objects:

AGENT

  = interpreter / actor

  

GRAPH

  = current relational state

  

LEDGER

  = historical continuity

  

GOVERNANCE

  = mechanism for changing shared state

And then a fifth:

FEEDBACK

  = mechanism through which the system learns

Together:

Agents + Graph + Governance + Ledger + Feedback

form a minimal experimental version of the larger Living Intelligence Mesh.

  

18. Future Extension

Once this works with two agents, scale it:

2 agents

   ↓

5 agents

   ↓

20 agents

   ↓

100+ agents

At that point the central problem changes.

It is no longer:

“How do we make an agent smarter?”

It becomes:

“How do we coordinate intelligence across many agents while preserving shared context, provenance, disagreement, and learning?”

That is where the Ledger becomes increasingly important.

And that is also where Lindenberg’s shared-graph/branch-and-merge thinking becomes directly relevant to the architecture.