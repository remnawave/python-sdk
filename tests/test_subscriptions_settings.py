import pytest

from remnawave_api.models import (
    SubscriptionSettingsResponseDto,
    UpdateSubscriptionSettingsRequestDto,
)


@pytest.mark.asyncio
async def test_subscriptions_settings(remnawave):
    settings = await remnawave.subscriptions_settings.get_settings()
    assert isinstance(settings, SubscriptionSettingsResponseDto)

    update_settings = await remnawave.subscriptions_settings.update_settings(
        UpdateSubscriptionSettingsRequestDto(uuid=settings.uuid)
    )
    assert isinstance(update_settings, SubscriptionSettingsResponseDto)
