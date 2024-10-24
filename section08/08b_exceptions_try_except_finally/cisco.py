"""
This module is designed to interact with Cisco appliances
"""
import requests
import pprint
import json

requests.packages.urllib3.disable_warnings()


class CiscoRestconf():
    """
    This class is designed to query a Cisco device via restconf
    """
    def __init__(self, ip, port, username, password):
        self.ip = ip
        self.auth = (username, password)
        self.port = str(port)

    def get_request(self, headers, dn):
        url_base = f'https://{self.ip}:{self.port}/restconf'
        uri = url_base + dn
        try:
            response = requests.get(uri, 
                headers=headers,
                auth=self.auth,
                verify=False
            )
            response.raise_for_status()
        except requests.ConnectionError as error:
            output = 'Failed to connect, check IP and port.\n' + url_base
        except requests.HTTPError as error:
            output = 'HTTP error raised, see error message.\n' + str(error)
        else:
            output = response
        finally:
            return output
    
    def get_interface_info(self, data_type='json'):
        """
        Returns dictionary containing JSON interface information
        """
        dn = '/data/Cisco-IOS-XE-native:native/interface'
        # dn = '/data/Cisco-IOS-XE-native:native/interface/fail'
        headers={'Accept':'application/yang-data+' + data_type}
        return self.get_request(headers, dn)

    def get_interface_ips(self, interface_info, data_type='json'):
        """
        Returns list of interfaces that have a primary IP address
        """
        interface_dict = dict(interface_info)['Cisco-IOS-XE-native:interface']
        interface_list = interface_dict['GigabitEthernet']
        for intf in interface_list:
            if 'ip' not in intf:
                interface_list.remove(intf)
        return json.dumps(interface_info, indent=4)

def main():
    ip = '10.254.0.1'
    # ip = '10.254.0.100'
    port = '443'
    csr = CiscoRestconf(ip, port, 'cisco', 'cisco')
    # csr = CiscoRestconf(ip, port, 'cisco', 'wrong')
    print(csr.get_interface_info())

if __name__ == '__main__':
    main()
