from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from remnawave.enums import TrafficLimitStrategy, UserStatus


class HappCrypto(BaseModel):
    crypto_link: str = Field(alias="cryptoLink")


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


class SubscriptionInfoData(BaseModel):
    is_found: bool = Field(alias="isFound")
    user: UserSubscription
    links: List[str]
    ss_conf_links: Dict[str, str] = Field(alias="ssConfLinks")
    subscription_url: str = Field(alias="subscriptionUrl")
    happ: HappCrypto


class GetSubscriptionInfoResponseDto(BaseModel):
    is_found: bool = Field(alias="isFound")
    user: UserSubscription
    links: List[str]
    ss_conf_links: Dict[str, str] = Field(alias="ssConfLinks")
    subscription_url: str = Field(alias="subscriptionUrl")
    happ: HappCrypto


class SubscriptionWithoutHapp(BaseModel):
    is_found: bool = Field(alias="isFound")
    user: UserSubscription
    links: List[str]
    ss_conf_links: Dict[str, str] = Field(alias="ssConfLinks")
    subscription_url: str = Field(alias="subscriptionUrl")


class GetAllSubscriptionsResponseDto(BaseModel):
    subscriptions: List[SubscriptionWithoutHapp]
    total: float


class GetSubscriptionByUsernameResponseDto(BaseModel):
    is_found: bool = Field(alias="isFound")
    user: UserSubscription
    links: List[str]
    ss_conf_links: Dict[str, str] = Field(alias="ssConfLinks")
    subscription_url: str = Field(alias="subscriptionUrl")


# Legacy alias for backward compatibility
SubscriptionInfoResponseDto = GetSubscriptionInfoResponseDto
