import pytest

from remnawave_api.enums import ClientType
from remnawave_api.models import GetSubscriptionInfoResponseDto
from tests.conftest import REMNAWAVE_SHORT_UUID


@pytest.mark.asyncio
async def test_subscriptions(remnawave):
    subscription_info = (
        await remnawave.subscription.get_subscription_info_by_short_uuid(
            short_uuid=REMNAWAVE_SHORT_UUID
        )
    )
    assert isinstance(subscription_info, GetSubscriptionInfoResponseDto)
    assert subscription_info.is_found is True

    subscription = await remnawave.subscription.get_subscription(
        short_uuid=REMNAWAVE_SHORT_UUID
    )
    assert isinstance(subscription, str)

    subscription_by_client_type = (
        await remnawave.subscription.get_subscription_by_client_type(
            short_uuid=REMNAWAVE_SHORT_UUID, client_type=ClientType.SINGBOX
        )
    )
    assert isinstance(subscription_by_client_type, str)

    subscription_with_type = await remnawave.subscription.get_subscription_with_type(
        short_uuid=REMNAWAVE_SHORT_UUID
    )
    assert isinstance(subscription_with_type, str)
