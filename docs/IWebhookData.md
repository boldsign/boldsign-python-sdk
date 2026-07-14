# IWebhookData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] 
**document_id** | **str** |  | [optional] 
**message_title** | **str** |  | [optional] 
**document_description** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**sender_detail** | [**DocumentSender**](DocumentSender.md) |  | [optional] 
**signer_details** | [**List[TemplateSigner]**](TemplateSigner.md) |  | [optional] 
**cc_details** | [**List[TemplateCcWebhookModel]**](TemplateCcWebhookModel.md) |  | [optional] 
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
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**modified_date** | **datetime** |  | [optional] 
**approved_date_time** | **datetime** |  | [optional] 
**redirect_url** | **str** |  | [optional] 
**created_by** | [**SenderIdentityCreator**](SenderIdentityCreator.md) |  | [optional] 
**locale** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**allow_new_files** | **bool** |  | [optional] 
**allow_modify_files** | **bool** |  | [optional] 
**activity_date** | **datetime** |  | [optional] 
**activity_by** | **str** |  | [optional] 
**template_name** | **str** |  | [optional] 
**template_description** | **str** |  | [optional] 
**is_template** | **bool** |  | [optional] [default to False]
**template_labels** | **List[str]** |  | [optional] 
**form_field_permission** | [**FormFieldPermissionWebhookModel**](FormFieldPermissionWebhookModel.md) |  | [optional] 
**signer_detail** | [**DocumentSignerWebhookModel**](DocumentSignerWebhookModel.md) |  | [optional] 

## Example

```python
from boldsign.models.i_webhook_data import IWebhookData

# TODO update the JSON string below
json = "{}"
# create an instance of IWebhookData from a JSON string
i_webhook_data_instance = IWebhookData.from_json(json)
# print the JSON string representation of the object
print(IWebhookData.to_json())

# convert the object into a dict
i_webhook_data_dict = i_webhook_data_instance.to_dict()
# create an instance of IWebhookData from a dict
i_webhook_data_from_dict = IWebhookData.from_dict(i_webhook_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


