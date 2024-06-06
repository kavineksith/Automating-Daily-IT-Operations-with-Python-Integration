## Documentation: Port Scanner Script

### Overview
The Port Scanner is a Python script designed to scan TCP, UDP, and ICMP ports on a specified IP address within a given range of ports. It utilizes socket programming to establish connections and retrieve information about the status of ports, services running on those ports, and banners where available.

### Usage
To use the Port Scanner script, follow these steps:

1. **Installation**: Ensure you have Python installed on your system. The script is compatible with Python 3.

2. **Execution**: Run the script from the command line with the following command:
   ```
   python port_scanner.py ip_address start_port end_port protocol [output_file]
   ```
   - `ip_address`: The IP address of the target host.
   - `start_port`: The starting port number of the port range to scan.
   - `end_port`: The ending port number of the port range to scan.
   - `protocol`: The protocol to use for scanning. Supported protocols are TCP, UDP, and ICMP.
   - `[output_file]` (optional): Specify an output file to save the scan results in CSV format.

3. **View Results**: The script will display the scan results on the command line, showing the port number, service name, port status, IP address, and banner (if available).

4. **Save Results (Optional)**: If an output file is specified, the script will save the scan results to a CSV file for further analysis.

### Class: PortScanner

The `PortScanner` class serves as the backbone of the Port Scanner script, offering functionalities for initializing the scanner, validating input parameters, scanning various protocols, retrieving service information, and presenting or saving scan results.

### Methods
1. `__init__(self, ip_address, start_port, end_port, protocol)`: Initializes the PortScanner object with the target IP address, port range, and protocol.
   
2. `validate_ip_address(self, ip_address)`: Validates the format of the IP address provided as input.
   
3. `validate_port(self, port)`: Validates the format and range of the port number provided as input.
   
4. `validate_input(self)`: Validates the input parameters provided by the user, including IP address, port numbers, and protocol.
   
5. `scan_ports(self)`: Initiates the port scanning process based on the specified protocol.
   
6. `scan_tcp_ports(self)`: Scans TCP ports within the specified range and retrieves information about open and closed ports along with service names and banners.
   
7. `scan_udp_ports(self)`: Scans UDP ports within the specified range and determines the status of each port.
   
8. `scan_icmp_ports(self)`: Scans ICMP ports and checks for valid ICMP Echo Reply responses.
   
9. `grab_banner_tcp(self, s)`: Retrieves the banner information from a TCP connection.
   
10. `create_icmp_request(self, packet_id, sequence)`: Creates an ICMP request packet.
   
11. `calculate_checksum(self, data)`: Calculates the checksum for ICMP packets.
   
12. `is_icmp_response_valid(self, response, packet_id)`: Validates ICMP Echo Reply responses.
   
13. `get_service_name(self, port, protocol)`: Retrieves the service name associated with a port.
   
14. `print_results(self)`: Prints the scan results to the console.
   
15. `save_results_to_csv(self, file_name)`: Saves the scan results to a CSV file.

### Attributes
- `ip_address`: The target IP address. (Type: str)
- `start_port`: The starting port of the scan range. (Type: int)
- `end_port`: The ending port of the scan range. (Type: int)
- `protocol`: The protocol to use for scanning (TCP, UDP, ICMP). (Type: str)
- `results`: A list to store the scan results. (Type: list)

### Dependencies
The Port Scanner script relies on the following standard Python libraries:
- `socket`: For socket programming to establish connections and perform port scanning.
- `struct`: For packing and unpacking binary data (used for ICMP packet construction).
- `sys`: For system-specific functionality and error handling.
- `csv`: For saving scan results to a CSV file.
- `ipaddress`: For IP address validation.

### Functionality
The Port Scanner script consists of the following components:

- **Input Validation**: Validates the input parameters provided by the user, including IP address, port numbers, and protocol.

- **Port Scanning**: Utilizes socket programming to scan for open ports on the specified host. It supports TCP, UDP, and ICMP protocols and scans ports within the specified range.

- **Banner Grabbing (TCP)**: For TCP ports, the script attempts to grab banners by establishing a connection to the open port and retrieving the service information.

- **Result Presentation**: Presents the scan results in a tabular format on the command line, providing detailed information about each scanned port.

- **Result Saving**: Optionally saves the scan results to a CSV file if an output file is specified by the user.

### Output
The output of the `PortScanner` class methods includes detailed information about the scan results, including port number, service name, port status, IP address, and banner (if available).

### Main Function
The `main()` function parses command-line arguments, initializes the PortScanner object, performs port scans, prints results, and saves results to a CSV file.

### Execution
The script executes the `main()` function when run as the main program, scanning TCP, UDP, and ICMP ports sequentially and saving the results to the specified output file.

### Error Handling
The script incorporates robust error handling to gracefully handle exceptions and unexpected scenarios. It provides informative error messages to guide users in troubleshooting any issues encountered during execution. An also error handling for various exceptions such as KeyboardInterrupt, socket errors, file-related errors, and general exceptions to ensure graceful termination and informative error messages.

### Conclusion
The Port Scanner script provides a versatile tool for network administrators and security professionals to analyze the status of ports on a target system, identify services running on those ports, and gather additional information where available. This enhanced documentation provides comprehensive details about the `PortScanner` class, its attributes, and methods, along with the expected output format. 

## **License**
This project is licensed under the MIT License. See the [LICENSE](https://github.com/kavineksith/Automating-Daily-IT-Operations-with-Python-Integration/blob/main/LICENSE) file for details.

### **Disclaimer:**
Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.