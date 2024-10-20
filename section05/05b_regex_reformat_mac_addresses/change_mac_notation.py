def change_notation(mac_address, format):
    mac_string = mac_address.replace('.', '')
    mac_string = format.join(mac_string[i:i+2] for i in range(0,12,2))
    return mac_string