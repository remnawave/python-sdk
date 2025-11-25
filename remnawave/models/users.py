from datetime import datetime
from typing import Annotated, List, Optional
from uuid import UUID

from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    RootModel,
    StringConstraints,
)
from pydantic.alias_generators import to_camel

from remnawave.enums import TrafficLimitStrategy, UserStatus
from remnawave.utils.happ_crypt import create_happ_crypto_link


class UserActiveInboundsDto(BaseModel):
    uuid: UUID
    tag: str
    type: str
    network: str | None = None
    security: str | None = None


class UserLastConnectedNodeDto(BaseModel):
    connected_at: datetime = Field(alias="connectedAt")
    node_name: str = Field(alias="nodeName")


class ActiveInternalSquadDto(BaseModel):
    uuid: UUID
    name: str


class HappCrypto(BaseModel):
    cryptoLink: str



class CreateUserRequestDto(BaseModel):
    """Request DTO for creating a user"""
    # Required fields
    username: Annotated[
        str, 
        StringConstraints(pattern=r"^[a-zA-Z0-9_-]+$", min_length=3, max_length=36)
    ] = Field(..., description="Unique username for the user")
    expire_at: datetime = Field(..., serialization_alias="expireAt", description="Account expiration date")
    
    # Optional fields with defaults
    status: UserStatus = Field(default=UserStatus.ACTIVE, description="User account status")
    traffic_limit_strategy: TrafficLimitStrategy = Field(
        default=TrafficLimitStrategy.NO_RESET,
        serialization_alias="trafficLimitStrategy",
        description="Traffic reset strategy"
    )
    
    # Optional fields
    short_uuid: Optional[str] = Field(None, serialization_alias="shortUuid")
    trojan_password: Optional[Annotated[str, StringConstraints(min_length=8, max_length=32)]] = Field(
        None, serialization_alias="trojanPassword"
    )
    vless_uuid: Optional[UUID] = Field(None, serialization_alias="vlessUuid")
    ss_password: Optional[Annotated[str, StringConstraints(min_length=8, max_length=32)]] = Field(
        None, serialization_alias="ssPassword"
    )
    traffic_limit_bytes: Optional[int] = Field(
        None, serialization_alias="trafficLimitBytes", ge=0
    )
    created_at: Optional[datetime] = Field(None, serialization_alias="createdAt")
    last_traffic_reset_at: Optional[datetime] = Field(None, serialization_alias="lastTrafficResetAt")
    description: Optional[str] = None
    tag: Optional[Annotated[str, StringConstraints(max_length=16, pattern=r"^[A-Z0-9_]+$")]] = None
    telegram_id: Optional[int] = Field(None, serialization_alias="telegramId")
    email: Optional[EmailStr] = None
    hwid_device_limit: Optional[int] = Field(None, serialization_alias="hwidDeviceLimit", ge=0)
    active_internal_squads: Optional[List[UUID]] = Field(None, serialization_alias="activeInternalSquads")
    uuid: Optional[UUID] = Field(
        None, 
        description="Optional. Pass UUID to create user with specific UUID, otherwise it will be generated automatically."
    )
    external_squad_uuid: Optional[UUID] = Field(None, serialization_alias="externalSquadUuid")


class UpdateUserRequestDto(BaseModel):
    """Request DTO for updating a user"""
    # Either username or uuid must be provided, uuid has priority
    username: Optional[str] = Field(None, description="Username of the user")
    uuid: Optional[UUID] = Field(
        None, 
        description="UUID of the user. UUID has higher priority than username"
    )
    
    # Optional update fields
    status: Optional[UserStatus] = None
    description: Optional[str] = None
    email: Optional[EmailStr] = None
    expire_at: Optional[datetime] = Field(None, serialization_alias="expireAt")
    hwid_device_limit: Optional[int] = Field(None, serialization_alias="hwidDeviceLimit", ge=0)
    tag: Optional[Annotated[str, StringConstraints(max_length=16, pattern=r"^[A-Z0-9_]+$")]] = None
    telegram_id: Optional[int] = Field(None, serialization_alias="telegramId")
    traffic_limit_bytes: Optional[int] = Field(None, serialization_alias="trafficLimitBytes", ge=0)
    traffic_limit_strategy: Optional[TrafficLimitStrategy] = Field(
        None, serialization_alias="trafficLimitStrategy"
    )
    active_internal_squads: Optional[List[UUID]] = Field(
        None, serialization_alias="activeInternalSquads"
    )
    external_squad_uuid: Optional[UUID] = Field(None, serialization_alias="externalSquadUuid")

class UserTrafficDto(BaseModel):
    """User traffic information"""
    used_traffic_bytes: float = Field(alias="usedTrafficBytes")
    lifetime_used_traffic_bytes: float = Field(alias="lifetimeUsedTrafficBytes")
    online_at: Optional[datetime] = Field(None, alias="onlineAt")
    first_connected_at: Optional[datetime] = Field(None, alias="firstConnectedAt")
    last_connected_node_uuid: Optional[UUID] = Field(None, alias="lastConnectedNodeUuid")


