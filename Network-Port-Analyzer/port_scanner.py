import socket
import struct
import sys
import csv
from pathlib import Path


class PortScanner:
    def __init__(self, ip_address, start_port, end_port):
        self.ip_address = ip_address
        self.start_port = int(start_port)
        self.end_port = int(end_port)
        self.results = []

    def scan_tcp_ports(self):
        try:
            for port in range(self.start_port, self.end_port + 1):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3)
                result = s.connect_ex((self.ip_address, port))
                if result == 0:
                    service = self.get_service_name(port, 'tcp')
                    banner = self.grab_banner_tcp(s)
                    self.results.append((port, service, "Open", self.ip_address, banner))
                else:
                    self.results.append((port, "Unknown", "Closed", self.ip_address, "Unknown"))
                s.close()
        except KeyboardInterrupt:
            print("Operation interrupted by user.")
            sys.exit(1)
        except socket.gaierror:
            print("IP address couldn't be resolved.")
            sys.exit(1)
        except socket.error:
            print("Couldn't connect to server.")
            sys.exit(1)

    def grab_banner_tcp(self, s):
        try:
            # Receive up to 1024 bytes of data from the socket
            banner = s.recv(1024)
            if banner:
                return banner.decode().strip('\n').strip('\r').splitlines()[0]  # Only return the first line
            else:
                return "Unknown"
        except ConnectionError as e:
            print(f"Connection error occurred: {e}")
            sys.exit(1)
        except TimeoutError as e:
            print(f"Timeout error occurred: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            sys.exit(1)

    def scan_udp_ports(self):
        try:
            for port in range(self.start_port, self.end_port + 1):
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.settimeout(2)
                s.sendto(b'', (self.ip_address, port))
                try:
                    response, _ = s.recvfrom(1024)
                    service = self.get_service_name(port, 'udp')
                    self.results.append((port, service, "Open", self.ip_address, "Unknown"))
                except socket.timeout:
                    self.results.append((port, "Unknown", "Closed", self.ip_address, "Unknown"))
                finally:
                    s.close()
        except KeyboardInterrupt:
            print("Operation interrupted by user.")
            sys.exit(1)
        except socket.gaierror:
            print("IP address couldn't be resolved.")
            sys.exit(1)
        except socket.error:
            print("Couldn't connect to server.")
            sys.exit(1)

    def scan_icmp_ports(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            s.settimeout(2)
            packet_id = 12345  # Random packet ID
            sequence = 1  # Sequence number
            icmp_request = self.create_icmp_request(packet_id, sequence)
            s.sendto(icmp_request, (self.ip_address, 0))  # Sending to port 0 as ICMP doesn't have ports
            try:
                response, _ = s.recvfrom(1024)
                if self.is_icmp_response_valid(response, packet_id):
                    self.results.append(("ICMP", "Echo Reply", "Open", self.ip_address, "Unknown"))
                else:
                    self.results.append(("ICMP", "No response", "Closed", self.ip_address, "Unknown"))
            except socket.timeout:
                self.results.append(("ICMP", "No response", "Closed", self.ip_address, "Unknown"))
            finally:
                s.close()
        except KeyboardInterrupt:
            print("Operation interrupted by user.")
            sys.exit(1)
        except socket.gaierror:
            print("IP address couldn't be resolved.")
            sys.exit(1)
        except socket.error:
            print("Couldn't connect to server.")
            sys.exit(1)

    def create_icmp_request(self, packet_id, sequence):
        # ICMP Echo Request packet structure: Type (8 bits), Code (8 bits), Checksum (16 bits), Identifier (16 bits),
        # Sequence Number (16 bits)
        icmp_type = 8  # ICMP Echo Request type
        icmp_code = 0  # ICMP Echo Request code
        icmp_checksum = 0  # Placeholder for checksum calculation
        icmp_identifier = packet_id
        icmp_seq_number = sequence
        # Constructing the packet
        icmp_header = struct.pack("!BBHHH", icmp_type, icmp_code, icmp_checksum, icmp_identifier, icmp_seq_number)
        icmp_checksum = self.calculate_checksum(icmp_header)
        # Reconstructing the packet with correct checksum
        icmp_header = struct.pack("!BBHHH", icmp_type, icmp_code, icmp_checksum, icmp_identifier, icmp_seq_number)
        return icmp_header

    def calculate_checksum(self, data):
        # ICMP uses a checksum calculated over the ICMP header and data, with the checksum field itself zeroed out
        # Checksum is calculated by summing up 16-bit words and taking the one's complement
        checksum = 0
        for i in range(0, len(data), 2):
            word = (data[i] << 8) + (data[i + 1])
            checksum += word
        checksum = (checksum >> 16) + (checksum & 0xFFFF)
        checksum = ~checksum & 0xFFFF
        return checksum

    def is_icmp_response_valid(self, response, packet_id):
        # Validate ICMP Echo Reply response by checking packet ID
        icmp_type = response[20]  # ICMP Type is at offset 20
        icmp_code = response[21]  # ICMP Code is at offset 21
        if icmp_type == 0 and icmp_code == 0:  # ICMP Type 0 (Echo Reply), Code 0
            received_packet_id = response[24] << 8 | response[25]  # Packet ID is at offset 24-25
            if received_packet_id == packet_id:
                return True
        return False

    def get_service_name(self, port, protocol):
        try:
            service_name = socket.getservbyport(port, protocol)
            return service_name
        except OSError:
            return "Unknown"
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)

    def print_results(self):
        print("Results:")
        print("{:<10} {:<20} {:<15} {:<15} {:<50}".format("Port", "Service", "Port Status", "IP Address", "Banner"))
        for result in self.results:
            print("{:<10} {:<20} {:<15} {:<15} {:<50}".format(*result))

    def save_results_to_csv(self, file_name):
        try:
            file_path = Path(file_name)
            with open(file_path, 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(["Port", "Service", "Port Status", "IP Address", "Banner"])
                for result in self.results:
                    csv_writer.writerow(result)
            print(f"Results saved to {file_name}")
        except FileNotFoundError:
            print(f"Error: File not found: {file_name}")
        except PermissionError:
            print(f"Error: Permission denied for file: {file_name}")
        except Exception as e:
            print(f"An error occurred while saving results to CSV: {str(e)}")


def main():
    if len(sys.argv) != 5:
        print('Usage: python port_scanner.py ip_address start_port end_port output_file')
        sys.exit(1)

    ip_address, start_port, end_port, output_file = sys.argv[1:]
    scanner = PortScanner(ip_address, start_port, end_port)
    try:
        scanner.scan_tcp_ports()
        scanner.scan_udp_ports()
        scanner.scan_icmp_ports()
        scanner.print_results()
        scanner.save_results_to_csv(output_file)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
    sys.exit(0)
