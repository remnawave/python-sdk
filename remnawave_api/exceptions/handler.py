from datetime import datetime

import httpx

from remnawave_api.enums import ErrorCode
from .general import (
    ApiError,
    ApiErrorResponse,
    BadRequestError,
    ConflictError,
    ForbiddenError,
    NotFoundError,
    ServerError,
    UnauthorizedError,
)

ERRORS: dict[str, dict] = {
    ErrorCode.INTERNAL_SERVER_ERROR: ServerError,
    ErrorCode.LOGIN_ERROR: ServerError,
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
    ErrorCode.USER_USERNAME_ALREADY_EXISTS: BadRequestError,
    ErrorCode.USER_SHORT_UUID_ALREADY_EXISTS: BadRequestError,
    ErrorCode.USER_SUBSCRIPTION_UUID_ALREADY_EXISTS: BadRequestError,
    ErrorCode.CREATE_USER_WITH_INBOUNDS_ERROR: ServerError,
    ErrorCode.CANT_GET_CREATED_USER_WITH_INBOUNDS: ServerError,
    ErrorCode.GET_ALL_USERS_ERROR: ServerError,
    ErrorCode.USER_NOT_FOUND: NotFoundError,
    ErrorCode.GET_USER_BY_ERROR: ServerError,
    ErrorCode.REVOKE_USER_SUBSCRIPTION_ERROR: ServerError,
    ErrorCode.DISABLE_USER_ERROR: ServerError,
    ErrorCode.USER_ALREADY_DISABLED: BadRequestError,
    ErrorCode.USER_ALREADY_ENABLED: BadRequestError,
    ErrorCode.ENABLE_USER_ERROR: ServerError,
    ErrorCode.CREATE_NODE_ERROR: ServerError,
    ErrorCode.NODE_NAME_ALREADY_EXISTS: BadRequestError,
    ErrorCode.NODE_ADDRESS_ALREADY_EXISTS: BadRequestError,
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
    ErrorCode.HOST_REMARK_ALREADY_EXISTS: BadRequestError,
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
    ErrorCode.CONFIG_VALIDATION_ERROR: ServerError,
    ErrorCode.USERS_NOT_FOUND: NotFoundError,
    ErrorCode.GET_USER_BY_UNIQUE_FIELDS_NOT_FOUND: NotFoundError,
    ErrorCode.UPDATE_EXCEEDED_TRAFFIC_USERS_ERROR: ServerError,
    ErrorCode.ADMIN_NOT_FOUND: NotFoundError,
    ErrorCode.CREATE_ADMIN_ERROR: ServerError,
    ErrorCode.GET_AUTH_STATUS_ERROR: ServerError,
    ErrorCode.FORBIDDEN_ONE: ForbiddenError,
    ErrorCode.DISABLE_NODE_ERROR: ServerError,
    ErrorCode.GET_ONE_HOST_ERROR: ServerError,
    ErrorCode.SUBSCRIPTION_SETTINGS_NOT_FOUND: NotFoundError,
    ErrorCode.GET_SUBSCRIPTION_SETTINGS_ERROR: ServerError,
    ErrorCode.UPDATE_SUBSCRIPTION_SETTINGS_ERROR: ServerError,
}


def handle_api_error(response: httpx.Response) -> None:
    if response.status_code >= 400:
        try:
            error_data = response.json()
            error_response = ApiErrorResponse(**error_data)

            if error_response.code in ERRORS:
                exception_class = ERRORS[error_response.code]
            else:
                if response.status_code == 400:
                    exception_class = BadRequestError
                elif response.status_code == 401:
                    exception_class = UnauthorizedError
                elif response.status_code == 403:
                    exception_class = ForbiddenError
                elif response.status_code == 404:
                    exception_class = NotFoundError
                elif response.status_code == 409:
                    exception_class = ConflictError
                elif response.status_code >= 500:
                    exception_class = ServerError
                else:
                    exception_class = ApiError

            raise exception_class(response.status_code, error_response)
        except ValueError:
            raise ApiError(
                response.status_code,
                ApiErrorResponse(
                    timestamp=datetime.now(),
                    path=response.request.url.path,
                    message="Unknown error " + response.text,
                    code="UNKNOWN",
                ),
            )
