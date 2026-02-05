# AttachmentInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**accepted_file_types** | **List[str]** |  | 
**description** | **str** |  | [optional] 
**allowed_file_types** | **str** |  | [optional] 

## Example

```python
from boldsign.models.attachment_info import AttachmentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentInfo from a JSON string
attachment_info_instance = AttachmentInfo.from_json(json)
# print the JSON string representation of the object
print(AttachmentInfo.to_json())

# convert the object into a dict
attachment_info_dict = attachment_info_instance.to_dict()
# create an instance of AttachmentInfo from a dict
attachment_info_from_dict = AttachmentInfo.from_dict(attachment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


