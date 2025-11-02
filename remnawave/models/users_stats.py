import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, Field
from pydantic.alias_generators import to_camel


class UserUsageByRange(BaseModel):
    user_uuid: UUID = Field(alias="userUuid")
    node_uuid: UUID = Field(alias="nodeUuid")
    node_name: str = Field(alias="nodeName")
    total: int
    date: datetime.date
    
    model_config = {"alias_generator": to_camel, "populate_by_name": True}


class UserUsageByRangeResponseDto(List[UserUsageByRange]):
    pass
