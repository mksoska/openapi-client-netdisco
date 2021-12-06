# coding: utf-8

"""
    App::Netdisco

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.050003
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_netdisco
from openapi_netdisco.api.reports_api import ReportsApi  # noqa: E501
from openapi_netdisco.rest import ApiException


class TestReportsApi(unittest.TestCase):
    """ReportsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_netdisco.api.reports_api.ReportsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_report_device_deviceaddrnodns_get(self):
        """Test case for api_v1_report_device_deviceaddrnodns_get

        """
        pass

    def test_api_v1_report_device_devicebylocation_get(self):
        """Test case for api_v1_report_device_devicebylocation_get

        """
        pass

    def test_api_v1_report_device_devicednsmismatch_get(self):
        """Test case for api_v1_report_device_devicednsmismatch_get

        """
        pass

    def test_api_v1_report_device_devicepoestatus_get(self):
        """Test case for api_v1_report_device_devicepoestatus_get

        """
        pass

    def test_api_v1_report_device_portutilization_get(self):
        """Test case for api_v1_report_device_portutilization_get

        """
        pass

    def test_api_v1_report_ip_ipinventory_get(self):
        """Test case for api_v1_report_ip_ipinventory_get

        """
        pass

    def test_api_v1_report_ip_subnets_get(self):
        """Test case for api_v1_report_ip_subnets_get

        """
        pass

    def test_api_v1_report_node_nodemultiips_get(self):
        """Test case for api_v1_report_node_nodemultiips_get

        """
        pass

    def test_api_v1_report_node_nodesdiscovered_get(self):
        """Test case for api_v1_report_node_nodesdiscovered_get

        """
        pass

    def test_api_v1_report_port_duplexmismatch_get(self):
        """Test case for api_v1_report_port_duplexmismatch_get

        """
        pass

    def test_api_v1_report_port_halfduplex_get(self):
        """Test case for api_v1_report_port_halfduplex_get

        """
        pass

    def test_api_v1_report_port_portadmindown_get(self):
        """Test case for api_v1_report_port_portadmindown_get

        """
        pass

    def test_api_v1_report_port_portblocking_get(self):
        """Test case for api_v1_report_port_portblocking_get

        """
        pass

    def test_api_v1_report_port_portmultinodes_get(self):
        """Test case for api_v1_report_port_portmultinodes_get

        """
        pass

    def test_api_v1_report_port_portserrordisabled_get(self):
        """Test case for api_v1_report_port_portserrordisabled_get

        """
        pass

    def test_api_v1_report_port_portssid_get(self):
        """Test case for api_v1_report_port_portssid_get

        """
        pass

    def test_api_v1_report_port_portvlanmismatch_get(self):
        """Test case for api_v1_report_port_portvlanmismatch_get

        """
        pass

    def test_api_v1_report_vlan_vlaninventory_get(self):
        """Test case for api_v1_report_vlan_vlaninventory_get

        """
        pass

    def test_api_v1_report_wireless_apchanneldist_get(self):
        """Test case for api_v1_report_wireless_apchanneldist_get

        """
        pass

    def test_api_v1_report_wireless_apclients_get(self):
        """Test case for api_v1_report_wireless_apclients_get

        """
        pass

    def test_api_v1_report_wireless_apradiochannelpower_get(self):
        """Test case for api_v1_report_wireless_apradiochannelpower_get

        """
        pass

    def test_api_v1_report_wireless_ssidinventory_get(self):
        """Test case for api_v1_report_wireless_ssidinventory_get

        """
        pass


if __name__ == '__main__':
    unittest.main()