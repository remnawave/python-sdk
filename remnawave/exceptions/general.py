from datetime import datetime
from typing import Any, List, Optional

from pydantic import AliasChoices, BaseModel, Field

from remnawave.enums import ErrorCode


class ApiErrorResponse(BaseModel):
    """Standard API error response model"""
    timestamp: Optional[datetime] = Field(None, description="Время возникновения ошибки")
    path: Optional[str] = Field(None, description="Путь запроса")
    message: str = Field(..., description="Сообщение об ошибке")
    code: Optional[ErrorCode | str] = Field(
        None,
        validation_alias=AliasChoices("errorCode", "code", "error_code"),
        description="Код ошибки",
    )
    # Support for API v2 error format
    status_code: Optional[int] = Field(None, alias="statusCode")
    errors: Optional[List[Any]] = Field(None, description="Детали ошибок валидации")


class ApiError(Exception):
    """Base API error exception"""
    
    def __init__(self, status_code: int, error: ApiErrorResponse):
        self.status_code = status_code
        self.error = error
        super().__init__(
            f"API Error {error.code}: {error.message} (HTTP {status_code})"
        )

    @property
    def code(self) -> Optional[str]:
        """Get error code"""
        return self.error.code

    @property
    def message(self) -> str:
        """Get error message"""
        return self.error.message

    @property
    def timestamp(self) -> Optional[datetime]:
        """Get error timestamp"""
        return self.error.timestamp

    @property
    def path(self) -> Optional[str]:
        """Get request path"""
        return self.error.path


class BadRequestError(ApiError):
    """Ошибки клиента (400)"""
    pass


class UnauthorizedError(ApiError):
    """Ошибка авторизации (401)"""
    pass


class ForbiddenError(ApiError):
    """Доступ запрещен (403)"""
    pass


class NotFoundError(ApiError):
    """Ресурс не найден (404)"""
    pass


class ConflictError(ApiError):
    """Конфликт (409)"""
    pass


class ValidationError(ApiError):
    """Ошибка валидации данных (422)"""
    pass


class ServerError(ApiError):
    """Серверная ошибка (500+)"""
    pass


# Новые специализированные исключения
class NetworkError(ApiError):
    """Сетевые ошибки"""
    pass


class AuthenticationError(ApiError):
    """Ошибки аутентификации"""
    pass


class BusinessLogicError(ApiError):
    """Ошибки бизнес-логики"""
    pass


class RateLimitError(BadRequestError):
    """Превышен лимит запросов"""
    pass


class MaintenanceError(ServerError):
    """Режим обслуживания"""
    pass


class QuotaExceededError(BusinessLogicError):
    """Превышена квота"""
    pass


class FeatureNotAvailableError(BusinessLogicError):
    """Функция недоступна"""
    pass