# CreateUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_id** | **str** |  | 
**team_id** | **str** |  | [optional] 
**user_role** | **str** |  | [optional] 
**meta_data** | **Dict[str, Optional[str]]** |  | [optional] 

## Example

```python
from boldsign.models.create_user import CreateUser

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUser from a JSON string
create_user_instance = CreateUser.from_json(json)
# print the JSON string representation of the object
print(CreateUser.to_json())

# convert the object into a dict
create_user_dict = create_user_instance.to_dict()
# create an instance of CreateUser from a dict
create_user_from_dict = CreateUser.from_dict(create_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


