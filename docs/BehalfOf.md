# BehalfOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 

## Example

```python
from boldsign.models.behalf_of import BehalfOf

# TODO update the JSON string below
json = "{}"
# create an instance of BehalfOf from a JSON string
behalf_of_instance = BehalfOf.from_json(json)
# print the JSON string representation of the object
print(BehalfOf.to_json())

# convert the object into a dict
behalf_of_dict = behalf_of_instance.to_dict()
# create an instance of BehalfOf from a dict
behalf_of_from_dict = BehalfOf.from_dict(behalf_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


