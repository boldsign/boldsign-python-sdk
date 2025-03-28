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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictBytes, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from boldsign.models.document_cc import DocumentCC
from boldsign.models.document_info import DocumentInfo
from boldsign.models.form_group import FormGroup
from boldsign.models.recipient_notification_settings import RecipientNotificationSettings
from boldsign.models.template_role import TemplateRole
from boldsign.models.text_tag_definition import TextTagDefinition
from typing import Optional, Set, Tuple
from typing_extensions import Self
import io
from pydantic import StrictBool
from typing import Union

class EmbeddedCreateTemplateRequest(BaseModel):
    """
    EmbeddedCreateTemplateRequest
    """ # noqa: E501
    title: Annotated[str, Field(min_length=0, strict=True, max_length=256)]
    redirect_url: Optional[StrictStr] = Field(default=None, alias="redirectUrl")
    show_toolbar: Optional[StrictBool] = Field(default=False, alias="showToolbar")
    view_option: Optional[StrictStr] = Field(default='PreparePage', alias="viewOption")
    show_save_button: Optional[StrictBool] = Field(default=True, alias="showSaveButton")
    locale: Optional[StrictStr] = 'EN'
    show_send_button: Optional[StrictBool] = Field(default=None, alias="showSendButton")
    show_create_button: Optional[StrictBool] = Field(default=True, alias="showCreateButton")
    show_preview_button: Optional[StrictBool] = Field(default=True, alias="showPreviewButton")
    show_navigation_buttons: Optional[StrictBool] = Field(default=True, alias="showNavigationButtons")
    link_valid_till: Optional[datetime] = Field(default=None, alias="linkValidTill")
    show_tooltip: Optional[StrictBool] = Field(default=False, alias="showTooltip")
    description: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=5000)]] = None
    document_title: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=256)]] = Field(default=None, alias="documentTitle")
    document_message: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=5000)]] = Field(default=None, alias="documentMessage")
    files: Optional[List[Union[StrictBytes, StrictStr]]] = None
    file_urls: Optional[List[StrictStr]] = Field(default=None, alias="fileUrls")
    roles: Optional[List[TemplateRole]] = None
    allow_modify_files: Optional[StrictBool] = Field(default=True, alias="allowModifyFiles")
    cc: Optional[List[DocumentCC]] = None
    brand_id: Optional[StrictStr] = Field(default=None, alias="brandId")
    allow_message_editing: Optional[StrictBool] = Field(default=True, alias="allowMessageEditing")
    allow_new_roles: Optional[StrictBool] = Field(default=True, alias="allowNewRoles")
    allow_new_files: Optional[StrictBool] = Field(default=True, alias="allowNewFiles")
    enable_reassign: Optional[StrictBool] = Field(default=True, alias="enableReassign")
    enable_print_and_assign: Optional[StrictBool] = Field(default=False, alias="enablePrintAndAssign")
    enable_signing_order: Optional[StrictBool] = Field(default=False, alias="enableSigningOrder")
    document_info: Optional[List[DocumentInfo]] = Field(default=None, alias="documentInfo")
    use_text_tags: Optional[StrictBool] = Field(default=False, alias="useTextTags")
    text_tag_definitions: Optional[List[TextTagDefinition]] = Field(default=None, alias="textTagDefinitions")
    auto_detect_fields: Optional[StrictBool] = Field(default=False, alias="autoDetectFields")
    on_behalf_of: Optional[StrictStr] = Field(default=None, alias="onBehalfOf")
    labels: Optional[List[StrictStr]] = None
    template_labels: Optional[List[StrictStr]] = Field(default=None, alias="templateLabels")
    recipient_notification_settings: Optional[RecipientNotificationSettings] = Field(default=None, alias="recipientNotificationSettings")
    form_groups: Optional[List[FormGroup]] = Field(default=None, alias="formGroups")
    __properties: ClassVar[List[str]] = ["title", "redirectUrl", "showToolbar", "viewOption", "showSaveButton", "locale", "showSendButton", "showCreateButton", "showPreviewButton", "showNavigationButtons", "linkValidTill", "showTooltip", "description", "documentTitle", "documentMessage", "files", "fileUrls", "roles", "allowModifyFiles", "cc", "brandId", "allowMessageEditing", "allowNewRoles", "allowNewFiles", "enableReassign", "enablePrintAndAssign", "enableSigningOrder", "documentInfo", "useTextTags", "textTagDefinitions", "autoDetectFields", "onBehalfOf", "labels", "templateLabels", "recipientNotificationSettings", "formGroups"]

    @field_validator('view_option')
    def view_option_validate_enum(cls, value):
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
        """Create an instance of EmbeddedCreateTemplateRequest from a JSON string"""
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
        """Create an instance of EmbeddedCreateTemplateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "redirectUrl": obj.get("redirectUrl"),
            "showToolbar": obj.get("showToolbar") if obj.get("showToolbar") is not None else False,
            "viewOption": obj.get("viewOption") if obj.get("viewOption") is not None else 'PreparePage',
            "showSaveButton": obj.get("showSaveButton") if obj.get("showSaveButton") is not None else True,
            "locale": obj.get("locale") if obj.get("locale") is not None else 'EN',
            "showSendButton": obj.get("showSendButton"),
            "showCreateButton": obj.get("showCreateButton") if obj.get("showCreateButton") is not None else True,
            "showPreviewButton": obj.get("showPreviewButton") if obj.get("showPreviewButton") is not None else True,
            "showNavigationButtons": obj.get("showNavigationButtons") if obj.get("showNavigationButtons") is not None else True,
            "linkValidTill": obj.get("linkValidTill"),
            "showTooltip": obj.get("showTooltip") if obj.get("showTooltip") is not None else False,
            "description": obj.get("description"),
            "documentTitle": obj.get("documentTitle"),
            "documentMessage": obj.get("documentMessage"),
            "files": obj.get("files"),
            "fileUrls": obj.get("fileUrls"),
            "roles": [TemplateRole.from_dict(_item) for _item in obj["roles"]] if obj.get("roles") is not None else None,
            "allowModifyFiles": obj.get("allowModifyFiles") if obj.get("allowModifyFiles") is not None else True,
            "cc": [DocumentCC.from_dict(_item) for _item in obj["cc"]] if obj.get("cc") is not None else None,
            "brandId": obj.get("brandId"),
            "allowMessageEditing": obj.get("allowMessageEditing") if obj.get("allowMessageEditing") is not None else True,
            "allowNewRoles": obj.get("allowNewRoles") if obj.get("allowNewRoles") is not None else True,
            "allowNewFiles": obj.get("allowNewFiles") if obj.get("allowNewFiles") is not None else True,
            "enableReassign": obj.get("enableReassign") if obj.get("enableReassign") is not None else True,
            "enablePrintAndAssign": obj.get("enablePrintAndAssign") if obj.get("enablePrintAndAssign") is not None else False,
            "enableSigningOrder": obj.get("enableSigningOrder") if obj.get("enableSigningOrder") is not None else False,
            "documentInfo": [DocumentInfo.from_dict(_item) for _item in obj["documentInfo"]] if obj.get("documentInfo") is not None else None,
            "useTextTags": obj.get("useTextTags") if obj.get("useTextTags") is not None else False,
            "textTagDefinitions": [TextTagDefinition.from_dict(_item) for _item in obj["textTagDefinitions"]] if obj.get("textTagDefinitions") is not None else None,
            "autoDetectFields": obj.get("autoDetectFields") if obj.get("autoDetectFields") is not None else False,
            "onBehalfOf": obj.get("onBehalfOf"),
            "labels": obj.get("labels"),
            "templateLabels": obj.get("templateLabels"),
            "recipientNotificationSettings": RecipientNotificationSettings.from_dict(obj["recipientNotificationSettings"]) if obj.get("recipientNotificationSettings") is not None else None,
            "formGroups": [FormGroup.from_dict(_item) for _item in obj["formGroups"]] if obj.get("formGroups") is not None else None
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
            "title": "(str,)",
            "redirect_url": "(str,)",
            "show_toolbar": "(bool,)",
            "view_option": "(str,)",
            "show_save_button": "(bool,)",
            "locale": "(str,)",
            "show_send_button": "(bool,)",
            "show_create_button": "(bool,)",
            "show_preview_button": "(bool,)",
            "show_navigation_buttons": "(bool,)",
            "link_valid_till": "(datetime,)",
            "show_tooltip": "(bool,)",
            "description": "(str,)",
            "document_title": "(str,)",
            "document_message": "(str,)",
            "files": "(List[io.IOBase],)",
            "file_urls": "(List[str],)",
            "roles": "(List[TemplateRole],)",
            "allow_modify_files": "(bool,)",
            "cc": "(List[DocumentCC],)",
            "brand_id": "(str,)",
            "allow_message_editing": "(bool,)",
            "allow_new_roles": "(bool,)",
            "allow_new_files": "(bool,)",
            "enable_reassign": "(bool,)",
            "enable_print_and_assign": "(bool,)",
            "enable_signing_order": "(bool,)",
            "document_info": "(List[DocumentInfo],)",
            "use_text_tags": "(bool,)",
            "text_tag_definitions": "(List[TextTagDefinition],)",
            "auto_detect_fields": "(bool,)",
            "on_behalf_of": "(str,)",
            "labels": "(List[str],)",
            "template_labels": "(List[str],)",
            "recipient_notification_settings": "(RecipientNotificationSettings,)",
            "form_groups": "(List[FormGroup],)",
        }

    @classmethod
    def openapi_type_is_array(cls, property_name: str) -> bool:
        return property_name in [
            "files",
            "file_urls",
            "roles",
            "cc",
            "document_info",
            "text_tag_definitions",
            "labels",
            "template_labels",
            "form_groups",
        ]

