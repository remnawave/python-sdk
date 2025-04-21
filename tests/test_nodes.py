import random

import pytest

from remnawave_api.models import (
    CreateNodeRequestDto,
    DeleteNodeResponseDto,
    NodeResponseDto,
    NodesResponseDto,
    ReorderNodeRequestDto,
    UpdateNodeRequestDto,
)
from tests.utils import generate_random_string


@pytest.mark.asyncio
async def test_nodes(remnawave):
    all_nodes = await remnawave.nodes.get_all_nodes()
    assert isinstance(all_nodes, NodesResponseDto)

    random_ip: str = f"{random.randint(500, 800)}" + ".0.0.1"
    random_port: int = random.randint(5000, 8000)
    random_name: str = generate_random_string()
    create_node = await remnawave.nodes.create_node(
        CreateNodeRequestDto(name=random_name, address=random_ip, port=random_port)
    )
    assert isinstance(create_node, NodeResponseDto)

    string_uuid = str(create_node.uuid)

    node = await remnawave.nodes.get_one_node(uuid=string_uuid)
    assert isinstance(node, NodeResponseDto)

    reorder_node = await remnawave.nodes.reorder_nodes(
        nodes=[ReorderNodeRequestDto(view_position=1, uuid=string_uuid)]
    )
    assert isinstance(reorder_node, NodesResponseDto)
    assert any(node.uuid == create_node.uuid for node in reorder_node.response)

    update_name: str = "TEST_NAME"
    update_node = await remnawave.nodes.update_node(
        UpdateNodeRequestDto(uuid=string_uuid, name=update_name)
    )
    assert isinstance(update_node, NodeResponseDto)
    assert update_node.uuid == create_node.uuid
    assert update_node.name == update_name

    delete_node = await remnawave.nodes.delete_node(uuid=string_uuid)
    assert isinstance(delete_node, DeleteNodeResponseDto)
    assert delete_node.is_deleted is True
