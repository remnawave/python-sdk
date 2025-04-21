from datetime import datetime
from typing import Annotated, List, Optional
from uuid import UUID

from pydantic import BaseModel, Field, StringConstraints


class ExcludedInbounds(BaseModel):
    uuid: UUID
    tag: str
    type: str


class RestartNodeResponseDto(BaseModel):
    event_sent: bool = Field(alias="eventSent")


class CreateNodeRequestDto(BaseModel):
    name: Annotated[str, StringConstraints(min_length=5)]
    address: Annotated[str, StringConstraints(min_length=2)]
    port: int = Field(strict=True, ge=1)
    is_traffic_tracking_active: Optional[bool] = Field(
        None,
        serialization_alias="isTrafficTrackingActive",
    )
    traffic_limit_bytes: Optional[int] = Field(
        None, serialization_alias="trafficLimitBytes", strict=True, ge=0
    )
    notify_percent: Optional[int] = Field(
        None, serialization_alias="notifyPercent", strict=True, ge=0
    )
    traffic_reset_day: Optional[int] = Field(
        None, serialization_alias="trafficResetDay", strict=True, ge=1
    )
    excluded_inbounds: Optional[List[UUID]] = Field(
        None, serialization_alias="excludedInbounds"
    )
    country_code: Annotated[Optional[str], StringConstraints(max_length=2)] = Field(
        None, serialization_alias="countryCode"
    )
    consumption_multiplier: Optional[float] = Field(
        None, serialization_alias="consumptionMultiplier"
    )


class UpdateNodeRequestDto(BaseModel):
    uuid: UUID
    name: Annotated[Optional[str], StringConstraints(min_length=5)] = None
    address: Annotated[Optional[str], StringConstraints(min_length=2)] = None
    port: Optional[int] = None
    is_traffic_tracking_active: Optional[bool] = Field(
        None, serialization_alias="isTrafficTrackingActive"
    )
    traffic_limit_bytes: Optional[float] = Field(
        None, serialization_alias="trafficLimitBytes"
    )
    notify_percent: Optional[float] = Field(None, serialization_alias="notifyPercent")
    traffic_reset_day: Optional[float] = Field(
        None, serialization_alias="trafficResetDay"
    )
    excluded_inbounds: Optional[List[UUID]] = Field(
        None, serialization_alias="excludedInbounds"
    )
    country_code: Annotated[Optional[str], StringConstraints(max_length=2)] = Field(
        None, serialization_alias="countryCode"
    )
    consumption_multiplier: Optional[float] = Field(
        None, serialization_alias="consumptionMultiplier"
    )


class ReorderNodeRequestDto(BaseModel):
    view_position: int = Field(serialization_alias="viewPosition")
    uuid: UUID


class NodeResponseDto(BaseModel):
    uuid: UUID
    name: str
    address: str
    port: Optional[int] = None
    is_connected: bool = Field(alias="isConnected")
    is_disabled: bool = Field(alias="isDisabled")
    is_connecting: bool = Field(alias="isConnecting")
    is_node_online: bool = Field(alias="isNodeOnline")
    is_xray_running: bool = Field(alias="isXrayRunning")
    last_status_change: Optional[datetime] = Field(None, alias="lastStatusChange")
    last_status_message: Optional[str] = Field(None, alias="lastStatusMessage")
    xray_version: Optional[str] = Field(None, alias="xrayVersion")
    xray_uptime: str = Field(alias="xrayUptime")
    is_traffic_tracking_active: bool = Field(alias="isTrafficTrackingActive")
    traffic_reset_day: Optional[int] = Field(None, alias="trafficResetDay")
    traffic_limit_bytes: Optional[float] = Field(None, alias="trafficLimitBytes")
    traffic_used_bytes: Optional[float] = Field(None, alias="trafficUsedBytes")
    notify_percent: Optional[int] = Field(None, alias="notifyPercent")
    users_online: Optional[int] = Field(None, alias="usersOnline")
    view_position: int = Field(alias="viewPosition")
    country_code: str = Field(alias="countryCode")
    consumption_multiplier: float = Field(alias="consumptionMultiplier")
    cpu_count: Optional[int] = Field(None, alias="cpuCount")
    cpu_model: Optional[str] = Field(None, alias="cpuModel")
    total_ram: Optional[str] = Field(None, alias="totalRam")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    excluded_inbounds: List[ExcludedInbounds] = Field(alias="excludedInbounds")


class NodesResponseDto(BaseModel):
    response: List[NodeResponseDto]


class DeleteNodeResponseDto(BaseModel):
    is_deleted: bool = Field(alias="isDeleted")
