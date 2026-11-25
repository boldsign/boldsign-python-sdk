# TemplateFileChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edit_action** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**file_order** | **int** |  | [optional] 

## Example

```python
from boldsign.models.template_file_change import TemplateFileChange

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateFileChange from a JSON string
template_file_change_instance = TemplateFileChange.from_json(json)
# print the JSON string representation of the object
print(TemplateFileChange.to_json())

# convert the object into a dict
template_file_change_dict = template_file_change_instance.to_dict()
# create an instance of TemplateFileChange from a dict
template_file_change_from_dict = TemplateFileChange.from_dict(template_file_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


