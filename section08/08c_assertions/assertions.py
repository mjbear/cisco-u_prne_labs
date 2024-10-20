import re
import netmiko

ip_pattern = re.compile(r'(?:(?:25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])\.){3}'
                            r'(?:25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])')
