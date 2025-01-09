# ContactPageDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_size** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**total_records_count** | **int** |  | [optional] 

## Example

```python
from boldsign.models.contact_page_details import ContactPageDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ContactPageDetails from a JSON string
contact_page_details_instance = ContactPageDetails.from_json(json)
# print the JSON string representation of the object
print(ContactPageDetails.to_json())

# convert the object into a dict
contact_page_details_dict = contact_page_details_instance.to_dict()
# create an instance of ContactPageDetails from a dict
contact_page_details_from_dict = ContactPageDetails.from_dict(contact_page_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


