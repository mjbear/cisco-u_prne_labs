import netmiko

username = 'cisco' 
password = 'cisco' 
device_type = 'cisco_ios' 
port = 22 
    
for ip in ip_list:
    net_connect = netmiko.ConnectHandler(ip=ip, device_type=device_type, 
        username=username, password=password, port=port)
    output = net_connect.send_command('show ip interface brief')
