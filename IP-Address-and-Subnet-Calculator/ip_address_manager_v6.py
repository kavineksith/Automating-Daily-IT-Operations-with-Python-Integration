import ipaddress
import sys


class IPAddressConverter:
    def __init__(self, ip):
        self.ip = ip

    def to_decimal_and_hex(self):
        try:
            decimal_ip = int(ipaddress.ip_address(self.ip))
            hex_ip = hex(decimal_ip)
            return decimal_ip, hex_ip
        except ValueError:
            raise ValueError("Invalid IP address format")

    def to_binary(self):
        try:
            # Convert IPv6 address to packed bytes and then to hexadecimal representation
            binary_ip = ipaddress.IPv6Address(self.ip).exploded
            return binary_ip
        except ValueError:
            raise ValueError("Invalid IP address format")

    def to_decimal(self):
        try:
            decimal_ip = int(ipaddress.IPv6Address(self.ip))
            return decimal_ip
        except ValueError:
            raise ValueError("Invalid IP address format")


class SubnetCalculator:
    def __init__(self, ip, cidr):
        self.ip = ip
        self.cidr = cidr

    def calculate_subnet(self):
        try:
            network = ipaddress.ip_network(self.ip + '/' + str(self.cidr), strict=False)
            return network.network_address, network.netmask
        except ValueError:
            raise ValueError("Invalid IP address or CIDR notation")

    def subnet_mask_binary(self):
        try:
            subnet_mask = ipaddress.ip_network(self.ip + '/' + str(self.cidr), strict=False).netmask
            binary_subnet_mask = bin(int(subnet_mask))[2:]  # Remove '0b' prefix
            return binary_subnet_mask.zfill(128)  # Pad with zeros to ensure 128 bits
        except ValueError:
            raise ValueError("Invalid IP address or CIDR notation")

    def host_mask_calculator(self):
        try:
            host_mask = ipaddress.ip_network(self.ip + '/' + str(self.cidr), strict=False).hostmask
            return host_mask
        except ValueError:
            raise ValueError("Invalid IP address or CIDR notation")

    def host_mask_binary(self):
        try:
            host_mask = self.host_mask_calculator()
            # For IPv6, use 128 bits
            return "{0:0128b}".format(int(host_mask))
        except ValueError:
            raise ValueError("Invalid IP address or CIDR notation")

    def subnet_binary(self):
        try:
            subnet = ipaddress.ip_network(self.ip + '/' + str(self.cidr), strict=False).network_address
            return format(int(subnet), '032b')
        except ValueError:
            raise ValueError("Invalid IP address or CIDR notation")


    def usable_host_ip_range(self):
        try:
            network = ipaddress.ip_network(self.ip + '/' + str(self.cidr), strict=False)
            subnet = network.network_address
            broadcast = network.broadcast_address
            first_usable = subnet + 1
            last_usable = broadcast - 1
            return first_usable, last_usable
        except ValueError:
            raise ValueError("Invalid IP address or CIDR notation")

    def broadcast_address(self):
        try:
            network = ipaddress.ip_network(self.ip + '/' + str(self.cidr), strict=False)
            return network.broadcast_address
        except ValueError:
            raise ValueError("Invalid IP address or CIDR notation")
    
    def total_number_of_hosts(self):
        try:
            network = ipaddress.ip_network(self.ip + '/' + str(self.cidr), strict=False)
            return network.num_addresses
        except ValueError:
            raise ValueError("Invalid IP address or CIDR notation")
    
    def number_of_usable_hosts(self):
        try:
            network = ipaddress.ip_network(self.ip + '/' + str(self.cidr), strict=False)
            check_host_count = network.num_addresses - 2
            if check_host_count <= 0:
                return 0
            else:
                return check_host_count
        except ValueError:
            raise ValueError("Invalid IP address or CIDR notation")
    
    def network_address(self):
        try:
            network = ipaddress.ip_network(self.ip + '/' + str(self.cidr), strict=False)
            return network.network_address
        except ValueError:
            raise ValueError("Invalid IP address or CIDR notation")

    def cidr_notation(self):
        return self.cidr

    def ip_type(self):
        try:
            ip_obj = ipaddress.ip_address(self.ip)
            if isinstance(ip_obj, ipaddress.IPv6Address):
                if ip_obj.is_private:
                    return "Private IPv6"
                elif ip_obj.is_loopback:
                    return "Loopback IPv6"
                elif ip_obj.is_link_local:
                    return "Link-local IPv6"
                elif ip_obj.is_site_local:
                    return 'Site-local IPv6'
                elif ip_obj.is_reserved:
                    return "Reserved IPv6"
                elif ip_obj.is_unspecified:
                    return "APIPA (Automatic Private IP Addressing) IPv6"
                elif ip_obj.is_global:
                    return "Public IPv6"
                elif ip_obj.ipv4_mapped:
                    return 'IPv4-Mapped IPv6'
                else:
                    # For other IPv6 addresses, check if it's multicast
                    if ip_obj.is_multicast:
                        return 'Multicast IPv6'
                    else:
                        return 'Global Unicast IPv6'
            else:
                return "Other IPv6"
        except ValueError:
            raise ValueError("Invalid IP address")

