import pytest

from lios.models.context import Context, Layer, LifecycleStage
from lios.models.event import Event, EventType
from lios.navigation import Navigator


def test_cannot_advance_listening_post_without_events():
    ctx = Context(layer=Layer.PERSONAL)
    nav = Navigator()
    with pytest.raises(ValueError):
        nav.advance(ctx)


def test_advance_through_full_pipeline():
    ctx = Context(layer=Layer.PERSONAL)
    nav = Navigator()
    nav.log(Event(type=EventType.SIGNAL, context_id=ctx.id, description="noticed a pattern"))

    stages = [
        LifecycleStage.OBSERVATORY,
        LifecycleStage.KNOWLEDGE_GARDEN,
        LifecycleStage.SCENARIO_ENGINE,
        LifecycleStage.BLINK_OF_INSIGHT,
    ]
    for expected in stages:
        assert nav.advance(ctx) == expected

    # advancing past the end is a no-op, stays at Blink of Insight
    assert nav.advance(ctx) == LifecycleStage.BLINK_OF_INSIGHT


def test_reset_returns_to_listening_post():
    ctx = Context(layer=Layer.PERSONAL)
    nav = Navigator()
    nav.log(Event(type=EventType.SIGNAL, context_id=ctx.id))
    nav.advance(ctx)
    nav.reset(ctx)
    assert ctx.lifecycle_stage == LifecycleStage.LISTENING_POST


def test_events_for_filters_by_context():
    ctx_a = Context(layer=Layer.PERSONAL)
    ctx_b = Context(layer=Layer.COMMUNITY)
    nav = Navigator()
    nav.log(Event(type=EventType.SIGNAL, context_id=ctx_a.id))
    nav.log(Event(type=EventType.SIGNAL, context_id=ctx_b.id))
    assert len(nav.events_for(ctx_a)) == 1
    assert len(nav.events_for(ctx_b)) == 1
