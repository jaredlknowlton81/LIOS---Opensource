# Bidirectional Feedback Loops

**Status:** Open — named and grounded in Adapt & Iterate, previously undesigned. Drafted here for review.
**Position in LIA:** Fourth and final cross-layer integration component (after Permission-Aware Routing, Shared Context Protocol, Layer Adapters).
**Depends on:** Layer Adapters (a loop cannot propagate what it cannot translate).

---

## 1. Problem this component solves

The first three components make a *single* crossing legible: permission (may this move), envelope (in what form), translation (reshaped how). None of them account for what happens when a layer *changes as a result* of what it received, and that change needs to propagate back. Without this component, the architecture supports one-way information flow but not learning — a Network-layer policy shift never reaches back down to alter Individual-layer behavior, and an Individual-layer pattern never accumulates into Crew-level insight. Feedback Loops are what make the five-layer stack adaptive rather than merely hierarchical.

## 2. Core mechanism — splitting internal change from behavioral change

Per the open design question already on record: this draft treats "internal change" (learning — an update to what a layer *knows*) and "behavioral change" (adaptation — an update to what a layer *does*) as two distinct, sequential steps rather than one bundled event. Reasoning: a layer can learn something (via a received, adapted ContextPacket) without yet acting on it — there may be a deliberate delay for validation, consent, or simply because the learning hasn't crossed a threshold that warrants a behavior change. Bundling them would force every received signal into an immediate action, which conflicts with the Exit & Repair and Adapt & Iterate cross-cutting foundations (both of which assume revisability, not reflexive response).

**Step 1 — Registration (learning):** A translated ContextPacket arriving via a Layer Adapter is logged as a candidate update to the receiving layer's model of itself/its environment. This is a Ledger Architecture event, not yet a behavior change.

**Step 2 — Activation threshold:** A registered update becomes a behavior change only when it crosses a threshold — defined per layer, not globally. Candidate thresholds: repetition (the same signal arrives N times), corroboration (multiple independent origin-scopes converge on the same signal), or explicit confirmation (a human or governing process at the receiving layer approves the change).

**Step 3 — Propagation (adaptation):** Once activated, the behavior change is itself packaged as a new ContextPacket and routed back through Permission-Aware Routing / Shared Context Protocol / Layer Adapters toward whichever layer(s) are affected — including, potentially, back toward the origin layer (true bidirectionality, not just upward reporting).

## 3. Loop topology

Not every layer pair needs a loop in both directions at the same cadence. Proposed default cadences, consistent with the Living Blueprint Implementation Roadmap's phase sequencing:

| Loop | Direction | Typical cadence | Rationale |
|---|---|---|---|
| Individual ↔ Dyad | fast, near-continuous | Matches "Build Trust" phase — tight feedback is how trust forms |
| Dyad ↔ Crew | medium | Matches "Build Shared Memory" |
| Crew ↔ Network | slower, batched | Matches "Enable Coordination" / "Distribute Governance" |
| Network ↔ Ecosystem | slowest, deliberate | Matches "Federate & Scale" / "Evolve a Regenerative Ecosystem" |

This gives the roadmap's six phases a mechanical interpretation: each phase is, in part, the point at which a given loop's cadence tightens enough to function.

## 4. Relationship to other cross-cutting foundations

- **AI as Memory & Support ("librarian not manager"):** the AI's role in a loop is Step 1 (registration/surfacing candidate patterns), not Step 2 (it does not unilaterally cross the activation threshold on behalf of a human layer).
- **Transparent Funding / Measurement That Matters:** natural candidates for what gets *measured* to determine whether a threshold in Step 2 has been crossed.
- **Exit & Repair:** a loop must be interruptible — any layer can decline propagation of a Step 3 change directed at it, which routes back through Permission-Aware Routing's consent-status question rather than forcing the update.

## 5. Open questions carried forward

- What happens when Step 2 thresholds conflict — e.g., Crew layer activates a change that Network layer's own threshold logic would reject? Does Boundary Architecture arbitrate?
- Should Step 1 registrations that never cross threshold be retained indefinitely (full Evidence Ledger) or expire — and if they expire, does that constitute the layer "forgetting" a true but under-corroborated signal?
- Is the four-cadence table (§3) a claim about how loops *should* run, or a description extracted from the existing tech-example mapping? Currently unconfirmed either way — flag for Evidence Architecture.

---
*Derived from: Living Intelligence — Master Architecture; Adaptation Architecture; Learning Architecture; Living Blueprint Implementation Roadmap. No experiment yet exists for this component (see 04_Experiments gap).*
