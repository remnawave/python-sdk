from remnawave_api.models import NodesUsageResponseDto
from tests.utils import generate_isoformat_range


async def test_bandwidthstats(remnawave):
    start, end = generate_isoformat_range()
    nodes_usage_by_range = await remnawave.bandwidthstats.get_nodes_usage_by_range(
        start=start, end=end
    )
    assert isinstance(nodes_usage_by_range, NodesUsageResponseDto)
