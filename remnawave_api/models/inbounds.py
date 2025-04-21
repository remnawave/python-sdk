from typing import Any, List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class InboundResponseDto(BaseModel):
    uuid: UUID
    tag: str
    type: str
    port: float
    network: Optional[str] = None
    security: Optional[str] = None


class InboundsResponseDto(BaseModel):
    response: List[InboundResponseDto]


class FullInboundStatistic(BaseModel):
    enabled: float
    disabled: float


class FullInboundResponseDto(BaseModel):
    uuid: UUID
    tag: str
    type: str
    port: float
    network: Optional[str] = None
    security: Optional[str] = None
    raw_from_config: Any = Field(alias="rawFromConfig")
    users: FullInboundStatistic
    nodes: FullInboundStatistic


class FullInboundsResponseDto(BaseModel):
    response: List[FullInboundResponseDto]
