import pytest

from lios.provenance import ProvenanceLedger, SourceKind


def test_record_and_link_claim():
    ledger = ProvenanceLedger()
    rec = ledger.record(SourceKind.HUMAN_REPORT, source_ref="event-123", method="manual entry")
    ledger.link_claim("claim-1", rec.id)
    traced = ledger.trace("claim-1")
    assert traced is not None
    assert traced.source_ref == "event-123"


def test_link_unknown_provenance_raises():
    ledger = ProvenanceLedger()
    with pytest.raises(KeyError):
        ledger.link_claim("claim-1", "nonexistent-id")


def test_audit_flags_unlinked_claims():
    ledger = ProvenanceLedger()
    rec = ledger.record(SourceKind.OBSERVED_EVENT, source_ref="event-1")
    ledger.link_claim("claim-1", rec.id)
    missing = ledger.audit(["claim-1", "claim-2", "claim-3"])
    assert missing == ["claim-2", "claim-3"]
