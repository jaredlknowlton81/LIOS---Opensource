# Boundary Architecture

**Status:** Open — no Experiment pairing yet exists (04_Experiments gap). Drafted for review. Resolves an open question flagged in Bidirectional Feedback Loops §5.

---

## 1. Problem this component solves

Permission-Aware Routing decides whether a specific piece of information may move. Agency Architecture decides who may act. Neither specifies what happens when two layers' own internal rules *conflict* — e.g., Bidirectional Feedback Loops §5 asked directly: when Crew-layer activation and Network-layer activation logic disagree, does Boundary Architecture arbitrate? This note answers yes, and specifies how.

## 2. Core definition

A boundary, in this framework, is **a standing constraint on what may cross between two layers, set independently of any single exchange** — as distinct from a permission decision (Permission-Aware Routing), which is made per-packet, and from agency (Agency Architecture), which governs actors rather than the space between layers. Boundaries are the *background rules* Permission-Aware Routing's six-question mechanism operates within; a packet can pass every one of the six questions and still be blocked if it violates a standing boundary.

## 3. Boundary Architecture as arbiter — resolving the Bidirectional Feedback Loops open question

When Crew-layer and Network-layer activation thresholds (Adaptation Architecture §3) genuinely conflict — Crew has confirmed and wants to propagate, Network's own threshold logic would reject the same signal — this note proposes Boundary Architecture holds the deciding rule, on the following basis: **a lower layer's confirmed adaptation may cross a boundary into a higher layer only if it does not itself attempt to override that higher layer's own threshold logic.** Concretely: Crew can propagate the *candidate* (a registration, per Learning Architecture) to Network regardless of the conflict, but cannot force Network past its own Step 2 threshold — that decision stays with Network. This keeps the arbitration answer consistent with Agency Architecture's claim that agency shrinks in kind moving outward: Crew's agency to propagate does not include Network's agency to activate.

## 4. Boundary types

1. **Hard boundaries** — cannot be crossed regardless of permission or agency (e.g., raw Individual-layer self-model data should never reach Ecosystem layer in identifiable form — a hard boundary, not just a routing decision).
2. **Soft boundaries** — can be crossed with sufficient permission/agency but require the standing default to be explicitly overridden, leaving a Ledger trace of the override (ties to Selective Sharing).
3. **Threshold-arbitration boundaries** — the category described in §3, specific to resolving conflicting Adaptation Architecture logic across layers.

## 5. Relationship to Exit & Repair

Boundary Architecture is the natural mechanical home for the Exit & Repair cross-cutting foundation: "exit" is a hard boundary a node can invoke unilaterally on its own behalf (withdrawing from a Dyad or Crew relationship), while "repair" is the process for renegotiating a soft boundary after a violation. Framing Exit & Repair this way makes it an instance of Boundary Architecture rather than a free-standing principle — worth checking against how Exit & Repair is described elsewhere before treating this as settled.

## 6. Open questions

- Are hard boundaries ever revisable, or are they definitionally the *non*-revisable category — and if the latter, who has the agency to declare something a hard boundary in the first place (this is itself an Agency Architecture question, applied reflexively to Boundary Architecture's own rule-setting)?
- Does §3's arbitration rule generalize cleanly to all layer pairs, or only Crew↔Network specifically (the case that prompted it)? Currently only justified for that one pair.
- No Experiment yet designed — candidate: the Ledger Experiment may already be positioned to test soft-boundary override tracing (§4.2), since both concern what gets logged when a default is crossed.

---
*Derived from: Bidirectional Feedback Loops §5 open question; Adaptation Architecture §3 threshold table; Agency Architecture's agency-shrinks-outward claim; cross-reference against Exit & Repair, Selective Sharing, Ledger Architecture.*
