# Removed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signer_name** | **str** |  | [optional] 
**signer_email** | **str** |  | [optional] 
**signer_phone_number** | **str** |  | [optional] 

## Example

```python
from boldsign.models.removed import Removed

# TODO update the JSON string below
json = "{}"
# create an instance of Removed from a JSON string
removed_instance = Removed.from_json(json)
# print the JSON string representation of the object
print(Removed.to_json())

# convert the object into a dict
removed_dict = removed_instance.to_dict()
# create an instance of Removed from a dict
removed_from_dict = Removed.from_dict(removed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


