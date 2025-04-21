from typing import Annotated

from rapid_api_client.annotations import PydanticBody

from remnawave_api.models import (
    LoginRequestDto,
    LoginResponseDto,
    RegisterRequestDto,
    RegisterResponseDto,
    StatusResponseDto,
)
from remnawave_api.rapid import BaseController, get, post


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

    @get("/auth/status", response_class=StatusResponseDto)
    async def get_status(
        self,
    ) -> StatusResponseDto:
        """Get status"""
        ...
