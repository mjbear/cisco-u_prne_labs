#!/usr/bin/env python
import netmiko
import paramiko

device = {
    'ip': '10.254.0.1',
    'username': 'cisco',
    # 'password': 'cisco',
    'device_type': 'cisco_ios',
    'port': 22,
}

# conn = netmiko.ConnectHandler(**device)

try:
    conn = netmiko.ConnectHandler(**device)
except paramiko.ssh_exception.SSHException as e:
    msg = f'Authentication issue: {e}'
else:
    msg = conn.send_command('show run | include hostname')
finally:
    print(msg)

try:
    conn.disconnect()
except NameError:
    pass