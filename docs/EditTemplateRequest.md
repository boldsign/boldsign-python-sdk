# EditTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**document_title** | **str** |  | [optional] 
**document_message** | **str** |  | [optional] 
**roles** | [**List[TemplateRole]**](TemplateRole.md) |  | [optional] 
**cc** | [**List[DocumentCC]**](DocumentCC.md) |  | [optional] 
**brand_id** | **str** |  | [optional] 
**allow_message_editing** | **bool** |  | [optional] 
**allow_new_roles** | **bool** |  | [optional] 
**allow_new_files** | **bool** |  | [optional] 
**enable_reassign** | **bool** |  | [optional] 
**enable_print_and_sign** | **bool** |  | [optional] 
**enable_signing_order** | **bool** |  | [optional] 
**document_info** | [**List[DocumentInfo]**](DocumentInfo.md) |  | [optional] 
**on_behalf_of** | **str** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**template_labels** | **List[str]** |  | [optional] 
**form_groups** | [**List[FormGroup]**](FormGroup.md) |  | [optional] 

## Example

```python
from boldsign.models.edit_template_request import EditTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditTemplateRequest from a JSON string
edit_template_request_instance = EditTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(EditTemplateRequest.to_json())

# convert the object into a dict
edit_template_request_dict = edit_template_request_instance.to_dict()
# create an instance of EditTemplateRequest from a dict
edit_template_request_from_dict = EditTemplateRequest.from_dict(edit_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


