"""Relationship — a trust/coordination link between two Entities.

Covers Layer 2 mechanics: the Weekly Dyadic Practice and Exit-First
Coordination protocol, as well as looser ties like mentorship or crew
membership.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum


class RelationshipType(str, Enum):
    DYADIC_PRACTICE = "dyadic_practice"  # Weekly Dyadic Practice pairing
    EXIT_FIRST_COORDINATION = "exit_first_coordination"
    MENTORSHIP = "mentorship"
    CREW = "crew"  # Microsolidarity-style crew membership
    GENERAL = "general"


@dataclass
class Relationship:
    """A directed-or-undirected link between two Entities, carrying a trust
    level that Events (esp. TRUST_SHIFT) update over time."""

    entity_a: str  # Entity id
    entity_b: str  # Entity id
    type: RelationshipType = RelationshipType.GENERAL
    trust_level: float = 0.5  # 0.0-1.0
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    last_interaction: datetime | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __post_init__(self) -> None:
        if not 0.0 <= self.trust_level <= 1.0:
            raise ValueError("trust_level must be between 0.0 and 1.0")

    def record_interaction(self, trust_delta: float = 0.0) -> None:
        """Call when a TRUST_SHIFT Event touches this relationship."""
        self.last_interaction = datetime.now(timezone.utc)
        self.trust_level = min(1.0, max(0.0, self.trust_level + trust_delta))

    def involves(self, entity_id: str) -> bool:
        return entity_id in (self.entity_a, self.entity_b)
