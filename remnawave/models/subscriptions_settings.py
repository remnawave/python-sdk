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


class SubscriptionSettingsResponseDto(BaseModel):
    uuid: UUID
    profile_title: str = Field(alias="profileTitle")
    support_link: str = Field(alias="supportLink")
    profile_update_interval: int = Field(
        alias="profileUpdateInterval", strict=True, ge=1
    )
    is_profile_webpage_url_enabled: bool = Field(alias="isProfileWebpageUrlEnabled")
    serve_json_at_base_subscription: bool = Field(alias="serveJsonAtBaseSubscription")
    add_username_to_base_subscription: bool = Field(
        alias="addUsernameToBaseSubscription"
    )
    show_custom_remarks: bool = Field(alias="isShowCustomRemarks")
    happ_announce: Optional[str] = Field(None, alias="happAnnounce")
    happ_routing: Optional[str] = Field(None, alias="happRouting")
    expired_users_remarks: List[str] = Field(alias="expiredUsersRemarks")
    limited_users_remarks: List[str] = Field(alias="limitedUsersRemarks")
    disabled_users_remarks: List[str] = Field(alias="disabledUsersRemarks")
    custom_response_headers: Optional[Dict[str, str]] = Field(
        None, alias="customResponseHeaders"
    )
    randomize_hosts: bool = Field(alias="randomizeHosts")
    response_rules: Optional[ResponseRules] = Field(None, alias="responseRules")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class GetSubscriptionSettingsResponseDto(SubscriptionSettingsResponseDto):
    pass


class UpdateSubscriptionSettingsResponseDto(SubscriptionSettingsResponseDto):
    pass


class UpdateSubscriptionSettingsRequestDto(BaseModel):
    uuid: UUID
    profile_title: Optional[str] = Field(None, alias="profileTitle")
    support_link: Optional[str] = Field(None, alias="supportLink")
    profile_update_interval: Optional[int] = Field(
        None, alias="profileUpdateInterval"
    )
    is_profile_webpage_url_enabled: Optional[bool] = Field(
        None, alias="isProfileWebpageUrlEnabled"
    )
    serve_json_at_base_subscription: Optional[bool] = Field(
        None, alias="serveJsonAtBaseSubscription"
    )
    add_username_to_base_subscription: Optional[bool] = Field(
        None, alias="addUsernameToBaseSubscription"
    )
    is_show_custom_remarks: Optional[bool] = Field(
        None, alias="isShowCustomRemarks"
    )
    happ_announce: Annotated[Optional[str], StringConstraints(max_length=200)] = Field(
        None, alias="happAnnounce"
    )
    happ_routing: Optional[str] = Field(None, alias="happRouting")
    expired_users_remarks: Optional[List[str]] = Field(
        None, alias="expiredUsersRemarks"
    )
    limited_users_remarks: Optional[List[str]] = Field(
        None, alias="limitedUsersRemarks"
    )
    disabled_users_remarks: Optional[List[str]] = Field(
        None, alias="disabledUsersRemarks"
    )
    custom_response_headers: Optional[Dict[str, str]] = Field(
        None, alias="customResponseHeaders"
    )
    randomize_hosts: Optional[bool] = Field(None, alias="randomizeHosts")
    response_rules: Optional[ResponseRules] = Field(None, alias="responseRules")