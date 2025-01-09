# CustomFormField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_type** | **str** |  | 
**width** | **float** |  | [optional] 
**height** | **float** |  | [optional] 
**is_required** | **bool** |  | [optional] 
**is_read_only** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 
**font_size** | **float** |  | [optional] [default to 13]
**font** | **str** |  | [optional] 
**font_hex_color** | **str** |  | [optional] 
**is_bold_font** | **bool** |  | [optional] 
**is_italic_font** | **bool** |  | [optional] 
**is_under_line_font** | **bool** |  | [optional] 
**line_height** | **int** |  | [optional] [default to 15]
**character_limit** | **int** |  | [optional] [default to 0]
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
**data_sync_tag** | **str** |  | [optional] 
**dropdown_options** | **List[str]** |  | [optional] 
**text_align** | **str** |  | [optional] 
**text_direction** | **str** |  | [optional] 
**character_spacing** | **float** |  | [optional] 
**id_prefix** | **str** |  | [optional] 
**restrict_id_prefix_change** | **bool** |  | [optional] [default to False]
**background_hex_color** | **str** |  | [optional] 

## Example

```python
from boldsign.models.custom_form_field import CustomFormField

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFormField from a JSON string
custom_form_field_instance = CustomFormField.from_json(json)
# print the JSON string representation of the object
print(CustomFormField.to_json())

# convert the object into a dict
custom_form_field_dict = custom_form_field_instance.to_dict()
# create an instance of CustomFormField from a dict
custom_form_field_from_dict = CustomFormField.from_dict(custom_form_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


