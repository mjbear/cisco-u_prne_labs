import netmiko
import pandas as pd

class cisco():
    
    
    def __init__(self, ip, username=None, password=None, port=22, device_type=None):

        self.conn_data = {
            'ip' : ip,
            'device_type' : device_type,
            'username' : username,
            'password' : password
        }

    def login(self):

        return netmiko.ConnectHandler(**self.conn_data)


class ciscoIOS(cisco):
    
    
    def __init__(self, ip, username=None, password=None, port=22):

        self.conn_data = {
            'ip'            : ip,
            'device_type'   : 'cisco_ios',
            'username'      : username,
            'password'      : password,
            'port'          : 22
        }
        self.conn = super().login()

    def get_ip_int_br(self):
        return self.conn.send_command('sh ip int br')

    def get_ip_arp(self):
        return self.conn.send_command('sh ip arp')
    
    def get_interface_IPs(self):
        self.conn.send_command('')
        return int_IP_dict

    def get_interface_MACs(self):
        pass
        return int_MAC_dict

    def get_ip_route(self, connected=False):
        if connected:
            return self.conn.send_command('sh ip route connected')
        else:
            return self.conn.send_command('sh ip route')

    def get_run_cfg(self, include=''):
        if include:
            return self.conn.send_command('sh run | ' + include)
        else:
            return self.conn.send_command('sh run')

    def commit_changes(self):
        self.conn.send_command('copy running-config startup-config')


csr1vk1 = ciscoIOS('10.254.0.1', username='cisco', password='cisco')
csr1vk1.populate_interface_list()
print(csr1vk1.interface_list)

main()



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

