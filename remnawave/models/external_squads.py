from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional
from uuid import UUID

from pydantic import BaseModel, Field
from remnawave.models import CustomRemarksDto, HwidSettingsDto


class TemplateType(StrEnum):
    """Template type enum"""
    XRAY_JSON = "XRAY_JSON"
    XRAY_BASE64 = "XRAY_BASE64"
    MIHOMO = "MIHOMO"
    STASH = "STASH"
    CLASH = "CLASH"
    SINGBOX = "SINGBOX"


class ExternalSquadInfoDto(BaseModel):
    """External squad info"""
    members_count: float = Field(alias="membersCount")


class ExternalSquadTemplateDto(BaseModel):
    """External squad template"""
    template_uuid: UUID = Field(alias="templateUuid")
    template_type: TemplateType = Field(alias="templateType")


class ExternalSquadSubscriptionSettingsDto(BaseModel):
    """External squad subscription settings"""
    profile_title: str = Field(alias="profileTitle")
    support_link: str = Field(alias="supportLink")
    profile_update_interval: int = Field(alias="profileUpdateInterval", ge=1)
    is_profile_webpage_url_enabled: bool = Field(alias="isProfileWebpageUrlEnabled")
    serve_json_at_base_subscription: bool = Field(alias="serveJsonAtBaseSubscription")
    is_show_custom_remarks: bool = Field(alias="isShowCustomRemarks")
    happ_announce: Optional[str] = Field(None, alias="happAnnounce")
    happ_routing: Optional[str] = Field(None, alias="happRouting")
    randomize_hosts: bool = Field(alias="randomizeHosts")

class ExternalSquadHostOverridesDto(BaseModel):
    """External squad host overrides"""
    server_description: Optional[str] = Field(None, alias="serverDescription", max_length=30)
    vless_route_id: Optional[int] = Field(None, alias="vlessRouteId", ge=0, le=65535)


class ExternalSquadDto(BaseModel):
    """External squad data model"""
    uuid: UUID
    name: str
    info: ExternalSquadInfoDto
    templates: List[ExternalSquadTemplateDto]
    subscription_settings: Optional[ExternalSquadSubscriptionSettingsDto] = Field(None, alias="subscriptionSettings")
    host_overrides: Optional[ExternalSquadHostOverridesDto] = Field(None, alias="hostOverrides")
    response_headers: Optional[Dict[str, str]] = Field(None, alias="responseHeaders")
    hwid_settings: Optional[HwidSettingsDto] = Field(None, alias="hwidSettings")
    custom_remarks: Optional[CustomRemarksDto] = Field(None, alias="customRemarks")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


# Request/Response models
class GetExternalSquadsResponseDto(BaseModel):
    """Response with all external squads"""
    total: int = Field(alias="total")
    external_squads: List[ExternalSquadDto] = Field(alias="externalSquads")


class GetExternalSquadByUuidResponseDto(ExternalSquadDto):
    """Response with external squad by UUID"""
    pass


class CreateExternalSquadRequestDto(BaseModel):
    """Request to create external squad"""
    name: str = Field(min_length=2, max_length=30, pattern=r"^[A-Za-z0-9_\s-]+$")


class CreateExternalSquadResponseDto(ExternalSquadDto):
    """Response after creating external squad"""
    pass


class UpdateExternalSquadRequestDto(BaseModel):
    """Request to update external squad"""
    uuid: UUID
    name: Optional[str] = Field(None, min_length=2, max_length=30, pattern=r"^[A-Za-z0-9_\s-]+$")
    templates: Optional[List[ExternalSquadTemplateDto]] = None
    subscription_settings: Optional[ExternalSquadSubscriptionSettingsDto] = Field(None, serialization_alias="subscriptionSettings")
    host_overrides: Optional[ExternalSquadHostOverridesDto] = Field(None, serialization_alias="hostOverrides")
    hwid_settings: Optional[HwidSettingsDto] = Field(None, alias="hwidSettings")
    custom_remarks: Optional[CustomRemarksDto] = Field(None, alias="customRemarks")
    response_headers: Optional[Dict[str, str]] = Field(None, serialization_alias="responseHeaders")


class UpdateExternalSquadResponseDto(ExternalSquadDto):
    """Response after updating external squad"""
    pass


class DeleteExternalSquadResponseDto(BaseModel):
    """Response after deleting external squad"""
    is_deleted: bool = Field(alias="isDeleted")


class AddUsersToExternalSquadResponseDto(BaseModel):
    """Response after adding users to external squad"""
    event_sent: bool = Field(alias="eventSent")


class RemoveUsersFromExternalSquadResponseDto(BaseModel):
    """Response after removing users from external squad"""
    event_sent: bool = Field(alias="eventSent")