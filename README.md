LIOS

Living Intelligence Operating System

LIOS is an open-source exploration of a Living Intelligence Operating System: an architecture for connecting experience, context, intelligence, knowledge, goals, action, and feedback across individual, community, and planetary scales.

The central idea is simple:

Experience becomes context. Context enables intelligence. Intelligence informs action. Action produces feedback. Feedback creates new experience.

LIOS is increasingly understood not as a single loop or a fixed collection of primitives, but as a multi-module architecture in which different concerns have explicit boundaries.

⸻

The Core Loop

LIOS operates through a continuous cycle:

Experience
    ↓
Capture
    ↓
Context / Ledger
    ↓
Intelligence / Sensemaking
    ↓
Knowledge
    ↓
Goals
    ↓
Action
    ↓
Feedback
    ↓
Experience

The loop describes how intelligence develops over time.

The modules describe where the different responsibilities live.

These are complementary views of the same system.

⸻

The Emerging Architecture

The repository is moving toward the following architectural separation:

LIOS

This structure is an emerging architectural model, not a claim that every boundary has been finalized.

⸻

01 — Architecture

01-architecture/ defines the ontology and conceptual substrate of LIOS.

It asks:

What exists, what happens, what is remembered, and how do those things relate?

This layer includes concepts such as:

* Entities
* Relationships
* Experience
* Events
* Ledger
* Claims
* Knowledge
* Goals
* Contribution
* Learning
* Adaptation
* Feedback

The Ledger is particularly important.

It is not merely a database or storage mechanism. It represents persistent relational context across time:

People
Events
Relationships
Decisions
Actions
Projects
Knowledge
Outcomes
Time
        ↓
     Ledger
        ↓
Persistent Context

The Ledger allows the system to remember not only what is known, but what happened, who was involved, what was decided, what resulted, and what was learned.

⸻

02 — Runtime

02-runtime/ is the execution layer of LIOS.

This is where Hermes belongs.

If the architecture defines what LIOS is, the runtime determines how those concepts become executable processes.

Hermes connects things such as:

* events
* context
* agents
* AI
* tools
* workflows
* schedules
* actions
* verification
* feedback

A simplified runtime cycle is:

Notice
  ↓
Understand
  ↓
Activate
  ↓
Execute
  ↓
Verify
  ↓
Record
  ↓
Continue

The architectural distinction is:

Architecture defines the model. Runtime executes the model.

⸻

03 — Interfaces

03-interfaces/ is the device and interaction layer.

This is where systems such as Fieldy and Omi fit.

Interfaces connect LIOS to lived experience and the physical or digital environment.

They can provide:

* experience capture
* sensory input
* observation
* interaction
* context acquisition
* human-computer interaction
* device-level feedback

The architectural boundary is important:

Fieldy and Omi are interfaces to LIOS, not LIOS itself.

They provide access to experience.

The architecture determines how that experience is represented, contextualized, interpreted, remembered, and acted upon.

⸻

04 — Applications

04-applications/ contains the applications of LIOS at different scales.

The emerging model is:

04-applications/
├── individual/
├── community/
└── planetary/

These are not necessarily separate systems.

They represent different scales at which the underlying architecture can operate.

Individual

Personal context, goals, projects, learning, decision-making, and action.

Community

Shared context, relationships, collective learning, contribution, coordination, and action.

Planetary

Networks of entities and relationships, distributed knowledge, persistent context, learning, adaptation, and emergent intelligence.

The hypothesis is:

Individual → Community → Planetary

is a scaling property of the architecture rather than three unrelated products.

⸻

05 — Development

05-development/ contains the material required to build and evolve LIOS.

In particular:

05-development/
└── architecture-decisions/

Architecture decisions record confirmed calls about the system.

This creates an important separation:

Concern	Purpose
Architecture	Defines the model
Research	Explores possibilities
Architecture Decisions	Records confirmed decisions
Runtime	Executes the model
Applications	Apply the model

This prevents important architectural reasoning from disappearing into implementation history.

⸻

Research

research/ is where uncertainty remains explicit.

The emerging structure includes:

research/
└── unresolved-questions/

An unresolved question should not have to become an architectural commitment prematurely.

Current questions include:

