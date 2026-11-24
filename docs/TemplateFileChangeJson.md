# TemplateFileChangeJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | [**Base64File**](Base64File.md) |  | [optional] 
**file_url** | **str** |  | [optional] 
**edit_action** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**file_order** | **int** |  | [optional] 

## Example

```python
from boldsign.models.template_file_change_json import TemplateFileChangeJson

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateFileChangeJson from a JSON string
template_file_change_json_instance = TemplateFileChangeJson.from_json(json)
# print the JSON string representation of the object
print(TemplateFileChangeJson.to_json())

# convert the object into a dict
template_file_change_json_dict = template_file_change_json_instance.to_dict()
# create an instance of TemplateFileChangeJson from a dict
template_file_change_json_from_dict = TemplateFileChangeJson.from_dict(template_file_change_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


