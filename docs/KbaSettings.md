# KbaSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**maximum_retry_count** | **int** |  | [optional] 
**name_matcher** | **str** |  | [optional] 

## Example

```python
from boldsign.models.kba_settings import KbaSettings

# TODO update the JSON string below
json = "{}"
# create an instance of KbaSettings from a JSON string
kba_settings_instance = KbaSettings.from_json(json)
# print the JSON string representation of the object
print(KbaSettings.to_json())

# convert the object into a dict
kba_settings_dict = kba_settings_instance.to_dict()
# create an instance of KbaSettings from a dict
kba_settings_from_dict = KbaSettings.from_dict(kba_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


