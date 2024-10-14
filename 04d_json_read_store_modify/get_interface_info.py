import json
import pprint

with open('interface_info.json') as json_file:
    json_data = json.loads(json_file.read())

    pprint.pprint(json_data)