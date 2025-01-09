# ContactsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_details** | [**ContactPageDetails**](ContactPageDetails.md) |  | [optional] 
**result** | [**List[ContactsDetails]**](ContactsDetails.md) |  | [optional] 

## Example

```python
from boldsign.models.contacts_list import ContactsList

# TODO update the JSON string below
json = "{}"
# create an instance of ContactsList from a JSON string
contacts_list_instance = ContactsList.from_json(json)
# print the JSON string representation of the object
print(ContactsList.to_json())

# convert the object into a dict
contacts_list_dict = contacts_list_instance.to_dict()
# create an instance of ContactsList from a dict
contacts_list_from_dict = ContactsList.from_dict(contacts_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


