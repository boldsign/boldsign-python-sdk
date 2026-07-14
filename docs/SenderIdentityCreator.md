# SenderIdentityCreator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 

## Example

```python
from boldsign.models.sender_identity_creator import SenderIdentityCreator

# TODO update the JSON string below
json = "{}"
# create an instance of SenderIdentityCreator from a JSON string
sender_identity_creator_instance = SenderIdentityCreator.from_json(json)
# print the JSON string representation of the object
print(SenderIdentityCreator.to_json())

# convert the object into a dict
sender_identity_creator_dict = sender_identity_creator_instance.to_dict()
# create an instance of SenderIdentityCreator from a dict
sender_identity_creator_from_dict = SenderIdentityCreator.from_dict(sender_identity_creator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


