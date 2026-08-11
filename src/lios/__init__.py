"""LIOS — Living Intelligence Operating System.

A reflective, non-authoritative substrate for tracking direction, trust, and
shared understanding across personal, small-group, community, and societal
scales.
"""

__version__ = "0.1.0"

from lios.models.entity import Entity, EntityType
from lios.models.context import Context, Layer, EpistemicMode
from lios.models.event import Event, EventType
from lios.models.claim import Claim
from lios.models.relationship import Relationship, RelationshipType
from lios.models.goal import Goal, Horizon

__all__ = [
    "Entity",
    "EntityType",
    "Context",
    "Layer",
    "EpistemicMode",
    "Event",
    "EventType",
    "Claim",
    "Relationship",
    "RelationshipType",
    "Goal",
    "Horizon",
]
