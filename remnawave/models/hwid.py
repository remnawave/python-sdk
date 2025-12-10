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
    total: int
    devices: List[HwidDeviceDto]


class CreateUserHwidDeviceResponseDto(BaseModel):
    total: int
    devices: List[HwidDeviceDto]


class DeleteUserHwidDeviceResponseDto(BaseModel):
    total: int
    devices: List[HwidDeviceDto]


class GetUserHwidDevicesResponseDto(BaseModel):
    total: int
    devices: List[HwidDeviceDto]

class PlatformStatItem(BaseModel):
    platform: str
    count: float


class AppStatItem(BaseModel):
    app: str
    count: float


class HwidStats(BaseModel):
    total_unique_devices: float = Field(alias="totalUniqueDevices")
    total_hwid_devices: float = Field(alias="totalHwidDevices")
    average_hwid_devices_per_user: float = Field(alias="averageHwidDevicesPerUser")


class HwidStatisticsData(BaseModel):
    by_platform: List[PlatformStatItem] = Field(alias="byPlatform")
    by_app: List[AppStatItem] = Field(alias="byApp")
    stats: HwidStats


class GetHwidStatisticsResponseDto(HwidStatisticsData):
    pass

class DeleteUserAllHwidDeviceRequestDto(BaseModel):
    user_uuid: UUID = Field(serialization_alias="userUuid")
    
class TopUserByHwidDevicesDto(BaseModel):
    """Top user by HWID devices"""
    user_uuid: UUID = Field(alias="userUuid")
    id: int
    username: str
    devices_count: int = Field(alias="devicesCount")


class TopUsersByHwidDevicesData(BaseModel):
    """Top users by HWID devices data"""
    users: list[TopUserByHwidDevicesDto]
    total: int


class GetTopUsersByHwidDevicesResponseDto(TopUsersByHwidDevicesData):
    """Response for get top users by HWID devices"""
    pass

# Legacy aliases for backward compatibility
CreateHWIDUser = CreateUserHwidDeviceRequestDto
HWIDUserResponseDto = HwidDeviceDto
HWIDUserResponseDtoList = HwidDevicesData
HWIDDeleteRequest = DeleteUserHwidDeviceRequestDto