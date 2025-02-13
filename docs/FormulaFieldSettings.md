# FormulaFieldSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formula_expression** | **str** |  | [optional] 
**decimal_precision** | **int** |  | [optional] [default to 0]

## Example

```python
from boldsign.models.formula_field_settings import FormulaFieldSettings

# TODO update the JSON string below
json = "{}"
# create an instance of FormulaFieldSettings from a JSON string
formula_field_settings_instance = FormulaFieldSettings.from_json(json)
# print the JSON string representation of the object
print(FormulaFieldSettings.to_json())

# convert the object into a dict
formula_field_settings_dict = formula_field_settings_instance.to_dict()
# create an instance of FormulaFieldSettings from a dict
formula_field_settings_from_dict = FormulaFieldSettings.from_dict(formula_field_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


