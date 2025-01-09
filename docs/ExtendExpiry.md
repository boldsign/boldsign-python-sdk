# ExtendExpiry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_expiry_value** | **str** |  | [optional] 
**new_expiry_date** | **str** |  | [optional] 
**warn_prior** | **bool** |  | [optional] 
**on_behalf_of** | **str** |  | [optional] 

## Example

```python
from boldsign.models.extend_expiry import ExtendExpiry

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendExpiry from a JSON string
extend_expiry_instance = ExtendExpiry.from_json(json)
# print the JSON string representation of the object
print(ExtendExpiry.to_json())

# convert the object into a dict
extend_expiry_dict = extend_expiry_instance.to_dict()
# create an instance of ExtendExpiry from a dict
extend_expiry_from_dict = ExtendExpiry.from_dict(extend_expiry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


