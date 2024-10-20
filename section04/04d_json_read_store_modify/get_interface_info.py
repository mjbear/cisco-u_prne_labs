import json
import pprint
from textwrap import indent

with open('interface_info.json') as json_file:
    json_data = json.loads(json_file.read())

    # pprint.pprint(json_data)
    
    # create pointer variable
    interface_list = json_data['Cisco-IOS-XE-native:interface']['GigabitEthernet']
    for intf in interface_list:
        if 'ip' not in intf:
            interface_list.remove(intf)

    # has only 2-4 since we removed number GigabitEthernet1
    # pprint.pprint(json_data)

    formatted_json_data = json.dumps(json_data, indent=4)
    with open('interfaces_with_IPs.json', 'w') as json_file:
        print(formatted_json_data, file=json_file)