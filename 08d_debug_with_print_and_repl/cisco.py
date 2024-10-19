import netmiko
import pandas as pd
import getpass
import sys


class CiscoIOS():
    """
    This class is designed to connect to a cisco IOS appliance and get various data or
    issue configuration commands
    """

    def __init__(self, ip, port=22, username=None, password=None, device_type=None):
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
        self.device_type = 'cisco_ios'

        self.conn = self.connect()
        self.hostname = self.conn.send_command('sh run | include hostname').split()[-1]

    def connect(self):
        conn = netmiko.ConnectHandler(self.ip,
            port=self.port,
            username=self.username,
            password=self.password,
            device_type=self.device_type)
        return conn
    
    def get_creds(self):
        """
        Prompts for username and password. Use in the event of auth failure.
        """
        print('Authentication Failed.')
        self.username = input('Enter username: ')
        self.password = getpass.getpass('Enter password: ')

    def get_interface_names(self):
        """
        Returns list containing interface names from show ip interface brief
        """
        ip_int_br = self.conn.send_command('sh ip int br')
        df = pd.DataFrame(ip_int_br)
        interface_names = df['intf'].to_list()
        return interface_names

    def get_ip_int_br(self):
        """
        Returns the router output from the command sh ip int br
        """
        return self.conn.send_command('sh ip int br')

    def get_ip_arp(self):
        """
        Returns the router output from the command sh ip arp
        """
        ip_arp = self.conn.send_command('sh ip arp', use_textfsm=True)
        return pd.DataFrame(ip_arp)

    def get_interface_ips(self):
        """
        Returns a dictionary containing interface names as keys and the list of IP
        addresses associated with each interface as values.
        """
        data = self.get_ip_arp()
        int_ip_dict = {}
        for interface in data['interface'].unique():
            ip_list = data['address'].loc[data['interface']==interface].to_list()
            int_ip_dict[interface] = ip_list
        return int_ip_dict

    def get_interface_macs(self):
        """
        Returns a dictionary containing interface names as keys and the list of MAC
        addresses associated with each interface as values.
        """
        data = self.get_ip_arp(as_dataframe=True)
        int_mac_dict = {}
        for interface in data['interface'].unique():
            mac_list = data['mac'].loc[data['interface']==interface].to_list()
            int_mac_dict[interface] = mac_list
        return int_mac_dict

    def commit_changes(self):
        """
        commits configuration changes with copy run start
        """
        self.conn.send('copy running-config startup-config')


def main():
    csr = CiscoIOS(
        '10.254.0.1', 
        username='cisco', 
        password='cisco',
        device_type='cisco_ios'
    )
    print(csr.get_interface_names())

if __name__ == '__main__':
    main()