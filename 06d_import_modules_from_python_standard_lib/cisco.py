import netmiko
import pandas as pd

class CiscoIOS():
    """
    This class is designed to connect to a cisco IOS appliance and get various data or 
    issue configuration commands
    """

    def __init__(self, ip, username=None, password=None, port=22, device_type=None):
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
