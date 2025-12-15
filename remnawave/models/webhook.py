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

    model_config = {"alias_generator": to_camel, "populate_by_name": True}



class UserTrafficDto(BaseModel):
    """User traffic information for webhooks"""
    used_traffic_bytes: int
    lifetime_used_traffic_bytes: int
    online_at: Optional[datetime] = None
    first_connected_at: Optional[datetime] = None
    last_connected_node_uuid: Optional[UUID] = None

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


class BaseUserDto(BaseModel):
    uuid: UUID
    short_uuid: str
    username: str
    status: TUsersStatus
    user_traffic: UserTrafficDto

    traffic_limit_bytes: int
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
    telegram_id: Optional[int] = None
    email: Optional[str] = None

    hwid_device_limit: Optional[int] = None
    last_triggered_threshold: int

    created_at: datetime
    updated_at: datetime


    model_config = {"alias_generator": to_camel, "populate_by_name": True}

    # Backward compatibility properties
    @property
    def used_traffic_bytes(self) -> int:
        """Backward compatibility property"""
        return self.user_traffic.used_traffic_bytes
    
    @property
    def lifetime_used_traffic_bytes(self) -> int:
        """Backward compatibility property"""
        return self.user_traffic.lifetime_used_traffic_bytes
    
    @property
    def online_at(self) -> Optional[datetime]:
        """Backward compatibility property"""
        return self.user_traffic.online_at
    
    @property
    def first_connected_at(self) -> Optional[datetime]:
        """Backward compatibility property"""
        return self.user_traffic.first_connected_at
    
    @property
    def last_connected_node_uuid(self) -> Optional[UUID]:
        """Backward compatibility property"""
        return self.user_traffic.last_connected_node_uuid



class UserDto(BaseUserDto):
    active_internal_squads: List[InternalSquadDto] = Field(default_factory=list)
    last_connected_node: Optional[LastConnectedNodeDto] = None

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


class UserEventDto(BaseModel):
    event_name: TUserEvents
    user: UserDto

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
    
    @property
    def user(self) -> UserDto:
        return self.data["user"]

    @property
    def hwid_user_device(self) -> HwidUserDeviceDto:
        return self.data["hwidUserDevice"]

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
    profile_uuid: UUID

    tag: str
    type: str
    network: Optional[str]
    security: Optional[str]
    port: Optional[int]

    raw_inbound: Optional[dict]

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


class InfraBillingHistoryDto(BaseModel):
    total_amount: int
    total_bills: int

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


class InfraBillingNodeDto(BaseModel):
    node_uuid: UUID
    name: str
    country_code: str

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


class InfraProviderDto(BaseModel):
    name: str
    uuid: UUID
    favicon_link: Optional[str] = None
    login_url: Optional[str] = None

    created_at: datetime
    updated_at: datetime

    billing_history: Optional[InfraBillingHistoryDto] = None
    billing_nodes: Optional[List[InfraBillingNodeDto]] = None

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


class NodeDto(BaseModel):
    uuid: UUID
    name: str
    address: str
    port: Optional[int] = None
    is_connected: bool
    is_connecting: bool
    is_disabled: bool
    last_status_change: Optional[datetime] = None
    last_status_message: Optional[str] = None

    xray_version: Optional[str] = None
    node_version: Optional[str] = None
    xray_uptime: str

    users_online: Optional[int] = None
    
    is_traffic_tracking_active: bool
    traffic_reset_day: Optional[int] = None
    traffic_limit_bytes: Optional[int] = None
    traffic_used_bytes: Optional[int] = None
    notify_percent: Optional[int] = None

    view_position: int
    country_code: str
    consumption_multiplier: int

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
    event_name: TNodeEvents
    data: NodeDto

    model_config = {"alias_generator": to_camel, "populate_by_name": True}

# ---------------- ERROR EVENTS ---------------- #

# https://github.com/remnawave/backend/blob/main/src/queue/user-jobs/user-jobs.processor.ts#L224
# Not implemented yet!

class ErrorDto(BaseModel):
    description: str

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


class CustomErrorEventDto(BaseModel):
    event_name: TErrorsEvents
    data: ErrorDto

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


# ---------------- CRM EVENTS ---------------- #

class BillingNodeDto(BaseModel):
    provider_name: str
    node_name: str
    next_billing_at: datetime
    login_url: str

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


class CrmEventDto(BaseModel):
    event_name: TCRMEvents
    data: BillingNodeDto

    model_config = {"alias_generator": to_camel, "populate_by_name": True}


# ---------------- WEBHOOK PAYLOAD ---------------- #

class WebhookPayloadDto(BaseModel):
    event: str
    timestamp: datetime
    data: Union[
        UserDto,
        NodeDto,
        HwidUserDeviceDto,
        LoginAttemptDto,
        UserHwidDeviceEventDto,
        BillingNodeDto,
        dict
    ]

    model_config = {"alias_generator": to_camel, "populate_by_name": True}

    @classmethod
    def from_dict(cls, payload: dict) -> "WebhookPayloadDto":
        event = payload.get("event", "")
        data_raw = payload.get("data", {})

        if event.startswith("user."):
            data = UserDto(**data_raw)
        elif event.startswith("user_hwid_devices."):
            user = UserDto(**data_raw["user"])
            hwid_device = HwidUserDeviceDto(**data_raw["hwidUserDevice"])
            data = UserHwidDeviceEventDto.build(
                user=user,
                hwid_device=hwid_device,
                event=event,
            )
        elif event.startswith("node."):
            data = NodeDto(**data_raw)
        elif event.startswith("service."):
            if event.startswith("service.login_attempt"):
                login_attempt_data = data_raw.get("loginAttempt", {})
                data = LoginAttemptDto(**login_attempt_data)
            else: # service.panel_started - содержит пустой json
                data = data_raw
        elif event.startswith("errors."):
            data = ErrorDto(**data_raw)
        elif event.startswith("crm."):
            data = BillingNodeDto(**data_raw)
        else:
            data = data_raw

        timestamp_raw = payload.get("timestamp")
        if isinstance(timestamp_raw, (int, float)):
            timestamp = datetime.fromtimestamp(timestamp_raw)
        else:
            timestamp = timestamp_raw

        return cls(event=event, data=data, timestamp=timestamp)