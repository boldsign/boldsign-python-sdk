# SenderIdentityList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[SenderIdentityViewModel]**](SenderIdentityViewModel.md) |  | [optional] 
**page_details** | [**PageDetails**](PageDetails.md) |  | [optional] 

## Example

```python
from boldsign.models.sender_identity_list import SenderIdentityList

# TODO update the JSON string below
json = "{}"
# create an instance of SenderIdentityList from a JSON string
sender_identity_list_instance = SenderIdentityList.from_json(json)
# print the JSON string representation of the object
print(SenderIdentityList.to_json())

# convert the object into a dict
sender_identity_list_dict = sender_identity_list_instance.to_dict()
# create an instance of SenderIdentityList from a dict
sender_identity_list_from_dict = SenderIdentityList.from_dict(sender_identity_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


