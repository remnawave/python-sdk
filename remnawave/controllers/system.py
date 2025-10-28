from typing import Annotated
from rapid_api_client import PydanticBody
from remnawave.models import (
    GetBandwidthStatsResponseDto,
    GetNodesStatisticsResponseDto,
    GetStatsResponseDto,
    GetNodesMetricsResponseDto,
    GetRemnawaveHealthResponseDto,
    GetX25519KeyPairResponseDto,
    EncryptHappCryptoLinkRequestDto,
    EncryptHappCryptoLinkResponseDto,
    DebugSrrMatcherRequestDto,
    DebugSrrMatcherResponseDto,
)
from remnawave.rapid import BaseController, get, post


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

    @get("/system/tools/x25519/generate", response_class=GetX25519KeyPairResponseDto)
    async def get_x25519_key_pair(
        self,
    ) -> GetX25519KeyPairResponseDto:
        """Get X25519 Key Pair"""
        ...
        
    @post("/system/tools/happ/encrypt", response_class=EncryptHappCryptoLinkResponseDto)
    async def encrypt_happ_crypto_link(
        self,
        body: Annotated[EncryptHappCryptoLinkRequestDto, PydanticBody()],
    ) -> EncryptHappCryptoLinkResponseDto:
        """Encrypt Happ Crypto Link"""
        ...

    @post("/system/testers/srr-matcher", response_class=DebugSrrMatcherResponseDto)
    async def debug_srr_matcher(
        self,
        body: Annotated[DebugSrrMatcherRequestDto, PydanticBody()],
    ) -> DebugSrrMatcherResponseDto:
        """Test SRR Matcher"""
        ...