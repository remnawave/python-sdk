from datetime import datetime
from typing import Dict, Type

import httpx

from remnawave.enums import ErrorCode
from .general import (
    ApiError,
    ApiErrorResponse,
    BadRequestError,
    ConflictError,
    ForbiddenError,
    NotFoundError,
    ServerError,
    UnauthorizedError,
    ValidationError,
    NetworkError,
    AuthenticationError,
    BusinessLogicError,
)

ERRORS: Dict[str, Type[ApiError]] = {
    ErrorCode.INTERNAL_SERVER_ERROR: ServerError,
    ErrorCode.LOGIN_ERROR: AuthenticationError,
    ErrorCode.UNAUTHORIZED: UnauthorizedError,
    ErrorCode.FORBIDDEN_ROLE_ERROR: ForbiddenError,
    ErrorCode.CREATE_API_TOKEN_ERROR: ServerError,
    ErrorCode.DELETE_API_TOKEN_ERROR: ServerError,
    ErrorCode.REQUESTED_TOKEN_NOT_FOUND: NotFoundError,
    ErrorCode.FIND_ALL_API_TOKENS_ERROR: ServerError,
    ErrorCode.GET_PUBLIC_KEY_ERROR: ServerError,
    ErrorCode.ENABLE_NODE_ERROR: ServerError,
    ErrorCode.NODE_NOT_FOUND: NotFoundError,
    ErrorCode.CONFIG_NOT_FOUND: NotFoundError,
    ErrorCode.UPDATE_CONFIG_ERROR: ServerError,
    ErrorCode.GET_CONFIG_ERROR: ServerError,
    ErrorCode.DELETE_MANY_INBOUNDS_ERROR: ServerError,
    ErrorCode.CREATE_MANY_INBOUNDS_ERROR: ServerError,
    ErrorCode.FIND_ALL_INBOUNDS_ERROR: ServerError,
    ErrorCode.CREATE_USER_ERROR: ServerError,
    ErrorCode.USER_USERNAME_ALREADY_EXISTS: ConflictError,
    ErrorCode.USER_SHORT_UUID_ALREADY_EXISTS: ConflictError,
    ErrorCode.USER_SUBSCRIPTION_UUID_ALREADY_EXISTS: ConflictError,
    ErrorCode.CREATE_USER_WITH_INBOUNDS_ERROR: ServerError,
    ErrorCode.CANT_GET_CREATED_USER_WITH_INBOUNDS: ServerError,
    ErrorCode.GET_ALL_USERS_ERROR: ServerError,
    ErrorCode.USER_NOT_FOUND: NotFoundError,
    ErrorCode.GET_USER_BY_ERROR: ServerError,
    ErrorCode.REVOKE_USER_SUBSCRIPTION_ERROR: ServerError,
    ErrorCode.DISABLE_USER_ERROR: ServerError,
    ErrorCode.USER_ALREADY_DISABLED: ConflictError,
    ErrorCode.USER_ALREADY_ENABLED: ConflictError,
    ErrorCode.ENABLE_USER_ERROR: ServerError,
    ErrorCode.CREATE_NODE_ERROR: ServerError,
    ErrorCode.NODE_NAME_ALREADY_EXISTS: ConflictError,
    ErrorCode.NODE_ADDRESS_ALREADY_EXISTS: ConflictError,
    ErrorCode.NODE_ERROR_WITH_MSG: ServerError,
    ErrorCode.NODE_ERROR_500_WITH_MSG: ServerError,
    ErrorCode.RESTART_NODE_ERROR: ServerError,
    ErrorCode.GET_CONFIG_WITH_USERS_ERROR: ServerError,
    ErrorCode.DELETE_USER_ERROR: ServerError,
    ErrorCode.UPDATE_NODE_ERROR: ServerError,
    ErrorCode.UPDATE_USER_ERROR: ServerError,
    ErrorCode.INCREMENT_USED_TRAFFIC_ERROR: ServerError,
    ErrorCode.GET_ALL_NODES_ERROR: ServerError,
    ErrorCode.GET_ONE_NODE_ERROR: ServerError,
    ErrorCode.DELETE_NODE_ERROR: ServerError,
    ErrorCode.CREATE_HOST_ERROR: ServerError,
    ErrorCode.HOST_REMARK_ALREADY_EXISTS: ConflictError,
    ErrorCode.HOST_NOT_FOUND: NotFoundError,
    ErrorCode.DELETE_HOST_ERROR: ServerError,
    ErrorCode.GET_USER_STATS_ERROR: ServerError,
    ErrorCode.UPDATE_USER_WITH_INBOUNDS_ERROR: ServerError,
    ErrorCode.GET_ALL_HOSTS_ERROR: ServerError,
    ErrorCode.REORDER_HOSTS_ERROR: ServerError,
    ErrorCode.UPDATE_HOST_ERROR: ServerError,
    ErrorCode.CREATE_CONFIG_ERROR: ServerError,
    ErrorCode.ENABLED_NODES_NOT_FOUND: ConflictError,
    ErrorCode.GET_NODES_USAGE_BY_RANGE_ERROR: ServerError,
    ErrorCode.RESET_USER_TRAFFIC_ERROR: ServerError,
    ErrorCode.REORDER_NODES_ERROR: ServerError,
    ErrorCode.GET_ALL_INBOUNDS_ERROR: ServerError,
    ErrorCode.BULK_DELETE_USERS_BY_STATUS_ERROR: ServerError,
    ErrorCode.UPDATE_INBOUND_ERROR: ServerError,
    ErrorCode.CONFIG_VALIDATION_ERROR: ValidationError,
    ErrorCode.USERS_NOT_FOUND: NotFoundError,
    ErrorCode.GET_USER_BY_UNIQUE_FIELDS_NOT_FOUND: NotFoundError,
    ErrorCode.UPDATE_EXCEEDED_TRAFFIC_USERS_ERROR: ServerError,
    ErrorCode.ADMIN_NOT_FOUND: NotFoundError,
    ErrorCode.CREATE_ADMIN_ERROR: ServerError,
    ErrorCode.GET_AUTH_STATUS_ERROR: ServerError,
    ErrorCode.FORBIDDEN_ONE: ForbiddenError,
    ErrorCode.FORBIDDEN_TWO: ForbiddenError,
    ErrorCode.DISABLE_NODE_ERROR: ServerError,
    ErrorCode.GET_ONE_HOST_ERROR: ServerError,
    ErrorCode.SUBSCRIPTION_SETTINGS_NOT_FOUND: NotFoundError,
    ErrorCode.GET_SUBSCRIPTION_SETTINGS_ERROR: ServerError,
    ErrorCode.UPDATE_SUBSCRIPTION_SETTINGS_ERROR: ServerError,
    
    ErrorCode.CREATE_SUBSCRIPTION_TEMPLATE_ERROR: ServerError,
    ErrorCode.SUBSCRIPTION_TEMPLATE_NOT_FOUND: NotFoundError,
    ErrorCode.UPDATE_SUBSCRIPTION_TEMPLATE_ERROR: ServerError,
    ErrorCode.DELETE_SUBSCRIPTION_TEMPLATE_ERROR: ServerError,
    ErrorCode.GET_SUBSCRIPTION_TEMPLATE_ERROR: ServerError,
    
    ErrorCode.CREATE_INBOUND_ERROR: ServerError,
    ErrorCode.DELETE_INBOUND_ERROR: ServerError,
    ErrorCode.GET_INBOUND_ERROR: ServerError,
    ErrorCode.INBOUND_NOT_FOUND: NotFoundError,
    ErrorCode.INBOUND_TAG_ALREADY_EXISTS: ConflictError,
    
    ErrorCode.CREATE_EXTERNAL_SQUAD_ERROR: ServerError,
    ErrorCode.EXTERNAL_SQUAD_NOT_FOUND: NotFoundError,
    ErrorCode.UPDATE_EXTERNAL_SQUAD_ERROR: ServerError,
    ErrorCode.DELETE_EXTERNAL_SQUAD_ERROR: ServerError,
    ErrorCode.EXTERNAL_SQUAD_NAME_ALREADY_EXISTS: ConflictError,
    ErrorCode.ADD_USERS_TO_EXTERNAL_SQUAD_ERROR: ServerError,
    ErrorCode.REMOVE_USERS_FROM_EXTERNAL_SQUAD_ERROR: ServerError,
    ErrorCode.GET_EXTERNAL_SQUAD_ERROR: ServerError,
    ErrorCode.GET_ALL_EXTERNAL_SQUADS_ERROR: ServerError,
    
    ErrorCode.CREATE_INTERNAL_SQUAD_ERROR: ServerError,
    ErrorCode.INTERNAL_SQUAD_NOT_FOUND: NotFoundError,
    ErrorCode.UPDATE_INTERNAL_SQUAD_ERROR: ServerError,
    ErrorCode.DELETE_INTERNAL_SQUAD_ERROR: ServerError,
    ErrorCode.INTERNAL_SQUAD_NAME_ALREADY_EXISTS: ConflictError,
    ErrorCode.GET_INTERNAL_SQUAD_ERROR: ServerError,
    ErrorCode.GET_ALL_INTERNAL_SQUADS_ERROR: ServerError,
    
    ErrorCode.CREATE_SNIPPET_ERROR: ServerError,
    ErrorCode.SNIPPET_NOT_FOUND: NotFoundError,
    ErrorCode.UPDATE_SNIPPET_ERROR: ServerError,
    ErrorCode.DELETE_SNIPPET_ERROR: ServerError,
    ErrorCode.SNIPPET_NAME_ALREADY_EXISTS: ConflictError,
    ErrorCode.GET_SNIPPET_ERROR: ServerError,
    ErrorCode.GET_ALL_SNIPPETS_ERROR: ServerError,
    
    # Валидационные ошибки
    ErrorCode.VALIDATION_ERROR: ValidationError,
    ErrorCode.INVALID_UUID_FORMAT: ValidationError,
    ErrorCode.INVALID_EMAIL_FORMAT: ValidationError,
    ErrorCode.INVALID_DATE_FORMAT: ValidationError,
    ErrorCode.REQUIRED_FIELD_MISSING: ValidationError,
    ErrorCode.FIELD_TOO_LONG: ValidationError,
    ErrorCode.FIELD_TOO_SHORT: ValidationError,
    ErrorCode.INVALID_ENUM_VALUE: ValidationError,
    ErrorCode.INVALID_REGEX_PATTERN: ValidationError,
    ErrorCode.NUMERIC_VALIDATION_ERROR: ValidationError,
    
    # Сетевые ошибки
    ErrorCode.NETWORK_ERROR: NetworkError,
    ErrorCode.TIMEOUT_ERROR: NetworkError,
    ErrorCode.CONNECTION_ERROR: NetworkError,
    ErrorCode.DNS_ERROR: NetworkError,
    ErrorCode.SSL_ERROR: NetworkError,
    
    # Ошибки аутентификации
    ErrorCode.INVALID_TOKEN: AuthenticationError,
    ErrorCode.TOKEN_EXPIRED: AuthenticationError,
    ErrorCode.INVALID_CREDENTIALS: AuthenticationError,
    ErrorCode.TWO_FACTOR_REQUIRED: AuthenticationError,
    ErrorCode.ACCOUNT_LOCKED: AuthenticationError,
    ErrorCode.PASSWORD_COMPLEXITY_ERROR: ValidationError,
    
    # Бизнес-логика
    ErrorCode.TRAFFIC_LIMIT_EXCEEDED: BusinessLogicError,
    ErrorCode.USER_LIMIT_EXCEEDED: BusinessLogicError,
    ErrorCode.SUBSCRIPTION_EXPIRED: BusinessLogicError,
    ErrorCode.FEATURE_NOT_AVAILABLE: BusinessLogicError,
    ErrorCode.QUOTA_EXCEEDED: BusinessLogicError,
    ErrorCode.RESOURCE_LOCKED: ConflictError,
    
    # Системные ошибки
    ErrorCode.SYSTEM_STATS_ERROR: ServerError,
    ErrorCode.SYSTEM_HEALTH_ERROR: ServerError,
    ErrorCode.NODES_METRICS_ERROR: ServerError,
    ErrorCode.X25519_KEYGEN_ERROR: ServerError,
    ErrorCode.HAPP_CRYPTO_ERROR: ServerError,
    ErrorCode.SRR_MATCHER_ERROR: ServerError,
    
    # Настройки Remnawave
    ErrorCode.GET_REMNAWAVE_SETTINGS_ERROR: ServerError,
    ErrorCode.UPDATE_REMNAWAVE_SETTINGS_ERROR: ServerError,
    ErrorCode.OAUTH_ERROR: AuthenticationError,
    ErrorCode.PASSKEY_SETTINGS_ERROR: ServerError,
    ErrorCode.TELEGRAM_AUTH_ERROR: AuthenticationError,
    ErrorCode.BRANDING_SETTINGS_ERROR: ServerError,
}


