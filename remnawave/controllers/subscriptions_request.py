from typing import Annotated

from rapid_api_client import Query

from remnawave.models import (
    GetAllSubscriptionRequestHistoryResponseDto,
    GetSubscriptionRequestHistoryStatsResponseDto,
)
from remnawave.rapid import BaseController, get


class SubscriptionRequestHistoryController(BaseController):
    @get("/subscription-request-history", response_class=GetAllSubscriptionRequestHistoryResponseDto)
    async def get_all_subscription_request_history(
        self,
        size: Annotated[
            int, Query(default=25, ge=1, description="Page size for pagination")
        ] = 25,
        start: Annotated[
            int, Query(default=0, ge=0, description="Offset for pagination")
        ] = 0,
    ) -> GetAllSubscriptionRequestHistoryResponseDto:
        """Get all subscription request history"""
        ...

    @get(
        "/subscription-request-history/stats",
        response_class=GetSubscriptionRequestHistoryStatsResponseDto,
    )
    async def get_subscription_request_history_stats(
        self,
    ) -> GetSubscriptionRequestHistoryStatsResponseDto:
        """Get subscription request history stats"""
        ...