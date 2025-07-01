from pydantic import BaseModel, Field


class PubKeyData(BaseModel):
    pub_key: str = Field(alias="pubKey")


class GetPubKeyResponseDto(BaseModel):
    pub_key: str = Field(alias="pubKey")


# Legacy alias for backward compatibility
PubKeyResponseDto = PubKeyData
