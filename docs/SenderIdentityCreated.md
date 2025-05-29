# SenderIdentityCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender_identity_id** | **str** |  | [optional] 

## Example

```python
from boldsign.models.sender_identity_created import SenderIdentityCreated

# TODO update the JSON string below
json = "{}"
# create an instance of SenderIdentityCreated from a JSON string
sender_identity_created_instance = SenderIdentityCreated.from_json(json)
# print the JSON string representation of the object
print(SenderIdentityCreated.to_json())

# convert the object into a dict
sender_identity_created_dict = sender_identity_created_instance.to_dict()
# create an instance of SenderIdentityCreated from a dict
sender_identity_created_from_dict = SenderIdentityCreated.from_dict(sender_identity_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


