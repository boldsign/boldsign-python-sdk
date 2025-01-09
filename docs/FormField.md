# FormField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_type** | **str** |  | 
**page_number** | **int** |  | 
**bounds** | [**Rectangle**](Rectangle.md) |  | 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**is_required** | **bool** |  | [optional] 
**is_read_only** | **bool** |  | [optional] 
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
**hyperlink_text** | **str** |  | [optional] 
**conditional_rules** | [**List[ConditionalRule]**](ConditionalRule.md) |  | [optional] 
**data_sync_tag** | **str** |  | [optional] 
**dropdown_options** | **List[str]** |  | [optional] 
**text_align** | **str** |  | [optional] 
**text_direction** | **str** |  | [optional] 
**character_spacing** | **float** |  | [optional] 
**background_hex_color** | **str** |  | [optional] 
**tab_index** | **int** |  | [optional] 

## Example

```python
from boldsign.models.form_field import FormField

# TODO update the JSON string below
json = "{}"
# create an instance of FormField from a JSON string
form_field_instance = FormField.from_json(json)
# print the JSON string representation of the object
print(FormField.to_json())

# convert the object into a dict
form_field_dict = form_field_instance.to_dict()
# create an instance of FormField from a dict
form_field_from_dict = FormField.from_dict(form_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


