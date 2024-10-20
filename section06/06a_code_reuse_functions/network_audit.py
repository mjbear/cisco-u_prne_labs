import netmiko

net_connect = netmiko.ConnectHandler(ip='10.254.0.1', device_type='cisco_ios',
    username='cisco', password='cisco', port=22)
print(net_connect.send_command('sh ip int br'))