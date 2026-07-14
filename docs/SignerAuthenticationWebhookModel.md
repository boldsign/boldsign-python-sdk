# SignerAuthenticationWebhookModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_frequency** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from boldsign.models.signer_authentication_webhook_model import SignerAuthenticationWebhookModel

# TODO update the JSON string below
json = "{}"
# create an instance of SignerAuthenticationWebhookModel from a JSON string
signer_authentication_webhook_model_instance = SignerAuthenticationWebhookModel.from_json(json)
# print the JSON string representation of the object
print(SignerAuthenticationWebhookModel.to_json())

# convert the object into a dict
signer_authentication_webhook_model_dict = signer_authentication_webhook_model_instance.to_dict()
# create an instance of SignerAuthenticationWebhookModel from a dict
signer_authentication_webhook_model_from_dict = SignerAuthenticationWebhookModel.from_dict(signer_authentication_webhook_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


