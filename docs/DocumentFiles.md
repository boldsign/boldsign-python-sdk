# DocumentFiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**document_name** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**page_count** | **int** |  | [optional] 
**template_name** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 

## Example

```python
from boldsign.models.document_files import DocumentFiles

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFiles from a JSON string
document_files_instance = DocumentFiles.from_json(json)
# print the JSON string representation of the object
print(DocumentFiles.to_json())

# convert the object into a dict
document_files_dict = document_files_instance.to_dict()
# create an instance of DocumentFiles from a dict
document_files_from_dict = DocumentFiles.from_dict(document_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


