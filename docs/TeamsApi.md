# boldsign.TeamsApi

All URIs are relative to *https://api.boldsign.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_team**](TeamsApi.md#create_team) | **POST** /v1/teams/create | Create Team.
[**get_team**](TeamsApi.md#get_team) | **GET** /v1/teams/get | Get Team details.
[**list_teams**](TeamsApi.md#list_teams) | **GET** /v1/teams/list | List Teams.
[**update_team**](TeamsApi.md#update_team) | **PUT** /v1/teams/update | Update Team.


# **create_team**
> TeamCreated create_team(create_team_request)

Create Team.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.create_team_request import CreateTeamRequest
from boldsign.models.team_created import TeamCreated
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.TeamsApi(api_client)
    create_team_request = boldsign.CreateTeamRequest() # CreateTeamRequest | team creation.

    try:
        # Create Team.
        api_response = api_instance.create_team(create_team_request)
        print("The response of TeamsApi->create_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->create_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_team_request** | [**CreateTeamRequest**](CreateTeamRequest.md)| team creation. | 

### Return type

[**TeamCreated**](TeamCreated.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team**
> TeamResponse get_team(team_id)

Get Team details.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.team_response import TeamResponse
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.TeamsApi(api_client)
    team_id = 'team_id_example' # str | Team Id.

    try:
        # Get Team details.
        api_response = api_instance.get_team(team_id)
        print("The response of TeamsApi->get_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| Team Id. | 

### Return type

[**TeamResponse**](TeamResponse.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_teams**
> TeamListResponse list_teams(page, page_size=page_size, search_key=search_key)

List Teams.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.team_list_response import TeamListResponse
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.TeamsApi(api_client)
    page = 1 # int | Page index specified in get team list request. (default to 1)
    page_size = 10 # int | Page size specified in get team list request. (optional) (default to 10)
    search_key = 'search_key_example' # str | Teams can be listed by the search key (optional)

    try:
        # List Teams.
        api_response = api_instance.list_teams(page, page_size=page_size, search_key=search_key)
        print("The response of TeamsApi->list_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->list_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page index specified in get team list request. | [default to 1]
 **page_size** | **int**| Page size specified in get team list request. | [optional] [default to 10]
 **search_key** | **str**| Teams can be listed by the search key | [optional] 

### Return type

[**TeamListResponse**](TeamListResponse.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team**
> update_team(team_update_request)

Update Team.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.team_update_request import TeamUpdateRequest
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.TeamsApi(api_client)
    team_update_request = boldsign.TeamUpdateRequest() # TeamUpdateRequest | update team.

    try:
        # Update Team.
        api_instance.update_team(team_update_request)
    except Exception as e:
        print("Exception when calling TeamsApi->update_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_update_request** | [**TeamUpdateRequest**](TeamUpdateRequest.md)| update team. | 

### Return type

void (empty response body)

### Authorization

[X-API-KEY](../README.md#X-API-KEY), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

