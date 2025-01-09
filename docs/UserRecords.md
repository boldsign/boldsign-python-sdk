# UserRecords


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_details** | [**UserPageDetails**](UserPageDetails.md) |  | [optional] 
**result** | [**List[UsersDetails]**](UsersDetails.md) |  | [optional] 

## Example

```python
from boldsign.models.user_records import UserRecords

# TODO update the JSON string below
json = "{}"
# create an instance of UserRecords from a JSON string
user_records_instance = UserRecords.from_json(json)
# print the JSON string representation of the object
print(UserRecords.to_json())

# convert the object into a dict
user_records_dict = user_records_instance.to_dict()
# create an instance of UserRecords from a dict
user_records_from_dict = UserRecords.from_dict(user_records_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


