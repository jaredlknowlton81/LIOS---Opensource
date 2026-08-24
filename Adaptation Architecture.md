# Adaptation Architecture

**Status:** Open — no Experiment pairing yet exists (04_Experiments gap). Drafted for review.
**Position in LIA:** Layer-subsystem note — defines "behavioral change" as used in Bidirectional Feedback Loops §2 Steps 2–3 (Activation Threshold, Propagation); companion to Learning Architecture.

---

## 1. Problem this component solves

Learning Architecture governs how a layer's internal model changes. This note governs the separate question of when and how that changed model translates into changed behavior — the gap Bidirectional Feedback Loops left open by naming a "threshold" without specifying what crosses it or how. Without this note, "adaptation" risks being read as automatic once learning occurs, which the sequential-steps design in Bidirectional Feedback Loops explicitly rejects.

## 2. Core definition

Adaptation is **a change to a layer's behavior that is traceable to a specific confirmed learning event and to a specific threshold-crossing decision** — both conditions matter. Traceable-to-learning excludes reflexive or externally-imposed behavior changes (a Network-layer policy mandate isn't "adaptation" in this sense unless the Network layer's own model changed first — it's closer to Agency Architecture's representational-agency category, a constraint, not a learned response). Traceable-to-a-decision excludes drift — behavior that changes gradually without any identifiable point where a threshold was crossed, which this framework would treat as unaccounted-for and therefore a Missingness Analysis flag rather than legitimate adaptation.

## 3. Threshold types (elaborating Bidirectional Feedback Loops §2 Step 2)

Bidirectional Feedback Loops names three candidate thresholds — repetition, corroboration, explicit confirmation — without specifying how a layer chooses among them. This note proposes the choice is itself layer-dependent, following the same logic as Agency Architecture's per-layer agency table:

| Layer | Default threshold type | Why |
|---|---|---|
| Individual | Explicit confirmation | Full unilateral agency (per Agency Architecture) means the individual can just decide |
| Dyad | Corroboration | Requires both parties' models to converge — mutual, per Relationship Architecture |
| Crew | Repetition or corroboration | Depends on Crew's internal governance norm — not fixed by this architecture alone |
| Network | Explicit confirmation, formalized | Representational agency requires accountable, auditable decisions (ties to Institutional Intelligence) |
| Ecosystem | Repetition (aggregate/emergent) | No single confirming actor exists at this layer |

## 4. Propagation and the risk of runaway adaptation

Step 3 (Propagation) sends the behavior change back out as a new ContextPacket. This creates an obvious risk: an adaptation at layer A propagates to layer B, which adapts in turn and propagates back to A, compounding without limit. Adaptation Architecture's proposed safeguard: every propagated adaptation-packet carries a **decay flag** — a marker that, absent independent re-confirmation at the receiving layer, the adaptation's influence attenuates rather than compounding indefinitely. This is a direct mechanical reading of the Adapt & Iterate cross-cutting foundation, and gives it a specific enforcement point rather than leaving it as a general principle.

## 5. Open questions

- Is the decay-flag mechanism (§4) actually necessary, or does Boundary Architecture already prevent runaway propagation through a different mechanism (scope limits rather than decay)? Possible redundancy — flag for Contradiction Map.
- The per-layer threshold table (§3) is this draft's own inference, not confirmed anywhere in existing material — treat as Derived at best, likely Open, pending Crew-layer governance norms actually being specified elsewhere (Institutional Intelligence may be the right home for that).
- No Experiment yet designed — candidate: instrument an actual Crew-layer loop and check which threshold type it defaults to in practice, against the table's prediction.

---
*Derived from: Bidirectional Feedback Loops §2 Steps 2–3; Agency Architecture's per-layer agency table; Adapt & Iterate cross-cutting foundation. Companion to Learning Architecture.*
