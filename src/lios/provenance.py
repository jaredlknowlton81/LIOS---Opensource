"""Provenance — the verification principle in code.

Every Claim should be traceable to a ProvenanceRecord answering: who or what
produced this, from what source material, and via what method. Claims without
a resolvable ProvenanceRecord are a code smell — `ProvenanceLedger.audit()`
surfaces them so they don't quietly become treated as settled.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum


class SourceKind(str, Enum):
    HUMAN_REPORT = "human_report"  # e.g. a nightly reflection entry
    PROVIDER_REFLECTION = "provider_reflection"  # produced by an AI Provider
    OBSERVED_EVENT = "observed_event"  # derived directly from an Event
    EXTERNAL_DOCUMENT = "external_document"  # imported from outside LIOS


@dataclass
class ProvenanceRecord:
    """Where a Claim came from and how much to trust the chain."""

    source_kind: SourceKind
    source_ref: str  # id of the Event, Provider, or document this traces to
    method: str = ""  # e.g. "gpt-x reflection pass", "manual entry"
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class ProvenanceLedger:
    """In-memory registry of ProvenanceRecords, keyed by id.

    A real deployment would back this with `storage.py`; kept separate here so
    provenance can be audited independently of *where* data lives.
    """

    def __init__(self) -> None:
        self._records: dict[str, ProvenanceRecord] = {}
        # claim_id -> provenance_id, tracked externally by callers so this
        # module has no dependency on models.claim.
        self._claim_links: dict[str, str] = {}

    def record(self, source_kind: SourceKind, source_ref: str, method: str = "") -> ProvenanceRecord:
        rec = ProvenanceRecord(source_kind=source_kind, source_ref=source_ref, method=method)
        self._records[rec.id] = rec
        return rec

    def link_claim(self, claim_id: str, provenance_id: str) -> None:
        if provenance_id not in self._records:
            raise KeyError(f"Unknown provenance id: {provenance_id}")
        self._claim_links[claim_id] = provenance_id

    def get(self, provenance_id: str) -> ProvenanceRecord | None:
        return self._records.get(provenance_id)

    def trace(self, claim_id: str) -> ProvenanceRecord | None:
        provenance_id = self._claim_links.get(claim_id)
        return self._records.get(provenance_id) if provenance_id else None

    def audit(self, claim_ids: list[str]) -> list[str]:
        """Return the subset of claim_ids that have NO provenance on file."""
        return [cid for cid in claim_ids if cid not in self._claim_links]
