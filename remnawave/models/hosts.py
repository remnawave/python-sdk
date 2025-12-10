from typing import Annotated, Any, Dict, List, Optional
from uuid import UUID

from pydantic import BaseModel, Field, StringConstraints, RootModel

from remnawave.enums import ALPN, Fingerprint, SecurityLayer


class ReorderHostItem(BaseModel):
    view_position: int = Field(serialization_alias="viewPosition")
    uuid: UUID


class ReorderHostRequestDto(BaseModel):
    hosts: List[ReorderHostItem]


class HostInboundData(BaseModel):
    config_profile_uuid: Optional[UUID] = Field(None, alias="configProfileUuid")
    config_profile_inbound_uuid: Optional[UUID] = Field(None, alias="configProfileInboundUuid")


class CreateHostInboundData(BaseModel):
    config_profile_uuid: UUID = Field(serialization_alias="configProfileUuid")
    config_profile_inbound_uuid: UUID = Field(serialization_alias="configProfileInboundUuid")


class UpdateHostRequestDto(BaseModel):
    uuid: UUID
    inbound: Optional[CreateHostInboundData] = None
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
    security_layer: Optional[SecurityLayer] = Field(None, serialization_alias="securityLayer")
    server_description: Optional[str] = Field(None, serialization_alias="serverDescription", max_length=30)
    tag: Optional[Annotated[str, StringConstraints(max_length=32, pattern=r"^[A-Z0-9_:]+$")]] = None
    is_hidden: Optional[bool] = Field(None, serialization_alias="isHidden")
    override_sni_from_address: Optional[bool] = Field(None, serialization_alias="overrideSniFromAddress")
    keep_blank_sni: Optional[bool] = Field(None, serialization_alias="keepBlankSni")
    vless_route_id: Optional[int] = Field(None, serialization_alias="vlessRouteId", ge=0, le=65535)
    shuffle_host: Optional[bool] = Field(None, serialization_alias="shuffleHost")
    mihomo_x25519: Optional[bool] = Field(None, serialization_alias="mihomoX25519")
    x_http_extra_params: Optional[Dict[str, Any]] = Field(None, serialization_alias="xHttpExtraParams")
    mux_params: Optional[Dict[str, Any]] = Field(None, serialization_alias="muxParams")
    sockopt_params: Optional[Dict[str, Any]] = Field(None, serialization_alias="sockoptParams")
    nodes: Optional[List[UUID]] = None
    xray_json_template_uuid: Optional[UUID] = Field(None, serialization_alias="xrayJsonTemplateUuid")
    excluded_internal_squads: Optional[List[UUID]] = Field(None, serialization_alias="excludedInternalSquads")

    @property
    def inbound_uuid(self) -> Optional[UUID]:
        return self.inbound.config_profile_inbound_uuid if self.inbound else None


class HostResponseDto(BaseModel):
    uuid: UUID
    view_position: int = Field(alias="viewPosition")
    remark: str
    address: str
    port: int
    path: Optional[str] = None
    sni: Optional[str] = None
    host: Optional[str] = None
    alpn: Optional[str] = None
    fingerprint: Optional[str] = None
    x_http_extra_params: Optional[Dict[str, Any]] = Field(None, alias="xHttpExtraParams")
    mux_params: Optional[Dict[str, Any]] = Field(None, alias="muxParams")
    sockopt_params: Optional[Dict[str, Any]] = Field(None, alias="sockoptParams")
    inbound: HostInboundData
    server_description: Optional[str] = Field(None, alias="serverDescription")
    tag: Optional[str] = None
    vless_route_id: Optional[int] = Field(None, alias="vlessRouteId")
    shuffle_host: bool = Field(alias="shuffleHost")
    mihomo_x25519: bool = Field(alias="mihomoX25519")
    nodes: List[UUID]
    is_disabled: bool = Field(False, alias="isDisabled")
    security_layer: SecurityLayer = Field(SecurityLayer.DEFAULT, alias="securityLayer")
    is_hidden: bool = Field(False, alias="isHidden")
    override_sni_from_address: bool = Field(False, alias="overrideSniFromAddress")
    keep_blank_sni: bool = Field(False, alias="keepBlankSni")
    allow_insecure: bool = Field(False, alias="allowInsecure")
    xray_json_template_uuid: Optional[UUID] = Field(None, alias="xrayJsonTemplateUuid")
    excluded_internal_squads: List[UUID] = Field(default_factory=list, alias="excludedInternalSquads")

    @property
    def inbound_uuid(self) -> Optional[UUID]:
        return self.inbound.config_profile_inbound_uuid


