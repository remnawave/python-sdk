from typing import Annotated

from rapid_api_client.annotations import JsonBody

from remnawave.models import GetConfigResponseDto, UpdateConfigResponseDto
from remnawave.rapid import BaseController, get, put


class XrayConfigController(BaseController):
    @get("/xray", response_class=GetConfigResponseDto)
    async def get_config(
        self,
    ) -> GetConfigResponseDto:
        """Get Xray Config"""
        ...

    @put("/xray", response_class=UpdateConfigResponseDto)
    async def update_config(
        self,
        body: Annotated[dict, JsonBody()],
    ) -> UpdateConfigResponseDto:
        """Update Xray Config"""
        ...
