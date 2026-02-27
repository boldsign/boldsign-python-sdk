# boldsign.GroupContactsApi

All URIs are relative to *https://api.boldsign.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group_contact**](GroupContactsApi.md#create_group_contact) | **POST** /v1/contactGroups/create | Create a new Group Contact.
[**delete_group_contact**](GroupContactsApi.md#delete_group_contact) | **DELETE** /v1/contactGroups/delete | Deletes a Group Contact.
[**get_group_contact**](GroupContactsApi.md#get_group_contact) | **GET** /v1/contactGroups/get | Get Summary of the Group Contact.
[**group_contact_list**](GroupContactsApi.md#group_contact_list) | **GET** /v1/contactGroups/list | List Group Contacts.
[**update_group_contact**](GroupContactsApi.md#update_group_contact) | **PUT** /v1/contactGroups/update | Update the Group Contact.


# **create_group_contact**
> CreateGroupContactResponse create_group_contact(group_contact_details=group_contact_details)

Create a new Group Contact.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.create_group_contact_response import CreateGroupContactResponse
from boldsign.models.group_contact_details import GroupContactDetails
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.GroupContactsApi(api_client)
    group_contact_details = boldsign.GroupContactDetails() # GroupContactDetails | The group contact details. (optional)

    try:
        # Create a new Group Contact.
        api_response = api_instance.create_group_contact(group_contact_details=group_contact_details)
        print("The response of GroupContactsApi->create_group_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupContactsApi->create_group_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_contact_details** | [**GroupContactDetails**](GroupContactDetails.md)| The group contact details. | [optional] 

### Return type

[**CreateGroupContactResponse**](CreateGroupContactResponse.md)

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

# **delete_group_contact**
> delete_group_contact(group_id)

Deletes a Group Contact.

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
    api_instance = boldsign.GroupContactsApi(api_client)
    group_id = 'group_id_example' # str | The group contact id.

    try:
        # Deletes a Group Contact.
        api_instance.delete_group_contact(group_id)
    except Exception as e:
        print("Exception when calling GroupContactsApi->delete_group_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group contact id. | 

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

# **get_group_contact**
> GetGroupContactDetails get_group_contact(group_id)

Get Summary of the Group Contact.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.get_group_contact_details import GetGroupContactDetails
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.GroupContactsApi(api_client)
    group_id = 'group_id_example' # str | Group Contact Id.

    try:
        # Get Summary of the Group Contact.
        api_response = api_instance.get_group_contact(group_id)
        print("The response of GroupContactsApi->get_group_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupContactsApi->get_group_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Group Contact Id. | 

### Return type

[**GetGroupContactDetails**](GetGroupContactDetails.md)

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

# **group_contact_list**
> GroupContactsList group_contact_list(page, page_size=page_size, search_key=search_key, contact_type=contact_type, directories=directories)

List Group Contacts.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.group_contacts_list import GroupContactsList
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.GroupContactsApi(api_client)
    page = 1 # int | Page index specified in get user group contact list request. Default value is 1. (default to 1)
    page_size = 10 # int | Page size specified in get user group contact list request. Default value is 10. (optional) (default to 10)
    search_key = 'search_key_example' # str | Group Contacts can be listed by the search  based on the Name or Email (optional)
    contact_type = 'contact_type_example' # str | Group Contact type whether the contact is my contacts or all contacts. Default value is AllContacts. (optional)
    directories = ['directories_example'] # List[str] | Group Contacts can be listed by the search  based on the directories (optional)

    try:
        # List Group Contacts.
        api_response = api_instance.group_contact_list(page, page_size=page_size, search_key=search_key, contact_type=contact_type, directories=directories)
        print("The response of GroupContactsApi->group_contact_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupContactsApi->group_contact_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page index specified in get user group contact list request. Default value is 1. | [default to 1]
 **page_size** | **int**| Page size specified in get user group contact list request. Default value is 10. | [optional] [default to 10]
 **search_key** | **str**| Group Contacts can be listed by the search  based on the Name or Email | [optional] 
 **contact_type** | **str**| Group Contact type whether the contact is my contacts or all contacts. Default value is AllContacts. | [optional] 
 **directories** | [**List[str]**](str.md)| Group Contacts can be listed by the search  based on the directories | [optional] 

### Return type

[**GroupContactsList**](GroupContactsList.md)

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

# **update_group_contact**
> update_group_contact(group_id, update_group_contact)

Update the Group Contact.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.update_group_contact import UpdateGroupContact
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.GroupContactsApi(api_client)
    group_id = 'group_id_example' # str | The group contact ID.
    update_group_contact = boldsign.UpdateGroupContact() # UpdateGroupContact | The group contact details.

    try:
        # Update the Group Contact.
        api_instance.update_group_contact(group_id, update_group_contact)
    except Exception as e:
        print("Exception when calling GroupContactsApi->update_group_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group contact ID. | 
 **update_group_contact** | [**UpdateGroupContact**](UpdateGroupContact.md)| The group contact details. | 

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

