from typing import Annotated, List

from rapid_api_client import Path
from rapid_api_client.annotations import PydanticBody

from remnawave_api.models import (
    CreateHostRequestDto,
    DeleteHostResponseDto,
    HostResponseDto,
    HostsResponseDto,
    ReorderHostRequestDto,
    ReorderHostResponseDto,
    UpdateHostRequestDto,
)
from remnawave_api.rapid import AttributeBody, BaseController, delete, get, post


class HostsController(BaseController):
    @post("/hosts/create", response_class=HostResponseDto)
    async def create_host(
        self,
        body: Annotated[CreateHostRequestDto, PydanticBody()],
    ) -> HostResponseDto:
        """Create Host"""
        ...

    @post("/hosts/update", response_class=HostResponseDto)
    async def update_host(
        self,
        body: Annotated[UpdateHostRequestDto, PydanticBody()],
    ) -> HostResponseDto:
        """Update Host"""
        ...

    @get("/hosts/all", response_class=HostsResponseDto)
    async def get_all_hosts(
        self,
    ) -> HostsResponseDto:
        """Get All Hosts"""
        ...

    @get("/hosts/get-one/{uuid}", response_class=HostResponseDto)
    async def get_one_host(
        self,
        uuid: Annotated[str, Path(description="UUID of the host")],
    ) -> HostResponseDto:
        """Get One Host"""
        ...

    @post("/hosts/reorder", response_class=ReorderHostResponseDto)
    async def reorder_hosts(
        self,
        hosts: Annotated[List[ReorderHostRequestDto], AttributeBody()],
    ) -> ReorderHostResponseDto:
        """Reorder Hosts"""
        ...

    @delete("/hosts/delete/{uuid}", response_class=DeleteHostResponseDto)
    async def delete_host(
        self,
        uuid: Annotated[str, Path(description="UUID of the host")],
    ) -> DeleteHostResponseDto:
        """Delete Host"""
        ...
