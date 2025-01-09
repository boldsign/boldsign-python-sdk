# UserProperties


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
from boldsign.models.user_properties import UserProperties

# TODO update the JSON string below
json = "{}"
# create an instance of UserProperties from a JSON string
user_properties_instance = UserProperties.from_json(json)
# print the JSON string representation of the object
print(UserProperties.to_json())

# convert the object into a dict
user_properties_dict = user_properties_instance.to_dict()
# create an instance of UserProperties from a dict
user_properties_from_dict = UserProperties.from_dict(user_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


