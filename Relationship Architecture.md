# Relationship Architecture

**Status:** Open — pairs conceptually with the existing Relational Learning Experiment, but the Architecture note itself has no direct Experiment of its own (see note in §5). Drafted for review.
**Position in LIA:** Layer-subsystem note — defines what constitutes a "relationship" at each layer and how relationships differ structurally from mere information exchange.

---

## 1. Problem this component solves

Shared Context Protocol defines the envelope information travels in. Agency Architecture defines who may act. Neither defines what makes a *sustained* connection between two nodes (human-human, human-AI, AI-AI, or institution-institution) a **relationship** rather than a series of unconnected transactions. This matters because Identity & Continuity, Memory Architecture, and the Dyad layer itself are only meaningful if something persists between exchanges — Relationship Architecture is the note that specifies what that "something" is.

## 2. Core definition

A relationship, in this framework, is **an accumulating, mutually-referenced context that changes how future exchanges are interpreted** — distinct from a transaction, which is a single exchange interpreted on its own terms. The test for whether a relationship exists between two nodes: does exchange N+1 get interpreted differently *because of* exchange N, and is that difference legible to both nodes (not just inferred by one)? This ties directly to Memory Architecture (the accumulation mechanism) and Identity & Continuity (what persists across exchanges as "the same" relationship rather than a new one each time).

## 3. Relationship structure per layer

| Layer | Relationship unit | What accumulates |
|---|---|---|
| Individual | Self-relationship (continuity with one's own past states) | Personal history, self-model |
| Dyad | The core relational unit — two nodes, explicit mutual reference | Shared context, negotiated agency (see Agency Architecture) |
| Crew | Many-to-many relationships bounded by shared membership | Group norms, delegated trust |
| Network | Institutional relationships — role-to-role, not person-to-person | Precedent, formal agreement |
| Ecosystem | Emergent, often unnamed relationships (mutual dependency without direct exchange) | Aggregate pattern, not individually legible |

## 4. Relationship to AI-human pairing specifically

The Dyad layer is the natural home for a single AI-human working relationship — this is the layer at which "accumulating, mutually-referenced context" is most directly analogous to what a persistent memory system provides. Relationship Architecture's boundary condition here: the accumulation must be **legible to the human**, not just stored by the AI, or the relationship-test in §2 fails (the human can't confirm exchange N+1 was interpreted differently because of N). This has a direct bearing on the appropriate_boundaries concern already present elsewhere in the framework — an AI holding memory the human can't see or verify isn't building a Dyad relationship by this definition, it's building an asymmetric transaction history.

## 5. Open questions

- The directory pairs "Relational Learning" with an Experiment, but doesn't specify whether that Experiment tests this Architecture note directly, or a narrower slice of it (learning specifically, vs. the broader relationship-definition question). Worth confirming which — this draft assumes the broader note still needs its own dedicated Experiment.
- Does the Dyad-layer definition of relationship generalize to Crew, or does "many-to-many, bounded by membership" require a genuinely different test than "does exchange N+1 get interpreted differently because of N" — which presupposes two identifiable parties?
- How does a relationship *end* — is dissolution a Lineage-layer event (Decision Log / Abandoned Ideas) or does Relationship Architecture need its own termination clause, symmetrical with Exit & Repair?

---
*Derived from: Dyad-layer definition already established in LIA; cross-reference against Memory Architecture, Identity & Continuity, and Agency Architecture.*
