from datetime import datetime
from typing import Any, Dict, List

from pydantic import BaseModel, Field


class PasskeyDto(BaseModel):
    """Passkey data model"""
    id: str
    name: str
    created_at: datetime = Field(alias="createdAt")
    last_used_at: datetime = Field(alias="lastUsedAt")


# Registration models
class GetPasskeyRegistrationOptionsResponseDto(BaseModel):
    """Response with passkey registration options"""
    # WebAuthn registration options are complex objects, using Any for flexibility
    response: Dict[str, Any]


class VerifyPasskeyRegistrationRequestDto(BaseModel):
    """Request to verify passkey registration"""
    # WebAuthn registration response is complex object
    response: Dict[str, Any]


class VerifyPasskeyRegistrationResponseDto(BaseModel):
    """Response with passkey registration verification result"""
    verified: bool


# Passkeys management models
class GetAllPasskeysResponseDto(BaseModel):
    """Response with all user's passkeys"""
    passkeys: List[PasskeyDto]


class DeletePasskeyRequestDto(BaseModel):
    """Request to delete a passkey"""
    id: str


class DeletePasskeyResponseDto(BaseModel):
    """Response with updated passkeys list after deletion"""
    passkeys: List[PasskeyDto]