# Ontology

Six primitives. Everything else in the Living Intelligence Model is expressed
in terms of these.

## Entity

Any actor: a person, a group/crew, a community, or an institution. Typed
loosely via `EntityType`; actually positioned by which `Context` it appears in.

**Maps to:** a node at any scale of the Four-Layer System; a Post Nation
resident or village; a Microsolidarity crew member or crew.

## Context

A situating frame: `Layer` (Personal/Small-Group/Community/Societal) crossed
with `EpistemicMode` (Reality/Possibility/Decision), plus a `lifecycle_stage`
tracking position in the Listening Post -> Blink of Insight pipeline. Contexts
can nest (`parent_context`) but Layer and EpistemicMode are always independent
axes on the same Context — see `architecture.md` for why.

**Maps to:** which scale-layer and which epistemic mode a given piece of work
is happening in; the current stage of a Knowledge Garden pass.

## Event

Something that happened, timestamped and attributed to one or more Entities
within a Context.

**Maps to:** a Signal, Contact, or Resolution in the Meeting model; a Trust
Shift in a Relationship; a Disclosure Spiral stage transition; a nightly
two-question reflection (the Omi experiment's unit of data).

## Claim

A provisional assertion about an Entity, always carrying a `confidence` and a
`provenance_id`, never presented as settled. Claims are append-only —
superseded, never edited.

**Maps to:** output of a Knowledge Garden pass; a pattern noticed via the AI
Possibility Mirror; anything a Provider reflects back.

## Relationship

A trust/coordination link between two Entities, with a `trust_level` that
Events update over time.

**Maps to:** Weekly Dyadic Practice pairing; Exit-First Coordination link;
Microsolidarity crew membership; general mentorship.

## Goal

Directional intent held by one Entity, scoped to a `Horizon` (daily through
annual) and optionally linked to the Claims that motivated it.

**Maps to:** the "Actionable Steps" end of the AI-as-mirror pipeline; 80,000
Hours-style direction-setting in the Garden System.

## Deliberately not modeled (yet)

- **Framework identity** (Four-Layer System vs. Living Intelligence Model vs.
  Post Nation as named things) — these are organizing narratives, not data.
  LIOS models the *substance* underneath them so it doesn't have to take a
  position on how the frameworks themselves relate. `integration.py` is where
  that reconciliation happens when it's needed.
- **Compass & Map** — the Map half of the Compass Principle hasn't resurfaced
  in the framework work yet, so there's no model for it. Adding one before
  it's needed would guess at a shape that isn't settled.
