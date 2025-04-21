from typing import Optional

from pydantic import BaseModel, Field


class CreateApiTokenRequestDto(BaseModel):
    token_name: str = Field(serialization_alias="tokenName")
    token_description: Optional[str] = Field(
        None, serialization_alias="tokenDescription"
    )
