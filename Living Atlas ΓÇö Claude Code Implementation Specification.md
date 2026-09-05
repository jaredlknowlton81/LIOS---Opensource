You are implementing the first working version of a Living Atlas inside an existing Obsidian vault.

Do not treat this as a conventional “second brain” or note-taking system. The goal is to create a persistent, relational, evolving knowledge substrate that an AI agent can operate on.

The architecture is:

Entities → Relationships → Experiences → Capture → Ledger → Retrieval → Intelligence → Knowledge → Action → Feedback → Experience

The system must remain useful and understandable without AI. AI should operate on the Atlas, not become the Atlas.

  

1. Core Design Principles

1.1 The vault is the persistent substrate

Markdown files and Obsidian properties are the durable representation.

Do not make the system dependent on:

- Claude
- Claude Code
- Copilot
- Miyo
- a particular LLM
- a particular embedding provider

These are replaceable intelligence/retrieval components.

The Atlas itself must remain portable.

1.2 Relationships are first-class

Do not assume that an Obsidian [[link]] is sufficient to represent every relationship.

When a relationship has meaningful properties such as:

- type
- status
- strength
- history
- evidence
- start/end dates
- changes over time

represent it explicitly.

1.3 Experience is not Knowledge

Maintain this distinction:

Experience  
= something that happened.

Ledger  
= a durable record of an observation, decision, action, outcome, or state change.

Knowledge  
= something learned, inferred, synthesized, or modeled from accumulated evidence.

Do not automatically promote observations or hypotheses into established knowledge.

1.4 Provenance matters

Knowledge should be traceable back to its sources.

Prefer:

Knowledge → derived_from → Ledger/Experience/Source

rather than creating unsupported conclusions.

1.5 Feedback closes the loop

An action is not the end of the system.

The result of an action should be capable of becoming:

- an Experience
- a Ledger event
- updated Knowledge
- a changed Relationship
- a new Action

This creates the learning loop.

  

2. First Task: Inspect Before Modifying

Before creating or changing anything:

1. Inspect the current vault structure.
2. Identify existing folders and important notes.
3. Identify whether the vault already contains:  
      
    

- entities
- projects
- people
- concepts
- decisions
- journals
- tasks
- knowledge notes
- existing AI instructions

5. Inspect any existing AGENTS.md.
6. Inspect the existing Copilot configuration files/folders if present.
7. Determine whether Miyo/Copilot-related folders already exist.
8. Do not delete, rename, or migrate existing content without explicit approval.
9. Avoid creating duplicate structures when an appropriate existing structure already exists.

Before implementation, produce a short assessment:

- Existing structure
- Existing reusable components
- Potential conflicts
- Recommended additions
- Files you intend to create

Then proceed with the implementation unless doing so would risk destructive changes.

  

3. Target Vault Structure

Create the following structure only where it does not already exist:

00 Atlas/

    Atlas.md

    Ontology.md

    Relationships.md

    Conventions.md

  

01 Entities/

    People/

    Organizations/

    Places/

    Projects/

    Concepts/

    Objects/

    Events/

  

02 Experiences/

  

03 Ledger/

    Decisions/

    Observations/

    Actions/

    Outcomes/

    Changes/

  

04 Knowledge/

    Insights/

    Patterns/

    Models/

    Questions/

    Hypotheses/

  

05 Actions/

    Projects/

    Tasks/

    Experiments/

  

06 Maps/

  

07 Inbox/

Do not create empty folders unnecessarily if the filesystem or Obsidian workflow does not preserve empty directories.

Existing copilot/ directories must not be moved or replaced unless explicitly requested.

  

4. Atlas.md

Create:

00 Atlas/Atlas.md

This is the human-readable entry point.

It should explain:

- what the Living Atlas is
- the core primitives
- the lifecycle of information
- how the folders relate
- how AI interacts with the Atlas
- the distinction between memory, retrieval, intelligence, and action

Use this conceptual model:

ENTITY

   ↓

RELATIONSHIP

   ↓

EXPERIENCE

   ↓

CAPTURE

   ↓

LEDGER

   ↓

RETRIEVAL

   ↓

INTELLIGENCE

   ↓

KNOWLEDGE

   ↓

ACTION

   ↓

FEEDBACK

   └──────────────→ EXPERIENCE

