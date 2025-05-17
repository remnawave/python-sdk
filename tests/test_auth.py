import pytest

from remnawave_api.models import LoginRequestDto, LoginResponseDto, LoginTelegramRequestDto
from remnawave_api.exceptions import ForbiddenError, ApiError
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

    try:
        telegram_login = await remnawave.auth.oauth2_tg_callback(
            LoginTelegramRequestDto(
                id=123456789,
                first_name="Test",
                last_name="User",
                username="testuser",
                photo_url="https://example.com/photo.jpg",
                auth_date=1234567890,
                hash="examplehash",
            )
        )
        pytest.fail("Expected 403 error, but got successful response")
    except ForbiddenError as e:
        assert e.status_code == 403, f"Expected 403, got {e.status_code}"
        print(f"Получено ожидаемое исключение: {e}")
    except ApiError as e:
        pytest.fail(f"Неожиданное исключение: {e}")