# GroupUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 

## Example

```python
from boldsign.models.group_user import GroupUser

# TODO update the JSON string below
json = "{}"
# create an instance of GroupUser from a JSON string
group_user_instance = GroupUser.from_json(json)
# print the JSON string representation of the object
print(GroupUser.to_json())

# convert the object into a dict
group_user_dict = group_user_instance.to_dict()
# create an instance of GroupUser from a dict
group_user_from_dict = GroupUser.from_dict(group_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


