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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictBytes, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from boldsign.models.document_cc import DocumentCC
from boldsign.models.document_info import DocumentInfo
from boldsign.models.form_group import FormGroup
from boldsign.models.reminder_settings import ReminderSettings
from boldsign.models.role import Role
from typing import Optional, Set, Tuple
from typing_extensions import Self
import io
from pydantic import StrictBool
from typing import Union

class SendForSignFromTemplateForm(BaseModel):
    """
    SendForSignFromTemplateForm
    """ # noqa: E501
    files: Optional[List[Union[StrictBytes, StrictStr]]] = None
    file_urls: Optional[List[StrictStr]] = Field(default=None, alias="fileUrls")
    document_id: Optional[StrictStr] = Field(default=None, alias="documentId")
    title: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=256)]] = None
    message: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=5000)]] = None
    roles: Optional[List[Role]] = None
    brand_id: Optional[StrictStr] = Field(default=None, alias="brandId")
    labels: Optional[List[StrictStr]] = None
    disable_emails: Optional[StrictBool] = Field(default=None, alias="disableEmails")
    disable_sms: Optional[StrictBool] = Field(default=False, alias="disableSMS")
    hide_document_id: Optional[StrictBool] = Field(default=None, alias="hideDocumentId")
    reminder_settings: Optional[ReminderSettings] = Field(default=None, alias="reminderSettings")
    cc: Optional[List[DocumentCC]] = None
    expiry_days: Optional[StrictInt] = Field(default=None, alias="expiryDays")
    expiry_date_type: Optional[StrictStr] = Field(default=None, alias="expiryDateType")
    expiry_value: Optional[StrictInt] = Field(default=60, alias="expiryValue")
    enable_print_and_sign: Optional[StrictBool] = Field(default=None, alias="enablePrintAndSign")
    enable_reassign: Optional[StrictBool] = Field(default=None, alias="enableReassign")
    enable_signing_order: Optional[StrictBool] = Field(default=None, alias="enableSigningOrder")
    disable_expiry_alert: Optional[StrictBool] = Field(default=None, alias="disableExpiryAlert")
    document_info: Optional[List[DocumentInfo]] = Field(default=None, alias="documentInfo")
    on_behalf_of: Optional[StrictStr] = Field(default=None, alias="onBehalfOf")
    is_sandbox: Optional[StrictBool] = Field(default=None, alias="isSandbox")
    role_removal_indices: Optional[List[StrictInt]] = Field(default=None, alias="roleRemovalIndices")
    document_download_option: Optional[StrictStr] = Field(default=None, alias="documentDownloadOption")
    meta_data: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, alias="metaData")
    form_groups: Optional[List[FormGroup]] = Field(default=None, alias="formGroups")
    remove_form_fields: Optional[List[StrictStr]] = Field(default=None, alias="removeFormFields")
    enable_audit_trail_localization: Optional[StrictBool] = Field(default=None, alias="enableAuditTrailLocalization")
    download_file_name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=250)]] = Field(default=None, alias="downloadFileName")
    __properties: ClassVar[List[str]] = ["files", "fileUrls", "documentId", "title", "message", "roles", "brandId", "labels", "disableEmails", "disableSMS", "hideDocumentId", "reminderSettings", "cc", "expiryDays", "expiryDateType", "expiryValue", "enablePrintAndSign", "enableReassign", "enableSigningOrder", "disableExpiryAlert", "documentInfo", "onBehalfOf", "isSandbox", "roleRemovalIndices", "documentDownloadOption", "metaData", "formGroups", "removeFormFields", "enableAuditTrailLocalization", "downloadFileName"]

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
        """Create an instance of SendForSignFromTemplateForm from a JSON string"""
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
        """Create an instance of SendForSignFromTemplateForm from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "files": obj.get("files"),
            "fileUrls": obj.get("fileUrls"),
            "documentId": obj.get("documentId"),
            "title": obj.get("title"),
            "message": obj.get("message"),
            "roles": [Role.from_dict(_item) for _item in obj["roles"]] if obj.get("roles") is not None else None,
            "brandId": obj.get("brandId"),
            "labels": obj.get("labels"),
            "disableEmails": obj.get("disableEmails"),
            "disableSMS": obj.get("disableSMS") if obj.get("disableSMS") is not None else False,
            "hideDocumentId": obj.get("hideDocumentId"),
            "reminderSettings": ReminderSettings.from_dict(obj["reminderSettings"]) if obj.get("reminderSettings") is not None else None,
            "cc": [DocumentCC.from_dict(_item) for _item in obj["cc"]] if obj.get("cc") is not None else None,
            "expiryDays": obj.get("expiryDays"),
            "expiryDateType": obj.get("expiryDateType"),
            "expiryValue": obj.get("expiryValue") if obj.get("expiryValue") is not None else 60,
            "enablePrintAndSign": obj.get("enablePrintAndSign"),
            "enableReassign": obj.get("enableReassign"),
            "enableSigningOrder": obj.get("enableSigningOrder"),
            "disableExpiryAlert": obj.get("disableExpiryAlert"),
            "documentInfo": [DocumentInfo.from_dict(_item) for _item in obj["documentInfo"]] if obj.get("documentInfo") is not None else None,
            "onBehalfOf": obj.get("onBehalfOf"),
            "isSandbox": obj.get("isSandbox"),
            "roleRemovalIndices": obj.get("roleRemovalIndices"),
            "documentDownloadOption": obj.get("documentDownloadOption"),
            "metaData": obj.get("metaData"),
            "formGroups": [FormGroup.from_dict(_item) for _item in obj["formGroups"]] if obj.get("formGroups") is not None else None,
            "removeFormFields": obj.get("removeFormFields"),
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
            "files": "(List[io.IOBase],)",
            "file_urls": "(List[str],)",
            "document_id": "(str,)",
            "title": "(str,)",
            "message": "(str,)",
            "roles": "(List[Role],)",
            "brand_id": "(str,)",
            "labels": "(List[str],)",
            "disable_emails": "(bool,)",
            "disable_sms": "(bool,)",
            "hide_document_id": "(bool,)",
            "reminder_settings": "(ReminderSettings,)",
            "cc": "(List[DocumentCC],)",
            "expiry_days": "(int,)",
            "expiry_date_type": "(str,)",
            "expiry_value": "(int,)",
            "enable_print_and_sign": "(bool,)",
            "enable_reassign": "(bool,)",
            "enable_signing_order": "(bool,)",
            "disable_expiry_alert": "(bool,)",
            "document_info": "(List[DocumentInfo],)",
            "on_behalf_of": "(str,)",
            "is_sandbox": "(bool,)",
            "role_removal_indices": "(List[int],)",
            "document_download_option": "(str,)",
            "meta_data": "(Dict[str, Optional[str]],)",
            "form_groups": "(List[FormGroup],)",
            "remove_form_fields": "(List[str],)",
            "enable_audit_trail_localization": "(bool,)",
            "download_file_name": "(str,)",
        }

    @classmethod
    def openapi_type_is_array(cls, property_name: str) -> bool:
        return property_name in [
            "files",
            "file_urls",
            "roles",
            "labels",
            "cc",
            "document_info",
            "role_removal_indices",
            "form_groups",
            "remove_form_fields",
        ]

