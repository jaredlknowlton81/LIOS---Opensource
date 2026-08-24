# Context Architecture

**Status:** Open — no Experiment pairing yet exists (04_Experiments gap). Drafted for review.
**Position in LIA:** Layer-subsystem note — defines what "context" is and how it is scoped, as distinct from Shared Context Protocol, which defines the *envelope format* a unit of context travels in once scoped.

---

## 1. Problem this component solves

Shared Context Protocol answers "what envelope does context travel in." It presupposes an answer to a prior question that this note supplies: what *counts* as context in the first place, at what grain, and bounded by what. Without a Context Architecture, "context" risks becoming an undifferentiated catch-all — everything a layer knows — which would make Permission-Aware Routing's origin-scope and granularity questions impossible to answer precisely, since you can't specify the scope or granularity of something undefined.

## 2. Core definition

Context, in this framework, is **the subset of a layer's accumulated state that is relevant to interpreting a specific exchange, bounded by situation rather than by time**. This distinguishes it from Memory (which is the full accumulated state, unbounded by any particular exchange) and from Relationship (which is the subset that persists *because* it's mutually referenced across exchanges, per Relationship Architecture). Context is the narrower, situational cut through both.

## 3. Three axes of context scoping

1. **Temporal scope** — how far back does relevant context extend for this exchange (the last message vs. the full relationship history vs. a specific bounded episode)?
2. **Relational scope** — whose context is it: the Individual's, the Dyad's shared context, or context borrowed from a higher layer (e.g., a Crew norm informing a Dyad exchange)?
3. **Situational scope** — is the boundary drawn by topic, by task, by role, or by explicit request? This axis is what a Layer Adapter's "fit check" (§4 of Layer Adapters) actually evaluates when it asks whether a translated packet "still makes sense" at the receiving layer — fit-check failure is, more precisely, a situational-scope mismatch.

## 4. Relationship to Situated Intelligence

This note and Situated Intelligence are closely coupled and worth explicitly distinguishing to avoid overlap: Context Architecture defines the *boundary* of relevant state; Situated Intelligence (separate note) presumably addresses how intelligence *uses* situational grounding to act — i.e., Context Architecture is about scoping the input, Situated Intelligence is about what the system does with a well-scoped input. Flagging this pairing for Convergence Map / Contradiction Map review, since the two notes could easily drift into redundant territory without a clear division of labor.

## 5. Open questions

- Is the three-axis scoping model (§3) exhaustive, or is there a fourth axis — e.g., *epistemic scope* (what's confirmed vs. assumed within the context window) — that overlaps with the Confirmed/Derived/Open/Unconfirmed status framework already applied elsewhere?
- When Layer Adapters perform "granularity resolution," is that operating on Context Architecture's temporal axis, situational axis, or both? Currently unspecified — worth resolving so the two notes reference the same underlying model rather than each implying a slightly different one.
- No Experiment yet designed — candidate: test whether the three-axis model predicts actual fit-check failures better than an undifferentiated notion of context would.

---
*Derived from: Shared Context Protocol's ContextPacket envelope; Layer Adapters' fit-check mechanism; cross-reference against Situated Intelligence and Memory Architecture.*
