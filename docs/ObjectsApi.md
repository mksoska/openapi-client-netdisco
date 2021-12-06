# openapi_netdisco.ObjectsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_object_device_ip_device_ips_get**](ObjectsApi.md#api_v1_object_device_ip_device_ips_get) | **GET** /api/v1/object/device/{ip}/device_ips | 
[**api_v1_object_device_ip_get**](ObjectsApi.md#api_v1_object_device_ip_get) | **GET** /api/v1/object/device/{ip} | 
[**api_v1_object_device_ip_modules_get**](ObjectsApi.md#api_v1_object_device_ip_modules_get) | **GET** /api/v1/object/device/{ip}/modules | 
[**api_v1_object_device_ip_nodes_get**](ObjectsApi.md#api_v1_object_device_ip_nodes_get) | **GET** /api/v1/object/device/{ip}/nodes | 
[**api_v1_object_device_ip_port_port_active_nodes_get**](ObjectsApi.md#api_v1_object_device_ip_port_port_active_nodes_get) | **GET** /api/v1/object/device/{ip}/port/{port}/active_nodes | 
[**api_v1_object_device_ip_port_port_active_nodes_with_age_get**](ObjectsApi.md#api_v1_object_device_ip_port_port_active_nodes_with_age_get) | **GET** /api/v1/object/device/{ip}/port/{port}/active_nodes_with_age | 
[**api_v1_object_device_ip_port_port_agg_master_get**](ObjectsApi.md#api_v1_object_device_ip_port_port_agg_master_get) | **GET** /api/v1/object/device/{ip}/port/{port}/agg_master | 
[**api_v1_object_device_ip_port_port_get**](ObjectsApi.md#api_v1_object_device_ip_port_port_get) | **GET** /api/v1/object/device/{ip}/port/{port} | 
[**api_v1_object_device_ip_port_port_last_node_get**](ObjectsApi.md#api_v1_object_device_ip_port_port_last_node_get) | **GET** /api/v1/object/device/{ip}/port/{port}/last_node | 
[**api_v1_object_device_ip_port_port_logs_get**](ObjectsApi.md#api_v1_object_device_ip_port_port_logs_get) | **GET** /api/v1/object/device/{ip}/port/{port}/logs | 
[**api_v1_object_device_ip_port_port_neighbor_get**](ObjectsApi.md#api_v1_object_device_ip_port_port_neighbor_get) | **GET** /api/v1/object/device/{ip}/port/{port}/neighbor | 
[**api_v1_object_device_ip_port_port_nodes_get**](ObjectsApi.md#api_v1_object_device_ip_port_port_nodes_get) | **GET** /api/v1/object/device/{ip}/port/{port}/nodes | 
[**api_v1_object_device_ip_port_port_nodes_with_age_get**](ObjectsApi.md#api_v1_object_device_ip_port_port_nodes_with_age_get) | **GET** /api/v1/object/device/{ip}/port/{port}/nodes_with_age | 
[**api_v1_object_device_ip_port_port_power_get**](ObjectsApi.md#api_v1_object_device_ip_port_port_power_get) | **GET** /api/v1/object/device/{ip}/port/{port}/power | 
[**api_v1_object_device_ip_port_port_properties_get**](ObjectsApi.md#api_v1_object_device_ip_port_port_properties_get) | **GET** /api/v1/object/device/{ip}/port/{port}/properties | 
[**api_v1_object_device_ip_port_port_ssid_get**](ObjectsApi.md#api_v1_object_device_ip_port_port_ssid_get) | **GET** /api/v1/object/device/{ip}/port/{port}/ssid | 
[**api_v1_object_device_ip_port_port_vlans_get**](ObjectsApi.md#api_v1_object_device_ip_port_port_vlans_get) | **GET** /api/v1/object/device/{ip}/port/{port}/vlans | 
[**api_v1_object_device_ip_port_port_wireless_get**](ObjectsApi.md#api_v1_object_device_ip_port_port_wireless_get) | **GET** /api/v1/object/device/{ip}/port/{port}/wireless | 
[**api_v1_object_device_ip_port_vlans_get**](ObjectsApi.md#api_v1_object_device_ip_port_vlans_get) | **GET** /api/v1/object/device/{ip}/port_vlans | 
[**api_v1_object_device_ip_ports_get**](ObjectsApi.md#api_v1_object_device_ip_ports_get) | **GET** /api/v1/object/device/{ip}/ports | 
[**api_v1_object_device_ip_powered_ports_get**](ObjectsApi.md#api_v1_object_device_ip_powered_ports_get) | **GET** /api/v1/object/device/{ip}/powered_ports | 
[**api_v1_object_device_ip_ssids_get**](ObjectsApi.md#api_v1_object_device_ip_ssids_get) | **GET** /api/v1/object/device/{ip}/ssids | 
[**api_v1_object_device_ip_vlans_get**](ObjectsApi.md#api_v1_object_device_ip_vlans_get) | **GET** /api/v1/object/device/{ip}/vlans | 
[**api_v1_object_device_ip_wireless_ports_get**](ObjectsApi.md#api_v1_object_device_ip_wireless_ports_get) | **GET** /api/v1/object/device/{ip}/wireless_ports | 
[**api_v1_object_vlan_vlan_nodes_get**](ObjectsApi.md#api_v1_object_vlan_vlan_nodes_get) | **GET** /api/v1/object/vlan/{vlan}/nodes | 


# **api_v1_object_device_ip_device_ips_get**
> list[Address] api_v1_object_device_ip_device_ips_get(ip)



Returns device_ips rows for a given device

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.

    try:
        api_response = api_instance.api_v1_object_device_ip_device_ips_get(ip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_device_ips_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 

### Return type

[**list[Address]**](Address.md)

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

# **api_v1_object_device_ip_get**
> Device api_v1_object_device_ip_get(ip)



Returns a row from the device table

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.

    try:
        api_response = api_instance.api_v1_object_device_ip_get(ip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 

### Return type

[**Device**](Device.md)

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

# **api_v1_object_device_ip_modules_get**
> api_v1_object_device_ip_modules_get(ip)



Returns modules rows for a given device

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.

    try:
        api_instance.api_v1_object_device_ip_modules_get(ip)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_modules_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 

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

# **api_v1_object_device_ip_nodes_get**
> api_v1_object_device_ip_nodes_get(ip, active_only=active_only)



Returns the nodes found on a given Device

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.
active_only = True # bool | Restrict results to active Nodes only (optional) (default to True)

    try:
        api_instance.api_v1_object_device_ip_nodes_get(ip, active_only=active_only)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_nodes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 
 **active_only** | **bool**| Restrict results to active Nodes only | [optional] [default to True]

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

# **api_v1_object_device_ip_port_port_active_nodes_get**
> api_v1_object_device_ip_port_port_active_nodes_get(ip, port)



Returns active_nodes rows for a given port

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.
port = 'port_example' # str | Name of the port. Use the \".../device/{ip}/ports\" method to find these.

    try:
        api_instance.api_v1_object_device_ip_port_port_active_nodes_get(ip, port)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_port_port_active_nodes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 
 **port** | **str**| Name of the port. Use the \&quot;.../device/{ip}/ports\&quot; method to find these. | 

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

# **api_v1_object_device_ip_port_port_active_nodes_with_age_get**
> api_v1_object_device_ip_port_port_active_nodes_with_age_get(ip, port)



Returns active_nodes_with_age rows for a given port

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.
port = 'port_example' # str | Name of the port. Use the \".../device/{ip}/ports\" method to find these.

    try:
        api_instance.api_v1_object_device_ip_port_port_active_nodes_with_age_get(ip, port)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_port_port_active_nodes_with_age_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 
 **port** | **str**| Name of the port. Use the \&quot;.../device/{ip}/ports\&quot; method to find these. | 

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

# **api_v1_object_device_ip_port_port_agg_master_get**
> api_v1_object_device_ip_port_port_agg_master_get(ip, port)



Returns the related agg_master table entry for a given port

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.
port = 'port_example' # str | Name of the port. Use the \".../device/{ip}/ports\" method to find these.

    try:
        api_instance.api_v1_object_device_ip_port_port_agg_master_get(ip, port)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_port_port_agg_master_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 
 **port** | **str**| Name of the port. Use the \&quot;.../device/{ip}/ports\&quot; method to find these. | 

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

# **api_v1_object_device_ip_port_port_get**
> Port api_v1_object_device_ip_port_port_get(ip, port)



Returns a row from the device_port table

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.
port = 'port_example' # str | Name of the port. Use the \".../device/{ip}/ports\" method to find these.

    try:
        api_response = api_instance.api_v1_object_device_ip_port_port_get(ip, port)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_port_port_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 
 **port** | **str**| Name of the port. Use the \&quot;.../device/{ip}/ports\&quot; method to find these. | 

### Return type

[**Port**](Port.md)

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

# **api_v1_object_device_ip_port_port_last_node_get**
> api_v1_object_device_ip_port_port_last_node_get(ip, port)



Returns the related last_node table entry for a given port

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.
port = 'port_example' # str | Name of the port. Use the \".../device/{ip}/ports\" method to find these.

    try:
        api_instance.api_v1_object_device_ip_port_port_last_node_get(ip, port)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_port_port_last_node_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 
 **port** | **str**| Name of the port. Use the \&quot;.../device/{ip}/ports\&quot; method to find these. | 

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

# **api_v1_object_device_ip_port_port_logs_get**
> api_v1_object_device_ip_port_port_logs_get(ip, port)



Returns logs rows for a given port

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.
port = 'port_example' # str | Name of the port. Use the \".../device/{ip}/ports\" method to find these.

    try:
        api_instance.api_v1_object_device_ip_port_port_logs_get(ip, port)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_port_port_logs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 
 **port** | **str**| Name of the port. Use the \&quot;.../device/{ip}/ports\&quot; method to find these. | 

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

# **api_v1_object_device_ip_port_port_neighbor_get**
> api_v1_object_device_ip_port_port_neighbor_get(ip, port)



Returns the related neighbor table entry for a given port

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.
port = 'port_example' # str | Name of the port. Use the \".../device/{ip}/ports\" method to find these.

    try:
        api_instance.api_v1_object_device_ip_port_port_neighbor_get(ip, port)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_port_port_neighbor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 
 **port** | **str**| Name of the port. Use the \&quot;.../device/{ip}/ports\&quot; method to find these. | 

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

# **api_v1_object_device_ip_port_port_nodes_get**
> api_v1_object_device_ip_port_port_nodes_get(ip, port)



Returns nodes rows for a given port

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.
port = 'port_example' # str | Name of the port. Use the \".../device/{ip}/ports\" method to find these.

    try:
        api_instance.api_v1_object_device_ip_port_port_nodes_get(ip, port)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_port_port_nodes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 
 **port** | **str**| Name of the port. Use the \&quot;.../device/{ip}/ports\&quot; method to find these. | 

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

# **api_v1_object_device_ip_port_port_nodes_with_age_get**
> api_v1_object_device_ip_port_port_nodes_with_age_get(ip, port)



Returns nodes_with_age rows for a given port

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.
port = 'port_example' # str | Name of the port. Use the \".../device/{ip}/ports\" method to find these.

    try:
        api_instance.api_v1_object_device_ip_port_port_nodes_with_age_get(ip, port)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_port_port_nodes_with_age_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 
 **port** | **str**| Name of the port. Use the \&quot;.../device/{ip}/ports\&quot; method to find these. | 

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

# **api_v1_object_device_ip_port_port_power_get**
> api_v1_object_device_ip_port_port_power_get(ip, port)



Returns the related power table entry for a given port

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.
port = 'port_example' # str | Name of the port. Use the \".../device/{ip}/ports\" method to find these.

    try:
        api_instance.api_v1_object_device_ip_port_port_power_get(ip, port)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_port_port_power_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 
 **port** | **str**| Name of the port. Use the \&quot;.../device/{ip}/ports\&quot; method to find these. | 

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

# **api_v1_object_device_ip_port_port_properties_get**
> api_v1_object_device_ip_port_port_properties_get(ip, port)



Returns the related properties table entry for a given port

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.
port = 'port_example' # str | Name of the port. Use the \".../device/{ip}/ports\" method to find these.

    try:
        api_instance.api_v1_object_device_ip_port_port_properties_get(ip, port)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_port_port_properties_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 
 **port** | **str**| Name of the port. Use the \&quot;.../device/{ip}/ports\&quot; method to find these. | 

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

# **api_v1_object_device_ip_port_port_ssid_get**
> api_v1_object_device_ip_port_port_ssid_get(ip, port)



Returns the related ssid table entry for a given port

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.
port = 'port_example' # str | Name of the port. Use the \".../device/{ip}/ports\" method to find these.

    try:
        api_instance.api_v1_object_device_ip_port_port_ssid_get(ip, port)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_port_port_ssid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 
 **port** | **str**| Name of the port. Use the \&quot;.../device/{ip}/ports\&quot; method to find these. | 

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

# **api_v1_object_device_ip_port_port_vlans_get**
> api_v1_object_device_ip_port_port_vlans_get(ip, port)



Returns vlans rows for a given port

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.
port = 'port_example' # str | Name of the port. Use the \".../device/{ip}/ports\" method to find these.

    try:
        api_instance.api_v1_object_device_ip_port_port_vlans_get(ip, port)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_port_port_vlans_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 
 **port** | **str**| Name of the port. Use the \&quot;.../device/{ip}/ports\&quot; method to find these. | 

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

# **api_v1_object_device_ip_port_port_wireless_get**
> api_v1_object_device_ip_port_port_wireless_get(ip, port)



Returns the related wireless table entry for a given port

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.
port = 'port_example' # str | Name of the port. Use the \".../device/{ip}/ports\" method to find these.

    try:
        api_instance.api_v1_object_device_ip_port_port_wireless_get(ip, port)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_port_port_wireless_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 
 **port** | **str**| Name of the port. Use the \&quot;.../device/{ip}/ports\&quot; method to find these. | 

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

# **api_v1_object_device_ip_port_vlans_get**
> api_v1_object_device_ip_port_vlans_get(ip)



Returns port_vlans rows for a given device

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.

    try:
        api_instance.api_v1_object_device_ip_port_vlans_get(ip)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_port_vlans_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 

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

# **api_v1_object_device_ip_ports_get**
> list[Port] api_v1_object_device_ip_ports_get(ip)



Returns ports rows for a given device

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.

    try:
        api_response = api_instance.api_v1_object_device_ip_ports_get(ip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_ports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 

### Return type

[**list[Port]**](Port.md)

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

# **api_v1_object_device_ip_powered_ports_get**
> api_v1_object_device_ip_powered_ports_get(ip)



Returns powered_ports rows for a given device

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.

    try:
        api_instance.api_v1_object_device_ip_powered_ports_get(ip)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_powered_ports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 

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

# **api_v1_object_device_ip_ssids_get**
> api_v1_object_device_ip_ssids_get(ip)



Returns ssids rows for a given device

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.

    try:
        api_instance.api_v1_object_device_ip_ssids_get(ip)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_ssids_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 

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

# **api_v1_object_device_ip_vlans_get**
> list[Vlan] api_v1_object_device_ip_vlans_get(ip)



Returns vlans rows for a given device

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.

    try:
        api_response = api_instance.api_v1_object_device_ip_vlans_get(ip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_vlans_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 

### Return type

[**list[Vlan]**](Vlan.md)

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

# **api_v1_object_device_ip_wireless_ports_get**
> api_v1_object_device_ip_wireless_ports_get(ip)



Returns wireless_ports rows for a given device

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    ip = 'ip_example' # str | Canonical IP of the Device. Use Search methods to find this.

    try:
        api_instance.api_v1_object_device_ip_wireless_ports_get(ip)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_device_ip_wireless_ports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Canonical IP of the Device. Use Search methods to find this. | 

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

# **api_v1_object_vlan_vlan_nodes_get**
> api_v1_object_vlan_vlan_nodes_get(vlan, active_only=active_only)



Returns the nodes found in a given VLAN

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
    api_instance = openapi_netdisco.ObjectsApi(api_client)
    vlan = 56 # int | VLAN number
active_only = True # bool | Restrict results to active Nodes only (optional) (default to True)

    try:
        api_instance.api_v1_object_vlan_vlan_nodes_get(vlan, active_only=active_only)
    except ApiException as e:
        print("Exception when calling ObjectsApi->api_v1_object_vlan_vlan_nodes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vlan** | **int**| VLAN number | 
 **active_only** | **bool**| Restrict results to active Nodes only | [optional] [default to True]

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

