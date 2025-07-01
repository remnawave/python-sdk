from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field

class InboundsDto(BaseModel):
    uuid: UUID
    profile_uuid: UUID = Field(alias="profileUuid")
    tag: str
    type: str
    network: Optional[str] = Field(default=None)
    security: Optional[str] = Field(default=None)
    port: Optional[float] = Field(default=None)
    raw_inbound: Optional[dict] = Field(default=None, alias="rawInbound")

class InfoDto(BaseModel):
    members_count: int = Field(alias="membersCount")
    inbounds_count: int = Field(alias="inboundsCount")

class InternalSquadDto(BaseModel):
    uuid: UUID
    name: str
    info: Optional[InfoDto] = Field(default=None)
    inbounds: List[InboundsDto] = Field(default_factory=list)
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class CreateInternalSquadRequestDto(BaseModel):
    name: str
    inbounds: List[UUID] = Field(default_factory=list)


class CreateInternalSquadResponseDto(InternalSquadDto):
    pass


class UpdateInternalSquadRequestDto(BaseModel):
    uuid: UUID
    inbounds: List[UUID] = Field(default_factory=list)


class UpdateInternalSquadResponseDto(InternalSquadDto):
    pass

class GetAllInternalSquadsResponse(BaseModel):
    total: int
    internal_squads: List[InternalSquadDto] = Field(alias="internalSquads")

class GetAllInternalSquadsResponseDto(GetAllInternalSquadsResponse):
    pass


class GetInternalSquadByUuidResponseDto(InternalSquadDto):
    pass


class DeleteInternalSquadResponseDto(BaseModel):
    is_deleted: bool = Field(alias="isDeleted")


class AddUsersToInternalSquadRequestDto(BaseModel):
    user_uuids: List[UUID] = Field(alias="userUuids")

class BulkActionsResponseDto(BaseModel):
    event_sent: bool = Field(alias="eventSent")

class AddUsersToInternalSquadResponseDto(BulkActionsResponseDto):
    pass


class DeleteUsersFromInternalSquadRequestDto(BaseModel):
    user_uuids: List[UUID] = Field(alias="userUuids")


class DeleteUsersFromInternalSquadResponseDto(BulkActionsResponseDto):
    pass
