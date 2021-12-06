# coding: utf-8

"""
    App::Netdisco

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.050003
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_netdisco.configuration import Configuration


class PortUtilization(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'ip': 'str',
        'dns': 'str',
        'port_count': 'int',
        'ports_in_use': 'int',
        'ports_shutdown': 'int',
        'ports_free': 'int'
    }

    attribute_map = {
        'ip': 'ip',
        'dns': 'dns',
        'port_count': 'port_count',
        'ports_in_use': 'ports_in_use',
        'ports_shutdown': 'ports_shutdown',
        'ports_free': 'ports_free'
    }

    def __init__(self, ip=None, dns=None, port_count=None, ports_in_use=None, ports_shutdown=None, ports_free=None, local_vars_configuration=None):  # noqa: E501
        """PortUtilization - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._ip = None
        self._dns = None
        self._port_count = None
        self._ports_in_use = None
        self._ports_shutdown = None
        self._ports_free = None
        self.discriminator = None

        self.ip = ip
        if dns is not None:
            self.dns = dns
        if port_count is not None:
            self.port_count = port_count
        if ports_in_use is not None:
            self.ports_in_use = ports_in_use
        if ports_shutdown is not None:
            self.ports_shutdown = ports_shutdown
        if ports_free is not None:
            self.ports_free = ports_free

    @property
    def ip(self):
        """Gets the ip of this PortUtilization.  # noqa: E501


        :return: The ip of this PortUtilization.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this PortUtilization.


        :param ip: The ip of this PortUtilization.  # noqa: E501
        :type ip: str
        """
        if self.local_vars_configuration.client_side_validation and ip is None:  # noqa: E501
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

    @property
    def dns(self):
        """Gets the dns of this PortUtilization.  # noqa: E501


        :return: The dns of this PortUtilization.  # noqa: E501
        :rtype: str
        """
        return self._dns

    @dns.setter
    def dns(self, dns):
        """Sets the dns of this PortUtilization.


        :param dns: The dns of this PortUtilization.  # noqa: E501
        :type dns: str
        """

        self._dns = dns

    @property
    def port_count(self):
        """Gets the port_count of this PortUtilization.  # noqa: E501


        :return: The port_count of this PortUtilization.  # noqa: E501
        :rtype: int
        """
        return self._port_count

    @port_count.setter
    def port_count(self, port_count):
        """Sets the port_count of this PortUtilization.


        :param port_count: The port_count of this PortUtilization.  # noqa: E501
        :type port_count: int
        """

        self._port_count = port_count

    @property
    def ports_in_use(self):
        """Gets the ports_in_use of this PortUtilization.  # noqa: E501


        :return: The ports_in_use of this PortUtilization.  # noqa: E501
        :rtype: int
        """
        return self._ports_in_use

    @ports_in_use.setter
    def ports_in_use(self, ports_in_use):
        """Sets the ports_in_use of this PortUtilization.


        :param ports_in_use: The ports_in_use of this PortUtilization.  # noqa: E501
        :type ports_in_use: int
        """

        self._ports_in_use = ports_in_use

    @property
    def ports_shutdown(self):
        """Gets the ports_shutdown of this PortUtilization.  # noqa: E501


        :return: The ports_shutdown of this PortUtilization.  # noqa: E501
        :rtype: int
        """
        return self._ports_shutdown

    @ports_shutdown.setter
    def ports_shutdown(self, ports_shutdown):
        """Sets the ports_shutdown of this PortUtilization.


        :param ports_shutdown: The ports_shutdown of this PortUtilization.  # noqa: E501
        :type ports_shutdown: int
        """

        self._ports_shutdown = ports_shutdown

    @property
    def ports_free(self):
        """Gets the ports_free of this PortUtilization.  # noqa: E501


        :return: The ports_free of this PortUtilization.  # noqa: E501
        :rtype: int
        """
        return self._ports_free

    @ports_free.setter
    def ports_free(self, ports_free):
        """Sets the ports_free of this PortUtilization.


        :param ports_free: The ports_free of this PortUtilization.  # noqa: E501
        :type ports_free: int
        """

        self._ports_free = ports_free

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PortUtilization):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortUtilization):
            return True

        return self.to_dict() != other.to_dict()
