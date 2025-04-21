from typing import Annotated

from rapid_api_client.annotations import PydanticBody

from remnawave_api.models import (
    SubscriptionSettingsResponseDto,
    UpdateSubscriptionSettingsRequestDto,
)
from remnawave_api.rapid import BaseController, get, post


class SubscriptionsSettingsController(BaseController):
    @get("/subscription-settings/get", response_class=SubscriptionSettingsResponseDto)
    async def get_settings(
        self,
    ) -> SubscriptionSettingsResponseDto:
        """Get Subscription Settings"""
        ...

    @post(
        "/subscription-settings/update",
        response_class=SubscriptionSettingsResponseDto,
    )
    async def update_settings(
        self,
        body: Annotated[UpdateSubscriptionSettingsRequestDto, PydanticBody()],
    ) -> SubscriptionSettingsResponseDto:
        """Update Subscription Settings"""
        ...
