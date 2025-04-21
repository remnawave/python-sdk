import datetime
from typing import List

from pydantic import BaseModel, Field


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
    active: int = Field(alias="ACTIVE")
    disabled: int = Field(alias="DISABLED")
    limited: int = Field(alias="LIMITED")
    expired: int = Field(alias="EXPIRED")


class UsersStatistic(BaseModel):
    status_counts: StatusCounts = Field(alias="statusCounts")
    total_users: int = Field(alias="totalUsers")
    total_traffic_bytes: int = Field(alias="totalTrafficBytes")


class OnlineStatistic(BaseModel):
    last_day: int = Field(alias="lastDay")
    last_week: int = Field(alias="lastWeek")
    never_online: int = Field(alias="neverOnline")
    online_now: int = Field(alias="onlineNow")


class StatisticResponseDto(BaseModel):
    cpu: CPUStatistic
    memory: MemoryStatistic
    uptime: float
    timestamp: int
    users: UsersStatistic
    online_stats: OnlineStatistic = Field(alias="onlineStats")
