from typing import Any, Dict

from pydantic import BaseModel
from pydantic.alias_generators import to_camel


class ConfigData(BaseModel):
    config: Any
    
    model_config = {"alias_generator": to_camel, "populate_by_name": True}


class GetConfigResponseDto(ConfigData):
    pass


class UpdateConfigRequestDto(BaseModel):
    pass  # Empty model as per OpenAPI spec


class UpdateConfigResponseDto(ConfigData):
    pass


# Legacy alias for backward compatibility
ConfigResponseDto = ConfigData
