# ExistingFormField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**is_read_only** | **bool** |  | [optional] 

## Example

```python
from boldsign.models.existing_form_field import ExistingFormField

# TODO update the JSON string below
json = "{}"
# create an instance of ExistingFormField from a JSON string
existing_form_field_instance = ExistingFormField.from_json(json)
# print the JSON string representation of the object
print(ExistingFormField.to_json())

# convert the object into a dict
existing_form_field_dict = existing_form_field_instance.to_dict()
# create an instance of ExistingFormField from a dict
existing_form_field_from_dict = ExistingFormField.from_dict(existing_form_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


