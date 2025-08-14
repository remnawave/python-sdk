from typing import Annotated, List, Optional
from uuid import UUID

from pydantic import BaseModel, Field, StringConstraints, RootModel

from remnawave.enums import ALPN, Fingerprint, SecurityLayer


class ReorderResponse(BaseModel):
    is_updated: bool = Field(alias="isUpdated")


class DeleteResponse(BaseModel):
    is_deleted: bool = Field(alias="isDeleted")


class ReorderHostItem(BaseModel):
    view_position: int = Field(serialization_alias="viewPosition")
    uuid: UUID


class ReorderHostRequestDto(BaseModel):
    hosts: List[ReorderHostItem]


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
    server_description: Optional[str] = Field(
        None, alias="serverDescription", max_length=30
    )
    muxParams: Optional[str] = Field(
        None,
        serialization_alias="muxParams",
    )
    sockopt_params: Optional[str] = Field(
        None,
        serialization_alias="sockoptParams",
    )
    tag: Optional[Annotated[str, StringConstraints(max_length=32)]] = Field(
        None, serialization_alias="tag"
    )
    is_hidden: Optional[bool] = Field(
        None,
        serialization_alias="isHidden",
    )
    override_sni_from_address: Optional[bool] = Field(
        None,
        serialization_alias="overrideSniFromAddress",
    )


class HostInboundData(BaseModel):
    config_profile_uuid: UUID = Field(alias="configProfileUuid")
    config_profile_inbound_uuid: UUID = Field(alias="configProfileInboundUuid")


class HostResponseDto(BaseModel):
    uuid: UUID
    view_position: int = Field(alias="viewPosition")
    remark: str
    address: str
    port: int
    path: Optional[str] = None
    sni: Optional[str] = None
    host: Optional[str] = None
    alpn: Optional[ALPN] = None
    fingerprint: Optional[Fingerprint] = None
    is_disabled: Optional[bool] = Field(
        None,
        alias="isDisabled",
    )
    security_layer: Optional[SecurityLayer] = Field(
        None,
        alias="securityLayer",
    )
    x_http_extra_params: Optional[str] = Field(
        None,
        alias="xHttpExtraParams",
    )
    server_description: Optional[str] = Field(
        None, alias="serverDescription", max_length=30
    )
    inbound: HostInboundData
    muxParams: Optional[str] = Field(
        None,
        serialization_alias="muxParams",
    )
    sockopt_params: Optional[str] = Field(
        None,
        serialization_alias="sockoptParams",
    )
    tag: Optional[Annotated[str, StringConstraints(max_length=32)]] = Field(
        None, serialization_alias="tag"
    )
    is_hidden: Optional[bool] = Field(
        None,
        serialization_alias="isHidden",
    )
    override_sni_from_address: Optional[bool] = Field(
        None,
        serialization_alias="overrideSniFromAddress",
    )

    # Legacy compatibility property
    @property
    def inbound_uuid(self) -> UUID:
        return self.inbound.config_profile_inbound_uuid


class HostsResponseDto(List[HostResponseDto]):
    pass


class CreateHostResponseDto(HostResponseDto):
    pass


class UpdateHostResponseDto(HostResponseDto):
    pass


class GetAllHostTagsResponseDto(BaseModel):
    tags: list[str] = None


class GetAllHostsResponseDto(RootModel[List[HostResponseDto]]):
    root: List[HostResponseDto]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]


class GetOneHostResponseDto(HostResponseDto):
    pass


class ReorderHostResponseDto(BaseModel):
    is_updated: bool = Field(alias="isUpdated", default=True)


class DeleteHostResponseDto(BaseModel):
    is_deleted: bool = Field(alias="isDeleted")


class CreateHostInboundData(BaseModel):
    config_profile_uuid: UUID = Field(serialization_alias="configProfileUuid")
    config_profile_inbound_uuid: UUID = Field(
        serialization_alias="configProfileInboundUuid"
    )


class CreateHostRequestDto(BaseModel):
    inbound: CreateHostInboundData
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
    muxParams: Optional[str] = Field(
        None,
        serialization_alias="muxParams",
    )
    sockopt_params: Optional[str] = Field(
        None,
        serialization_alias="sockoptParams",
    )
    tag: Optional[Annotated[str, StringConstraints(max_length=32)]] = Field(
        None, serialization_alias="tag"
    )
    is_hidden: Optional[bool] = Field(
        None,
        serialization_alias="isHidden",
    )
    override_sni_from_address: Optional[bool] = Field(
        None,
        serialization_alias="overrideSniFromAddress",
    )
    server_description: Optional[str] = Field(
        None, alias="serverDescription", max_length=30
    )

    # Legacy compatibility property
    @property
    def inbound_uuid(self) -> UUID:
        return self.inbound.config_profile_inbound_uuid

    # Constructor compatibility - support old-style inbound_uuid
    def __init__(
        self,
        inbound_uuid: Optional[UUID] = None,
        config_profile_uuid: Optional[UUID] = None,
        **data,
    ):
        if inbound_uuid is not None and "inbound" not in data:
            # Legacy mode: create inbound object from UUID
            # Use hardcoded config_profile_uuid from API response for compatibility
            data["inbound"] = CreateHostInboundData(
                config_profile_uuid=config_profile_uuid
                or UUID("107541f1-ae1a-4e2d-9dec-7297557b5125"),
                config_profile_inbound_uuid=inbound_uuid,
            )
        super().__init__(**data)
