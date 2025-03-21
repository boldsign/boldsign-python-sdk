# boldsign.BrandingApi

All URIs are relative to *https://api.boldsign.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**brand_list**](BrandingApi.md#brand_list) | **GET** /v1/brand/list | List all the brands.
[**create_brand**](BrandingApi.md#create_brand) | **POST** /v1/brand/create | Create the brand.
[**delete_brand**](BrandingApi.md#delete_brand) | **DELETE** /v1/brand/delete | Delete the brand.
[**edit_brand**](BrandingApi.md#edit_brand) | **POST** /v1/brand/edit | Edit the brand.
[**get_brand**](BrandingApi.md#get_brand) | **GET** /v1/brand/get | Get the specific brand details.
[**reset_default_brand**](BrandingApi.md#reset_default_brand) | **POST** /v1/brand/resetdefault | Reset default brand.


# **brand_list**
> BrandingRecords brand_list()

List all the brands.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.branding_records import BrandingRecords
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.BrandingApi(api_client)

    try:
        # List all the brands.
        api_response = api_instance.brand_list()
        print("The response of BrandingApi->brand_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingApi->brand_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BrandingRecords**](BrandingRecords.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_brand**
> BrandCreated create_brand(brand_name, brand_logo, background_color=background_color, button_color=button_color, button_text_color=button_text_color, email_display_name=email_display_name, disclaimer_description=disclaimer_description, disclaimer_title=disclaimer_title, redirect_url=redirect_url, is_default=is_default, can_hide_tag_line=can_hide_tag_line, combine_audit_trail=combine_audit_trail, exclude_audit_trail_from_email=exclude_audit_trail_from_email, email_signed_document=email_signed_document, document_time_zone=document_time_zone, show_built_in_form_fields=show_built_in_form_fields, allow_custom_field_creation=allow_custom_field_creation, show_shared_custom_fields=show_shared_custom_fields, hide_decline=hide_decline, hide_save=hide_save, document_expiry_settings_expiry_date_type=document_expiry_settings_expiry_date_type, document_expiry_settings_expiry_value=document_expiry_settings_expiry_value, document_expiry_settings_enable_default_expiry_alert=document_expiry_settings_enable_default_expiry_alert, document_expiry_settings_enable_auto_reminder=document_expiry_settings_enable_auto_reminder, document_expiry_settings_reminder_days=document_expiry_settings_reminder_days, document_expiry_settings_reminder_count=document_expiry_settings_reminder_count, custom_domain_settings_domain_name=custom_domain_settings_domain_name, custom_domain_settings_from_name=custom_domain_settings_from_name)

Create the brand.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.brand_created import BrandCreated
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.BrandingApi(api_client)
    brand_name = 'brand_name_example' # str | 
    brand_logo = None # io.IOBase | 
    background_color = 'background_color_example' # str |  (optional)
    button_color = 'button_color_example' # str |  (optional)
    button_text_color = 'button_text_color_example' # str |  (optional)
    email_display_name = 'email_display_name_example' # str |  (optional)
    disclaimer_description = 'disclaimer_description_example' # str |  (optional)
    disclaimer_title = 'disclaimer_title_example' # str |  (optional)
    redirect_url = 'redirect_url_example' # str |  (optional)
    is_default = False # bool |  (optional) (default to False)
    can_hide_tag_line = False # bool |  (optional) (default to False)
    combine_audit_trail = False # bool |  (optional) (default to False)
    exclude_audit_trail_from_email = False # bool |  (optional) (default to False)
    email_signed_document = Attachment # str |  (optional) (default to Attachment)
    document_time_zone = 'document_time_zone_example' # str |  (optional)
    show_built_in_form_fields = True # bool |  (optional) (default to True)
    allow_custom_field_creation = False # bool |  (optional) (default to False)
    show_shared_custom_fields = False # bool |  (optional) (default to False)
    hide_decline = True # bool |  (optional)
    hide_save = True # bool |  (optional)
    document_expiry_settings_expiry_date_type = 'document_expiry_settings_expiry_date_type_example' # str |  (optional)
    document_expiry_settings_expiry_value = 56 # int |  (optional)
    document_expiry_settings_enable_default_expiry_alert = True # bool |  (optional)
    document_expiry_settings_enable_auto_reminder = True # bool |  (optional)
    document_expiry_settings_reminder_days = 56 # int |  (optional)
    document_expiry_settings_reminder_count = 56 # int |  (optional)
    custom_domain_settings_domain_name = 'custom_domain_settings_domain_name_example' # str |  (optional)
    custom_domain_settings_from_name = 'custom_domain_settings_from_name_example' # str |  (optional)

    try:
        # Create the brand.
        api_response = api_instance.create_brand(brand_name, brand_logo, background_color=background_color, button_color=button_color, button_text_color=button_text_color, email_display_name=email_display_name, disclaimer_description=disclaimer_description, disclaimer_title=disclaimer_title, redirect_url=redirect_url, is_default=is_default, can_hide_tag_line=can_hide_tag_line, combine_audit_trail=combine_audit_trail, exclude_audit_trail_from_email=exclude_audit_trail_from_email, email_signed_document=email_signed_document, document_time_zone=document_time_zone, show_built_in_form_fields=show_built_in_form_fields, allow_custom_field_creation=allow_custom_field_creation, show_shared_custom_fields=show_shared_custom_fields, hide_decline=hide_decline, hide_save=hide_save, document_expiry_settings_expiry_date_type=document_expiry_settings_expiry_date_type, document_expiry_settings_expiry_value=document_expiry_settings_expiry_value, document_expiry_settings_enable_default_expiry_alert=document_expiry_settings_enable_default_expiry_alert, document_expiry_settings_enable_auto_reminder=document_expiry_settings_enable_auto_reminder, document_expiry_settings_reminder_days=document_expiry_settings_reminder_days, document_expiry_settings_reminder_count=document_expiry_settings_reminder_count, custom_domain_settings_domain_name=custom_domain_settings_domain_name, custom_domain_settings_from_name=custom_domain_settings_from_name)
        print("The response of BrandingApi->create_brand:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingApi->create_brand: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_name** | **str**|  | 
 **brand_logo** | **io.IOBase**|  | 
 **background_color** | **str**|  | [optional] 
 **button_color** | **str**|  | [optional] 
 **button_text_color** | **str**|  | [optional] 
 **email_display_name** | **str**|  | [optional] 
 **disclaimer_description** | **str**|  | [optional] 
 **disclaimer_title** | **str**|  | [optional] 
 **redirect_url** | **str**|  | [optional] 
 **is_default** | **bool**|  | [optional] [default to False]
 **can_hide_tag_line** | **bool**|  | [optional] [default to False]
 **combine_audit_trail** | **bool**|  | [optional] [default to False]
 **exclude_audit_trail_from_email** | **bool**|  | [optional] [default to False]
 **email_signed_document** | **str**|  | [optional] [default to Attachment]
 **document_time_zone** | **str**|  | [optional] 
 **show_built_in_form_fields** | **bool**|  | [optional] [default to True]
 **allow_custom_field_creation** | **bool**|  | [optional] [default to False]
 **show_shared_custom_fields** | **bool**|  | [optional] [default to False]
 **hide_decline** | **bool**|  | [optional] 
 **hide_save** | **bool**|  | [optional] 
 **document_expiry_settings_expiry_date_type** | **str**|  | [optional] 
 **document_expiry_settings_expiry_value** | **int**|  | [optional] 
 **document_expiry_settings_enable_default_expiry_alert** | **bool**|  | [optional] 
 **document_expiry_settings_enable_auto_reminder** | **bool**|  | [optional] 
 **document_expiry_settings_reminder_days** | **int**|  | [optional] 
 **document_expiry_settings_reminder_count** | **int**|  | [optional] 
 **custom_domain_settings_domain_name** | **str**|  | [optional] 
 **custom_domain_settings_from_name** | **str**|  | [optional] 

### Return type

[**BrandCreated**](BrandCreated.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=minimal;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=minimal;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=minimal;IEEE754Compatible=false, application/json;odata.metadata=minimal;IEEE754Compatible=true, application/json;odata.metadata=full;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=full;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=full;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=full;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=full;IEEE754Compatible=false, application/json;odata.metadata=full;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=none;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=none;IEEE754Compatible=false, application/json;odata.metadata=none;IEEE754Compatible=true, application/json;odata.streaming=true;IEEE754Compatible=false, application/json;odata.streaming=true;IEEE754Compatible=true, application/json;odata.streaming=false;IEEE754Compatible=false, application/json;odata.streaming=false;IEEE754Compatible=true, application/json;IEEE754Compatible=false, application/json;IEEE754Compatible=true, application/xml, text/plain, application/octet-stream, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_brand**
> BrandingMessage delete_brand(brand_id)

Delete the brand.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.branding_message import BrandingMessage
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.BrandingApi(api_client)
    brand_id = 'brand_id_example' # str | brand Id.

    try:
        # Delete the brand.
        api_response = api_instance.delete_brand(brand_id)
        print("The response of BrandingApi->delete_brand:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingApi->delete_brand: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| brand Id. | 

### Return type

[**BrandingMessage**](BrandingMessage.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=minimal;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=minimal;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=minimal;IEEE754Compatible=false, application/json;odata.metadata=minimal;IEEE754Compatible=true, application/json;odata.metadata=full;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=full;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=full;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=full;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=full;IEEE754Compatible=false, application/json;odata.metadata=full;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=none;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=none;IEEE754Compatible=false, application/json;odata.metadata=none;IEEE754Compatible=true, application/json;odata.streaming=true;IEEE754Compatible=false, application/json;odata.streaming=true;IEEE754Compatible=true, application/json;odata.streaming=false;IEEE754Compatible=false, application/json;odata.streaming=false;IEEE754Compatible=true, application/json;IEEE754Compatible=false, application/json;IEEE754Compatible=true, application/xml, text/plain, application/octet-stream, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_brand**
> BrandCreated edit_brand(brand_id, brand_name=brand_name, brand_logo=brand_logo, background_color=background_color, button_color=button_color, button_text_color=button_text_color, email_display_name=email_display_name, disclaimer_description=disclaimer_description, disclaimer_title=disclaimer_title, redirect_url=redirect_url, is_default=is_default, can_hide_tag_line=can_hide_tag_line, combine_audit_trail=combine_audit_trail, exclude_audit_trail_from_email=exclude_audit_trail_from_email, email_signed_document=email_signed_document, document_time_zone=document_time_zone, show_built_in_form_fields=show_built_in_form_fields, allow_custom_field_creation=allow_custom_field_creation, show_shared_custom_fields=show_shared_custom_fields, hide_decline=hide_decline, hide_save=hide_save, document_expiry_settings_expiry_date_type=document_expiry_settings_expiry_date_type, document_expiry_settings_expiry_value=document_expiry_settings_expiry_value, document_expiry_settings_enable_default_expiry_alert=document_expiry_settings_enable_default_expiry_alert, document_expiry_settings_enable_auto_reminder=document_expiry_settings_enable_auto_reminder, document_expiry_settings_reminder_days=document_expiry_settings_reminder_days, document_expiry_settings_reminder_count=document_expiry_settings_reminder_count, custom_domain_settings_domain_name=custom_domain_settings_domain_name, custom_domain_settings_from_name=custom_domain_settings_from_name)

Edit the brand.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.brand_created import BrandCreated
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.BrandingApi(api_client)
    brand_id = 'brand_id_example' # str | The brand id.
    brand_name = 'brand_name_example' # str |  (optional)
    brand_logo = None # io.IOBase |  (optional)
    background_color = 'background_color_example' # str |  (optional)
    button_color = 'button_color_example' # str |  (optional)
    button_text_color = 'button_text_color_example' # str |  (optional)
    email_display_name = 'email_display_name_example' # str |  (optional)
    disclaimer_description = 'disclaimer_description_example' # str |  (optional)
    disclaimer_title = 'disclaimer_title_example' # str |  (optional)
    redirect_url = 'redirect_url_example' # str |  (optional)
    is_default = False # bool |  (optional) (default to False)
    can_hide_tag_line = False # bool |  (optional) (default to False)
    combine_audit_trail = False # bool |  (optional) (default to False)
    exclude_audit_trail_from_email = False # bool |  (optional) (default to False)
    email_signed_document = Attachment # str |  (optional) (default to Attachment)
    document_time_zone = 'document_time_zone_example' # str |  (optional)
    show_built_in_form_fields = True # bool |  (optional) (default to True)
    allow_custom_field_creation = False # bool |  (optional) (default to False)
    show_shared_custom_fields = False # bool |  (optional) (default to False)
    hide_decline = True # bool |  (optional)
    hide_save = True # bool |  (optional)
    document_expiry_settings_expiry_date_type = 'document_expiry_settings_expiry_date_type_example' # str |  (optional)
    document_expiry_settings_expiry_value = 56 # int |  (optional)
    document_expiry_settings_enable_default_expiry_alert = True # bool |  (optional)
    document_expiry_settings_enable_auto_reminder = True # bool |  (optional)
    document_expiry_settings_reminder_days = 56 # int |  (optional)
    document_expiry_settings_reminder_count = 56 # int |  (optional)
    custom_domain_settings_domain_name = 'custom_domain_settings_domain_name_example' # str |  (optional)
    custom_domain_settings_from_name = 'custom_domain_settings_from_name_example' # str |  (optional)

    try:
        # Edit the brand.
        api_response = api_instance.edit_brand(brand_id, brand_name=brand_name, brand_logo=brand_logo, background_color=background_color, button_color=button_color, button_text_color=button_text_color, email_display_name=email_display_name, disclaimer_description=disclaimer_description, disclaimer_title=disclaimer_title, redirect_url=redirect_url, is_default=is_default, can_hide_tag_line=can_hide_tag_line, combine_audit_trail=combine_audit_trail, exclude_audit_trail_from_email=exclude_audit_trail_from_email, email_signed_document=email_signed_document, document_time_zone=document_time_zone, show_built_in_form_fields=show_built_in_form_fields, allow_custom_field_creation=allow_custom_field_creation, show_shared_custom_fields=show_shared_custom_fields, hide_decline=hide_decline, hide_save=hide_save, document_expiry_settings_expiry_date_type=document_expiry_settings_expiry_date_type, document_expiry_settings_expiry_value=document_expiry_settings_expiry_value, document_expiry_settings_enable_default_expiry_alert=document_expiry_settings_enable_default_expiry_alert, document_expiry_settings_enable_auto_reminder=document_expiry_settings_enable_auto_reminder, document_expiry_settings_reminder_days=document_expiry_settings_reminder_days, document_expiry_settings_reminder_count=document_expiry_settings_reminder_count, custom_domain_settings_domain_name=custom_domain_settings_domain_name, custom_domain_settings_from_name=custom_domain_settings_from_name)
        print("The response of BrandingApi->edit_brand:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingApi->edit_brand: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The brand id. | 
 **brand_name** | **str**|  | [optional] 
 **brand_logo** | **io.IOBase**|  | [optional] 
 **background_color** | **str**|  | [optional] 
 **button_color** | **str**|  | [optional] 
 **button_text_color** | **str**|  | [optional] 
 **email_display_name** | **str**|  | [optional] 
 **disclaimer_description** | **str**|  | [optional] 
 **disclaimer_title** | **str**|  | [optional] 
 **redirect_url** | **str**|  | [optional] 
 **is_default** | **bool**|  | [optional] [default to False]
 **can_hide_tag_line** | **bool**|  | [optional] [default to False]
 **combine_audit_trail** | **bool**|  | [optional] [default to False]
 **exclude_audit_trail_from_email** | **bool**|  | [optional] [default to False]
 **email_signed_document** | **str**|  | [optional] [default to Attachment]
 **document_time_zone** | **str**|  | [optional] 
 **show_built_in_form_fields** | **bool**|  | [optional] [default to True]
 **allow_custom_field_creation** | **bool**|  | [optional] [default to False]
 **show_shared_custom_fields** | **bool**|  | [optional] [default to False]
 **hide_decline** | **bool**|  | [optional] 
 **hide_save** | **bool**|  | [optional] 
 **document_expiry_settings_expiry_date_type** | **str**|  | [optional] 
 **document_expiry_settings_expiry_value** | **int**|  | [optional] 
 **document_expiry_settings_enable_default_expiry_alert** | **bool**|  | [optional] 
 **document_expiry_settings_enable_auto_reminder** | **bool**|  | [optional] 
 **document_expiry_settings_reminder_days** | **int**|  | [optional] 
 **document_expiry_settings_reminder_count** | **int**|  | [optional] 
 **custom_domain_settings_domain_name** | **str**|  | [optional] 
 **custom_domain_settings_from_name** | **str**|  | [optional] 

### Return type

[**BrandCreated**](BrandCreated.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=minimal;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=minimal;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=minimal;IEEE754Compatible=false, application/json;odata.metadata=minimal;IEEE754Compatible=true, application/json;odata.metadata=full;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=full;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=full;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=full;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=full;IEEE754Compatible=false, application/json;odata.metadata=full;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=none;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=none;IEEE754Compatible=false, application/json;odata.metadata=none;IEEE754Compatible=true, application/json;odata.streaming=true;IEEE754Compatible=false, application/json;odata.streaming=true;IEEE754Compatible=true, application/json;odata.streaming=false;IEEE754Compatible=false, application/json;odata.streaming=false;IEEE754Compatible=true, application/json;IEEE754Compatible=false, application/json;IEEE754Compatible=true, application/xml, text/plain, application/octet-stream, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_brand**
> ViewBrandDetails get_brand(brand_id)

Get the specific brand details.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.view_brand_details import ViewBrandDetails
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.BrandingApi(api_client)
    brand_id = 'brand_id_example' # str | The brand id.

    try:
        # Get the specific brand details.
        api_response = api_instance.get_brand(brand_id)
        print("The response of BrandingApi->get_brand:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingApi->get_brand: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The brand id. | 

### Return type

[**ViewBrandDetails**](ViewBrandDetails.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_default_brand**
> BrandingMessage reset_default_brand(brand_id)

Reset default brand.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.branding_message import BrandingMessage
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.BrandingApi(api_client)
    brand_id = 'brand_id_example' # str | brand Id.

    try:
        # Reset default brand.
        api_response = api_instance.reset_default_brand(brand_id)
        print("The response of BrandingApi->reset_default_brand:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingApi->reset_default_brand: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| brand Id. | 

### Return type

[**BrandingMessage**](BrandingMessage.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=minimal;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=minimal;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=minimal;IEEE754Compatible=false, application/json;odata.metadata=minimal;IEEE754Compatible=true, application/json;odata.metadata=full;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=full;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=full;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=full;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=full;IEEE754Compatible=false, application/json;odata.metadata=full;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=none;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=none;IEEE754Compatible=false, application/json;odata.metadata=none;IEEE754Compatible=true, application/json;odata.streaming=true;IEEE754Compatible=false, application/json;odata.streaming=true;IEEE754Compatible=true, application/json;odata.streaming=false;IEEE754Compatible=false, application/json;odata.streaming=false;IEEE754Compatible=true, application/json;IEEE754Compatible=false, application/json;IEEE754Compatible=true, application/xml, text/plain, application/octet-stream, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

