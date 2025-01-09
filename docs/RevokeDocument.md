# RevokeDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**on_behalf_of** | **str** |  | [optional] 

## Example

```python
from boldsign.models.revoke_document import RevokeDocument

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeDocument from a JSON string
revoke_document_instance = RevokeDocument.from_json(json)
# print the JSON string representation of the object
print(RevokeDocument.to_json())

# convert the object into a dict
revoke_document_dict = revoke_document_instance.to_dict()
# create an instance of RevokeDocument from a dict
revoke_document_from_dict = RevokeDocument.from_dict(revoke_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


