### description
minimal python script which gives information about ipv4 and ipv6 networks, 

### usage
network address (in cidr) notation has to be given as argument
script outputs information like the first and last usable ip address, the network address, with and without cidr

```
./ipcalc.py -h
usage: ipcalc.py [-h] [-4 | -6] network_address

Calculate IP subnet information for IPv4 or IPv6. Defaults to IPv6 if no version flag is specified.

positional arguments:
  network_address  The IP address and prefix in CIDR notation (e.g., 192.168.1.0/24 or 2001:db8::/32).

options:
  -h, --help       show this help message and exit
  -4               Specify IPv4 address calculation.
  -6               Specify IPv6 address calculation.
```

### example output
```
./ipcalc.py -6 2001:abc::abc/46
  IP Version:           6
  Network (CIDR):       2001:abc::/46
  Network Address:      2001:abc::
  First usable Address: 2001:abc::1
  Last usable Address:  2001:abc:3:ffff:ffff:ffff:ffff:ffff
  Total Addresses:      4,835,703,278,458,516,698,824,704
```
