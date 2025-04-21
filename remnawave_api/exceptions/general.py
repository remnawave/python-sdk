from datetime import datetime

from pydantic import AliasChoices, BaseModel, Field

from remnawave_api.enums import ErrorCode


class ApiErrorResponse(BaseModel):
    timestamp: datetime = Field(..., description="Время возникновения ошибки")
    path: str = Field(..., description="Путь запроса")
    message: str = Field(..., description="Сообщение об ошибке")
    code: ErrorCode | str = Field(
        ...,
        validation_alias=AliasChoices("errorCode", "code", "error_code"),
        description="Код ошибки",
    )


class ApiError(Exception):
    def __init__(self, status_code: int, error: ApiErrorResponse):
        self.status_code = status_code
        self.error = error
        super().__init__(
            f"API Error {error.code}: {error.message} (HTTP {status_code})"
        )


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


class ServerError(ApiError):
    """Серверная ошибка (500)"""

    pass
