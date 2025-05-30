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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from boldsign.models.custom_domain_settings import CustomDomainSettings
from boldsign.models.document_expiry_settings import DocumentExpirySettings
from typing import Optional, Set, Tuple
from typing_extensions import Self
import io
from pydantic import StrictBool
from typing import Union

class ViewBrandDetails(BaseModel):
    """
    ViewBrandDetails
    """ # noqa: E501
    brand_id: Optional[StrictStr] = Field(default=None, alias="brandId")
    brand_logo: Optional[StrictStr] = Field(default=None, alias="brandLogo")
    brand_name: Optional[StrictStr] = Field(default=None, alias="brandName")
    background_color: Optional[StrictStr] = Field(default=None, alias="backgroundColor")
    button_color: Optional[StrictStr] = Field(default=None, alias="buttonColor")
    button_text_color: Optional[StrictStr] = Field(default=None, alias="buttonTextColor")
    email_display_name: Optional[StrictStr] = Field(default=None, alias="emailDisplayName")
    disclaimer_title: Optional[StrictStr] = Field(default=None, alias="disclaimerTitle")
    disclaimer_description: Optional[StrictStr] = Field(default=None, alias="disclaimerDescription")
    redirect_url: Optional[StrictStr] = Field(default=None, alias="redirectUrl")
    is_default: Optional[StrictBool] = Field(default=None, alias="isDefault")
    can_hide_tag_line: Optional[StrictBool] = Field(default=None, alias="canHideTagLine")
    combine_audit_trail: Optional[StrictBool] = Field(default=None, alias="combineAuditTrail")
    exclude_audit_trail_from_email: Optional[StrictBool] = Field(default=None, alias="excludeAuditTrailFromEmail")
    email_signed_document: Optional[StrictStr] = Field(default=None, alias="emailSignedDocument")
    document_time_zone: Optional[StrictStr] = Field(default=None, alias="documentTimeZone")
    show_built_in_form_fields: Optional[StrictBool] = Field(default=None, alias="showBuiltInFormFields")
    allow_custom_field_creation: Optional[StrictBool] = Field(default=None, alias="allowCustomFieldCreation")
    show_shared_custom_fields: Optional[StrictBool] = Field(default=None, alias="showSharedCustomFields")
    hide_decline: Optional[StrictBool] = Field(default=None, alias="hideDecline")
    hide_save: Optional[StrictBool] = Field(default=None, alias="hideSave")
    document_expiry_settings: Optional[DocumentExpirySettings] = Field(default=None, alias="documentExpirySettings")
    custom_domain_settings: Optional[CustomDomainSettings] = Field(default=None, alias="customDomainSettings")
    is_domain_verified: Optional[StrictBool] = Field(default=None, alias="isDomainVerified")
    __properties: ClassVar[List[str]] = ["brandId", "brandLogo", "brandName", "backgroundColor", "buttonColor", "buttonTextColor", "emailDisplayName", "disclaimerTitle", "disclaimerDescription", "redirectUrl", "isDefault", "canHideTagLine", "combineAuditTrail", "excludeAuditTrailFromEmail", "emailSignedDocument", "documentTimeZone", "showBuiltInFormFields", "allowCustomFieldCreation", "showSharedCustomFields", "hideDecline", "hideSave", "documentExpirySettings", "customDomainSettings", "isDomainVerified"]

    @field_validator('email_signed_document')
    def email_signed_document_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Attachment', 'DocumentLink']):
            raise ValueError("must be one of enum values ('Attachment', 'DocumentLink')")
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
        """Create an instance of ViewBrandDetails from a JSON string"""
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
        """Create an instance of ViewBrandDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "brandId": obj.get("brandId"),
            "brandLogo": obj.get("brandLogo"),
            "brandName": obj.get("brandName"),
            "backgroundColor": obj.get("backgroundColor"),
            "buttonColor": obj.get("buttonColor"),
            "buttonTextColor": obj.get("buttonTextColor"),
            "emailDisplayName": obj.get("emailDisplayName"),
            "disclaimerTitle": obj.get("disclaimerTitle"),
            "disclaimerDescription": obj.get("disclaimerDescription"),
            "redirectUrl": obj.get("redirectUrl"),
            "isDefault": obj.get("isDefault"),
            "canHideTagLine": obj.get("canHideTagLine"),
            "combineAuditTrail": obj.get("combineAuditTrail"),
            "excludeAuditTrailFromEmail": obj.get("excludeAuditTrailFromEmail"),
            "emailSignedDocument": obj.get("emailSignedDocument"),
            "documentTimeZone": obj.get("documentTimeZone"),
            "showBuiltInFormFields": obj.get("showBuiltInFormFields"),
            "allowCustomFieldCreation": obj.get("allowCustomFieldCreation"),
            "showSharedCustomFields": obj.get("showSharedCustomFields"),
            "hideDecline": obj.get("hideDecline"),
            "hideSave": obj.get("hideSave"),
            "documentExpirySettings": DocumentExpirySettings.from_dict(obj["documentExpirySettings"]) if obj.get("documentExpirySettings") is not None else None,
            "customDomainSettings": CustomDomainSettings.from_dict(obj["customDomainSettings"]) if obj.get("customDomainSettings") is not None else None,
            "isDomainVerified": obj.get("isDomainVerified")
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
            "brand_id": "(str,)",
            "brand_logo": "(str,)",
            "brand_name": "(str,)",
            "background_color": "(str,)",
            "button_color": "(str,)",
            "button_text_color": "(str,)",
            "email_display_name": "(str,)",
            "disclaimer_title": "(str,)",
            "disclaimer_description": "(str,)",
            "redirect_url": "(str,)",
            "is_default": "(bool,)",
            "can_hide_tag_line": "(bool,)",
            "combine_audit_trail": "(bool,)",
            "exclude_audit_trail_from_email": "(bool,)",
            "email_signed_document": "(str,)",
            "document_time_zone": "(str,)",
            "show_built_in_form_fields": "(bool,)",
            "allow_custom_field_creation": "(bool,)",
            "show_shared_custom_fields": "(bool,)",
            "hide_decline": "(bool,)",
            "hide_save": "(bool,)",
            "document_expiry_settings": "(DocumentExpirySettings,)",
            "custom_domain_settings": "(CustomDomainSettings,)",
            "is_domain_verified": "(bool,)",
        }

    @classmethod
    def openapi_type_is_array(cls, property_name: str) -> bool:
        return property_name in [
        ]

