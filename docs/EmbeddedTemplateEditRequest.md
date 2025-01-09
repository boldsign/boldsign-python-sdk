# EmbeddedTemplateEditRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_url** | **str** |  | [optional] 
**show_toolbar** | **bool** |  | [optional] [default to False]
**view_option** | **str** |  | [optional] [default to 'PreparePage']
**show_save_button** | **bool** |  | [optional] [default to True]
**locale** | **str** |  | [optional] [default to 'EN']
**show_create_button** | **bool** |  | [optional] [default to True]
**show_preview_button** | **bool** |  | [optional] [default to True]
**show_navigation_buttons** | **bool** |  | [optional] [default to True]
**link_valid_till** | **datetime** |  | [optional] 
**show_tooltip** | **bool** |  | [optional] [default to False]
**on_behalf_of** | **str** |  | [optional] 

## Example

```python
from boldsign.models.embedded_template_edit_request import EmbeddedTemplateEditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedTemplateEditRequest from a JSON string
embedded_template_edit_request_instance = EmbeddedTemplateEditRequest.from_json(json)
# print the JSON string representation of the object
print(EmbeddedTemplateEditRequest.to_json())

# convert the object into a dict
embedded_template_edit_request_dict = embedded_template_edit_request_instance.to_dict()
# create an instance of EmbeddedTemplateEditRequest from a dict
embedded_template_edit_request_from_dict = EmbeddedTemplateEditRequest.from_dict(embedded_template_edit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


