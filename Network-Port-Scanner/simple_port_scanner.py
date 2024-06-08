import socket
import sys

class PortScanner:
    def __init__(self, ip_address, start_port, end_port):
        self.ip_address = ip_address
        self.start_port = int(start_port)
        self.end_port = int(end_port)
        self.open_ports = []
        self.closed_ports = []

    def scan_ports(self):
        for port in range(self.start_port, self.end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((self.ip_address, port))
            if result == 0:
                self.open_ports.append(port)
            else:
                self.closed_ports.append(port)
            sock.close()

    def print_results(self):
        print(f'Opened Port List : {self.open_ports}')
        print(f'Closed Port List : {self.closed_ports}')

def main():
    if len(sys.argv) != 4:
        print('Usage: python port_scanner.py ip_address start_port end_port')
        sys.exit(1)

    ip_address, start_port, end_port = sys.argv[1:]
    scanner = PortScanner(ip_address, start_port, end_port)
    scanner.scan_ports()
    scanner.print_results()

if __name__ == "__main__":
    main()
    sys.exit(0)
