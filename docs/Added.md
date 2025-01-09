# Added


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signer_name** | **str** |  | [optional] 
**signer_email** | **str** |  | [optional] 
**signer_phone_number** | **str** |  | [optional] 

## Example

```python
from boldsign.models.added import Added

# TODO update the JSON string below
json = "{}"
# create an instance of Added from a JSON string
added_instance = Added.from_json(json)
# print the JSON string representation of the object
print(Added.to_json())

# convert the object into a dict
added_dict = added_instance.to_dict()
# create an instance of Added from a dict
added_from_dict = Added.from_dict(added_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


