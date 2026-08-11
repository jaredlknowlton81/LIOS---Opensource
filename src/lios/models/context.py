"""Context — situates every Event and Claim.

A Context is the resolution of the open integration question in the Living
Intelligence Model: it is a Layer (a point on the Four-Layer scale axis)
*combined with* an EpistemicMode (a point on the Reality/Possibility/Decision
axis), plus a lifecycle stage in the Listening Post -> ... -> Blink of Insight
pipeline. Layer and EpistemicMode are independent axes on the same Context —
neither nests inside the other. See docs/ontology.md for the reasoning.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum


class Layer(str, Enum):
    """The Four-Layer System scale axis."""

    PERSONAL = "personal"
    SMALL_GROUP = "small_group"
    COMMUNITY = "community"
    SOCIETAL = "societal"


class EpistemicMode(str, Enum):
    """The Reality/Possibility/Decision stack — orthogonal to Layer."""

    REALITY = "reality"  # what is verifiably true / observed
    POSSIBILITY = "possibility"  # what could be true / could happen
    DECISION = "decision"  # what will be acted on


class LifecycleStage(str, Enum):
    """Stages of the Listening Post -> Blink of Insight pipeline."""

    LISTENING_POST = "listening_post"
    OBSERVATORY = "observatory"
    KNOWLEDGE_GARDEN = "knowledge_garden"
    SCENARIO_ENGINE = "scenario_engine"
    BLINK_OF_INSIGHT = "blink_of_insight"


# Order in which stages naturally progress. Navigator.advance() walks this list.
LIFECYCLE_ORDER: list[LifecycleStage] = [
    LifecycleStage.LISTENING_POST,
    LifecycleStage.OBSERVATORY,
    LifecycleStage.KNOWLEDGE_GARDEN,
    LifecycleStage.SCENARIO_ENGINE,
    LifecycleStage.BLINK_OF_INSIGHT,
]


@dataclass
class Context:
    """A situating frame: one Layer x one EpistemicMode x a lifecycle stage.

    Contexts can nest via `parent_context` — e.g. a SMALL_GROUP context whose
    parent is a COMMUNITY context — but Layer and EpistemicMode themselves
    never nest inside each other.
    """

    layer: Layer
    epistemic_mode: EpistemicMode = EpistemicMode.REALITY
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    lifecycle_stage: LifecycleStage = LifecycleStage.LISTENING_POST
    active_entities: list[str] = field(default_factory=list)  # Entity ids
    parent_context: str | None = None  # Context id
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        return (
            f"Context({self.layer.value}/{self.epistemic_mode.value}, "
            f"{self.lifecycle_stage.value})"
        )
