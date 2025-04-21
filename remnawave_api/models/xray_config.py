from pydantic import BaseModel


class ConfigResponseDto(BaseModel):
    config: dict
