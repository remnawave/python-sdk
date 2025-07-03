from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class InfraProviderDto(BaseModel):
    uuid: UUID
    name: str
    favicon_link: Optional[str] = Field(None, alias="faviconLink")
    login_url: Optional[str] = Field(None, alias="loginUrl")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class InfraBillingHistoryDto(BaseModel):
    uuid: UUID
    node_uuid: UUID = Field(alias="nodeUuid")
    provider_uuid: UUID = Field(alias="providerUuid")
    provider: InfraProviderDto
    node: "NodeDto"
    next_billing_at: datetime = Field(alias="nextBillingAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class NodeDto(BaseModel):
    uuid: UUID
    name: str
    country_code: str = Field(alias="countryCode")


class InfraBillingNodeDto(BaseModel):
    uuid: UUID
    node_uuid: UUID = Field(alias="nodeUuid")
    provider_uuid: UUID = Field(alias="providerUuid")
    provider: InfraProviderDto
    node: NodeDto
    next_billing_at: datetime = Field(alias="nextBillingAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


# Provider models
class CreateInfraProviderRequestDto(BaseModel):
    name: str
    favicon_link: Optional[str] = Field(None, serialization_alias="faviconLink")
    login_url: Optional[str] = Field(None, serialization_alias="loginUrl")


class CreateInfraProviderResponseDto(InfraProviderDto):
    pass


class UpdateInfraProviderRequestDto(BaseModel):
    uuid: UUID
    name: Optional[str] = None
    favicon_link: Optional[str] = Field(None, serialization_alias="faviconLink")
    login_url: Optional[str] = Field(None, serialization_alias="loginUrl")


class UpdateInfraProviderResponseDto(InfraProviderDto):
    pass


class AllInfraProvidersData(BaseModel):
    total: int
    providers: List[InfraProviderDto]


class GetAllInfraProvidersResponseDto(AllInfraProvidersData):
    pass


class GetInfraProviderByUuidResponseDto(InfraProviderDto):
    pass


class DeleteInfraProviderResponseDto(BaseModel):
    is_deleted: bool = Field(alias="isDeleted")


# Billing History models
class InfraBillingHistoryData(BaseModel):
    records: List[InfraBillingHistoryDto]
    total: int


class GetAllInfraBillingHistoryResponseDto(InfraBillingHistoryData):
    pass


class GetInfraBillingHistoryByUuidResponseDto(InfraBillingHistoryDto):
    pass


# Billing Nodes models
class CreateInfraBillingNodeRequestDto(BaseModel):
    node_uuid: UUID = Field(serialization_alias="nodeUuid")
    provider_uuid: UUID = Field(serialization_alias="providerUuid")
    next_billing_at: datetime = Field(serialization_alias="nextBillingAt")


class CreateInfraBillingNodeResponseDto(InfraBillingNodeDto):
    pass


class UpdateInfraBillingNodeRequestDto(BaseModel):
    uuid: UUID
    node_uuid: Optional[UUID] = Field(None, serialization_alias="nodeUuid")
    provider_uuid: Optional[UUID] = Field(None, serialization_alias="providerUuid")
    next_billing_at: Optional[datetime] = Field(None, serialization_alias="nextBillingAt")


class UpdateInfraBillingNodeResponseDto(InfraBillingNodeDto):
    pass


class InfraBillingNodesData(BaseModel):
    total_billing_nodes: int = Field(alias="totalBillingNodes")
    total_active_nodes: Optional[int] = Field(None, alias="totalActiveNodes")
    total_spent: Optional[int] = Field(None, alias="totalSpent")
    billing_nodes: List[InfraBillingNodeDto] = Field(alias="billingNodes")


class GetAllInfraBillingNodesResponseDto(InfraBillingNodesData):
    pass


class GetInfraBillingNodeByUuidResponseDto(InfraBillingNodeDto):
    pass


class DeleteInfraBillingNodeResponseDto(BaseModel):
    is_deleted: bool = Field(alias="isDeleted")
