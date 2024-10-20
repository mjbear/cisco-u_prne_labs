import netmiko
import pprint

username = 'cisco' 
password = 'cisco' 
device_type = 'cisco_ios' 
port = 22 

for ip in ip_tuple:
    net_connect = netmiko.ConnectHandler(ip=ip, device_type=device_type, 
        username=username, password=password, port=port) 
    hostname = net_connect.send_command(
        'sh run | include hostname'
    ).strip() 
    ios_xe_version = net_connect.send_command(
        'sh version | section Cisco IOS XE Software, Version'
    ).strip()
