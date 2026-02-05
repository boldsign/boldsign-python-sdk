# TemplateSharing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | [**List[TemplateTeamShare]**](TemplateTeamShare.md) |  | [optional] 

## Example

```python
from boldsign.models.template_sharing import TemplateSharing

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateSharing from a JSON string
template_sharing_instance = TemplateSharing.from_json(json)
# print the JSON string representation of the object
print(TemplateSharing.to_json())

# convert the object into a dict
template_sharing_dict = template_sharing_instance.to_dict()
# create an instance of TemplateSharing from a dict
template_sharing_from_dict = TemplateSharing.from_dict(template_sharing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


