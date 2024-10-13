import netmiko

ip_3_octets = '10.254.0'
ip_last_octet = 1

username = 'cisco'
password = 'cisco'
device_type = 'cisco_ios'
port = '22'

def get_ip_int_br(ip):
    net_connect = netmiko.ConnectHandler(ip=ip, device_type=device_type,
        username=username, password=password, port=port)
    return net_connect.send_command('show ip interface brief')

while ip_last_octet <= 3:
    ip = ip_3_octets + str(ip_last_octet)
    ip_int_br = get_ip_int_br(ip)
    print(ip_int_br)
    print('_' * 80)
    ip_last_octet += 1