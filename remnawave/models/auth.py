from typing import Annotated, Any, Dict, Optional

from pydantic import BaseModel, Field, StringConstraints

from remnawave.enums.auth import OAuth2Provider


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


# OAuth2 Authorization models
class OAuth2AuthorizeRequestDto(BaseModel):
    """Request to initiate OAuth2 authorization"""
    provider: OAuth2Provider


class OAuth2AuthorizeResponseDto(BaseModel):
    """Response with OAuth2 authorization URL"""
    authorization_url: Optional[str] = Field(alias="authorizationUrl")


# OAuth2 Callback models
class OAuth2CallbackRequestDto(BaseModel):
    """Request for OAuth2 callback"""
    provider: OAuth2Provider
    code: str
    state: str


class OAuth2CallbackResponseDto(BaseModel):
    """Response with access token from OAuth2 callback"""
    access_token: str = Field(alias="accessToken")


# Passkey Authentication models
class GetPasskeyAuthenticationOptionsResponseDto(BaseModel):
    """Response with passkey authentication options"""
    # Passkey options are complex WebAuthn objects, using Any for flexibility
    response: Dict[str, Any]


class VerifyPasskeyAuthenticationRequestDto(BaseModel):
    """Request to verify passkey authentication"""
    # Passkey authentication response is complex WebAuthn object
    response: Dict[str, Any]


class VerifyPasskeyAuthenticationResponseDto(BaseModel):
    """Response with access token after successful passkey authentication"""
    access_token: str = Field(alias="accessToken")

# Legacy alias for backward compatibility
StatusResponseDto = GetStatusResponseDto
LoginTelegramRequestDto = TelegramCallbackRequestDto
