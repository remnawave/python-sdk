from typing import Any, Dict

from pydantic import BaseModel


class ConfigData(BaseModel):
    config: Any


class GetConfigResponseDto(ConfigData):
    pass


class UpdateConfigRequestDto(BaseModel):
    pass  # Empty model as per OpenAPI spec


class UpdateConfigResponseDto(ConfigData):
    pass


# Legacy alias for backward compatibility
ConfigResponseDto = ConfigData
