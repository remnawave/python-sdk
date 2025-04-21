from pydantic import BaseModel, Field


class PubKeyResponseDto(BaseModel):
    pub_key: str = Field(alias="pubKey")
