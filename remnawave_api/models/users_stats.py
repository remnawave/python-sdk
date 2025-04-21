import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, Field


class UserUsageByRange(BaseModel):
    user_uuid: UUID = Field(alias="userUuid")
    node_uuid: UUID = Field(alias="nodeUuid")
    node_name: str = Field(alias="nodeName")
    total: int
    date: datetime.date


class UserUsageByRangeResponseDto(BaseModel):
    response: List[UserUsageByRange]
