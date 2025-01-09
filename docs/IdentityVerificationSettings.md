# IdentityVerificationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**maximum_retry_count** | **int** |  | [optional] 
**require_live_capture** | **bool** |  | [optional] 
**require_matching_selfie** | **bool** |  | [optional] 
**name_matcher** | **str** |  | [optional] 
**hold_for_prefill** | **bool** |  | [optional] 

## Example

```python
from boldsign.models.identity_verification_settings import IdentityVerificationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityVerificationSettings from a JSON string
identity_verification_settings_instance = IdentityVerificationSettings.from_json(json)
# print the JSON string representation of the object
print(IdentityVerificationSettings.to_json())

# convert the object into a dict
identity_verification_settings_dict = identity_verification_settings_instance.to_dict()
# create an instance of IdentityVerificationSettings from a dict
identity_verification_settings_from_dict = IdentityVerificationSettings.from_dict(identity_verification_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


