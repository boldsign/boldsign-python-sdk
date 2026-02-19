# EditDocumentFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edit_action** | **str** |  | 
**file** | **io.IOBase** |  | [optional] 
**file_url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from boldsign.models.edit_document_file import EditDocumentFile

# TODO update the JSON string below
json = "{}"
# create an instance of EditDocumentFile from a JSON string
edit_document_file_instance = EditDocumentFile.from_json(json)
# print the JSON string representation of the object
print(EditDocumentFile.to_json())

# convert the object into a dict
edit_document_file_dict = edit_document_file_instance.to_dict()
# create an instance of EditDocumentFile from a dict
edit_document_file_from_dict = EditDocumentFile.from_dict(edit_document_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


