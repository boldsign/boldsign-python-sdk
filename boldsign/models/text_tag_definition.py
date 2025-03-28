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
from typing_extensions import Annotated
from boldsign.models.attachment_info import AttachmentInfo
from boldsign.models.font import Font
from boldsign.models.formula_field_settings import FormulaFieldSettings
from boldsign.models.image_info import ImageInfo
from boldsign.models.size import Size
from boldsign.models.text_tag_offset import TextTagOffset
from boldsign.models.validation import Validation
from typing import Optional, Set, Tuple
from typing_extensions import Self
import io
from pydantic import StrictBool
from typing import Union

class TextTagDefinition(BaseModel):
    """
    TextTagDefinition
    """ # noqa: E501
    definition_id: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="definitionId")
    type: StrictStr
    signer_index: Annotated[int, Field(le=50, strict=True, ge=1)] = Field(alias="signerIndex")
    is_required: Optional[StrictBool] = Field(default=None, alias="isRequired")
    placeholder: Optional[StrictStr] = None
    field_id: Optional[StrictStr] = Field(default=None, alias="fieldId")
    font: Optional[Font] = None
    validation: Optional[Validation] = None
    size: Optional[Size] = None
    date_format: Optional[StrictStr] = Field(default=None, alias="dateFormat")
    time_format: Optional[StrictStr] = Field(default=None, alias="timeFormat")
    radio_group_name: Optional[StrictStr] = Field(default=None, alias="radioGroupName")
    group_name: Optional[StrictStr] = Field(default=None, alias="groupName")
    value: Optional[StrictStr] = None
    dropdown_options: Optional[List[StrictStr]] = Field(default=None, alias="dropdownOptions")
    image_info: Optional[ImageInfo] = Field(default=None, alias="imageInfo")
    hyperlink_text: Optional[StrictStr] = Field(default=None, alias="hyperlinkText")
    attachment_info: Optional[AttachmentInfo] = Field(default=None, alias="attachmentInfo")
    background_hex_color: Optional[StrictStr] = Field(default=None, alias="backgroundHexColor")
    is_read_only: Optional[StrictBool] = Field(default=None, alias="isReadOnly")
    offset: Optional[TextTagOffset] = None
    label: Optional[StrictStr] = None
    tab_index: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-1)]] = Field(default=None, alias="tabIndex")
    formula_field_settings: Optional[FormulaFieldSettings] = Field(default=None, alias="formulaFieldSettings")
    resize_option: Optional[StrictStr] = Field(default=None, alias="resizeOption")
    __properties: ClassVar[List[str]] = ["definitionId", "type", "signerIndex", "isRequired", "placeholder", "fieldId", "font", "validation", "size", "dateFormat", "timeFormat", "radioGroupName", "groupName", "value", "dropdownOptions", "imageInfo", "hyperlinkText", "attachmentInfo", "backgroundHexColor", "isReadOnly", "offset", "label", "tabIndex", "formulaFieldSettings", "resizeOption"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Signature', 'Initial', 'CheckBox', 'TextBox', 'Label', 'DateSigned', 'RadioButton', 'Image', 'Attachment', 'EditableDate', 'Hyperlink', 'Dropdown', 'Title', 'Company', 'Formula']):
            raise ValueError("must be one of enum values ('Signature', 'Initial', 'CheckBox', 'TextBox', 'Label', 'DateSigned', 'RadioButton', 'Image', 'Attachment', 'EditableDate', 'Hyperlink', 'Dropdown', 'Title', 'Company', 'Formula')")
        return value

    @field_validator('resize_option')
    def resize_option_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['GrowVertically', 'GrowHorizontally', 'GrowBoth', 'Fixed', 'AutoResizeFont']):
            raise ValueError("must be one of enum values ('GrowVertically', 'GrowHorizontally', 'GrowBoth', 'Fixed', 'AutoResizeFont')")
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
        """Create an instance of TextTagDefinition from a JSON string"""
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
        """Create an instance of TextTagDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "definitionId": obj.get("definitionId"),
            "type": obj.get("type"),
            "signerIndex": obj.get("signerIndex"),
            "isRequired": obj.get("isRequired"),
            "placeholder": obj.get("placeholder"),
            "fieldId": obj.get("fieldId"),
            "font": Font.from_dict(obj["font"]) if obj.get("font") is not None else None,
            "validation": Validation.from_dict(obj["validation"]) if obj.get("validation") is not None else None,
            "size": Size.from_dict(obj["size"]) if obj.get("size") is not None else None,
            "dateFormat": obj.get("dateFormat"),
            "timeFormat": obj.get("timeFormat"),
            "radioGroupName": obj.get("radioGroupName"),
            "groupName": obj.get("groupName"),
            "value": obj.get("value"),
            "dropdownOptions": obj.get("dropdownOptions"),
            "imageInfo": ImageInfo.from_dict(obj["imageInfo"]) if obj.get("imageInfo") is not None else None,
            "hyperlinkText": obj.get("hyperlinkText"),
            "attachmentInfo": AttachmentInfo.from_dict(obj["attachmentInfo"]) if obj.get("attachmentInfo") is not None else None,
            "backgroundHexColor": obj.get("backgroundHexColor"),
            "isReadOnly": obj.get("isReadOnly"),
            "offset": TextTagOffset.from_dict(obj["offset"]) if obj.get("offset") is not None else None,
            "label": obj.get("label"),
            "tabIndex": obj.get("tabIndex"),
            "formulaFieldSettings": FormulaFieldSettings.from_dict(obj["formulaFieldSettings"]) if obj.get("formulaFieldSettings") is not None else None,
            "resizeOption": obj.get("resizeOption")
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
            "definition_id": "(str,)",
            "type": "(str,)",
            "signer_index": "(int,)",
            "is_required": "(bool,)",
            "placeholder": "(str,)",
            "field_id": "(str,)",
            "font": "(Font,)",
            "validation": "(Validation,)",
            "size": "(Size,)",
            "date_format": "(str,)",
            "time_format": "(str,)",
            "radio_group_name": "(str,)",
            "group_name": "(str,)",
            "value": "(str,)",
            "dropdown_options": "(List[str],)",
            "image_info": "(ImageInfo,)",
            "hyperlink_text": "(str,)",
            "attachment_info": "(AttachmentInfo,)",
            "background_hex_color": "(str,)",
            "is_read_only": "(bool,)",
            "offset": "(TextTagOffset,)",
            "label": "(str,)",
            "tab_index": "(int,)",
            "formula_field_settings": "(FormulaFieldSettings,)",
            "resize_option": "(str,)",
        }

    @classmethod
    def openapi_type_is_array(cls, property_name: str) -> bool:
        return property_name in [
            "dropdown_options",
        ]

