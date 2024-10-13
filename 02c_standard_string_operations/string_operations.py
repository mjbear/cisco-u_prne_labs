connection_info = '10.254.0.1,cisco,cisco'

print(connection_info)
print()

# split
connection_info_list = connection_info.split(',')
print(connection_info_list)
print()

n = 1
ip_three_octets = '10.254.0.'
# concatenate
print(ip_three_octets + str(n))
print(ip_three_octets + str(n + 1))
print(ip_three_octets + str(n + 2))
print()

# f-string (format string)
ip = '10.254.0.1'
device_type = 'cisco_ios'
print(f'The router at {ip} is running {device_type}')
print()

# using escape characters to format a string
print(f"Connection Info\n{'_'*30}\nIP:\t\t{ip}\nDevice Type:\t{device_type}")
print()

print(device_type.upper())
print()
print(device_type.replace('_', ' '))
print(device_type.upper().replace('_', ' '))
