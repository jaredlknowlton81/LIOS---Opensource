# LIOS — Living Intelligence Operating System

LIOS is a small, dependency-light Python library for modeling how individuals,
groups, communities, and institutions develop direction, trust, and shared
understanding over time — with AI in a strictly **reflective**, non-authoritative
role.

It is the code substrate for the *Living Intelligence Model*: a framework built
around a Four-Layer System (Personal → Small-Group → Community → Societal), a
Meeting model (contact, resolution, trust), a Knowledge Garden pipeline
(Listening Post → Observatory → Knowledge Garden → Scenario Engine → Blink of
Insight), and a hard rule that AI expands perception without ever being granted
decision authority.

LIOS exists to close the **Testing Gap**: frameworks that are fully designed
but have no real field data behind them. It gives you a minimal, honest data
model to log real Events, Claims, and Relationships as they happen, instead of
only reasoning about them in the abstract.

## Core ideas

- **Entities** are people, crews, communities, or institutions — nodes at any
  scale of the Four-Layer System.
- **Contexts** situate everything: which Layer you're operating at, and which
  epistemic mode you're in (Reality / Possibility / Decision).
- **Events** are things that happened — a signal, a contact, a resolution, a
  trust shift, a Disclosure Spiral stage transition.
- **Claims** are assertions produced by a Knowledge Garden pass. Every claim
  carries provenance and a confidence level. None are ground truth.
- **Relationships** track trust and coordination between two entities — Weekly
  Dyadic Practice, Exit-First Coordination, mentorship, crew membership.
- **Goals** are directional intent, scoped to a time horizon (daily through
  annual, matching the Garden System rhythms).
- **Providers** are AI backends. The provider interface makes it structurally
  impossible for a provider to return a directive — it can only return Claims,
  each with confidence and provenance attached. This is "AI as Compass, Not
  Controller" enforced in code, not just in prose.
- **Navigation** runs the Listening Post → Observatory → Knowledge Garden →
  Scenario Engine → Blink of Insight pipeline as an explicit, inspectable
  sequence of Context transitions.
- **Integration** is where cross-framework reconciliation happens: Four-Layer
  System ↔ Post Nation ↔ Microsolidarity, and where a Context's epistemic mode
  (Reality/Possibility/Decision) is resolved against its scale-layer, rather
  than left as an open question.
- **Provenance** enforces the verification principle: every Claim must be able
  to answer "where did this come from and how confident should I be."

## Install

```bash
pip install -e .
```

## Quickstart

```python
from lios.models.entity import Entity, EntityType
from lios.models.context import Context, Layer, EpistemicMode
from lios.models.event import Event, EventType
from lios.navigation import Navigator

greg = Entity(name="Greg", type=EntityType.PERSON)
ctx = Context(layer=Layer.PERSONAL, epistemic_mode=EpistemicMode.REALITY)

nav = Navigator()
nav.log(Event(type=EventType.SIGNAL, context_id=ctx.id, entities=[greg.id],
               description="Noticed I keep re-deriving the same open question."))
nav.advance(ctx)  # Listening Post -> Observatory
print(ctx.lifecycle_stage)
```

## Repository layout

```
lios/
├── docs/                 architecture, ontology, and context-lifecycle notes
├── src/lios/
│   ├── models/           Entity, Event, Claim, Relationship, Goal, Context
│   ├── providers/        AI provider interface (reflective-only)
│   ├── integration.py    cross-framework reconciliation
│   ├── navigation.py     Listening Post -> ... -> Blink of Insight pipeline
│   ├── provenance.py     verification principle
│   └── storage.py        backend-agnostic persistence
└── tests/
```

## Status

Early scaffold. The ontology is stable; storage backends and provider
implementations beyond the in-memory reference are not yet built out. This is
intentional — the point is to get real field data flowing before over-building.

## License

See `LICENSE`.
