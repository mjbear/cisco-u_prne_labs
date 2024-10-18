import requests

dn = '/restconf/data/Cisco-IOS-XE-native:native/interface/'
headers = {'Accept': 'application/yang-data+json'}
# response = requests.get('http://10.254.0.1:443/' + dn,
response = requests.get('https://10.254.0.1:443/' + dn,
    # add headers
    headers=headers,
    auth=('cisco', 'cisco'),
    verify=False)
data_dict = response.json()
# print(response.status_code)
# print(response.reason)
# print(response.content)
print(data_dict)