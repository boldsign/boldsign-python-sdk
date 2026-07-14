# KbaAuthenticationEvent


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
from boldsign.models.kba_authentication_event import KbaAuthenticationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of KbaAuthenticationEvent from a JSON string
kba_authentication_event_instance = KbaAuthenticationEvent.from_json(json)
# print the JSON string representation of the object
print(KbaAuthenticationEvent.to_json())

# convert the object into a dict
kba_authentication_event_dict = kba_authentication_event_instance.to_dict()
# create an instance of KbaAuthenticationEvent from a dict
kba_authentication_event_from_dict = KbaAuthenticationEvent.from_dict(kba_authentication_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


