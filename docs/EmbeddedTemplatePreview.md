# EmbeddedTemplatePreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_url** | **str** |  | [optional] 

## Example

```python
from boldsign.models.embedded_template_preview import EmbeddedTemplatePreview

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedTemplatePreview from a JSON string
embedded_template_preview_instance = EmbeddedTemplatePreview.from_json(json)
# print the JSON string representation of the object
print(EmbeddedTemplatePreview.to_json())

# convert the object into a dict
embedded_template_preview_dict = embedded_template_preview_instance.to_dict()
# create an instance of EmbeddedTemplatePreview from a dict
embedded_template_preview_from_dict = EmbeddedTemplatePreview.from_dict(embedded_template_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


