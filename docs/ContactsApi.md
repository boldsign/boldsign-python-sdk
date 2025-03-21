# boldsign.ContactsApi

All URIs are relative to *https://api.boldsign.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contact_user_list**](ContactsApi.md#contact_user_list) | **GET** /v1/contacts/list | List Contact document.
[**create_contact**](ContactsApi.md#create_contact) | **POST** /v1/contacts/create | Create the new Contact.
[**delete_contacts**](ContactsApi.md#delete_contacts) | **DELETE** /v1/contacts/delete | Deletes a contact.
[**get_contact**](ContactsApi.md#get_contact) | **GET** /v1/contacts/get | Get summary of the contact.
[**update_contact**](ContactsApi.md#update_contact) | **PUT** /v1/contacts/update | Update the contact.


# **contact_user_list**
> ContactsList contact_user_list(page, page_size=page_size, search_key=search_key, contact_type=contact_type)

List Contact document.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.contacts_list import ContactsList
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.ContactsApi(api_client)
    page = 1 # int | Page index specified in get user contact list request. Default value is 1. (default to 1)
    page_size = 10 # int | Page size specified in get user contact list request. Default value is 10. (optional) (default to 10)
    search_key = 'search_key_example' # str | Contacts can be listed by the search  based on the Name or Email (optional)
    contact_type = 'contact_type_example' # str | Contact type whether the contact is My Contacts or All Contacts. Default value is AllContacts. (optional)

    try:
        # List Contact document.
        api_response = api_instance.contact_user_list(page, page_size=page_size, search_key=search_key, contact_type=contact_type)
        print("The response of ContactsApi->contact_user_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->contact_user_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page index specified in get user contact list request. Default value is 1. | [default to 1]
 **page_size** | **int**| Page size specified in get user contact list request. Default value is 10. | [optional] [default to 10]
 **search_key** | **str**| Contacts can be listed by the search  based on the Name or Email | [optional] 
 **contact_type** | **str**| Contact type whether the contact is My Contacts or All Contacts. Default value is AllContacts. | [optional] 

### Return type

[**ContactsList**](ContactsList.md)

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

# **create_contact**
> CreateContactResponse create_contact(contact_details=contact_details)

Create the new Contact.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.contact_details import ContactDetails
from boldsign.models.create_contact_response import CreateContactResponse
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.ContactsApi(api_client)
    contact_details = [boldsign.ContactDetails()] # List[ContactDetails] | The contact details. (optional)

    try:
        # Create the new Contact.
        api_response = api_instance.create_contact(contact_details=contact_details)
        print("The response of ContactsApi->create_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->create_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_details** | [**List[ContactDetails]**](ContactDetails.md)| The contact details. | [optional] 

### Return type

[**CreateContactResponse**](CreateContactResponse.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=minimal;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=minimal;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=minimal;IEEE754Compatible=false, application/json;odata.metadata=minimal;IEEE754Compatible=true, application/json;odata.metadata=full;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=full;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=full;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=full;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=full;IEEE754Compatible=false, application/json;odata.metadata=full;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=true;IEEE754Compatible=false, application/json;odata.metadata=none;odata.streaming=true;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=false;IEEE754Compatible=true, application/json;odata.metadata=none;odata.streaming=false;IEEE754Compatible=false, application/json;odata.metadata=none;IEEE754Compatible=false, application/json;odata.metadata=none;IEEE754Compatible=true, application/json;odata.streaming=true;IEEE754Compatible=false, application/json;odata.streaming=true;IEEE754Compatible=true, application/json;odata.streaming=false;IEEE754Compatible=false, application/json;odata.streaming=false;IEEE754Compatible=true, application/json;IEEE754Compatible=false, application/json;IEEE754Compatible=true, application/xml, text/plain, application/json-patch+json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contacts**
> delete_contacts(id)

Deletes a contact.

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
    api_instance = boldsign.ContactsApi(api_client)
    id = 'id_example' # str | The contact id.

    try:
        # Deletes a contact.
        api_instance.delete_contacts(id)
    except Exception as e:
        print("Exception when calling ContactsApi->delete_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The contact id. | 

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

# **get_contact**
> ContactsDetails get_contact(id)

Get summary of the contact.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.contacts_details import ContactsDetails
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.ContactsApi(api_client)
    id = 'id_example' # str | Contact Id.

    try:
        # Get summary of the contact.
        api_response = api_instance.get_contact(id)
        print("The response of ContactsApi->get_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Contact Id. | 

### Return type

[**ContactsDetails**](ContactsDetails.md)

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

# **update_contact**
> update_contact(id=id, contact_details=contact_details)

Update the contact.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.contact_details import ContactDetails
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.ContactsApi(api_client)
    id = 'id_example' # str | The contactId. (optional)
    contact_details = boldsign.ContactDetails() # ContactDetails | The contact details. (optional)

    try:
        # Update the contact.
        api_instance.update_contact(id=id, contact_details=contact_details)
    except Exception as e:
        print("Exception when calling ContactsApi->update_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The contactId. | [optional] 
 **contact_details** | [**ContactDetails**](ContactDetails.md)| The contact details. | [optional] 

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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

