import pytest

from remnawave.models import GetPubKeyResponseDto


@pytest.mark.asyncio
async def test_keygen(remnawave):
    key = await remnawave.keygen.generate_key()
    assert isinstance(key, GetPubKeyResponseDto)
