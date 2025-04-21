from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

from remnawave_api.enums import TemplateType


class TemplateResponseDto(BaseModel):
    uuid: UUID
    template_type: TemplateType = Field(alias="templateType")
    template_json: Optional[dict] = Field(None, alias="templateJson")
    encoded_template_yaml: Optional[str] = Field(None, alias="encodedTemplateYaml")


class UpdateTemplateRequestDto(BaseModel):
    template_type: TemplateType = Field(serialization_alias="templateType")
    template_json: Optional[dict] = Field(None, serialization_alias="templateJson")
    encoded_template_yaml: Optional[str] = Field(
        None, serialization_alias="encodedTemplateYaml"
    )
