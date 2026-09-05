
0. Core Loop

Experience → Capture → Graph → Agent Sensemaking → Proposed Change → Review → Ledger → Knowledge → Action → Feedback

The shared graph represents the current relational model.

The Ledger preserves the history of how that model came to be.

  

1. Vault Structure

Living-Intelligence-Mesh/

│

├── 00-System/

│   ├── Architecture.md

│   ├── Principles.md

│   ├── Ontology.md

│   └── Governance.md

│

├── 01-Entities/

│   ├── Agents/

│   ├── People/

│   ├── Organizations/

│   ├── Objects/

│   └── Concepts/

│

├── 02-Relationships/

│   ├── Relationship-Types.md

│   └── Relationship-Records/

│

├── 03-Experiences/

│   ├── Observations/

│   ├── Interactions/

│   └── Events/

│

├── 04-Agents/

│   ├── Agent-Registry.md

│   ├── Agent-Templates/

│   └── Agent-Records/

│

├── 05-Graph/

│   ├── Graph-Schema.md

│   ├── Graph-Views/

│   └── Proposed-Changes/

│

├── 06-Ledger/

│   ├── Ledger-Schema.md

│   ├── Events/

│   ├── Decisions/

│   ├── Beliefs/

│   └── Provenance/

│

├── 07-Knowledge/

│   ├── Insights/

│   ├── Patterns/

│   ├── Hypotheses/

│   └── Syntheses/

│

├── 08-Actions/

│   ├── Proposed/

│   ├── Approved/

│   └── Completed/

│

└── 09-Feedback/

    ├── Outcomes/

    ├── Evaluations/

    └── Learning/

  

2. The Shared Graph

The graph is the current relational state of the system.

It answers:

- What exists?
- What is connected?
- How are entities related?
- What does the system currently believe?
- What context surrounds an entity?

The graph should not be treated as the complete history.

That distinction belongs to the Ledger.

Graph

Current state

Ledger

History of state changes

This gives us:

Graph = What is true/currently represented

Ledger = How we got here

  

3. Agent Lifecycle

Every agent follows the same basic cycle:

OBSERVE

   ↓

READ CONTEXT

   ↓

REASON

   ↓

PROPOSE

   ↓

VALIDATE

   ↓

REVIEW

   ↓

MERGE

   ↓

LEARN

An agent should preferably propose graph changes rather than silently modifying shared state.

  

4. Agent Branching

When multiple agents work simultaneously:

                 Shared Graph

                      │

          ┌───────────┼───────────┐

          ↓           ↓           ↓

       Agent A     Agent B     Agent C

          │           │           │

       Branch A    Branch B    Branch C

          │           │           │

          └───────────┼───────────┘

                      ↓

                 Review Layer

                      ↓

              Conflict Resolution

                      ↓

                  Merge

                      ↓

                Shared Graph

                      ↓

                    Ledger

This prevents one agent from silently overwriting another agent’s interpretation.

  

5. Proposed Graph Change

Every agent-generated change should have a record.

Example:

---

type: graph-change

change_id: CHANGE-0001

agent: "[[Agent-Researcher]]"

target: "[[Entity-X]]"

change_type: relationship

status: proposed

confidence: 0.82

created: 2026-09-03

---

Proposed Change

Add relationship:

Entity-X → related_to → Entity-Y

Evidence

- Source:
- Observation:
- Supporting context:

Agent Reasoning

Why does the agent believe this relationship should exist?

Conflicts

Are there existing relationships that contradict this proposal?

Review

- Reviewer:
- Decision:
- Reason:

Result

- Accepted
- Rejected
- Modified
- Deferred

  

6. Agent Template

---

type: agent

agent_id:

name:

role:

version:

status: active

capabilities:

  - 

inputs:

  - 

outputs:

  - 

reads_from:

  - graph

  - ledger

writes_to:

  - proposed-changes

memory_policy:

governance_level:

---

Agent Purpose

What problem does this agent solve?

Role

What is this agent responsible for?

