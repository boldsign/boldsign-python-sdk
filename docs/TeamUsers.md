# TeamUsers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**user_role** | **str** |  | [optional] 
**user_status** | **str** |  | [optional] 

## Example

```python
from boldsign.models.team_users import TeamUsers

# TODO update the JSON string below
json = "{}"
# create an instance of TeamUsers from a JSON string
team_users_instance = TeamUsers.from_json(json)
# print the JSON string representation of the object
print(TeamUsers.to_json())

# convert the object into a dict
team_users_dict = team_users_instance.to_dict()
# create an instance of TeamUsers from a dict
team_users_from_dict = TeamUsers.from_dict(team_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


