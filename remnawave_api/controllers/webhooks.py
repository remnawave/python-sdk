import hmac
import hashlib
import json
from typing import Union

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