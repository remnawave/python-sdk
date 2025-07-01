from typing import Annotated, Optional

from pydantic import BaseModel, Field, StringConstraints


class AuthTokenResponseData(BaseModel):
    access_token: str = Field(alias="accessToken")


class RegisterResponseDto(BaseModel):
    access_token: str = Field(alias="accessToken")


class LoginResponseDto(BaseModel):
    access_token: str = Field(alias="accessToken")


class TelegramBotInfo(BaseModel):
    bot_id: int = Field(alias="botId")


class StatusResponseData(BaseModel):
    is_login_allowed: bool = Field(alias="isLoginAllowed")
    is_register_allowed: bool = Field(alias="isRegisterAllowed")
    tg_auth: Optional[TelegramBotInfo] = Field(None, alias="tgAuth")


class GetStatusResponseDto(StatusResponseData):
    pass


class LoginRequestDto(BaseModel):
    username: str
    password: str


class RegisterRequestDto(BaseModel):
    username: str
    password: Annotated[str, StringConstraints(min_length=24)]


class TelegramCallbackRequestDto(BaseModel):
    id: int
    first_name: str
    last_name: Optional[str] = None
    username: Optional[str] = None
    photo_url: Optional[str] = None
    auth_date: int
    hash: str


class TelegramCallbackResponseDto(AuthTokenResponseData):
    pass


# Legacy alias for backward compatibility
StatusResponseDto = GetStatusResponseDto
LoginTelegramRequestDto = TelegramCallbackRequestDto