#!/usr/bin/env bash

pydoc3 cisco_routers

/usr/bin/env python -c "help('cisco_routers')"

/usr/bin/env python <<EOF
import cisco_routers
csr = cisco_routers.ciscoIOS('10.254.0.1', username='cisco', password='cisco')
print(csr.get_interface_IPs())
print()
print(csr.get_ip_arp(as_dataframe=True))
EOF