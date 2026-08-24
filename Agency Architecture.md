# Agency Architecture

**Status:** Open — no Experiment pairing yet exists (04_Experiments gap). Drafted for review.
**Position in LIA:** Layer-subsystem note — defines how agency (the capacity to act, decide, and be held accountable for acting) is distributed and constrained across Individual → Dyad → Crew → Network → Ecosystem.

---

## 1. Problem this component solves

Permission-Aware Routing governs whether *information* may move. Agency Architecture governs whether *action* may be taken, and by whom, once information has arrived. Without a distinct agency layer, the cross-layer integration components (Routing, Shared Context Protocol, Layer Adapters, Bidirectional Feedback Loops) would only describe how signals move — not who is authorized to act on them once they do. A ContextPacket crossing Crew→Network under full permission still needs an answer to "who at the Network layer is entitled to act on this, and within what bounds."

## 2. Core distinction: agency is layer-relative, not layer-absolute

An actor (human, AI, or hybrid pairing) does not carry a single fixed agency level across the whole stack. The same person may hold full unilateral agency at the Individual layer, shared/negotiated agency at the Dyad layer, delegated/bounded agency at the Crew layer, and representational (not personal) agency at the Network layer, speaking as a role rather than as themselves. Agency Architecture's core claim: **agency shrinks and changes in kind, not just in degree, as it moves outward through the layers** — this is the same directional asymmetry Layer Adapters already identifies for information (compression ≠ inverse of expansion applies to authority too).

## 3. Agency components per layer

| Layer | Nature of agency | Constraint mechanism |
|---|---|---|
| Individual | Full, unilateral | Self-imposed only |
| Dyad | Shared, negotiated | Mutual consent (ties to Relationship Architecture) |
| Crew | Delegated, bounded | Explicit scope grant, revocable |
| Network | Representational | Role-bound, accountable to Crew that delegated it |
| Ecosystem | Distributed, emergent | No single actor — governed by aggregate/institutional rules (ties to Institutional Intelligence) |

## 4. Relationship to AI agency specifically

The AI's own agency is not exempt from this table — it is a special case worth naming explicitly, since AgentVillage already treats `SKILL.md` files as institutional/policy layers rather than instructions. Under this architecture, a `SKILL.md` file is best read as a **Crew-layer delegated-agency grant to the AI**: bounded, revocable, scoped, and accountable back to whoever authored it — not a standing capability the AI carries into every context. This gives "librarian not manager" (from the cross-cutting foundations) a structural grounding rather than leaving it as a stylistic principle: the AI's agency is architecturally bounded to Step 1 (registration) in Bidirectional Feedback Loops, and Crew-layer delegation is what would be required to grant it Step 2/3 authority.

## 5. Open questions

- Does agency ever *expand* moving outward (e.g., an Ecosystem-layer emergent norm constraining what an Individual can unilaterally do) — is that a separate downward-flowing constraint mechanism, or the same table read in reverse?
- How does Agency Architecture interact with Boundary Architecture — is a boundary violation always an agency violation, or can a boundary be crossed with full agency but without permission (i.e., are Agency and Permission-Aware Routing actually orthogonal, not layered)?
- No Experiment yet designed — candidate: test whether the delegated-agency reading of `SKILL.md` files holds up against actual AgentVillage behavior, or whether agency in practice is more continuous than this five-row table suggests.

---
*Derived from: AgentVillage `SKILL.md` framing; Agency Architecture's position in the LIA layer stack; cross-reference against Layer Adapters and Agency's still-undrafted Experiment.*
