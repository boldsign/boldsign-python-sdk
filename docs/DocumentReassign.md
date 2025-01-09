# DocumentReassign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signer_email** | **str** |  | [optional] 
**order** | **int** |  | [optional] [default to 0]
**message** | **str** |  | [optional] 

## Example

```python
from boldsign.models.document_reassign import DocumentReassign

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentReassign from a JSON string
document_reassign_instance = DocumentReassign.from_json(json)
# print the JSON string representation of the object
print(DocumentReassign.to_json())

# convert the object into a dict
document_reassign_dict = document_reassign_instance.to_dict()
# create an instance of DocumentReassign from a dict
document_reassign_from_dict = DocumentReassign.from_dict(document_reassign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


