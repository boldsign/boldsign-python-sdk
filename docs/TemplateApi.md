# boldsign.TemplateApi

All URIs are relative to *https://api.boldsign.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_tag**](TemplateApi.md#add_tag) | **PATCH** /v1/template/addTags | Add the Tags in Templates.
[**create_embedded_preview_url**](TemplateApi.md#create_embedded_preview_url) | **POST** /v1/template/createEmbeddedPreviewUrl | Generates a preview URL for a template to view it.
[**create_embedded_request_url_template**](TemplateApi.md#create_embedded_request_url_template) | **POST** /v1/template/createEmbeddedRequestUrl | Generates a send URL using a template which embeds document sending process into your application.
[**create_embedded_template_url**](TemplateApi.md#create_embedded_template_url) | **POST** /v1/template/createEmbeddedTemplateUrl | Generates a create URL to embeds template create process into your application.
[**create_template**](TemplateApi.md#create_template) | **POST** /v1/template/create | Creates a new template.
[**delete_template**](TemplateApi.md#delete_template) | **DELETE** /v1/template/delete | Deletes a template.
[**delete_tag**](TemplateApi.md#delete_tag) | **DELETE** /v1/template/deleteTags | Delete the Tags in Templates.
[**download**](TemplateApi.md#download) | **GET** /v1/template/download | Download the template.
[**edit_template**](TemplateApi.md#edit_template) | **PUT** /v1/template/edit | Edit and updates an existing template.
[**get_embedded_template_edit_url**](TemplateApi.md#get_embedded_template_edit_url) | **POST** /v1/template/getEmbeddedTemplateEditUrl | Generates a edit URL to embeds template edit process into your application.
[**get_properties**](TemplateApi.md#get_properties) | **GET** /v1/template/properties | Get summary of the template.
[**list_templates**](TemplateApi.md#list_templates) | **GET** /v1/template/list | List all the templates.
[**merge_and_send**](TemplateApi.md#merge_and_send) | **POST** /v1/template/mergeAndSend | Send the document by merging multiple templates.
[**merge_create_embedded_request_url_template**](TemplateApi.md#merge_create_embedded_request_url_template) | **POST** /v1/template/mergeCreateEmbeddedRequestUrl | Generates a merge request URL using a template that combines document merging and sending processes into your application.
[**send_using_template**](TemplateApi.md#send_using_template) | **POST** /v1/template/send | Send a document for signature using a Template.


# **add_tag**
> add_tag(template_tag=template_tag)

Add the Tags in Templates.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.template_tag import TemplateTag
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.TemplateApi(api_client)
    template_tag = boldsign.TemplateTag() # TemplateTag | ContainsTemplateId and Label Names for AddingTags. (optional)

    try:
        # Add the Tags in Templates.
        api_instance.add_tag(template_tag=template_tag)
    except Exception as e:
        print("Exception when calling TemplateApi->add_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_tag** | [**TemplateTag**](TemplateTag.md)| ContainsTemplateId and Label Names for AddingTags. | [optional] 

### Return type

void (empty response body)

### Authorization

[X-API-KEY](../README.md#X-API-KEY), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=minimal;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=minimal;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=minimal;IEEE754Compatible=false, application/json;odata.metadata=minimal;IEEE754Compatible=true, application/json;odata.metadata=full;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=full;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=full;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=full;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=full;IEEE754Compatible=false, application/json;odata.metadata=full;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=none;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=none;IEEE754Compatible=false, application/json;odata.metadata=none;IEEE754Compatible=true, application/json;odata.streaming=true;IEEE754Compatible=false, application/json;odata.streaming=true;IEEE754Compatible=true, application/json;odata.streaming=false;IEEE754Compatible=false, application/json;odata.streaming=false;IEEE754Compatible=true, application/json;IEEE754Compatible=false, application/json;IEEE754Compatible=true, application/xml, text/plain, application/json-patch+json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=minimal;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=minimal;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=minimal;IEEE754Compatible=false, application/json;odata.metadata=minimal;IEEE754Compatible=true, application/json;odata.metadata=full;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=full;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=full;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=full;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=full;IEEE754Compatible=false, application/json;odata.metadata=full;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=none;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=none;IEEE754Compatible=false, application/json;odata.metadata=none;IEEE754Compatible=true, application/json;odata.streaming=true;IEEE754Compatible=false, application/json;odata.streaming=true;IEEE754Compatible=true, application/json;odata.streaming=false;IEEE754Compatible=false, application/json;odata.streaming=false;IEEE754Compatible=true, application/json;IEEE754Compatible=false, application/json;IEEE754Compatible=true, application/xml, text/plain, application/octet-stream, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_embedded_preview_url**
> EmbeddedTemplatePreview create_embedded_preview_url(template_id, embedded_template_preview_json_request=embedded_template_preview_json_request)

Generates a preview URL for a template to view it.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.embedded_template_preview import EmbeddedTemplatePreview
from boldsign.models.embedded_template_preview_json_request import EmbeddedTemplatePreviewJsonRequest
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.TemplateApi(api_client)
    template_id = 'template_id_example' # str | The template id.
    embedded_template_preview_json_request = boldsign.EmbeddedTemplatePreviewJsonRequest() # EmbeddedTemplatePreviewJsonRequest | The embedded template preview request body. (optional)

    try:
        # Generates a preview URL for a template to view it.
        api_response = api_instance.create_embedded_preview_url(template_id, embedded_template_preview_json_request=embedded_template_preview_json_request)
        print("The response of TemplateApi->create_embedded_preview_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->create_embedded_preview_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template id. | 
 **embedded_template_preview_json_request** | [**EmbeddedTemplatePreviewJsonRequest**](EmbeddedTemplatePreviewJsonRequest.md)| The embedded template preview request body. | [optional] 

### Return type

[**EmbeddedTemplatePreview**](EmbeddedTemplatePreview.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_embedded_request_url_template**
> EmbeddedSendCreated create_embedded_request_url_template(template_id, embedded_send_template_form_request=embedded_send_template_form_request)

Generates a send URL using a template which embeds document sending process into your application.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.embedded_send_created import EmbeddedSendCreated
from boldsign.models.embedded_send_template_form_request import EmbeddedSendTemplateFormRequest
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.TemplateApi(api_client)
    template_id = 'template_id_example' # str | The template id.
    embedded_send_template_form_request = boldsign.EmbeddedSendTemplateFormRequest() # EmbeddedSendTemplateFormRequest | Embedded send template json request. (optional)

    try:
        # Generates a send URL using a template which embeds document sending process into your application.
        api_response = api_instance.create_embedded_request_url_template(template_id, embedded_send_template_form_request=embedded_send_template_form_request)
        print("The response of TemplateApi->create_embedded_request_url_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->create_embedded_request_url_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template id. | 
 **embedded_send_template_form_request** | [**EmbeddedSendTemplateFormRequest**](EmbeddedSendTemplateFormRequest.md)| Embedded send template json request. | [optional] 

### Return type

[**EmbeddedSendCreated**](EmbeddedSendCreated.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**422** | Unprocessable Content |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_embedded_template_url**
> EmbeddedTemplateCreated create_embedded_template_url(embedded_create_template_request=embedded_create_template_request)

Generates a create URL to embeds template create process into your application.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.embedded_create_template_request import EmbeddedCreateTemplateRequest
from boldsign.models.embedded_template_created import EmbeddedTemplateCreated
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.TemplateApi(api_client)
    embedded_create_template_request = boldsign.EmbeddedCreateTemplateRequest() # EmbeddedCreateTemplateRequest | The create embedded template request body. (optional)

    try:
        # Generates a create URL to embeds template create process into your application.
        api_response = api_instance.create_embedded_template_url(embedded_create_template_request=embedded_create_template_request)
        print("The response of TemplateApi->create_embedded_template_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->create_embedded_template_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **embedded_create_template_request** | [**EmbeddedCreateTemplateRequest**](EmbeddedCreateTemplateRequest.md)| The create embedded template request body. | [optional] 

### Return type

[**EmbeddedTemplateCreated**](EmbeddedTemplateCreated.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template**
> TemplateCreated create_template(create_template_request=create_template_request)

Creates a new template.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.create_template_request import CreateTemplateRequest
from boldsign.models.template_created import TemplateCreated
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.TemplateApi(api_client)
    create_template_request = boldsign.CreateTemplateRequest() # CreateTemplateRequest | The create template request body. (optional)

    try:
        # Creates a new template.
        api_response = api_instance.create_template(create_template_request=create_template_request)
        print("The response of TemplateApi->create_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->create_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_template_request** | [**CreateTemplateRequest**](CreateTemplateRequest.md)| The create template request body. | [optional] 

### Return type

[**TemplateCreated**](TemplateCreated.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template**
> delete_template(template_id, on_behalf_of=on_behalf_of)

Deletes a template.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.TemplateApi(api_client)
    template_id = 'template_id_example' # str | The template id.
    on_behalf_of = 'on_behalf_of_example' # str | The on behalfof email address. (optional)

    try:
        # Deletes a template.
        api_instance.delete_template(template_id, on_behalf_of=on_behalf_of)
    except Exception as e:
        print("Exception when calling TemplateApi->delete_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template id. | 
 **on_behalf_of** | **str**| The on behalfof email address. | [optional] 

### Return type

void (empty response body)

### Authorization

[X-API-KEY](../README.md#X-API-KEY), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> delete_tag(template_tag=template_tag)

Delete the Tags in Templates.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.template_tag import TemplateTag
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.TemplateApi(api_client)
    template_tag = boldsign.TemplateTag() # TemplateTag | Contains TemplateId and LabelNames for Adding Tags. (optional)

    try:
        # Delete the Tags in Templates.
        api_instance.delete_tag(template_tag=template_tag)
    except Exception as e:
        print("Exception when calling TemplateApi->delete_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_tag** | [**TemplateTag**](TemplateTag.md)| Contains TemplateId and LabelNames for Adding Tags. | [optional] 

### Return type

void (empty response body)

### Authorization

[X-API-KEY](../README.md#X-API-KEY), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=minimal;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=minimal;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=minimal;IEEE754Compatible=false, application/json;odata.metadata=minimal;IEEE754Compatible=true, application/json;odata.metadata=full;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=full;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=full;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=full;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=full;IEEE754Compatible=false, application/json;odata.metadata=full;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=none;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=none;IEEE754Compatible=false, application/json;odata.metadata=none;IEEE754Compatible=true, application/json;odata.streaming=true;IEEE754Compatible=false, application/json;odata.streaming=true;IEEE754Compatible=true, application/json;odata.streaming=false;IEEE754Compatible=false, application/json;odata.streaming=false;IEEE754Compatible=true, application/json;IEEE754Compatible=false, application/json;IEEE754Compatible=true, application/xml, text/plain, application/json-patch+json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=minimal;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=minimal;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=minimal;IEEE754Compatible=false, application/json;odata.metadata=minimal;IEEE754Compatible=true, application/json;odata.metadata=full;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=full;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=full;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=full;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=full;IEEE754Compatible=false, application/json;odata.metadata=full;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=none;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=none;IEEE754Compatible=false, application/json;odata.metadata=none;IEEE754Compatible=true, application/json;odata.streaming=true;IEEE754Compatible=false, application/json;odata.streaming=true;IEEE754Compatible=true, application/json;odata.streaming=false;IEEE754Compatible=false, application/json;odata.streaming=false;IEEE754Compatible=true, application/json;IEEE754Compatible=false, application/json;IEEE754Compatible=true, application/xml, text/plain, application/octet-stream, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download**
> io.IOBase download(template_id, on_behalf_of=on_behalf_of, include_form_field_values=include_form_field_values)

Download the template.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.TemplateApi(api_client)
    template_id = 'template_id_example' # str | Template Id.
    on_behalf_of = 'on_behalf_of_example' # str | The on behalfof email address. (optional)
    include_form_field_values = False # bool | Include form field data. (optional) (default to False)

    try:
        # Download the template.
        api_response = api_instance.download(template_id, on_behalf_of=on_behalf_of, include_form_field_values=include_form_field_values)
        print("The response of TemplateApi->download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Template Id. | 
 **on_behalf_of** | **str**| The on behalfof email address. | [optional] 
 **include_form_field_values** | **bool**| Include form field data. | [optional] [default to False]

### Return type

**io.IOBase**

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
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_template**
> edit_template(template_id, edit_template_request)

Edit and updates an existing template.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.edit_template_request import EditTemplateRequest
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.TemplateApi(api_client)
    template_id = 'template_id_example' # str | The template id.
    edit_template_request = boldsign.EditTemplateRequest() # EditTemplateRequest | The edit template request body.

    try:
        # Edit and updates an existing template.
        api_instance.edit_template(template_id, edit_template_request)
    except Exception as e:
        print("Exception when calling TemplateApi->edit_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template id. | 
 **edit_template_request** | [**EditTemplateRequest**](EditTemplateRequest.md)| The edit template request body. | 

### Return type

void (empty response body)

### Authorization

[X-API-KEY](../README.md#X-API-KEY), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=minimal;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=minimal;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=minimal;IEEE754Compatible=false, application/json;odata.metadata=minimal;IEEE754Compatible=true, application/json;odata.metadata=full;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=full;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=full;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=full;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=full;IEEE754Compatible=false, application/json;odata.metadata=full;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=none;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=none;IEEE754Compatible=false, application/json;odata.metadata=none;IEEE754Compatible=true, application/json;odata.streaming=true;IEEE754Compatible=false, application/json;odata.streaming=true;IEEE754Compatible=true, application/json;odata.streaming=false;IEEE754Compatible=false, application/json;odata.streaming=false;IEEE754Compatible=true, application/json;IEEE754Compatible=false, application/json;IEEE754Compatible=true, application/xml, text/plain, application/json-patch+json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**422** | Unprocessable Content |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_embedded_template_edit_url**
> EmbeddedTemplateEdited get_embedded_template_edit_url(template_id, embedded_template_edit_request=embedded_template_edit_request)

Generates a edit URL to embeds template edit process into your application.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.embedded_template_edit_request import EmbeddedTemplateEditRequest
from boldsign.models.embedded_template_edited import EmbeddedTemplateEdited
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.TemplateApi(api_client)
    template_id = 'template_id_example' # str | The template id.
    embedded_template_edit_request = boldsign.EmbeddedTemplateEditRequest() # EmbeddedTemplateEditRequest | The embedded edit template request body. (optional)

    try:
        # Generates a edit URL to embeds template edit process into your application.
        api_response = api_instance.get_embedded_template_edit_url(template_id, embedded_template_edit_request=embedded_template_edit_request)
        print("The response of TemplateApi->get_embedded_template_edit_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->get_embedded_template_edit_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template id. | 
 **embedded_template_edit_request** | [**EmbeddedTemplateEditRequest**](EmbeddedTemplateEditRequest.md)| The embedded edit template request body. | [optional] 

### Return type

[**EmbeddedTemplateEdited**](EmbeddedTemplateEdited.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_properties**
> TemplateProperties get_properties(template_id)

Get summary of the template.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.template_properties import TemplateProperties
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.TemplateApi(api_client)
    template_id = 'template_id_example' # str | Template Id.

    try:
        # Get summary of the template.
        api_response = api_instance.get_properties(template_id)
        print("The response of TemplateApi->get_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->get_properties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Template Id. | 

### Return type

[**TemplateProperties**](TemplateProperties.md)

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

# **list_templates**
> TemplateRecords list_templates(page, template_type=template_type, page_size=page_size, search_key=search_key, on_behalf_of=on_behalf_of, created_by=created_by, template_labels=template_labels, start_date=start_date, end_date=end_date, brand_ids=brand_ids, shared_with_team_id=shared_with_team_id)

List all the templates.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.template_records import TemplateRecords
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.TemplateApi(api_client)
    page = 1 # int |  (default to 1)
    template_type = 'template_type_example' # str |  (optional)
    page_size = 10 # int |  (optional) (default to 10)
    search_key = 'search_key_example' # str |  (optional)
    on_behalf_of = ['on_behalf_of_example'] # List[str] | The sender identity's email used to filter the templates returned in the API. The API will return templates that were sent on behalf of the specified email address. (optional)
    created_by = ['created_by_example'] # List[str] | The templates can be listed by the creator of the template. (optional)
    template_labels = ['template_labels_example'] # List[str] | Labels of the template. (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date of the template (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | End date of the template (optional)
    brand_ids = ['brand_ids_example'] # List[str] | BrandId(s) of the template. (optional)
    shared_with_team_id = ['shared_with_team_id_example'] # List[str] | The templates can be listed by the shared teams. (optional)

    try:
        # List all the templates.
        api_response = api_instance.list_templates(page, template_type=template_type, page_size=page_size, search_key=search_key, on_behalf_of=on_behalf_of, created_by=created_by, template_labels=template_labels, start_date=start_date, end_date=end_date, brand_ids=brand_ids, shared_with_team_id=shared_with_team_id)
        print("The response of TemplateApi->list_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->list_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [default to 1]
 **template_type** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] [default to 10]
 **search_key** | **str**|  | [optional] 
 **on_behalf_of** | [**List[str]**](str.md)| The sender identity&#39;s email used to filter the templates returned in the API. The API will return templates that were sent on behalf of the specified email address. | [optional] 
 **created_by** | [**List[str]**](str.md)| The templates can be listed by the creator of the template. | [optional] 
 **template_labels** | [**List[str]**](str.md)| Labels of the template. | [optional] 
 **start_date** | **datetime**| Start date of the template | [optional] 
 **end_date** | **datetime**| End date of the template | [optional] 
 **brand_ids** | [**List[str]**](str.md)| BrandId(s) of the template. | [optional] 
 **shared_with_team_id** | [**List[str]**](str.md)| The templates can be listed by the shared teams. | [optional] 

### Return type

[**TemplateRecords**](TemplateRecords.md)

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

# **merge_and_send**
> DocumentCreated merge_and_send(merge_and_send_for_sign_form=merge_and_send_for_sign_form)

Send the document by merging multiple templates.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.document_created import DocumentCreated
from boldsign.models.merge_and_send_for_sign_form import MergeAndSendForSignForm
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.TemplateApi(api_client)
    merge_and_send_for_sign_form = boldsign.MergeAndSendForSignForm() # MergeAndSendForSignForm | The merge and send details as JSON. (optional)

    try:
        # Send the document by merging multiple templates.
        api_response = api_instance.merge_and_send(merge_and_send_for_sign_form=merge_and_send_for_sign_form)
        print("The response of TemplateApi->merge_and_send:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->merge_and_send: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merge_and_send_for_sign_form** | [**MergeAndSendForSignForm**](MergeAndSendForSignForm.md)| The merge and send details as JSON. | [optional] 

### Return type

[**DocumentCreated**](DocumentCreated.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**422** | Unprocessable Content |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_create_embedded_request_url_template**
> EmbeddedSendCreated merge_create_embedded_request_url_template(embedded_merge_template_form_request=embedded_merge_template_form_request)

Generates a merge request URL using a template that combines document merging and sending processes into your application.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.embedded_merge_template_form_request import EmbeddedMergeTemplateFormRequest
from boldsign.models.embedded_send_created import EmbeddedSendCreated
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.TemplateApi(api_client)
    embedded_merge_template_form_request = boldsign.EmbeddedMergeTemplateFormRequest() # EmbeddedMergeTemplateFormRequest | Embedded merge and send template json request. (optional)

    try:
        # Generates a merge request URL using a template that combines document merging and sending processes into your application.
        api_response = api_instance.merge_create_embedded_request_url_template(embedded_merge_template_form_request=embedded_merge_template_form_request)
        print("The response of TemplateApi->merge_create_embedded_request_url_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->merge_create_embedded_request_url_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **embedded_merge_template_form_request** | [**EmbeddedMergeTemplateFormRequest**](EmbeddedMergeTemplateFormRequest.md)| Embedded merge and send template json request. | [optional] 

### Return type

[**EmbeddedSendCreated**](EmbeddedSendCreated.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**422** | Unprocessable Content |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_using_template**
> DocumentCreated send_using_template(template_id, send_for_sign_from_template_form=send_for_sign_from_template_form)

Send a document for signature using a Template.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.document_created import DocumentCreated
from boldsign.models.send_for_sign_from_template_form import SendForSignFromTemplateForm
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.TemplateApi(api_client)
    template_id = 'template_id_example' # str | The template id.
    send_for_sign_from_template_form = boldsign.SendForSignFromTemplateForm() # SendForSignFromTemplateForm | The send template details as JSON. (optional)

    try:
        # Send a document for signature using a Template.
        api_response = api_instance.send_using_template(template_id, send_for_sign_from_template_form=send_for_sign_from_template_form)
        print("The response of TemplateApi->send_using_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->send_using_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template id. | 
 **send_for_sign_from_template_form** | [**SendForSignFromTemplateForm**](SendForSignFromTemplateForm.md)| The send template details as JSON. | [optional] 

### Return type

[**DocumentCreated**](DocumentCreated.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

