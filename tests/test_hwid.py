import random
import uuid

import pytest

from remnawave.models import (
    CreateUserHwidDeviceRequestDto,
    DeleteUserHwidDeviceRequestDto,
    DeleteUserAllHwidDeviceRequestDto,
    CreateUserHwidDeviceResponseDto,
    DeleteUserHwidDeviceResponseDto,
    GetUserHwidDevicesResponseDto,
    GetHwidStatisticsResponseDto,
)
from tests.conftest import REMNAWAVE_USER_UUID

new_hwid = str(uuid.uuid4())

@pytest.mark.asyncio
async def test_get_hwid_user(remnawave):
    hwid = await remnawave.hwid.get_hwid_user(uuid=REMNAWAVE_USER_UUID)
    assert isinstance(hwid, GetUserHwidDevicesResponseDto)
    assert hwid.devices is not None


@pytest.mark.asyncio
async def test_get_hwid_users(remnawave):
    response = await remnawave.hwid.get_hwid_users(size=10, start=0)
    assert isinstance(response, GetUserHwidDevicesResponseDto)
    assert hasattr(response, "total")
    assert hasattr(response, "devices")


@pytest.mark.asyncio
async def test_get_hwid_stats(remnawave):
    response = await remnawave.hwid.get_hwid_stats()
    assert isinstance(response, GetHwidStatisticsResponseDto)
    assert hasattr(response, "by_platform")
    assert hasattr(response, "by_app")
    assert hasattr(response, "stats")
    assert hasattr(response.stats, "total_unique_devices")
    assert hasattr(response.stats, "total_hwid_devices")
    assert hasattr(response.stats, "average_hwid_devices_per_user")


@pytest.mark.asyncio
async def test_add_hwid_to_user(remnawave):
    create_request = CreateUserHwidDeviceRequestDto(
        hwid=new_hwid,
        user_uuid=REMNAWAVE_USER_UUID,
        platform="Windows",
        os_version="10.0.19042",
        device_model="Surface Pro",
        user_agent="Mozilla/5.0"
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


@pytest.mark.asyncio
async def test_delete_all_hwid_user(remnawave):
    # Сначала добавим новый HWID
    create_request = CreateUserHwidDeviceRequestDto(
        hwid=str(uuid.uuid4()),
        user_uuid=REMNAWAVE_USER_UUID,
        platform="iOS",
        os_version="15.0",
        device_model="iPhone 13",
        user_agent="Safari/605.1.15"
    )
    await remnawave.hwid.add_hwid_to_users(body=create_request)
    
    # Теперь удалим все HWID устройства пользователя
    delete_all_request = DeleteUserAllHwidDeviceRequestDto(
        user_uuid=REMNAWAVE_USER_UUID
    )
    response = await remnawave.hwid.delete_all_hwid_user(body=delete_all_request)
    
    assert isinstance(response, DeleteUserHwidDeviceResponseDto)
    assert len(response.devices) == 0
    
    # Проверим, что устройства действительно удалены
    hwid_check = await remnawave.hwid.get_hwid_user(uuid=REMNAWAVE_USER_UUID)
    assert len(hwid_check.devices) == 0