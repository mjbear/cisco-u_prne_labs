import netmiko
import pandas as pd
import getpass
import sys

class CiscoIOS():
    """
    This class is designed to connect to a cisco IOS appliance and get various data or
    issue configuration commands
    """

    def __init__(self, ip, port=22, username=None, password=None, device_type='cisco_ios'):
        """
        Establishes connection to target device.

        :param str IP:              IP address of target device.
        :param int port:            port for connection
        :param str username:        username for authentication
        :param str password:        password for authentication
        :param str device_type:     should not change, class is designed for Cisco IOS
        """
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.device_type = device_type

        self.conn = self.connect()

        self.hostname = self.conn.send_command('sh run | include hostname').split()[-1]

    def connect(self):
        return netmiko.ConnectHandler(self.ip,
            port=self.port,
            username=self.username,
            password=self.password,
            device_type=self.device_type
        )

    def get_creds(self):
        print('Authentication Failed.')
        self.username = input('Enter username: ')
        self.password = getpass.getpass('Enter password: ')

    def get_interface_names(self):
        """
        Returns list containing interface names from show ip interface brief
        """
        ip_int_br = self.conn.send_command('sh ip int br', use_textfsm=True)
        df = pd.DataFrame(ip_int_br)
        interface_names = df['intf'].to_list()
        return interface_names

    def get_ip_int_br(self):
        """
        Returns the router output from the command sh ip int br
        """
        return self.conn.send_command('sh ip int br')

    def get_ip_arp(self, as_dataframe=False):
        """
        Returns the router output from the command sh ip arp
        """
        if as_dataframe:
            ip_arp = self.conn.send_command('sh ip arp', use_textfsm=True)
            return pd.DataFrame(ip_arp)
        else:
            return self.conn.send_command('sh ip arp')

    def get_interface_IPs(self):
        """
        Returns a dictionary containing interface names as keys and the list of IP
        addresses associated with each interface as values.
        """
        df = self.get_ip_arp(as_dataframe=True)
        interface_names = df['interface'].unique()
        int_IP_dict = {}
        for interface in interface_names:
            ip_list = df['address'].loc[df['interface']==interface].to_list()
            int_IP_dict[interface] = ip_list
        return int_IP_dict

    def get_interface_MACs(self):
        """
        Returns a dictionary containing interface names as keys and the list of MAC
        addresses associated with each interface as values.
        """
        df = self.get_ip_arp(as_dataframe=True)
        interface_names = df['interface'].unique()
        int_MAC_dict = {}
        for interface in interface_names:
            mac_list = df['mac'].loc[df['interface']==interface].to_list()
            int_MAC_dict[interface] = mac_list
        return int_MAC_dict

    def get_ip_route(self, connected=False):
        """
        Returns router output from the command sh ip route, if connected is set to True,
        this function will only contain data on directly connected IP routes.
        """
        if connected:
            return self.conn.send_command('sh ip route connected')
        else:
            return self.conn.send_command('sh ip route')

    def get_run_cfg(self, include=''):
        """
        Returns router output from the command sh run, if include has value other than
        an empty string, this function will pipe sh run command to "include" followed by
        the value of include.
        """
        if include:
            return self.conn.send_command('sh run | ' + include)
        else:
            return self.conn.send_command('sh run')

    def commit_changes(self):
        """
        Commits configuration changes with copy run start
        """
        self.conn.send_command('copy running-config startup-config')

    def ssh_exception_output(self):
        print('\n',
                '*** SSH Exception Raised ***'.center(80),
                '\n',
                'Ensure you are using the correct connection information.'.center(80),
                '\n'
            )
