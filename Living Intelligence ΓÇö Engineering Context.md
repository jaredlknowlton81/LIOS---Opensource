
Purpose

This repository is the engineering environment for building a persistent, relational intelligence system.

The system is intended to accumulate context across time rather than treating each interaction as isolated.

The core loop is:

Experience → Capture → Intelligence → Knowledge → Action → Feedback → Experience

The engineering system must preserve both:

1. Runtime learning — what the intelligence learns from experience.
2. Engineering learning — what we learn while building the intelligence.

  

3. Core Architecture

The system consists of the following layers:

                         EXPERIENCE

                              │

                              ▼

                           FIELDY

                         CAPTURE

                              │

                              ▼

                     RUNTIME LEDGER

                              │

              ┌───────────────┼───────────────┐

              ▼               ▼               ▼

           MEMORY          PROJECTS        KNOWLEDGE

              │               │               │

              │               │            Obsidian

              │               │

              └───────────────┼───────────────┘

                              ▼

                       MORNING BRIEF

                              │

                              ▼

                        CONVERSATION

                              │

                              ▼

                         EXPERIENCE

The engineering layer operates alongside this:

                  ENGINEERING LEDGER

                          │

                          ▼

                       HARNESS

                          │

                          ▼

                  SYSTEM VERIFICATION

                          │

                          ▼

                  ENGINEERING LEDGER

  

2. Runtime Ledger

The Runtime Ledger is the canonical historical substrate for the intelligence.

It records what happened and how the system currently understands what happened.

A Runtime Ledger entry should preserve, where applicable:

- experience
- timestamp
- participants
- entities
- relationships
- theme
- project context
- raw evidence
- interpretation
- confidence
- provenance
- related memories
- related experiences
- contradictions
- changes in understanding
- resulting actions

Important principle

Do not silently rewrite historical experience.

Separate:

Evidence  
from  
Interpretation  
from  
Confidence

For example:

Evidence:

"The user said X."

  

Interpretation:

"X appears to mean Y."

  

Confidence:

0.82

If later evidence contradicts an interpretation, preserve the earlier interpretation and record the change.

Historical truth should remain recoverable.

  

3. Memory

Memory is the consolidated context derived from experiences.

Memory is not identical to the Runtime Ledger.

The distinction is:

Runtime Ledger  
→ What happened and how understanding evolved.

Memory  
→ What should be carried forward as useful context.

Memory may be represented through:

- structured records
- semantic/vector representations
- relational/graph representations
- associations
- summaries

Multiple representations should retain a common identity so that they can be traced back to the underlying experience.

  

4. Confidence

Interpretations and inferred relationships must use a confidence gradient.

Do not force uncertain conclusions into binary true/false states.

Represent uncertainty explicitly.

Example:

confidence: 0.94

status: high-confidence interpretation

confidence: 0.61

status: tentative interpretation

When confidence is sufficiently low that proceeding could meaningfully distort context, ask for clarification.

Clarification should be brief.

Preferred format:

I think you're saying:

[brief interpretation]

  

Confidence: 68%

  

Is that right?

User corrections should become new evidence and should update the relevant context.

  

5. Themes and Threads

The intelligence should continuously look for:

- recurring themes
- continuing threads
- related concepts
- relationships between ideas
- connections to previous conversations
- connections to active projects
- reinforcement of existing memory
- contradictions with existing memory
- emerging patterns

Do not treat each conversation as an isolated unit.

A current conversation may be a continuation of a thread that began many conversations earlier.

When a strong connection exists, preserve that relationship.

  

6. Projects

Projects represent persistent intention.

A Project answers:

What are we trying to accomplish, understand, build, or change?

A Project should maintain:

- purpose
- current objective
- current state
- history
- active threads
- key decisions
- open questions
- related memories
- related knowledge
- experiments
- next actions

Project context should influence retrieval.

When processing a new experience, determine whether it relates to an active Project.

Do not create a new project merely because a new topic appears.

Prefer connecting new information to an existing project when the relationship is meaningful.

  

7. Obsidian / Knowledge

Obsidian is a knowledge layer, not a dump for every interaction.

Use it to crystallize durable knowledge that is worth preserving, developing, connecting, or revisiting.

A conversation does not automatically become an Obsidian note.

Prefer:

Conversation

    ↓

Insight

    ↓

Repeated / validated / important

    ↓

Knowledge artifact

    ↓

Obsidian

Obsidian should remain human-readable and conceptually organized.

The Runtime Ledger remains the historical substrate.

  

8. Morning Brief

