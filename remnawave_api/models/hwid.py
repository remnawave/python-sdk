from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class CreateUserHwidDeviceRequestDto(BaseModel):
    hwid: str
    user_uuid: UUID = Field(serialization_alias="userUuid")
    platform: Optional[str] = None
    os_version: Optional[str] = Field(None, serialization_alias="osVersion")
    device_model: Optional[str] = Field(None, serialization_alias="deviceModel")
    user_agent: Optional[str] = Field(None, serialization_alias="userAgent")


class DeleteUserHwidDeviceRequestDto(BaseModel):
    user_uuid: UUID = Field(serialization_alias="userUuid")
    hwid: str


class HwidDeviceDto(BaseModel):
    hwid: str
    user_uuid: UUID = Field(alias="userUuid")
    platform: Optional[str] = None
    os_version: Optional[str] = Field(None, alias="osVersion")
    device_model: Optional[str] = Field(None, alias="deviceModel")
    user_agent: Optional[str] = Field(None, alias="userAgent")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class HwidDevicesData(BaseModel):
    total: float
    devices: List[HwidDeviceDto]


class CreateUserHwidDeviceResponseDto(BaseModel):
    total: float
    devices: List[HwidDeviceDto]


class DeleteUserHwidDeviceResponseDto(BaseModel):
    total: float
    devices: List[HwidDeviceDto]


class GetUserHwidDevicesResponseDto(BaseModel):
    total: float
    devices: List[HwidDeviceDto]


# Legacy aliases for backward compatibility
CreateHWIDUser = CreateUserHwidDeviceRequestDto
HWIDUserResponseDto = HwidDeviceDto
HWIDUserResponseDtoList = HwidDevicesData
HWIDDeleteRequest = DeleteUserHwidDeviceRequestDto
    
