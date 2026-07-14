# WebhookActorDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_type** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from boldsign.models.webhook_actor_details import WebhookActorDetails

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookActorDetails from a JSON string
webhook_actor_details_instance = WebhookActorDetails.from_json(json)
# print the JSON string representation of the object
print(WebhookActorDetails.to_json())

# convert the object into a dict
webhook_actor_details_dict = webhook_actor_details_instance.to_dict()
# create an instance of WebhookActorDetails from a dict
webhook_actor_details_from_dict = WebhookActorDetails.from_dict(webhook_actor_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


