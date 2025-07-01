from datetime import datetime, timedelta

import pytest

from remnawave_api.models import (
    CreateInfraBillingNodeRequestDto,
    CreateInfraBillingNodeResponseDto,
    CreateInfraProviderRequestDto,
    CreateInfraProviderResponseDto,
    DeleteInfraBillingNodeResponseDto,
    DeleteInfraProviderResponseDto,
    GetAllInfraBillingHistoryResponseDto,
    GetAllInfraBillingNodesResponseDto,
    GetAllInfraProvidersResponseDto,
    GetInfraBillingHistoryByUuidResponseDto,
    GetInfraBillingNodeByUuidResponseDto,
    GetInfraProviderByUuidResponseDto,
    UpdateInfraBillingNodeRequestDto,
    UpdateInfraBillingNodeResponseDto,
    UpdateInfraProviderRequestDto,
    UpdateInfraProviderResponseDto,
)
from tests.utils import generate_random_string


@pytest.mark.asyncio
async def test_infra_billing(remnawave) -> None:
    provider_name = f"test_provider_{generate_random_string(length=6)}"
    
    # Test create infra provider
    create_provider = await remnawave.infra_billing.create_infra_provider(
        CreateInfraProviderRequestDto(
            name=provider_name,
            favicon_link="https://example.com/favicon.ico",
            login_url="https://example.com/login"
        )
    )
    
    assert isinstance(create_provider, CreateInfraProviderResponseDto)
    assert create_provider.name == provider_name
    
    provider_uuid = str(create_provider.uuid)
    
    # Test get all infra providers
    all_providers = await remnawave.infra_billing.get_all_infra_providers()
    assert isinstance(all_providers, GetAllInfraProvidersResponseDto)
    assert all_providers.total > 0
    assert len(all_providers.providers) > 0
    
    # Test get infra provider by uuid
    provider_by_uuid = await remnawave.infra_billing.get_infra_provider_by_uuid(provider_uuid)
    assert isinstance(provider_by_uuid, GetInfraProviderByUuidResponseDto)
    assert provider_by_uuid.name == provider_name
    
    # Test update infra provider
    updated_name = f"updated_{provider_name}"
    update_provider = await remnawave.infra_billing.update_infra_provider(
        UpdateInfraProviderRequestDto(
            uuid=create_provider.uuid,
            name=updated_name,
            favicon_link="https://example.com/new-favicon.ico"
        )
    )
    
    assert isinstance(update_provider, UpdateInfraProviderResponseDto)
    assert update_provider.name == updated_name
    
    # Test get all infra billing history
    billing_history = await remnawave.infra_billing.get_all_infra_billing_history(start=0, size=25)
    assert isinstance(billing_history, GetAllInfraBillingHistoryResponseDto)
    
    # Test get all infra billing nodes
    billing_nodes = await remnawave.infra_billing.get_all_infra_billing_nodes(start=0, size=25)
    assert isinstance(billing_nodes, GetAllInfraBillingNodesResponseDto)
    
    # Skip testing actual billing node creation/update/delete as it requires existing nodes
    # These would need real node UUIDs which may not exist in test environment
    
    # Test delete infra provider
    delete_provider = await remnawave.infra_billing.delete_infra_provider_by_uuid(provider_uuid)
    assert isinstance(delete_provider, DeleteInfraProviderResponseDto)
    assert delete_provider.is_deleted is True
