#!/usr/bin/python3

from sys import argv, exit
from netaddr import EUI


try:
    mac = argv[1]
except (IndexError, ValueError):
    print("\nPlease supply an a mac-address as first argument\n")
    exit(2)

print("\nChecking database ...")
macaddress = EUI(mac)
vendor = macaddress.oui.registration().org
print(f"\nVendor: {vendor}\n")
