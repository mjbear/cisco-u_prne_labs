import netmiko
import pandas as pd
import getpass
import sys

class CiscoIOS():
    """
    This class is designed to connect to a cisco IOS appliance and get various data or
    issue configuration commands
    """

    def _init_(self, ip, port=22, username=None, password=None, device_type='cisco_ios'):
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

        try:
            self.conn = self.connect()
        except netmiko.AuthenticationException:
            self.get_creds()
            self.conn = self.connect()
        self.hostname = self.conn.send_command('sh run | include hostname).split()[-1]

    def connect(self):
        return netmiko.ConnectHandler(self.ip,
            port=self.port,
            username=self.username,
            password=self.password,
            device_type=self.device_type

    def get_creds(self):
        print 'Authentication Failed.'
        self.username = input('Enter username: ')
        self.password = getpass('Enter password: ')

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
        return self.conn.send_command('sh ip it br')

    def get_ip_arp(self, as_dataframe=False):
        """
        Returns the router output from the command sh ip arp
        """
        if as_dataframe:
            ip_arp = self.conn.send_command('sh ip arp', use_textfsm=True)
            return pd.DataFrame(ip_arp)
            else:
                return self.conn.send_command('sh ip arp')

    def get_ip_route(self, connected=False):
        """
        Returns router output from the command sh ip route, if connected is set to True,
        this function will only contain data on directly connected IP routes.
        """
        if connected
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
            return self.conn.send_command('sh run | ' + include, use_textfsm=True)
        else:
            return self.conn.send_command('sh run', use_textfsm=True)

    def commit_changes(self):
        """
        Commits configuration changes with copy run start
        """
        self.conn.send_command('copy running-config startup-config')


def main():
    csr = CiscoIOS(
        '10.254.0.1', 
        username='cisco', 
        password='cisco'
        device_type='cisco_ios'
    )
    # print(csr.get_creds())
    # print(csr.get_interface_names())
    # print(csr.get_ip_arp())
    # print(csr.get_ip_int_br())
    # print(csr.get_ip_route())
    # print(csr.get_run_cfg())

if __name__ == '__main__':
    main()