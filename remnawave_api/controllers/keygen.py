from remnawave_api.models import PubKeyResponseDto
from remnawave_api.rapid import BaseController, get


class KeygenController(BaseController):
    @get("/keygen/get", response_class=PubKeyResponseDto)
    async def generate_key(
        self,
    ) -> PubKeyResponseDto:
        """Get Public Key"""
        ...
