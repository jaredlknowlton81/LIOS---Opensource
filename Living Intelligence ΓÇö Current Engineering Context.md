
This file represents the current state of the system.  
It is a working projection of the Engineering Ledger, not a replacement for the historical ledger.

Current Objective

Build a persistent, relational intelligence system that can accumulate context across time, recognize themes and relationships, learn from experience, and use that accumulated context to improve future interactions and actions.

The immediate focus is the architecture of persistent context and memory.

  

Current Core Model

The current working model is:

Experience → Capture → Intelligence → Knowledge → Action → Feedback → Experience

Expanded:

Agents / Entities

       ↓

Relationships

       ↓

Interaction / Experience

       ↓

Fieldy / Capture

       ↓

Runtime Ledger

       ↓

Memory / Sensemaking

       ↓

Knowledge

       ↓

Projects / Action

       ↓

Feedback

       ↓

New Experience

  

Two-Ledger Architecture

We have established that the system requires two different forms of persistent history.

Runtime Ledger

The Runtime Ledger records the history of the intelligence’s experiences and evolving understanding.

It answers:

What happened, what did we learn from it, and how does it connect to everything else?

It should preserve:

- experiences
- observations
- entities
- relationships
- themes
- project context
- evidence
- interpretations
- confidence
- provenance
- related memories
- contradictions
- changes in understanding
- resulting actions

The Runtime Ledger is the canonical historical substrate.

  

Engineering Ledger

The Engineering Ledger records the history of building the intelligence system.

It answers:

What have we learned while building the system, and why does the architecture look the way it does?

It should preserve:

- architectural decisions
- design rationale
- hypotheses
- experiments
- implementation changes
- test results
- failures
- limitations
- assumptions
- rejected approaches
- evidence
- lessons learned
- unresolved questions

The Engineering Ledger is the developmental memory of the system.

  

CLAUDE.md vs CONTEXT.md vs Engineering Ledger

These are intentionally different.

CLAUDE.md

    ↓

How should an engineering agent work?

  

CONTEXT.md

    ↓

Where is the system right now?

  

ENGINEERING LEDGER

    ↓

How did the system get here?

CLAUDE.md contains relatively stable operating principles.

CONTEXT.md contains the current state required to continue work effectively.

The Engineering Ledger contains the historical record.

When the current state changes, CONTEXT.md should be updated.

When an important architectural decision or lesson is discovered, it should be recorded in the Engineering Ledger.

  

Runtime Memory Model

Memory should not be treated as a single text blob.

The current architectural hypothesis is:

Experience

    ↓

Runtime Ledger

    ↓

Memory formation / consolidation

    ↓

Multiple representations

Potential representations include:

- structured records
- semantic/vector representations
- graph relationships
- learned associations
- summaries

All representations should maintain a common identity so they can be traced back to their originating experience.

  

Evidence vs Interpretation

The system must distinguish between:

EVIDENCE

"What actually occurred or was explicitly stated."

  

INTERPRETATION

"What the intelligence believes the evidence means."

  

CONFIDENCE

"How certain is the interpretation?"

Example:

Evidence:

The user said X.

  

Interpretation:

X appears to mean Y.

  

Confidence:

0.82

Historical evidence should not be silently overwritten when interpretations change.

  

Confidence Model

The intelligence should represent uncertainty on a gradient rather than as binary certainty.

Current working representation:

confidence = 0.00 → 1.00

Confidence applies primarily to:

- interpretations
- inferred relationships
- thematic connections
- assumptions
- predictions

High-confidence interpretations can generally proceed without interruption.

Low-confidence interpretations should trigger clarification when proceeding could meaningfully distort context.

Preferred clarification format:

I think you're saying:

  

[brief interpretation]

  

Confidence: 68%

  

Is that right?

User confirmation or correction becomes new evidence and should update the relevant Runtime Ledger context.

  

Themes and Threads

The intelligence should continuously search for:

- common themes
- recurring ideas
- continuing threads
- relationships between concepts
- connections to previous conversations
- connections to active projects
- reinforcement of existing memory
- contradictions
- emerging patterns

A conversation should not automatically be treated as an isolated event.

A current conversation may be a continuation of a thread that began much earlier.

  

Projects

Projects represent persistent intention.

A Project answers:

What are we trying to accomplish, understand, build, or change?

Projects should maintain:

- purpose
- current objective
- current state
- history
- active threads
- decisions
- open questions
- related memories
- related knowledge
- experiments
- next actions

Project context should influence retrieval.

New information should be connected to an existing Project when the relationship is meaningful rather than creating unnecessary new projects.

  

Obsidian / Knowledge Layer

Obsidian is the durable, human-readable knowledge layer.

It should not become a dump of every conversation.

Preferred flow:

Conversation

    ↓

Insight

    ↓

Repeated / validated / important

    ↓

Knowledge artifact

    ↓

Obsidian

The Runtime Ledger preserves history.

Obsidian crystallizes knowledge.

A single Obsidian note may eventually represent knowledge derived from many Runtime Ledger experiences.

  

Morning Brief

The Morning Brief is a synthesis and reactivation mechanism.

It should examine:

- recent experiences
- Runtime Ledger changes
- active Projects
- important memories
- knowledge artifacts
- emerging themes
- unresolved questions
- uncertain interpretations
- relevant external developments

