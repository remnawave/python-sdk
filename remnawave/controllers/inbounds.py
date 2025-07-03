from typing import Annotated, Optional
from uuid import UUID

from rapid_api_client import Path
from remnawave.models import GetAllInboundsResponseDto, GetInboundsByProfileUuidResponseDto
from remnawave.rapid import BaseController, get


class InboundsController(BaseController):
    @get("/config-profiles/inbounds", response_class=GetAllInboundsResponseDto)
    async def get_all_inbounds(
        self,
    ) -> GetAllInboundsResponseDto:
        """Get all inbounds from all config profiles"""
        ...

    @get("/config-profiles/{uuid}/inbounds", response_class=GetInboundsByProfileUuidResponseDto)
    async def get_inbounds_by_profile_uuid(
        self,
        uuid: Annotated[str, Path(description="UUID of the config profile")],
    ) -> GetInboundsByProfileUuidResponseDto:
        """Get inbounds by profile uuid"""
        ...
