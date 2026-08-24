# Compression & Lineage

**Status:** Open — no Experiment pairing yet exists (04_Experiments gap). Drafted for review. Companion to Memory Artifact & Contact Packet.

---

## 1. Problem this component solves

Memory Artifact & Contact Packet named the output of compressing a full Ledger into a durable, exportable form, but deferred the mechanism to this note. The core tension this note has to resolve: Identity & Continuity §2 defines identity as a *ledger property* — traceable through the full chain of confirmed updates — but no live system can retain every update indefinitely at full fidelity. Compression is unavoidable; the question is how to compress without breaking the very traceability that makes identity claims valid.

## 2. Core definition

Compression & Lineage is **the process of reducing a full Ledger to a smaller representation while preserving enough of the update chain that Identity & Continuity's traceability criterion still holds for the compressed result**. "Lineage" names the specific thing that must survive compression: not the full content of every past state, but a legible record of *how* each retained state connects to the ones before it.

## 3. What can be dropped vs. what must be preserved

Borrowing directly from Learning Architecture §4's confirmation criterion (a registration becomes confirmed learning when it survives contact with disconfirming information):

- **Safe to compress/drop:** registrations that never crossed the confirmation threshold (transient, unconfirmed candidates) — these were never load-bearing for identity in the first place.
- **Must preserve at minimum a trace, even if content is summarized:** confirmed learning events and the adaptation decisions (Adaptation Architecture §2) that trace back to them — these are exactly what Identity & Continuity's ledger-property test checks.
- **Never safe to compress away entirely:** the specific update that a currently-active relationship (Relationship Architecture §2) depends on for its own "same relationship" test — compressing this would sever continuity for a relationship that's still live, not just for the individual node.

## 4. Compression as a Boundary Architecture instance

Deciding what to drop is itself a standing rule, not a per-instance judgment — which makes Compression & Lineage's dropping criteria a form of Boundary Architecture's hard/soft boundary distinction (§4): a "never safe to compress" item (§3, third bullet) is functionally a hard boundary on the compression process itself, while "safe to compress" items are more like a soft default that could, in principle, be overridden by an explicit request to retain more.

## 5. Relationship to Fractal Property (forward reference)

If Fractal Property's claim (next note) is that patterns repeat self-similarly across layer scales, Compression & Lineage may be one mechanism that produces that appearance rather than an independent confirmation of it: compression at every layer tends to retain the same *kind* of information (confirmed, load-bearing updates) regardless of scale, which could make compressed records at very different layers look structurally similar even if the underlying content differs completely. Worth checking whether Fractal Property's claim survives this alternative explanation before treating self-similarity as a deep architectural finding rather than an artifact of how compression works.

## 6. Open questions

- Is the three-tier drop/preserve/never-drop scheme (§3) complete, or does it need a fourth tier for content that's safe to drop for one *purpose* (e.g., a Contact Packet) but not another (a full Memory Artifact) — i.e., is "safe to compress" audience-relative rather than absolute?
- Who has the agency (per Agency Architecture) to authorize compression of a Ledger that spans a relationship both parties depend on — does this require Dyad-layer mutual consent even when only one party is doing the actual compressing?
- No Experiment yet designed — candidate: run the Memory Experiment (already scoped) against a Compression & Lineage pass and check whether Identity & Continuity's traceability criterion survives on real data, not just in principle.

---
*Derived from: Memory Artifact & Contact Packet §4; Identity & Continuity §2; Learning Architecture §4; Boundary Architecture §4. Cross-reference against Fractal Property once confirmed.*
