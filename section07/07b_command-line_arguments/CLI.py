class CiscoIOS_CLI():

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            'ip', 
            type=str, 
            help='IP address, SSH endpoint'
        )
        parser.add_argument(
            '--port', 
            type=int, 
            default=22, 
            help='Port for connection'
        )
        parser.add_argument(
            '-u', '--username', 
            type=str, 
            help='Username for SSH connection'
        )
        parser.add_argument(
            '-p', '--password', 
            type=str, 
            help='Password for SSH connection'
        )
        parser.add_argument(
            '--device_type', 
            type=str, 
            default='cisco_ios', 
            help='Device type of appliance'
        )
        
        args = parser.parse_args()

        ip = args.ip
        port = args.port
        username = args.username
        password = args.password
        device_type = args.device_type
        self.conn = netmiko.ConnectHandler(ip=ip, port=port, username=username,
            password=password, device_type=device_type)
        print(self.conn.send_command('show run | include hostname'))

    def get_interface_list(self):
        return super().get_interface_list()

    def get_run_int(self):
        return super().get_run_int()