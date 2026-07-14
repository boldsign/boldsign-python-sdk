# WebhookEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**WebhookEventMetadata**](WebhookEventMetadata.md) |  | [optional] 
**context** | [**WebhookContext**](WebhookContext.md) |  | [optional] 
**data** | [**IWebhookData**](IWebhookData.md) |  | [optional] 
**document** | [**DocumentEvent**](DocumentEvent.md) |  | [optional] 

## Example

```python
from boldsign.models.webhook_event import WebhookEvent

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEvent from a JSON string
webhook_event_instance = WebhookEvent.from_json(json)
# print the JSON string representation of the object
print(WebhookEvent.to_json())

# convert the object into a dict
webhook_event_dict = webhook_event_instance.to_dict()
# create an instance of WebhookEvent from a dict
webhook_event_from_dict = WebhookEvent.from_dict(webhook_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


