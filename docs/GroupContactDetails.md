# GroupContactDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_name** | **str** |  | 
**contacts** | [**List[GroupUser]**](GroupUser.md) |  | 
**directories** | **List[str]** |  | [optional] 

## Example

```python
from boldsign.models.group_contact_details import GroupContactDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GroupContactDetails from a JSON string
group_contact_details_instance = GroupContactDetails.from_json(json)
# print the JSON string representation of the object
print(GroupContactDetails.to_json())

# convert the object into a dict
group_contact_details_dict = group_contact_details_instance.to_dict()
# create an instance of GroupContactDetails from a dict
group_contact_details_from_dict = GroupContactDetails.from_dict(group_contact_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


