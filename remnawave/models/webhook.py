from datetime import datetime
from typing import List, Optional, Union, Literal
from uuid import UUID

from pydantic import BaseModel, Field
from pydantic.alias_generators import to_camel


class InboundWebhookDto(BaseModel):
    uuid: UUID
    tag: str
    type: str
    network: str | None = None
    security: str | None = None


class WebhookUserWebhookDto(BaseModel):
    uuid: UUID
    subscription_uuid: UUID
    short_uuid: str
    username: str
    status: Literal['DISABLED', 'LIMITED', 'EXPIRED', 'ACTIVE']
    used_traffic_bytes: str
    lifetime_used_traffic_bytes: str
    traffic_limit_bytes: str
    traffic_limit_strategy: Literal['NO_RESET', 'DAY', 'WEEK', 'MONTH']
    sub_last_user_agent: str | None = None
    sub_last_opened_at: datetime | None = None
    expire_at: datetime
    online_at: datetime | None = None
    sub_revoked_at: datetime | None = None
    last_traffic_reset_at: datetime | None = None
    trojan_password: str
    vless_uuid: UUID
    ss_password: str
    description: str | None = None
    telegram_id: str | None = None
    email: str | None = None
    hwid_device_limit: int | None = None
    created_at: datetime
    updated_at: datetime
    first_connected_at: datetime | None = None
    last_triggered_threshold: int
    active_user_inbounds: List[InboundWebhookDto]

    model_config = {
        "alias_generator": to_camel,
        "populate_by_name": True,
    }


class WebhookNodeWebhookDto(BaseModel):
    uuid: UUID
    name: str
    address: str
    port: int | None = None
    is_connected: bool
    is_connecting: bool
    is_disabled: bool
    is_node_online: bool
    is_xray_running: bool
    last_status_change: datetime | None = None
    last_status_message: str | None = None
    xray_version: str | None = None
    xray_uptime: str
    users_online: int | None = None
    is_traffic_tracking_active: bool
    traffic_reset_day: int | None = None
    traffic_limit_bytes: str | None = None
    traffic_used_bytes: str | None = None
    notify_percent: int | None = None
    view_position: int
    country_code: str
    consumption_multiplier: str
    cpu_count: int | None = None
    cpu_model: str | None = None
    total_ram: str | None = None
    created_at: datetime
    updated_at: datetime
    excluded_inbounds: List[InboundWebhookDto]

    model_config = {
        "alias_generator": to_camel,
        "populate_by_name": True,
    }


class InfraBillingSummaryWebhookDto(BaseModel):
    node_name: str
    provider_name: str
    login_url: str
    next_billing_at: datetime

    model_config = {
        "alias_generator": to_camel,
        "populate_by_name": True,
    }


class LoginAttemptWebhookDto(BaseModel):
    username: str
    ip: str
    user_agent: str
    description: str | None = None
    password: str | None = None

    model_config = {
        "alias_generator": to_camel,
        "populate_by_name": True,
    }


class WebhookServiceWebhookDto(BaseModel):
    login_attempt: LoginAttemptWebhookDto | None = None

    model_config = {
        "alias_generator": to_camel,
        "populate_by_name": True,
    }


class WebhookHeadersWebhookDto(BaseModel):
    signature: str = Field(alias="x-remnawave-signature")
    timestamp: str = Field(alias="x-remnawave-timestamp")

    model_config = {
        "populate_by_name": True,
        "extra": "allow",
    }

    @classmethod
    def from_headers(cls, headers: dict[str, str]) -> "WebhookHeadersWebhookDto":
        """
            Creates a WebhookHeadersWebhookDto from a dictionary of HTTP headers.
            Handles case-insensitive keys.
        """
        normalized = {k.lower(): v for k, v in headers.items()}
        return cls(
            **{
                "x-remnawave-signature": normalized.get("x-remnawave-signature"),
                "x-remnawave-timestamp": normalized.get("x-remnawave-timestamp"),
            }
        )


class WebhookPayloadWebhookDto(BaseModel):
    event: str
    data: Union[
        WebhookUserWebhookDto,
        WebhookNodeWebhookDto,
        InfraBillingSummaryWebhookDto,
        WebhookServiceWebhookDto,
        dict
    ]
    timestamp: datetime

    @classmethod
    def from_dict(cls, payload: dict) -> "WebhookPayloadWebhookDto":
        """
            Parses the webhook payload and automatically determines the WebhookDto based on the event type.
        """
        event = payload.get("event", "")
        data_raw = payload.get("data", {})

        if event.startswith("user."):
            data = WebhookUserWebhookDto(**data_raw)
        elif event.startswith("node."):
            data = WebhookNodeWebhookDto(**data_raw)
        elif event.startswith("crm.infra_billing"):
            data = InfraBillingSummaryWebhookDto(**data_raw)
        elif event.startswith("service."):
            data = WebhookServiceWebhookDto(**data_raw)
        else:
            data = data_raw

        timestamp_raw = payload.get("timestamp")
        if isinstance(timestamp_raw, (int, float)):
            timestamp = datetime.fromtimestamp(timestamp_raw)
        else:
            timestamp = timestamp_raw

        return cls(
            event=event,
            data=data,
            timestamp=timestamp
        )