**Port Scanner Documentation**

**Introduction:**

This document provides a comprehensive overview of a Python script designed for network port scanning. The script utilizes the socket library to scan for open and closed ports within a specified range on a given IP address. This tool can be used for network analysis, security auditing, and troubleshooting purposes.

**Script Overview:**

The provided script, named `port_scanner.py`, is a command-line utility that takes three arguments: IP address, start port, and end port. It then scans the specified range of ports on the given IP address and outputs the list of open and closed ports.

**Requirements:**

- Python 3.x
- socket library (included in Python standard library)

**Usage:**

To execute the script, follow the usage pattern below:

```
python port_scanner.py <ip_address> <start_port> <end_port>
```

Where:
- `<ip_address>`: The IP address of the target machine to scan.
- `<start_port>`: The starting port number of the port range to scan.
- `<end_port>`: The ending port number of the port range to scan.

**Example:**

```
python port_scanner.py 192.168.1.100 1 1024
```

**Script Functionality:**

The script performs the following actions:

1. Parses command-line arguments to extract the IP address, start port, and end port.
2. Creates an instance of the `PortScanner` class with the provided arguments.
3. Initiates a port scanning process using the `scan_ports()` method of the `PortScanner` class.
4. Checks each port in the specified range for openness using the `socket` library.
5. Stores the results (open and closed ports) in separate lists.
6. Prints the list of open and closed ports using the `print_results()` method of the `PortScanner` class.

**PortScanner Class:**

The `PortScanner` class encapsulates the functionality required for port scanning. It includes the following attributes and methods:

- **Attributes:**
  - `ip_address`: IP address of the target machine.
  - `start_port`: Starting port number of the port range.
  - `end_port`: Ending port number of the port range.
  - `open_ports`: List to store open ports.
  - `closed_ports`: List to store closed ports.

- **Methods:**
  - `__init__(self, ip_address, start_port, end_port)`: Initializes the PortScanner object with the provided IP address, start port, and end port.
  - `scan_ports(self)`: Scans the ports within the specified range and populates the `open_ports` and `closed_ports` lists accordingly.
  - `print_results(self)`: Prints the lists of open and closed ports.

**Conclusion:**

The `port_scanner.py` script provides a simple yet effective solution for network port scanning tasks. By leveraging Python's socket library, it enables users to identify open and closed ports on a target machine within a specified port range. This tool can be utilized by network administrators, security professionals, and system analysts to assess network security and diagnose connectivity issues.

Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.