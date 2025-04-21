import pytest

from remnawave_api.models import (
    BandwidthStatisticResponseDto,
    NodesStatisticResponseDto,
    StatisticResponseDto,
)


@pytest.mark.asyncio
async def test_system(remnawave):
    stats = await remnawave.system.get_stats()
    assert isinstance(stats, StatisticResponseDto)

    bandwidth_stats = await remnawave.system.get_bandwidth_stats()
    assert isinstance(bandwidth_stats, BandwidthStatisticResponseDto)

    nodes_statistics = await remnawave.system.get_nodes_statistics()
    assert isinstance(nodes_statistics, NodesStatisticResponseDto)
