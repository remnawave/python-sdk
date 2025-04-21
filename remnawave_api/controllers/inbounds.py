from remnawave_api.models import FullInboundsResponseDto, InboundsResponseDto
from remnawave_api.rapid import BaseController, get


class InboundsController(BaseController):
    @get("/inbounds", response_class=InboundsResponseDto)
    async def get_inbounds(
        self,
    ) -> InboundsResponseDto:
        """Get Inbounds"""
        ...

    @get("/inbounds/full", response_class=FullInboundsResponseDto)
    async def get_full_inbounds(
        self,
    ) -> FullInboundsResponseDto:
        """Get Full Inbounds"""
        ...
