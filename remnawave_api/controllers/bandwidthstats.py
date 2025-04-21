from typing import Annotated

from rapid_api_client import Query

from remnawave_api.models import NodesUsageResponseDto
from remnawave_api.rapid import BaseController, get


class BandWidthStatsController(BaseController):
    @get("/nodes/usage/range", response_class=NodesUsageResponseDto)
    async def get_nodes_usage_by_range(
        self,
        start: Annotated[str, Query(description="Start date in ISO format")],
        end: Annotated[str, Query(description="End date in ISO format")],
    ) -> NodesUsageResponseDto:
        """Get Nodes Usage By Range"""
        ...
