import pytest

from remnawave.models import (
    GetSubscriptionSettingsResponseDto,
    UpdateSubscriptionSettingsRequestDto,
    UpdateSubscriptionSettingsResponseDto,
)


@pytest.mark.asyncio
async def test_subscriptions_settings(remnawave):
    settings = await remnawave.subscriptions_settings.get_settings()
    assert isinstance(settings, GetSubscriptionSettingsResponseDto)

    update_settings = await remnawave.subscriptions_settings.update_settings(
        UpdateSubscriptionSettingsRequestDto(uuid=settings.uuid)
    )
    assert isinstance(update_settings, UpdateSubscriptionSettingsResponseDto)
