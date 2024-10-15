from netmiko import ConnectHandler
import pandas as pd


def get_router_output(ip, username=None, password=None, port=22,
                      device_type=None, command=None, use_textfsm=True):

    conn = ConnectHandler(
        ip,
        username=username,
        password=password,
        port=port,
        device_type=device_type
    )
    return conn.send_command(command, use_textfsm=True)

sh_ip_arp = get_router_output(
    '10.254.0.1',
    username='cisco',
    password='cisco',
    device_type='cisco_ios',
    command='show ip arp'
)

# print(sh_ip_arp)
df = pd.DataFrame(sh_ip_arp)
interface_names = df['interface'].unique()
# print(interface_names)

for interface in interface_names:
    print(interface)
    print(df['address'].loc[df['interface'] == interface].values)
    print('_' * 80)