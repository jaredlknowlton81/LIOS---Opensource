"""Goal — directional intent, scoped to a Garden System time horizon.

Goals are how "Directional Insight" (from the AI-as-mirror pipeline) becomes
"Actionable Steps." A Goal can have a parent Goal, letting an annual 80,000
Hours-style direction decompose into daily/weekly commitments.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum


class Horizon(str, Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    ANNUAL = "annual"


class GoalStatus(str, Enum):
    ACTIVE = "active"
    DONE = "done"
    DROPPED = "dropped"


@dataclass
class Goal:
    """A directional commitment held by an Entity."""

    entity_id: str  # Entity id who holds this goal
    description: str
    horizon: Horizon = Horizon.WEEKLY
    status: GoalStatus = GoalStatus.ACTIVE
    parent_goal: str | None = None  # Goal id, for goal trees
    linked_claims: list[str] = field(default_factory=list)  # Claim ids that motivated this goal
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def complete(self) -> None:
        self.status = GoalStatus.DONE

    def drop(self) -> None:
        self.status = GoalStatus.DROPPED
