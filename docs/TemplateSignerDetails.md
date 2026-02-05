# TemplateSignerDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signer_name** | **str** |  | [optional] 
**signer_role** | **str** |  | [optional] 
**signer_email** | **str** |  | [optional] 
**phone_number** | [**PhoneNumber**](PhoneNumber.md) |  | [optional] 
**status** | **str** |  | [optional] 
**enable_access_code** | **bool** |  | [optional] 
**enable_email_otp** | **bool** |  | [optional] 
**impose_authentication** | **str** |  | [optional] 
**delivery_mode** | **str** |  | [optional] 
**allow_field_configuration** | **bool** |  | [optional] [default to False]
**user_id** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**signer_type** | **str** |  | [optional] [default to 'Signer']
**host_email** | **str** |  | [optional] 
**host_name** | **str** |  | [optional] 
**host_user_id** | **str** |  | [optional] 
**sign_type** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**group_signers** | [**List[TemplateGroupSigner]**](TemplateGroupSigner.md) |  | [optional] 

## Example

```python
from boldsign.models.template_signer_details import TemplateSignerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateSignerDetails from a JSON string
template_signer_details_instance = TemplateSignerDetails.from_json(json)
# print the JSON string representation of the object
print(TemplateSignerDetails.to_json())

# convert the object into a dict
template_signer_details_dict = template_signer_details_instance.to_dict()
# create an instance of TemplateSignerDetails from a dict
template_signer_details_from_dict = TemplateSignerDetails.from_dict(template_signer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


