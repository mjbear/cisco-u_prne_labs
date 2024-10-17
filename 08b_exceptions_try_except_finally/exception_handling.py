import os
import requests

requests.packages.urllib3.disable_warnings()

test_uri = 'https://10.254.0.1:443/restconf/'
# test_uri = 'https://10.254.0.1:443/restconf/fail/'
# test_uri = 'https://10.254.0.100:443/restconf/'
dash = '-' * os.get_terminal_size().columns
print(dash)

try:
    response = requests.get(test_uri, auth=('cisco', 'cisco'), verify=False)
    # print(response.status_code)
    response.raise_for_status()
except requests.ConnectionError as error:
    output = error
except requests.HTTPError as error:
    output = error
else:
    output = response.content
finally:
    print(output)
    print(dash)