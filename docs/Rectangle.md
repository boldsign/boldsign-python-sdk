# Rectangle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **float** |  | [optional] [default to 0]
**y** | **float** |  | [optional] [default to 0]
**width** | **float** |  | [optional] [default to 1]
**height** | **float** |  | [optional] [default to 1]

## Example

```python
from boldsign.models.rectangle import Rectangle

# TODO update the JSON string below
json = "{}"
# create an instance of Rectangle from a JSON string
rectangle_instance = Rectangle.from_json(json)
# print the JSON string representation of the object
print(Rectangle.to_json())

# convert the object into a dict
rectangle_dict = rectangle_instance.to_dict()
# create an instance of Rectangle from a dict
rectangle_from_dict = Rectangle.from_dict(rectangle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


