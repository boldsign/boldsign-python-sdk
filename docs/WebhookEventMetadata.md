# WebhookEventMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**event_type** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**environment** | **str** |  | [optional] 

## Example

```python
from boldsign.models.webhook_event_metadata import WebhookEventMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEventMetadata from a JSON string
webhook_event_metadata_instance = WebhookEventMetadata.from_json(json)
# print the JSON string representation of the object
print(WebhookEventMetadata.to_json())

# convert the object into a dict
webhook_event_metadata_dict = webhook_event_metadata_instance.to_dict()
# create an instance of WebhookEventMetadata from a dict
webhook_event_metadata_from_dict = WebhookEventMetadata.from_dict(webhook_event_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


