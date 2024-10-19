import requests


def get_interface_info(to_terminal=False):
    """
    Returns interface information in XML format
    If to_terminal=True prints data instead of returning
    """
    api_root = 'https://10.254.0.1:443/restconf'
    dn = '/data/Cisco-IOS-XE-native:native/interface/'

    response = requests.get(api_root + dn,
        auth=('cisco', 'cisco'),
        verify=False
    )
    if to_terminal == True:
        print(response.content.decode('utf-8'))
    else:
        return response.content

get_interface_info(to_terminal=True)