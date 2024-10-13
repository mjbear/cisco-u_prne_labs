import netmiko

ip_base = '10.254.'
ip_end = 0.1

username = 'cisco'
password = 'cisco'
device_type = 'cisco_ios'
port = '22'

def get_ip_int_br(ip):
    net_connect = netmiko.ConnectHandler(ip=ip, device_type=device_type,
        username=username, password=password, port=port)
    return net_connect.send_command('show ip interface brief')

while ip_end <= 0.3:
    ip = ip_base + str(ip_end)
    ip_int_br = get_ip_int_br(ip)
    print(ip_int_br)
    print('IP int from ' + ip)
    print('_' * 80)
    ip_end += .1
    # fix binary conversion error (ex: 0.2 + 0.1)
    ip_end = round(ip_end, 2)