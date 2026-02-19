# EditDocumentSigner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edit_action** | **str** |  | 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**private_message** | **str** |  | [optional] 
**authentication_type** | **str** |  | [optional] 
**phone_number** | [**PhoneNumber**](PhoneNumber.md) |  | [optional] 
**delivery_mode** | **str** |  | [optional] 
**authentication_code** | **str** |  | [optional] 
**identity_verification_settings** | [**IdentityVerificationSettings**](IdentityVerificationSettings.md) |  | [optional] 
**signer_order** | **int** |  | [optional] 
**enable_email_otp** | **bool** |  | [optional] 
**signer_type** | **str** |  | [optional] 
**host_email** | **str** |  | [optional] 
**signer_role** | **str** |  | [optional] 
**allow_field_configuration** | **bool** |  | [optional] 
**form_fields** | [**List[EditFormField]**](EditFormField.md) |  | [optional] 
**language** | **int** |  | [optional] 
**locale** | **str** |  | [optional] 
**sign_type** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**recipient_notification_settings** | [**RecipientNotificationSettings**](RecipientNotificationSettings.md) |  | [optional] 
**authentication_retry_count** | **int** |  | [optional] 
**enable_qes** | **bool** |  | [optional] 
**authentication_settings** | [**AuthenticationSettings**](AuthenticationSettings.md) |  | [optional] 

## Example

```python
from boldsign.models.edit_document_signer import EditDocumentSigner

# TODO update the JSON string below
json = "{}"
# create an instance of EditDocumentSigner from a JSON string
edit_document_signer_instance = EditDocumentSigner.from_json(json)
# print the JSON string representation of the object
print(EditDocumentSigner.to_json())

# convert the object into a dict
edit_document_signer_dict = edit_document_signer_instance.to_dict()
# create an instance of EditDocumentSigner from a dict
edit_document_signer_from_dict = EditDocumentSigner.from_dict(edit_document_signer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


