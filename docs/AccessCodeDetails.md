# AccessCodeDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_code** | **str** |  | 
**phone_number** | [**PhoneNumber**](PhoneNumber.md) |  | [optional] 
**on_behalf_of** | **str** |  | [optional] 

## Example

```python
from boldsign.models.access_code_details import AccessCodeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AccessCodeDetails from a JSON string
access_code_details_instance = AccessCodeDetails.from_json(json)
# print the JSON string representation of the object
print(AccessCodeDetails.to_json())

# convert the object into a dict
access_code_details_dict = access_code_details_instance.to_dict()
# create an instance of AccessCodeDetails from a dict
access_code_details_from_dict = AccessCodeDetails.from_dict(access_code_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


