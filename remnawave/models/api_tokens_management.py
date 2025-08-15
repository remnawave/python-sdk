from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class CreateApiTokenRequestDto(BaseModel):
    token_name: str = Field(serialization_alias="tokenName")


class CreateApiTokenResponseData(BaseModel):
    token: str
    uuid: str


class CreateApiTokenResponseDto(CreateApiTokenResponseData):
    pass


class DeleteApiTokenResponseDto(BaseModel):
    is_deleted: bool = Field(..., alias="isDeleted")


class ApiTokenDto(BaseModel):
    uuid: str
    token: str
    token_name: str = Field(..., alias="tokenName")
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")


class DocsInfoDto(BaseModel):
    is_docs_enabled: bool = Field(..., alias="isDocsEnabled")
    scalar_path: Optional[str] = Field(None, alias="scalarPath")
    swagger_path: Optional[str] = Field(None, alias="swaggerPath")


class FindAllApiTokensResponseData(BaseModel):
    api_keys: List[ApiTokenDto] = Field(..., alias="apiKeys")
    docs: DocsInfoDto


class FindAllApiTokensResponseDto(FindAllApiTokensResponseData):
    pass
