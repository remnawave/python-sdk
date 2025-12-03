from datetime import datetime, timedelta
from typing import List

import pytest
import pytz

from remnawave.models import BulkResponseDto, UpdateUserFields, BulkUpdateUsersRequestDto
from tests.conftest import REMNAWAVE_USER_UUID


@pytest.mark.asyncio
async def test_users_bulk_actions(remnawave):
    expire_at = datetime.now(tz=pytz.utc) + timedelta(days=14)
    description = "TEST_DESCRIPTION"

    bulk_update_users = await remnawave.users_bulk_actions.bulk_update_users(
        body=BulkUpdateUsersRequestDto(
            uuids=[REMNAWAVE_USER_UUID],
            fields=UpdateUserFields(
                expire_at=expire_at,
                description=description,
            ),
        ),
    )
    assert isinstance(bulk_update_users, BulkResponseDto)
    assert bulk_update_users.affected_rows > 0
