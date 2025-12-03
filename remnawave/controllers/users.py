from typing import Annotated, Optional

from rapid_api_client import Path, Query
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    CreateUserRequestDto,
    CreateUserResponseDto,
    DeleteUserResponseDto,
    GetAllUsersResponseDto,
    GetAllTagsResponseDto,
    GetUserByIdResponseDto,
    GetUserByShortUuidResponseDto,
    GetUserByUsernameResponseDto,
    GetUserByUuidResponseDto,
    GetUserAccessibleNodesResponseDto,
    GetUserSubscriptionRequestHistoryResponseDto,
    TelegramUserResponseDto,
    EmailUserResponseDto,
    TagUserResponseDto,
    UpdateUserRequestDto,
    UpdateUserResponseDto,
    RevokeUserRequestDto,
)
from remnawave.rapid import BaseController, delete, get, patch, post


class UsersController(BaseController):
    @post("/users", response_class=CreateUserResponseDto)
    async def create_user(
        self,
        body: Annotated[CreateUserRequestDto, PydanticBody()],
    ) -> CreateUserResponseDto:
        """Create a new user"""
        ...

    @patch("/users", response_class=UpdateUserResponseDto)
    async def update_user(
        self,
        body: Annotated[UpdateUserRequestDto, PydanticBody()],
    ) -> UpdateUserResponseDto:
        """Update a user by UUID or username"""
        ...

    @get("/users", response_class=GetAllUsersResponseDto)
    async def get_all_users(
        self,
        start: Annotated[
            Optional[int], 
            Query(default=None, description="Offset for pagination")
        ] = None,
        size: Annotated[
            Optional[int], 
            Query(default=None, description="Page size for pagination")
        ] = None,
    ) -> GetAllUsersResponseDto:
        """Get all users"""
        ...

    @delete("/users/{uuid}", response_class=DeleteUserResponseDto)
    async def delete_user(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
    ) -> DeleteUserResponseDto:
        """Delete user"""
        ...

    @post("/users/{uuid}/actions/revoke", response_class=UpdateUserResponseDto)
    async def revoke_user_subscription(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
        body: Optional[Annotated[RevokeUserRequestDto, PydanticBody()]] = None,
    ) -> UpdateUserResponseDto:
        """Revoke User Subscription"""
        ...

    @post("/users/{uuid}/actions/disable", response_class=UpdateUserResponseDto)
    async def disable_user(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
    ) -> UpdateUserResponseDto:
        """Disable User"""
        ...

    @post("/users/{uuid}/actions/enable", response_class=UpdateUserResponseDto)
    async def enable_user(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
    ) -> UpdateUserResponseDto:
        """Enable User"""
        ...

    @post("/users/{uuid}/actions/reset-traffic", response_class=UpdateUserResponseDto)
    async def reset_user_traffic(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
    ) -> UpdateUserResponseDto:
        """Reset User Traffic"""
        ...

    @get("/users/{uuid}", response_class=GetUserByUuidResponseDto)
    async def get_user_by_uuid(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
    ) -> GetUserByUuidResponseDto:
        """Get user by UUID"""
        ...

    @get("/users/tags", response_class=GetAllTagsResponseDto)
    async def get_all_tags(
        self,
    ) -> GetAllTagsResponseDto:
        """Get all existing user tags"""
        ...

    @get(
        "/users/{uuid}/accessible-nodes",
        response_class=GetUserAccessibleNodesResponseDto,
    )
    async def get_user_accessible_nodes(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
    ) -> GetUserAccessibleNodesResponseDto:
        """Get user accessible nodes"""
        ...

    @get(
        "/users/{uuid}/subscription-request-history", 
        response_class=GetUserSubscriptionRequestHistoryResponseDto
    )
    async def get_user_subscription_request_history(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
    ) -> GetUserSubscriptionRequestHistoryResponseDto:
        """Get user subscription request history, recent 24 records"""
        ...

    # ИСПРАВЛЕНО: убран alias, используется short_uuid
    @get("/users/by-short-uuid/{shortUuid}", response_class=GetUserByShortUuidResponseDto)
    async def get_user_by_short_uuid(
        self,
        short_uuid: Annotated[str, Path(description="Short UUID of the user", alias="shortUuid")],
    ) -> GetUserByShortUuidResponseDto:
        """Get user by Short UUID"""
        ...

    @get("/users/by-username/{username}", response_class=GetUserByUsernameResponseDto)
    async def get_user_by_username(
        self,
        username: Annotated[str, Path(description="Username of the user")],
    ) -> GetUserByUsernameResponseDto:
        """Get user by username"""
        ...

    @get("/users/by-id/{id}", response_class=GetUserByIdResponseDto)
    async def get_user_by_id(
        self,
        id: Annotated[str, Path(description="ID of the user")],
    ) -> GetUserByIdResponseDto:
        """Get user by ID"""
        ...

    # ИСПРАВЛЕНО: убран alias, используется telegram_id
    @get(
        "/users/by-telegram-id/{telegramId}",
        response_class=TelegramUserResponseDto,
    )
    async def get_users_by_telegram_id(
        self,
        telegram_id: Annotated[str, Path(description="Telegram ID of the user", alias="telegramId")],
    ) -> TelegramUserResponseDto:
        """Get Users By Telegram ID"""
        ...

    @get("/users/by-email/{email}", response_class=EmailUserResponseDto)
    async def get_users_by_email(
        self,
        email: Annotated[str, Path(description="Email of the user")],
    ) -> EmailUserResponseDto:
        """Get Users By Email"""
        ...

    @get("/users/by-tag/{tag}", response_class=TagUserResponseDto)
    async def get_users_by_tag(
        self,
        tag: Annotated[str, Path(description="Tag of the user")],
    ) -> TagUserResponseDto:
        """Get Users By Tag"""
        ...