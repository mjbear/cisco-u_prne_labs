import re

def mac_eui48_to_eui64(mac_address):
    mac_eui48 = mac_address.replace('.', '')
    mac_eui64 = "fffe".join(mac_eui48[i:i+6] for i in range(0,12,6))
    mac_eui64 = re.sub(r'00', '02', mac_eui64)
    mac_eui64 = ':'.join(mac_eui64[i:i+4] for i in range(0,16,4))
    return mac_eui64

def convert(mac_list):
    eui64_list = []
    for mac in mac_list:
        eui64_list.append(mac_eui48_to_eui64(mac))
    return eui64_list