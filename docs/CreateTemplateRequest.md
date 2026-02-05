# CreateTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**document_title** | **str** |  | [optional] 
**document_message** | **str** |  | [optional] 
**files** | **List[io.IOBase]** |  | [optional] 
**file_urls** | **List[str]** |  | [optional] 
**roles** | [**List[TemplateRole]**](TemplateRole.md) |  | [optional] 
**allow_modify_files** | **bool** |  | [optional] [default to True]
**cc** | [**List[DocumentCC]**](DocumentCC.md) |  | [optional] 
**brand_id** | **str** |  | [optional] 
**allow_message_editing** | **bool** |  | [optional] [default to True]
**allow_new_roles** | **bool** |  | [optional] [default to True]
**allow_new_files** | **bool** |  | [optional] [default to True]
**enable_reassign** | **bool** |  | [optional] [default to True]
**enable_print_and_sign** | **bool** |  | [optional] [default to False]
**enable_signing_order** | **bool** |  | [optional] [default to False]
**document_info** | [**List[DocumentInfo]**](DocumentInfo.md) |  | [optional] 
**use_text_tags** | **bool** |  | [optional] [default to False]
**text_tag_definitions** | [**List[TextTagDefinition]**](TextTagDefinition.md) |  | [optional] 
**auto_detect_fields** | **bool** |  | [optional] [default to False]
**on_behalf_of** | **str** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**template_labels** | **List[str]** |  | [optional] 
**form_groups** | [**List[FormGroup]**](FormGroup.md) |  | [optional] 
**recipient_notification_settings** | [**RecipientNotificationSettings**](RecipientNotificationSettings.md) |  | [optional] 
**allowed_signature_types** | **List[str]** |  | [optional] 
**form_field_permission** | [**FormFieldPermission**](FormFieldPermission.md) |  | [optional] 
**group_signer_settings** | [**GroupSignerSettings**](GroupSignerSettings.md) |  | [optional] 

## Example

```python
from boldsign.models.create_template_request import CreateTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTemplateRequest from a JSON string
create_template_request_instance = CreateTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTemplateRequest.to_json())

# convert the object into a dict
create_template_request_dict = create_template_request_instance.to_dict()
# create an instance of CreateTemplateRequest from a dict
create_template_request_from_dict = CreateTemplateRequest.from_dict(create_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


