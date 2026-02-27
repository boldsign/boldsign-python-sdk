# Creators


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 

## Example

```python
from boldsign.models.creators import Creators

# TODO update the JSON string below
json = "{}"
# create an instance of Creators from a JSON string
creators_instance = Creators.from_json(json)
# print the JSON string representation of the object
print(Creators.to_json())

# convert the object into a dict
creators_dict = creators_instance.to_dict()
# create an instance of Creators from a dict
creators_from_dict = Creators.from_dict(creators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


