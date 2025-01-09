# EditableDateFieldSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | 
**min_date** | **datetime** |  | [optional] 
**max_date** | **datetime** |  | [optional] 

## Example

```python
from boldsign.models.editable_date_field_settings import EditableDateFieldSettings

# TODO update the JSON string below
json = "{}"
# create an instance of EditableDateFieldSettings from a JSON string
editable_date_field_settings_instance = EditableDateFieldSettings.from_json(json)
# print the JSON string representation of the object
print(EditableDateFieldSettings.to_json())

# convert the object into a dict
editable_date_field_settings_dict = editable_date_field_settings_instance.to_dict()
# create an instance of EditableDateFieldSettings from a dict
editable_date_field_settings_from_dict = EditableDateFieldSettings.from_dict(editable_date_field_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


