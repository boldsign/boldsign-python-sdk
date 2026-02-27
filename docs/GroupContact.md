# GroupContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_name** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**contacts** | [**List[GroupUser]**](GroupUser.md) |  | [optional] 
**directories** | **List[str]** |  | [optional] 

## Example

```python
from boldsign.models.group_contact import GroupContact

# TODO update the JSON string below
json = "{}"
# create an instance of GroupContact from a JSON string
group_contact_instance = GroupContact.from_json(json)
# print the JSON string representation of the object
print(GroupContact.to_json())

# convert the object into a dict
group_contact_dict = group_contact_instance.to_dict()
# create an instance of GroupContact from a dict
group_contact_from_dict = GroupContact.from_dict(group_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


