from datetime import datetime, timedelta

import pytest

from remnawave_api.models import (
    GetNodeUserUsageByRangeResponseDto,
    GetNodesUsageByRangeResponseDto,
)
from tests.conftest import REMNAWAVE_USER_UUID


@pytest.mark.asyncio
async def test_nodes_usage_history(remnawave) -> None:
    # Test get nodes usage by range
    start_date = (datetime.now() - timedelta(days=7)).isoformat()
    end_date = datetime.now().isoformat()
    
    nodes_usage = await remnawave.nodes_usage_history.get_nodes_usage_by_range(
        start=start_date,
        end=end_date
    )
    
    assert isinstance(nodes_usage, GetNodesUsageByRangeResponseDto)
    # Response should be a list now (RootModel)
    assert isinstance(nodes_usage.root, list)


@pytest.mark.asyncio
async def test_nodes_user_usage_history(remnawave) -> None:
    start_date = (datetime.now() - timedelta(days=7)).isoformat()
    end_date = datetime.now().isoformat()
    
    node_user_usage = await remnawave.nodes_user_usage_history.get_node_user_usage_by_range(
        uuid=REMNAWAVE_USER_UUID,
        start=start_date,
        end=end_date
    )
    
    assert isinstance(node_user_usage, GetNodeUserUsageByRangeResponseDto)
    

