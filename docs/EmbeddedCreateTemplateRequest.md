# EmbeddedCreateTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**redirect_url** | **str** |  | [optional] 
**show_toolbar** | **bool** |  | [optional] [default to False]
**view_option** | **str** |  | [optional] [default to 'PreparePage']
**show_save_button** | **bool** |  | [optional] [default to True]
**locale** | **str** |  | [optional] [default to 'EN']
**show_send_button** | **bool** |  | [optional] 
**show_create_button** | **bool** |  | [optional] [default to True]
**show_preview_button** | **bool** |  | [optional] [default to True]
**show_navigation_buttons** | **bool** |  | [optional] [default to True]
**link_valid_till** | **datetime** |  | [optional] 
**show_tooltip** | **bool** |  | [optional] [default to False]
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
**enable_print_and_assign** | **bool** |  | [optional] [default to False]
**enable_signing_order** | **bool** |  | [optional] [default to False]
**document_info** | [**List[DocumentInfo]**](DocumentInfo.md) |  | [optional] 
**use_text_tags** | **bool** |  | [optional] [default to False]
**text_tag_definitions** | [**List[TextTagDefinition]**](TextTagDefinition.md) |  | [optional] 
**auto_detect_fields** | **bool** |  | [optional] [default to False]
**on_behalf_of** | **str** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**template_labels** | **List[str]** |  | [optional] 
**recipient_notification_settings** | [**RecipientNotificationSettings**](RecipientNotificationSettings.md) |  | [optional] 
**form_groups** | [**List[FormGroup]**](FormGroup.md) |  | [optional] 

## Example

```python
from boldsign.models.embedded_create_template_request import EmbeddedCreateTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedCreateTemplateRequest from a JSON string
embedded_create_template_request_instance = EmbeddedCreateTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(EmbeddedCreateTemplateRequest.to_json())

# convert the object into a dict
embedded_create_template_request_dict = embedded_create_template_request_instance.to_dict()
# create an instance of EmbeddedCreateTemplateRequest from a dict
embedded_create_template_request_from_dict = EmbeddedCreateTemplateRequest.from_dict(embedded_create_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


