import re
import netmiko

ip = '10.254.0.1'
username = 'cisco'
password = 'cisco'
device_type = 'cisco_ios'
port = '22'

net_connect = netmiko.ConnectHandler(ip=ip, device_type=device_type,
    username=username, password=password, port=port)
show_arp = net_connect.send_command('show arp')
print(show_arp)

mac_list = re.findall(r'((?:[0-9a-f]{4}\.){2}[0-9a-f]{4})', show_arp)
print(mac_list)