from typing import Annotated

from rapid_api_client import Path, Query

from remnawave.enums import ClientType
from remnawave.rapid import BaseController, get
from remnawave.models import GetAllSubscriptionsResponseDto, GetSubscriptionByUsernameResponseDto, GetSubscriptionByShortUUIDResponseDto, GetSubscriptionByUUIDResponseDto


class SubscriptionsController(BaseController):
    @get("/subscriptions", response_class=GetAllSubscriptionsResponseDto)
    async def get_all_subscriptions(
        self,
        start: Annotated[
            int, Query(default=0, ge=0, description="Index to start pagination from")
        ],
        size: Annotated[
            int, Query(default=25, ge=1, description="Number of users per page")
        ],
    ) -> GetAllSubscriptionsResponseDto:
        """None"""
        ...

    @get("/subscriptions/by-username/{username}", response_class=GetSubscriptionByUsernameResponseDto)
    async def get_subscription_by_username(
        self,
        username: Annotated[str, Path(description="Username of the user")],
    ) -> GetSubscriptionByUsernameResponseDto:
        """None"""
        ...
        
    @get("/subscriptions/by-short-uuid/{short_uuid}", response_class=GetSubscriptionByShortUUIDResponseDto)
    async def get_subscription_by_short_uuid(
        self,
        short_uuid: Annotated[str, Path(description="Short UUID of the subscription")],
    ) -> GetSubscriptionByShortUUIDResponseDto:
        """None"""
        ...
        
    @get("/subscriptions/by-uuid/{uuid}", response_class=GetSubscriptionByUUIDResponseDto)
    async def get_subscription_by_uuid(
        self,
        uuid: Annotated[str, Path(description="UUID of the user")],
    ) -> GetSubscriptionByUUIDResponseDto:
        """None"""
        ...