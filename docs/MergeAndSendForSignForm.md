# MergeAndSendForSignForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | **List[io.IOBase]** |  | [optional] 
**file_urls** | **List[str]** |  | [optional] 
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
**recipient_notification_settings** | [**RecipientNotificationSettings**](RecipientNotificationSettings.md) |  | [optional] 
**form_groups** | [**List[FormGroup]**](FormGroup.md) |  | [optional] 
**remove_form_fields** | **List[str]** |  | [optional] 
**enable_audit_trail_localization** | **bool** |  | [optional] 
**download_file_name** | **str** |  | [optional] 
**scheduled_send_time** | **int** |  | [optional] 
**allow_scheduled_send** | **bool** |  | [optional] [default to False]

## Example

```python
from boldsign.models.merge_and_send_for_sign_form import MergeAndSendForSignForm

# TODO update the JSON string below
json = "{}"
# create an instance of MergeAndSendForSignForm from a JSON string
merge_and_send_for_sign_form_instance = MergeAndSendForSignForm.from_json(json)
# print the JSON string representation of the object
print(MergeAndSendForSignForm.to_json())

# convert the object into a dict
merge_and_send_for_sign_form_dict = merge_and_send_for_sign_form_instance.to_dict()
# create an instance of MergeAndSendForSignForm from a dict
merge_and_send_for_sign_form_from_dict = MergeAndSendForSignForm.from_dict(merge_and_send_for_sign_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


