from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from remnawave_api.enums import TrafficLimitStrategy, UserStatus


class UserSubscription(BaseModel):
    short_uuid: str = Field(alias="shortUuid")
    username: str
    days_left: int = Field(alias="daysLeft")
    traffic_used: str = Field(alias="trafficUsed")
    traffic_limit: str = Field(alias="trafficLimit")
    traffic_limit_strategy: TrafficLimitStrategy = Field(alias="trafficLimitStrategy")
    expires_at: datetime = Field(alias="expiresAt")
    user_status: UserStatus = Field(alias="userStatus")
    is_active: bool = Field(alias="isActive")


class SubscriptionInfoResponseDto(BaseModel):
    is_found: bool = Field(alias="isFound")
    user: Optional[UserSubscription] = None
    links: list[str]
    ss_conf_links: dict = Field(alias="ssConfLinks")
    subscription_url: str = Field(alias="subscriptionUrl")
