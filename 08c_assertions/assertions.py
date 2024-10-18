import re
import netmiko

ip_pattern = re.compile(r'(?:(?:25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])\.){3}'
                            r'(?:25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])')

def validate_ip(s):
    if ip_pattern.match(s):
        return True
    return False

def connect(ip, username, password):
    assert validate_ip(ip), 'Invalid IP Address'
    return netmiko.ConnectHandler(ip, username=username,
        password=password, device_type='cisco_ios')

def get_data(conn, command):
    router_output = conn.send_command(command)
    assert 'Invalid input' not in router_output, 'Invalid command: ' + command
    assert len(router_output) > 0, 'No output, check command: ' + command
    return router_output

csr = connect('10.254.0.1', 'cisco', 'cisco')
print(get_data(csr, 'show run | include hostname'))