Inputs

What information can it access?

Context

What graph and Ledger context should it retrieve before acting?

Capabilities

What can the agent do?

Constraints

What is it forbidden to do?

Outputs

What does it produce?

Graph Operations

What kinds of nodes or relationships may it propose?

Evidence Requirements

What evidence must support a proposed change?

Confidence

How does the agent express uncertainty?

Conflict Behavior

What should happen when the agent disagrees with another agent?

Governance

Which changes require:

- automatic acceptance?
- human approval?
- another agent’s review?
- multi-agent consensus?

Learning

What feedback does the agent receive after its proposals are accepted or rejected?

  

7. Agent Registry

The registry provides a map of the agent population.

|   |   |   |   |   |
|---|---|---|---|---|
|Agent|Role|Reads|Writes|Authority|
|Researcher|Find evidence|Graph + Ledger|Proposed changes|Low|
|Synthesizer|Connect evidence|Graph + Ledger|Insights|Medium|
|Reviewer|Evaluate changes|Graph + proposals|Decisions|High|
|Coordinator|Manage workflows|Entire system|Actions|High|

These are example roles, not requirements.

  

8. Ledger Entry Template

---

type: ledger-entry

ledger_id:

timestamp:

actor:

actor_type:

event_type:

subject:

action:

previous_state:

new_state:

evidence:

confidence:

provenance:

related_changes:

---

Event

What happened?

Context

What was known at the time?

Interpretation

What did the agent/system believe it meant?

Action

What happened as a result?

Outcome

What actually happened?

Learning

What should change because of this outcome?

  

9. Conflict Resolution

When two agents disagree:

Agent A proposes X

Agent B proposes Y

        ↓

Conflict detected

        ↓

Compare evidence

        ↓

Compare provenance

        ↓

Compare confidence

        ↓

Check ontology constraints

        ↓

Review

        ↓

X / Y / revised hypothesis

        ↓

Merge

        ↓

Record decision in Ledger

The important point:

The conflict itself becomes data.

A disagreement shouldn’t disappear once resolved.

The Ledger should remember:

Agent A believed X.  
Agent B believed Y.  
Evidence E was considered.  
Decision D was made.  
Later outcome O confirmed/contradicted the decision.

That is where the system begins to acquire learning history.

  

10. Belief Model

This is an important extension of the graph.

Instead of simply storing:

A → related_to → B

we can represent:

Agent A

   │

   ├── believes

   ↓

Relationship R

   │

   ├── confidence: 0.82

   ├── evidence: E

   ├── created: T1

   └── status: active

Now beliefs can change over time.

Belief₁

   ↓

Evidence

   ↓

Belief₂

   ↓

Evidence

   ↓

Belief₃

The system therefore has not just memory, but belief evolution.

  

11. The Complete Architecture

             AGENTS / ENTITIES

                     │

                     ↓

             RELATIONSHIPS

                     │

                     ↓

          EXPERIENCE / EVENTS

                     │

                     ↓

              FIELDY / CAPTURE

                     │

                     ↓

             SHARED GRAPH

                     ↕

                  AGENTS

                     │

                     ↓

             PROPOSED CHANGES

                     │

                     ↓

           REVIEW / GOVERNANCE

                     │

                     ↓

                  MERGE

                     │

                     ↓

                 LEDGER

                     │

          ┌──────────┼──────────┐

          ↓          ↓          ↓

       MEMORY     BELIEFS    PROVENANCE

          │          │          │

          └──────────┼──────────┘

                     ↓

                SENSEMAKING

                     ↓

                 KNOWLEDGE

                     ↓

                  ACTION

                     ↓

                 FEEDBACK

                     │

                     └──────────→ EXPERIENCE

Core Principle

The graph represents relationships.

The Ledger represents continuity.

Agents create interpretations.

Governance determines what becomes shared state.

Feedback determines what the system learns.

This gives us a potentially powerful distinction:

The intelligence is not the graph, the agents, or the model individually. It emerges from the interaction between them across time.