# TemplateProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**document_title** | **str** |  | [optional] 
**document_message** | **str** |  | [optional] 
**files** | [**List[TemplateFiles]**](TemplateFiles.md) |  | [optional] 
**roles** | [**List[Roles]**](Roles.md) |  | [optional] 
**form_groups** | [**List[FormGroup]**](FormGroup.md) |  | [optional] 
**common_fields** | [**List[TemplateFormFields]**](TemplateFormFields.md) |  | [optional] 
**c_c_details** | **List[str]** |  | [optional] 
**brand_id** | **str** |  | [optional] 
**allow_message_editing** | **bool** |  | [optional] 
**allow_new_roles** | **bool** |  | [optional] 
**allow_new_files** | **bool** |  | [optional] 
**allow_modify_files** | **bool** |  | [optional] 
**enable_reassign** | **bool** |  | [optional] 
**enable_print_and_sign** | **bool** |  | [optional] 
**enable_signing_order** | **bool** |  | [optional] 
**created_date** | **int** |  | [optional] 
**created_by** | [**TemplateSenderDetail**](TemplateSenderDetail.md) |  | [optional] 
**shared_template_detail** | [**List[TemplateSharedTemplateDetail]**](TemplateSharedTemplateDetail.md) |  | [optional] 
**document_info** | [**List[DocumentInfo]**](DocumentInfo.md) |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**template_labels** | **List[str]** |  | [optional] 
**behalf_of** | [**BehalfOf**](BehalfOf.md) |  | [optional] 
**document_download_option** | **str** |  | [optional] 
**recipient_notification_settings** | [**RecipientNotificationSettings**](RecipientNotificationSettings.md) |  | [optional] 
**form_field_permission** | [**FormFieldPermission**](FormFieldPermission.md) |  | [optional] 
**allowed_signature_types** | **List[str]** |  | [optional] 
**group_signer_settings** | [**GroupSignerSettings**](GroupSignerSettings.md) |  | [optional] 
**sharing** | [**TemplateSharing**](TemplateSharing.md) |  | [optional] 

## Example

```python
from boldsign.models.template_properties import TemplateProperties

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateProperties from a JSON string
template_properties_instance = TemplateProperties.from_json(json)
# print the JSON string representation of the object
print(TemplateProperties.to_json())

# convert the object into a dict
template_properties_dict = template_properties_instance.to_dict()
# create an instance of TemplateProperties from a dict
template_properties_from_dict = TemplateProperties.from_dict(template_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


