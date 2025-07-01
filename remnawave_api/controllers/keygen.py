from remnawave_api.models import GetPubKeyResponseDto
from remnawave_api.rapid import BaseController, get


class KeygenController(BaseController):
    @get("/keygen", response_class=GetPubKeyResponseDto)
    async def generate_key(
        self,
    ) -> GetPubKeyResponseDto:
        """Get Public Key"""
        ...
