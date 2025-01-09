# DocumentTags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** |  | 
**tags** | **List[str]** |  | 

## Example

```python
from boldsign.models.document_tags import DocumentTags

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTags from a JSON string
document_tags_instance = DocumentTags.from_json(json)
# print the JSON string representation of the object
print(DocumentTags.to_json())

# convert the object into a dict
document_tags_dict = document_tags_instance.to_dict()
# create an instance of DocumentTags from a dict
document_tags_from_dict = DocumentTags.from_dict(document_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


