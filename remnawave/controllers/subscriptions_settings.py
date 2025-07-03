from typing import Annotated

from rapid_api_client.annotations import PydanticBody

from remnawave.models import (
    GetSubscriptionSettingsResponseDto,
    UpdateSubscriptionSettingsRequestDto,
    UpdateSubscriptionSettingsResponseDto,
)
from remnawave.rapid import BaseController, get, patch


class SubscriptionsSettingsController(BaseController):
    @get("/subscription-settings", response_class=GetSubscriptionSettingsResponseDto)
    async def get_settings(
        self,
    ) -> GetSubscriptionSettingsResponseDto:
        """Get Subscription Settings"""
        ...

    @patch(
        "/subscription-settings",
        response_class=UpdateSubscriptionSettingsResponseDto,
    )
    async def update_settings(
        self,
        body: Annotated[UpdateSubscriptionSettingsRequestDto, PydanticBody()],
    ) -> UpdateSubscriptionSettingsResponseDto:
        """Update Subscription Settings"""
        ...
