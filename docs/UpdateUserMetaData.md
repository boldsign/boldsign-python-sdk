# UpdateUserMetaData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**meta_data** | **Dict[str, Optional[str]]** |  | 

## Example

```python
from boldsign.models.update_user_meta_data import UpdateUserMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserMetaData from a JSON string
update_user_meta_data_instance = UpdateUserMetaData.from_json(json)
# print the JSON string representation of the object
print(UpdateUserMetaData.to_json())

# convert the object into a dict
update_user_meta_data_dict = update_user_meta_data_instance.to_dict()
# create an instance of UpdateUserMetaData from a dict
update_user_meta_data_from_dict = UpdateUserMetaData.from_dict(update_user_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


