# EditDocumentJsonFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edit_action** | **str** |  | 
**file** | [**Base64File**](Base64File.md) |  | [optional] 
**file_url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from boldsign.models.edit_document_json_file import EditDocumentJsonFile

# TODO update the JSON string below
json = "{}"
# create an instance of EditDocumentJsonFile from a JSON string
edit_document_json_file_instance = EditDocumentJsonFile.from_json(json)
# print the JSON string representation of the object
print(EditDocumentJsonFile.to_json())

# convert the object into a dict
edit_document_json_file_dict = edit_document_json_file_instance.to_dict()
# create an instance of EditDocumentJsonFile from a dict
edit_document_json_file_from_dict = EditDocumentJsonFile.from_dict(edit_document_json_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


