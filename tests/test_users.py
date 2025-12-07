import random
from datetime import datetime, timedelta

import pytest
import pytz

from remnawave.enums import ErrorCode, UserStatus
from remnawave.exceptions import ApiError
from remnawave.models import (
    CreateUserRequestDto,
    DeleteUserResponseDto,
    EmailUserResponseDto,
    GetUserAccessibleNodesResponseDto,
    TelegramUserResponseDto,
    UpdateUserRequestDto,
    UserResponseDto,
    UsersResponseDto,
    TagsResponseDto,
    RevokeUserRequestDto,
    GetSubscriptionRequestsResponseDto
)
from remnawave.models.users import GetUserSubscriptionRequestHistoryResponseDto
from tests.utils import generate_email, generate_random_string


class TestUsersCRUD:
    """Тесты базовых CRUD операций для пользователей"""
    
    @pytest.mark.asyncio
    async def test_create_user(self, remnawave):
        email: str = generate_email(length=8)
        username: str = generate_random_string(length=8)
        telegram_id: int = random.randint(100000000, 999999999)
        expire_at: datetime = datetime.now(tz=pytz.UTC) + timedelta(days=7)

        create_user = await remnawave.users.create_user(
            CreateUserRequestDto(
                username=username,
                email=email,
                telegram_id=telegram_id,
                expire_at=expire_at,
            )
        )

        assert isinstance(create_user, UserResponseDto)
        assert create_user.username == username
        assert create_user.email == email
        assert create_user.telegram_id == telegram_id
        assert create_user.expire_at.isoformat(timespec="seconds") == expire_at.isoformat(
            timespec="seconds"
        )
        
        # Clean up - delete the test user
        string_uuid = str(create_user.uuid)
        await remnawave.users.delete_user(uuid=string_uuid)
    
    @pytest.mark.asyncio
    async def test_update_user(self, remnawave):
        # Create test user first
        username: str = generate_random_string(length=8)
        expire_at: datetime = datetime.now(tz=pytz.UTC) + timedelta(days=7)
        
        create_user = await remnawave.users.create_user(
            CreateUserRequestDto(
                username=username,
                expire_at=expire_at,
            )
        )
        
        string_uuid = str(create_user.uuid)
        
        # Update user
        update_description: str = "TEST"
        update_status: UserStatus = UserStatus.DISABLED
        update_user = await remnawave.users.update_user(
            UpdateUserRequestDto(
                uuid=string_uuid, status=update_status, description=update_description
            )
        )
        assert isinstance(update_user, UserResponseDto)
        assert update_user.uuid == create_user.uuid
        assert update_user.status == update_status
        assert update_user.description == update_description
        
        # Clean up
        await remnawave.users.delete_user(uuid=string_uuid)
    
    @pytest.mark.asyncio
    async def test_delete_user(self, remnawave):
        # Create test user first
        username: str = generate_random_string(length=8)
        expire_at: datetime = datetime.now(tz=pytz.UTC) + timedelta(days=7)
        
        create_user = await remnawave.users.create_user(
            CreateUserRequestDto(
                username=username,
                expire_at=expire_at,
            )
        )
        
        string_uuid = str(create_user.uuid)
        
        # Delete user
        delete_user = await remnawave.users.delete_user(uuid=string_uuid)
        assert isinstance(delete_user, DeleteUserResponseDto)
        assert delete_user.is_deleted is True


class TestUsersFetch:
    """Тесты получения информации о пользователях"""
    
    @pytest.mark.asyncio
    async def test_get_all_users(self, remnawave):
        all_users = await remnawave.users.get_all_users()
        assert isinstance(all_users, UsersResponseDto)
    
    @pytest.mark.asyncio
    async def test_get_user_by_uuid(self, remnawave, test_user):
        string_uuid = str(test_user.uuid)
        user_uuid = await remnawave.users.get_user_by_uuid(uuid=string_uuid)
        assert isinstance(user_uuid, UserResponseDto)
        assert user_uuid.uuid == test_user.uuid

    @pytest.mark.asyncio
    async def test_get_user_by_short_uuid(self, remnawave, test_user):
        user_short_uuid = await remnawave.users.get_user_by_short_uuid(
            short_uuid=test_user.short_uuid
        )
        assert isinstance(user_short_uuid, UserResponseDto)
        assert user_short_uuid.uuid == test_user.uuid

    @pytest.mark.asyncio
    async def test_get_user_by_username(self, remnawave, test_user):
        user_username = await remnawave.users.get_user_by_username(
            username=test_user.username
        )
        assert isinstance(user_username, UserResponseDto)
        assert user_username.uuid == test_user.uuid

    @pytest.mark.asyncio
    async def test_get_users_by_telegram_id(self, remnawave, test_user_with_telegram):
        string_telegram_id = str(test_user_with_telegram.telegram_id)
        user_telegram_id = await remnawave.users.get_users_by_telegram_id(
            telegram_id=string_telegram_id
        )
        assert isinstance(user_telegram_id, TelegramUserResponseDto)
        assert any(user.uuid == test_user_with_telegram.uuid for user in user_telegram_id)

    @pytest.mark.asyncio
    async def test_get_users_by_email(self, remnawave, test_user_with_email):
        user_email = await remnawave.users.get_users_by_email(email=test_user_with_email.email)
        assert isinstance(user_email, EmailUserResponseDto)
        assert any(user.uuid == test_user_with_email.uuid for user in user_email)
    
    @pytest.mark.asyncio
    async def test_get_all_tags(self, remnawave):
        users_tags = await remnawave.users.get_all_tags()
        assert isinstance(users_tags, TagsResponseDto)
    
    @pytest.mark.asyncio
    async def test_get_user_accessible_nodes(self, remnawave, test_user):
        try:
            string_uuid = str(test_user.uuid)
            user_accessible_nodes = await remnawave.users.get_user_accessible_nodes(uuid=string_uuid)
            assert isinstance(user_accessible_nodes, GetUserAccessibleNodesResponseDto)
            assert isinstance(user_accessible_nodes.nodes, list)
        except ApiError as e:
            # This might fail if the user doesn't have access to any nodes
            # or if the feature is not available, which is acceptable for testing
            assert e.error.code in [ErrorCode.USER_NOT_FOUND, ]

    @pytest.mark.asyncio
    async def test_get_subscription_requests(self, remnawave, test_user):
        """Test fetching user subscription request history"""
        string_uuid = str(test_user.uuid)
        try:
            subscription_requests = await remnawave.users.get_user_subscription_request_history(uuid=string_uuid)
            assert isinstance(subscription_requests, GetUserSubscriptionRequestHistoryResponseDto)
            assert hasattr(subscription_requests, 'total')
            assert hasattr(subscription_requests, 'records')
        except ApiError as e:
            # Этот блок должен срабатывать только если API вернуло ошибку
            # (404, 403 и т.д.), но не когда просто нет записей
            assert e.error.code in [ErrorCode.USER_NOT_FOUND]


