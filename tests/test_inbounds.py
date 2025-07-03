import pytest

from remnawave.models import GetAllInboundsResponseDto


@pytest.mark.asyncio
async def test_inbounds(remnawave):
    # Test new API v2 endpoint
    all_inbounds = await remnawave.inbounds.get_all_inbounds()
    assert isinstance(all_inbounds, GetAllInboundsResponseDto)
    assert hasattr(all_inbounds, 'total')
    assert hasattr(all_inbounds, 'inbounds')
    assert isinstance(all_inbounds.total, (int, float))
    assert isinstance(all_inbounds.inbounds, list)