The key question is:

What matters now?

The Morning Brief should bring accumulated context back into active attention.

It is primarily a synthesis layer, not the canonical storage layer.

  

Current System Loop

The current conceptual loop is:

                 EXPERIENCE

                      ↓

                   FIELDY

                 CAPTURE

                      ↓

              RUNTIME LEDGER

                      ↓

          ┌───────────┼───────────┐

          ↓           ↓           ↓

       MEMORY      PROJECTS     KNOWLEDGE

          ↓           ↓           ↓

          └───────────┼───────────┘

                      ↓

               MORNING BRIEF

                      ↓

                 CONVERSATION

                      ↓

                  EXPERIENCE

The loop should continuously accumulate context rather than reset after each conversation.

  

Engineering Loop

The engineering side operates in parallel:

Question

   ↓

Hypothesis

   ↓

Implementation

   ↓

Harness / Test

   ↓

Observation

   ↓

Result

   ↓

Decision

   ↓

Engineering Ledger

   ↓

Updated System

   ↓

Next Question

Failures should be preserved as engineering knowledge rather than simply erased after being fixed.

  

Harness

The Harness is the verification layer.

It should eventually verify not just individual functions but the behavior of the entire intelligence loop.

Important categories:

Persistence

Can an experience be stored and retrieved later?

Context

Does retrieval bring back relevant historical context?

Relationships

Can the system recover meaningful relationships between entities and experiences?

Themes

Can the system recognize recurring or connected themes?

Projects

Does Project context influence retrieval and interpretation?

Confidence

Does the system distinguish strong conclusions from uncertain ones?

Clarification

Does low-confidence reasoning appropriately request confirmation?

Contradiction

Can new evidence change an interpretation without destroying historical evidence?

Learning

Does repeated experience change future retrieval, memory, or behavior?

Engineering

Can the system explain why an architectural decision exists and what evidence supports it?

  

Current Architectural Insight

The most important current insight is:

Persistent intelligence is not created by storing more text. It emerges from accumulated experience plus persistent relational context plus the ability to retrieve, interpret, act, and learn from history.

Therefore:

Ledger ≠ Database

Memory ≠ Ledger

Vector index ≠ Memory

Graph ≠ Memory

Obsidian ≠ Ledger

Project ≠ Memory

These are complementary layers.

  

Current Layer Definitions

Conversation

→ where experience and reasoning occur

  

Fieldy

→ capture layer

  

Runtime Ledger

→ persistent history of experience and interpretation

  

Memory

→ consolidated context carried forward

  

Projects

→ persistent intention and direction

  

Obsidian

→ durable human-readable knowledge

  

Morning Brief

→ synthesis and reactivation

  

Engineering Ledger

→ history of building and learning about the system

  

CONTEXT.md

→ current engineering state

  

CLAUDE.md

→ current engineering operating instructions

  

Harness

→ verification and evidence

  

Current Open Questions

Runtime Ledger

1. What is the exact atomic unit of a Runtime Ledger entry?
2. Is the fundamental unit an experience, event, observation, or interaction?
3. Which fields are mandatory?
4. How should experiences be linked together temporally?
5. How should relationships evolve over time?

Memory

6. When does an experience become a consolidated memory?
7. When should memories merge?
8. When should memories remain separate?
9. How should contradictory memories be represented?
10. How should memory decay or archival work?

Confidence

11. What confidence threshold should trigger clarification?
12. Should confidence be assigned by the model, derived from evidence, or both?
13. How should user corrections modify confidence?

Retrieval

14. How should semantic, relational, temporal, and project-based retrieval be combined?
15. How should the system determine which context is relevant rather than simply retrieving everything?

Projects

16. When does a conversation become part of an existing Project?
17. When should a new Project be created?
18. How should Project state evolve from Runtime Ledger evidence?

Knowledge

19. When should Runtime Ledger information become an Obsidian knowledge artifact?
20. How should knowledge artifacts remain connected to their source experiences?

Morning Brief

21. What determines what deserves attention?
22. How should emerging themes be detected?
23. How should unresolved questions be surfaced?

Engineering

24. How should the Engineering Ledger be structured?
25. What belongs in historical engineering memory versus CONTEXT.md?
26. How should the Harness automatically produce evidence for Engineering Ledger entries?

  

Current Next Step

The next concrete design task is to define the Runtime Ledger schema and lifecycle.

Specifically:

Experience

    ↓

Capture

    ↓

Ledger Entry

    ↓

Observation / Interpretation

    ↓

Confidence

    ↓

Entity + Relationship extraction

    ↓

Memory formation

    ↓

Indexing

    ↓

Retrieval

    ↓

Sensemaking

    ↓

Action

    ↓

Feedback

    ↓

New Experience

The schema should be designed before choosing the final storage technologies.

The guiding principle is:

Preserve the history first. Optimize retrieval second.

  

Current Working Hypothesis

The system should ultimately maintain two continuously evolving histories:

RUNTIME HISTORY

"What has the intelligence experienced and learned?"

  

ENGINEERING HISTORY

"What have we learned while building the intelligence?"

The first enables intelligence to evolve.

The second enables the architecture to evolve.

The Harness provides evidence that both forms of evolution are actually occurring.