# Learning Architecture

**Status:** Open — no Experiment pairing yet exists (04_Experiments gap). Drafted for review.
**Position in LIA:** Layer-subsystem note — defines "internal change" as used in Bidirectional Feedback Loops §2 Step 1 (Registration).

---

## 1. Problem this component solves

Bidirectional Feedback Loops splits internal change (learning) from behavioral change (adaptation) as two sequential steps, but only sketched what "learning" means in passing — as a Ledger event, a candidate update to a layer's self-model. This note specifies what learning actually consists of: what changes, in what form, and by what criteria a registered signal counts as *learned* rather than merely received.

## 2. Core definition

Learning, in this framework, is **a durable change to a layer's model of itself or its environment, occurring prior to and independent of any resulting behavior change**. The independence clause matters: a layer can learn something true and useful and still not act on it (pending Bidirectional Feedback Loops' Step 2 threshold), and a layer can act differently without having "learned" anything in this sense (e.g., a one-off accommodation that doesn't update the underlying model — see Adaptation Architecture for that distinction).

## 3. What gets updated

Three candidate targets for a learning event, borrowed from the layer/model language already used elsewhere in the framework:

1. **Self-model** — what the layer believes about its own state, capacity, or history (ties to Identity & Continuity).
2. **Environment-model** — what the layer believes about other layers, actors, or conditions outside itself (this is the target most directly fed by translated ContextPackets arriving via Layer Adapters).
3. **Relationship-model** — what the layer believes about a specific ongoing Dyad or Crew relationship (ties directly to Relationship Architecture's accumulation criterion — arguably, this target *is* what Relationship Architecture calls "accumulation").

## 4. Confirmation criteria — when is a candidate update actually "learned"

A Registration event (Bidirectional Feedback Loops Step 1) becomes confirmed learning when it survives contact with new, potentially disconfirming information — the same logic behind the framework's own Confirmed/Derived/Open/Unconfirmed epistemic-status labels, applied here at the mechanism level rather than the documentation level. This gives Learning Architecture a direct, useful parallel to 03_Research's own apparatus: a layer's internal learning process and the vault's own research process are structurally the same operation, run at different scales.

## 5. Relationship to Adaptation Architecture

Learning is necessary but not sufficient for adaptation. The clean division: Learning Architecture governs what crosses from *unregistered* to *registered-and-confirmed*; Adaptation Architecture (companion note) governs what crosses from *confirmed* to *behavior change* — i.e., Bidirectional Feedback Loops' Step 2 threshold and Step 3 propagation are Adaptation Architecture's proper subject matter, not this note's. Drafting these as two notes rather than one is a deliberate choice to keep "what a layer believes" and "what a layer does" independently revisable.

## 6. Open questions

- Can a layer un-learn something — i.e., does disconfirmation retract a previously-confirmed self/environment/relationship-model update, or does it just add a new, contradictory registration (leaving both in the Ledger, à la Contradiction Map)?
- Is the three-target list (§3) exhaustive, or does Institutional Intelligence require a fourth target — a *norm-model* — that doesn't reduce cleanly to self/environment/relationship?
- No Experiment yet designed — candidate: test whether the confirmation criterion in §4 (survives disconfirming information) is actually how learning happens in practice, or whether layers in the actual AgentVillage implementation confirm updates on weaker grounds (repetition alone, without genuine disconfirmation-testing).

---
*Derived from: Bidirectional Feedback Loops §2 Step 1; Confirmed/Derived/Open/Unconfirmed epistemic-status framework; cross-reference against Adaptation Architecture, Identity & Continuity, Relationship Architecture.*
