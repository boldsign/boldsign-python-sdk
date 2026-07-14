# EmbeddedClonedDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** |  | [optional] 
**embed_url** | **str** |  | [optional] 

## Example

```python
from boldsign.models.embedded_cloned_document import EmbeddedClonedDocument

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedClonedDocument from a JSON string
embedded_cloned_document_instance = EmbeddedClonedDocument.from_json(json)
# print the JSON string representation of the object
print(EmbeddedClonedDocument.to_json())

# convert the object into a dict
embedded_cloned_document_dict = embedded_cloned_document_instance.to_dict()
# create an instance of EmbeddedClonedDocument from a dict
embedded_cloned_document_from_dict = EmbeddedClonedDocument.from_dict(embedded_cloned_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


