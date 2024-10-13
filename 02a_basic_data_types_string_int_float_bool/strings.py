import netmiko

# Replace this comment

username = 'cisco'
password = 'cisco'
device_type = 'cisco_ios'
port = '22'

def get_log(ip):
    net_connect = netmiko.ConnectHandler(ip=ip, device_type=device_type,
        username=username, password=password, port=port)
    return net_connect.send_command('show log')

# Replace this comment