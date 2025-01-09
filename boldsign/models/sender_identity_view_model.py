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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from boldsign.models.notification_settings import NotificationSettings
from typing import Optional, Set, Tuple
from typing_extensions import Self
import io
from pydantic import StrictBool
from typing import Union

class SenderIdentityViewModel(BaseModel):
    """
    SenderIdentityViewModel
    """ # noqa: E501
    name: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    created_by: Optional[StrictStr] = Field(default=None, alias="createdBy")
    approved_date: Optional[StrictStr] = Field(default=None, alias="approvedDate")
    notification_settings: Optional[NotificationSettings] = Field(default=None, alias="notificationSettings")
    brand_id: Optional[StrictStr] = Field(default=None, alias="brandId")
    redirect_url: Optional[StrictStr] = Field(default=None, alias="redirectUrl")
    __properties: ClassVar[List[str]] = ["name", "email", "status", "createdBy", "approvedDate", "notificationSettings", "brandId", "redirectUrl"]

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
        """Create an instance of SenderIdentityViewModel from a JSON string"""
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
        """Create an instance of SenderIdentityViewModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "email": obj.get("email"),
            "status": obj.get("status"),
            "createdBy": obj.get("createdBy"),
            "approvedDate": obj.get("approvedDate"),
            "notificationSettings": NotificationSettings.from_dict(obj["notificationSettings"]) if obj.get("notificationSettings") is not None else None,
            "brandId": obj.get("brandId"),
            "redirectUrl": obj.get("redirectUrl")
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
            "name": "(str,)",
            "email": "(str,)",
            "status": "(str,)",
            "created_by": "(str,)",
            "approved_date": "(str,)",
            "notification_settings": "(NotificationSettings,)",
            "brand_id": "(str,)",
            "redirect_url": "(str,)",
        }

    @classmethod
    def openapi_type_is_array(cls, property_name: str) -> bool:
        return property_name in [
        ]

