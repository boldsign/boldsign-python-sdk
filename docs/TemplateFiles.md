# TemplateFiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** |  | [optional] 
**document_name** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**page_count** | **int** |  | [optional] 

## Example

```python
from boldsign.models.template_files import TemplateFiles

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateFiles from a JSON string
template_files_instance = TemplateFiles.from_json(json)
# print the JSON string representation of the object
print(TemplateFiles.to_json())

# convert the object into a dict
template_files_dict = template_files_instance.to_dict()
# create an instance of TemplateFiles from a dict
template_files_from_dict = TemplateFiles.from_dict(template_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


