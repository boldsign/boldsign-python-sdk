# IdentityVerificationEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] 
**document_id** | **str** |  | [optional] 
**message_title** | **str** |  | [optional] 
**document_description** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**sender_detail** | [**DocumentSender**](DocumentSender.md) |  | [optional] 
**signer_detail** | [**DocumentSignerWebhookModel**](DocumentSignerWebhookModel.md) |  | [optional] 

## Example

```python
from boldsign.models.identity_verification_event import IdentityVerificationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityVerificationEvent from a JSON string
identity_verification_event_instance = IdentityVerificationEvent.from_json(json)
# print the JSON string representation of the object
print(IdentityVerificationEvent.to_json())

# convert the object into a dict
identity_verification_event_dict = identity_verification_event_instance.to_dict()
# create an instance of IdentityVerificationEvent from a dict
identity_verification_event_from_dict = IdentityVerificationEvent.from_dict(identity_verification_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


