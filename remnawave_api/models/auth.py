from typing import Annotated

from pydantic import BaseModel, Field, StringConstraints


class RegisterResponseDto(BaseModel):
    access_token: str = Field(alias="accessToken")


class LoginResponseDto(BaseModel):
    access_token: str = Field(alias="accessToken")


class LoginRequestDto(BaseModel):
    username: str
    password: str


class RegisterRequestDto(BaseModel):
    username: str
    password: Annotated[str, StringConstraints(min_length=24)]


class StatusResponseDto(BaseModel):
    is_login_allowed: bool = Field(alias="isLoginAllowed")
    is_register_allowed: bool = Field(alias="isRegisterAllowed")
