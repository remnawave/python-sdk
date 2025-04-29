from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field

from remnawave_api.enums import UserStatus
from remnawave_api.enums.users import TrafficLimitStrategy


class BulkUpdateUsersInboundsRequestDto(BaseModel):
    uuids: List[UUID]
    active_user_inbounds: List[UUID] = Field(serialization_alias="activeUserInbounds")


class UpdateUserFields(BaseModel):
    status: Optional[UserStatus] = None
    traffic_limit_bytes: Optional[int] = Field(
        None, serialization_alias="trafficLimitBytes", strict=True, ge=0
    )
    traffic_limit_strategy: Optional[TrafficLimitStrategy] = Field(
        None, serialization_alias="trafficLimitStrategy"
    )
    expire_at: Optional[datetime] = Field(None, serialization_alias="expireAt")
    description: Optional[str] = None
    telegram_id: Optional[int] = Field(None, serialization_alias="telegramId")
    email: Optional[str] = None


class BulkAllUpdateUsersRequestDto(BaseModel):
    status: Optional[str] = None
    traffic_limit_bytes: Optional[int] = Field(
        None, serialization_alias="trafficLimitBytes", strict=True, ge=0
    )
    traffic_limit_strategy: Optional[str] = Field(
        None, serialization_alias="trafficLimitStrategy"
    )
    expire_at: Optional[datetime] = Field(None, serialization_alias="expireAt")
    description: Optional[str] = None
    telegram_id: Optional[int] = Field(None, serialization_alias="telegramId")
    email: Optional[str] = None


class BulkResponseDto(BaseModel):
    affected_rows: int = Field(alias="affectedRows")


class BulkAllResetTrafficUsersResponseDto(BaseModel):
    event_sent: bool = Field(alias="eventSent")


class BulkAllUpdateUsersResponseDto(BaseModel):
    event_sent: bool = Field(alias="eventSent")
