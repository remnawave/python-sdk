from remnawave.models import (
    GetBandwidthStatsResponseDto,
    GetNodesStatisticsResponseDto,
    GetStatsResponseDto,
    GetNodesMetricsResponseDto,
    GetRemnawaveHealthResponseDto,
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

    @get("/system/health", response_class=GetRemnawaveHealthResponseDto)
    async def get_health(
        self,
    ) -> GetRemnawaveHealthResponseDto:
        """Get System Health"""
        ...

    @get("/system/nodes/metrics", response_class=GetNodesMetricsResponseDto)
    async def get_nodes_metrics(
        self,
    ) -> GetNodesMetricsResponseDto:
        """Get Nodes Metrics"""
        ...
