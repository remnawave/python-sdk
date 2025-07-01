import pytest

from remnawave_api.models import GetUserUsageByRangeResponseDto
from tests.conftest import REMNAWAVE_USER_UUID
from tests.utils import generate_isoformat_range


@pytest.mark.asyncio
async def test_users_stats(remnawave):
    start, end = generate_isoformat_range()
    user_usage_by_range = await remnawave.users_stats.get_user_usage_by_range(
        uuid=REMNAWAVE_USER_UUID, start=start, end=end
    )
    assert isinstance(user_usage_by_range, GetUserUsageByRangeResponseDto)
