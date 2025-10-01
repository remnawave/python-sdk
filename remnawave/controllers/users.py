from typing import Annotated, Optional

from rapid_api_client import Path, Query
from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    CreateUserRequestDto,
    DeleteUserResponseDto,
    EmailUserResponseDto,
    GetUserAccessibleNodesResponseDto,
    TelegramUserResponseDto,
    UpdateUserRequestDto,
    UserResponseDto,
    UsersResponseDto,
    TagsResponseDto,
    TagUserResponseDto,
    RevokeUserRequestDto,
    GetSubscriptionRequestsResponseDto
)
from remnawave.rapid import BaseController, delete, get, patch, post


class UsersController(BaseController):
    @post("/users", response_class=UserResponseDto)
    async def create_user(
        self,
        body: Annotated[CreateUserRequestDto, PydanticBody()],
    ) -> UserResponseDto:
        """Create User"""
        ...

    @patch("/users", response_class=UserResponseDto)
    async def update_user(
        self,
        body: Annotated[UpdateUserRequestDto, PydanticBody()],
    ) -> UserResponseDto:
        """Update User"""
        ...

    @get("/users", response_class=UsersResponseDto)
    async def get_all_users_v2(
        self,
        start: Annotated[
            int, Query(default=0, ge=0, description="Index to start pagination from")
        ],
        size: Annotated[
            int, Query(default=25, ge=1, description="Number of users per page")
        ],
    ) -> UsersResponseDto:
        """
        Get users page from the end.

        Args:
            page (int): Page number from the end (1 = last page).
            size (int): Number of users per page.

        Returns:
            UsersResponseDto
        """
        ...

    @delete("/users/{uuid}", response_class=DeleteUserResponseDto)
    async def delete_user(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
    ) -> DeleteUserResponseDto:
        """Delete User"""
        ...

    @post("users/{uuid}/actions/revoke", response_class=UserResponseDto)
    async def revoke_user_subscription(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
        body: Optional[Annotated[RevokeUserRequestDto, PydanticBody()]] = None,
    ) -> UserResponseDto:
        """Revoke User Subscription"""
        ...

    @post("/users/{uuid}/actions/disable", response_class=UserResponseDto)
    async def disable_user(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
    ) -> UserResponseDto:
        """Disable User"""
        ...

    @post("/users/{uuid}/actions/enable", response_class=UserResponseDto)
    async def enable_user(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
    ) -> UserResponseDto:
        """Enable User"""
        ...

    @post("/users/{uuid}/actions/reset-traffic", response_class=UserResponseDto)
    async def reset_user_traffic(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
    ) -> UserResponseDto:
        """Reset User Traffic"""
        ...

    @get("/users/by-short-uuid/{short_uuid}", response_class=UserResponseDto)
    async def get_user_by_short_uuid(
        self,
        short_uuid: Annotated[str, Path(description="Short UUID of the user")],
    ) -> UserResponseDto:
        """Get User By Short UUID"""
        ...

    @get(
        "/users/by-subscription-uuid/{subscription_uuid}",
        response_class=UserResponseDto,
    )
    async def get_user_by_subscription_uuid(
        self,
        subscription_uuid: Annotated[str, Path(description="UUID of the subscription")],
    ) -> UserResponseDto:
        """Get User By Subscription UUID"""
        ...

    @get("/users/{uuid}", response_class=UserResponseDto)
    async def get_user_by_uuid(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
    ) -> UserResponseDto:
        """Get User By UUID"""
        ...

    @get("/users/by-username/{username}", response_class=UserResponseDto)
    async def get_user_by_username(
        self,
        username: Annotated[str, Path(description="Username of the user")],
    ) -> UserResponseDto:
        """Get User By Username"""
        ...

    @get(
        "/users/by-telegram-id/{telegram_id}",
        response_class=TelegramUserResponseDto,
    )
    async def get_users_by_telegram_id(
        self,
        telegram_id: Annotated[str, Path(description="Telegram ID of the user")],
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

    @get("/users/tags", response_class=TagsResponseDto)
    async def get_all_tags(
        self,
    ) -> TagsResponseDto:
        """Get All Tags"""
        ...

    @get(
        "/users/{uuid}/accessible-nodes",
        response_class=GetUserAccessibleNodesResponseDto,
    )
    async def get_user_accessible_nodes(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
    ) -> GetUserAccessibleNodesResponseDto:
        """Get User Accessible Nodes"""
        ...

    @get("/users/{uuid}/subscription-request-history", response_class=GetSubscriptionRequestsResponseDto)
    async def get_subscription_requests(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
    ) -> GetSubscriptionRequestsResponseDto:
        """Get Subscription Requests History"""
        ...