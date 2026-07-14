# TemplateGroupSignerWebhookModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signer_email** | **str** |  | [optional] 
**signer_name** | **str** |  | [optional] 

## Example

```python
from boldsign.models.template_group_signer_webhook_model import TemplateGroupSignerWebhookModel

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateGroupSignerWebhookModel from a JSON string
template_group_signer_webhook_model_instance = TemplateGroupSignerWebhookModel.from_json(json)
# print the JSON string representation of the object
print(TemplateGroupSignerWebhookModel.to_json())

# convert the object into a dict
template_group_signer_webhook_model_dict = template_group_signer_webhook_model_instance.to_dict()
# create an instance of TemplateGroupSignerWebhookModel from a dict
template_group_signer_webhook_model_from_dict = TemplateGroupSignerWebhookModel.from_dict(template_group_signer_webhook_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


