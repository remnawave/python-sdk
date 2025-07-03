from typing import Annotated

from rapid_api_client import Path, Query

from remnawave.models import (
    GetNodeUserUsageByRangeResponseDto,
    GetNodesUsageByRangeResponseDto,
)
from remnawave.rapid import BaseController, get


class NodesUsageHistoryController(BaseController):
    @get("/nodes/usage/range", response_class=GetNodesUsageByRangeResponseDto)
    async def get_nodes_usage_by_range(
        self,
        start: Annotated[str, Query(description="Start date", format="date-time")],
        end: Annotated[str, Query(description="End date", format="date-time")],
    ) -> GetNodesUsageByRangeResponseDto:
        """Get nodes usage by range"""
        ...


class NodesUserUsageHistoryController(BaseController):
    @get("/nodes/usage/{uuid}/users/range", response_class=GetNodeUserUsageByRangeResponseDto)
    async def get_node_user_usage_by_range(
        self,
        uuid: Annotated[str, Path(description="UUID of the node")],
        start: Annotated[str, Query(description="Start date", format="date-time")],
        end: Annotated[str, Query(description="End date", format="date-time")],
    ) -> GetNodeUserUsageByRangeResponseDto:
        """Get nodes user usage by range"""
        ...
