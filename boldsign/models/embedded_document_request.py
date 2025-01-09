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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictBytes, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from boldsign.models.document_cc import DocumentCC
from boldsign.models.document_info import DocumentInfo
from boldsign.models.document_signer import DocumentSigner
from boldsign.models.form_group import FormGroup
from boldsign.models.reminder_settings import ReminderSettings
from boldsign.models.text_tag_definition import TextTagDefinition
from typing import Optional, Set, Tuple
from typing_extensions import Self
import io
from pydantic import StrictBool
from typing import Union

class EmbeddedDocumentRequest(BaseModel):
    """
    EmbeddedDocumentRequest
    """ # noqa: E501
    redirect_url: Optional[StrictStr] = Field(default=None, alias="redirectUrl")
    show_toolbar: Optional[StrictBool] = Field(default=False, alias="showToolbar")
    send_view_option: Optional[StrictStr] = Field(default='PreparePage', alias="sendViewOption")
    show_save_button: Optional[StrictBool] = Field(default=True, alias="showSaveButton")
    locale: Optional[StrictStr] = 'EN'
    show_send_button: Optional[StrictBool] = Field(default=True, alias="showSendButton")
    show_preview_button: Optional[StrictBool] = Field(default=True, alias="showPreviewButton")
    show_navigation_buttons: Optional[StrictBool] = Field(default=True, alias="showNavigationButtons")
    show_tooltip: Optional[StrictBool] = Field(default=False, alias="showTooltip")
    embedded_send_link_valid_till: Optional[datetime] = Field(default=None, alias="embeddedSendLinkValidTill")
    files: Optional[List[Union[StrictBytes, StrictStr]]] = None
    title: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=256)]] = None
    message: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=5000)]] = None
    signers: Optional[List[DocumentSigner]] = None
    cc: Optional[List[DocumentCC]] = None
    enable_signing_order: Optional[StrictBool] = Field(default=False, alias="enableSigningOrder")
    expiry_days: Optional[StrictInt] = Field(default=None, alias="expiryDays")
    expiry_date_type: Optional[StrictStr] = Field(default=None, alias="expiryDateType")
    expiry_value: Optional[StrictInt] = Field(default=60, alias="expiryValue")
    reminder_settings: Optional[ReminderSettings] = Field(default=None, alias="reminderSettings")
    enable_embedded_signing: Optional[StrictBool] = Field(default=False, alias="enableEmbeddedSigning")
    disable_emails: Optional[StrictBool] = Field(default=False, alias="disableEmails")
    disable_sms: Optional[StrictBool] = Field(default=False, alias="disableSMS")
    brand_id: Optional[StrictStr] = Field(default=None, alias="brandId")
    hide_document_id: Optional[StrictBool] = Field(default=False, alias="hideDocumentId")
    labels: Optional[List[StrictStr]] = None
    file_urls: Optional[List[StrictStr]] = Field(default=None, alias="fileUrls")
    send_link_valid_till: Optional[datetime] = Field(default=None, alias="sendLinkValidTill")
    use_text_tags: Optional[StrictBool] = Field(default=False, alias="useTextTags")
    text_tag_definitions: Optional[List[TextTagDefinition]] = Field(default=None, alias="textTagDefinitions")
    enable_print_and_sign: Optional[StrictBool] = Field(default=False, alias="enablePrintAndSign")
    enable_reassign: Optional[StrictBool] = Field(default=True, alias="enableReassign")
    disable_expiry_alert: Optional[StrictBool] = Field(default=None, alias="disableExpiryAlert")
    document_info: Optional[List[DocumentInfo]] = Field(default=None, alias="documentInfo")
    on_behalf_of: Optional[StrictStr] = Field(default=None, alias="onBehalfOf")
    auto_detect_fields: Optional[StrictBool] = Field(default=False, alias="AutoDetectFields")
    document_download_option: Optional[StrictStr] = Field(default=None, alias="documentDownloadOption")
    meta_data: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, alias="metaData")
    form_groups: Optional[List[FormGroup]] = Field(default=None, alias="formGroups")
    enable_audit_trail_localization: Optional[StrictBool] = Field(default=None, alias="enableAuditTrailLocalization")
    download_file_name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=250)]] = Field(default=None, alias="downloadFileName")
    __properties: ClassVar[List[str]] = ["redirectUrl", "showToolbar", "sendViewOption", "showSaveButton", "locale", "showSendButton", "showPreviewButton", "showNavigationButtons", "showTooltip", "embeddedSendLinkValidTill", "files", "title", "message", "signers", "cc", "enableSigningOrder", "expiryDays", "expiryDateType", "expiryValue", "reminderSettings", "enableEmbeddedSigning", "disableEmails", "disableSMS", "brandId", "hideDocumentId", "labels", "fileUrls", "sendLinkValidTill", "useTextTags", "textTagDefinitions", "enablePrintAndSign", "enableReassign", "disableExpiryAlert", "documentInfo", "onBehalfOf", "AutoDetectFields", "documentDownloadOption", "metaData", "formGroups", "enableAuditTrailLocalization", "downloadFileName"]

    @field_validator('send_view_option')
    def send_view_option_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PreparePage', 'FillingPage']):
            raise ValueError("must be one of enum values ('PreparePage', 'FillingPage')")
        return value

    @field_validator('locale')
    def locale_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['EN', 'NO', 'FR', 'DE', 'ES', 'BG', 'CS', 'DA', 'IT', 'NL', 'PL', 'PT', 'RO', 'RU', 'SV', 'Default']):
            raise ValueError("must be one of enum values ('EN', 'NO', 'FR', 'DE', 'ES', 'BG', 'CS', 'DA', 'IT', 'NL', 'PL', 'PT', 'RO', 'RU', 'SV', 'Default')")
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
        """Create an instance of EmbeddedDocumentRequest from a JSON string"""
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
        """Create an instance of EmbeddedDocumentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "redirectUrl": obj.get("redirectUrl"),
            "showToolbar": obj.get("showToolbar") if obj.get("showToolbar") is not None else False,
            "sendViewOption": obj.get("sendViewOption") if obj.get("sendViewOption") is not None else 'PreparePage',
            "showSaveButton": obj.get("showSaveButton") if obj.get("showSaveButton") is not None else True,
            "locale": obj.get("locale") if obj.get("locale") is not None else 'EN',
            "showSendButton": obj.get("showSendButton") if obj.get("showSendButton") is not None else True,
            "showPreviewButton": obj.get("showPreviewButton") if obj.get("showPreviewButton") is not None else True,
            "showNavigationButtons": obj.get("showNavigationButtons") if obj.get("showNavigationButtons") is not None else True,
            "showTooltip": obj.get("showTooltip") if obj.get("showTooltip") is not None else False,
            "embeddedSendLinkValidTill": obj.get("embeddedSendLinkValidTill"),
            "files": obj.get("files"),
            "title": obj.get("title"),
            "message": obj.get("message"),
            "signers": [DocumentSigner.from_dict(_item) for _item in obj["signers"]] if obj.get("signers") is not None else None,
            "cc": [DocumentCC.from_dict(_item) for _item in obj["cc"]] if obj.get("cc") is not None else None,
            "enableSigningOrder": obj.get("enableSigningOrder") if obj.get("enableSigningOrder") is not None else False,
            "expiryDays": obj.get("expiryDays"),
            "expiryDateType": obj.get("expiryDateType"),
            "expiryValue": obj.get("expiryValue") if obj.get("expiryValue") is not None else 60,
            "reminderSettings": ReminderSettings.from_dict(obj["reminderSettings"]) if obj.get("reminderSettings") is not None else None,
            "enableEmbeddedSigning": obj.get("enableEmbeddedSigning") if obj.get("enableEmbeddedSigning") is not None else False,
            "disableEmails": obj.get("disableEmails") if obj.get("disableEmails") is not None else False,
            "disableSMS": obj.get("disableSMS") if obj.get("disableSMS") is not None else False,
            "brandId": obj.get("brandId"),
            "hideDocumentId": obj.get("hideDocumentId") if obj.get("hideDocumentId") is not None else False,
            "labels": obj.get("labels"),
            "fileUrls": obj.get("fileUrls"),
            "sendLinkValidTill": obj.get("sendLinkValidTill"),
            "useTextTags": obj.get("useTextTags") if obj.get("useTextTags") is not None else False,
            "textTagDefinitions": [TextTagDefinition.from_dict(_item) for _item in obj["textTagDefinitions"]] if obj.get("textTagDefinitions") is not None else None,
            "enablePrintAndSign": obj.get("enablePrintAndSign") if obj.get("enablePrintAndSign") is not None else False,
            "enableReassign": obj.get("enableReassign") if obj.get("enableReassign") is not None else True,
            "disableExpiryAlert": obj.get("disableExpiryAlert"),
            "documentInfo": [DocumentInfo.from_dict(_item) for _item in obj["documentInfo"]] if obj.get("documentInfo") is not None else None,
            "onBehalfOf": obj.get("onBehalfOf"),
            "AutoDetectFields": obj.get("AutoDetectFields") if obj.get("AutoDetectFields") is not None else False,
            "documentDownloadOption": obj.get("documentDownloadOption"),
            "metaData": obj.get("metaData"),
            "formGroups": [FormGroup.from_dict(_item) for _item in obj["formGroups"]] if obj.get("formGroups") is not None else None,
            "enableAuditTrailLocalization": obj.get("enableAuditTrailLocalization"),
            "downloadFileName": obj.get("downloadFileName")
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
            "redirect_url": "(str,)",
            "show_toolbar": "(bool,)",
            "send_view_option": "(str,)",
            "show_save_button": "(bool,)",
            "locale": "(str,)",
            "show_send_button": "(bool,)",
            "show_preview_button": "(bool,)",
            "show_navigation_buttons": "(bool,)",
            "show_tooltip": "(bool,)",
            "embedded_send_link_valid_till": "(datetime,)",
            "files": "(List[io.IOBase],)",
            "title": "(str,)",
            "message": "(str,)",
            "signers": "(List[DocumentSigner],)",
            "cc": "(List[DocumentCC],)",
            "enable_signing_order": "(bool,)",
            "expiry_days": "(int,)",
            "expiry_date_type": "(str,)",
            "expiry_value": "(int,)",
            "reminder_settings": "(ReminderSettings,)",
            "enable_embedded_signing": "(bool,)",
            "disable_emails": "(bool,)",
            "disable_sms": "(bool,)",
            "brand_id": "(str,)",
            "hide_document_id": "(bool,)",
            "labels": "(List[str],)",
            "file_urls": "(List[str],)",
            "send_link_valid_till": "(datetime,)",
            "use_text_tags": "(bool,)",
            "text_tag_definitions": "(List[TextTagDefinition],)",
            "enable_print_and_sign": "(bool,)",
            "enable_reassign": "(bool,)",
            "disable_expiry_alert": "(bool,)",
            "document_info": "(List[DocumentInfo],)",
            "on_behalf_of": "(str,)",
            "auto_detect_fields": "(bool,)",
            "document_download_option": "(str,)",
            "meta_data": "(Dict[str, Optional[str]],)",
            "form_groups": "(List[FormGroup],)",
            "enable_audit_trail_localization": "(bool,)",
            "download_file_name": "(str,)",
        }

    @classmethod
    def openapi_type_is_array(cls, property_name: str) -> bool:
        return property_name in [
            "files",
            "signers",
            "cc",
            "labels",
            "file_urls",
            "text_tag_definitions",
            "document_info",
            "form_groups",
        ]

