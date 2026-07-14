# TemplateCcWebhookModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from boldsign.models.template_cc_webhook_model import TemplateCcWebhookModel

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateCcWebhookModel from a JSON string
template_cc_webhook_model_instance = TemplateCcWebhookModel.from_json(json)
# print the JSON string representation of the object
print(TemplateCcWebhookModel.to_json())

# convert the object into a dict
template_cc_webhook_model_dict = template_cc_webhook_model_instance.to_dict()
# create an instance of TemplateCcWebhookModel from a dict
template_cc_webhook_model_from_dict = TemplateCcWebhookModel.from_dict(template_cc_webhook_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


