# EditFormField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edit_action** | **str** |  | 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**field_type** | **str** |  | [optional] 
**page_number** | **int** |  | [optional] 
**bounds** | [**Rectangle**](Rectangle.md) |  | [optional] 
**is_required** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 
**font_size** | **float** |  | [optional] 
**font** | **str** |  | [optional] 
**font_hex_color** | **str** |  | [optional] 
**is_bold_font** | **bool** |  | [optional] 
**is_italic_font** | **bool** |  | [optional] 
**is_under_line_font** | **bool** |  | [optional] 
**line_height** | **int** |  | [optional] 
**character_limit** | **int** |  | [optional] 
**group_name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**place_holder** | **str** |  | [optional] 
**validation_type** | **str** |  | [optional] 
**validation_custom_regex** | **str** |  | [optional] 
**validation_custom_regex_message** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**time_format** | **str** |  | [optional] 
**image_info** | [**ImageInfo**](ImageInfo.md) |  | [optional] 
**attachment_info** | [**AttachmentInfo**](AttachmentInfo.md) |  | [optional] 
**editable_date_field_settings** | [**EditableDateFieldSettings**](EditableDateFieldSettings.md) |  | [optional] 
**conditional_rules** | [**List[ConditionalRule]**](ConditionalRule.md) |  | [optional] 
**hyperlink_text** | **str** |  | [optional] 
**dropdown_options** | **List[str]** |  | [optional] 
**is_read_only** | **bool** |  | [optional] 
**data_sync_tag** | **str** |  | [optional] 
**text_align** | **str** |  | [optional] 
**text_direction** | **str** |  | [optional] 
**character_spacing** | **float** |  | [optional] 
**background_hex_color** | **str** |  | [optional] 
**tab_index** | **int** |  | [optional] [readonly] 
**formula_field_settings** | [**FormulaFieldSettings**](FormulaFieldSettings.md) |  | [optional] 
**resize_option** | **str** |  | [optional] 
**allow_edit_form_field** | **bool** |  | [optional] 
**allow_delete_form_field** | **bool** |  | [optional] 
**is_masked** | **bool** |  | [optional] [default to False]

## Example

```python
from boldsign.models.edit_form_field import EditFormField

# TODO update the JSON string below
json = "{}"
# create an instance of EditFormField from a JSON string
edit_form_field_instance = EditFormField.from_json(json)
# print the JSON string representation of the object
print(EditFormField.to_json())

# convert the object into a dict
edit_form_field_dict = edit_form_field_instance.to_dict()
# create an instance of EditFormField from a dict
edit_form_field_from_dict = EditFormField.from_dict(edit_form_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


