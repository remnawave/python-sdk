import random
import uuid

import pytest

from remnawave.models import (
    CreateUserHwidDeviceRequestDto,
    DeleteUserHwidDeviceRequestDto,
    CreateUserHwidDeviceResponseDto,
    DeleteUserHwidDeviceResponseDto,
    GetUserHwidDevicesResponseDto,
)
from tests.conftest import REMNAWAVE_USER_UUID

new_hwid = str(uuid.uuid4())

@pytest.mark.asyncio
async def test_get_hwid_user(remnawave):
    hwid = await remnawave.hwid.get_hwid_user(uuid=REMNAWAVE_USER_UUID)
    assert isinstance(hwid, GetUserHwidDevicesResponseDto)
    assert hwid.devices is not None


@pytest.mark.asyncio
async def test_add_hwid_to_user(remnawave):
    create_request = CreateUserHwidDeviceRequestDto(
        hwid=new_hwid,
        user_uuid=REMNAWAVE_USER_UUID,
        platform="Windows",
        os_version="10.0.19042",
        deviceModel="Surface Pro",
        userAgent="Mozilla/5.0"
    )
    response = await remnawave.hwid.add_hwid_to_users(body=create_request)
    assert isinstance(response, CreateUserHwidDeviceResponseDto)
    assert any(item.hwid == new_hwid for item in response.devices)


@pytest.mark.asyncio
async def test_delete_hwid_user(remnawave):
    delete_request = DeleteUserHwidDeviceRequestDto(
        hwid=new_hwid,
        user_uuid=REMNAWAVE_USER_UUID
    )
    response = await remnawave.hwid.delete_hwid_to_user(body=delete_request)
    assert isinstance(response, DeleteUserHwidDeviceResponseDto)
    assert not any(item.hwid == new_hwid for item in response.devices)
