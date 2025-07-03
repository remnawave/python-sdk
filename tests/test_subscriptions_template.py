import pytest

from remnawave.enums import TemplateType
from remnawave.models import GetTemplateResponseDto, UpdateTemplateRequestDto, UpdateTemplateResponseDto


@pytest.mark.asyncio
async def test_subscriptions_template(remnawave):
    template_type: TemplateType = TemplateType.SINGBOX
    template = await remnawave.subscriptions_template.get_template(
        template_type=template_type
    )
    assert isinstance(template, GetTemplateResponseDto)

    update_template = await remnawave.subscriptions_template.update_template(
        UpdateTemplateRequestDto(template_type=template_type)
    )
    assert isinstance(update_template, UpdateTemplateResponseDto)
    assert update_template.template_type == template_type
