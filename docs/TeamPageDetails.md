# TeamPageDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_size** | **int** |  | [optional] 
**page** | **int** |  | [optional] 

## Example

```python
from boldsign.models.team_page_details import TeamPageDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TeamPageDetails from a JSON string
team_page_details_instance = TeamPageDetails.from_json(json)
# print the JSON string representation of the object
print(TeamPageDetails.to_json())

# convert the object into a dict
team_page_details_dict = team_page_details_instance.to_dict()
# create an instance of TeamPageDetails from a dict
team_page_details_from_dict = TeamPageDetails.from_dict(team_page_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


