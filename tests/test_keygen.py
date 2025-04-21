import pytest

from remnawave_api.models import PubKeyResponseDto


@pytest.mark.asyncio
async def test_keygen(remnawave):
    key = await remnawave.keygen.generate_key()
    assert isinstance(key, PubKeyResponseDto)
