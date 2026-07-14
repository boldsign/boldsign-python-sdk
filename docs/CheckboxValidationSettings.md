# CheckboxValidationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validation_type** | **str** |  | [optional] 
**min_selection** | **int** |  | [optional] 
**max_selection** | **int** |  | [optional] 

## Example

```python
from boldsign.models.checkbox_validation_settings import CheckboxValidationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CheckboxValidationSettings from a JSON string
checkbox_validation_settings_instance = CheckboxValidationSettings.from_json(json)
# print the JSON string representation of the object
print(CheckboxValidationSettings.to_json())

# convert the object into a dict
checkbox_validation_settings_dict = checkbox_validation_settings_instance.to_dict()
# create an instance of CheckboxValidationSettings from a dict
checkbox_validation_settings_from_dict = CheckboxValidationSettings.from_dict(checkbox_validation_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