def chunkstring(string, length, delimiter=':'):
    if delimiter in string:
        # IPv6 binary representation with delimiters
        chunks = [string[i:i + length] for i in range(0, len(string), length)]
        return delimiter.join(chunks)
    else:
        # IPv6 binary representation without delimiters
        chunks = [string[i:i + length] for i in range(0, len(string), length)]
        return '.'.join(chunks)

def main():
    while True:
        try:
            ip_address, cidr = input("Enter IPv6 address and CIDR notation (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334/64): ").strip().split('/')
            subnet_calculator = SubnetCalculator(ip_address, int(cidr))

            ip_type = subnet_calculator.ip_type()
            network_address = subnet_calculator.network_address()
            broadcast_address = subnet_calculator.broadcast_address()
            total_hosts = subnet_calculator.total_number_of_hosts()
            usable_hosts = subnet_calculator.number_of_usable_hosts()
            cidr_notation = subnet_calculator.cidr_notation()
            usable_host_range_start, usable_host_range_end = subnet_calculator.usable_host_ip_range()
            usable_host_range_str = f"{usable_host_range_start} - {usable_host_range_end}" if usable_host_range_start and usable_host_range_end else "N/A"

            ip_converter = IPAddressConverter(ip_address)
            binary_ip = ip_converter.to_binary()
            decimal_ip = ip_converter.to_decimal()
            print(f"IPv6 address: {ip_address}")
            print(f"IP Type: {ip_type}")
            print(f"Network Address: {network_address}")
            print(f"Broadcast Address: {broadcast_address}")
            print(f"Total Number of Hosts: {total_hosts}")
            print(f"Number of Usable Hosts: {usable_hosts}")
            print(f"CIDR Notation: /{cidr_notation}")
            print(f"Usable Host IP Range: {usable_host_range_str}")
            print(f"IP address hexadecimal representation: {binary_ip}")
            print(f"IP address decimal representation: {decimal_ip}")

            subnet_calculator = SubnetCalculator(ip_address, cidr)
            subnet, subnet_mask = subnet_calculator.calculate_subnet()
            subnet_mask_bin = subnet_calculator.subnet_mask_binary()
            subnet_bin = subnet_calculator.subnet_binary()
            host_mask = subnet_calculator.host_mask_calculator()
            host_mask_bin = subnet_calculator.host_mask_binary()

            # Convert subnet, subnet mask, and host mask to hexadecimal
            subnet_hex = subnet.exploded
            subnet_mask_hex = subnet_mask.exploded
            host_mask_hex = ipaddress.IPv6Address(int(host_mask_bin, 2)).exploded

            print(f"Subnet: {subnet}/{cidr}")
            print(f"Subnet mask: {subnet_mask}")
            print(f"Host mask: {host_mask}\n")
            
            print(f"Subnet binary: {chunkstring(subnet_bin, 8)}")
            print(f"Subnet mask binary: {chunkstring(subnet_mask_bin, 8)}")
            print(f"Host mask binary: {chunkstring(host_mask_bin, 8)}\n")

            print(f"Subnet hexadecimal representation: {subnet_hex}")
            print(f"Subnet mask hexadecimal representation: {subnet_mask_hex}")
            print(f"Host mask hexadecimal representation: {host_mask_hex}\n")

            print(f"Subnet decimal representation: {int(subnet)}")
            print(f"Subnet mask decimal representation: {int(subnet_mask)}")
            print(f"Host mask decimal representation: {int(host_mask_bin, 2)}\n")
        except ValueError as ve:
            print(ve)
        except KeyboardInterrupt:
            print("\nProcess interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
    sys.exit(0)
