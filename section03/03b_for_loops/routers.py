import netmiko

creds = [{
    'ip' : '10.254.0.1',
    'username' : 'cisco',
    'password' : 'cisco',
    'device_type' : 'cisco_ios'
},{
    'ip' : '10.254.0.2',
    'username' : 'cisco',
    'password' : 'cisco',
    'device_type' : 'cisco_ios'
},{
    'ip' : '10.254.0.3',
    'username' : 'cisco',
    'password' : 'cisco',
    'device_type' : 'cisco_ios'
}]

def get_ip_int_br(ip, username, password, device_type):
    username = 'cisco'
    password = 'cisco'
    device_type = 'cisco_ios'

    net_connect = netmiko.ConnectHandler(ip=ip, username=username, 
                        password=password, device_type=device_type)
    ip_int_br = net_connect.send_command('sh ip int br')
    return ip_int_br
