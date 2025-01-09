# Teams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_name** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**created_date** | **int** |  | [optional] 
**modified_date** | **int** |  | [optional] 

## Example

```python
from boldsign.models.teams import Teams

# TODO update the JSON string below
json = "{}"
# create an instance of Teams from a JSON string
teams_instance = Teams.from_json(json)
# print the JSON string representation of the object
print(Teams.to_json())

# convert the object into a dict
teams_dict = teams_instance.to_dict()
# create an instance of Teams from a dict
teams_from_dict = Teams.from_dict(teams_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


