import json
import os
import requests
import pandas


DASH = '-' * os.get_terminal_size().columns
conn_info = pandas.read_csv('conn_info.csv')

# for index, row in conn_info.iteritems():
for index, row in conn_info.iterrows():
    # import pdb; pdb.set_trace()
    ip = row['ip']
    username = row['username']
    password = row['password']
    uri = f'https://{ip}:443/restconf'
    auth = (username, password)

    # response = requests.get(uri, auth=auth)
    response = requests.get(uri, auth=auth, verify=False)
    # print(response.json())
    print(response.content)
    print(DASH)