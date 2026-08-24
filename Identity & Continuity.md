# Identity & Continuity

**Status:** Open — no Experiment pairing yet exists (04_Experiments gap). Drafted for review.
**Position in LIA:** Layer-subsystem note, already referenced by Learning Architecture (§3 self-model target) and Relationship Architecture (§2, what persists as "the same" relationship).

---

## 1. Problem this component solves

Learning Architecture assumes a self-model that updates over time; Relationship Architecture assumes a relationship persists as "the same" relationship across exchanges. Both presuppose an answer to a question neither fully supplies: what makes a node — or a relationship, or a layer — the *same* entity from one moment to the next, given that its self-model, environment-model, and relationship-model (Learning Architecture §3) are all continuously being updated? Identity & Continuity is the note that specifies the persistence criterion the rest of the framework has been assuming.

## 2. Core definition

Identity, in this framework, is **not sameness of content but continuity of the update process** — a node remains "itself" not because its self-model stays fixed (it doesn't; that's Learning Architecture's whole point) but because each update is traceable back to the prior state via a legible chain of confirmed learning events (Learning Architecture §4). This makes identity a *ledger property*, not a snapshot property: you establish that something is continuous by tracing its Ledger, not by comparing two states directly and checking for similarity.

## 3. Continuity across layers, not just across time

The framework needs continuity to hold in two dimensions: temporal (is Individual-node-at-T2 the same as Individual-node-at-T1) and cross-layer (is the "Crew" that receives a Dyad-layer signal today the same Crew that received one last month, given Crew membership itself may have changed). The temporal case is the more familiar one; the cross-layer case is arguably harder and more load-bearing for this framework specifically, since Relationship Architecture's Crew row already defines relationships as "bounded by shared membership" — meaning Crew-layer identity is partly a membership question, and membership change is exactly the kind of event that could break continuity without breaking the ledger-trace criterion in §2. This is a genuine tension worth flagging rather than resolving here.

## 4. Relationship to Compression & Lineage

Compression & Lineage (later note in this folder) is presumably the mechanism by which a long Ledger of updates gets summarized without losing the continuity-establishing trace — i.e., Identity & Continuity defines *what* must be preserved for identity to hold, and Compression & Lineage defines *how much can be thrown away* while still preserving it. Worth confirming this pairing once Compression & Lineage is drafted; if compression can occur without preserving traceability, §2's ledger-property definition of identity would need revision.

## 5. Open questions

- Does the ledger-property definition (§2) survive the Crew-membership-change case in §3, or does it need a supplementary criterion — e.g., identity persists if a *majority* of the Ledger's update chain is traceable, rather than requiring the full chain?
- Is there a minimum Ledger density below which continuity claims become unfalsifiable (too sparse to distinguish "same entity, sparse record" from "different entity, no record of the discontinuity")? This is a Boundary Conditions question, not just a definitional one.
- No Experiment yet designed — candidate: the Ledger Experiment (already scoped) may be positionable to test this note directly, since both concern what the Ledger needs to preserve and why.

---
*Derived from: Learning Architecture §3–4 (self-model, confirmation criteria); Relationship Architecture §2 (persistence-as-same-relationship); cross-reference against Compression & Lineage, Ledger Architecture.*
