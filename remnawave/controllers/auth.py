from typing import Annotated

from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    GetStatusResponseDto,
    LoginRequestDto,
    LoginResponseDto,
    RegisterRequestDto,
    RegisterResponseDto,
    TelegramCallbackRequestDto,
    TelegramCallbackResponseDto,
)
from remnawave.rapid import BaseController, get, post


class AuthController(BaseController):
    @post("/auth/login", response_class=LoginResponseDto)
    async def login(
        self,
        body: Annotated[LoginRequestDto, PydanticBody()],
    ) -> LoginResponseDto:
        """Login"""
        ...

    @post("/auth/register", response_class=RegisterResponseDto)
    async def register(
        self,
        body: Annotated[RegisterRequestDto, PydanticBody()],
    ) -> RegisterResponseDto:
        """Register"""
        ...

    @get("/auth/status", response_class=GetStatusResponseDto)
    async def get_status(
        self,
    ) -> GetStatusResponseDto:
        """Get status"""
        ...

    @post("/auth/oauth2/tg/callback", response_class=TelegramCallbackResponseDto)
    async def oauth2_tg_callback(
        self,
        body: Annotated[TelegramCallbackRequestDto, PydanticBody()],
    ) -> TelegramCallbackResponseDto:
        """OAuth2 Telegram callback"""
        ...