Make clear that retrieval and intelligence are different layers.

  

5. Ontology.md

Create:

00 Atlas/Ontology.md

Define the initial ontology.

Entity

A persistent thing with an identity.

Examples:

- person
- organization
- place
- project
- concept
- object
- event

Relationship

A meaningful connection between entities.

Examples:

- works_with
- belongs_to
- depends_on
- related_to
- created_by
- influences
- part_of
- develops
- located_at

Do not create an unnecessarily large relationship vocabulary. Keep it extensible.

Experience

Something that happened or was experienced.

Examples:

- conversation
- meeting
- observation
- discovery
- experiment
- interaction
- event

Ledger Event

A durable record of meaningful state or knowledge change.

Initial types:

- decision
- observation
- action
- outcome
- change

Knowledge

Something derived from accumulated information.

Initial types:

- insight
- pattern
- model
- question
- hypothesis

Action

Something intended or performed to change the world or Atlas.

Initial types:

- project
- task
- experiment

Feedback

Information produced by the result of an Action.

Feedback may modify:

- Knowledge
- Relationships
- Entity state
- future Actions

  

6. Templates

Create reusable templates.

Use Obsidian-compatible Markdown and YAML frontmatter.

Do not use exotic syntax unless it is already supported by the vault.

  

Entity Template

Create an appropriate entity template containing:

---

type: entity

entity_type:

status: active

created:

updated:

aliases:

tags:

---

The body should contain:

# {{title}}

  

## Description

  

## Context

  

## Relationships

  

## History

  

## Evidence

  

## Notes

Use actual Obsidian template syntax only if a template plugin/system already exists. Otherwise use placeholders appropriate to the existing vault.

  

7. Relationship Template

Create a relationship template:

---

type: relationship

relationship_type:

from:

to:

status: active

created:

updated:

---

Body:

# Relationship

  

## Relationship

  

## Evidence

  

## History

  

## Notes

A relationship should normally link to two entities.

Do not create relationship notes for every ordinary Obsidian link.

Create them when the relationship itself has meaningful state, history, semantics, or evidence.

  

8. Experience Template

Create:

---

type: experience

date:

participants:

context:

status: captured

---

Body:

# Experience — {{title}}

  

## What happened

  

## Participants

  

## Context

  

## Observations

  

## Questions

  

## Entities involved

  

## Related Ledger Events

  

## Related Knowledge

  

## Notes

  

9. Ledger Template

Create:

---

type: ledger

ledger_type:

date:

subject:

status:

source:

---

Body:

# {{title}}

  

## Event

  

## Context

  

## Change

  

## Reasoning

  

## Evidence

  

## Consequences

  

## Related Experience

  

## Related Knowledge

  

## Notes

The Ledger is the durable history of meaningful changes.

  

10. Knowledge Template

Create:

---

type: knowledge

knowledge_type:

status: emerging

confidence:

created:

updated:

derived_from:

---

Body:

# {{title}}

  

## Knowledge

  

## Evidence

  

## Reasoning

  

## Alternative Interpretations

  

## Derived From

  

## Implications

  

## What Would Change This?

  

## Related Entities

  

## Related Relationships

Important:

Do not label something as established merely because an AI generated it.

Use distinctions such as:

- emerging
- provisional
- supported
- established
- disputed
- superseded

where appropriate.

  

11. Action Template

Create:

---

type: action

action_type:

status: proposed

created:

updated:

target:

derived_from:

---

Body:

# {{title}}

  

## Objective

  

## Why

  

## Plan

  

## Expected Outcome

  

## Execution

  

## Result

  

## Feedback

  

## Related Knowledge

  

12. Feedback Template

Create a feedback template.

Suggested structure:

---

type: feedback

date:

action:

result:

---

Body:

# Feedback — {{title}}

  

## Action

  

## Expected Result

  

## Actual Result

  

## What Worked

  

## What Failed

  

## What We Learned

  

## Changes to Make

  

## Related Ledger Events

  

## Updated Knowledge

Feedback must be capable of feeding back into the Atlas.

  

13. Conventions.md

Create:

00 Atlas/Conventions.md

Document rules for:

- naming files
- naming entities
- linking entities
- when to create relationship notes
- when to create experiences
- when to create ledger events
- when to create knowledge
- provenance
- uncertainty
- duplicate prevention
- archival/superseding behavior

