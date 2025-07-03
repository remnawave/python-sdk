from typing import List
from uuid import UUID

from pydantic import BaseModel, Field

from remnawave.models import HostResponseDto


class SetInboundToManyHostsRequestDto(BaseModel):
    uuids: List[UUID]
    inbound_uuid: UUID = Field(serialization_alias="inboundUuid")


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
