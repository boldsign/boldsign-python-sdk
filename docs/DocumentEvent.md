# DocumentEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] 
**document_id** | **str** |  | [optional] 
**message_title** | **str** |  | [optional] 
**document_description** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**sender_detail** | [**DocumentSender**](DocumentSender.md) |  | [optional] 
**signer_details** | [**List[DocumentSignerWebhookModel]**](DocumentSignerWebhookModel.md) |  | [optional] 
**cc_details** | [**List[DocumentCcWebhookModel]**](DocumentCcWebhookModel.md) |  | [optional] 
**on_behalf_of** | **str** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**expiry_date** | **datetime** |  | [optional] 
**enable_signing_order** | **bool** |  | [optional] 
**disable_emails** | **bool** |  | [optional] 
**revoke_message** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**is_combined_audit** | **bool** |  | [optional] 
**is_combined_attachment** | **bool** |  | [optional] 
**brand_id** | **str** |  | [optional] 
**document_download_option** | **str** |  | [optional] 
**meta_data** | **Dict[str, Optional[str]]** |  | [optional] 
**failed_delivery_mode** | **str** |  | [optional] 
**behalf_of** | [**BehalfOfWebhookModel**](BehalfOfWebhookModel.md) |  | [optional] 
**allowed_signature_types** | **List[str]** |  | [optional] 
**group_signer_settings** | [**GroupSignerSettingsWebhookModel**](GroupSignerSettingsWebhookModel.md) |  | [optional] 
**enable_allow_sign_everywhere** | **bool** |  | [optional] 
**document_time_zone** | **str** |  | [optional] 

## Example

```python
from boldsign.models.document_event import DocumentEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentEvent from a JSON string
document_event_instance = DocumentEvent.from_json(json)
# print the JSON string representation of the object
print(DocumentEvent.to_json())

# convert the object into a dict
document_event_dict = document_event_instance.to_dict()
# create an instance of DocumentEvent from a dict
document_event_from_dict = DocumentEvent.from_dict(document_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


