from typing import List, Dict, Any
from uuid import UUID

from pydantic import BaseModel, Field, RootModel


class NodeInfoDto(BaseModel):
    uuid: UUID
    name: str
    country_code: str = Field(alias="countryCode")

class GetUserAccessibleNodesResponse(BaseModel):
    user_uuid: UUID = Field(alias="userUuid")
    nodes: List[NodeInfoDto] = Field(default_factory=list)

class GetUserAccessibleNodesResponseDto(GetUserAccessibleNodesResponse):
    pass


class NodeUsageDto(BaseModel):
    date: str
    upload: int
    download: int


class GetNodesUsageByRangeResponseDto(RootModel[List[NodeUsageDto]]):
    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]


class UserUsageDto(BaseModel):
    user_uuid: UUID = Field(alias="userUuid")
    username: str
    upload: int
    download: int


class GetNodeUserUsageByRangeResponseDto(RootModel[List[UserUsageDto]]):
    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]
