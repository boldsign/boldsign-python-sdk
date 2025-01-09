# ContactCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from boldsign.models.contact_created import ContactCreated

# TODO update the JSON string below
json = "{}"
# create an instance of ContactCreated from a JSON string
contact_created_instance = ContactCreated.from_json(json)
# print the JSON string representation of the object
print(ContactCreated.to_json())

# convert the object into a dict
contact_created_dict = contact_created_instance.to_dict()
# create an instance of ContactCreated from a dict
contact_created_from_dict = ContactCreated.from_dict(contact_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


