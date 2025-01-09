# CustomDomainSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** |  | [optional] 
**from_name** | **str** |  | [optional] 

## Example

```python
from boldsign.models.custom_domain_settings import CustomDomainSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDomainSettings from a JSON string
custom_domain_settings_instance = CustomDomainSettings.from_json(json)
# print the JSON string representation of the object
print(CustomDomainSettings.to_json())

# convert the object into a dict
custom_domain_settings_dict = custom_domain_settings_instance.to_dict()
# create an instance of CustomDomainSettings from a dict
custom_domain_settings_from_dict = CustomDomainSettings.from_dict(custom_domain_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


