"""Claim — an assertion produced by a Knowledge Garden pass.

A Claim is never ground truth. It always carries a confidence level and a
provenance reference (see provenance.py), and it can be superseded by a later
Claim as understanding develops. This is the code-level enforcement of the
Community Mirror's verification principle: nothing gets treated as settled
just because an AI provider said it.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum

from lios.models.context import EpistemicMode


class ClaimStatus(str, Enum):
    ACTIVE = "active"
    SUPERSEDED = "superseded"
    RETRACTED = "retracted"


@dataclass
class Claim:
    """An assertion about an Entity or situation, always provisional."""

    content: str
    subject_entity: str  # Entity id the claim is about
    confidence: float = 0.5  # 0.0-1.0, never presented as certainty
    epistemic_mode: EpistemicMode = EpistemicMode.POSSIBILITY
    provenance_id: str | None = None  # ProvenanceRecord.id
    status: ClaimStatus = ClaimStatus.ACTIVE
    superseded_by: str | None = None  # Claim id
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __post_init__(self) -> None:
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0.0 and 1.0")

    def supersede(self, new_claim: "Claim") -> None:
        """Mark this claim as superseded by a newer one. Never mutates content —
        claims are append-only; supersession is a pointer, not an edit."""
        self.status = ClaimStatus.SUPERSEDED
        self.superseded_by = new_claim.id
