from typing import Annotated

from rapid_api_client import Path, Query
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    CreateInfraBillingNodeRequestDto,
    CreateInfraBillingNodeResponseDto,
    CreateInfraProviderRequestDto,
    CreateInfraProviderResponseDto,
    DeleteInfraBillingNodeResponseDto,
    DeleteInfraProviderResponseDto,
    GetAllInfraBillingHistoryResponseDto,
    GetAllInfraBillingNodesResponseDto,
    GetAllInfraProvidersResponseDto,
    GetInfraBillingHistoryByUuidResponseDto,
    GetInfraBillingNodeByUuidResponseDto,
    GetInfraProviderByUuidResponseDto,
    UpdateInfraBillingNodeRequestDto,
    UpdateInfraBillingNodeResponseDto,
    UpdateInfraProviderRequestDto,
    UpdateInfraProviderResponseDto,
)
from remnawave.rapid import BaseController, delete, get, patch, post


class InfraBillingController(BaseController):
    @get("/infra-billing/providers", response_class=GetAllInfraProvidersResponseDto)
    async def get_all_infra_providers(self) -> GetAllInfraProvidersResponseDto:
        """Get all infra providers"""
        ...

    @post("/infra-billing/providers", response_class=CreateInfraProviderResponseDto)
    async def create_infra_provider(
        self,
        body: Annotated[CreateInfraProviderRequestDto, PydanticBody()],
    ) -> CreateInfraProviderResponseDto:
        """Create infra provider"""
        ...

    @patch("/infra-billing/providers", response_class=UpdateInfraProviderResponseDto)
    async def update_infra_provider(
        self,
        body: Annotated[UpdateInfraProviderRequestDto, PydanticBody()],
    ) -> UpdateInfraProviderResponseDto:
        """Update infra provider"""
        ...

    @get("/infra-billing/providers/{uuid}", response_class=GetInfraProviderByUuidResponseDto)
    async def get_infra_provider_by_uuid(
        self,
        uuid: Annotated[str, Path(description="UUID of the infra provider")],
    ) -> GetInfraProviderByUuidResponseDto:
        """Get infra provider by uuid"""
        ...

    @delete("/infra-billing/providers/{uuid}", response_class=DeleteInfraProviderResponseDto)
    async def delete_infra_provider_by_uuid(
        self,
        uuid: Annotated[str, Path(description="UUID of the infra provider")],
    ) -> DeleteInfraProviderResponseDto:
        """Delete infra provider"""
        ...

    @get("/infra-billing/history", response_class=GetAllInfraBillingHistoryResponseDto)
    async def get_all_infra_billing_history(
        self,
        start: Annotated[int, Query(default=0, ge=0, description="Index to start pagination from")],
        size: Annotated[int, Query(default=25, ge=1, description="Number of entries per page")],
    ) -> GetAllInfraBillingHistoryResponseDto:
        """Get all infra billing history"""
        ...

    @get("/infra-billing/history/{uuid}", response_class=GetInfraBillingHistoryByUuidResponseDto)
    async def get_infra_billing_history_by_uuid(
        self,
        uuid: Annotated[str, Path(description="UUID of the billing history entry")],
    ) -> GetInfraBillingHistoryByUuidResponseDto:
        """Get infra billing history by uuid"""
        ...

    @get("/infra-billing/nodes", response_class=GetAllInfraBillingNodesResponseDto)
    async def get_all_infra_billing_nodes(
        self,
        start: Annotated[int, Query(default=0, ge=0, description="Index to start pagination from")],
        size: Annotated[int, Query(default=25, ge=1, description="Number of entries per page")],
    ) -> GetAllInfraBillingNodesResponseDto:
        """Get all infra billing nodes"""
        ...

    @patch("/infra-billing/nodes", response_class=UpdateInfraBillingNodeResponseDto)
    async def update_infra_billing_node(
        self,
        body: Annotated[UpdateInfraBillingNodeRequestDto, PydanticBody()],
    ) -> UpdateInfraBillingNodeResponseDto:
        """Update infra billing node"""
        ...

    @post("/infra-billing/nodes", response_class=CreateInfraBillingNodeResponseDto)
    async def create_infra_billing_node(
        self,
        body: Annotated[CreateInfraBillingNodeRequestDto, PydanticBody()],
    ) -> CreateInfraBillingNodeResponseDto:
        """Create infra billing node"""
        ...

    @get("/infra-billing/nodes/{uuid}", response_class=GetInfraBillingNodeByUuidResponseDto)
    async def get_infra_billing_node_by_uuid(
        self,
        uuid: Annotated[str, Path(description="UUID of the infra billing node")],
    ) -> GetInfraBillingNodeByUuidResponseDto:
        """Get infra billing node by uuid"""
        ...

    @delete("/infra-billing/nodes/{uuid}", response_class=DeleteInfraBillingNodeResponseDto)
    async def delete_infra_billing_node_by_uuid(
        self,
        uuid: Annotated[str, Path(description="UUID of the infra billing node")],
    ) -> DeleteInfraBillingNodeResponseDto:
        """Delete infra billing node"""
        ...
