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
from typing_extensions import Annotated
from typing import Optional, Set, Tuple
from typing_extensions import Self
import io
from pydantic import StrictBool
from typing import Union

class DocumentInfo(BaseModel):
    """
    DocumentInfo
    """ # noqa: E501
    locale: StrictStr
    title: Annotated[str, Field(min_length=1, strict=True)]
    language: Optional[StrictInt] = Field(default=None, description="<p>Description:</p><ul><li><i>0</i> - None</li><li><i>1</i> - English</li><li><i>2</i> - Spanish</li><li><i>3</i> - German</li><li><i>4</i> - French</li><li><i>5</i> - Romanian</li><li><i>6</i> - Norwegian</li><li><i>7</i> - Bulgarian</li><li><i>8</i> - Italian</li><li><i>9</i> - Danish</li><li><i>10</i> - Polish</li><li><i>11</i> - Portuguese</li><li><i>12</i> - Czech</li><li><i>13</i> - Dutch</li><li><i>14</i> - Swedish</li><li><i>15</i> - Russian</li></ul>")
    description: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["locale", "title", "language", "description"]

    @field_validator('locale')
    def locale_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['EN', 'NO', 'FR', 'DE', 'ES', 'BG', 'CS', 'DA', 'IT', 'NL', 'PL', 'PT', 'RO', 'RU', 'SV', 'Default']):
            raise ValueError("must be one of enum values ('EN', 'NO', 'FR', 'DE', 'ES', 'BG', 'CS', 'DA', 'IT', 'NL', 'PL', 'PT', 'RO', 'RU', 'SV', 'Default')")
        return value

    @field_validator('language')
    def language_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]):
            raise ValueError("must be one of enum values (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)")
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
        """Create an instance of DocumentInfo from a JSON string"""
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
        """Create an instance of DocumentInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "locale": obj.get("locale"),
            "title": obj.get("title"),
            "language": obj.get("language"),
            "description": obj.get("description")
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
            "locale": "(str,)",
            "title": "(str,)",
            "language": "(int,)",
            "description": "(str,)",
        }

    @classmethod
    def openapi_type_is_array(cls, property_name: str) -> bool:
        return property_name in [
        ]

