# RemoveAuthentication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_id** | **str** |  | [optional] 
**z_order** | **int** |  | [optional] 
**phone_number** | [**PhoneNumber**](PhoneNumber.md) |  | [optional] 
**on_behalf_of** | **str** |  | [optional] 

## Example

```python
from boldsign.models.remove_authentication import RemoveAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveAuthentication from a JSON string
remove_authentication_instance = RemoveAuthentication.from_json(json)
# print the JSON string representation of the object
print(RemoveAuthentication.to_json())

# convert the object into a dict
remove_authentication_dict = remove_authentication_instance.to_dict()
# create an instance of RemoveAuthentication from a dict
remove_authentication_from_dict = RemoveAuthentication.from_dict(remove_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


