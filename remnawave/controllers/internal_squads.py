from typing import Annotated

from rapid_api_client import Path
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    AddUsersToInternalSquadRequestDto,
    AddUsersToInternalSquadResponseDto,
    CreateInternalSquadRequestDto,
    CreateInternalSquadResponseDto,
    DeleteInternalSquadResponseDto,
    DeleteUsersFromInternalSquadRequestDto,
    DeleteUsersFromInternalSquadResponseDto,
    GetAllInternalSquadsResponseDto,
    GetInternalSquadByUuidResponseDto,
    UpdateInternalSquadRequestDto,
    UpdateInternalSquadResponseDto,
    GetInternalSquadAccessibleNodesResponseDto,
)
from remnawave.rapid import BaseController, delete, get, patch, post


class InternalSquadsController(BaseController):
    @get("/internal-squads", response_class=GetAllInternalSquadsResponseDto)
    async def get_internal_squads(self) -> GetAllInternalSquadsResponseDto:
        """Get all internal squads"""
        ...

    @post("/internal-squads", response_class=CreateInternalSquadResponseDto)
    async def create_internal_squad(
        self,
        body: Annotated[CreateInternalSquadRequestDto, PydanticBody()],
    ) -> CreateInternalSquadResponseDto:
        """Create internal squad"""
        ...

    @patch("/internal-squads", response_class=UpdateInternalSquadResponseDto)
    async def update_internal_squad(
        self,
        body: Annotated[UpdateInternalSquadRequestDto, PydanticBody()],
    ) -> UpdateInternalSquadResponseDto:
        """Update internal squad"""
        ...

    @get("/internal-squads/{uuid}", response_class=GetInternalSquadByUuidResponseDto)
    async def get_internal_squad_by_uuid(
        self,
        uuid: Annotated[str, Path(description="UUID of the internal squad")],
    ) -> GetInternalSquadByUuidResponseDto:
        """Get internal squad by uuid"""
        ...

    @delete("/internal-squads/{uuid}", response_class=DeleteInternalSquadResponseDto)
    async def delete_internal_squad(
        self,
        uuid: Annotated[str, Path(description="UUID of the internal squad")],
    ) -> DeleteInternalSquadResponseDto:
        """Delete internal squad"""
        ...

    @post(
        "/internal-squads/{uuid}/bulk-actions/add-users",
        response_class=AddUsersToInternalSquadResponseDto,
    )
    async def add_users_to_internal_squad(
        self,
        uuid: Annotated[str, Path(description="UUID of the internal squad")],
    ) -> AddUsersToInternalSquadResponseDto:
        """Add users to internal squad"""
        ...

    @delete(
        "/internal-squads/{uuid}/bulk-actions/remove-users",
        response_class=DeleteUsersFromInternalSquadResponseDto,
    )
    async def remove_users_from_internal_squad(
        self,
        uuid: Annotated[str, Path(description="UUID of the internal squad")],
    ) -> DeleteUsersFromInternalSquadResponseDto:
        """Delete users from internal squad"""
        ...

    @get(
        "/internal-squads/{uuid}/accessible-nodes",
        response_class=GetInternalSquadAccessibleNodesResponseDto,
    )
    async def get_accessible_nodes(
        self,
        uuid: Annotated[str, Path(description="UUID of the internal squad")],
    ) -> GetInternalSquadAccessibleNodesResponseDto:
        """Get accessible nodes for internal squad"""
        ...
