from pydantic import BaseModel, Field


class AddInboundToUsersResponseDto(BaseModel):
    is_success: bool = Field(alias="isSuccess")


class RemoveInboundFromNodesResponseDto(BaseModel):
    is_success: bool = Field(alias="isSuccess")


class RemoveInboundFromUsersResponseDto(BaseModel):
    is_success: bool = Field(alias="isSuccess")


class AddInboundToNodesResponseDto(BaseModel):
    is_success: bool = Field(alias="isSuccess")
