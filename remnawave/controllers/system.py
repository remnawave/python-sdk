from remnawave.models import (
    GetBandwidthStatsResponseDto,
    GetNodesStatisticsResponseDto,
    GetStatsResponseDto,
)
from remnawave.rapid import BaseController, get


class SystemController(BaseController):
    @get("/system/stats", response_class=GetStatsResponseDto)
    async def get_stats(
        self,
    ) -> GetStatsResponseDto:
        """Get System Stats"""
        ...

    @get("/system/stats/bandwidth", response_class=GetBandwidthStatsResponseDto)
    async def get_bandwidth_stats(
        self,
    ) -> GetBandwidthStatsResponseDto:
        """Get System Bandwidth Statistics"""
        ...

    @get("/system/stats/nodes", response_class=GetNodesStatisticsResponseDto)
    async def get_nodes_statistics(
        self,
    ) -> GetNodesStatisticsResponseDto:
        """Get Nodes Statistics"""
        ...
