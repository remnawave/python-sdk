import pytest

from remnawave.models import (
    GetAllSubscriptionRequestHistoryResponseDto,
    GetSubscriptionRequestHistoryStatsResponseDto
)


class TestSubscriptionRequestHistory:
    """Тесты для истории запросов подписок"""
    
    @pytest.mark.asyncio
    async def test_get_all_subscription_request_history(self, remnawave):
        """Тест получения всей истории запросов подписок"""
        response = await remnawave.subscription_request_history.get_all_subscription_request_history(
            size=10,
            start=0
        )
        assert isinstance(response, GetAllSubscriptionRequestHistoryResponseDto)
        assert hasattr(response, 'total')
        assert hasattr(response, 'records')
    
    @pytest.mark.asyncio
    async def test_get_subscription_request_history_stats(self, remnawave):
        """Тест получения статистики истории запросов подписок"""
        response = await remnawave.subscription_request_history.get_subscription_request_history_stats()
        assert isinstance(response, GetSubscriptionRequestHistoryStatsResponseDto)
        assert hasattr(response, 'by_parsed_app')
        assert hasattr(response, 'hourly_request_stats')