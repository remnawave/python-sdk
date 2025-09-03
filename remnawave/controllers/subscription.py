from typing import Annotated

from rapid_api_client import Path

from remnawave.enums import ClientType
from remnawave.models import GetSubscriptionInfoResponseDto
from remnawave.rapid import BaseController, get


class SubscriptionController(BaseController):
    # Public endpoints below
    @get("/sub/{short_uuid}/info", response_class=GetSubscriptionInfoResponseDto)
    async def get_subscription_info_by_short_uuid(
        self,
        short_uuid: Annotated[str, Path(description="Short UUID of the user")],
    ) -> GetSubscriptionInfoResponseDto:
        """None"""
        ...

    @get("/sub/{short_uuid}", response_class=str)
    async def get_subscription(
        self,
        short_uuid: Annotated[str, Path(description="Short UUID of the user")],
    ) -> str:
        """None"""
        ...

    @get("/sub/{short_uuid}/{client_type}", response_class=str)
    async def get_subscription_by_client_type(
        self,
        client_type: Annotated[ClientType, Path(description="Client type")],
        short_uuid: Annotated[str, Path(description="Short UUID of the user")],
    ) -> str:
        """None"""
        ...

    @get("/sub/outline/{short_uuid}/{type}/{encoded_tag}", response_class=str)
    async def get_subscription_with_type(
        self,
        short_uuid: Annotated[str, Path(description="Short UUID of the user")],
        type: Annotated[
            str,
            Path(
                description="Subscription type (required if encodedTag is provided). Only SS is supported for now."
            ),
        ] = "ss",
        encoded_tag: Annotated[
            str,
            Path(
                description="Base64 encoded tag for Outline config. This paramter is optional. It is required only when type=ss."
            ),
        ] = "VGVzdGVy",
    ) -> str:
        """None"""
        ...