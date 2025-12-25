import pytest
from uuid import UUID

from remnawave.models import (
    # Legacy models (deprecated)
    GetNodesUsageByRangeResponseDto,
    GetNodesRealtimeUsageResponseDto,
    GetNodeUserUsageByRangeResponseDto,
    GetUserUsageByRangeResponseDto,
    
    # New stats models
    GetLegacyStatsUserUsageResponseDto,
    GetLegacyStatsNodesUsersUsageResponseDto,
    GetStatsNodesRealtimeUsageResponseDto,
    GetStatsNodesUsageResponseDto,
    GetStatsNodeUsersUsageResponseDto,
    GetStatsUserUsageResponseDto,
)
from tests.utils import generate_isoformat_range

@pytest.mark.asyncio
async def test_legacy_user_usage(remnawave):
    """Test legacy user usage endpoint (deprecated)"""
    # Get first user
    users = await remnawave.users.get_all_users()
    if not users.users:
        pytest.skip("No users available for testing")
    
    user_uuid = str(users.users[0].uuid)
    start, end = generate_isoformat_range()
    
    user_usage = await remnawave.bandwidthstats.get_user_usage_legacy_old(
        user_uuid=user_uuid,
        start=start,
        end=end
    )
    assert isinstance(user_usage, GetUserUsageByRangeResponseDto)
    assert len(user_usage) >= 0


@pytest.mark.asyncio
async def test_legacy_node_user_usage(remnawave):
    """Test legacy node user usage endpoint (deprecated)"""
    # Get first node
    nodes = await remnawave.nodes.get_all_nodes()
    if not nodes:
        pytest.skip("No nodes available for testing")
    
    node_uuid = str(nodes[0].uuid)
    start, end = generate_isoformat_range()
    
    node_user_usage = await remnawave.bandwidthstats.get_node_user_usage_legacy_old(
        node_uuid=node_uuid,
        start=start,
        end=end
    )
    assert isinstance(node_user_usage, GetNodeUserUsageByRangeResponseDto)
    assert len(node_user_usage) >= 0


@pytest.mark.asyncio
async def test_stats_nodes_realtime_usage(remnawave):
    """Test new stats nodes realtime usage endpoint"""
    realtime_usage = await remnawave.bandwidthstats.get_nodes_realtime_usage()
    assert isinstance(realtime_usage, GetStatsNodesRealtimeUsageResponseDto)
    assert hasattr(realtime_usage, 'response')
    assert isinstance(realtime_usage.response, list)
    
    # Check structure if data exists
    if realtime_usage.response:
        first_item = realtime_usage.response[0]
        assert hasattr(first_item, 'node_uuid')
        assert hasattr(first_item, 'node_name')
        assert hasattr(first_item, 'download_bytes')
        assert hasattr(first_item, 'upload_bytes')
        assert hasattr(first_item, 'total_bytes')


@pytest.mark.asyncio
async def test_stats_nodes_usage(remnawave):
    """Test new stats nodes usage endpoint with charts"""
    start, end = generate_isoformat_range()
    
    nodes_usage = await remnawave.bandwidthstats.get_stats_nodes_usage(
        start=start,
        end=end,
        top_nodes_limit=5
    )
    assert isinstance(nodes_usage, GetStatsNodesUsageResponseDto)
    assert hasattr(nodes_usage, 'response')
    assert hasattr(nodes_usage.response, 'categories')
    assert hasattr(nodes_usage.response, 'sparkline_data')
    assert hasattr(nodes_usage.response, 'top_nodes')
    assert hasattr(nodes_usage.response, 'series')
    
    # Check data types
    assert isinstance(nodes_usage.response.categories, list)
    assert isinstance(nodes_usage.response.sparkline_data, list)
    assert isinstance(nodes_usage.response.top_nodes, list)
    assert isinstance(nodes_usage.response.series, list)


@pytest.mark.asyncio
async def test_stats_node_users_usage(remnawave):
    """Test new stats node users usage endpoint"""
    # Get first node
    nodes = await remnawave.nodes.get_all_nodes()
    if not nodes:
        pytest.skip("No nodes available for testing")
    
    node_uuid = str(nodes[0].uuid)
    start, end = generate_isoformat_range()
    
    node_users_usage = await remnawave.bandwidthstats.get_stats_node_users_usage(
        uuid=node_uuid,
        start=start,
        end=end,
        top_users_limit=5
    )
    assert isinstance(node_users_usage, GetStatsNodeUsersUsageResponseDto)
    assert hasattr(node_users_usage, 'response')
    assert hasattr(node_users_usage.response, 'categories')
    assert hasattr(node_users_usage.response, 'sparkline_data')
    assert hasattr(node_users_usage.response, 'top_users')
    
    # Check data types
    assert isinstance(node_users_usage.response.categories, list)
    assert isinstance(node_users_usage.response.sparkline_data, list)
    assert isinstance(node_users_usage.response.top_users, list)


