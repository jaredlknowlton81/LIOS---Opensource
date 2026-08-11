"""Integration — where cross-framework reconciliation happens.

Two concrete jobs live here:

1. Resolving which Layer a given Entity/Community construct (Post Nation
   village, Microsolidarity crew) maps onto, so the Four-Layer System, Post
   Nation, and Microsolidarity can share one Entity/Context graph instead of
   three parallel ontologies.
2. Confirming that EpistemicMode (Reality/Possibility/Decision) is treated as
   an axis orthogonal to Layer, never nested inside it — this module is the
   place that would break first if that assumption stopped holding, so it's
   the natural home for the reconciliation logic and its tests.
"""

from __future__ import annotations

from lios.models.context import Context, EpistemicMode, Layer
from lios.models.entity import Entity, EntityType

# Maps a construct name from an adjacent framework to the Layer it occupies
# in LIOS's Four-Layer System. Extend this as new frameworks get integrated.
FRAMEWORK_LAYER_MAP: dict[str, Layer] = {
    "post_nation_village": Layer.COMMUNITY,
    "post_nation_resident": Layer.PERSONAL,
    "microsolidarity_crew": Layer.SMALL_GROUP,
    "microsolidarity_scale_of_belonging": Layer.SMALL_GROUP,
    "regenerative_research_village": Layer.COMMUNITY,
    "institution": Layer.SOCIETAL,
}


def resolve_layer(framework_construct: str) -> Layer:
    """Look up which Four-Layer scale a named construct from an adjacent
    framework (Post Nation, Microsolidarity, etc.) belongs to."""
    try:
        return FRAMEWORK_LAYER_MAP[framework_construct]
    except KeyError as exc:
        raise KeyError(
            f"Unmapped framework construct: {framework_construct!r}. "
            "Add it to FRAMEWORK_LAYER_MAP before using it."
        ) from exc


def entity_type_for_layer(layer: Layer) -> EntityType:
    """A reasonable default EntityType for a given Layer, used when creating
    Entities from imported framework data without more specific typing."""
    return {
        Layer.PERSONAL: EntityType.PERSON,
        Layer.SMALL_GROUP: EntityType.GROUP,
        Layer.COMMUNITY: EntityType.COMMUNITY,
        Layer.SOCIETAL: EntityType.INSTITUTION,
    }[layer]


def make_context(layer: Layer, epistemic_mode: EpistemicMode = EpistemicMode.REALITY,
                  parent_context: str | None = None) -> Context:
    """Construct a Context, making the Layer x EpistemicMode orthogonality
    explicit at the call site rather than implicit."""
    return Context(layer=layer, epistemic_mode=epistemic_mode, parent_context=parent_context)


def import_framework_entity(name: str, framework_construct: str) -> tuple[Entity, Context]:
    """Bring an Entity from an adjacent framework (Post Nation, Microsolidarity)
    into LIOS's graph, resolving its Layer and a default Context in one step.
    """
    layer = resolve_layer(framework_construct)
    entity = Entity(name=name, type=entity_type_for_layer(layer))
    context = make_context(layer=layer)
    context.active_entities.append(entity.id)
    return entity, context
