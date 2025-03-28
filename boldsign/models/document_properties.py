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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from boldsign.models.audit_trail import AuditTrail
from boldsign.models.behalf_of import BehalfOf
from boldsign.models.document_cc_details import DocumentCcDetails
from boldsign.models.document_files import DocumentFiles
from boldsign.models.document_form_fields import DocumentFormFields
from boldsign.models.document_reassign import DocumentReassign
from boldsign.models.document_sender_detail import DocumentSenderDetail
from boldsign.models.document_signer_details import DocumentSignerDetails
from boldsign.models.form_group import FormGroup
from boldsign.models.recipient_notification_settings import RecipientNotificationSettings
from boldsign.models.reminder_settings import ReminderSettings
from typing import Optional, Set, Tuple
from typing_extensions import Self
import io
from pydantic import StrictBool
from typing import Union

class DocumentProperties(BaseModel):
    """
    DocumentProperties
    """ # noqa: E501
    document_id: Optional[StrictStr] = Field(default=None, alias="documentId")
    brand_id: Optional[StrictStr] = Field(default=None, alias="brandId")
    message_title: Optional[StrictStr] = Field(default=None, alias="messageTitle")
    document_description: Optional[StrictStr] = Field(default=None, alias="documentDescription")
    status: Optional[StrictStr] = None
    files: Optional[List[DocumentFiles]] = None
    sender_detail: Optional[DocumentSenderDetail] = Field(default=None, alias="senderDetail")
    signer_details: Optional[List[DocumentSignerDetails]] = Field(default=None, alias="signerDetails")
    form_groups: Optional[List[FormGroup]] = Field(default=None, alias="formGroups")
    common_fields: Optional[List[DocumentFormFields]] = Field(default=None, alias="commonFields")
    behalf_of: Optional[BehalfOf] = Field(default=None, alias="behalfOf")
    cc_details: Optional[List[DocumentCcDetails]] = Field(default=None, alias="ccDetails")
    reminder_settings: Optional[ReminderSettings] = Field(default=None, alias="reminderSettings")
    reassign: Optional[List[DocumentReassign]] = None
    document_history: Optional[List[AuditTrail]] = Field(default=None, alias="documentHistory")
    activity_by: Optional[StrictStr] = Field(default=None, alias="activityBy")
    activity_date: Optional[StrictInt] = Field(default=None, alias="activityDate")
    activity_action: Optional[StrictStr] = Field(default=None, alias="activityAction")
    created_date: Optional[StrictInt] = Field(default=None, alias="createdDate")
    expiry_days: Optional[StrictInt] = Field(default=None, alias="expiryDays")
    expiry_date: Optional[StrictInt] = Field(default=None, alias="expiryDate")
    enable_signing_order: Optional[StrictBool] = Field(default=None, alias="enableSigningOrder")
    is_deleted: Optional[StrictBool] = Field(default=None, alias="isDeleted")
    revoke_message: Optional[StrictStr] = Field(default=None, alias="revokeMessage")
    decline_message: Optional[StrictStr] = Field(default=None, alias="declineMessage")
    application_id: Optional[StrictStr] = Field(default=None, alias="applicationId")
    labels: Optional[List[StrictStr]] = None
    disable_emails: Optional[StrictBool] = Field(default=None, alias="disableEmails")
    enable_print_and_sign: Optional[StrictBool] = Field(default=None, alias="enablePrintAndSign")
    enable_reassign: Optional[StrictBool] = Field(default=None, alias="enableReassign")
    disable_expiry_alert: Optional[StrictBool] = Field(default=None, alias="disableExpiryAlert")
    hide_document_id: Optional[StrictBool] = Field(default=None, alias="hideDocumentId")
    expiry_date_type: Optional[StrictStr] = Field(default=None, alias="expiryDateType")
    expiry_value: Optional[StrictInt] = Field(default=None, alias="expiryValue")
    document_download_option: Optional[StrictStr] = Field(default=None, alias="documentDownloadOption")
    meta_data: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, alias="metaData")
    recipient_notification_settings: Optional[RecipientNotificationSettings] = Field(default=None, alias="recipientNotificationSettings")
    enable_audit_trail_localization: Optional[StrictBool] = Field(default=None, alias="enableAuditTrailLocalization")
    download_file_name: Optional[StrictStr] = Field(default=None, alias="downloadFileName")
    scheduled_send_time: Optional[StrictInt] = Field(default=None, alias="scheduledSendTime")
    __properties: ClassVar[List[str]] = ["documentId", "brandId", "messageTitle", "documentDescription", "status", "files", "senderDetail", "signerDetails", "formGroups", "commonFields", "behalfOf", "ccDetails", "reminderSettings", "reassign", "documentHistory", "activityBy", "activityDate", "activityAction", "createdDate", "expiryDays", "expiryDate", "enableSigningOrder", "isDeleted", "revokeMessage", "declineMessage", "applicationId", "labels", "disableEmails", "enablePrintAndSign", "enableReassign", "disableExpiryAlert", "hideDocumentId", "expiryDateType", "expiryValue", "documentDownloadOption", "metaData", "recipientNotificationSettings", "enableAuditTrailLocalization", "downloadFileName", "scheduledSendTime"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['InProgress', 'Completed', 'Declined', 'Expired', 'Revoked', 'Draft', 'Scheduled']):
            raise ValueError("must be one of enum values ('InProgress', 'Completed', 'Declined', 'Expired', 'Revoked', 'Draft', 'Scheduled')")
        return value

    @field_validator('activity_action')
    def activity_action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Viewed', 'Signed', 'Reassigned', 'Declined', 'Revoked', 'Expired', 'Downloaded', 'DownloadedForPrintSign', 'InitiatePrintAndSign', 'InitiateFormSign', 'CancelPrintAndSign', 'CompletePrintAndSign', 'Reviewed', 'None', 'EditingInitiated', 'EditingCancelled', 'EditingCompleted', 'DocumentScheduled']):
            raise ValueError("must be one of enum values ('Viewed', 'Signed', 'Reassigned', 'Declined', 'Revoked', 'Expired', 'Downloaded', 'DownloadedForPrintSign', 'InitiatePrintAndSign', 'InitiateFormSign', 'CancelPrintAndSign', 'CompletePrintAndSign', 'Reviewed', 'None', 'EditingInitiated', 'EditingCancelled', 'EditingCompleted', 'DocumentScheduled')")
        return value

    @field_validator('expiry_date_type')
    def expiry_date_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Days', 'Hours', 'SpecificDateTime']):
            raise ValueError("must be one of enum values ('Days', 'Hours', 'SpecificDateTime')")
        return value

    @field_validator('document_download_option')
    def document_download_option_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Combined', 'Individually']):
            raise ValueError("must be one of enum values ('Combined', 'Individually')")
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
        """Create an instance of DocumentProperties from a JSON string"""
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
        """Create an instance of DocumentProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "documentId": obj.get("documentId"),
            "brandId": obj.get("brandId"),
            "messageTitle": obj.get("messageTitle"),
            "documentDescription": obj.get("documentDescription"),
            "status": obj.get("status"),
            "files": [DocumentFiles.from_dict(_item) for _item in obj["files"]] if obj.get("files") is not None else None,
            "senderDetail": DocumentSenderDetail.from_dict(obj["senderDetail"]) if obj.get("senderDetail") is not None else None,
            "signerDetails": [DocumentSignerDetails.from_dict(_item) for _item in obj["signerDetails"]] if obj.get("signerDetails") is not None else None,
            "formGroups": [FormGroup.from_dict(_item) for _item in obj["formGroups"]] if obj.get("formGroups") is not None else None,
            "commonFields": [DocumentFormFields.from_dict(_item) for _item in obj["commonFields"]] if obj.get("commonFields") is not None else None,
            "behalfOf": BehalfOf.from_dict(obj["behalfOf"]) if obj.get("behalfOf") is not None else None,
            "ccDetails": [DocumentCcDetails.from_dict(_item) for _item in obj["ccDetails"]] if obj.get("ccDetails") is not None else None,
            "reminderSettings": ReminderSettings.from_dict(obj["reminderSettings"]) if obj.get("reminderSettings") is not None else None,
            "reassign": [DocumentReassign.from_dict(_item) for _item in obj["reassign"]] if obj.get("reassign") is not None else None,
            "documentHistory": [AuditTrail.from_dict(_item) for _item in obj["documentHistory"]] if obj.get("documentHistory") is not None else None,
            "activityBy": obj.get("activityBy"),
            "activityDate": obj.get("activityDate"),
            "activityAction": obj.get("activityAction"),
            "createdDate": obj.get("createdDate"),
            "expiryDays": obj.get("expiryDays"),
            "expiryDate": obj.get("expiryDate"),
            "enableSigningOrder": obj.get("enableSigningOrder"),
            "isDeleted": obj.get("isDeleted"),
            "revokeMessage": obj.get("revokeMessage"),
            "declineMessage": obj.get("declineMessage"),
            "applicationId": obj.get("applicationId"),
            "labels": obj.get("labels"),
            "disableEmails": obj.get("disableEmails"),
            "enablePrintAndSign": obj.get("enablePrintAndSign"),
            "enableReassign": obj.get("enableReassign"),
            "disableExpiryAlert": obj.get("disableExpiryAlert"),
            "hideDocumentId": obj.get("hideDocumentId"),
            "expiryDateType": obj.get("expiryDateType"),
            "expiryValue": obj.get("expiryValue"),
            "documentDownloadOption": obj.get("documentDownloadOption"),
            "metaData": obj.get("metaData"),
            "recipientNotificationSettings": RecipientNotificationSettings.from_dict(obj["recipientNotificationSettings"]) if obj.get("recipientNotificationSettings") is not None else None,
            "enableAuditTrailLocalization": obj.get("enableAuditTrailLocalization"),
            "downloadFileName": obj.get("downloadFileName"),
            "scheduledSendTime": obj.get("scheduledSendTime")
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
            "document_id": "(str,)",
            "brand_id": "(str,)",
            "message_title": "(str,)",
            "document_description": "(str,)",
            "status": "(str,)",
            "files": "(List[DocumentFiles],)",
            "sender_detail": "(DocumentSenderDetail,)",
            "signer_details": "(List[DocumentSignerDetails],)",
            "form_groups": "(List[FormGroup],)",
            "common_fields": "(List[DocumentFormFields],)",
            "behalf_of": "(BehalfOf,)",
            "cc_details": "(List[DocumentCcDetails],)",
            "reminder_settings": "(ReminderSettings,)",
            "reassign": "(List[DocumentReassign],)",
            "document_history": "(List[AuditTrail],)",
            "activity_by": "(str,)",
            "activity_date": "(int,)",
            "activity_action": "(str,)",
            "created_date": "(int,)",
            "expiry_days": "(int,)",
            "expiry_date": "(int,)",
            "enable_signing_order": "(bool,)",
            "is_deleted": "(bool,)",
            "revoke_message": "(str,)",
            "decline_message": "(str,)",
            "application_id": "(str,)",
            "labels": "(List[str],)",
            "disable_emails": "(bool,)",
            "enable_print_and_sign": "(bool,)",
            "enable_reassign": "(bool,)",
            "disable_expiry_alert": "(bool,)",
            "hide_document_id": "(bool,)",
            "expiry_date_type": "(str,)",
            "expiry_value": "(int,)",
            "document_download_option": "(str,)",
            "meta_data": "(Dict[str, Optional[str]],)",
            "recipient_notification_settings": "(RecipientNotificationSettings,)",
            "enable_audit_trail_localization": "(bool,)",
            "download_file_name": "(str,)",
            "scheduled_send_time": "(int,)",
        }

    @classmethod
    def openapi_type_is_array(cls, property_name: str) -> bool:
        return property_name in [
            "files",
            "signer_details",
            "form_groups",
            "common_fields",
            "cc_details",
            "reassign",
            "document_history",
            "labels",
        ]

