# GetGroupContactDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_name** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**contacts** | [**List[GroupUser]**](GroupUser.md) |  | [optional] 
**creator** | [**Creators**](Creators.md) |  | [optional] 
**directories** | **List[str]** |  | [optional] 

## Example

```python
from boldsign.models.get_group_contact_details import GetGroupContactDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupContactDetails from a JSON string
get_group_contact_details_instance = GetGroupContactDetails.from_json(json)
# print the JSON string representation of the object
print(GetGroupContactDetails.to_json())

# convert the object into a dict
get_group_contact_details_dict = get_group_contact_details_instance.to_dict()
# create an instance of GetGroupContactDetails from a dict
get_group_contact_details_from_dict = GetGroupContactDetails.from_dict(get_group_contact_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


