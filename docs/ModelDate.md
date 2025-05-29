# ModelDate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **int** |  | [optional] 
**month** | **int** |  | [optional] 
**year** | **int** |  | [optional] 

## Example

```python
from boldsign.models.model_date import ModelDate

# TODO update the JSON string below
json = "{}"
# create an instance of ModelDate from a JSON string
model_date_instance = ModelDate.from_json(json)
# print the JSON string representation of the object
print(ModelDate.to_json())

# convert the object into a dict
model_date_dict = model_date_instance.to_dict()
# create an instance of ModelDate from a dict
model_date_from_dict = ModelDate.from_dict(model_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


