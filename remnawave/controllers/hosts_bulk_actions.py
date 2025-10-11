from typing import Annotated, List
from uuid import UUID

from rapid_api_client import PydanticBody

from remnawave.models import (
    BulkDeleteHostsResponseDto,
    BulkDisableHostsResponseDto,
    BulkEnableHostsResponseDto,
    SetInboundToManyHostsRequestDto,
    SetInboundToManyHostsResponseDto,
    SetPortToManyHostsResponseDto,
    SetPortToManyHostsRequestDto
)
from remnawave.rapid import AttributeBody, BaseController, post


class HostsBulkActionsController(BaseController):
    @post("/hosts/bulk/delete", response_class=BulkDeleteHostsResponseDto)
    async def delete_hosts(
        self,
        uuids: Annotated[List[UUID], AttributeBody()],
    ) -> BulkDeleteHostsResponseDto:
        """Delete many hosts"""
        ...

    @post("/hosts/bulk/disable", response_class=BulkDisableHostsResponseDto)
    async def disable_hosts(
        self,
        uuids: Annotated[List[UUID], AttributeBody()],
    ) -> BulkDisableHostsResponseDto:
        """Disable many hosts"""
        ...

    @post("/hosts/bulk/enable", response_class=BulkEnableHostsResponseDto)
    async def enable_hosts(
        self,
        uuids: Annotated[List[UUID], AttributeBody()],
    ) -> BulkEnableHostsResponseDto:
        """Enable many hosts"""
        ...

    @post(
        "/hosts/bulk/set-inbound",
        response_class=SetInboundToManyHostsResponseDto,
    )
    async def set_inbound_to_hosts(
        self,
        body: Annotated[SetInboundToManyHostsRequestDto, PydanticBody()],
    ) -> SetInboundToManyHostsResponseDto:
        """Set inbound to many hosts"""
        ...

    @post("/hosts/bulk/set-port", response_class=SetPortToManyHostsResponseDto)
    async def set_port_to_hosts(
        self,
        body: Annotated[SetPortToManyHostsRequestDto, PydanticBody()],
    ) -> SetPortToManyHostsResponseDto:
        """Set port to many hosts"""
        ...
