# ChangeTeamRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_team_id** | **str** |  | 
**transfer_documents_to_user_id** | **str** |  | [optional] 

## Example

```python
from boldsign.models.change_team_request import ChangeTeamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeTeamRequest from a JSON string
change_team_request_instance = ChangeTeamRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeTeamRequest.to_json())

# convert the object into a dict
change_team_request_dict = change_team_request_instance.to_dict()
# create an instance of ChangeTeamRequest from a dict
change_team_request_from_dict = ChangeTeamRequest.from_dict(change_team_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


