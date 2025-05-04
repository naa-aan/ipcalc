#!/usr/bin/env python3

import ipaddress
import argparse

def calculate_ipv4_subnet_info(ipv4_address_with_prefix):
    """
    Calculates and returns core information about an IPv4 subnet,
    aligned with IPv6 output structure.

    Args:
        ipv4_address_with_prefix: A string representing the IPv4 address
                                  and prefix length in CIDR notation (e.g.,
                                  "192.168.1.0/24").

    Returns:
        A dictionary containing subnet information, or an error message
        string if the input is invalid.
    """
    try:
        network = ipaddress.IPv4Network(ipv4_address_with_prefix, strict=False)

        info = {
            "version": 4,
            "Input CIDR": str(network.with_prefixlen),
            "Network Address": str(network.network_address),
            "Broadcast Address": str(network.broadcast_address),
            "First usable Address": str(network[1]),
            "Last usable Address":  str(network[-2]),
            "Total Addresses": network.num_addresses
        }

        return info

    except ValueError as e:
        return f"Error: Invalid IPv4 address or prefix. {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


def calculate_ipv6_subnet_info(ipv6_address_with_prefix):
    """
    Calculates and returns core information about an IPv6 subnet.

    Args:
        ipv6_address_with_prefix: A string representing the IPv6 address
                                  and prefix length in CIDR notation (e.g.,
                                  "2001:db8::1/32").

    Returns:
        A dictionary containing subnet information, or an error message
        string if the input is invalid.
    """
    try:
        network = ipaddress.IPv6Network(ipv6_address_with_prefix, strict=False)

        # network address
        network_address = network.network_address

        # In IPv6, network[0] is the network address, and network[-1] is the
        # last address in the subnet (broadcast equivalent). Both are generally usable.
        first_address = network[1]
        last_address = network[-1]

        total_addresses = network.num_addresses

        info = {
            "version": 6,
            "Input CIDR": str(network.with_prefixlen),
            "Network Address": str(network.network_address),
            "First usable Address": str(network[1]),
            "Last usable Address":  str(network[-1]),
            "Total Addresses": network.num_addresses
        }

        return info

    except ValueError as e:
        return f"Error: Invalid IPv6 address or prefix. {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


def print_subnet_info(subnet_info):
    """
    Prints the calculated subnet information from a dictionary of labels and values.

    Args:
        subnet_info: A dictionary where keys are descriptive strings and
                     values are the information to print.
    """

    # Determine the maximum width needed for the labels for alignment
    max_label_width = 0
    for label in subnet_info.keys():
        if len(label) > max_label_width:
            max_label_width = len(label)

    # Print the remaining key-value pairs with padding
    for label, value in subnet_info.items():
        # Use string formatting to left-align the label and pad it
        # to the maximum width, followed by a colon and space.
        # Adding 2 for the initial indentation spaces, and 2 for ": "
        formatted_label = f"  {label}:".ljust(max_label_width + 4)

        # Format large numbers with commas
        if isinstance(value, int):
             print(f"{formatted_label}{value:,}")
        else:
             print(f"{formatted_label}{value}")


def main():
    """
    Main function to get user input and display subnet information
    for IPv4 or IPv6 using argparse.
    """
    parser = argparse.ArgumentParser(description="Calculate IP subnet information for IPv4 or IPv6. Defaults to IPv6 if no version flag is specified.")

    version_group = parser.add_mutually_exclusive_group()
    # Use 'dest' to provide valid attribute names
    version_group.add_argument("-4", action="store_true", dest="is_ipv4", help="Specify IPv4 address calculation.")
    version_group.add_argument("-6", action="store_true", dest="is_ipv6", help="Specify IPv6 address calculation.")

    parser.add_argument("network_address", help="The IP address and prefix in CIDR notation (e.g., 192.168.1.0/24 or 2001:db8::/32).")

    args = parser.parse_args()

    ip_input = args.network_address
    subnet_info = None # Initialize subnet_info

    # Check if neither flag was set, and if so, default to IPv6
    if not args.is_ipv4 and not args.is_ipv6:
        args.is_ipv6 = True # Default to IPv6

    if args.is_ipv4:
        subnet_info = calculate_ipv4_subnet_info(ip_input)
    elif args.is_ipv6:
        subnet_info = calculate_ipv6_subnet_info(ip_input)

    if isinstance(subnet_info, str):
        print(subnet_info) # Print error message
    elif subnet_info: # Check if subnet_info is not None
        print_subnet_info(subnet_info) # Call the simplified print function


if __name__ == "__main__":
    main()
