import hmac
import hashlib
import json
from typing import Union, Optional, Dict
from remnawave.enums import UserEvent, NodeEvent, InfraBillingEvent, ServiceEvent
from remnawave.models import WebhookHeadersWebhookDto, WebhookPayloadWebhookDto


class WebhookUtility:
    @staticmethod
    def validate_webhook(
        body: Union[str, dict],
        signature: str,
        webhook_secret: str
    ) -> bool:
        """
            Webhook authentication via HMAC SHA-256.
        """
        if isinstance(body, str):
            original_body = body
        else:
            original_body = json.dumps(body, separators=(',', ':'))

        computed_signature = hmac.new(
            webhook_secret.encode("utf-8"),
            original_body.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

        return hmac.compare_digest(computed_signature, signature)

    @staticmethod
    def validate_webhook_with_headers(
        body: Union[str, dict],
        headers: Union[Dict[str, str], WebhookHeadersWebhookDto],
        webhook_secret: str
    ) -> bool:
        """
            Checking webhook headers.
        """
        if isinstance(headers, dict):
            headers = WebhookHeadersWebhookDto.from_headers(headers)

        return WebhookUtility.validate_webhook(body, headers.signature, webhook_secret)

    @staticmethod
    def parse_webhook(
        body: Union[str, dict],
        headers: Union[Dict[str, str], WebhookHeadersWebhookDto],
        webhook_secret: str,
        validate: bool = True
    ) -> Optional[WebhookPayloadWebhookDto]:
        """
            Parsing and (optional) validating the webhook payload.
        """
        if validate and not WebhookUtility.validate_webhook_with_headers(body, headers, webhook_secret):
            return None

        if isinstance(body, str):
            body = json.loads(body)

        return WebhookPayloadWebhookDto.from_dict(body)

    @staticmethod
    def is_user_event(event: str) -> bool:
        return event in {e.value for e in UserEvent}

    @staticmethod
    def is_node_event(event: str) -> bool:
        return event in {e.value for e in NodeEvent}

    @staticmethod
    def is_infra_billing_event(event: str) -> bool:
        return event in {e.value for e in InfraBillingEvent}

    @staticmethod
    def is_service_event(event: str) -> bool:
        return event in {e.value for e in ServiceEvent}