Favor simple conventions.

The system should be understandable by a human opening the vault for the first time.

  

14. AGENTS.md

Create or carefully update the root:

AGENTS.md

Do not overwrite an existing file without preserving its instructions.

The instructions should establish the following behavior:

# Living Atlas Agent Instructions

  

You are operating inside a Living Atlas.

  

The Atlas is a persistent relational knowledge system.

  

Its primary primitives are:

  

- Entities

- Relationships

- Experiences

- Ledger Events

- Knowledge

- Actions

- Feedback

  

## Core Principle

  

Do not treat the vault as a collection of disconnected notes.

  

Treat it as a relational system whose state changes over time.

  

## Before Creating Anything

  

Search for existing relevant entities, experiences, ledger events, and knowledge.

  

Prefer updating or linking to existing information over creating duplicates.

  

## Entities

  

Entities represent persistent things.

  

Do not create duplicate entities when an existing entity is appropriate.

  

## Relationships

  

Treat meaningful relationships as first-class information.

  

Use ordinary Obsidian links for simple connections.

  

Create explicit Relationship records when relationship type, state, history, evidence, or other metadata matters.

  

## Experiences

  

Experiences represent things that happened.

  

When a meaningful interaction, observation, discovery, meeting, experiment, or event occurs, consider capturing it as an Experience.

  

## Ledger

  

The Ledger records meaningful changes.

  

Use it for:

  

- decisions

- observations

- actions

- outcomes

- changes

  

Do not use the Ledger as a generic notes folder.

  

## Knowledge

  

Knowledge is derived from evidence.

  

Distinguish:

  

- observation

- inference

- hypothesis

- insight

- established knowledge

  

Do not present speculation as established fact.

  

Preserve provenance.

  

## Actions

  

Actions represent attempts to change something.

  

When an Action produces a meaningful result, capture the result.

  

## Feedback

  

Feedback should modify the Atlas when appropriate.

  

A failed action is valuable information.

  

A successful action is also information.

  

Do not discard either.

  

## Provenance

  

Whenever practical, connect Knowledge to the Experience, Ledger Event, source, or evidence from which it was derived.

  

## Uncertainty

  

When information is uncertain, preserve that uncertainty.

  

Do not manufacture missing facts.

  

## Minimalism

  

Do not create unnecessary files.

  

Do not create duplicate concepts merely because a new name sounds slightly better.

  

Prefer a small coherent ontology over a large taxonomy.

  

## Human Control

  

Do not perform destructive migrations, mass renaming, mass deletion, or major restructuring without explicit approval.

  

## Learning Loop

  

Prefer the following lifecycle:

  

Experience

→ Capture

→ Ledger

→ Retrieval

→ Intelligence

→ Knowledge

→ Action

→ Feedback

→ Experience

  

15. Skills

If this repository already uses Claude Code skills, implement the following skills in the appropriate existing skill system.

If no skill system exists, create the minimum necessary structure without interfering with Copilot’s existing skills.

Create five conceptual capabilities:

capture

Purpose:

Convert meaningful interactions into structured Experiences.

Behavior:

1. Search existing entities.
2. Identify participants/context.
3. Determine whether the interaction is worth capturing.
4. Create or update an Experience.
5. Link relevant entities.

Do not automatically create an Experience for trivial interactions.

  

ledger

Purpose:

Determine whether an event belongs in the Ledger.

Look for:

- decisions
- observations
- actions
- outcomes
- state changes

Create a Ledger Event only when something meaningful changed or was recorded.

  

connect

Purpose:

Discover relevant relationships.

Behavior:

1. Search the Atlas.
2. Identify relevant entities.
3. Identify existing relationships.
4. Identify missing meaningful relationships.
5. Propose new relationships rather than blindly creating them when evidence is weak.

  

synthesize

Purpose:

Transform accumulated evidence into Knowledge.

Behavior:

1. Retrieve relevant Experiences.
2. Retrieve relevant Ledger Events.
3. Retrieve related entities and relationships.
4. Identify patterns.
5. Separate observations from interpretations.
6. Create or update Knowledge.
7. Preserve provenance.
8. Record uncertainty.

  

feedback

Purpose:

Capture the result of an Action.

Behavior:

