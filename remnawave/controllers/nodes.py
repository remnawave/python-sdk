from typing import Annotated

from rapid_api_client import Path
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    CreateNodeRequestDto,
    CreateNodeResponseDto,
    DeleteNodeResponseDto,
    DisableNodeResponseDto,
    EnableNodeResponseDto,
    GetAllNodesResponseDto,
    GetOneNodeResponseDto,
    ReorderNodeRequestDto,
    ReorderNodeResponseDto,
    RestartAllNodesResponseDto,
    RestartNodeResponseDto,
    UpdateNodeRequestDto,
    UpdateNodeResponseDto,
    RestartAllNodesRequestBodyDto, 
    ResetNodeTrafficRequestDto,
    ResetNodeTrafficResponseDto
)
from remnawave.rapid import BaseController, delete, get, patch, post


class NodesController(BaseController):
    @post("/nodes", response_class=CreateNodeResponseDto)
    async def create_node(
        self,
        body: Annotated[CreateNodeRequestDto, PydanticBody()],
    ) -> CreateNodeResponseDto:
        """Create Node"""
        ...

    @get("/nodes", response_class=GetAllNodesResponseDto)
    async def get_all_nodes(
        self,
    ) -> GetAllNodesResponseDto:
        """Get All Nodes"""
        ...

    @get("/nodes/{uuid}", response_class=GetOneNodeResponseDto)
    async def get_one_node(
        self,
        uuid: Annotated[str, Path(description="Node UUID")],
    ) -> GetOneNodeResponseDto:
        """Get One Node"""
        ...

    @delete("/nodes/{uuid}", response_class=DeleteNodeResponseDto)
    async def delete_node(
        self,
        uuid: Annotated[str, Path(description="Node UUID")],
    ) -> DeleteNodeResponseDto:
        """Delete Node"""
        ...

    @patch("/nodes", response_class=UpdateNodeResponseDto)
    async def update_node(
        self,
        body: Annotated[UpdateNodeRequestDto, PydanticBody()],
    ) -> UpdateNodeResponseDto:
        """Update Node"""
        ...

    @post("/nodes/{uuid}/actions/enable", response_class=EnableNodeResponseDto)
    async def enable_node(
        self,
        uuid: Annotated[str, Path(description="Node UUID")],
    ) -> EnableNodeResponseDto:
        """Enable Node"""
        ...

    @post("/nodes/{uuid}/actions/disable", response_class=DisableNodeResponseDto)
    async def disable_node(
        self,
        uuid: Annotated[str, Path(description="Node UUID")],
    ) -> DisableNodeResponseDto:
        """Disable Node"""
        ...

    @post("/nodes/{uuid}/actions/restart", response_class=RestartNodeResponseDto)
    async def restart_node(
        self,
        uuid: Annotated[str, Path(description="Node UUID")],
    ) -> RestartNodeResponseDto:
        """Restart Node"""
        ...

    @post("/nodes/actions/restart-all", response_class=RestartAllNodesResponseDto)
    async def restart_all_nodes(
        self,
        body: Annotated[RestartAllNodesRequestBodyDto, PydanticBody()],
    ) -> RestartAllNodesResponseDto:
        """Restart All Nodes"""
        ...

    @post("/nodes/actions/reorder", response_class=ReorderNodeResponseDto)
    async def reorder_nodes(
        self,
        body: Annotated[ReorderNodeRequestDto, PydanticBody()],
    ) -> ReorderNodeResponseDto:
        """Reorder Nodes"""
        ...
        
    @post("/nodes/actions/reset-traffic", response_class=ResetNodeTrafficResponseDto)
    async def reset_traffic_all_nodes(
        self,
        body: Annotated[ResetNodeTrafficRequestDto, PydanticBody()],
    ) -> ResetNodeTrafficResponseDto:
        """Reset Traffic All Nodes"""
        ...