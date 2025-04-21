import pytest

from remnawave_api.models import FullInboundsResponseDto, InboundsResponseDto


@pytest.mark.asyncio
async def test_inbounds(remnawave):
    full_inbounds = await remnawave.inbounds.get_full_inbounds()
    assert isinstance(full_inbounds, FullInboundsResponseDto)

    inbounds = await remnawave.inbounds.get_inbounds()
    assert isinstance(inbounds, InboundsResponseDto)