class CreateHostRequestDto(BaseModel):
    inbound: CreateHostInboundData
    remark: Annotated[str, StringConstraints(min_length=1, max_length=40)]
    address: str
    port: int
    path: Optional[str] = None
    sni: Optional[str] = None
    host: Optional[str] = None
    alpn: Optional[ALPN] = None
    fingerprint: Optional[Fingerprint] = None
    x_http_extra_params: Optional[Dict[str, Any]] = Field(None, serialization_alias="xHttpExtraParams")
    mux_params: Optional[Dict[str, Any]] = Field(None, serialization_alias="muxParams")
    sockopt_params: Optional[Dict[str, Any]] = Field(None, serialization_alias="sockoptParams")
    server_description: Optional[str] = Field(None, serialization_alias="serverDescription", max_length=30)
    tag: Optional[Annotated[str, StringConstraints(max_length=32, pattern=r"^[A-Z0-9_:]+$")]] = None
    vless_route_id: Optional[int] = Field(None, serialization_alias="vlessRouteId", ge=0, le=65535)
    shuffle_host: bool = Field(False, serialization_alias="shuffleHost")
    mihomo_x25519: bool = Field(False, serialization_alias="mihomoX25519")
    nodes: List[UUID] = Field(default_factory=list)
    allow_insecure: bool = Field(False, serialization_alias="allowInsecure")
    is_disabled: bool = Field(False, serialization_alias="isDisabled")
    security_layer: SecurityLayer = Field(SecurityLayer.DEFAULT, serialization_alias="securityLayer")
    is_hidden: bool = Field(False, serialization_alias="isHidden")
    override_sni_from_address: bool = Field(False, serialization_alias="overrideSniFromAddress")
    keep_blank_sni: bool = Field(False, serialization_alias="keepBlankSni")
    xray_json_template_uuid: Optional[UUID] = Field(None, serialization_alias="xrayJsonTemplateUuid")
    excluded_internal_squads: List[UUID] = Field(default_factory=list, serialization_alias="excludedInternalSquads")

    @property
    def inbound_uuid(self) -> Optional[UUID]:
        return self.inbound.config_profile_inbound_uuid

    def __init__(
        self,
        inbound_uuid: Optional[UUID] = None,
        config_profile_uuid: Optional[UUID] = None,
        **data,
    ):
        if inbound_uuid is not None and "inbound" not in data:
            data["inbound"] = CreateHostInboundData(
                config_profile_uuid=config_profile_uuid
                or UUID("107541f1-ae1a-4e2d-9dec-7297557b5125"),
                config_profile_inbound_uuid=inbound_uuid,
            )
        super().__init__(**data)


class GetAllHostTagsResponseDto(BaseModel):
    tags: List[str]


# Response wrappers - обернуты в response
class CreateHostResponseDto(HostResponseDto):
    """Create host response"""
    pass


class UpdateHostResponseDto(CreateHostResponseDto):
    """Update host response"""
    pass


class GetAllHostsResponseDto(RootModel[List[HostResponseDto]]):
    root: List[HostResponseDto]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]
    
    def __bool__(self):
        """Return True if list is not empty"""
        return bool(self.root)
    
    def __len__(self):
        """Return length of list"""
        return len(self.root)


class GetOneHostResponseDto(HostResponseDto):
    """Get one host response"""
    pass


class ReorderHostResponseDto(BaseModel):
    """Reorder hosts response"""
    is_updated: bool = Field(alias="isUpdated", default=True)


class DeleteHostResponseDto(BaseModel):
    """Delete host response"""
    is_deleted: bool = Field(alias="isDeleted")
    
class HostsResponseDto(HostResponseDto):
    """Host response data with backward compatibility properties"""
    
    @property
    def allow_insecure(self) -> bool:
        """Backward compatibility property"""
        return self.security_layer == SecurityLayer.NONE