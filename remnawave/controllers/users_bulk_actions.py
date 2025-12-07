from typing import Annotated, List
from uuid import UUID

from rapid_api_client.annotations import PydanticBody

from remnawave.enums import UserStatus
from remnawave.models import (
    BulkAllExtendExpirationDateRequestDto,
    BulkAllExtendExpirationDateResponseDto,
    BulkAllResetTrafficUsersResponseDto,
    BulkAllUpdateUsersRequestDto,
    BulkAllUpdateUsersResponseDto,
    BulkDeleteUsersByStatusRequestDto,
    BulkDeleteUsersByStatusResponseDto,
    BulkDeleteUsersRequestDto,
    BulkDeleteUsersResponseDto,
    BulkExtendExpirationDateRequestDto,
    BulkExtendExpirationDateResponseDto,
    BulkResetTrafficUsersRequestDto,
    BulkResetTrafficUsersResponseDto,
    BulkRevokeUsersSubscriptionRequestDto,
    BulkRevokeUsersSubscriptionResponseDto,
    BulkUpdateUsersRequestDto,
    BulkUpdateUsersResponseDto,
    BulkUpdateUsersSquadsRequestDto,
    BulkUpdateUsersSquadsResponseDto,
)
from remnawave.rapid import BaseController, post


class UsersBulkActionsController(BaseController):
    @post(
        "/users/bulk/delete-by-status",
        response_class=BulkDeleteUsersByStatusResponseDto,
    )
    async def bulk_delete_users_by_status(
        self, 
        body: Annotated[BulkDeleteUsersByStatusRequestDto, PydanticBody()]
    ) -> BulkDeleteUsersByStatusResponseDto:
        """Bulk Delete Users By Status"""
        ...

    @post("/users/bulk/delete", response_class=BulkDeleteUsersResponseDto)
    async def bulk_delete_users(
        self,
        body: Annotated[BulkDeleteUsersRequestDto, PydanticBody()],
    ) -> BulkDeleteUsersResponseDto:
        """Bulk Delete Users By UUIDs"""
        ...

    @post(
        "/users/bulk/revoke-subscription",
        response_class=BulkRevokeUsersSubscriptionResponseDto,
    )
    async def bulk_revoke_users_subscription(
        self,
        body: Annotated[BulkRevokeUsersSubscriptionRequestDto, PydanticBody()],
    ) -> BulkRevokeUsersSubscriptionResponseDto:
        """Bulk Revoke Users Subscription"""
        ...

    @post("/users/bulk/reset-traffic", response_class=BulkResetTrafficUsersResponseDto)
    async def bulk_reset_user_traffic(
        self,
        body: Annotated[BulkResetTrafficUsersRequestDto, PydanticBody()],
    ) -> BulkResetTrafficUsersResponseDto:
        """Bulk Reset User Traffic"""
        ...

    @post("/users/bulk/update", response_class=BulkUpdateUsersResponseDto)
    async def bulk_update_users(
        self,
        body: Annotated[BulkUpdateUsersRequestDto, PydanticBody()],
    ) -> BulkUpdateUsersResponseDto:
        """Bulk Update Users"""
        ...

    @post("/users/bulk/update-squads", response_class=BulkUpdateUsersSquadsResponseDto)
    async def bulk_update_users_internal_squads(
        self,
        body: Annotated[BulkUpdateUsersSquadsRequestDto, PydanticBody()],
    ) -> BulkUpdateUsersSquadsResponseDto:
        """Bulk Update Users Internal Squads"""
        ...

    @post(
        "/users/bulk/extend-expiration-date",
        response_class=BulkExtendExpirationDateResponseDto,
    )
    async def bulk_extend_expiration_date(
        self,
        body: Annotated[BulkExtendExpirationDateRequestDto, PydanticBody()],
    ) -> BulkExtendExpirationDateResponseDto:
        """Bulk Extend Users Expiration Date"""
        ...

    @post("/users/bulk/all/update", response_class=BulkAllUpdateUsersResponseDto)
    async def bulk_update_all_users(
        self,
        body: Annotated[BulkAllUpdateUsersRequestDto, PydanticBody()],
    ) -> BulkAllUpdateUsersResponseDto:
        """Bulk Update All Users"""
        ...

    @post(
        "/users/bulk/all/reset-traffic",
        response_class=BulkAllResetTrafficUsersResponseDto,
    )
    async def bulk_all_reset_user_traffic(
        self,
    ) -> BulkAllResetTrafficUsersResponseDto:
        """Bulk Reset All Users Traffic"""
        ...

    @post(
        "/users/bulk/all/extend-expiration-date",
        response_class=BulkAllExtendExpirationDateResponseDto,
    )
    async def bulk_all_extend_expiration_date(
        self,
        body: Annotated[BulkAllExtendExpirationDateRequestDto, PydanticBody()],
    ) -> BulkAllExtendExpirationDateResponseDto:
        """Bulk Extend All Users Expiration Date"""
        ...