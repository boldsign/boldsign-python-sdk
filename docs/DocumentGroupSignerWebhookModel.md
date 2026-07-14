# DocumentGroupSignerWebhookModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**signer_email** | **str** |  | [optional] 
**signer_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**is_viewed** | **bool** |  | [optional] 
**is_delivery_failed** | **bool** |  | [optional] 
**is_authentication_failed** | **bool** |  | [optional] 
**last_reminder_sent_on** | **datetime** |  | [optional] 

## Example

```python
from boldsign.models.document_group_signer_webhook_model import DocumentGroupSignerWebhookModel

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentGroupSignerWebhookModel from a JSON string
document_group_signer_webhook_model_instance = DocumentGroupSignerWebhookModel.from_json(json)
# print the JSON string representation of the object
print(DocumentGroupSignerWebhookModel.to_json())

# convert the object into a dict
document_group_signer_webhook_model_dict = document_group_signer_webhook_model_instance.to_dict()
# create an instance of DocumentGroupSignerWebhookModel from a dict
document_group_signer_webhook_model_from_dict = DocumentGroupSignerWebhookModel.from_dict(document_group_signer_webhook_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


