import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, Field

from remnawave.enums import ResponseType
from remnawave.models.subscriptions_settings import ResponseRule, ResponseRules


class NodeStatistic(BaseModel):
    node_name: str = Field(alias="nodeName")
    date: datetime.date
    total_bytes: int = Field(alias="totalBytes")


class NodesStatisticResponseDto(BaseModel):
    last_seven_days: List[NodeStatistic] = Field(alias="lastSevenDays")


class BandwidthStatistic(BaseModel):
    current: str
    previous: str
    difference: str


class BandwidthStatisticResponseDto(BaseModel):
    last_two_days: BandwidthStatistic = Field(alias="bandwidthLastTwoDays")
    last_seven_days: BandwidthStatistic = Field(alias="bandwidthLastSevenDays")
    last_30_days: BandwidthStatistic = Field(alias="bandwidthLast30Days")
    calendar_month: BandwidthStatistic = Field(alias="bandwidthCalendarMonth")
    current_year: BandwidthStatistic = Field(alias="bandwidthCurrentYear")


class CPUStatistic(BaseModel):
    cores: int
    physical_cores: int = Field(alias="physicalCores")


class MemoryStatistic(BaseModel):
    total: int
    free: int
    used: int
    active: int
    available: int


class StatusCounts(BaseModel):
    """Dynamic status counts - использует additionalProperties"""
    model_config = {"extra": "allow"}
    
    def __getitem__(self, key: str) -> int:
        """Allow dict-like access"""
        return getattr(self, key, 0)
    
    def get(self, key: str, default: int = 0) -> int:
        """Dict-like get method"""
        return getattr(self, key, default)


class UsersStatistic(BaseModel):
    status_counts: StatusCounts = Field(alias="statusCounts")
    total_users: int = Field(alias="totalUsers")


class OnlineStatistic(BaseModel):
    last_day: int = Field(alias="lastDay")
    last_week: int = Field(alias="lastWeek")
    never_online: int = Field(alias="neverOnline")
    online_now: int = Field(alias="onlineNow")


class NodesStatistic(BaseModel):
    total_online: int = Field(alias="totalOnline")
    total_bytes_lifetime: str = Field(alias="totalBytesLifetime")


class StatisticResponseDto(BaseModel):
    """System statistics data"""
    cpu: CPUStatistic
    memory: MemoryStatistic
    uptime: float
    timestamp: int
    users: UsersStatistic
    online_stats: OnlineStatistic = Field(alias="onlineStats")
    nodes: NodesStatistic


class PM2Stat(BaseModel):
    name: str
    memory: str
    cpu: str


class RemnawaveHealthData(BaseModel):
    pm2_stats: List[PM2Stat] = Field(alias="pm2Stats")


class GetStatsResponseDto(StatisticResponseDto):
    """Get system statistics response"""
    pass


class GetBandwidthStatsResponseDto(BaseModel):
    last_two_days: BandwidthStatistic = Field(alias="bandwidthLastTwoDays")
    last_seven_days: BandwidthStatistic = Field(alias="bandwidthLastSevenDays")
    last_30_days: BandwidthStatistic = Field(alias="bandwidthLast30Days")
    calendar_month: BandwidthStatistic = Field(alias="bandwidthCalendarMonth")
    current_year: BandwidthStatistic = Field(alias="bandwidthCurrentYear")


class GetNodesStatisticsResponseDto(BaseModel):
    last_seven_days: List[NodeStatistic] = Field(alias="lastSevenDays")


class GetRemnawaveHealthResponseDto(BaseModel):
    pm2_stats: List[PM2Stat] = Field(alias="pm2Stats")


class NodeMetric(BaseModel):
    """Node metric data"""
    uuid: str = Field(alias="nodeUuid")
    name: Optional[str] = None
    address: Optional[str] = None
    is_online: Optional[bool] = Field(None, alias="isOnline")
    cpu_usage: Optional[float] = Field(None, alias="cpuUsage")
    memory_usage: Optional[float] = Field(None, alias="memoryUsage")
    network_upload: Optional[int] = Field(None, alias="networkUpload")
    network_download: Optional[int] = Field(None, alias="networkDownload")
    uptime: Optional[int] = None
    last_seen: Optional[datetime.datetime] = Field(None, alias="lastSeen")
    connected_users: Optional[int] = Field(None, alias="connectedUsers")
    upload: Optional[str] = None
    download: Optional[str] = None


class GetNodesMetricsResponseDto(BaseModel):
    nodes: List[NodeMetric]


class X25519KeyPair(BaseModel):
    public_key: str = Field(alias="publicKey")
    private_key: str = Field(alias="privateKey")


class GetX25519KeyPairResponseDto(BaseModel):
    key_pairs: List[X25519KeyPair] = Field(alias="keyPairs")


class EncryptHappCryptoLinkRequestDto(BaseModel):
    link_to_encrypt: str = Field(serialization_alias="linkToEncrypt")


class EncryptHappCryptoLinkData(BaseModel):
    encrypted_link: str = Field(alias="encryptedLink")


class EncryptHappCryptoLinkResponseDto(EncryptHappCryptoLinkData):
    pass


class DebugSrrMatcherRequestDto(BaseModel):
    response_rules: ResponseRules = Field(serialization_alias="responseRules")


class DebugSrrMatcherData(BaseModel):
    matched: bool
    response_type: ResponseType = Field(alias="responseType")
    matched_rule: Optional[ResponseRule] = Field(alias="matchedRule")
    input_headers: Dict[str, str] = Field(alias="inputHeaders")
    output_headers: Dict[str, str] = Field(alias="outputHeaders")


class DebugSrrMatcherResponseDto(DebugSrrMatcherData):
    pass