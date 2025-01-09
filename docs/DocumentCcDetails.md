# DocumentCcDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** |  | [optional] 
**is_viewed** | **bool** |  | [optional] [default to False]

## Example

```python
from boldsign.models.document_cc_details import DocumentCcDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCcDetails from a JSON string
document_cc_details_instance = DocumentCcDetails.from_json(json)
# print the JSON string representation of the object
print(DocumentCcDetails.to_json())

# convert the object into a dict
document_cc_details_dict = document_cc_details_instance.to_dict()
# create an instance of DocumentCcDetails from a dict
document_cc_details_from_dict = DocumentCcDetails.from_dict(document_cc_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


