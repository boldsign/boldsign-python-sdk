# DocumentFormFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**font** | **str** |  | [optional] 
**is_required** | **bool** |  | [optional] 
**is_read_only** | **bool** |  | [optional] 
**line_height** | **float** |  | [optional] 
**font_size** | **float** |  | [optional] 
**font_color** | **str** |  | [optional] 
**is_underline** | **bool** |  | [optional] 
**is_italic** | **bool** |  | [optional] 
**is_bold** | **bool** |  | [optional] 
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
**file_info** | [**FileInfo**](FileInfo.md) |  | [optional] 
**editable_date_field_settings** | [**EditableDateFieldSettings**](EditableDateFieldSettings.md) |  | [optional] 
**hyperlink_text** | **str** |  | [optional] 
**conditional_rules** | [**List[ConditionalRule]**](ConditionalRule.md) |  | [optional] 
**bounds** | [**Rectangle**](Rectangle.md) |  | [optional] 
**page_number** | **int** |  | [optional] 
**data_sync_tag** | **str** |  | [optional] 
**dropdown_options** | **List[str]** |  | [optional] 
**text_align** | **str** |  | [optional] 
**text_direction** | **str** |  | [optional] 
**character_spacing** | **float** |  | [optional] 
**background_hex_color** | **str** |  | [optional] 
**tab_index** | **int** |  | [optional] 

## Example

```python
from boldsign.models.document_form_fields import DocumentFormFields

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFormFields from a JSON string
document_form_fields_instance = DocumentFormFields.from_json(json)
# print the JSON string representation of the object
print(DocumentFormFields.to_json())

# convert the object into a dict
document_form_fields_dict = document_form_fields_instance.to_dict()
# create an instance of DocumentFormFields from a dict
document_form_fields_from_dict = DocumentFormFields.from_dict(document_form_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


