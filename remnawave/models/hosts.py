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
        None, serialization_alias="serverDescription", max_length=30
    )
    mux_params: Optional[str] = Field(
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
    vless_route_id: Optional[int] = Field(
        None,
        serialization_alias="vlessRouteId",
        ge=0,
        le=65535
    )
    shuffle_host: Optional[bool] = Field(
        None,
        serialization_alias="shuffleHost",
    )
    mihomo_x25519: Optional[bool] = Field(
        None,
        serialization_alias="mihomoX25519",
    )
    x_http_extra_params: Optional[str] = Field(
        None,
        serialization_alias="xHttpExtraParams",
    )
    nodes: Optional[List[str]] = None


class HostInboundData(BaseModel):
    config_profile_uuid: Optional[UUID] = Field(alias="configProfileUuid")
    config_profile_inbound_uuid: Optional[UUID] = Field(alias="configProfileInboundUuid")


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
    x_http_extra_params: Optional[str] = Field(
        None,
        alias="xHttpExtraParams",
    )
    mux_params: Optional[str] = Field(
        None,
        alias="muxParams",
    )
    sockopt_params: Optional[str] = Field(
        None,
        alias="sockoptParams",
    )
    inbound: HostInboundData
    server_description: Optional[str] = Field(
        None, alias="serverDescription"
    )
    tag: Optional[str] = None
    vless_route_id: Optional[int] = Field(
        None,
        alias="vlessRouteId",
    )
    shuffle_host: bool = Field(alias="shuffleHost")
    mihomo_x25519: bool = Field(alias="mihomoX25519")
    nodes: List[str]
    is_disabled: bool = Field(
        default=False,
        alias="isDisabled",
    )
    security_layer: SecurityLayer = Field(
        default=SecurityLayer.DEFAULT,
        alias="securityLayer",
    )
    is_hidden: bool = Field(
        default=False,
        alias="isHidden",
    )
    override_sni_from_address: bool = Field(
        default=False,
        alias="overrideSniFromAddress",
    )
    allow_insecure: bool = Field(
        default=False,
        alias="allowInsecure",
    )

    # Legacy compatibility property
    @property
    def inbound_uuid(self) -> Optional[UUID]:
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
    config_profile_uuid: Optional[UUID] = Field(serialization_alias="configProfileUuid")
    config_profile_inbound_uuid: Optional[UUID] = Field(
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
    x_http_extra_params: Optional[str] = Field(
        None,
        serialization_alias="xHttpExtraParams",
    )
    mux_params: Optional[str] = Field(
        None,
        serialization_alias="muxParams",
    )
    sockopt_params: Optional[str] = Field(
        None,
        serialization_alias="sockoptParams",
    )
    server_description: Optional[str] = Field(
        None, serialization_alias="serverDescription", max_length=30
    )
    tag: Optional[Annotated[str, StringConstraints(max_length=32)]] = Field(
        None, serialization_alias="tag"
    )
    vless_route_id: Optional[int] = Field(
        None,
        serialization_alias="vlessRouteId",
        ge=0,
        le=65535
    )
    shuffle_host: bool = Field(
        False,
        serialization_alias="shuffleHost",
    )
    mihomo_x25519: bool = Field(
        False,
        serialization_alias="mihomoX25519",
    )
    nodes: List[str] = Field(default_factory=list)
    allow_insecure: bool = Field(
        False,
        serialization_alias="allowInsecure",
    )
    is_disabled: bool = Field(
        False, 
        serialization_alias="isDisabled",
    )
    security_layer: SecurityLayer = Field(
        SecurityLayer.DEFAULT, 
        serialization_alias="securityLayer",
    )
    is_hidden: bool = Field(
        False,
        serialization_alias="isHidden",
    )
    override_sni_from_address: bool = Field(
        False, 
        serialization_alias="overrideSniFromAddress",
    )

    # Legacy compatibility property
    @property
    def inbound_uuid(self) -> Optional[UUID]:
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