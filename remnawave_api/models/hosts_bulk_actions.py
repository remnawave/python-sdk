from typing import List
from uuid import UUID

from pydantic import BaseModel, Field

from remnawave_api.models import HostResponseDto


class SetInboundToManyHostsRequestDto(BaseModel):
    uuids: List[UUID]
    inbound_uuid: UUID = Field(serialization_alias="inboundUuid")


class BulkDeleteHostsResponseDto(BaseModel):
    response: List[HostResponseDto]


class BulkDisableHostsResponseDto(BaseModel):
    response: List[HostResponseDto]


class BulkEnableHostsResponseDto(BaseModel):
    response: List[HostResponseDto]


class SetInboundToManyHostsResponseDto(BaseModel):
    response: List[HostResponseDto]


class SetPortToManyHostsResponseDto(BaseModel):
    response: List[HostResponseDto]
