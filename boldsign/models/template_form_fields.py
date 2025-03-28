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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from boldsign.models.attachment_info import AttachmentInfo
from boldsign.models.conditional_rule import ConditionalRule
from boldsign.models.editable_date_field_settings import EditableDateFieldSettings
from boldsign.models.formula_field_settings import FormulaFieldSettings
from boldsign.models.image_info import ImageInfo
from boldsign.models.rectangle import Rectangle
from typing import Optional, Set, Tuple
from typing_extensions import Self
import io
from pydantic import StrictBool
from typing import Union

class TemplateFormFields(BaseModel):
    """
    TemplateFormFields
    """ # noqa: E501
    id: Optional[StrictStr] = None
    field_type: Optional[StrictStr] = Field(default=None, alias="fieldType")
    type: Optional[StrictStr] = None
    value: Optional[StrictStr] = None
    font: Optional[StrictStr] = None
    is_required: Optional[StrictBool] = Field(default=None, alias="isRequired")
    is_read_only: Optional[StrictBool] = Field(default=None, alias="isReadOnly")
    line_height: Optional[StrictInt] = Field(default=None, alias="lineHeight")
    font_size: Optional[StrictInt] = Field(default=None, alias="fontSize")
    font_hex_color: Optional[StrictStr] = Field(default=None, alias="fontHexColor")
    is_under_line_font: Optional[StrictBool] = Field(default=None, alias="isUnderLineFont")
    is_italic_font: Optional[StrictBool] = Field(default=None, alias="isItalicFont")
    is_bold_font: Optional[StrictBool] = Field(default=None, alias="isBoldFont")
    group_name: Optional[StrictStr] = Field(default=None, alias="groupName")
    label: Optional[StrictStr] = None
    placeholder: Optional[StrictStr] = None
    validationtype: Optional[StrictStr] = None
    validation_custom_regex: Optional[StrictStr] = Field(default=None, alias="validationCustomRegex")
    validation_custom_regex_message: Optional[StrictStr] = Field(default=None, alias="validationCustomRegexMessage")
    date_format: Optional[StrictStr] = Field(default=None, alias="dateFormat")
    time_format: Optional[StrictStr] = Field(default=None, alias="timeFormat")
    image_info: Optional[ImageInfo] = Field(default=None, alias="imageInfo")
    attachment_info: Optional[AttachmentInfo] = Field(default=None, alias="attachmentInfo")
    editable_date_field_settings: Optional[EditableDateFieldSettings] = Field(default=None, alias="editableDateFieldSettings")
    dropdown_options: Optional[List[StrictStr]] = Field(default=None, alias="dropdownOptions")
    bounds: Optional[Rectangle] = None
    page_number: Optional[StrictInt] = Field(default=None, alias="pageNumber")
    conditional_rules: Optional[List[ConditionalRule]] = Field(default=None, alias="conditionalRules")
    data_sync_tag: Optional[StrictStr] = Field(default=None, alias="dataSyncTag")
    text_align: Optional[StrictStr] = Field(default=None, alias="textAlign")
    text_direction: Optional[StrictStr] = Field(default=None, alias="textDirection")
    character_spacing: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="characterSpacing")
    character_limit: Optional[StrictInt] = Field(default=None, alias="characterLimit")
    hyperlink_text: Optional[StrictStr] = Field(default=None, alias="hyperlinkText")
    background_hex_color: Optional[StrictStr] = Field(default=None, alias="backgroundHexColor")
    tab_index: Optional[StrictInt] = Field(default=None, alias="tabIndex")
    formula_field_settings: Optional[FormulaFieldSettings] = Field(default=None, alias="formulaFieldSettings")
    resize_option: Optional[StrictStr] = Field(default=None, alias="resizeOption")
    __properties: ClassVar[List[str]] = ["id", "fieldType", "type", "value", "font", "isRequired", "isReadOnly", "lineHeight", "fontSize", "fontHexColor", "isUnderLineFont", "isItalicFont", "isBoldFont", "groupName", "label", "placeholder", "validationtype", "validationCustomRegex", "validationCustomRegexMessage", "dateFormat", "timeFormat", "imageInfo", "attachmentInfo", "editableDateFieldSettings", "dropdownOptions", "bounds", "pageNumber", "conditionalRules", "dataSyncTag", "textAlign", "textDirection", "characterSpacing", "characterLimit", "hyperlinkText", "backgroundHexColor", "tabIndex", "formulaFieldSettings", "resizeOption"]

    @field_validator('validationtype')
    def validationtype_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['None', 'NumbersOnly', 'EmailAddress', 'Currency', 'CustomRegex']):
            raise ValueError("must be one of enum values ('None', 'NumbersOnly', 'EmailAddress', 'Currency', 'CustomRegex')")
        return value

    @field_validator('text_align')
    def text_align_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Left', 'Center', 'Right']):
            raise ValueError("must be one of enum values ('Left', 'Center', 'Right')")
        return value

    @field_validator('text_direction')
    def text_direction_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['LTR', 'RTL']):
            raise ValueError("must be one of enum values ('LTR', 'RTL')")
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
        """Create an instance of TemplateFormFields from a JSON string"""
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
        """Create an instance of TemplateFormFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "fieldType": obj.get("fieldType"),
            "type": obj.get("type"),
            "value": obj.get("value"),
            "font": obj.get("font"),
            "isRequired": obj.get("isRequired"),
            "isReadOnly": obj.get("isReadOnly"),
            "lineHeight": obj.get("lineHeight"),
            "fontSize": obj.get("fontSize"),
            "fontHexColor": obj.get("fontHexColor"),
            "isUnderLineFont": obj.get("isUnderLineFont"),
            "isItalicFont": obj.get("isItalicFont"),
            "isBoldFont": obj.get("isBoldFont"),
            "groupName": obj.get("groupName"),
            "label": obj.get("label"),
            "placeholder": obj.get("placeholder"),
            "validationtype": obj.get("validationtype"),
            "validationCustomRegex": obj.get("validationCustomRegex"),
            "validationCustomRegexMessage": obj.get("validationCustomRegexMessage"),
            "dateFormat": obj.get("dateFormat"),
            "timeFormat": obj.get("timeFormat"),
            "imageInfo": ImageInfo.from_dict(obj["imageInfo"]) if obj.get("imageInfo") is not None else None,
            "attachmentInfo": AttachmentInfo.from_dict(obj["attachmentInfo"]) if obj.get("attachmentInfo") is not None else None,
            "editableDateFieldSettings": EditableDateFieldSettings.from_dict(obj["editableDateFieldSettings"]) if obj.get("editableDateFieldSettings") is not None else None,
            "dropdownOptions": obj.get("dropdownOptions"),
            "bounds": Rectangle.from_dict(obj["bounds"]) if obj.get("bounds") is not None else None,
            "pageNumber": obj.get("pageNumber"),
            "conditionalRules": [ConditionalRule.from_dict(_item) for _item in obj["conditionalRules"]] if obj.get("conditionalRules") is not None else None,
            "dataSyncTag": obj.get("dataSyncTag"),
            "textAlign": obj.get("textAlign"),
            "textDirection": obj.get("textDirection"),
            "characterSpacing": obj.get("characterSpacing"),
            "characterLimit": obj.get("characterLimit"),
            "hyperlinkText": obj.get("hyperlinkText"),
            "backgroundHexColor": obj.get("backgroundHexColor"),
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
            "id": "(str,)",
            "field_type": "(str,)",
            "type": "(str,)",
            "value": "(str,)",
            "font": "(str,)",
            "is_required": "(bool,)",
            "is_read_only": "(bool,)",
            "line_height": "(int,)",
            "font_size": "(int,)",
            "font_hex_color": "(str,)",
            "is_under_line_font": "(bool,)",
            "is_italic_font": "(bool,)",
            "is_bold_font": "(bool,)",
            "group_name": "(str,)",
            "label": "(str,)",
            "placeholder": "(str,)",
            "validationtype": "(str,)",
            "validation_custom_regex": "(str,)",
            "validation_custom_regex_message": "(str,)",
            "date_format": "(str,)",
            "time_format": "(str,)",
            "image_info": "(ImageInfo,)",
            "attachment_info": "(AttachmentInfo,)",
            "editable_date_field_settings": "(EditableDateFieldSettings,)",
            "dropdown_options": "(List[str],)",
            "bounds": "(Rectangle,)",
            "page_number": "(int,)",
            "conditional_rules": "(List[ConditionalRule],)",
            "data_sync_tag": "(str,)",
            "text_align": "(str,)",
            "text_direction": "(str,)",
            "character_spacing": "(float,)",
            "character_limit": "(int,)",
            "hyperlink_text": "(str,)",
            "background_hex_color": "(str,)",
            "tab_index": "(int,)",
            "formula_field_settings": "(FormulaFieldSettings,)",
            "resize_option": "(str,)",
        }

    @classmethod
    def openapi_type_is_array(cls, property_name: str) -> bool:
        return property_name in [
            "dropdown_options",
            "conditional_rules",
        ]

