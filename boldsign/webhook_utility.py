import hashlib
import hmac
import time
import json
from typing import Dict, List, Optional
from boldsign import models
from boldsign.exceptions import ApiException

class BoldSignSignatureException(Exception):
    """Exception thrown when there is a mismatch in signature comparison."""
    pass

class WebhookUtility:
    """The webhook event utility."""

    BOLD_SIGN_EVENT_HEADER = "X-BoldSign-Event"
    BOLD_SIGN_SIGNATURE_HEADER = "X-BoldSign-Signature"
    DEFAULT_TIME_TOLERANCE = 300

    @staticmethod
    def parse_event(
        json_payload: str,
    ) -> models.WebhookEvent:
        """
        Parses a JSON string from a BoldSign webhook into a WebhookEvent object.
        """

        if not json_payload:
            raise ValueError("json_payload cannot be null or empty")

        return models.WebhookEvent.from_json(json_payload)

    @staticmethod
    def validate_signature(json_payload: str, signature_header: str, secret_key: str, tolerance: int = DEFAULT_TIME_TOLERANCE):
        """
        Comparing the hmac signature by request header.
        """
        WebhookUtility._validate_signature(json_payload, signature_header, secret_key, tolerance, int(time.time()))

    @staticmethod
    def _validate_signature(json_payload: str, signature_header: str, secret_key: str, tolerance: int, utc_now: int):
        if not json_payload:
            raise ValueError("json_payload cannot be null or empty")
        if not signature_header:
            raise ValueError("signature_header cannot be null or empty")
        if not secret_key:
            raise ValueError("secret_key cannot be null or empty")

        hmac_signatures = WebhookUtility._parse_boldsign_signature(signature_header)
        
        t_values = hmac_signatures.get("t", [])
        if not t_values:
            raise BoldSignSignatureException("Timestamp 't' not found in signature header")
        
        timestamp = t_values[0]
        
        try:
            generated_signature = WebhookUtility._generate_hmac_signature(secret_key, json_payload, timestamp)
        except Exception:
            raise BoldSignSignatureException("Error generating signature")

        s0_values = hmac_signatures.get("s0", [])
        s1_values = hmac_signatures.get("s1", [])
        
        if not WebhookUtility._is_signature_matched(generated_signature, s0_values) and \
           not WebhookUtility._is_signature_matched(generated_signature, s1_values):
            raise BoldSignSignatureException("Signature mismatch")

        try:
            ts_int = int(timestamp)
        except ValueError:
            raise BoldSignSignatureException("Invalid timestamp format")

        if abs(utc_now - ts_int) > tolerance:
            raise BoldSignSignatureException("Timestamp not in allowed tolerance")

    @staticmethod
    def _parse_boldsign_signature(signature_header: str) -> Dict[str, List[str]]:
        pairs = signature_header.split(',')
        result = {}
        for pair_str in pairs:
            parts = pair_str.strip().split('=', 1)
            if len(parts) != 2:
                raise BoldSignSignatureException("Unexpected characters found while parsing signature header")
            key, value = parts[0], parts[1]
            if key not in result:
                result[key] = []
            result[key].append(value)
        return result

    @staticmethod
    def _generate_hmac_signature(secret_key: str, payload: str, timestamp: str) -> str:
        message = f"{timestamp}.{payload}".encode('utf-8')
        secret = secret_key.encode('utf-8')
        signature = hmac.new(secret, message, hashlib.sha256).hexdigest()
        return signature.lower()

    @staticmethod
    def _is_signature_matched(signature: str, signatures: List[str]) -> bool:
        for s in signatures:
            if hmac.compare_digest(s, signature):
                return True
        return False
