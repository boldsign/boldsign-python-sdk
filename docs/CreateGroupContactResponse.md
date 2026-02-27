# CreateGroupContactResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 

## Example

```python
from boldsign.models.create_group_contact_response import CreateGroupContactResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGroupContactResponse from a JSON string
create_group_contact_response_instance = CreateGroupContactResponse.from_json(json)
# print the JSON string representation of the object
print(CreateGroupContactResponse.to_json())

# convert the object into a dict
create_group_contact_response_dict = create_group_contact_response_instance.to_dict()
# create an instance of CreateGroupContactResponse from a dict
create_group_contact_response_from_dict = CreateGroupContactResponse.from_dict(create_group_contact_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


