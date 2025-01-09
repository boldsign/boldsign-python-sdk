# PrefillField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from boldsign.models.prefill_field import PrefillField

# TODO update the JSON string below
json = "{}"
# create an instance of PrefillField from a JSON string
prefill_field_instance = PrefillField.from_json(json)
# print the JSON string representation of the object
print(PrefillField.to_json())

# convert the object into a dict
prefill_field_dict = prefill_field_instance.to_dict()
# create an instance of PrefillField from a dict
prefill_field_from_dict = PrefillField.from_dict(prefill_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


