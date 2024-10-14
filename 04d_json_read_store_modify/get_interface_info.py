import json
import pprint

with open('interface_info.json') as json_file:
    json_data = json.loads(json_file.read())

    # pprint.pprint(json_data)
    
    # create pointer variable
    interface_list = json_data['Cisco-IOS-XE-native:interface']['GigabitEthernet']
    for intf in interface_list:
        if 'ip' not in intf:
            interface_list.remove(intf)

    # has only 2-4 since we removed number GigabitEthernet1
    pprint.pprint(json_data)