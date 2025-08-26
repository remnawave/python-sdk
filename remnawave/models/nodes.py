from datetime import datetime
from typing import Annotated, List, Optional
from uuid import UUID

from pydantic import BaseModel, Field, StringConstraints, RootModel

from remnawave.models.internal_squads import InboundsDto


class ExcludedInbounds(BaseModel):
    uuid: UUID
    tag: str
    type: str
    network: Optional[str] = None
    security: Optional[str] = None


class RestartEventResponse(BaseModel):
    event_sent: bool = Field(alias="eventSent")


class DeleteResponse(BaseModel):
    is_deleted: bool = Field(alias="isDeleted")


class ReorderNodeItem(BaseModel):
    view_position: int = Field(serialization_alias="viewPosition")
    uuid: UUID


class NodeConfigProfileDto(BaseModel):
    active_config_profile_uuid: UUID = Field(alias="activeConfigProfileUuid")
    active_inbounds: List[InboundsDto] = Field(alias="activeInbounds")


class NodeConfigProfileRequestDto(BaseModel):
    active_config_profile_uuid: UUID = Field(alias="activeConfigProfileUuid")
    active_inbounds: List[UUID] = Field(alias="activeInbounds")


class CreateNodeRequestDto(BaseModel):
    name: Annotated[str, StringConstraints(min_length=3)]
    address: Annotated[str, StringConstraints(min_length=2)]
    port: Optional[int] = Field(None, strict=True, ge=1)
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
    config_profile: NodeConfigProfileRequestDto = Field(
        serialization_alias="configProfile"
    )
    provider_uuid: Optional[UUID] = Field(None, serialization_alias="providerUuid")


class UpdateNodeRequestDto(BaseModel):
    uuid: UUID
    name: Annotated[Optional[str], StringConstraints(min_length=3)] = None
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
    nodes: List[ReorderNodeItem]


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
    config_profile: NodeConfigProfileDto = Field(alias="configProfile")


class NodesResponseDto(RootModel[List[NodeResponseDto]]):
    root: List[NodeResponseDto]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]


class CreateNodeResponseDto(NodeResponseDto):
    pass


class UpdateNodeResponseDto(NodeResponseDto):
    pass


class GetOneNodeResponseDto(NodeResponseDto):
    pass


class GetAllNodesResponseDto(RootModel[List[NodeResponseDto]]):
    root: List[NodeResponseDto]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]


class EnableNodeResponseDto(NodeResponseDto):
    pass


class DisableNodeResponseDto(NodeResponseDto):
    pass


class RestartNodeResponseDto(BaseModel):
    message: str


class RestartAllNodesResponseDto(BaseModel):
    message: str


class ReorderNodeResponseDto(RootModel[List[NodeResponseDto]]):
    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]


class DeleteNodeResponseDto(BaseModel):
    is_deleted: bool = Field(alias="isDeleted")

    def __bool__(self):
        return self.is_deleted


class RestartAllNodesRequestDto(BaseModel):
    force_restart: bool = Field(default=False, alias="forceRestart")
