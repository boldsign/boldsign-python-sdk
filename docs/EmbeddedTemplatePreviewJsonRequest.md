# EmbeddedTemplatePreviewJsonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_valid_till** | **datetime** |  | [optional] 
**show_toolbar** | **bool** |  | [optional] 

## Example

```python
from boldsign.models.embedded_template_preview_json_request import EmbeddedTemplatePreviewJsonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedTemplatePreviewJsonRequest from a JSON string
embedded_template_preview_json_request_instance = EmbeddedTemplatePreviewJsonRequest.from_json(json)
# print the JSON string representation of the object
print(EmbeddedTemplatePreviewJsonRequest.to_json())

# convert the object into a dict
embedded_template_preview_json_request_dict = embedded_template_preview_json_request_instance.to_dict()
# create an instance of EmbeddedTemplatePreviewJsonRequest from a dict
embedded_template_preview_json_request_from_dict = EmbeddedTemplatePreviewJsonRequest.from_dict(embedded_template_preview_json_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


