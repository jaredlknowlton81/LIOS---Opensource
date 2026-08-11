"""Entity — any actor/node in the system.

An Entity is deliberately scale-agnostic: the same class represents a person,
a small crew, a community, or an institution. What distinguishes them is not
their type alone but which Layer(s) of the Four-Layer System they show up in,
tracked via their Relationships and Events rather than hard-coded here.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


class EntityType(str, Enum):
    PERSON = "person"
    GROUP = "group"  # a crew / dyad / small-group unit
    COMMUNITY = "community"  # e.g. a Post Nation regenerative village
    INSTITUTION = "institution"  # Layer 4 / societal actor
    AI_AGENT = "ai_agent"  # a Provider, represented as a first-class entity


@dataclass
class Entity:
    """A node that can participate in Events, hold Claims, and form
    Relationships.
    """

    name: str
    type: EntityType = EntityType.PERSON
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    attributes: dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        return f"Entity({self.type.value}:{self.name})"
