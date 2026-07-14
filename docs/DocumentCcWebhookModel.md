# DocumentCcWebhookModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from boldsign.models.document_cc_webhook_model import DocumentCcWebhookModel

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCcWebhookModel from a JSON string
document_cc_webhook_model_instance = DocumentCcWebhookModel.from_json(json)
# print the JSON string representation of the object
print(DocumentCcWebhookModel.to_json())

# convert the object into a dict
document_cc_webhook_model_dict = document_cc_webhook_model_instance.to_dict()
# create an instance of DocumentCcWebhookModel from a dict
document_cc_webhook_model_from_dict = DocumentCcWebhookModel.from_dict(document_cc_webhook_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


