from lios.models.context import Context, EpistemicMode, Layer, LifecycleStage


def test_context_defaults():
    ctx = Context(layer=Layer.PERSONAL)
    assert ctx.epistemic_mode == EpistemicMode.REALITY
    assert ctx.lifecycle_stage == LifecycleStage.LISTENING_POST
    assert ctx.active_entities == []


def test_layer_and_epistemic_mode_are_independent():
    for layer in Layer:
        for mode in EpistemicMode:
            ctx = Context(layer=layer, epistemic_mode=mode)
            assert ctx.layer == layer
            assert ctx.epistemic_mode == mode


def test_context_nesting():
    parent = Context(layer=Layer.COMMUNITY)
    child = Context(layer=Layer.SMALL_GROUP, parent_context=parent.id)
    assert child.parent_context == parent.id
