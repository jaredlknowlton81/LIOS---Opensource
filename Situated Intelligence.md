# Situated Intelligence

**Status:** Open — no Experiment pairing yet exists (04_Experiments gap). Drafted for review. Resolves the division-of-labor question flagged in Context Architecture §4.

---

## 1. Problem this component solves

Context Architecture defines the *boundary* of relevant state for a given exchange — what counts as context, scoped along temporal, relational, and situational axes. It explicitly flagged an open overlap risk with this note: is Situated Intelligence a separate concern, or does it duplicate Context Architecture under a different name? This draft resolves that by taking Situated Intelligence to be about the **use** of scoped context — how a layer's intelligence (human, AI, or hybrid) actually draws on bounded context to act well, as distinct from how that context gets bounded in the first place.

## 2. Core definition

Situated intelligence is **the capacity to act appropriately using only the context actually available at a given layer and moment, without requiring context that scoping has excluded**. This makes it a *skill* or *property* of the acting node, evaluated against Context Architecture's boundary — not a separate boundary-setting mechanism. A node with poor situated intelligence might have perfectly well-scoped context (Context Architecture working correctly) and still act badly because it fails to use what's available, or reaches for context it doesn't actually have.

## 3. Why this matters distinctly from Context Architecture

If context scoping is a purely mechanical operation (temporal/relational/situational cuts) and situated intelligence is a purely usage-side skill, then a fit-check failure (Layer Adapters §2.4) could originate from *either* side, and Emergence Architecture's discipline (don't claim emergence before ruling out a tracing gap) applies here too: a bad outcome at a layer could be a Context Architecture failure (wrong scope), a Situated Intelligence failure (right scope, poor use), or both — and conflating them would misdirect any attempted fix.

## 4. Relationship to AI specifically

This is the note that gives "librarian not manager" (cross-cutting foundation, already tied to Agency Architecture's bounded-delegation reading of `SKILL.md`) its behavioral content: a librarian's situated intelligence is knowing what's in the room and helping the person use it, without either withholding available context or reaching past the room's actual boundary to manufacture false confidence. An AI with high situated intelligence, by this definition, should be *more* willing to say "I don't have context for that" than one optimizing for apparent helpfulness — a testable, slightly counter-intuitive prediction worth flagging for Novelty Claims.

## 5. Open questions

- Is situated intelligence layer-general (one capacity, exercised differently at each layer) or does each layer require a structurally distinct competence — i.e., does this note need its own per-layer table the way Agency and Adaptation Architecture do?
- The division of labor in §1 (Context Architecture = boundary, Situated Intelligence = use) is this draft's proposal, not confirmed prior art — flag as Derived, and revisit once the actual Situated Intelligence note's original intent (if different from this reconstruction) surfaces.
- No Experiment yet designed — candidate: hold context scope constant and vary only situated-intelligence-relevant factors (e.g., how a response uses available context) to isolate this note's claim from Context Architecture's.

---
*Derived from: Context Architecture §4 division-of-labor flag; Agency Architecture's "librarian not manager" reading; cross-reference against Layer Adapters' fit-check and Emergence Architecture's tracing discipline.*
