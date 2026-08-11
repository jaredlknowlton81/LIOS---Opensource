# Architecture

## Design goal

LIOS has one job: let real field data accumulate against the Living
Intelligence Model without forcing a commitment to any single framework's
final shape. The ontology (`models/`) is intentionally minimal — six
primitives, no framework-specific classes — so that Post Nation, Microsolidarity,
the Meeting, and the Disclosure Spiral can all be expressed *in terms of* the
same six things instead of each getting their own schema.

## Layers of the codebase

```
models/        pure data — no behavior beyond small invariants
providers/     AI boundary — enforces reflective-only AI
navigation.py  pipeline logic over Context lifecycle
integration.py cross-framework reconciliation
provenance.py  verification principle
storage.py     persistence, swappable backend
```

Dependencies flow one direction: `storage` and `provenance` depend on nothing
but `models`; `navigation` and `integration` depend on `models` only;
`providers` depends on `models.claim` and `models.context` only. Nothing in
`models/` imports from outside `models/`. This keeps the ontology reusable
even if navigation, integration, or storage get rewritten.

## Why Entity is scale-agnostic

A person, a crew, a village, and an institution are all "nodes that
participate in Events and hold Relationships." Giving each its own class would
force the Four-Layer System's boundaries into the type system permanently.
Instead, `EntityType` is a soft tag and `Layer` (on `Context`) is what actually
positions an Entity at a given moment — the same Entity can show up in a
PERSONAL context (as themselves) and a COMMUNITY context (as a resident) with
no schema change.

## Why EpistemicMode is not nested inside Layer

This was an explicit open question: does the Reality/Possibility/Decision
stack sit *inside* each Four-Layer scale-layer, or run as a separate axis
across all of them? LIOS commits to the second: `Context` carries both `layer`
and `epistemic_mode` as independent fields. A COMMUNITY-layer Context can be in
REALITY, POSSIBILITY, or DECISION mode; so can a PERSONAL-layer one. This
means a single Scenario Engine pass can walk a Context through Possibility
mode without changing which Layer it belongs to — matching how the Knowledge
Garden pipeline is meant to work (see `context-lifecycle.md`).

If field data ends up showing this is wrong — e.g. Decision-mode only ever
makes sense at Societal scale — `integration.py` is the place that would need
to change, since it's the only module that reasons about Layer and
EpistemicMode together.

## Why Provider can only return a Reflection

`providers/base.py` has no method, and `Reflection` has no field, capable of
carrying a directive. This is a structural (not policy) enforcement of "AI as
Compass, Not Controller": a new Provider implementation cannot accidentally
become an authority, because the return type doesn't allow it. Decisions are
made by a human Entity creating a `Goal` — a separate model that a Provider
never touches directly.

## Why Claims are append-only

`Claim.supersede()` never mutates `content` — it flips `status` and points
`superseded_by` at a new Claim. This preserves a full history of what was
believed and when, which is exactly the kind of longitudinal signal the
Testing Gap needs: you can later ask "how did our Claims about X evolve over
six months," not just "what do we currently believe about X."

## Extensibility points

- New `Provider` subclasses for real AI backends (each still bound to
  `Reflection`-only output).
- New `Store` implementations (sqlite, postgres) behind the same protocol.
- New entries in `integration.FRAMEWORK_LAYER_MAP` as more adjacent frameworks
  (beyond Post Nation and Microsolidarity) get pulled in.
