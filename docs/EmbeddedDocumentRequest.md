# EmbeddedDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_url** | **str** |  | [optional] 
**show_toolbar** | **bool** |  | [optional] [default to False]
**send_view_option** | **str** |  | [optional] [default to 'PreparePage']
**show_save_button** | **bool** |  | [optional] [default to True]
**locale** | **str** |  | [optional] [default to 'EN']
**show_send_button** | **bool** |  | [optional] [default to True]
**show_preview_button** | **bool** |  | [optional] [default to True]
**show_navigation_buttons** | **bool** |  | [optional] [default to True]
**show_tooltip** | **bool** |  | [optional] [default to False]
**embedded_send_link_valid_till** | **datetime** |  | [optional] 
**files** | **List[io.IOBase]** |  | [optional] 
**title** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**signers** | [**List[DocumentSigner]**](DocumentSigner.md) |  | [optional] 
**cc** | [**List[DocumentCC]**](DocumentCC.md) |  | [optional] 
**enable_signing_order** | **bool** |  | [optional] [default to False]
**expiry_days** | **int** |  | [optional] 
**expiry_date_type** | **str** |  | [optional] 
**expiry_value** | **int** |  | [optional] [default to 60]
**reminder_settings** | [**ReminderSettings**](ReminderSettings.md) |  | [optional] 
**enable_embedded_signing** | **bool** |  | [optional] [default to False]
**disable_emails** | **bool** |  | [optional] [default to False]
**disable_sms** | **bool** |  | [optional] [default to False]
**brand_id** | **str** |  | [optional] 
**hide_document_id** | **bool** |  | [optional] [default to False]
**labels** | **List[str]** |  | [optional] 
**file_urls** | **List[str]** |  | [optional] 
**send_link_valid_till** | **datetime** |  | [optional] 
**use_text_tags** | **bool** |  | [optional] [default to False]
**text_tag_definitions** | [**List[TextTagDefinition]**](TextTagDefinition.md) |  | [optional] 
**enable_print_and_sign** | **bool** |  | [optional] [default to False]
**enable_reassign** | **bool** |  | [optional] [default to True]
**disable_expiry_alert** | **bool** |  | [optional] 
**document_info** | [**List[DocumentInfo]**](DocumentInfo.md) |  | [optional] 
**on_behalf_of** | **str** |  | [optional] 
**auto_detect_fields** | **bool** |  | [optional] [default to False]
**document_download_option** | **str** |  | [optional] 
**is_sandbox** | **bool** |  | [optional] 
**meta_data** | **Dict[str, Optional[str]]** |  | [optional] 
**form_groups** | [**List[FormGroup]**](FormGroup.md) |  | [optional] 
**recipient_notification_settings** | [**RecipientNotificationSettings**](RecipientNotificationSettings.md) |  | [optional] 
**enable_audit_trail_localization** | **bool** |  | [optional] 
**download_file_name** | **str** |  | [optional] 
**scheduled_send_time** | **int** |  | [optional] 
**allow_scheduled_send** | **bool** |  | [optional] [default to False]
**allowed_signature_types** | **List[str]** |  | [optional] 
**group_signer_settings** | [**GroupSignerSettings**](GroupSignerSettings.md) |  | [optional] 

## Example

```python
from boldsign.models.embedded_document_request import EmbeddedDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedDocumentRequest from a JSON string
embedded_document_request_instance = EmbeddedDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(EmbeddedDocumentRequest.to_json())

# convert the object into a dict
embedded_document_request_dict = embedded_document_request_instance.to_dict()
# create an instance of EmbeddedDocumentRequest from a dict
embedded_document_request_from_dict = EmbeddedDocumentRequest.from_dict(embedded_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


