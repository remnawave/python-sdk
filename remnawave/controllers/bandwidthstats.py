from typing import Annotated

from rapid_api_client import Query

from remnawave.models import GetNodesUsageByRangeResponseDto, GetNodesRealtimeUsageResponseDto
from remnawave.rapid import BaseController, get


class BandWidthStatsController(BaseController):
    @get("/nodes/usage/range", response_class=GetNodesUsageByRangeResponseDto)
    async def get_nodes_usage_by_range(
        self,
        start: Annotated[str, Query(description="Start date in ISO format")],
        end: Annotated[str, Query(description="End date in ISO format")],
    ) -> GetNodesUsageByRangeResponseDto:
        """Get Nodes Usage By Range"""
        ...

    @get("/nodes/usage/realtime", response_class=GetNodesRealtimeUsageResponseDto)
    async def get_nodes_usage_realtime(
        self,
    ) -> GetNodesRealtimeUsageResponseDto:
        """Get Nodes Usage Realtime"""
        ...
        