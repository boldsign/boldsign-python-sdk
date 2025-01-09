# UsersDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**team_name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**user_status** | **str** |  | [optional] 
**created_date** | **int** |  | [optional] 
**modified_date** | **int** |  | [optional] 
**meta_data** | **Dict[str, Optional[str]]** |  | [optional] 

## Example

```python
from boldsign.models.users_details import UsersDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UsersDetails from a JSON string
users_details_instance = UsersDetails.from_json(json)
# print the JSON string representation of the object
print(UsersDetails.to_json())

# convert the object into a dict
users_details_dict = users_details_instance.to_dict()
# create an instance of UsersDetails from a dict
users_details_from_dict = UsersDetails.from_dict(users_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


