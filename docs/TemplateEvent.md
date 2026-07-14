# TemplateEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**allow_new_files** | **bool** |  | [optional] 
**allow_modify_files** | **bool** |  | [optional] 
**sender_detail** | [**TemplateSender**](TemplateSender.md) |  | [optional] 
**cc_details** | [**List[TemplateCcWebhookModel]**](TemplateCcWebhookModel.md) |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**activity_date** | **datetime** |  | [optional] 
**activity_by** | **str** |  | [optional] 
**message_title** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**signer_details** | [**List[TemplateSigner]**](TemplateSigner.md) |  | [optional] 
**enable_signing_order** | **bool** |  | [optional] 
**template_name** | **str** |  | [optional] 
**template_description** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**is_template** | **bool** |  | [optional] [default to False]
**brand_id** | **str** |  | [optional] 
**on_behalf_of** | **str** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**template_labels** | **List[str]** |  | [optional] 
**form_field_permission** | [**FormFieldPermissionWebhookModel**](FormFieldPermissionWebhookModel.md) |  | [optional] 
**group_signer_settings** | [**GroupSignerSettingsWebhookModel**](GroupSignerSettingsWebhookModel.md) |  | [optional] 
**behalf_of** | [**BehalfOfWebhookModel**](BehalfOfWebhookModel.md) |  | [optional] 
**enable_allow_sign_everywhere** | **bool** |  | [optional] 
**document_time_zone** | **str** |  | [optional] 

## Example

```python
from boldsign.models.template_event import TemplateEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateEvent from a JSON string
template_event_instance = TemplateEvent.from_json(json)
# print the JSON string representation of the object
print(TemplateEvent.to_json())

# convert the object into a dict
template_event_dict = template_event_instance.to_dict()
# create an instance of TemplateEvent from a dict
template_event_from_dict = TemplateEvent.from_dict(template_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


