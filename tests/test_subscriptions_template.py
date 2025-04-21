import pytest

from remnawave_api.enums import TemplateType
from remnawave_api.models import TemplateResponseDto, UpdateTemplateRequestDto


@pytest.mark.asyncio
async def test_subscriptions_template(remnawave):
    template_type: TemplateType = TemplateType.SINGBOX
    template = await remnawave.subscriptions_template.get_template(
        template_type=template_type
    )
    assert isinstance(template, TemplateResponseDto)

    update_template = await remnawave.subscriptions_template.update_template(
        UpdateTemplateRequestDto(template_type=template_type)
    )
    assert isinstance(update_template, TemplateResponseDto)
    assert update_template.template_type == template_type
