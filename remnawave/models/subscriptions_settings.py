from datetime import datetime
from typing import Annotated, Dict, List, Optional
from uuid import UUID

from pydantic import BaseModel, Field, StringConstraints

from remnawave.enums import (
    ResponseRuleConditionOperator,
    ResponseRuleOperator,
    ResponseRuleVersion,
    ResponseType,
)


class ResponseRuleCondition(BaseModel):
    """Condition to check against request headers"""
    header_name: Annotated[str, StringConstraints(pattern=r"^[!#$%&'*+\-.0-9A-Z^_`a-z|~]+$")] = Field(
        alias="headerName"
    )
    operator: ResponseRuleConditionOperator
    value: Annotated[str, StringConstraints(min_length=1, max_length=255)]
    case_sensitive: bool = Field(alias="caseSensitive")


class ResponseModificationHeader(BaseModel):
    """Response header modification"""
    key: Annotated[str, StringConstraints(pattern=r"^[!#$%&'*+\-.0-9A-Z^_`a-z|~]+$")]
    value: Annotated[str, StringConstraints(min_length=1)]


class ResponseModifications(BaseModel):
    """Response modifications to apply when rule matches"""
    headers: Optional[List[ResponseModificationHeader]] = None
    subscription_template: Optional[Annotated[str, StringConstraints(min_length=1)]] = Field(
        None, alias="subscriptionTemplate"
    )


class ResponseRule(BaseModel):
    """Individual response rule configuration"""
    name: Annotated[str, StringConstraints(min_length=1, max_length=50)]
    description: Optional[Annotated[str, StringConstraints(min_length=1, max_length=250)]] = None
    enabled: bool
    operator: ResponseRuleOperator
    conditions: List[ResponseRuleCondition]
    response_type: ResponseType = Field(alias="responseType")
    response_modifications: Optional[ResponseModifications] = Field(
        None, alias="responseModifications"
    )


class ResponseRules(BaseModel):
    """Response rules configuration"""
    version: ResponseRuleVersion
    rules: List[ResponseRule]


class CustomRemarksDto(BaseModel):
    """Custom remarks for different user states"""
    expired_users: List[str] = Field(alias="expiredUsers", min_length=1)
    limited_users: List[str] = Field(alias="limitedUsers", min_length=1)
    disabled_users: List[str] = Field(alias="disabledUsers", min_length=1)
    empty_hosts: List[str] = Field(alias="emptyHosts", min_length=1)
    empty_internal_squads: List[str] = Field(alias="emptyInternalSquads", min_length=1)


class HwidSettingsDto(BaseModel):
    """HWID (Hardware ID) settings"""
    enabled: bool
    fallback_device_limit: int = Field(alias="fallbackDeviceLimit")
    max_devices_announce: Optional[Annotated[str, StringConstraints(max_length=200)]] = Field(
        None, alias="maxDevicesAnnounce"
    )

class SubscriptionSettingsResponseDto(BaseModel):
    """Subscription settings response data"""
    uuid: UUID
    profile_title: str = Field(alias="profileTitle")
    support_link: str = Field(alias="supportLink")
    profile_update_interval: int = Field(alias="profileUpdateInterval", ge=1)
    is_profile_webpage_url_enabled: bool = Field(alias="isProfileWebpageUrlEnabled")
    serve_json_at_base_subscription: bool = Field(alias="serveJsonAtBaseSubscription")
    show_custom_remarks: bool = Field(alias="isShowCustomRemarks")
    
    custom_remarks: CustomRemarksDto = Field(alias="customRemarks")
    
    happ_announce: Optional[str] = Field(None, alias="happAnnounce")
    happ_routing: Optional[str] = Field(None, alias="happRouting")
    custom_response_headers: Optional[Dict[str, str]] = Field(None, alias="customResponseHeaders")
    randomize_hosts: bool = Field(alias="randomizeHosts")
    response_rules: Optional[ResponseRules] = Field(None, alias="responseRules")
    
    hwid_settings: Optional[HwidSettingsDto] = Field(None, alias="hwidSettings")
    
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class GetSubscriptionSettingsResponseDto(SubscriptionSettingsResponseDto):
    pass


class UpdateSubscriptionSettingsResponseDto(SubscriptionSettingsResponseDto):
    pass


class UpdateSubscriptionSettingsRequestDto(BaseModel):
    """Update subscription settings request"""
    uuid: UUID
    profile_title: Optional[str] = Field(None, serialization_alias="profileTitle")
    support_link: Optional[str] = Field(None, serialization_alias="supportLink")
    profile_update_interval: Optional[int] = Field(None, serialization_alias="profileUpdateInterval")
    is_profile_webpage_url_enabled: Optional[bool] = Field(
        None, serialization_alias="isProfileWebpageUrlEnabled"
    )
    serve_json_at_base_subscription: Optional[bool] = Field(
        None, serialization_alias="serveJsonAtBaseSubscription"
    )
    is_show_custom_remarks: Optional[bool] = Field(None, serialization_alias="isShowCustomRemarks")
    
    custom_remarks: Optional[CustomRemarksDto] = Field(None, serialization_alias="customRemarks")
    
    happ_announce: Optional[Annotated[str, StringConstraints(max_length=200)]] = Field(
        None, serialization_alias="happAnnounce"
    )
    happ_routing: Optional[str] = Field(None, serialization_alias="happRouting")
    custom_response_headers: Optional[Dict[str, str]] = Field(
        None, serialization_alias="customResponseHeaders"
    )
    randomize_hosts: Optional[bool] = Field(None, serialization_alias="randomizeHosts")
    response_rules: Optional[ResponseRules] = Field(None, serialization_alias="responseRules")
    
    hwid_settings: Optional[HwidSettingsDto] = Field(None, serialization_alias="hwidSettings")


# Backward compatibility aliases
CustomRemarks = CustomRemarksDto
HwidSettings = HwidSettingsDto