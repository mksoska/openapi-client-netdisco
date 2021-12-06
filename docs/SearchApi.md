# openapi_netdisco.SearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_search_device_get**](SearchApi.md#api_v1_search_device_get) | **GET** /api/v1/search/device | 
[**api_v1_search_node_get**](SearchApi.md#api_v1_search_node_get) | **GET** /api/v1/search/node | 
[**api_v1_search_port_get**](SearchApi.md#api_v1_search_port_get) | **GET** /api/v1/search/port | 
[**api_v1_search_vlan_get**](SearchApi.md#api_v1_search_vlan_get) | **GET** /api/v1/search/vlan | 


# **api_v1_search_device_get**
> api_v1_search_device_get(q=q, name=name, location=location, dns=dns, ip=ip, description=description, mac=mac, model=model, os=os, os_ver=os_ver, vendor=vendor, layers=layers, matchall=matchall)



Device Search

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
    api_instance = openapi_netdisco.SearchApi(api_client)
    q = 'q_example' # str | Partial match of Device contact, serial, chassis ID, module serials, location, name, description, dns, or any IP alias (optional)
name = 'name_example' # str | Partial match of the Device name (optional)
location = 'location_example' # str | Partial match of the Device location (optional)
dns = 'dns_example' # str | Partial match of any of the Device IP aliases (optional)
ip = 'ip_example' # str | IP or IP Prefix within which the Device must have an interface address (optional)
description = 'description_example' # str | Partial match of the Device description (optional)
mac = 'mac_example' # str | MAC Address of the Device or any of its Interfaces (optional)
model = 'model_example' # str | Exact match of the Device model (optional)
os = 'os_example' # str | Exact match of the Device operating system (optional)
os_ver = 'os_ver_example' # str | Exact match of the Device operating system version (optional)
vendor = 'vendor_example' # str | Exact match of the Device vendor (optional)
layers = 'layers_example' # str | OSI Layer which the device must support (optional)
matchall = False # bool | If true, all fields (except \"q\") must match the Device (optional) (default to False)

    try:
        api_instance.api_v1_search_device_get(q=q, name=name, location=location, dns=dns, ip=ip, description=description, mac=mac, model=model, os=os, os_ver=os_ver, vendor=vendor, layers=layers, matchall=matchall)
    except ApiException as e:
        print("Exception when calling SearchApi->api_v1_search_device_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Partial match of Device contact, serial, chassis ID, module serials, location, name, description, dns, or any IP alias | [optional] 
 **name** | **str**| Partial match of the Device name | [optional] 
 **location** | **str**| Partial match of the Device location | [optional] 
 **dns** | **str**| Partial match of any of the Device IP aliases | [optional] 
 **ip** | **str**| IP or IP Prefix within which the Device must have an interface address | [optional] 
 **description** | **str**| Partial match of the Device description | [optional] 
 **mac** | **str**| MAC Address of the Device or any of its Interfaces | [optional] 
 **model** | **str**| Exact match of the Device model | [optional] 
 **os** | **str**| Exact match of the Device operating system | [optional] 
 **os_ver** | **str**| Exact match of the Device operating system version | [optional] 
 **vendor** | **str**| Exact match of the Device vendor | [optional] 
 **layers** | **str**| OSI Layer which the device must support | [optional] 
 **matchall** | **bool**| If true, all fields (except \&quot;q\&quot;) must match the Device | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_search_node_get**
> api_v1_search_node_get(q=q, partial=partial, deviceports=deviceports, show_vendor=show_vendor, archived=archived, daterange=daterange, age_invert=age_invert)



Node Search

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
    api_instance = openapi_netdisco.SearchApi(api_client)
    q = 'q_example' # str | MAC Address or IP Address or Hostname (without Domain Suffix) of a Node (supports SQL or \"*\" wildcards) (optional)
partial = False # bool | Partially match the \"q\" parameter (wildcard characters not required) (optional) (default to False)
deviceports = True # bool | MAC Address search will include Device Port MACs (optional) (default to True)
show_vendor = False # bool | Include interface Vendor in results (optional) (default to False)
archived = False # bool | Include archived records in results (optional) (default to False)
daterange = '1970-01-01 to 2021-11-03' # str | Date Range in format \"YYYY-MM-DD to YYYY-MM-DD\" (optional) (default to '1970-01-01 to 2021-11-03')
age_invert = False # bool | Results should NOT be within daterange (optional) (default to False)

    try:
        api_instance.api_v1_search_node_get(q=q, partial=partial, deviceports=deviceports, show_vendor=show_vendor, archived=archived, daterange=daterange, age_invert=age_invert)
    except ApiException as e:
        print("Exception when calling SearchApi->api_v1_search_node_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| MAC Address or IP Address or Hostname (without Domain Suffix) of a Node (supports SQL or \&quot;*\&quot; wildcards) | [optional] 
 **partial** | **bool**| Partially match the \&quot;q\&quot; parameter (wildcard characters not required) | [optional] [default to False]
 **deviceports** | **bool**| MAC Address search will include Device Port MACs | [optional] [default to True]
 **show_vendor** | **bool**| Include interface Vendor in results | [optional] [default to False]
 **archived** | **bool**| Include archived records in results | [optional] [default to False]
 **daterange** | **str**| Date Range in format \&quot;YYYY-MM-DD to YYYY-MM-DD\&quot; | [optional] [default to &#39;1970-01-01 to 2021-11-03&#39;]
 **age_invert** | **bool**| Results should NOT be within daterange | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_search_port_get**
> api_v1_search_port_get(q=q, partial=partial, uplink=uplink, ethernet=ethernet)



Port Search

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
    api_instance = openapi_netdisco.SearchApi(api_client)
    q = 'q_example' # str | Port name or VLAN or MAC address (optional)
partial = True # bool | Search for a partial match on parameter \"q\" (optional) (default to True)
uplink = False # bool | Include uplinks in results (optional) (default to False)
ethernet = True # bool | Only Ethernet type interfaces in results (optional) (default to True)

    try:
        api_instance.api_v1_search_port_get(q=q, partial=partial, uplink=uplink, ethernet=ethernet)
    except ApiException as e:
        print("Exception when calling SearchApi->api_v1_search_port_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Port name or VLAN or MAC address | [optional] 
 **partial** | **bool**| Search for a partial match on parameter \&quot;q\&quot; | [optional] [default to True]
 **uplink** | **bool**| Include uplinks in results | [optional] [default to False]
 **ethernet** | **bool**| Only Ethernet type interfaces in results | [optional] [default to True]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_search_vlan_get**
> api_v1_search_vlan_get(q=q)



VLAN Search

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
    api_instance = openapi_netdisco.SearchApi(api_client)
    q = 'q_example' # str | VLAN name or number (optional)

    try:
        api_instance.api_v1_search_vlan_get(q=q)
    except ApiException as e:
        print("Exception when calling SearchApi->api_v1_search_vlan_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| VLAN name or number | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

