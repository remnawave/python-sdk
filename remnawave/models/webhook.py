from datetime import datetime
from typing import List, Optional, Literal, Union
from uuid import UUID
from pydantic import BaseModel, Field
from pydantic.alias_generators import to_camel
from remnawave.enums import (
    TUsersStatus, TUserEvents, TUserHwidDevicesEvents, TServiceEvents, TNodeEvents, TErrorsEvents, TCRMEvents, TResetPeriods
)
# ---------------- USER ---------------- #

class LastConnectedNodeDto(BaseModel):
    node_name: str
    country_code: str
    connected_at: datetime

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


class InternalSquadDto(BaseModel):
    uuid: UUID
    name: str
    description: Optional[str] = None

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


class BaseUserDto(BaseModel):
    uuid: UUID
    short_uuid: str
    username: str
    status: TUsersStatus

    used_traffic_bytes: str
    lifetime_used_traffic_bytes: str

    traffic_limit_bytes: str
    traffic_limit_strategy: TResetPeriods
    sub_last_user_agent: Optional[str] = None
    sub_last_opened_at: Optional[datetime] = None

    expire_at: datetime
    sub_revoked_at: Optional[datetime] = None
    last_traffic_reset_at: Optional[datetime] = None

    trojan_password: str
    vless_uuid: UUID
    ss_password: str

    description: Optional[str] = None
    tag: Optional[str] = None
    telegram_id: Optional[str] = None
    email: Optional[str] = None

    hwid_device_limit: Optional[int] = None

    first_connected_at: Optional[datetime] = None
    last_triggered_threshold: int

    online_at: Optional[datetime] = None
    last_connected_node_uuid: Optional[str] = None

    created_at: datetime
    updated_at: datetime

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


class UserDto(BaseUserDto):
    active_internal_squads: List[InternalSquadDto] = Field(default_factory=list)
    last_connected_node: Optional[LastConnectedNodeDto] = None

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


class UserEventDto(BaseModel):
    user: UserDto
    event_name: TUserEvents
    skip_telegram_notification: bool = False

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


# ---------------- HWID DEVICES ---------------- #

class HwidUserDeviceDto(BaseModel):
    hwid: str
    user_uuid: UUID
    platform: Optional[str] = None
    os_version: Optional[str] = None
    device_model: Optional[str] = None
    user_agent: Optional[str] = None

    created_at: datetime
    updated_at: datetime

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


class UserHwidDeviceEventDto(BaseModel):
    data: dict
    event_name: TUserHwidDevicesEvents

    model_config = {"alias_generator": to_camel, "populate_by_name": True}

    @classmethod
    def build(cls, user: UserDto, hwid_device: HwidUserDeviceDto, event: TUserHwidDevicesEvents):
        return cls(data={"user": user, "hwidUserDevice": hwid_device}, event_name=event)


# ---------------- SERVICE EVENTS ---------------- #

class LoginAttemptDto(BaseModel):
    username: str
    ip: str
    user_agent: str
    description: Optional[str] = None
    password: Optional[str] = None

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


class ServiceEventDto(BaseModel):
    event_name: TServiceEvents
    data: dict

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


# ---------------- NODE ENTITIES ---------------- #

class ConfigProfileInboundDto(BaseModel):
    uuid: UUID
    name: str
    config: dict

    created_at: datetime
    updated_at: datetime

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


class InfraProviderDto(BaseModel):
    name: str
    uuid: UUID
    favicon_link: Optional[str] = None
    login_url: Optional[str] = None

    created_at: datetime
    updated_at: datetime

    billing_history: Optional[dict] = None
    billing_nodes: Optional[List[dict]] = None

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


class NodesDto(BaseModel):
    uuid: UUID
    name: str
    address: str
    port: Optional[int] = None
    is_connected: bool
    is_connecting: bool
    is_disabled: bool
    is_node_online: bool
    is_xray_running: bool

    last_status_change: Optional[datetime] = None
    last_status_message: Optional[str] = None

    xray_version: Optional[str] = None
    node_version: Optional[str] = None
    xray_uptime: str

    users_online: Optional[int] = None

    is_traffic_tracking_active: bool
    traffic_reset_day: Optional[int] = None
    traffic_limit_bytes: Optional[str] = None
    traffic_used_bytes: Optional[str] = None
    notify_percent: Optional[int] = None

    view_position: int
    country_code: str
    consumption_multiplier: str

    cpu_count: Optional[int] = None
    cpu_model: Optional[str] = None
    total_ram: Optional[str] = None

    created_at: datetime
    updated_at: datetime

    active_config_profile_uuid: Optional[UUID] = None
    active_inbounds: List[ConfigProfileInboundDto] = Field(default_factory=list)

    provider_uuid: Optional[UUID] = None
    provider: Optional[InfraProviderDto] = None

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


class NodeEventDto(BaseModel):
    node: NodesDto
    event_name: TNodeEvents

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


# ---------------- ERROR EVENTS ---------------- #

class CustomErrorEventDto(BaseModel):
    event_name: TErrorsEvents
    data: dict

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


# ---------------- CRM EVENTS ---------------- #

class CrmEventDto(BaseModel):
    event_name: TCRMEvents
    data: dict
    skip_telegram_notification: bool = False

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


# ---------------- WEBHOOK PAYLOAD ---------------- #

class WebhookPayloadDto(BaseModel):
    event: str
    data: Union[
        UserDto,
        NodesDto,
        HwidUserDeviceDto,
        LoginAttemptDto,
        UserHwidDeviceEventDto,
        dict
    ]
    timestamp: datetime

    model_config = {"alias_generator": to_camel, "populate_by_name": True}

    @classmethod
    def from_dict(cls, payload: dict) -> "WebhookPayloadDto":
        event = payload.get("event", "")
        data_raw = payload.get("data", {})

        if event.startswith("user."):
            data = UserDto(**data_raw)
        elif event.startswith("user_hwid_devices."):
            data = HwidUserDeviceDto(**data_raw)
        elif event.startswith("node."):
            data = NodesDto(**data_raw)
        elif event.startswith("service."):
            # может быть loginAttempt или другое
            if "username" in data_raw and "ip" in data_raw:
                data = LoginAttemptDto(**data_raw)
            else:
                data = data_raw
        elif event.startswith("errors."):
            data = data_raw
        elif event.startswith("crm."):
            data = data_raw
        else:
            data = data_raw

        timestamp_raw = payload.get("timestamp")
        if isinstance(timestamp_raw, (int, float)):
            timestamp = datetime.fromtimestamp(timestamp_raw)
        else:
            timestamp = timestamp_raw

        return cls(event=event, data=data, timestamp=timestamp)