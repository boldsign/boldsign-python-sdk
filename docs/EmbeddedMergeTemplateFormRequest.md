# EmbeddedMergeTemplateFormRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | **List[io.IOBase]** |  | [optional] 
**file_urls** | **List[str]** |  | [optional] 
**redirect_url** | **str** |  | [optional] 
**show_toolbar** | **bool** |  | [optional] 
**send_view_option** | **str** |  | [optional] 
**show_save_button** | **bool** |  | [optional] 
**locale** | **str** |  | [optional] 
**show_send_button** | **bool** |  | [optional] 
**show_preview_button** | **bool** |  | [optional] 
**show_navigation_buttons** | **bool** |  | [optional] 
**send_link_valid_till** | **datetime** |  | [optional] 
**show_tooltip** | **bool** |  | [optional] 
**template_ids** | **List[str]** |  | [optional] 
**use_text_tags** | **bool** |  | [optional] 
**text_tag_definitions** | [**List[TextTagDefinition]**](TextTagDefinition.md) |  | [optional] 
**document_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**roles** | [**List[Role]**](Role.md) |  | [optional] 
**brand_id** | **str** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**disable_emails** | **bool** |  | [optional] 
**disable_sms** | **bool** |  | [optional] [default to False]
**hide_document_id** | **bool** |  | [optional] 
**reminder_settings** | [**ReminderSettings**](ReminderSettings.md) |  | [optional] 
**cc** | [**List[DocumentCC]**](DocumentCC.md) |  | [optional] 
**expiry_days** | **int** |  | [optional] 
**expiry_date_type** | **str** |  | [optional] 
**expiry_value** | **int** |  | [optional] [default to 60]
**enable_print_and_sign** | **bool** |  | [optional] 
**enable_reassign** | **bool** |  | [optional] 
**enable_signing_order** | **bool** |  | [optional] 
**disable_expiry_alert** | **bool** |  | [optional] 
**document_info** | [**List[DocumentInfo]**](DocumentInfo.md) |  | [optional] 
**on_behalf_of** | **str** |  | [optional] 
**is_sandbox** | **bool** |  | [optional] 
**role_removal_indices** | **List[int]** |  | [optional] 
**document_download_option** | **str** |  | [optional] 
**meta_data** | **Dict[str, Optional[str]]** |  | [optional] 
**form_groups** | [**List[FormGroup]**](FormGroup.md) |  | [optional] 
**remove_form_fields** | **List[str]** |  | [optional] 
**recipient_notification_settings** | [**RecipientNotificationSettings**](RecipientNotificationSettings.md) |  | [optional] 
**enable_audit_trail_localization** | **bool** |  | [optional] 
**download_file_name** | **str** |  | [optional] 
**scheduled_send_time** | **int** |  | [optional] 
**allow_scheduled_send** | **bool** |  | [optional] [default to False]
**allowed_signature_types** | **List[str]** |  | [optional] 
**group_signer_settings** | [**GroupSignerSettings**](GroupSignerSettings.md) |  | [optional] 

## Example

```python
from boldsign.models.embedded_merge_template_form_request import EmbeddedMergeTemplateFormRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedMergeTemplateFormRequest from a JSON string
embedded_merge_template_form_request_instance = EmbeddedMergeTemplateFormRequest.from_json(json)
# print the JSON string representation of the object
print(EmbeddedMergeTemplateFormRequest.to_json())

# convert the object into a dict
embedded_merge_template_form_request_dict = embedded_merge_template_form_request_instance.to_dict()
# create an instance of EmbeddedMergeTemplateFormRequest from a dict
embedded_merge_template_form_request_from_dict = EmbeddedMergeTemplateFormRequest.from_dict(embedded_merge_template_form_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


