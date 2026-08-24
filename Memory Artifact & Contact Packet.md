# Memory Artifact & Contact Packet

**Status:** Open — no Experiment pairing yet exists (04_Experiments gap). Drafted for review.
**Position in LIA:** Layer-subsystem note — specifies the durable, exportable form that accumulated memory takes when it needs to exist independently of any single layer's live state.

---

## 1. Problem this component solves

Shared Context Protocol's `ContextPacket` is built for routing — it carries a specific unit of context across a specific Layer Adapter crossing, gated by Permission-Aware Routing, and (per Bidirectional Feedback Loops) may carry a decay flag. None of that is well-suited to memory meant to *outlast* any single routing event — a durable record a node can hold, hand off, or present independent of an active loop. This note specifies that separate artifact type and its narrower cousin, the Contact Packet.

## 2. Core definition — two related but distinct objects

**Memory Artifact:** a durable, self-contained export of a node's accumulated state (or a bounded slice of it), built to persist and be reviewed outside any live routing context. Where a `ContextPacket` is built for a single crossing, a Memory Artifact is built to be re-opened later, by the same or a different party, without needing the original loop still active.

**Contact Packet:** a narrower, minimal Memory Artifact — specifically the subset needed for two nodes to *re-establish* a relationship (Relationship Architecture §2) after a gap, rather than the full accumulated state. A Contact Packet answers "who are you and what do we already share," not "everything we've learned."

## 3. Relationship to Identity & Continuity

A Memory Artifact is only useful if it satisfies Identity & Continuity §2's ledger-property criterion when re-opened — i.e., re-importing a Memory Artifact should let the receiving party trace the update chain it represents, not just read a snapshot. This is the direct mechanical requirement that makes Memory Artifacts distinct from an arbitrary data export: an export without traceable lineage is not a Memory Artifact in this framework's sense, just a dump.

## 4. Where Compression & Lineage fits (forward reference)

Building a Memory Artifact from a full, live Ledger necessarily involves compression — deciding what to keep at full fidelity, what to summarize, and what to drop. That is squarely Compression & Lineage's subject matter (next note); this note treats the Memory Artifact as the *output* of that process and Compression & Lineage as the process itself. The two should be read together; drafting order here is Artifact-first only because it's the more concrete, directory-adjacent concept.

## 5. Practical role — this is likely the mechanism behind the vault synthesis note

Worth naming directly: the "dedicated Synthesis note... intended to preserve cross-concept lineage" already on record for the broader Living Intelligence vault is, functionally, a Memory Artifact at the vault/project scale rather than the individual-node scale this note has been describing. If that reading holds, Memory Artifact & Contact Packet isn't just an abstract architecture concept — it's the same mechanism the vault itself is already using for its own synthesis note, one level up. Worth confirming this correspondence rather than assuming it.

## 6. Open questions

- Does a Contact Packet need its own permission gate distinct from Permission-Aware Routing's six questions, given it's explicitly meant to survive outside an active routing context — or does it just carry the original grant's terms forward unchanged?
- What invalidates a Memory Artifact — does it expire (a decay-flag analog, per Adaptation Architecture §4), or does it remain valid until explicitly superseded by a newer Artifact from the same lineage?
- No Experiment yet designed — candidate: the Memory Experiment (already scoped, per the directory) may be the right home for testing this note directly rather than Ledger Architecture generally — worth checking scope once that Experiment file is drafted.

---
*Derived from: Shared Context Protocol's ContextPacket (contrast case); Identity & Continuity §2; forward reference to Compression & Lineage; cross-reference against the vault-level Synthesis note already on record.*
