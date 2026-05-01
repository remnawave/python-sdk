from typing import Annotated

from rapid_api_client import Path
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    GetNodeMetadataResponseDto,
    GetUserMetadataResponseDto,
    UpsertNodeMetadataRequestBodyDto,
    UpsertNodeMetadataResponseDto,
    UpsertUserMetadataRequestBodyDto,
    UpsertUserMetadataResponseDto,
)
from remnawave.rapid import BaseController, get, put


class MetadataController(BaseController):
    @get("/metadata/user/{uuid}", response_class=GetUserMetadataResponseDto)
    async def get_user_metadata(
        self,
        uuid: Annotated[str, Path(description="User UUID")],
    ) -> GetUserMetadataResponseDto:
        """Get user metadata"""
        ...

    @put("/metadata/user/{uuid}", response_class=UpsertUserMetadataResponseDto)
    async def upsert_user_metadata(
        self,
        uuid: Annotated[str, Path(description="User UUID")],
        body: Annotated[UpsertUserMetadataRequestBodyDto, PydanticBody()],
    ) -> UpsertUserMetadataResponseDto:
        """Update or create User Metadata"""
        ...

    @get("/metadata/node/{uuid}", response_class=GetNodeMetadataResponseDto)
    async def get_node_metadata(
        self,
        uuid: Annotated[str, Path(description="Node UUID")],
    ) -> GetNodeMetadataResponseDto:
        """Get node metadata"""
        ...

    @put("/metadata/node/{uuid}", response_class=UpsertNodeMetadataResponseDto)
    async def upsert_node_metadata(
        self,
        uuid: Annotated[str, Path(description="Node UUID")],
        body: Annotated[UpsertNodeMetadataRequestBodyDto, PydanticBody()],
    ) -> UpsertNodeMetadataResponseDto:
        """Update or create Node Metadata"""
        ...
