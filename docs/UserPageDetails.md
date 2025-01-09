# UserPageDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_size** | **int** |  | [optional] 
**page** | **int** |  | [optional] 

## Example

```python
from boldsign.models.user_page_details import UserPageDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UserPageDetails from a JSON string
user_page_details_instance = UserPageDetails.from_json(json)
# print the JSON string representation of the object
print(UserPageDetails.to_json())

# convert the object into a dict
user_page_details_dict = user_page_details_instance.to_dict()
# create an instance of UserPageDetails from a dict
user_page_details_from_dict = UserPageDetails.from_dict(user_page_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


