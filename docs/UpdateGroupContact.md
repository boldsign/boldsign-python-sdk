# UpdateGroupContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_name** | **str** |  | [optional] 
**directories** | **List[str]** |  | [optional] 
**contacts** | [**List[GroupUser]**](GroupUser.md) |  | [optional] 

## Example

```python
from boldsign.models.update_group_contact import UpdateGroupContact

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGroupContact from a JSON string
update_group_contact_instance = UpdateGroupContact.from_json(json)
# print the JSON string representation of the object
print(UpdateGroupContact.to_json())

# convert the object into a dict
update_group_contact_dict = update_group_contact_instance.to_dict()
# create an instance of UpdateGroupContact from a dict
update_group_contact_from_dict = UpdateGroupContact.from_dict(update_group_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


