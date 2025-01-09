# DocumentRecords


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_details** | [**PageDetails**](PageDetails.md) |  | [optional] 
**result** | [**List[Document]**](Document.md) |  | [optional] 

## Example

```python
from boldsign.models.document_records import DocumentRecords

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentRecords from a JSON string
document_records_instance = DocumentRecords.from_json(json)
# print the JSON string representation of the object
print(DocumentRecords.to_json())

# convert the object into a dict
document_records_dict = document_records_instance.to_dict()
# create an instance of DocumentRecords from a dict
document_records_from_dict = DocumentRecords.from_dict(document_records_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


