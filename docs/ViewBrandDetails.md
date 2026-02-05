# ViewBrandDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand_id** | **str** |  | [optional] 
**brand_logo** | **str** |  | [optional] 
**brand_name** | **str** |  | [optional] 
**background_color** | **str** |  | [optional] 
**button_color** | **str** |  | [optional] 
**button_text_color** | **str** |  | [optional] 
**email_display_name** | **str** |  | [optional] 
**disclaimer_title** | **str** |  | [optional] 
**disclaimer_description** | **str** |  | [optional] 
**redirect_url** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**can_hide_tag_line** | **bool** |  | [optional] 
**combine_audit_trail** | **bool** |  | [optional] 
**combine_attachments** | **bool** |  | [optional] 
**exclude_audit_trail_from_email** | **bool** |  | [optional] 
**email_signed_document** | **str** |  | [optional] 
**document_time_zone** | **str** |  | [optional] 
**show_built_in_form_fields** | **bool** |  | [optional] 
**allow_custom_field_creation** | **bool** |  | [optional] 
**show_shared_custom_fields** | **bool** |  | [optional] 
**hide_decline** | **bool** |  | [optional] 
**hide_save** | **bool** |  | [optional] 
**document_expiry_settings** | [**DocumentExpirySettings**](DocumentExpirySettings.md) |  | [optional] 
**custom_domain_settings** | [**CustomDomainSettings**](CustomDomainSettings.md) |  | [optional] 
**is_domain_verified** | **bool** |  | [optional] 
**signature_frame_settings** | [**SignatureFrameSettings**](SignatureFrameSettings.md) |  | [optional] 

## Example

```python
from boldsign.models.view_brand_details import ViewBrandDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ViewBrandDetails from a JSON string
view_brand_details_instance = ViewBrandDetails.from_json(json)
# print the JSON string representation of the object
print(ViewBrandDetails.to_json())

# convert the object into a dict
view_brand_details_dict = view_brand_details_instance.to_dict()
# create an instance of ViewBrandDetails from a dict
view_brand_details_from_dict = ViewBrandDetails.from_dict(view_brand_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


