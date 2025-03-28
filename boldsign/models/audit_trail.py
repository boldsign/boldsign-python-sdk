# coding: utf-8

"""
    BoldSign API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Contact: support@boldsign.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set, Tuple
from typing_extensions import Self
import io
from pydantic import StrictBool
from typing import Union

class AuditTrail(BaseModel):
    """
    AuditTrail
    """ # noqa: E501
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    to_name: Optional[StrictStr] = Field(default=None, alias="toName")
    to_email: Optional[StrictStr] = Field(default=None, alias="toEmail")
    ipaddress: Optional[StrictStr] = None
    action: Optional[StrictStr] = None
    timestamp: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["id", "name", "email", "toName", "toEmail", "ipaddress", "action", "timestamp"]

    @field_validator('action')
    def action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Sent', 'Viewed', 'Signed', 'Completed', 'Downloaded', 'Reassigned', 'Declined', 'Recalled', 'Created', 'AuthenticationFailed', 'Reminder', 'AccessCodeChanged', 'AccessCodeViewed', 'DownloadedForPrintSign', 'FormCreated', 'EmailOTP', 'AuthenticationRemoved', 'DownloadedAuditTrail', 'Cloned', 'ClonedWithFieldValues', 'Deleted', 'MovedToTrash', 'Restored', 'AutoReminder', 'Resend', 'Reviewed', 'InitiatePrintSign', 'CancelPrintSign', 'CompletePrintSign', 'GeneratedEmbeddedSignLink', 'EmbeddedSigned', 'EmbeddedReviewed', 'ExpiryDateExtended', 'Attachment', 'EditRecipient', 'AuthenticationAdded', 'AutoReminderON', 'AutoReminderOFF', 'SMSOTP', 'PhoneNumberChanged', 'UnlockedSMSOTP', 'SMSAuthenticationAdded', 'SMSAuthenticationRemoved', 'SMSOTPVerified', 'SMSAuthenticationFailed', 'UnlockEmailOTP', 'EmailAuthenticationAdded', 'EmailAuthenticationRemoved', 'EmailOtpVerify', 'EmailAuthenticationFailed', 'SMSOTPResend', 'EmailOTPResend', 'ResumeDocumentSigning', 'EmailOTPAuthenticationAdded', 'EmailOTPAuthenticationRemoved', 'EmailOTPAuthenticationFailed', 'EmailOTPVerified', 'IdentityVerificationInitiated', 'IdentityVerificationRemoved', 'IdentityVerificationCompleted', 'IdentityVerificationFailed', 'DownloadedVerificationData', 'ManualIdentityVerificationCompleted', 'IdentityVerificationReset', 'CreateEmbeddedVerificationLink', 'SensitiveDataDownloaded', 'IdVerificationRemoved', 'IdVerificationAdded', 'ManualIdentityVerificationInitiated', 'GeneratedSigningLink', 'EditingInitiated', 'EditingCancelled', 'EditingCompleted', 'QESVerificationInitiated', 'QESVerified', 'QESRejected', 'QESExpired', 'QESWithdrawn']):
            raise ValueError("must be one of enum values ('Sent', 'Viewed', 'Signed', 'Completed', 'Downloaded', 'Reassigned', 'Declined', 'Recalled', 'Created', 'AuthenticationFailed', 'Reminder', 'AccessCodeChanged', 'AccessCodeViewed', 'DownloadedForPrintSign', 'FormCreated', 'EmailOTP', 'AuthenticationRemoved', 'DownloadedAuditTrail', 'Cloned', 'ClonedWithFieldValues', 'Deleted', 'MovedToTrash', 'Restored', 'AutoReminder', 'Resend', 'Reviewed', 'InitiatePrintSign', 'CancelPrintSign', 'CompletePrintSign', 'GeneratedEmbeddedSignLink', 'EmbeddedSigned', 'EmbeddedReviewed', 'ExpiryDateExtended', 'Attachment', 'EditRecipient', 'AuthenticationAdded', 'AutoReminderON', 'AutoReminderOFF', 'SMSOTP', 'PhoneNumberChanged', 'UnlockedSMSOTP', 'SMSAuthenticationAdded', 'SMSAuthenticationRemoved', 'SMSOTPVerified', 'SMSAuthenticationFailed', 'UnlockEmailOTP', 'EmailAuthenticationAdded', 'EmailAuthenticationRemoved', 'EmailOtpVerify', 'EmailAuthenticationFailed', 'SMSOTPResend', 'EmailOTPResend', 'ResumeDocumentSigning', 'EmailOTPAuthenticationAdded', 'EmailOTPAuthenticationRemoved', 'EmailOTPAuthenticationFailed', 'EmailOTPVerified', 'IdentityVerificationInitiated', 'IdentityVerificationRemoved', 'IdentityVerificationCompleted', 'IdentityVerificationFailed', 'DownloadedVerificationData', 'ManualIdentityVerificationCompleted', 'IdentityVerificationReset', 'CreateEmbeddedVerificationLink', 'SensitiveDataDownloaded', 'IdVerificationRemoved', 'IdVerificationAdded', 'ManualIdentityVerificationInitiated', 'GeneratedSigningLink', 'EditingInitiated', 'EditingCancelled', 'EditingCompleted', 'QESVerificationInitiated', 'QESVerified', 'QESRejected', 'QESExpired', 'QESWithdrawn')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        arbitrary_types_allowed=True,
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    def to_json_form_params(self, excluded_fields: Set[str] = None) -> List[Tuple[str, str]]:
        data: List[Tuple[str, str]] = []

        for key, value in self.to_dict(excluded_fields).items():
            if isinstance(value, (int, str, bool)):
                data.append((key, value))
            elif isinstance(value, list):
                for index, item in enumerate(value):
                    if(isinstance(item, (int, str, bool))):
                        data.append((f'{key}[{index}]', item))
                    else:
                        data.append((key, json.dumps(value[index], ensure_ascii=False)))
            else:
                data.append((key, json.dumps(value, ensure_ascii=False)))

        return data

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AuditTrail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self, excluded_fields: Set[str] = None) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuditTrail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "email": obj.get("email"),
            "toName": obj.get("toName"),
            "toEmail": obj.get("toEmail"),
            "ipaddress": obj.get("ipaddress"),
            "action": obj.get("action"),
            "timestamp": obj.get("timestamp")
        })
        return _obj

    @classmethod
    def init(cls, data: Any) -> Self:
        """
        Attempt to instantiate and hydrate a new instance of this class
        """
        if isinstance(data, str):
            data = json.loads(data)

        return cls.from_dict(data)

    @classmethod
    def openapi_types(cls) -> Dict[str, str]:
        return {
            "id": "(str,)",
            "name": "(str,)",
            "email": "(str,)",
            "to_name": "(str,)",
            "to_email": "(str,)",
            "ipaddress": "(str,)",
            "action": "(str,)",
            "timestamp": "(int,)",
        }

    @classmethod
    def openapi_type_is_array(cls, property_name: str) -> bool:
        return property_name in [
        ]

