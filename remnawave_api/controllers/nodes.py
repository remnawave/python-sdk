from typing import Annotated, List

from rapid_api_client import Path
from rapid_api_client.annotations import PydanticBody

from remnawave_api.models import (
    CreateNodeRequestDto,
    DeleteNodeResponseDto,
    NodeResponseDto,
    NodesResponseDto,
    ReorderNodeRequestDto,
    RestartNodeResponseDto,
    UpdateNodeRequestDto,
)
from remnawave_api.rapid import AttributeBody, BaseController, delete, get, patch, post


class NodesController(BaseController):
    @post("/nodes/create", response_class=NodeResponseDto)
    async def create_node(
        self,
        body: Annotated[CreateNodeRequestDto, PydanticBody()],
    ) -> NodeResponseDto:
        """Create Node"""
        ...

    @get("/nodes/get-all", response_class=NodesResponseDto)
    async def get_all_nodes(
        self,
    ) -> NodesResponseDto:
        """Get All Nodes"""
        ...

    @get("/nodes/get-one/{uuid}", response_class=NodeResponseDto)
    async def get_one_node(
        self,
        uuid: Annotated[str, Path(description="Node UUID")],
    ) -> NodeResponseDto:
        """Get One Node"""
        ...

    @patch("/nodes/enable/{uuid}", response_class=NodeResponseDto)
    async def enable_node(
        self,
        uuid: Annotated[str, Path(description="Node UUID")],
    ) -> NodeResponseDto:
        """Enable Node"""
        ...

    @patch("/nodes/disable/{uuid}", response_class=NodeResponseDto)
    async def disable_node(
        self,
        uuid: Annotated[str, Path(description="Node UUID")],
    ) -> NodeResponseDto:
        """Disable Node"""
        ...

    @delete("/nodes/delete/{uuid}", response_class=DeleteNodeResponseDto)
    async def delete_node(
        self,
        uuid: Annotated[str, Path(description="Node UUID")],
    ) -> DeleteNodeResponseDto:
        """Delete Node"""
        ...

    @post("/nodes/update", response_class=NodeResponseDto)
    async def update_node(
        self,
        body: Annotated[UpdateNodeRequestDto, PydanticBody()],
    ) -> NodeResponseDto:
        """Update Node"""
        ...

    @get("/nodes/restart/{uuid}", response_class=RestartNodeResponseDto)
    async def restart_node(
        self,
        uuid: Annotated[str, Path(description="Node UUID")],
    ) -> RestartNodeResponseDto:
        """Restart Node"""
        ...

    @patch("/nodes/restart-all", response_class=RestartNodeResponseDto)
    async def restart_all_nodes(
        self,
    ) -> RestartNodeResponseDto:
        """Restart All Nodes"""
        ...

    @post("/nodes/reorder", response_class=NodesResponseDto)
    async def reorder_nodes(
        self,
        nodes: Annotated[List[ReorderNodeRequestDto], AttributeBody()],
    ) -> NodesResponseDto:
        """Reorder Nodes"""
        ...
