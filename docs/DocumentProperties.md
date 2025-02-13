# DocumentProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** |  | [optional] 
**brand_id** | **str** |  | [optional] 
**message_title** | **str** |  | [optional] 
**document_description** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**files** | [**List[DocumentFiles]**](DocumentFiles.md) |  | [optional] 
**sender_detail** | [**DocumentSenderDetail**](DocumentSenderDetail.md) |  | [optional] 
**signer_details** | [**List[DocumentSignerDetails]**](DocumentSignerDetails.md) |  | [optional] 
**form_groups** | [**List[FormGroup]**](FormGroup.md) |  | [optional] 
**common_fields** | [**List[DocumentFormFields]**](DocumentFormFields.md) |  | [optional] 
**behalf_of** | [**BehalfOf**](BehalfOf.md) |  | [optional] 
**cc_details** | [**List[DocumentCcDetails]**](DocumentCcDetails.md) |  | [optional] 
**reminder_settings** | [**ReminderSettings**](ReminderSettings.md) |  | [optional] 
**reassign** | [**List[DocumentReassign]**](DocumentReassign.md) |  | [optional] 
**document_history** | [**List[AuditTrail]**](AuditTrail.md) |  | [optional] 
**activity_by** | **str** |  | [optional] 
**activity_date** | **int** |  | [optional] 
**activity_action** | **str** |  | [optional] 
**created_date** | **int** |  | [optional] 
**expiry_days** | **int** |  | [optional] 
**expiry_date** | **int** |  | [optional] 
**enable_signing_order** | **bool** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**revoke_message** | **str** |  | [optional] 
**decline_message** | **str** |  | [optional] 
**application_id** | **str** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**disable_emails** | **bool** |  | [optional] 
**enable_print_and_sign** | **bool** |  | [optional] 
**enable_reassign** | **bool** |  | [optional] 
**disable_expiry_alert** | **bool** |  | [optional] 
**hide_document_id** | **bool** |  | [optional] 
**expiry_date_type** | **str** |  | [optional] 
**expiry_value** | **int** |  | [optional] 
**document_download_option** | **str** |  | [optional] 
**meta_data** | **Dict[str, Optional[str]]** |  | [optional] 
**enable_audit_trail_localization** | **bool** |  | [optional] 
**download_file_name** | **str** |  | [optional] 
**recipient_notification_settings** | [**RecipientNotificationSettings**](RecipientNotificationSettings.md) |  | [optional] 

## Example

```python
from boldsign.models.document_properties import DocumentProperties

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentProperties from a JSON string
document_properties_instance = DocumentProperties.from_json(json)
# print the JSON string representation of the object
print(DocumentProperties.to_json())

# convert the object into a dict
document_properties_dict = document_properties_instance.to_dict()
# create an instance of DocumentProperties from a dict
document_properties_from_dict = DocumentProperties.from_dict(document_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


