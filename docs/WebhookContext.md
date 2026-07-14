# WebhookContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** |  | [optional] 
**actor** | [**WebhookActorDetails**](WebhookActorDetails.md) |  | [optional] 
**previous_state** | **object** |  | [optional] 

## Example

```python
from boldsign.models.webhook_context import WebhookContext

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookContext from a JSON string
webhook_context_instance = WebhookContext.from_json(json)
# print the JSON string representation of the object
print(WebhookContext.to_json())

# convert the object into a dict
webhook_context_dict = webhook_context_instance.to_dict()
# create an instance of WebhookContext from a dict
webhook_context_from_dict = WebhookContext.from_dict(webhook_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


