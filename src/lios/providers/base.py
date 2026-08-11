"""Provider — the AI-as-mirror interface.

This is the load-bearing abstraction for "AI expands perception, you keep
agency." A Provider can only ever return a `Reflection`: a bundle of Claims,
each carrying confidence and provenance. There is deliberately no method on
this interface, and no field on Reflection, that lets a provider return a
Decision or a directive. Decisions are made by Entities, expressed as Goals,
outside this module entirely.

If you find yourself wanting a provider to "just decide," that is a signal to
stop and route the choice back to a human Entity instead of extending this
interface.
"""

from __future__ import annotations

import abc
from dataclasses import dataclass, field
from datetime import datetime, timezone

from lios.models.claim import Claim
from lios.models.context import Context, EpistemicMode


@dataclass
class Reflection:
    """The only thing a Provider is allowed to return.

    A Reflection is a set of candidate Claims plus optional pattern notes. It
    intentionally has no `decision`, `recommendation`, or `directive` field.
    """

    claims: list[Claim] = field(default_factory=list)
    pattern_notes: list[str] = field(default_factory=list)
    generated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __post_init__(self) -> None:
        for claim in self.claims:
            if claim.epistemic_mode == EpistemicMode.DECISION:
                raise ValueError(
                    "A Provider cannot emit a DECISION-mode claim. "
                    "Decisions belong to Entities, expressed as Goals."
                )


class Provider(abc.ABC):
    """Abstract base for any AI backend plugged into LIOS.

    Implementations wrap a specific model or service, but every implementation
    must reduce to `reflect()` returning a Reflection — never a decision.
    """

    name: str = "unnamed-provider"

    @abc.abstractmethod
    def reflect(self, context: Context, prompt: str) -> Reflection:
        """Given a Context and a prompt (e.g. "what pattern do you see in
        these events?"), return a Reflection: candidate Claims with
        confidence and provenance, never a directive.
        """
        raise NotImplementedError


class NullProvider(Provider):
    """A no-op reference implementation, useful for tests and as a template."""

    name = "null-provider"

    def reflect(self, context: Context, prompt: str) -> Reflection:
        return Reflection(claims=[], pattern_notes=["NullProvider emits no claims."])
