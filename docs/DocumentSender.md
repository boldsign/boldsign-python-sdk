# DocumentSender


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 

## Example

```python
from boldsign.models.document_sender import DocumentSender

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSender from a JSON string
document_sender_instance = DocumentSender.from_json(json)
# print the JSON string representation of the object
print(DocumentSender.to_json())

# convert the object into a dict
document_sender_dict = document_sender_instance.to_dict()
# create an instance of DocumentSender from a dict
document_sender_from_dict = DocumentSender.from_dict(document_sender_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


