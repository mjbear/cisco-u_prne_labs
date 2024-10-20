username = 'cisco'
password = 'cisco'
device_type = 'cisco_ios'

net_connect = netmiko.ConnectHandler(ip=ip, username=username, 
                    password=password, device_type=device_type)
sh_ip_int = net_connect.send_command('sh ip int')
print(sh_ip_int)
