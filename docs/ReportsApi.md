# openapi_netdisco.ReportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_report_device_deviceaddrnodns_get**](ReportsApi.md#api_v1_report_device_deviceaddrnodns_get) | **GET** /api/v1/report/device/deviceaddrnodns | 
[**api_v1_report_device_devicebylocation_get**](ReportsApi.md#api_v1_report_device_devicebylocation_get) | **GET** /api/v1/report/device/devicebylocation | 
[**api_v1_report_device_devicednsmismatch_get**](ReportsApi.md#api_v1_report_device_devicednsmismatch_get) | **GET** /api/v1/report/device/devicednsmismatch | 
[**api_v1_report_device_devicepoestatus_get**](ReportsApi.md#api_v1_report_device_devicepoestatus_get) | **GET** /api/v1/report/device/devicepoestatus | 
[**api_v1_report_device_portutilization_get**](ReportsApi.md#api_v1_report_device_portutilization_get) | **GET** /api/v1/report/device/portutilization | 
[**api_v1_report_ip_ipinventory_get**](ReportsApi.md#api_v1_report_ip_ipinventory_get) | **GET** /api/v1/report/ip/ipinventory | 
[**api_v1_report_ip_subnets_get**](ReportsApi.md#api_v1_report_ip_subnets_get) | **GET** /api/v1/report/ip/subnets | 
[**api_v1_report_node_nodemultiips_get**](ReportsApi.md#api_v1_report_node_nodemultiips_get) | **GET** /api/v1/report/node/nodemultiips | 
[**api_v1_report_node_nodesdiscovered_get**](ReportsApi.md#api_v1_report_node_nodesdiscovered_get) | **GET** /api/v1/report/node/nodesdiscovered | 
[**api_v1_report_port_duplexmismatch_get**](ReportsApi.md#api_v1_report_port_duplexmismatch_get) | **GET** /api/v1/report/port/duplexmismatch | 
[**api_v1_report_port_halfduplex_get**](ReportsApi.md#api_v1_report_port_halfduplex_get) | **GET** /api/v1/report/port/halfduplex | 
[**api_v1_report_port_portadmindown_get**](ReportsApi.md#api_v1_report_port_portadmindown_get) | **GET** /api/v1/report/port/portadmindown | 
[**api_v1_report_port_portblocking_get**](ReportsApi.md#api_v1_report_port_portblocking_get) | **GET** /api/v1/report/port/portblocking | 
[**api_v1_report_port_portmultinodes_get**](ReportsApi.md#api_v1_report_port_portmultinodes_get) | **GET** /api/v1/report/port/portmultinodes | 
[**api_v1_report_port_portserrordisabled_get**](ReportsApi.md#api_v1_report_port_portserrordisabled_get) | **GET** /api/v1/report/port/portserrordisabled | 
[**api_v1_report_port_portssid_get**](ReportsApi.md#api_v1_report_port_portssid_get) | **GET** /api/v1/report/port/portssid | 
[**api_v1_report_port_portvlanmismatch_get**](ReportsApi.md#api_v1_report_port_portvlanmismatch_get) | **GET** /api/v1/report/port/portvlanmismatch | 
[**api_v1_report_vlan_vlaninventory_get**](ReportsApi.md#api_v1_report_vlan_vlaninventory_get) | **GET** /api/v1/report/vlan/vlaninventory | 
[**api_v1_report_wireless_apchanneldist_get**](ReportsApi.md#api_v1_report_wireless_apchanneldist_get) | **GET** /api/v1/report/wireless/apchanneldist | 
[**api_v1_report_wireless_apclients_get**](ReportsApi.md#api_v1_report_wireless_apclients_get) | **GET** /api/v1/report/wireless/apclients | 
[**api_v1_report_wireless_apradiochannelpower_get**](ReportsApi.md#api_v1_report_wireless_apradiochannelpower_get) | **GET** /api/v1/report/wireless/apradiochannelpower | 
[**api_v1_report_wireless_ssidinventory_get**](ReportsApi.md#api_v1_report_wireless_ssidinventory_get) | **GET** /api/v1/report/wireless/ssidinventory | 


# **api_v1_report_device_deviceaddrnodns_get**
> api_v1_report_device_deviceaddrnodns_get()



Addresses without DNS Entries Report

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
    api_instance = openapi_netdisco.ReportsApi(api_client)
    
    try:
        api_instance.api_v1_report_device_deviceaddrnodns_get()
    except ApiException as e:
        print("Exception when calling ReportsApi->api_v1_report_device_deviceaddrnodns_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **api_v1_report_device_devicebylocation_get**
> api_v1_report_device_devicebylocation_get()



By Location Report

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
    api_instance = openapi_netdisco.ReportsApi(api_client)
    
    try:
        api_instance.api_v1_report_device_devicebylocation_get()
    except ApiException as e:
        print("Exception when calling ReportsApi->api_v1_report_device_devicebylocation_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **api_v1_report_device_devicednsmismatch_get**
> api_v1_report_device_devicednsmismatch_get()



Device Name / DNS Mismatches Report

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
    api_instance = openapi_netdisco.ReportsApi(api_client)
    
    try:
        api_instance.api_v1_report_device_devicednsmismatch_get()
    except ApiException as e:
        print("Exception when calling ReportsApi->api_v1_report_device_devicednsmismatch_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **api_v1_report_device_devicepoestatus_get**
> api_v1_report_device_devicepoestatus_get()



Power over Ethernet (PoE) Status Report

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
    api_instance = openapi_netdisco.ReportsApi(api_client)
    
    try:
        api_instance.api_v1_report_device_devicepoestatus_get()
    except ApiException as e:
        print("Exception when calling ReportsApi->api_v1_report_device_devicepoestatus_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **api_v1_report_device_portutilization_get**
> list[PortUtilization] api_v1_report_device_portutilization_get(age_num=age_num, age_unit=age_unit)



Port Utilization Report

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
    api_instance = openapi_netdisco.ReportsApi(api_client)
    age_num = '3' # str | Mark as Free if down for (quantity) (optional) (default to '3')
age_unit = 'months' # str | Mark as Free if down for (period) (optional) (default to 'months')

    try:
        api_response = api_instance.api_v1_report_device_portutilization_get(age_num=age_num, age_unit=age_unit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->api_v1_report_device_portutilization_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **age_num** | **str**| Mark as Free if down for (quantity) | [optional] [default to &#39;3&#39;]
 **age_unit** | **str**| Mark as Free if down for (period) | [optional] [default to &#39;months&#39;]

### Return type

[**list[PortUtilization]**](PortUtilization.md)

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

# **api_v1_report_ip_ipinventory_get**
> api_v1_report_ip_ipinventory_get(subnet=subnet, daterange=daterange, age_invert=age_invert, limit=limit, never=never)



IP Inventory Report

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
    api_instance = openapi_netdisco.ReportsApi(api_client)
    subnet = 'subnet_example' # str | IP Prefix to search (optional)
daterange = '1970-01-01 to 2021-11-03' # str | Date range to search (optional) (default to '1970-01-01 to 2021-11-03')
age_invert = False # bool | Results should NOT be within daterange (optional) (default to False)
limit = '256' # str | Maximum number of historical records (optional) (default to '256')
never = False # bool | Include in the report IPs never seen (optional) (default to False)

    try:
        api_instance.api_v1_report_ip_ipinventory_get(subnet=subnet, daterange=daterange, age_invert=age_invert, limit=limit, never=never)
    except ApiException as e:
        print("Exception when calling ReportsApi->api_v1_report_ip_ipinventory_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subnet** | **str**| IP Prefix to search | [optional] 
 **daterange** | **str**| Date range to search | [optional] [default to &#39;1970-01-01 to 2021-11-03&#39;]
 **age_invert** | **bool**| Results should NOT be within daterange | [optional] [default to False]
 **limit** | **str**| Maximum number of historical records | [optional] [default to &#39;256&#39;]
 **never** | **bool**| Include in the report IPs never seen | [optional] [default to False]

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

# **api_v1_report_ip_subnets_get**
> api_v1_report_ip_subnets_get(subnet=subnet, daterange=daterange, age_invert=age_invert)



Subnet Utilization Report

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
    api_instance = openapi_netdisco.ReportsApi(api_client)
    subnet = '0.0.0.0/32' # str | IP Prefix to search (optional) (default to '0.0.0.0/32')
daterange = '1970-01-01 to 2021-11-03' # str | Date range to search (optional) (default to '1970-01-01 to 2021-11-03')
age_invert = False # bool | Results should NOT be within daterange (optional) (default to False)

    try:
        api_instance.api_v1_report_ip_subnets_get(subnet=subnet, daterange=daterange, age_invert=age_invert)
    except ApiException as e:
        print("Exception when calling ReportsApi->api_v1_report_ip_subnets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subnet** | **str**| IP Prefix to search | [optional] [default to &#39;0.0.0.0/32&#39;]
 **daterange** | **str**| Date range to search | [optional] [default to &#39;1970-01-01 to 2021-11-03&#39;]
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

# **api_v1_report_node_nodemultiips_get**
> api_v1_report_node_nodemultiips_get()



Nodes with multiple active IP addresses Report

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
    api_instance = openapi_netdisco.ReportsApi(api_client)
    
    try:
        api_instance.api_v1_report_node_nodemultiips_get()
    except ApiException as e:
        print("Exception when calling ReportsApi->api_v1_report_node_nodemultiips_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **api_v1_report_node_nodesdiscovered_get**
> api_v1_report_node_nodesdiscovered_get(remote_id=remote_id, remote_type=remote_type, aps=aps, phones=phones, matchall=matchall)



Nodes discovered through LLDP/CDP Report

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
    api_instance = openapi_netdisco.ReportsApi(api_client)
    remote_id = 'remote_id_example' # str | Host Name reported (optional)
remote_type = 'remote_type_example' # str | Platform reported (optional)
aps = False # bool | Include Wireless APs in the report (optional) (default to False)
phones = False # bool | Include IP Phones in the report (optional) (default to False)
matchall = False # bool | Match all parameters (true) or any (false) (optional) (default to False)

    try:
        api_instance.api_v1_report_node_nodesdiscovered_get(remote_id=remote_id, remote_type=remote_type, aps=aps, phones=phones, matchall=matchall)
    except ApiException as e:
        print("Exception when calling ReportsApi->api_v1_report_node_nodesdiscovered_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remote_id** | **str**| Host Name reported | [optional] 
 **remote_type** | **str**| Platform reported | [optional] 
 **aps** | **bool**| Include Wireless APs in the report | [optional] [default to False]
 **phones** | **bool**| Include IP Phones in the report | [optional] [default to False]
 **matchall** | **bool**| Match all parameters (true) or any (false) | [optional] [default to False]

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

# **api_v1_report_port_duplexmismatch_get**
> api_v1_report_port_duplexmismatch_get()



Duplex Mismatches Between Devices Report

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
    api_instance = openapi_netdisco.ReportsApi(api_client)
    
    try:
        api_instance.api_v1_report_port_duplexmismatch_get()
    except ApiException as e:
        print("Exception when calling ReportsApi->api_v1_report_port_duplexmismatch_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **api_v1_report_port_halfduplex_get**
> api_v1_report_port_halfduplex_get()



Ports in Half Duplex Mode Report

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
    api_instance = openapi_netdisco.ReportsApi(api_client)
    
    try:
        api_instance.api_v1_report_port_halfduplex_get()
    except ApiException as e:
        print("Exception when calling ReportsApi->api_v1_report_port_halfduplex_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **api_v1_report_port_portadmindown_get**
> api_v1_report_port_portadmindown_get()



Ports administratively disabled Report

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
    api_instance = openapi_netdisco.ReportsApi(api_client)
    
    try:
        api_instance.api_v1_report_port_portadmindown_get()
    except ApiException as e:
        print("Exception when calling ReportsApi->api_v1_report_port_portadmindown_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **api_v1_report_port_portblocking_get**
> api_v1_report_port_portblocking_get()



Ports that are blocking Report

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
    api_instance = openapi_netdisco.ReportsApi(api_client)
    
    try:
        api_instance.api_v1_report_port_portblocking_get()
    except ApiException as e:
        print("Exception when calling ReportsApi->api_v1_report_port_portblocking_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **api_v1_report_port_portmultinodes_get**
> api_v1_report_port_portmultinodes_get(vlan=vlan)



Ports with multiple nodes attached Report

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
    api_instance = openapi_netdisco.ReportsApi(api_client)
    vlan = 56 # int | Filter by VLAN (optional)

    try:
        api_instance.api_v1_report_port_portmultinodes_get(vlan=vlan)
    except ApiException as e:
        print("Exception when calling ReportsApi->api_v1_report_port_portmultinodes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vlan** | **int**| Filter by VLAN | [optional] 

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

# **api_v1_report_port_portserrordisabled_get**
> api_v1_report_port_portserrordisabled_get()



Error Disabled Ports Report

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
    api_instance = openapi_netdisco.ReportsApi(api_client)
    
    try:
        api_instance.api_v1_report_port_portserrordisabled_get()
    except ApiException as e:
        print("Exception when calling ReportsApi->api_v1_report_port_portserrordisabled_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **api_v1_report_port_portssid_get**
> api_v1_report_port_portssid_get(ssid=ssid)



Port SSID Inventory Report

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
    api_instance = openapi_netdisco.ReportsApi(api_client)
    ssid = 'ssid_example' # str | Get details for this SSID (optional)

    try:
        api_instance.api_v1_report_port_portssid_get(ssid=ssid)
    except ApiException as e:
        print("Exception when calling ReportsApi->api_v1_report_port_portssid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssid** | **str**| Get details for this SSID | [optional] 

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

# **api_v1_report_port_portvlanmismatch_get**
> api_v1_report_port_portvlanmismatch_get()



Port VLAN Mismatches Report

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
    api_instance = openapi_netdisco.ReportsApi(api_client)
    
    try:
        api_instance.api_v1_report_port_portvlanmismatch_get()
    except ApiException as e:
        print("Exception when calling ReportsApi->api_v1_report_port_portvlanmismatch_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **api_v1_report_vlan_vlaninventory_get**
> api_v1_report_vlan_vlaninventory_get()



VLAN Inventory Report

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
    api_instance = openapi_netdisco.ReportsApi(api_client)
    
    try:
        api_instance.api_v1_report_vlan_vlaninventory_get()
    except ApiException as e:
        print("Exception when calling ReportsApi->api_v1_report_vlan_vlaninventory_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **api_v1_report_wireless_apchanneldist_get**
> api_v1_report_wireless_apchanneldist_get()



Access Point Channel Distribution Report

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
    api_instance = openapi_netdisco.ReportsApi(api_client)
    
    try:
        api_instance.api_v1_report_wireless_apchanneldist_get()
    except ApiException as e:
        print("Exception when calling ReportsApi->api_v1_report_wireless_apchanneldist_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **api_v1_report_wireless_apclients_get**
> api_v1_report_wireless_apclients_get()



Access Point Client Count Report

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
    api_instance = openapi_netdisco.ReportsApi(api_client)
    
    try:
        api_instance.api_v1_report_wireless_apclients_get()
    except ApiException as e:
        print("Exception when calling ReportsApi->api_v1_report_wireless_apclients_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **api_v1_report_wireless_apradiochannelpower_get**
> api_v1_report_wireless_apradiochannelpower_get()



Access Point Radios Channel and Power Report

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
    api_instance = openapi_netdisco.ReportsApi(api_client)
    
    try:
        api_instance.api_v1_report_wireless_apradiochannelpower_get()
    except ApiException as e:
        print("Exception when calling ReportsApi->api_v1_report_wireless_apradiochannelpower_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **api_v1_report_wireless_ssidinventory_get**
> api_v1_report_wireless_ssidinventory_get()



SSID Inventory Report

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
    api_instance = openapi_netdisco.ReportsApi(api_client)
    
    try:
        api_instance.api_v1_report_wireless_ssidinventory_get()
    except ApiException as e:
        print("Exception when calling ReportsApi->api_v1_report_wireless_ssidinventory_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

