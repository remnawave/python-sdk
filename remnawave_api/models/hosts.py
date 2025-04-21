from typing import Annotated, List, Optional
from uuid import UUID

from pydantic import BaseModel, Field, StringConstraints

from remnawave_api.enums import ALPN, Fingerprint, SecurityLayer


class ReorderHostRequestDto(BaseModel):
    view_position: int = Field(serialization_alias="viewPosition")
    uuid: UUID


class UpdateHostRequestDto(BaseModel):
    uuid: UUID
    inbound_uuid: Optional[UUID] = Field(None, serialization_alias="inboundUuid")
    remark: Annotated[Optional[str], StringConstraints(max_length=40)] = None
    address: Optional[str] = None
    port: Optional[int] = None
    path: Optional[str] = None
    sni: Optional[str] = None
    host: Optional[str] = None
    alpn: Optional[ALPN] = None
    fingerprint: Optional[Fingerprint] = None
    allow_insecure: Optional[bool] = Field(None, serialization_alias="allowInsecure")
    is_disabled: Optional[bool] = Field(None, serialization_alias="isDisabled")
    security_layer: Optional[SecurityLayer] = Field(
        None, serialization_alias="securityLayer"
    )


class HostResponseDto(BaseModel):
    uuid: UUID
    inbound_uuid: UUID = Field(alias="inboundUuid")
    view_position: int = Field(alias="viewPosition")
    remark: str
    address: str
    port: int
    path: Optional[str] = None
    sni: Optional[str] = None
    host: Optional[str] = None
    alpn: Optional[ALPN] = None
    fingerprint: Optional[Fingerprint] = None
    allow_insecure: Optional[bool] = Field(
        None,
        alias="allowInsecure",
    )
    is_disabled: Optional[bool] = Field(
        None,
        alias="isDisabled",
    )
    security_layer: Optional[SecurityLayer] = Field(
        None,
        alias="securityLayer",
    )


class HostsResponseDto(BaseModel):
    response: List[HostResponseDto]


class ReorderHostResponseDto(BaseModel):
    is_updated: bool = Field(alias="isUpdated")


class CreateHostRequestDto(BaseModel):
    inbound_uuid: UUID = Field(serialization_alias="inboundUuid")
    remark: Annotated[str, StringConstraints(max_length=40)]
    address: str
    port: int
    path: Optional[str] = None
    sni: Optional[str] = None
    host: Optional[str] = None
    alpn: Optional[ALPN] = None
    fingerprint: Optional[Fingerprint] = None
    allow_insecure: Optional[bool] = Field(
        None,
        serialization_alias="allowInsecure",
    )
    is_disabled: Optional[bool] = Field(
        None,
        serialization_alias="isDisabled",
    )
    security_layer: Optional[SecurityLayer] = Field(
        None,
        serialization_alias="securityLayer",
    )


class DeleteHostResponseDto(BaseModel):
    is_deleted: bool = Field(alias="isDeleted")
