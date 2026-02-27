# GroupContactsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_details** | [**ContactPageDetails**](ContactPageDetails.md) |  | [optional] 
**result** | [**List[GroupContact]**](GroupContact.md) |  | [optional] 

## Example

```python
from boldsign.models.group_contacts_list import GroupContactsList

# TODO update the JSON string below
json = "{}"
# create an instance of GroupContactsList from a JSON string
group_contacts_list_instance = GroupContactsList.from_json(json)
# print the JSON string representation of the object
print(GroupContactsList.to_json())

# convert the object into a dict
group_contacts_list_dict = group_contacts_list_instance.to_dict()
# create an instance of GroupContactsList from a dict
group_contacts_list_from_dict = GroupContactsList.from_dict(group_contacts_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


