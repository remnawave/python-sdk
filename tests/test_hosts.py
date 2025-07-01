import random

import pytest

from remnawave_api.enums import ALPN, Fingerprint
from remnawave_api.models import (
    CreateHostRequestDto,
    CreateHostResponseDto,
    DeleteHostResponseDto,
    GetAllHostsResponseDto,
    GetOneHostResponseDto,
    ReorderHostItem,
    ReorderHostRequestDto,
    ReorderHostResponseDto,
    UpdateHostRequestDto,
    UpdateHostResponseDto,
)
from tests.conftest import REMNAWAVE_INBOUND_UUID, REMNAWAVE_CONFIG_PROFILE_UUID
from tests.utils import generate_random_string


@pytest.mark.asyncio
async def test_hosts(remnawave):
    all_hosts = await remnawave.hosts.get_all_hosts()
    assert isinstance(all_hosts, GetAllHostsResponseDto)

    random_ip: str = f"{random.randint(500, 800)}" + ".0.0.1"
    random_port: int = random.randint(5000, 8000)
    random_remark: str = generate_random_string()
    create_host = await remnawave.hosts.create_host(
        CreateHostRequestDto(
            inbound_uuid=REMNAWAVE_INBOUND_UUID,
            config_profile_inbound_uuid=REMNAWAVE_CONFIG_PROFILE_UUID,
            remark=random_remark,
            address=random_ip,
            port=random_port,
        )
    )
    assert isinstance(create_host, CreateHostResponseDto)
    assert str(create_host.inbound_uuid) == REMNAWAVE_INBOUND_UUID
    assert create_host.address == random_ip
    assert create_host.port == random_port
    assert create_host.remark == random_remark

    string_uuid = str(create_host.uuid)

    host = await remnawave.hosts.get_one_host(uuid=string_uuid)
    assert isinstance(host, GetOneHostResponseDto)
    assert host.uuid == create_host.uuid

    reorder_host = await remnawave.hosts.reorder_hosts(
        data=ReorderHostRequestDto(hosts=[ReorderHostItem(view_position=1, uuid=string_uuid)])
    )
    assert isinstance(reorder_host, ReorderHostResponseDto)
    assert reorder_host.is_updated is True

    update_remark: str = "TEST_REMARK"
    update_fingerprint: Fingerprint = Fingerprint.ANDROID
    update_alpn: ALPN = ALPN.H3_H2_COMBINED
    update_host = await remnawave.hosts.update_host(
        UpdateHostRequestDto(
            uuid=string_uuid,
            remark=update_remark,
            alpn=update_alpn,
            fingerprint=update_fingerprint,
        )
    )
    assert isinstance(update_host, UpdateHostResponseDto)
    assert update_host.remark == update_remark
    assert update_host.alpn == update_alpn
    assert update_host.fingerprint == update_fingerprint

    delete_host = await remnawave.hosts.delete_host(uuid=string_uuid)
    assert isinstance(delete_host, DeleteHostResponseDto)
    assert delete_host.is_deleted is True
