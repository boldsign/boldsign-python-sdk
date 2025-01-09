# Validation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**regex** | **str** |  | [optional] 

## Example

```python
from boldsign.models.validation import Validation

# TODO update the JSON string below
json = "{}"
# create an instance of Validation from a JSON string
validation_instance = Validation.from_json(json)
# print the JSON string representation of the object
print(Validation.to_json())

# convert the object into a dict
validation_dict = validation_instance.to_dict()
# create an instance of Validation from a dict
validation_from_dict = Validation.from_dict(validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


