# EmbeddedClonedTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** |  | [optional] 
**embed_url** | **str** |  | [optional] 

## Example

```python
from boldsign.models.embedded_cloned_template import EmbeddedClonedTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedClonedTemplate from a JSON string
embedded_cloned_template_instance = EmbeddedClonedTemplate.from_json(json)
# print the JSON string representation of the object
print(EmbeddedClonedTemplate.to_json())

# convert the object into a dict
embedded_cloned_template_dict = embedded_cloned_template_instance.to_dict()
# create an instance of EmbeddedClonedTemplate from a dict
embedded_cloned_template_from_dict = EmbeddedClonedTemplate.from_dict(embedded_cloned_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


