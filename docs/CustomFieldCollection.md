# CustomFieldCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[ViewCustomFieldDetails]**](ViewCustomFieldDetails.md) |  | [optional] 

## Example

```python
from boldsign.models.custom_field_collection import CustomFieldCollection

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldCollection from a JSON string
custom_field_collection_instance = CustomFieldCollection.from_json(json)
# print the JSON string representation of the object
print(CustomFieldCollection.to_json())

# convert the object into a dict
custom_field_collection_dict = custom_field_collection_instance.to_dict()
# create an instance of CustomFieldCollection from a dict
custom_field_collection_from_dict = CustomFieldCollection.from_dict(custom_field_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


