# TemplateTeamShare


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **str** |  | [optional] 
**access_type** | **str** |  | [optional] 

## Example

```python
from boldsign.models.template_team_share import TemplateTeamShare

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateTeamShare from a JSON string
template_team_share_instance = TemplateTeamShare.from_json(json)
# print the JSON string representation of the object
print(TemplateTeamShare.to_json())

# convert the object into a dict
template_team_share_dict = template_team_share_instance.to_dict()
# create an instance of TemplateTeamShare from a dict
template_team_share_from_dict = TemplateTeamShare.from_dict(template_team_share_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


