from datetime import datetime
from typing import Any, Dict, List

from pydantic import BaseModel, Field, StringConstraints
from typing import Annotated


class PasskeyDto(BaseModel):
    """Passkey data model"""
    id: str
    name: str
    created_at: datetime = Field(alias="createdAt")
    last_used_at: datetime = Field(alias="lastUsedAt")


# Registration models
class GetPasskeyRegistrationOptionsResponseDto(BaseModel):
    """Response with passkey registration options"""
    # WebAuthn registration options are complex objects
    pass


class VerifyPasskeyRegistrationRequestDto(BaseModel):
    """Request to verify passkey registration"""
    # WebAuthn registration response is complex object
    response: Dict[str, Any]


class VerifyPasskeyRegistrationResponseData(BaseModel):
    """Passkey registration verification result data"""
    verified: bool


class VerifyPasskeyRegistrationResponseDto(BaseModel):
    """Response with passkey registration verification result"""
    verified: bool


class GetAllPasskeysResponseData(BaseModel):
    """Response data with all user's passkeys"""
    passkeys: List[PasskeyDto]


class GetAllPasskeysResponseDto(BaseModel):
    """Response with all user's passkeys"""
    passkeys: List[PasskeyDto]


class DeletePasskeyRequestDto(BaseModel):
    """Request to delete a passkey"""
    id: str


class DeletePasskeyResponseData(BaseModel):
    """Response data with updated passkeys list after deletion"""
    passkeys: List[PasskeyDto]


class DeletePasskeyResponseDto(BaseModel):
    """Response with updated passkeys list after deletion"""
    passkeys: List[PasskeyDto]


class UpdatePasskeyRequestDto(BaseModel):
    """Request to update a passkey"""
    id: str
    name: Annotated[str, StringConstraints(min_length=2, max_length=30, pattern=r"^[A-Za-z0-9_\s-]+$")]


class UpdatePasskeyResponseData(BaseModel):
    """Response data with updated passkeys list"""
    passkeys: List[PasskeyDto]


class UpdatePasskeyResponseDto(BaseModel):
    """Response with updated passkey information"""
    passkeys: List[PasskeyDto]
