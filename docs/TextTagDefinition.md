# TextTagDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition_id** | **str** |  | 
**type** | **str** |  | 
**signer_index** | **int** |  | 
**is_required** | **bool** |  | [optional] 
**placeholder** | **str** |  | [optional] 
**field_id** | **str** |  | [optional] 
**font** | [**Font**](Font.md) |  | [optional] 
**validation** | [**Validation**](Validation.md) |  | [optional] 
**size** | [**Size**](Size.md) |  | [optional] 
**date_format** | **str** |  | [optional] 
**time_format** | **str** |  | [optional] 
**radio_group_name** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**dropdown_options** | **List[str]** |  | [optional] 
**image_info** | [**ImageInfo**](ImageInfo.md) |  | [optional] 
**hyperlink_text** | **str** |  | [optional] 
**attachment_info** | [**AttachmentInfo**](AttachmentInfo.md) |  | [optional] 
**background_hex_color** | **str** |  | [optional] 
**is_read_only** | **bool** |  | [optional] 
**offset** | [**TextTagOffset**](TextTagOffset.md) |  | [optional] 
**label** | **str** |  | [optional] 
**tab_index** | **int** |  | [optional] 
**data_sync_tag** | **str** |  | [optional] 
**text_align** | **str** |  | [optional] 
**text_direction** | **str** |  | [optional] 
**character_spacing** | **float** |  | [optional] 
**character_limit** | **int** |  | [optional] 
**formula_field_settings** | [**FormulaFieldSettings**](FormulaFieldSettings.md) |  | [optional] 
**resize_option** | **str** |  | [optional] 

## Example

```python
from boldsign.models.text_tag_definition import TextTagDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of TextTagDefinition from a JSON string
text_tag_definition_instance = TextTagDefinition.from_json(json)
# print the JSON string representation of the object
print(TextTagDefinition.to_json())

# convert the object into a dict
text_tag_definition_dict = text_tag_definition_instance.to_dict()
# create an instance of TextTagDefinition from a dict
text_tag_definition_from_dict = TextTagDefinition.from_dict(text_tag_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