The Morning Brief is a synthesis and reactivation mechanism.

It should not merely summarize yesterday.

It should examine:

- recent experiences
- Runtime Ledger changes
- active Projects
- important memories
- newly crystallized knowledge
- emerging themes
- unresolved questions
- uncertain interpretations
- relevant external developments

Then identify:

What matters now?

The Morning Brief creates active context for the next period of conversation and work.

It is primarily a synthesis layer, not the canonical storage layer.

  

9. Engineering Ledger

The Engineering Ledger records the development history of the intelligence system.

It should preserve:

- architectural decisions
- design rationale
- hypotheses
- experiments
- implementation changes
- test results
- failures
- discovered limitations
- assumptions
- unresolved questions
- rejected approaches
- evidence supporting decisions
- lessons learned

Use the following developmental pattern:

Question

   ↓

Hypothesis

   ↓

Implementation

   ↓

Test

   ↓

Result

   ↓

Decision

   ↓

Next Question

Do not erase failed approaches simply because they were replaced.

Failures are engineering knowledge.

  

10. CLAUDE.md vs Engineering Ledger

CLAUDE.md is the current operating context for the engineering agent.

It answers:

How should an agent work on this system right now?

The Engineering Ledger answers:

What have we learned while building this system?

Therefore:

CLAUDE.md

    ↓

Current operating instructions

  

Engineering Ledger

    ↓

Historical engineering knowledge

Do not use CLAUDE.md as a replacement for the Engineering Ledger.

When an engineering decision becomes important enough to affect future work, record its rationale in the Engineering Ledger and update CLAUDE.md with the resulting current rule when appropriate.

  

11. Harness

The Harness is the verification layer around the system.

It must test not only whether individual components function, but whether the intelligence loop actually works.

Important verification categories include:

Memory

Can an experience be stored and retrieved later?

Context

Does retrieval include relevant historical context?

Relationships

Can the system recover meaningful connections between entities and experiences?

Projects

Does current Project context influence interpretation and retrieval?

Confidence

Does the system distinguish strong conclusions from uncertain ones?

Contradiction

Can new evidence change an existing interpretation without destroying historical evidence?

Learning

Does repeated experience change future behavior or retrieval?

Engineering

Can the system explain why an architectural decision exists and what evidence supports it?

The Harness should produce evidence that can be recorded in the Engineering Ledger.

  

12. Provenance

Whenever practical, important conclusions should be traceable to their source.

Prefer:

Conclusion

    ↓

Memory

    ↓

Experience

    ↓

Original evidence

Do not manufacture provenance.

If the origin of a conclusion is unknown, represent that uncertainty explicitly.

  

13. Preserve the Distinctions

Do not collapse these concepts into one system merely because they are related.

Conversation

→ where experience and reasoning occur

  

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

  

Harness

→ verification and evidence

These layers should cooperate without becoming indistinguishable.

  

14. General Engineering Principles

Prefer evidence over assumption.

If the implementation does not support an assumption, investigate it.

Preserve history.

Do not destroy information merely to create a cleaner current state.

Separate observation from interpretation.

The system must be able to distinguish what happened from what it thinks happened.

Represent uncertainty.

A tentative inference is preferable to an unsupported certainty.

Preserve relationships.

Context is not merely a collection of facts. Relationships between experiences, entities, projects, and ideas are part of the intelligence.

Make important decisions traceable.

Future agents should be able to understand why the architecture looks the way it does.

Test the loop, not just the components.

A functioning database does not prove that the intelligence remembers.

A functioning vector search does not prove that the intelligence understands context.

A passing unit test does not prove that learning is occurring.

Verify behavior at the system level.

  

15. Current Architectural Hypothesis

The current working hypothesis is:

Persistent intelligence emerges from accumulated experience plus persistent relational context plus the ability to retrieve, interpret, act, and learn from that history.

The Runtime Ledger is therefore considered a foundational component rather than merely a storage mechanism.

The Engineering Ledger provides the analogous persistent context for the development of the system itself.

The long-term architecture should allow both layers to evolve through evidence and feedback.

  

16. When Unsure

Do not silently invent architecture.

When an important decision is ambiguous:

1. Identify the ambiguity.
2. State the competing interpretations.
3. Determine what evidence already exists.
4. Ask for clarification if necessary.
5. Record the resulting decision.
6. Update the appropriate ledger.
7. Update current operating instructions if the decision changes how future work should proceed.

The goal is not merely to make the next change work.

The goal is to make the system increasingly understandable, testable, persistent, and capable of learning from its own history.