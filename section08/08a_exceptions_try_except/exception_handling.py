import netmiko
import getpass

ip = '10.254.0.1'
username = 'cisco'
password = 'wrong_password'
device_type = 'cisco_ios'

# csr = netmiko.ConnectHandler(ip=ip, username=username,
#     password=password, device_type=device_type)

try:
    csr = netmiko.ConnectHandler(ip=ip, username=username,
        password=password, device_type=device_type)
except netmiko.ssh_exception.NetmikoAuthenticationException:
    print('Authentication Failed.')
    username = input('Enter username: ')
    password = getpass.getpass('Enter password: ')
    csr = netmiko.ConnectHandler(ip=ip, username=username,
        password=password, device_type=device_type)
    print(csr.send_command('show ip int br'))