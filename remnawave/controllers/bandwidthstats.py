from typing import Annotated

from rapid_api_client import Path, Query

from remnawave.models.bandwidthstats import (
    GetLegacyStatsNodesUsersUsageResponseDto,
    GetLegacyStatsUserUsageResponseDto,
    GetNodeUserUsageByRangeResponseDto,
    GetNodesRealtimeUsageResponseDto,
    GetNodesUsageByRangeResponseDto,
    GetStatsNodesRealtimeUsageResponseDto,
    GetStatsNodesUsageResponseDto,
    GetStatsNodeUsersUsageResponseDto,
    GetStatsUserUsageResponseDto,
    GetUserUsageByRangeResponseDto,
)
from remnawave.rapid import BaseController, get


class BandWidthStatsController(BaseController):
    # ============ Legacy Endpoints (Deprecated) ============

    @get("/bandwidth-stats/users/{user_uuid}/legacy-old", response_class=GetUserUsageByRangeResponseDto)
    async def get_user_usage_legacy_old(
        self,
        user_uuid: Annotated[str, Path(description="UUID of the user", alias="userUuid")],
        start: Annotated[str, Query(description="Start date")],
        end: Annotated[str, Query(description="End date")],
    ) -> GetUserUsageByRangeResponseDto:
        """Get User Usage by Range (Legacy - Deprecated)"""
        ...

    @get("/bandwidth-stats/nodes/{node_uuid}/users/legacy-old", response_class=GetNodeUserUsageByRangeResponseDto)
    async def get_node_user_usage_legacy_old(
        self,
        node_uuid: Annotated[str, Path(description="UUID of the node", alias="nodeUuid")],
        start: Annotated[str, Query(description="Start date")],
        end: Annotated[str, Query(description="End date")],
    ) -> GetNodeUserUsageByRangeResponseDto:
        """Get Node User Usage by Range and Node UUID (Legacy - Deprecated)"""
        ...

    # ============ New Stats Endpoints ============
    
    @get("/bandwidth-stats/nodes/realtime", response_class=GetStatsNodesRealtimeUsageResponseDto)
    async def get_nodes_realtime_usage(
        self,
    ) -> GetStatsNodesRealtimeUsageResponseDto:
        """Get Nodes Realtime Usage"""
        ...

    @get("/bandwidth-stats/nodes/{uuid}/users/legacy", response_class=GetLegacyStatsNodesUsersUsageResponseDto)
    async def get_node_users_usage_legacy_stats(
        self,
        uuid: Annotated[str, Path(description="UUID of the node")],
        start: Annotated[str, Query(description="Start date")],
        end: Annotated[str, Query(description="End date")],
    ) -> GetLegacyStatsNodesUsersUsageResponseDto:
        """Get Node Users Usage by Range and Node UUID (Legacy Stats)"""
        ...

    @get("/bandwidth-stats/nodes/{uuid}/users", response_class=GetStatsNodeUsersUsageResponseDto)
    async def get_stats_node_users_usage(
        self,
        uuid: Annotated[str, Path(description="UUID of the node")],
        top_users_limit: Annotated[int, Query(description="Limit of top users to return", alias="topUsersLimit")],
        start: Annotated[str, Query(description="Start date")],
        end: Annotated[str, Query(description="End date")],
    ) -> GetStatsNodeUsersUsageResponseDto:
        """Get Node Users Usage by Node UUID"""
        ...

    @get("/bandwidth-stats/users/{uuid}", response_class=GetStatsUserUsageResponseDto)
    async def get_stats_user_usage(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
        top_nodes_limit: Annotated[int, Query(description="Limit of top nodes to return", alias="topNodesLimit")],
        start: Annotated[str, Query(description="Start date")],
        end: Annotated[str, Query(description="End date")],
    ) -> GetStatsUserUsageResponseDto:
        """Get User Usage by Range"""
        ...

    @get("/bandwidth-stats/nodes", response_class=GetStatsNodesUsageResponseDto)
    async def get_stats_nodes_usage(
        self,
        top_nodes_limit: Annotated[int, Query(description="Limit of top nodes to return", alias="topNodesLimit")],
        start: Annotated[str, Query(description="Start date")],
        end: Annotated[str, Query(description="End date")],
    ) -> GetStatsNodesUsageResponseDto:
        """Get Nodes Usage by Range"""
        ...

    @get("/bandwidth-stats/users/{uuid}/legacy", response_class=GetLegacyStatsUserUsageResponseDto)
    async def get_user_usage_legacy_stats(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
        start: Annotated[str, Query(description="Start date")],
        end: Annotated[str, Query(description="End date")],
    ) -> GetLegacyStatsUserUsageResponseDto:
        """Get User Usage by Range (Legacy Stats)"""
        ...