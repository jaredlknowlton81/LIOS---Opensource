"""Event — something that happened.

Events are the raw material for closing the Testing Gap: they are timestamped,
attributable, and cheap to log (a two-question nightly reflection produces one
Event). The Meeting model's Signal -> Contact -> Resolution pipeline and the
Disclosure Spiral's eight stage transitions are both represented as Events.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


class EventType(str, Enum):
    SIGNAL = "signal"  # noticed something worth attending to
    CONTACT = "contact"  # a Meeting occurred between entities
    RESOLUTION = "resolution"  # a Meeting reached resolution
    TRUST_SHIFT = "trust_shift"  # trust level changed in a Relationship
    DISCLOSURE_TRANSITION = "disclosure_transition"  # moved a Disclosure Spiral stage
    REFLECTION = "reflection"  # e.g. a nightly two-question log entry


@dataclass
class Event:
    """A single, timestamped occurrence involving one or more Entities."""

    type: EventType
    context_id: str  # Context.id this occurred within
    entities: list[str] = field(default_factory=list)  # Entity ids involved
    description: str = ""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    metadata: dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        return f"Event({self.type.value} @ {self.timestamp.isoformat()})"
