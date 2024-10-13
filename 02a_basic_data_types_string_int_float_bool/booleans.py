import netmiko

ip_list = [
    '10.254.0.1',
    '10.254.0.2',
    '10.254.0.3',
]

username = 'cisco'
password = 'cisco'
device_type = 'cisco_ios'
port = '22'

def get_ip_int_br(ip):
    net_connect = netmiko.ConnectHandler(ip=ip, device_type=device_type,
        username=username, password=password, port=port)
    return net_connect.send_command('show ip interface brief')

ip_3_octets = '10.254.0.'
ip_last_octet = 1

while ip_last_octet <= 3:
    ip = ip_3_octets + str(ip_last_octet)
    ip_int_br = get_ip_int_br(ip)
    print('IP interface from ' + ip)
    print(ip_int_br)
    print('-' * 80)
    ip_last_octet += 1
