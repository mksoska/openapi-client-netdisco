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


class Vlan(object):
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
        'vlan': 'str',
        'description': 'str',
        'creation': 'str',
        'last_discover': 'str'
    }

    attribute_map = {
        'ip': 'ip',
        'vlan': 'vlan',
        'description': 'description',
        'creation': 'creation',
        'last_discover': 'last_discover'
    }

    def __init__(self, ip=None, vlan=None, description=None, creation=None, last_discover=None, local_vars_configuration=None):  # noqa: E501
        """Vlan - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._ip = None
        self._vlan = None
        self._description = None
        self._creation = None
        self._last_discover = None
        self.discriminator = None

        self.ip = ip
        self.vlan = vlan
        if description is not None:
            self.description = description
        if creation is not None:
            self.creation = creation
        if last_discover is not None:
            self.last_discover = last_discover

    @property
    def ip(self):
        """Gets the ip of this Vlan.  # noqa: E501


        :return: The ip of this Vlan.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Vlan.


        :param ip: The ip of this Vlan.  # noqa: E501
        :type ip: str
        """
        if self.local_vars_configuration.client_side_validation and ip is None:  # noqa: E501
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

    @property
    def vlan(self):
        """Gets the vlan of this Vlan.  # noqa: E501


        :return: The vlan of this Vlan.  # noqa: E501
        :rtype: str
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this Vlan.


        :param vlan: The vlan of this Vlan.  # noqa: E501
        :type vlan: str
        """
        if self.local_vars_configuration.client_side_validation and vlan is None:  # noqa: E501
            raise ValueError("Invalid value for `vlan`, must not be `None`")  # noqa: E501

        self._vlan = vlan

    @property
    def description(self):
        """Gets the description of this Vlan.  # noqa: E501


        :return: The description of this Vlan.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Vlan.


        :param description: The description of this Vlan.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def creation(self):
        """Gets the creation of this Vlan.  # noqa: E501


        :return: The creation of this Vlan.  # noqa: E501
        :rtype: str
        """
        return self._creation

    @creation.setter
    def creation(self, creation):
        """Sets the creation of this Vlan.


        :param creation: The creation of this Vlan.  # noqa: E501
        :type creation: str
        """

        self._creation = creation

    @property
    def last_discover(self):
        """Gets the last_discover of this Vlan.  # noqa: E501


        :return: The last_discover of this Vlan.  # noqa: E501
        :rtype: str
        """
        return self._last_discover

    @last_discover.setter
    def last_discover(self, last_discover):
        """Sets the last_discover of this Vlan.


        :param last_discover: The last_discover of this Vlan.  # noqa: E501
        :type last_discover: str
        """

        self._last_discover = last_discover

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
        if not isinstance(other, Vlan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Vlan):
            return True

        return self.to_dict() != other.to_dict()