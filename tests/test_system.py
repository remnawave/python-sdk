import pytest

from remnawave_api.models import (
    GetBandwidthStatsResponseDto,
    GetNodesStatisticsResponseDto,
    GetStatsResponseDto,
)


@pytest.mark.asyncio
async def test_system(remnawave):
    stats = await remnawave.system.get_stats()
    assert isinstance(stats, GetStatsResponseDto)

    bandwidth_stats = await remnawave.system.get_bandwidth_stats()
    assert isinstance(bandwidth_stats, GetBandwidthStatsResponseDto)

    nodes_statistics = await remnawave.system.get_nodes_statistics()
    assert isinstance(nodes_statistics, GetNodesStatisticsResponseDto)