class TestUserActions:
    """Тесты действий над пользователями"""
    
    @pytest.mark.asyncio
    async def test_reset_user_traffic(self, remnawave, test_user):
        string_uuid = str(test_user.uuid)
        user_reset_traffic = await remnawave.users.reset_user_traffic(uuid=string_uuid)
        assert isinstance(user_reset_traffic, UserResponseDto)
        assert user_reset_traffic.uuid == test_user.uuid
        assert user_reset_traffic.used_traffic_bytes == 0

    @pytest.mark.asyncio
    async def test_disable_enable_user(self, remnawave, test_user):
        string_uuid = str(test_user.uuid)
        
        # Disable user
        try:
            disable_user = await remnawave.users.disable_user(uuid=string_uuid)
            assert isinstance(disable_user, UserResponseDto)
            assert disable_user.uuid == test_user.uuid
            assert disable_user.status == UserStatus.DISABLED
        except ApiError as e:
            assert e.error.code == ErrorCode.USER_ALREADY_DISABLED

        # Enable user
        try:
            enable_user = await remnawave.users.enable_user(uuid=string_uuid)
            assert isinstance(enable_user, UserResponseDto)
            assert enable_user.uuid == test_user.uuid
            assert enable_user.status == UserStatus.ACTIVE
        except ApiError as e:
            assert e.error.code == ErrorCode.USER_ALREADY_ENABLED

    @pytest.mark.asyncio
    async def test_revoke_user_subscription(self, remnawave, test_user):
        string_uuid = str(test_user.uuid)
        old_short_uuid = test_user.short_uuid
        
        revoke_user_subscription = await remnawave.users.revoke_user_subscription(uuid=string_uuid)
        assert isinstance(revoke_user_subscription, UserResponseDto)
        assert revoke_user_subscription.uuid == test_user.uuid
        assert revoke_user_subscription.short_uuid != old_short_uuid


@pytest.fixture
async def test_user(remnawave):
    """Fixture to create a test user for tests"""
    username = generate_random_string(length=8)
    expire_at = datetime.now(tz=pytz.UTC) + timedelta(days=7)
    
    user = await remnawave.users.create_user(
        CreateUserRequestDto(
            username=username,
            expire_at=expire_at,
        )
    )
    
    yield user
    
    # Clean up
    await remnawave.users.delete_user(uuid=str(user.uuid))


@pytest.fixture
async def test_user_with_email(remnawave):
    """Fixture to create a test user with email for tests"""
    username = generate_random_string(length=8)
    email = generate_email(length=8)
    expire_at = datetime.now(tz=pytz.UTC) + timedelta(days=7)
    
    user = await remnawave.users.create_user(
        CreateUserRequestDto(
            username=username,
            email=email,
            expire_at=expire_at,
        )
    )
    
    yield user
    
    # Clean up
    await remnawave.users.delete_user(uuid=str(user.uuid))


@pytest.fixture
async def test_user_with_telegram(remnawave):
    """Fixture to create a test user with telegram ID for tests"""
    username = generate_random_string(length=8)
    telegram_id = random.randint(100000000, 999999999)
    expire_at = datetime.now(tz=pytz.UTC) + timedelta(days=7)
    
    user = await remnawave.users.create_user(
        CreateUserRequestDto(
            username=username,
            telegram_id=telegram_id,
            expire_at=expire_at,
        )
    )
    
    yield user
    
    # Clean up
    await remnawave.users.delete_user(uuid=str(user.uuid))