import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, Field


class NodeUsageResponseDto(BaseModel):
    node_uuid: UUID = Field(alias="nodeUuid")
    node_name: str = Field(alias="nodeName")
    total: float
    total_download: float = Field(alias="totalDownload")
    total_upload: float = Field(alias="totalUpload")
    human_readable_total: str = Field(alias="humanReadableTotal")
    human_readable_total_download: str = Field(alias="humanReadableTotalDownload")
    human_readable_total_upload: str = Field(alias="humanReadableTotalUpload")
    date: datetime.date


class NodesUsageResponseDto(BaseModel):
    response: List[NodeUsageResponseDto]
