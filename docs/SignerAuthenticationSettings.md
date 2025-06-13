# SignerAuthenticationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_frequency** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from boldsign.models.signer_authentication_settings import SignerAuthenticationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SignerAuthenticationSettings from a JSON string
signer_authentication_settings_instance = SignerAuthenticationSettings.from_json(json)
# print the JSON string representation of the object
print(SignerAuthenticationSettings.to_json())

# convert the object into a dict
signer_authentication_settings_dict = signer_authentication_settings_instance.to_dict()
# create an instance of SignerAuthenticationSettings from a dict
signer_authentication_settings_from_dict = SignerAuthenticationSettings.from_dict(signer_authentication_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


