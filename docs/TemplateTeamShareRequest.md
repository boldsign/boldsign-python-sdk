# TemplateTeamShareRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **str** |  | 
**action** | **str** |  | 
**access_level** | **str** |  | [optional] 

## Example

```python
from boldsign.models.template_team_share_request import TemplateTeamShareRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateTeamShareRequest from a JSON string
template_team_share_request_instance = TemplateTeamShareRequest.from_json(json)
# print the JSON string representation of the object
print(TemplateTeamShareRequest.to_json())

# convert the object into a dict
template_team_share_request_dict = template_team_share_request_instance.to_dict()
# create an instance of TemplateTeamShareRequest from a dict
template_team_share_request_from_dict = TemplateTeamShareRequest.from_dict(template_team_share_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


