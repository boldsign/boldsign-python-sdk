# EditDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[EditDocumentFile]**](EditDocumentFile.md) |  | [optional] 
**title** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**signers** | [**List[EditDocumentSigner]**](EditDocumentSigner.md) |  | [optional] 
**cc** | [**List[DocumentCC]**](DocumentCC.md) |  | [optional] 
**enable_signing_order** | **bool** |  | [optional] 
**enable_audit_trail_localization** | **bool** |  | [optional] 
**expiry_date_type** | **str** |  | [optional] 
**expiry_value** | **int** |  | [optional] 
**reminder_settings** | [**ReminderSettings**](ReminderSettings.md) |  | [optional] 
**disable_emails** | **bool** |  | [optional] 
**disable_sms** | **bool** |  | [optional] 
**brand_id** | **str** |  | [optional] 
**hide_document_id** | **bool** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**disable_expiry_alert** | **bool** |  | [optional] 
**enable_print_and_sign** | **bool** |  | [optional] 
**enable_reassign** | **bool** |  | [optional] 
**use_text_tags** | **bool** |  | [optional] 
**text_tag_definitions** | [**List[TextTagDefinition]**](TextTagDefinition.md) |  | [optional] 
**document_info** | [**List[DocumentInfo]**](DocumentInfo.md) |  | [optional] 
**on_behalf_of** | **str** |  | [optional] 
**document_download_option** | **str** |  | [optional] 
**meta_data** | **Dict[str, Optional[str]]** |  | [optional] 
**recipient_notification_settings** | [**RecipientNotificationSettings**](RecipientNotificationSettings.md) |  | [optional] 
**form_groups** | [**List[FormGroup]**](FormGroup.md) |  | [optional] 
**download_file_name** | **str** |  | [optional] 
**scheduled_send_time** | **int** |  | [optional] 
**allowed_signature_types** | **List[str]** |  | [optional] 
**group_signer_settings** | [**GroupSignerSettings**](GroupSignerSettings.md) |  | [optional] 

## Example

```python
from boldsign.models.edit_document_request import EditDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditDocumentRequest from a JSON string
edit_document_request_instance = EditDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(EditDocumentRequest.to_json())

# convert the object into a dict
edit_document_request_dict = edit_document_request_instance.to_dict()
# create an instance of EditDocumentRequest from a dict
edit_document_request_from_dict = EditDocumentRequest.from_dict(edit_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


