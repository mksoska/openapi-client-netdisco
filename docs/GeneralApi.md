# openapi_netdisco.GeneralApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_post**](GeneralApi.md#login_post) | **POST** /login | 
[**logout_get**](GeneralApi.md#logout_get) | **GET** /logout | 


# **login_post**
> ApiKey login_post()



Obtain an API Key

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import openapi_netdisco
from openapi_netdisco.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_netdisco.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_netdisco.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_netdisco.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_netdisco.GeneralApi(api_client)
    
    try:
        api_response = api_instance.login_post()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GeneralApi->login_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_get**
> logout_get()



Destroy user API Key and session cookie

### Example

* Api Key Authentication (APIKeyHeader):
```python
from __future__ import print_function
import time
import openapi_netdisco
from openapi_netdisco.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_netdisco.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_netdisco.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_netdisco.GeneralApi(api_client)
    
    try:
        api_instance.logout_get()
    except ApiException as e:
        print("Exception when calling GeneralApi->logout_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