@pytest.mark.asyncio
async def test_stats_user_usage(remnawave):
    """Test new stats user usage endpoint"""
    # Get first user
    users = await remnawave.users.get_all_users()
    if not users.users:
        pytest.skip("No users available for testing")
    
    user_uuid = str(users.users[0].uuid)
    start, end = generate_isoformat_range()
    
    user_usage = await remnawave.bandwidthstats.get_stats_user_usage(
        uuid=user_uuid,
        start=start,
        end=end,
        top_nodes_limit=5
    )
    assert isinstance(user_usage, GetStatsUserUsageResponseDto)
    assert hasattr(user_usage, 'response')
    assert hasattr(user_usage.response, 'categories')
    assert hasattr(user_usage.response, 'sparkline_data')
    assert hasattr(user_usage.response, 'top_nodes')
    assert hasattr(user_usage.response, 'series')
    
    # Check data types
    assert isinstance(user_usage.response.categories, list)
    assert isinstance(user_usage.response.sparkline_data, list)
    assert isinstance(user_usage.response.top_nodes, list)
    assert isinstance(user_usage.response.series, list)


@pytest.mark.asyncio
async def test_legacy_stats_user_usage(remnawave):
    """Test legacy stats user usage endpoint"""
    # Get first user
    users = await remnawave.users.get_all_users()
    if not users.users:
        pytest.skip("No users available for testing")
    
    user_uuid = str(users.users[0].uuid)
    start, end = generate_isoformat_range()
    
    legacy_user_usage = await remnawave.bandwidthstats.get_user_usage_legacy_stats(
        uuid=user_uuid,
        start=start,
        end=end
    )
    assert isinstance(legacy_user_usage, GetLegacyStatsUserUsageResponseDto)
    assert hasattr(legacy_user_usage, 'response')
    assert isinstance(legacy_user_usage.response, list)
    
    # Check structure if data exists
    if legacy_user_usage.response:
        first_item = legacy_user_usage.response[0]
        assert hasattr(first_item, 'user_uuid')
        assert hasattr(first_item, 'node_uuid')
        assert hasattr(first_item, 'node_name')
        assert hasattr(first_item, 'total')


@pytest.mark.asyncio
async def test_legacy_stats_nodes_users_usage(remnawave):
    """Test legacy stats nodes users usage endpoint"""
    # Get first node
    nodes = await remnawave.nodes.get_all_nodes()
    if not nodes:
        pytest.skip("No nodes available for testing")
    
    node_uuid = str(nodes[0].uuid)
    start, end = generate_isoformat_range()
    
    legacy_node_users = await remnawave.bandwidthstats.get_node_users_usage_legacy_stats(
        uuid=node_uuid,
        start=start,
        end=end
    )
    assert isinstance(legacy_node_users, GetLegacyStatsNodesUsersUsageResponseDto)
    assert hasattr(legacy_node_users, 'response')
    assert isinstance(legacy_node_users.response, list)
    
    # Check structure if data exists
    if legacy_node_users.response:
        first_item = legacy_node_users.response[0]
        assert hasattr(first_item, 'user_uuid')
        assert hasattr(first_item, 'username')
        assert hasattr(first_item, 'node_uuid')
        assert hasattr(first_item, 'total')

@pytest.mark.asyncio
async def test_bandwidth_data_structure(remnawave):
    """Test bandwidth stats data structure validity"""
    start, end = generate_isoformat_range()
    
    # Get realtime data
    realtime = await remnawave.bandwidthstats.get_nodes_realtime_usage()
    
    if realtime.response:
        # Verify each node has required fields
        for node in realtime.response:
            assert isinstance(node.node_uuid, UUID)
            assert isinstance(node.node_name, str)
            assert isinstance(node.download_bytes, (int, float))
            assert isinstance(node.upload_bytes, (int, float))
            assert isinstance(node.total_bytes, (int, float))
            assert node.total_bytes >= 0
    
    # Get stats data
    stats = await remnawave.bandwidthstats.get_stats_nodes_usage(
        start=start,
        end=end,
        top_nodes_limit=3
    )
    
    # Verify stats structure
    assert len(stats.response.categories) == len(stats.response.sparkline_data)
    assert len(stats.response.top_nodes) <= 3
    
    if stats.response.series:
        for series_item in stats.response.series:
            assert len(series_item.data) == len(stats.response.categories)