"""
This module is designed to interact with Cisco appliances

"""
import netmiko
import pandas as pd

class CiscoIOS():
    """
    This class is designed to connect to a cisco IOS appliance and get various data or
    issue configuration commands
    """

    def __init__(self, ip, port=22, username=None, password=None, device_type=None):
        """
        The constructor creates an instance variable connected to a cisco IOS router
        """
        self.conn = netmiko.ConnectHandler(ip=ip, port=port, username=username,
                password=password, device_type=device_type)
        self.hostname = self.conn.send_command('sh run | include hostname').split()[-1]

    def get_interface_names(self):
        """
        Returns list containing interface names from show ip interface brief
        """
        ip_int_br = self.conn.send_command('sh ip int br', use_textfsm=True)
        df = pd.DataFrame(ip_int_br)
        interface_names = df['intf'].to_list()
        return interface_names

    def get_run_cfg(self):
        """
        Returns running configuration as string from the appliance
        """
        return self.conn.send_command('sh run')

class CiscoRestconf():
    """
    This class is designed to query and manage a Cisco appliance via restconf
    """
    def __init__(self, ip, username, password, port=443):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = str(port)

    def get_interface_info(self, data_type='json'):
        """
        Returns dictionary containing JSON interface information
        """
        url_base = ''
        dn = '/restconf/data/Cisco-IOS-XE-native:native/interface/'
        pass

    def get_interface_ips(self, interface_info, data_type='json'):
        """
        Returns list of interfaces that have a primary IP address
        """
        pass
