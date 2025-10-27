from datetime import datetime
from typing import Any, Dict, List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class InboundDto(BaseModel):
    uuid: UUID
    profile_uuid: UUID = Field(alias="profileUuid")
    tag: str
    type: str
    network: Optional[str] = None
    security: Optional[str] = None
    port: Optional[int] = None
    raw_inbound: Optional[Any] = Field(None, alias="rawInbound")

class NodesProfileDto(BaseModel):
    uuid: UUID
    name: str
    country_code: str = Field(alias="countryCode")

class ConfigProfileDto(BaseModel):
    uuid: UUID
    name: str
    config: Dict[str, Any]
    inbounds: List[InboundDto]
    nodes: List[NodesProfileDto] = []
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class CreateConfigProfileRequestDto(BaseModel):
    name: str
    config: Dict[str, Any]


class CreateConfigProfileResponseDto(ConfigProfileDto):
    pass


class UpdateConfigProfileRequestDto(BaseModel):
    uuid: UUID
    name: Optional[str] = Field(None, pattern=r"^[A-Za-z0-9_-]+$")
    config: Optional[Dict[str, Any]] = None


class UpdateConfigProfileResponseDto(ConfigProfileDto):
    pass


class GetAllConfigProfilesResponsePaginated(BaseModel):
    total: int
    config_profiles: List[ConfigProfileDto] = Field(alias="configProfiles")


class GetAllConfigProfilesResponseDto(GetAllConfigProfilesResponsePaginated):
    pass


class GetConfigProfileByUuidResponseDto(ConfigProfileDto):
    pass


class DeleteConfigProfileResponseDto(BaseModel):
    is_deleted: bool = Field(alias="isDeleted")


class GetAllInboundsResponseDto(List[InboundDto]):
    pass


class GetInboundsByProfileUuidResponseDto(List[InboundDto]):
    pass
