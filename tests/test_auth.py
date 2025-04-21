import pytest

from remnawave_api.models import LoginRequestDto, LoginResponseDto
from tests.conftest import REMNAWAVE_ADMIN_PASSWORD, REMNAWAVE_ADMIN_USERNAME


@pytest.mark.asyncio
async def test_auth(remnawave):
    login = await remnawave.auth.login(
        LoginRequestDto(
            username=REMNAWAVE_ADMIN_USERNAME,
            password=REMNAWAVE_ADMIN_PASSWORD,
        )
    )
    assert isinstance(login, LoginResponseDto)
