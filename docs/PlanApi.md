# boldsign.PlanApi

All URIs are relative to *https://api.boldsign.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_credits_count**](PlanApi.md#api_credits_count) | **GET** /v1/plan/apiCreditsCount | Gets the Api credits details.


# **api_credits_count**
> BillingViewModel api_credits_count()

Gets the Api credits details.

### Example

* Api Key Authentication (X-API-KEY):
* Api Key Authentication (Bearer):

```python
import boldsign
from boldsign.models.billing_view_model import BillingViewModel
from boldsign.rest import ApiException
from pprint import pprint

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boldsign.PlanApi(api_client)

    try:
        # Gets the Api credits details.
        api_response = api_instance.api_credits_count()
        print("The response of PlanApi->api_credits_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanApi->api_credits_count: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BillingViewModel**](BillingViewModel.md)

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

