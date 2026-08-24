# Layer Adapters

**Status:** Derived / Open — role implied by the cross-layer integration architecture; mechanism drafted here for review, not yet confirmed.
**Position in LIA:** Third of four cross-layer integration components (after Permission-Aware Routing and Shared Context Protocol; before Bidirectional Feedback Loops).
**Depends on:** Permission-Aware Routing (six-question gate), Shared Context Protocol (`ContextPacket` envelope).

---

## 1. Problem this component solves

Permission-Aware Routing decides *whether* information may move between layers. Shared Context Protocol decides *what envelope* it moves in. Neither says what happens when the packet **arrives** at a layer whose native representation, granularity, or tooling doesn't match the one it left. A `ContextPacket` built at the Individual layer (fine-grained, personal, informal) can't be dropped unmodified into the Network layer (coarse-grained, institutional, formal) — it needs translation, not just permission.

Layer Adapters are the translation function: they take a permitted, enveloped `ContextPacket` and reshape it into the native form of the receiving layer, in both directions.

## 2. Core mechanism

An adapter is defined per **layer-pair edge**, not per layer — because the transformation from Individual→Dyad is not the inverse of Dyad→Individual, and both differ from Crew→Network. Each edge adapter performs four operations on a `ContextPacket`:

1. **Granularity resolution** — aggregate or expand detail to match the receiving layer's native resolution (e.g., a Dyad's specific exchange compresses to a Crew-level pattern; a Network-level policy expands to Dyad-specific implications).
2. **Vocabulary translation** — remap terms/roles from the sending layer's ontology to the receiving layer's (personal language → institutional language, or vice versa).
3. **Provenance carry-through** — preserve the ContextPacket's origin-scope metadata (from Permission-Aware Routing) so the receiving layer knows what it's allowed to do with the translated artifact, not just what the artifact says.
4. **Fit check** — a lightweight validity gate: does the translated packet still make sense at the receiving layer, or does the adapter flag a translation failure (e.g., an Individual-layer emotional nuance that has no meaningful Network-layer equivalent and should be summarized as "context withheld" rather than forced into a form it doesn't fit)?

## 3. Adapters needed (five layers → four directional edges, both ways = 8 adapters)

| Edge | Compresses toward... | Native tech examples (from grounding material) |
|---|---|---|
| Individual → Dyad | shared context, still personal | ChatGPT memory → shared conversation |
| Dyad → Individual | personalized recall | — |
| Dyad → Crew | pattern extraction, de-identification of the specific exchange | Notion (shared workspace) |
| Crew → Dyad | relevant precedent surfaced | — |
| Crew → Network | institutional pattern, aggregated | AutoGen (multi-agent coordination) |
| Network → Crew | applicable policy/precedent | — |
| Network → Ecosystem | public/durable record | GitHub / Wikipedia |
| Ecosystem → Network | external signal ingestion | digital twins |

This table is a first pass — it inherits the layer/tech mapping already established in the LIA grounding material rather than inventing new correspondences.

## 4. Relationship to Bidirectional Feedback Loops (next component)

Layer Adapters are the *static* translation mechanism — they define how a packet's *form* changes crossing an edge. Bidirectional Feedback Loops (still undesigned) are the *dynamic* counterpart — they define how a change at one layer propagates back and alters behavior at another over time. Adapters make a single crossing legible; Feedback Loops make repeated crossings accumulate into learning/adaptation. It's reasonable to treat Adapters as a prerequisite for Feedback Loops: you can't loop information you can't yet translate.

## 5. Open questions carried forward

- Should adapters be symmetric in structure (one function, parameterized by direction) or genuinely separate mechanisms per direction, given that compression (moving up) and expansion (moving down) are not mirror-image operations?
- Where does adapter *failure* (the fit-check gate) route to — does a failed translation get logged in the Ledger Architecture, surfaced to the human, or silently dropped?
- Does each edge need one adapter, or does adapter behavior itself vary by ContextPacket type (e.g., a Ledger-type packet crossing Crew→Network translates differently than a Memory-type packet crossing the same edge)?

---
*Derived from: Living Intelligence — Master Architecture; Boundary Architecture; Context Architecture; Bartlett's Microsolidarity Five Scales grounding material. Cross-reference against 04_Experiments — no experiment yet exists for this component.*
