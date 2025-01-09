# DocumentSenderDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**private_message** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**is_viewed** | **bool** |  | [optional] [default to False]

## Example

```python
from boldsign.models.document_sender_detail import DocumentSenderDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSenderDetail from a JSON string
document_sender_detail_instance = DocumentSenderDetail.from_json(json)
# print the JSON string representation of the object
print(DocumentSenderDetail.to_json())

# convert the object into a dict
document_sender_detail_dict = document_sender_detail_instance.to_dict()
# create an instance of DocumentSenderDetail from a dict
document_sender_detail_from_dict = DocumentSenderDetail.from_dict(document_sender_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


