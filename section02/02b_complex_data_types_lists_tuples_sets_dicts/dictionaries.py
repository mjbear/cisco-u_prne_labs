import netmiko 

net_connect = netmiko.ConnectHandler( 
    ip=csr1kv1_connection_info['ip'],  
    device_type=csr1kv1_connection_info['device_type'], 
    username=csr1kv1_connection_info['username'],  
    password=csr1kv1_connection_info['password'],  
    port=csr1kv1_connection_info['port']) 

print(net_connect.send_command('show run'))