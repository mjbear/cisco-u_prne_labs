ip = '192.168.0.1'
subnet = '255.255.255.0'

if subnet.endswith('0'):
    subnet_slash_notation = '/24'
    print(ip + subnet_slash_notation)
else:
    print('Subnet slash notation could not to be determined')