# TemplateSigner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signer_name** | **str** |  | [optional] 
**signer_role** | **str** |  | [optional] 
**signer_email** | **str** |  | [optional] 
**group_signers** | [**List[TemplateGroupSignerWebhookModel]**](TemplateGroupSignerWebhookModel.md) |  | [optional] 
**phone_number** | [**PhoneNumberWebhookModel**](PhoneNumberWebhookModel.md) |  | [optional] 
**enable_access_code** | **bool** |  | [optional] 
**enable_email_otp** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**signer_type** | **str** |  | [optional] 
**sign_type** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**host_email** | **str** |  | [optional] 
**host_name** | **str** |  | [optional] 
**host_user_id** | **str** |  | [optional] 
**impose_authentication** | **str** |  | [optional] 
**allow_field_configuration** | **bool** |  | [optional] 
**role_index** | **int** |  | [optional] 

## Example

```python
from boldsign.models.template_signer import TemplateSigner

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateSigner from a JSON string
template_signer_instance = TemplateSigner.from_json(json)
# print the JSON string representation of the object
print(TemplateSigner.to_json())

# convert the object into a dict
template_signer_dict = template_signer_instance.to_dict()
# create an instance of TemplateSigner from a dict
template_signer_from_dict = TemplateSigner.from_dict(template_signer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


