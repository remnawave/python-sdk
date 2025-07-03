from typing import Annotated
from uuid import UUID

from remnawave.models import (
    CreateUserHwidDeviceResponseDto,
    DeleteUserHwidDeviceResponseDto,
    GetUserHwidDevicesResponseDto,
    CreateHWIDUser,
    HWIDDeleteRequest
)
from rapid_api_client import Path, PydanticBody
from remnawave.rapid import AttributeBody, BaseController, post, get


class HWIDUserController(BaseController):
    @post("/hwid/devices", response_class=CreateUserHwidDeviceResponseDto)
    async def add_hwid_to_users(
        self,
        body: Annotated[CreateHWIDUser, PydanticBody()],
    ) -> CreateUserHwidDeviceResponseDto:
        """Create a user HWID device"""
        ...
        
    @post("/hwid/devices/delete", response_class=DeleteUserHwidDeviceResponseDto)
    async def delete_hwid_to_user(
        self,
        body: Annotated[HWIDDeleteRequest, PydanticBody()],
    ) -> DeleteUserHwidDeviceResponseDto:
        """Delete a user HWID device"""
        ...
    
    @get("/hwid/devices/{uuid}", response_class=GetUserHwidDevicesResponseDto)
    async def get_hwid_user(
        self,
        uuid: Annotated[str, Path(description="UUID of the User")],
    ) -> GetUserHwidDevicesResponseDto:
        """Get a user HWID device"""
        ...