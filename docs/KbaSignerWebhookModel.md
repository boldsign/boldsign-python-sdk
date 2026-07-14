# KbaSignerWebhookModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**maximum_retry_count** | **int** |  | [optional] 
**name_matcher** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from boldsign.models.kba_signer_webhook_model import KbaSignerWebhookModel

# TODO update the JSON string below
json = "{}"
# create an instance of KbaSignerWebhookModel from a JSON string
kba_signer_webhook_model_instance = KbaSignerWebhookModel.from_json(json)
# print the JSON string representation of the object
print(KbaSignerWebhookModel.to_json())

# convert the object into a dict
kba_signer_webhook_model_dict = kba_signer_webhook_model_instance.to_dict()
# create an instance of KbaSignerWebhookModel from a dict
kba_signer_webhook_model_from_dict = KbaSignerWebhookModel.from_dict(kba_signer_webhook_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


