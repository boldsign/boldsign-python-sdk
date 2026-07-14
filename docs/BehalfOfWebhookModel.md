# BehalfOfWebhookModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from boldsign.models.behalf_of_webhook_model import BehalfOfWebhookModel

# TODO update the JSON string below
json = "{}"
# create an instance of BehalfOfWebhookModel from a JSON string
behalf_of_webhook_model_instance = BehalfOfWebhookModel.from_json(json)
# print the JSON string representation of the object
print(BehalfOfWebhookModel.to_json())

# convert the object into a dict
behalf_of_webhook_model_dict = behalf_of_webhook_model_instance.to_dict()
# create an instance of BehalfOfWebhookModel from a dict
behalf_of_webhook_model_from_dict = BehalfOfWebhookModel.from_dict(behalf_of_webhook_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


