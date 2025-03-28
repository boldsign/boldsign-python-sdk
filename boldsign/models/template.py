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
from boldsign.models.behalf_of import BehalfOf
from boldsign.models.template_cc import TemplateCC
from boldsign.models.template_sender_details import TemplateSenderDetails
from boldsign.models.template_signer_details import TemplateSignerDetails
from typing import Optional, Set, Tuple
from typing_extensions import Self
import io
from pydantic import StrictBool
from typing import Union

class Template(BaseModel):
    """
    Template
    """ # noqa: E501
    document_id: Optional[StrictStr] = Field(default=None, alias="documentId")
    sender_detail: Optional[TemplateSenderDetails] = Field(default=None, alias="senderDetail")
    cc_details: Optional[List[TemplateCC]] = Field(default=None, alias="ccDetails")
    created_date: Optional[StrictInt] = Field(default=None, alias="createdDate")
    activity_date: Optional[StrictInt] = Field(default=None, alias="activityDate")
    activity_by: Optional[StrictStr] = Field(default=None, alias="activityBy")
    message_title: Optional[StrictStr] = Field(default=None, alias="messageTitle")
    status: Optional[StrictStr] = None
    signer_details: Optional[List[TemplateSignerDetails]] = Field(default=None, alias="signerDetails")
    enable_signing_order: Optional[StrictBool] = Field(default=None, alias="enableSigningOrder")
    template_name: Optional[StrictStr] = Field(default=None, alias="templateName")
    template_description: Optional[StrictStr] = Field(default=None, alias="templateDescription")
    access_type: Optional[StrictStr] = Field(default=None, alias="accessType")
    access_tid: Optional[StrictStr] = Field(default=None, alias="accessTid")
    is_template: Optional[StrictBool] = Field(default=False, alias="isTemplate")
    behalf_of: Optional[BehalfOf] = Field(default=None, alias="behalfOf")
    template_labels: Optional[List[StrictStr]] = Field(default=None, alias="templateLabels")
    labels: Optional[List[StrictStr]] = None
    brand_id: Optional[StrictStr] = Field(default=None, alias="brandId")
    __properties: ClassVar[List[str]] = ["documentId", "senderDetail", "ccDetails", "createdDate", "activityDate", "activityBy", "messageTitle", "status", "signerDetails", "enableSigningOrder", "templateName", "templateDescription", "accessType", "accessTid", "isTemplate", "behalfOf", "templateLabels", "labels", "brandId"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['InProgress', 'Completed', 'Declined', 'Expired', 'Revoked', 'Draft', 'Scheduled']):
            raise ValueError("must be one of enum values ('InProgress', 'Completed', 'Declined', 'Expired', 'Revoked', 'Draft', 'Scheduled')")
        return value

    @field_validator('access_type')
    def access_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Use', 'Edit', 'None']):
            raise ValueError("must be one of enum values ('Use', 'Edit', 'None')")
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
        """Create an instance of Template from a JSON string"""
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
        """Create an instance of Template from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "documentId": obj.get("documentId"),
            "senderDetail": TemplateSenderDetails.from_dict(obj["senderDetail"]) if obj.get("senderDetail") is not None else None,
            "ccDetails": [TemplateCC.from_dict(_item) for _item in obj["ccDetails"]] if obj.get("ccDetails") is not None else None,
            "createdDate": obj.get("createdDate"),
            "activityDate": obj.get("activityDate"),
            "activityBy": obj.get("activityBy"),
            "messageTitle": obj.get("messageTitle"),
            "status": obj.get("status"),
            "signerDetails": [TemplateSignerDetails.from_dict(_item) for _item in obj["signerDetails"]] if obj.get("signerDetails") is not None else None,
            "enableSigningOrder": obj.get("enableSigningOrder"),
            "templateName": obj.get("templateName"),
            "templateDescription": obj.get("templateDescription"),
            "accessType": obj.get("accessType"),
            "accessTid": obj.get("accessTid"),
            "isTemplate": obj.get("isTemplate") if obj.get("isTemplate") is not None else False,
            "behalfOf": BehalfOf.from_dict(obj["behalfOf"]) if obj.get("behalfOf") is not None else None,
            "templateLabels": obj.get("templateLabels"),
            "labels": obj.get("labels"),
            "brandId": obj.get("brandId")
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
            "sender_detail": "(TemplateSenderDetails,)",
            "cc_details": "(List[TemplateCC],)",
            "created_date": "(int,)",
            "activity_date": "(int,)",
            "activity_by": "(str,)",
            "message_title": "(str,)",
            "status": "(str,)",
            "signer_details": "(List[TemplateSignerDetails],)",
            "enable_signing_order": "(bool,)",
            "template_name": "(str,)",
            "template_description": "(str,)",
            "access_type": "(str,)",
            "access_tid": "(str,)",
            "is_template": "(bool,)",
            "behalf_of": "(BehalfOf,)",
            "template_labels": "(List[str],)",
            "labels": "(List[str],)",
            "brand_id": "(str,)",
        }

    @classmethod
    def openapi_type_is_array(cls, property_name: str) -> bool:
        return property_name in [
            "cc_details",
            "signer_details",
            "template_labels",
            "labels",
        ]