* Where exactly do Entity, Event, and Claim belong?
* Are they primitives, ontology concepts, or representations derived from deeper relationships?
* Where does Contribution belong?
* Is Contribution fundamental or emergent?
* What is the precise boundary between the Ledger and Knowledge?
* What belongs to Architecture versus Runtime?
* How does intelligence emerge from persistent relational context?
* Which properties remain invariant as LIOS scales from individual to planetary systems?

Research should feed architecture.

Architecture decisions should preserve the conclusions reached.

⸻

Entity, Event, Claim, and Contribution

Several concepts remain intentionally unresolved.

Entity

What participates in the system?

Event

What happens?

Claim

What is asserted, believed, inferred, or recorded as potentially true?

Contribution

What does an entity contribute to the system, relationship, community, or larger process?

These concepts were previously being considered as part of a small set of fundamental primitives.

The current architecture does not yet force that conclusion.

They remain candidates for further ontology work.

This is deliberate.

Unresolved ontology should remain unresolved until the architecture provides sufficient evidence to settle it.

⸻

Experience, Context, Intelligence, Action

One way to understand LIOS is through four broad transformations:

Experience
    ↓
Context
    ↓
Intelligence
    ↓
Action
    ↓
Experience

Experience

Something happens in the world.

Context

The system preserves relationships, history, and relevant knowledge.

Intelligence

The system interprets, reasons, compares, imagines, learns, and supports decisions.

Action

People, agents, and tools act in the world.

Feedback

The result becomes new experience and updates the system’s understanding.

This is what makes LIOS a living system rather than merely an information system.

⸻

Human Agency

LIOS is intended to increase human capability rather than eliminate human judgment.

People remain responsible for:

* purpose
* values
* judgment
* responsibility
* meaning
* important decisions

AI is treated as a capability within the architecture, rather than as the owner of the architecture.

The goal is not:

AI decides for people.

The goal is:

People and intelligent systems become more capable of understanding, deciding, acting, learning, and adapting.

⸻

From Personal Intelligence to Planetary Intelligence

The same architectural principles can potentially operate across increasing scales:

Individual
    ↓
Relationship
    ↓
Community
    ↓
Organization
    ↓
Network
    ↓
Planetary

At each level, entities interact, experience events, accumulate context, make decisions, act, and learn.

The resulting hypothesis is a Planetary Intelligence Mesh:

Entities
    ↓
Relationships
    ↓
Experience
    ↓
Persistent Context
    ↓
Learning
    ↓
Adaptation
    ↓
Emergence
    ↓
Network Intelligence
    ↓
Planetary Intelligence

The intelligence does not necessarily have to reside in one central system.

It may emerge from the relationships between many autonomous participants sharing persistent context and feedback.

⸻

Repository Philosophy

This repository is itself an evolving intelligence system.

The project began with a deliberately flatter exploratory structure because the concepts were still being discovered.

That exploration produced a large body of interconnected work.

As the concepts mature, some distinctions have become clearer:

Exploration
    ↓
Sensemaking
    ↓
Architectural distinction
    ↓
Decision
    ↓
Implementation
    ↓
Use
    ↓
Feedback
    ↓
Revision

The repository therefore continues to evolve alongside the architecture.

The goal is not to impose a perfect taxonomy prematurely.

The goal is to make real architectural boundaries visible when the evidence supports them.

⸻

Current Status

Status: Architectural transition / evolving

The repository is moving from a predominantly flat exploratory corpus toward an explicit multi-module architecture.

The central architectural question is now:

Is LIOS best understood as a multi-module Living Intelligence architecture rather than as a single loop or a fixed set of primitives?

The current evidence points toward yes, but the proposition remains open to revision.

The next architectural work focuses particularly on:

1. Establishing the ontology boundary.
2. Resolving Entity, Event, and Claim.
3. Determining the architectural role of Contribution.
4. Clarifying the Ledger/Knowledge boundary.
5. Confirming Hermes as the runtime boundary.
6. Clarifying Fieldy/Omi as interface boundaries.
7. Defining how Individual → Community → Planetary applications share the same underlying architecture.

⸻

The Working Proposition

LIOS is a multi-module architecture for living intelligence in which ontology and persistent relational context support runtime execution, human/device interaction, and applications operating across individual, community, and planetary scales.

This proposition is intentionally provisional.

The architecture should continue to change when new evidence requires it.

The repository is not documenting a finished system. It is being used to discover and build one.