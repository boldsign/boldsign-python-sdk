# TemplateFormFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**field_type** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**font** | **str** |  | [optional] 
**is_required** | **bool** |  | [optional] 
**is_read_only** | **bool** |  | [optional] 
**line_height** | **int** |  | [optional] 
**font_size** | **int** |  | [optional] 
**font_hex_color** | **str** |  | [optional] 
**is_under_line_font** | **bool** |  | [optional] 
**is_italic_font** | **bool** |  | [optional] 
**is_bold_font** | **bool** |  | [optional] 
**group_name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**placeholder** | **str** |  | [optional] 
**validationtype** | **str** |  | [optional] 
**validation_custom_regex** | **str** |  | [optional] 
**validation_custom_regex_message** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**time_format** | **str** |  | [optional] 
**image_info** | [**ImageInfo**](ImageInfo.md) |  | [optional] 
**attachment_info** | [**AttachmentInfo**](AttachmentInfo.md) |  | [optional] 
**editable_date_field_settings** | [**EditableDateFieldSettings**](EditableDateFieldSettings.md) |  | [optional] 
**dropdown_options** | **List[str]** |  | [optional] 
**bounds** | [**Rectangle**](Rectangle.md) |  | [optional] 
**page_number** | **int** |  | [optional] 
**conditional_rules** | [**List[ConditionalRule]**](ConditionalRule.md) |  | [optional] 
**data_sync_tag** | **str** |  | [optional] 
**text_align** | **str** |  | [optional] 
**text_direction** | **str** |  | [optional] 
**character_spacing** | **float** |  | [optional] 
**character_limit** | **int** |  | [optional] 
**hyperlink_text** | **str** |  | [optional] 
**background_hex_color** | **str** |  | [optional] 
**tab_index** | **int** |  | [optional] 
**formula_field_settings** | [**FormulaFieldSettings**](FormulaFieldSettings.md) |  | [optional] 
**resize_option** | **str** |  | [optional] 

## Example

```python
from boldsign.models.template_form_fields import TemplateFormFields

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateFormFields from a JSON string
template_form_fields_instance = TemplateFormFields.from_json(json)
# print the JSON string representation of the object
print(TemplateFormFields.to_json())

# convert the object into a dict
template_form_fields_dict = template_form_fields_instance.to_dict()
# create an instance of TemplateFormFields from a dict
template_form_fields_from_dict = TemplateFormFields.from_dict(template_form_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


