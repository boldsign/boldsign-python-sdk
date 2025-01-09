# ChangeRecipient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_signer_name** | **str** |  | 
**reason** | **str** |  | 
**order** | **int** |  | [optional] 
**new_signer_email** | **str** |  | [optional] 
**old_signer_email** | **str** |  | [optional] 
**on_behalf_of** | **str** |  | [optional] 
**phone_number** | [**PhoneNumber**](PhoneNumber.md) |  | [optional] 
**old_phone_number** | [**PhoneNumber**](PhoneNumber.md) |  | [optional] 

## Example

```python
from boldsign.models.change_recipient import ChangeRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeRecipient from a JSON string
change_recipient_instance = ChangeRecipient.from_json(json)
# print the JSON string representation of the object
print(ChangeRecipient.to_json())

# convert the object into a dict
change_recipient_dict = change_recipient_instance.to_dict()
# create an instance of ChangeRecipient from a dict
change_recipient_from_dict = ChangeRecipient.from_dict(change_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


