# EmbeddedDocumentEditJsonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_url** | **str** |  | [optional] 
**show_toolbar** | **bool** |  | [optional] [default to False]
**send_view_option** | **str** |  | [optional] [default to 'PreparePage']
**locale** | **str** |  | [optional] [default to 'EN']
**show_send_button** | **bool** |  | [optional] [default to True]
**show_preview_button** | **bool** |  | [optional] [default to True]
**show_navigation_buttons** | **bool** |  | [optional] [default to True]
**link_valid_till** | **datetime** |  | [optional] 
**on_behalf_of** | **str** |  | [optional] 

## Example

```python
from boldsign.models.embedded_document_edit_json_request import EmbeddedDocumentEditJsonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedDocumentEditJsonRequest from a JSON string
embedded_document_edit_json_request_instance = EmbeddedDocumentEditJsonRequest.from_json(json)
# print the JSON string representation of the object
print(EmbeddedDocumentEditJsonRequest.to_json())

# convert the object into a dict
embedded_document_edit_json_request_dict = embedded_document_edit_json_request_instance.to_dict()
# create an instance of EmbeddedDocumentEditJsonRequest from a dict
embedded_document_edit_json_request_from_dict = EmbeddedDocumentEditJsonRequest.from_dict(embedded_document_edit_json_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


