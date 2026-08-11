import pytest

from lios.integration import (
    entity_type_for_layer,
    import_framework_entity,
    resolve_layer,
)
from lios.models.context import Layer
from lios.models.entity import EntityType


def test_resolve_layer_known_constructs():
    assert resolve_layer("post_nation_village") == Layer.COMMUNITY
    assert resolve_layer("microsolidarity_crew") == Layer.SMALL_GROUP
    assert resolve_layer("institution") == Layer.SOCIETAL


def test_resolve_layer_unknown_raises():
    with pytest.raises(KeyError):
        resolve_layer("not_a_real_construct")


def test_entity_type_for_layer():
    assert entity_type_for_layer(Layer.PERSONAL) == EntityType.PERSON
    assert entity_type_for_layer(Layer.COMMUNITY) == EntityType.COMMUNITY


def test_import_framework_entity_creates_matching_context():
    entity, context = import_framework_entity("Riverbend Village", "post_nation_village")
    assert entity.type == EntityType.COMMUNITY
    assert context.layer == Layer.COMMUNITY
    assert entity.id in context.active_entities
