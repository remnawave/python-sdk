from typing import List
from uuid import UUID

from pydantic import BaseModel, Field

from remnawave.models import HostResponseDto


class SetInboundToManyHostsRequestDto(BaseModel):
    uuids: List[UUID]
    config_profile_uuid: UUID = Field(serialization_alias="configProfileUuid")
    config_profile_inbound_uuid: UUID = Field(
        serialization_alias="configProfileInboundUuid"
    )

class SetPortToManyHostsRequestDto(BaseModel):
    uuids: List[UUID]
    port: int = Field(ge=1, le=65535)

class BulkDeleteHostsResponseDto(List[HostResponseDto]):
    pass


class BulkDisableHostsResponseDto(List[HostResponseDto]):
    pass


class BulkEnableHostsResponseDto(List[HostResponseDto]):
    pass


class SetInboundToManyHostsResponseDto(List[HostResponseDto]):
    pass

class SetPortToManyHostsResponseDto(List[HostResponseDto]):
    pass
