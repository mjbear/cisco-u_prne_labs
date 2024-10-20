import netmiko


class CiscoIOS():
    """
    This class is designed to connect to a cisco IOS appliance and get various data or 
    issue configuration commands
    """

    def __init__(self, ip, port=22, prompt=False, username=None, 
                        password=None, device_type='cisco_ios'):
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

    def get_run_cfg(self):
        """
        Returns the running-config from the appliance as a string
        """
        running_config = self.conn.send_command('sh run')
        return running_config

    def get_ip_int(self):
        """
        Returns the output from show ip interface as a string
        """
        ip_int = self.conn.send_command('sh ip int')
        return ip_int

    def get_log(self):
        """
        Returns the log from the appliance as a string
        """
        log = self.conn.send_command('sh log')
        return log