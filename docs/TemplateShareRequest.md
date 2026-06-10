# TemplateShareRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | [**List[TemplateTeamShareRequest]**](TemplateTeamShareRequest.md) |  | [optional] 

## Example

```python
from boldsign.models.template_share_request import TemplateShareRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateShareRequest from a JSON string
template_share_request_instance = TemplateShareRequest.from_json(json)
# print the JSON string representation of the object
print(TemplateShareRequest.to_json())

# convert the object into a dict
template_share_request_dict = template_share_request_instance.to_dict()
# create an instance of TemplateShareRequest from a dict
template_share_request_from_dict = TemplateShareRequest.from_dict(template_share_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


