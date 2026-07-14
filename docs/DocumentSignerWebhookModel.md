# DocumentSignerWebhookModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signer_name** | **str** |  | [optional] 
**signer_role** | **str** |  | [optional] 
**signer_email** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**group_signers** | [**List[DocumentGroupSignerWebhookModel]**](DocumentGroupSignerWebhookModel.md) |  | [optional] 
**phone_number** | [**PhoneNumberWebhookModel**](PhoneNumberWebhookModel.md) |  | [optional] 
**status** | **str** |  | [optional] 
**enable_access_code** | **bool** |  | [optional] 
**is_authentication_failed** | **bool** |  | [optional] 
**enable_email_otp** | **bool** |  | [optional] 
**is_delivery_failed** | **bool** |  | [optional] 
**is_viewed** | **bool** |  | [optional] 
**order** | **int** |  | [optional] 
**signer_type** | **str** |  | [optional] 
**sign_type** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**is_reassigned** | **bool** |  | [optional] 
**reassign_message** | **str** |  | [optional] 
**decline_message** | **str** |  | [optional] 
**last_activity_date** | **datetime** |  | [optional] 
**authentication_type** | **str** |  | [optional] 
**id_verification** | [**IdVerificationSignerWebhookModel**](IdVerificationSignerWebhookModel.md) |  | [optional] 
**kba** | [**KbaSignerWebhookModel**](KbaSignerWebhookModel.md) |  | [optional] 
**allow_field_configuration** | **bool** |  | [optional] 
**last_reminder_sent_on** | **datetime** |  | [optional] 
**authentication_retry_count** | **int** |  | [optional] 
**authentication_settings** | [**SignerAuthenticationWebhookModel**](SignerAuthenticationWebhookModel.md) |  | [optional] 

## Example

```python
from boldsign.models.document_signer_webhook_model import DocumentSignerWebhookModel

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSignerWebhookModel from a JSON string
document_signer_webhook_model_instance = DocumentSignerWebhookModel.from_json(json)
# print the JSON string representation of the object
print(DocumentSignerWebhookModel.to_json())

# convert the object into a dict
document_signer_webhook_model_dict = document_signer_webhook_model_instance.to_dict()
# create an instance of DocumentSignerWebhookModel from a dict
document_signer_webhook_model_from_dict = DocumentSignerWebhookModel.from_dict(document_signer_webhook_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


