# Institutional Intelligence

**Status:** Open — no Experiment pairing yet exists (04_Experiments gap). Drafted for review. Resolves two open questions flagged in Agency Architecture and Adaptation Architecture.

---

## 1. Problem this component solves

Two prior notes deferred specific questions here by name. Agency Architecture's Network row describes agency as "representational... accountable to Crew that delegated it" but didn't specify the mechanism of accountability. Adaptation Architecture's Network row requires "formalized, auditable decisions" but noted that Crew-layer governance norms are "not fixed by this architecture alone" and pointed here. Institutional Intelligence is the note that supplies both: the formal mechanism by which Network-layer (and, by extension, Ecosystem-layer) representational agency is held accountable.

## 2. Core definition

Institutional intelligence is **the capacity of a layer to act consistently on behalf of others without direct, per-decision confirmation from every party it represents** — the thing that makes representational agency (Agency Architecture) workable at all, since requiring per-decision confirmation from an entire Crew for every Network-layer act would collapse the Network layer back into an unwieldy Crew-layer process. Institutional intelligence substitutes standing rules and auditability for per-instance confirmation.

## 3. The accountability mechanism (resolving Agency Architecture's deferral)

A Network-layer act is accountable to its delegating Crew when three conditions hold:
1. **Scope legibility** — the delegation grant (the `SKILL.md`-style Crew-layer grant described in Agency Architecture §4) is explicit enough that a Crew member can check any given Network act against it without needing to have witnessed the act itself.
2. **Ledger traceability** — per Identity & Continuity §2, the act is recorded such that its chain back to the originating delegation is legible, not just asserted.
3. **Revocability** — the Crew retains the standing ability to narrow or withdraw the delegation (ties to Boundary Architecture §4.2, soft boundaries), and that ability isn't itself gated behind Network-layer approval — otherwise "delegated" agency would have quietly become independent agency.

## 4. Formalized decisions (resolving Adaptation Architecture's deferral)

Adaptation Architecture's Network row calls for "explicit confirmation, formalized." Institutional Intelligence specifies what formalization adds beyond an ordinary explicit-confirmation threshold: a formalized decision is one where the confirming rule itself (not just the confirming act) is written down in advance and applied consistently across instances — which is what makes it auditable under §3's Ledger-traceability condition. An informal explicit confirmation ("someone at Network layer agreed") doesn't satisfy the Network-layer threshold type on its own; it needs to cite which standing rule the agreement applied.

## 5. Open questions

- Does Institutional Intelligence apply *only* to the Network layer, or does Ecosystem-layer emergent governance (per Emergence Architecture) also require something like institutional intelligence, despite Emergence Architecture explicitly noting "no single confirming actor exists at this layer"? If Ecosystem needs it too, the mechanism in §3–4 (which presupposes an identifiable delegating Crew) would need real revision, not just extension.
- Is §3's three-condition accountability test sufficient, or does it need a fourth condition addressing what happens when Ledger traceability (condition 2) and scope legibility (condition 1) conflict — e.g., a Network act is traceable but turns out to exceed its cited delegation?
- No Experiment yet designed — candidate: audit an actual Network-layer decision from the existing tech-example mapping (GitHub/Wikipedia governance is the natural test case, per the layer/tech table already established) against the three conditions in §3.

---
*Derived from: Agency Architecture §4 (delegated-agency reading of `SKILL.md`); Adaptation Architecture §3 (Network threshold row); Boundary Architecture §4.2; Identity & Continuity §2.*
