import hmac
import hashlib
import json
from typing import Union, Optional

from remnawave.models.webhook import (
    WebhookPayloadDto,
    UserDto,
    NodeDto,
    HwidUserDeviceDto,
    LoginAttemptDto,
    UserHwidDeviceEventDto,
)

class WebhookHeadersDto:
    """Helper class for webhook headers"""
    
    def __init__(self, signature: str, timestamp: str):
        self.signature = signature
        self.timestamp = timestamp
    
    @classmethod
    def from_headers(cls, headers: dict[str, str]) -> "WebhookHeadersDto":
        """
        Create WebhookHeadersDto from headers dictionary.
        Handles case-insensitive header names.
        """
        signature = None
        timestamp = None
        
        for key, value in headers.items():
            lower_key = key.lower()
            if lower_key == "x-remnawave-signature":
                signature = value
            elif lower_key == "x-remnawave-timestamp":
                timestamp = value
        
        if not signature or not timestamp:
            raise ValueError("Missing required webhook headers")
        
        return cls(signature=signature, timestamp=timestamp)


class WebhookUtility:
    @staticmethod
    def validate_webhook(
        body: Union[str, dict],
        signature: str,
        webhook_secret: str
    ) -> bool:
        """
        Validates the webhook's authenticity using HMAC SHA-256.

        :param body: The webhook request body (either a JSON string or a parsed dictionary).
        :param signature: The signature received from the server.
        :param webhook_secret: The secret key used to compute the HMAC.
        :return: True if the signature matches, otherwise False.
        """
        if isinstance(body, str):
            original_body = body
        else:
            original_body = json.dumps(body, separators=(',', ':'))

        computed_signature = hmac.new(
            webhook_secret.encode('utf-8'),
            original_body.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

        return hmac.compare_digest(computed_signature, signature)

    @staticmethod
    def validate_webhook_with_headers(
        body: Union[str, dict],
        headers: Union[dict[str, str], WebhookHeadersDto],
        webhook_secret: str
    ) -> bool:
        """
        Validates the webhook using headers object.

        :param body: The webhook request body.
        :param headers: Dictionary with headers or WebhookHeadersDto object.
        :param webhook_secret: The secret key used to compute the HMAC.
        :return: True if the signature matches, otherwise False.
        """
        if isinstance(headers, dict):
            headers = WebhookHeadersDto.from_headers(headers)
        
        return WebhookUtility.validate_webhook(body, headers.signature, webhook_secret)

    @staticmethod
    def parse_webhook(
        body: Union[str, dict],
        headers: Union[dict[str, str], WebhookHeadersDto],
        webhook_secret: str,
        validate: bool = True
    ) -> Optional[WebhookPayloadDto]:
        """
        Parses and optionally validates the webhook payload.

        :param body: The webhook request body.
        :param headers: Dictionary with headers or WebhookHeadersDto object.
        :param webhook_secret: The secret key used to compute the HMAC.
        :param validate: Whether to validate the webhook signature (default: True).
        :return: Parsed WebhookPayloadDto or None if validation fails.
        """
        if validate and not WebhookUtility.validate_webhook_with_headers(body, headers, webhook_secret):
            return None

        if isinstance(body, str):
            body = json.loads(body)

        return WebhookPayloadDto.from_dict(body)

    @staticmethod
    def is_user_event(event: str) -> bool:
        """Check if event is a user event."""
        return event.startswith("user.")

    @staticmethod
    def is_user_hwid_devices_event(event: str) -> bool:
        """Check if event is a user HWID devices event."""
        return event.startswith("user_hwid_devices.")

    @staticmethod
    def is_node_event(event: str) -> bool:
        """Check if event is a node event."""
        return event.startswith("node.")

    @staticmethod
    def is_infra_billing_event(event: str) -> bool:
        """Check if event is an infra billing event."""
        return event.startswith("crm.infra_billing")

    @staticmethod
    def is_crm_event(event: str) -> bool:
        """Check if event is a CRM event."""
        return event.startswith("crm.")

    @staticmethod
    def is_service_event(event: str) -> bool:
        """Check if event is a service event."""
        return event.startswith("service.")

    @staticmethod
    def is_errors_event(event: str) -> bool:
        """Check if event is an errors event."""
        return event.startswith("errors.")

    @staticmethod
    def get_typed_data(payload: WebhookPayloadDto) -> Union[UserDto, NodeDto, HwidUserDeviceDto, LoginAttemptDto, UserHwidDeviceEventDto, dict]:
        """
        Get typed data from webhook payload based on event type.
        
        :param payload: Parsed webhook payload.
        :return: Typed data object.
        """
        return payload.data

    @staticmethod
    def extract_user_hwid_event_data(payload: WebhookPayloadDto) -> Optional[tuple[UserDto, HwidUserDeviceDto]]:
        """
        Extract user and HWID device from user_hwid_devices event.
        
        :param payload: Parsed webhook payload.
        :return: Tuple of (UserDto, HwidUserDeviceDto) or None if not a HWID event.
        """
        if not WebhookUtility.is_user_hwid_devices_event(payload.event):
            return None
        
        if isinstance(payload.data, dict):
            user_data = payload.data.get("user", {})
            hwid_data = payload.data.get("hwidUserDevice", {})
            
            return (
                UserDto(**user_data),
                HwidUserDeviceDto(**hwid_data)
            )
        
        return None