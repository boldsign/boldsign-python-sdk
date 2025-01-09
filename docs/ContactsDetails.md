# ContactsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 
**phone_number** | [**PhoneNumber**](PhoneNumber.md) |  | [optional] 

## Example

```python
from boldsign.models.contacts_details import ContactsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ContactsDetails from a JSON string
contacts_details_instance = ContactsDetails.from_json(json)
# print the JSON string representation of the object
print(ContactsDetails.to_json())

# convert the object into a dict
contacts_details_dict = contacts_details_instance.to_dict()
# create an instance of ContactsDetails from a dict
contacts_details_from_dict = ContactsDetails.from_dict(contacts_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