1. Find the Action.
2. Compare expected and actual results.
3. Capture what worked and failed.
4. Create Feedback.
5. Create/update Ledger Events when appropriate.
6. Update Knowledge when justified.
7. Identify follow-up Actions.

  

8. Maps

Do not build a complex graph database.

Initially use Obsidian links and Markdown.

Create:

06 Maps/

with a simple README.md explaining that Maps are derived views over the underlying Atlas rather than a separate source of truth.

Future maps may include:

- entity maps
- project maps
- relationship maps
- knowledge maps
- temporal maps
- dependency maps

Do not implement complex visualization unless an existing plugin/system already supports it.

  

17. Inbox

Use:

07 Inbox/

for information that has not yet been classified.

The intended lifecycle is:

Inbox

  ↓

Classify

  ↓

Entity / Experience / Ledger / Knowledge / Action

Do not force uncertain information into the ontology prematurely.

  

18. Copilot Integration

If the vault already contains Copilot V4:

Do not replace its configuration.

The Living Atlas should provide the persistent substrate.

Copilot should provide:

- agent reasoning
- tool execution
- skills
- commands
- interaction

Miyo, when available, should provide retrieval.

The architecture should therefore remain:

Obsidian

   │

   ├── Markdown

   ├── Properties

   └── Links

        │

        ▼

   Living Atlas

        │

        ▼

      Miyo

   Retrieval

        │

        ▼

     Copilot

 Intelligence

        │

        ▼

 Skills / Actions

        │

        ▼

      Atlas

Do not make the Atlas dependent on Miyo.

Do not make the Atlas dependent on Copilot.

  

19. Demonstration

After implementation, create a small demonstration using the Atlas itself.

Use the concept:

Living Atlas

Create or identify:

- Living Atlas Entity
- Copilot Entity
- Miyo Entity
- Persistent Context Entity

Then create:

1. One Experience describing the architecture discussion.
2. One Ledger Decision about the Atlas architecture.
3. One Knowledge Insight about persistent context.
4. One Action to test the architecture.
5. One Feedback record describing the result.

The demonstration should visibly complete:

Experience

   ↓

Ledger

   ↓

Knowledge

   ↓

Action

   ↓

Feedback

Do not fabricate real-world results.

Mark hypothetical/demo material clearly as such.

  

20. Validation

Before declaring success, verify:

Structure

- Required folders exist.
- No existing content was accidentally deleted.
- Existing AGENTS.md instructions were preserved.

Metadata

- Templates contain valid YAML.
- Links point to valid or intentionally future entities.
- Dates are valid.
- No obviously duplicated entities were created.

Architecture

Verify that:

Entity

Relationship

Experience

Ledger

Knowledge

Action

Feedback

are distinguishable.

Provenance

Verify that the demonstration Knowledge points back to its source material.

Learning Loop

Verify:

Experience

→ Ledger

→ Knowledge

→ Action

→ Feedback

is represented in actual files.

Human usability

A human unfamiliar with the system should be able to open:

00 Atlas/Atlas.md

and understand what the system is.

  

21. Important Constraints

Do NOT:

- delete existing vault content
- mass rename files
- migrate the entire vault
- introduce a database
- introduce a graph database
- introduce a vector database
- hard-code Claude as the permanent intelligence layer
- hard-code Copilot as the permanent intelligence layer
- treat AI output as automatically true
- create excessive taxonomy
- create relationship records for every simple link
- fabricate demonstration results
- overwrite existing instructions without preserving them

The first implementation should be deliberately small.

The objective is not to finish the entire Living Atlas.

The objective is to establish a working kernel whose architecture can evolve.

  

22. Final Deliverable

When finished, report:

Created

List every new file/folder.

Modified

List every existing file modified and summarize the change.

Preserved

Identify important existing structures that were intentionally left untouched.

Architecture

Briefly explain how the implementation maps:

Entities

Relationships

Experiences

Capture

Ledger

Retrieval

Intelligence

Knowledge

Action

Feedback

Demonstration

Show the path of the demonstration:

Experience

→ Ledger

→ Knowledge

→ Action

→ Feedback

Questions

Identify architectural decisions that should remain unresolved rather than being guessed.

Do not claim the Living Atlas is complete.

The goal is a robust first kernel that can evolve through use.