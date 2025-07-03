from typing import Annotated
from uuid import UUID

from remnawave.models import (
    AddInboundToNodesResponseDto,
    AddInboundToUsersResponseDto,
    RemoveInboundFromNodesResponseDto,
    RemoveInboundFromUsersResponseDto,
)
from remnawave.rapid import AttributeBody, BaseController, post


class InboundsBulkActionsController(BaseController):
    @post("/inbounds/bulk/add-to-users", response_class=AddInboundToUsersResponseDto)
    async def add_inbound_to_users(
        self,
        inbound_uuid: Annotated[UUID, AttributeBody()],
    ) -> AddInboundToUsersResponseDto:
        """Add Inbound To Users"""
        ...

    @post(
        "/inbounds/bulk/remove-from-users",
        response_class=RemoveInboundFromUsersResponseDto,
    )
    async def remove_inbound_from_users(
        self,
        inbound_uuid: Annotated[UUID, AttributeBody()],
    ) -> RemoveInboundFromUsersResponseDto:
        """Remove Inbound From Users"""
        ...

    @post("/inbounds/bulk/add-to-nodes", response_class=AddInboundToNodesResponseDto)
    async def add_inbound_to_nodes(
        self,
        inbound_uuid: Annotated[UUID, AttributeBody()],
    ) -> AddInboundToNodesResponseDto:
        """Add Inbound To All Nodes"""
        ...

    @post(
        "/inbounds/bulk/remove-from-nodes",
        response_class=RemoveInboundFromNodesResponseDto,
    )
    async def remove_inbound_from_nodes(
        self,
        inbound_uuid: Annotated[UUID, AttributeBody()],
    ) -> RemoveInboundFromNodesResponseDto:
        """Remove Inbound From All Nodes"""
        ...
