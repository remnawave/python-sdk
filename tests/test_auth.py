import pytest

from remnawave.models import (
    LoginRequestDto, 
    LoginResponseDto, 
    LoginTelegramRequestDto,
    TelegramCallbackRequestDto,
)
from remnawave.exceptions import ForbiddenError, ApiError
from tests.conftest import REMNAWAVE_ADMIN_PASSWORD, REMNAWAVE_ADMIN_USERNAME


class TestAuthentication:
    """Тесты для проверки функциональности аутентификации"""
    
    @pytest.mark.asyncio
    async def test_login_with_credentials(self, remnawave):
        """Тест базовой аутентификации по имени пользователя и паролю"""
        login = await remnawave.auth.login(
            LoginRequestDto(
                username=REMNAWAVE_ADMIN_USERNAME,
                password=REMNAWAVE_ADMIN_PASSWORD,
            )
        )
        assert isinstance(login, LoginResponseDto)
        assert login.access_token is not None
        # Проверяем наличие токена, но не обращаемся к полю user,
        # так как в текущей версии API это поле не возвращается
        assert login.access_token.startswith("eyJ")  # JWT token всегда начинается с eyJ

    @pytest.mark.asyncio
    async def test_login_with_invalid_credentials(self, remnawave):
        """Тест аутентификации с неверными учетными данными"""
        try:
            await remnawave.auth.login(
                LoginRequestDto(
                    username="invalid_username",
                    password="invalid_password",
                )
            )
            pytest.fail("Expected authentication error for invalid credentials")
        except ApiError as e:
            assert e.status_code in [401, 403], f"Expected 401 or 403, got {e.status_code}"