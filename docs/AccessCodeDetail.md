# AccessCodeDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_type** | **str** |  | 
**email_id** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**access_code** | **str** |  | [optional] 
**on_behalf_of** | **str** |  | [optional] 
**phone_number** | [**PhoneNumber**](PhoneNumber.md) |  | [optional] 
**identity_verification_settings** | [**IdentityVerificationSettings**](IdentityVerificationSettings.md) |  | [optional] 
**authentication_retry_count** | **int** |  | [optional] 

## Example

```python
from boldsign.models.access_code_detail import AccessCodeDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AccessCodeDetail from a JSON string
access_code_detail_instance = AccessCodeDetail.from_json(json)
# print the JSON string representation of the object
print(AccessCodeDetail.to_json())

# convert the object into a dict
access_code_detail_dict = access_code_detail_instance.to_dict()
# create an instance of AccessCodeDetail from a dict
access_code_detail_from_dict = AccessCodeDetail.from_dict(access_code_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


