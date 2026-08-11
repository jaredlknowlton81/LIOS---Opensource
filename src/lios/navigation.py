"""Navigation — the Listening Post -> Observatory -> Knowledge Garden ->
Scenario Engine -> Blink of Insight pipeline, as an explicit state machine
over Context objects.

This exists so the "Journey From Paper Map to Living Landscape" arc is
something you can actually run against logged Events, instead of only
narrating.
"""

from __future__ import annotations

from lios.models.context import LIFECYCLE_ORDER, Context, LifecycleStage
from lios.models.event import Event


class Navigator:
    """Logs Events and advances Contexts through the lifecycle pipeline."""

    def __init__(self) -> None:
        self._events: list[Event] = []

    def log(self, event: Event) -> Event:
        """Record an Event (a signal, contact, resolution, etc.)."""
        self._events.append(event)
        return event

    def events_for(self, context: Context) -> list[Event]:
        return [e for e in self._events if e.context_id == context.id]

    def advance(self, context: Context) -> LifecycleStage:
        """Move a Context to the next lifecycle stage.

        Advancing from LISTENING_POST requires at least one logged Event —
        you can't move to Observatory on the strength of zero signals. Every
        later stage advances freely, since Knowledge Garden / Scenario Engine
        / Blink of Insight work is expected to happen off fresh Events too.
        """
        current_index = LIFECYCLE_ORDER.index(context.lifecycle_stage)

        if context.lifecycle_stage == LifecycleStage.LISTENING_POST and not self.events_for(context):
            raise ValueError(
                "Cannot advance past Listening Post with zero logged events "
                "for this context. Log a signal first."
            )

        if current_index + 1 >= len(LIFECYCLE_ORDER):
            return context.lifecycle_stage  # already at Blink of Insight

        context.lifecycle_stage = LIFECYCLE_ORDER[current_index + 1]
        return context.lifecycle_stage

    def reset(self, context: Context) -> None:
        """Send a Context back to Listening Post — e.g. starting a new cycle."""
        context.lifecycle_stage = LifecycleStage.LISTENING_POST
