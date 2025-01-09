# CreateContactResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_contacts** | [**List[ContactCreated]**](ContactCreated.md) |  | [optional] 

## Example

```python
from boldsign.models.create_contact_response import CreateContactResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContactResponse from a JSON string
create_contact_response_instance = CreateContactResponse.from_json(json)
# print the JSON string representation of the object
print(CreateContactResponse.to_json())

# convert the object into a dict
create_contact_response_dict = create_contact_response_instance.to_dict()
# create an instance of CreateContactResponse from a dict
create_contact_response_from_dict = CreateContactResponse.from_dict(create_contact_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


