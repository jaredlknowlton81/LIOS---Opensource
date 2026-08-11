# Context Lifecycle

Every `Context` carries a `lifecycle_stage`, walked in order by
`navigation.Navigator.advance()`:

```
LISTENING_POST -> OBSERVATORY -> KNOWLEDGE_GARDEN -> SCENARIO_ENGINE -> BLINK_OF_INSIGHT
```

## Stage meanings

**Listening Post** — raw signal collection. A Context starts here. You cannot
advance out of this stage with zero logged Events; the pipeline enforces that
Observatory work is grounded in at least one real signal, not started from
nothing.

**Observatory** — signals get looked at together. No new invariant is
enforced here yet; this is where a human, or a Provider's `Reflection`, starts
noticing patterns across the Events logged at Listening Post.

**Knowledge Garden** — patterns become Claims. This is where `Provider.reflect()`
is typically called and its output Claims get attached to the Context's active
Entities, each with a `ProvenanceRecord`.

**Scenario Engine** — Claims get projected forward. This is naturally where
`EpistemicMode.POSSIBILITY` work concentrates — same Context, same Layer,
different epistemic mode from where Listening Post started.

**Blink of Insight** — a Decision gets made. Not a Provider output — a human
Entity turns a Claim into a `Goal`. This is the only stage where
`EpistemicMode.DECISION` should be in play.

## Why advancement is manual, not automatic

`Navigator.advance()` never runs itself. A framework built around "AI expands
perception, you keep agency" should not have Contexts silently walking
themselves to Blink of Insight — the human (or the calling application on a
human's behalf) decides when a Context is ready to move forward. The one
guardrail (no advancing past Listening Post with zero Events) exists to keep
the data honest, not to automate judgment.

## Resetting

`Navigator.reset()` sends a Context back to Listening Post. Use this to start
a fresh cycle on the same Layer/EpistemicMode pairing — e.g. a recurring
weekly Dyadic Practice check-in reuses one Context across many cycles rather
than creating a new Context each week.
