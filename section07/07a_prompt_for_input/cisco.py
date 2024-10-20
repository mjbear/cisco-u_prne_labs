import netmiko
import pandas as pd


class ciscoIOS():
    """
    This class is designed to connect to a cisco IOS appliance and get various data or 
    issue configuration commands
    """

    def __init__(self, ip, username=None, password=None, 
                port=22, device_type='cisco_ios'):
        """
        Establishes connection to target device.
        
        :param str ip:              ip address of target device.
        :param int port:            port for connection
        :param str username:        username for authentication
        :param str password:        password for authentication
        :param str device_type:     should not change, class is designed for Cisco IOS
        """
        self.conn = netmiko.ConnectHandler(ip=ip, port=port, username=username,
                    password=password, device_type=device_type)
        _ = self.conn.send_command('sh run | include hostname')
        self.hostname = _.split()[-1]

    def get_interface_list(self):
        """
        Returns list containing interface names from show ip interface brief
        """
        ip_int_br = self.conn.send_command('sh ip int br', use_textfsm=True)
        df = pd.DataFrame(ip_int_br)
        interface_names = df['intf'].to_list()
        return interface_names