from typing import Annotated

from rapid_api_client import Path, Query
from rapid_api_client.annotations import PydanticBody

from remnawave.enums import ClientType
from remnawave.models.subscription import GetRawSubscriptionByShortUuidResponseDto
from remnawave.rapid import BaseController, get
from remnawave.models import (
    GetAllSubscriptionsResponseDto,
    GetSubscriptionByUsernameResponseDto,
    GetSubscriptionByShortUUIDResponseDto,
    GetSubscriptionByUUIDResponseDto,
    GetSubpageConfigByShortUuidRequestBodyDto,
    GetSubpageConfigByShortUuidResponseDto,
)


class SubscriptionsController(BaseController):
    # Protected endpoints below
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

    @get("/subscriptions/subpage-config/{short_uuid}", response_class=GetSubpageConfigByShortUuidResponseDto)
    async def get_subpage_config(
        self,
        short_uuid: Annotated[str, Path(description="Short UUID of the subscription")],
        body: Annotated[GetSubpageConfigByShortUuidRequestBodyDto, PydanticBody()],
    ) -> GetSubpageConfigByShortUuidResponseDto:
        """Get subscription page config by short UUID"""
        ...

    @get("/subscriptions/by-short-uuid/{short_uuid}/raw", response_class=GetRawSubscriptionByShortUuidResponseDto)
    async def get_raw_subscription(
        self,
        short_uuid: Annotated[str, Path(description="Short UUID of the user")],
        withDisabledHosts: Annotated[Annotated[bool, Path(description="Include disabled hosts")], bool] = False,
    ) -> GetRawSubscriptionByShortUuidResponseDto:
        """None"""
        ...