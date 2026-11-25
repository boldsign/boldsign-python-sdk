# TemplateFileChangeForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **io.IOBase** |  | [optional] 
**file_url** | **str** |  | [optional] 
**edit_action** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**file_order** | **int** |  | [optional] 

## Example

```python
from boldsign.models.template_file_change_form import TemplateFileChangeForm

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateFileChangeForm from a JSON string
template_file_change_form_instance = TemplateFileChangeForm.from_json(json)
# print the JSON string representation of the object
print(TemplateFileChangeForm.to_json())

# convert the object into a dict
template_file_change_form_dict = template_file_change_form_instance.to_dict()
# create an instance of TemplateFileChangeForm from a dict
template_file_change_form_from_dict = TemplateFileChangeForm.from_dict(template_file_change_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


