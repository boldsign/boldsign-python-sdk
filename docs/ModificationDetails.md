# ModificationDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**removed_count** | **int** |  | [optional] 
**added_count** | **int** |  | [optional] 

## Example

```python
from boldsign.models.modification_details import ModificationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ModificationDetails from a JSON string
modification_details_instance = ModificationDetails.from_json(json)
# print the JSON string representation of the object
print(ModificationDetails.to_json())

# convert the object into a dict
modification_details_dict = modification_details_instance.to_dict()
# create an instance of ModificationDetails from a dict
modification_details_from_dict = ModificationDetails.from_dict(modification_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