class UserResponseDto(BaseModel):
    """User response DTO - обновленная структура с userTraffic"""
    uuid: UUID
    short_uuid: str = Field(alias="shortUuid")
    username: str
    status: UserStatus = Field(default=UserStatus.ACTIVE)
    traffic_limit_bytes: int = Field(0, alias="trafficLimitBytes")
    traffic_limit_strategy: TrafficLimitStrategy = Field(
        TrafficLimitStrategy.NO_RESET, alias="trafficLimitStrategy"
    )
    expire_at: datetime = Field(alias="expireAt")
    telegram_id: Optional[int] = Field(None, alias="telegramId")
    email: Optional[str] = None
    description: Optional[str] = None
    tag: Optional[str] = None
    hwid_device_limit: Optional[int] = Field(None, alias="hwidDeviceLimit")
    external_squad_uuid: Optional[UUID] = Field(None, alias="externalSquadUuid")
    trojan_password: str = Field(alias="trojanPassword")
    vless_uuid: UUID = Field(alias="vlessUuid")
    ss_password: str = Field(alias="ssPassword")
    last_trigger_threshold: int = Field(0, alias="lastTriggeredThreshold")
    sub_revoked_at: Optional[datetime] = Field(None, alias="subRevokedAt")
    sub_last_user_agent: Optional[str] = Field(None, alias="subLastUserAgent")
    sub_last_opened_at: Optional[datetime] = Field(None, alias="subLastOpenedAt")
    last_traffic_reset_at: Optional[datetime] = Field(None, alias="lastTrafficResetAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    subscription_url: str = Field(alias="subscriptionUrl")
    active_internal_squads: list[ActiveInternalSquadDto] = Field(alias="activeInternalSquads")
    user_traffic: UserTrafficDto = Field(alias="userTraffic")
    
    @property
    def used_traffic_bytes(self) -> float:
        """Backward compatibility property"""
        return self.user_traffic.used_traffic_bytes
    
    @property
    def lifetime_used_traffic_bytes(self) -> float:
        """Backward compatibility property"""
        return self.user_traffic.lifetime_used_traffic_bytes
    
    @property
    def online_at(self) -> Optional[datetime]:
        """Backward compatibility property"""
        return self.user_traffic.online_at
    
    @property
    def first_connected(self) -> Optional[datetime]:
        """Backward compatibility property"""
        return self.user_traffic.first_connected_at
    
    @property
    def last_connected_node_uuid(self) -> Optional[UUID]:
        """Backward compatibility property"""
        return self.user_traffic.last_connected_node_uuid
    
    # generate happ link 
    @property
    def happ(self) -> HappCrypto:
        """Generate Happ Crypto Link"""
        crypto_link = create_happ_crypto_link(self.subscription_url)
        return HappCrypto(cryptoLink=crypto_link)

class EmailUserResponseDto(RootModel[list[UserResponseDto]]):
    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]


class TagUserResponseDto(RootModel[list[UserResponseDto]]):
    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]


class TelegramUserResponseDto(RootModel[list[UserResponseDto]]):
    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]


class UsersResponseDto(BaseModel):
    users: list[UserResponseDto]
    total: int


class DeleteUserResponseDto(BaseModel):
    is_deleted: bool = Field(alias="isDeleted")


class TagsResponseDto(BaseModel):
    tags: list[str]


class CreateUserResponseDto(UserResponseDto):
    pass


class UpdateUserResponseDto(UserResponseDto):
    pass


class DisableUserResponseDto(UserResponseDto):
    pass


class EnableUserResponseDto(UserResponseDto):
    pass


class ResetUserTrafficResponseDto(UserResponseDto):
    pass


class RevokeUserSubscriptionResponseDto(UserResponseDto):
    pass


class ActivateAllInboundsResponseDto(UserResponseDto):
    pass


class GetUserByUuidResponseDto(UserResponseDto):
    pass


class GetUserByShortUuidResponseDto(UserResponseDto):
    pass


class GetUserByUsernameResponseDto(UserResponseDto):
    pass


class RevokeUserRequestDto(BaseModel):
    short_uuid: str | None = Field(
        None,
        serialization_alias="shortUuid",
        description="Optional. If not provided, a new short UUID will be generated by Remnawave. Please note that it is strongly recommended to allow Remnawave to generate the short UUID.",
        min_length=6,
        max_length=48,
        pattern=r"^[a-zA-Z0-9_-]+$",
    )


class SubscriptionRequestRecord(BaseModel):
    id: int
    user_uuid: UUID = Field(alias="userUuid")
    request_at: datetime = Field(alias="requestAt")
    request_ip: Optional[str] = Field(alias="requestIp")
    user_agent: Optional[str] = Field(alias="userAgent")


class SubscriptionRequestsResponseData(BaseModel):
    total: int
    records: List[SubscriptionRequestRecord]


class GetSubscriptionRequestsResponseDto(SubscriptionRequestsResponseData):
    pass