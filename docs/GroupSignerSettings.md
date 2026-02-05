# GroupSignerSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**allowed_directories** | **List[str]** |  | [optional] 

## Example

```python
from boldsign.models.group_signer_settings import GroupSignerSettings

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSignerSettings from a JSON string
group_signer_settings_instance = GroupSignerSettings.from_json(json)
# print the JSON string representation of the object
print(GroupSignerSettings.to_json())

# convert the object into a dict
group_signer_settings_dict = group_signer_settings_instance.to_dict()
# create an instance of GroupSignerSettings from a dict
group_signer_settings_from_dict = GroupSignerSettings.from_dict(group_signer_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


