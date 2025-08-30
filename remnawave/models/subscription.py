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
    lifetime_traffic_used: str = Field(alias="lifetimeTrafficUsed")
    traffic_used_bytes: str = Field(alias="trafficUsedBytes")
    traffic_limit_bytes: str = Field(alias="trafficLimitBytes")
    lifetime_traffic_used_bytes: int = Field(alias="lifetimeTrafficUsedBytes")
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


class RawHostAdditionalParams(BaseModel):
    mode: Optional[str] = None
    heartbeat_period: Optional[int] = Field(None, alias="heartbeatPeriod")


class RawHostProtocolOptions(BaseModel):
    class SSOptions(BaseModel):
        method: Optional[str] = None
    
    ss: Optional[SSOptions] = None


class RawHostDbData(BaseModel):
    raw_inbound: Optional[Dict[str, Any]] = Field(alias="rawInbound")
    inbound_tag: str = Field(alias="inboundTag")
    uuid: str
    config_profile_uuid: Optional[str] = Field(alias="configProfileUuid")
    config_profile_inbound_uuid: Optional[str] = Field(alias="configProfileInboundUuid")
    is_disabled: bool = Field(alias="isDisabled")
    view_position: int = Field(alias="viewPosition")
    remark: str
    is_hidden: bool = Field(alias="isHidden")
    tag: Optional[str] = None


class RawHost(BaseModel):
    address: Optional[str] = None
    alpn: Optional[str] = None
    fingerprint: Optional[str] = None
    host: Optional[str] = None
    network: Optional[str] = None
    password: Optional[str] = None
    path: Optional[str] = None
    public_key: Optional[str] = Field(None, alias="publicKey")
    port: Optional[int] = None
    protocol: Optional[str] = None
    remark: Optional[str] = None
    short_id: Optional[str] = Field(None, alias="shortId")
    sni: Optional[str] = None
    spider_x: Optional[str] = Field(None, alias="spiderX")
    tls: Optional[str] = None
    header_type: Optional[str] = Field(None, alias="headerType")
    additional_params: Optional[RawHostAdditionalParams] = Field(None, alias="additionalParams")
    x_http_extra_params: Optional[Dict[str, Any]] = Field(None, alias="xHttpExtraParams")
    mux_params: Optional[Dict[str, Any]] = Field(None, alias="muxParams")
    sockopt_params: Optional[Dict[str, Any]] = Field(None, alias="sockoptParams")
    server_description: Optional[str] = Field(None, alias="serverDescription")
    flow: Optional[str] = None
    protocol_options: Optional[RawHostProtocolOptions] = Field(None, alias="protocolOptions")
    db_data: RawHostDbData = Field(alias="dbData")


class RawSubscriptionResponse(BaseModel):
    user: UserSubscription
    subscription_url: str = Field(alias="subscriptionUrl")
    raw_hosts: List[RawHost] = Field(alias="rawHosts")
    headers: Dict[str, str]
    is_hwid_limited: bool = Field(alias="isHwidLimited")


class GetRawSubscriptionByShortUuidResponseDto(RawSubscriptionResponse):
    pass

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

class GetSubscriptionByShortUUIDResponseDto(GetSubscriptionByUsernameResponseDto):
    pass

class GetSubscriptionByUUIDResponseDto(GetSubscriptionByUsernameResponseDto):
    pass

# Legacy alias for backward compatibility
SubscriptionInfoResponseDto = GetSubscriptionInfoResponseDto
