import psutil

# Get a dictionary of network interfaces and their addresses
networks = psutil.net_if_addrs()

# Print available network interfaces and their details
for interface, addresses in networks.items():
    print(f"Interface: {interface}")
    for address in addresses:
        print(f"  Address Family: {address.family.name}")
        print(f"  Address: {address.address}")
        if address.netmask:
            print(f"  Netmask: {address.netmask}")
        if address.broadcast:
            print(f"  Broadcast: {address.broadcast}")
        if address.ptp:
            print(f"  PTP: {address.ptp}")
    print()
