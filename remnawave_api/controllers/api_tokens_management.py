from typing import Annotated

from httpx import Response
from rapid_api_client import Path
from rapid_api_client.annotations import PydanticBody

from remnawave_api.models import CreateApiTokenRequestDto
from remnawave_api.rapid import BaseController, delete, get, post


class APITokensManagementController(BaseController):
    @post("/tokens/create", response_class=Response)
    async def create(
        self,
        body: Annotated[CreateApiTokenRequestDto, PydanticBody()],
    ) -> Response:
        """Create new API token"""
        ...

    @delete("/tokens/delete/{uuid}", response_class=Response)
    async def delete(
        self,
        uuid: Annotated[str, Path(description="UUID of the API token")],
    ) -> Response:
        """Delete API token"""
        ...

    @get("/tokens", response_class=Response)
    async def find_all(
        self,
    ) -> Response:
        """Get all API tokens"""
        ...