def handle_api_error(response: httpx.Response) -> None:
    """Handle API error responses and raise appropriate exceptions"""
    if response.status_code >= 400:
        try:
            error_data = response.json()
            error_response = ApiErrorResponse(**error_data)
            
            # Fill missing fields for API v2 format
            if error_response.timestamp is None:
                error_response.timestamp = datetime.now()
            if error_response.path is None:
                error_response.path = str(response.request.url.path)
            if error_response.code is None:
                # Use status_code or default to UNKNOWN
                if error_response.status_code:
                    error_response.code = f"HTTP_{error_response.status_code}"
                else:
                    error_response.code = "UNKNOWN"

            # Map error code to exception class
            if error_response.code in ERRORS:
                exception_class = ERRORS[error_response.code]
            else:
                # Fallback based on HTTP status code
                exception_class = _get_exception_by_status_code(response.status_code)

            raise exception_class(response.status_code, error_response)
            
        except ValueError:
            # JSON parsing failed, create generic error
            raise ApiError(
                response.status_code,
                ApiErrorResponse(
                    timestamp=datetime.now(),
                    path=str(response.request.url.path),
                    message=f"Unknown error: {response.text}",
                    code="UNKNOWN",
                    status_code=response.status_code,
                ),
            )


def _get_exception_by_status_code(status_code: int) -> Type[ApiError]:
    """Get exception class based on HTTP status code"""
    if status_code == 400:
        return BadRequestError
    elif status_code == 401:
        return UnauthorizedError
    elif status_code == 403:
        return ForbiddenError
    elif status_code == 404:
        return NotFoundError
    elif status_code == 409:
        return ConflictError
    elif status_code == 422:
        return ValidationError
    elif status_code == 429:
        return BadRequestError  # Rate limit
    elif status_code >= 500:
        return ServerError
    else:
        return ApiError