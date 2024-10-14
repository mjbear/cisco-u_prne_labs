# ip_list = []

def populate_ip_list(ip_base, ip_range):
    ip_list = []
    for n in ip_range:
        ip_addr = ip_base + str(n)
        ip_list.append(ip_addr)
    return ip_list

ip_list = populate_ip_list('10.0.0.', range(1,33))
print(ip_list)