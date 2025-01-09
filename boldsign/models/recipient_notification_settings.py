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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set, Tuple
from typing_extensions import Self
import io
from pydantic import StrictBool
from typing import Union

class RecipientNotificationSettings(BaseModel):
    """
    RecipientNotificationSettings
    """ # noqa: E501
    signature_request: Optional[StrictBool] = Field(default=True, alias="signatureRequest")
    declined: Optional[StrictBool] = True
    revoked: Optional[StrictBool] = True
    signed: Optional[StrictBool] = True
    completed: Optional[StrictBool] = True
    expired: Optional[StrictBool] = True
    reassigned: Optional[StrictBool] = True
    deleted: Optional[StrictBool] = True
    reminders: Optional[StrictBool] = True
    edit_recipient: Optional[StrictBool] = Field(default=True, alias="editRecipient")
    edit_document: Optional[StrictBool] = Field(default=True, alias="editDocument")
    __properties: ClassVar[List[str]] = ["signatureRequest", "declined", "revoked", "signed", "completed", "expired", "reassigned", "deleted", "reminders", "editRecipient", "editDocument"]

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
        """Create an instance of RecipientNotificationSettings from a JSON string"""
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
        """Create an instance of RecipientNotificationSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "signatureRequest": obj.get("signatureRequest") if obj.get("signatureRequest") is not None else True,
            "declined": obj.get("declined") if obj.get("declined") is not None else True,
            "revoked": obj.get("revoked") if obj.get("revoked") is not None else True,
            "signed": obj.get("signed") if obj.get("signed") is not None else True,
            "completed": obj.get("completed") if obj.get("completed") is not None else True,
            "expired": obj.get("expired") if obj.get("expired") is not None else True,
            "reassigned": obj.get("reassigned") if obj.get("reassigned") is not None else True,
            "deleted": obj.get("deleted") if obj.get("deleted") is not None else True,
            "reminders": obj.get("reminders") if obj.get("reminders") is not None else True,
            "editRecipient": obj.get("editRecipient") if obj.get("editRecipient") is not None else True,
            "editDocument": obj.get("editDocument") if obj.get("editDocument") is not None else True
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
            "signature_request": "(bool,)",
            "declined": "(bool,)",
            "revoked": "(bool,)",
            "signed": "(bool,)",
            "completed": "(bool,)",
            "expired": "(bool,)",
            "reassigned": "(bool,)",
            "deleted": "(bool,)",
            "reminders": "(bool,)",
            "edit_recipient": "(bool,)",
            "edit_document": "(bool,)",
        }

    @classmethod
    def openapi_type_is_array(cls, property_name: str) -> bool:
        return property_name in [
        ]
