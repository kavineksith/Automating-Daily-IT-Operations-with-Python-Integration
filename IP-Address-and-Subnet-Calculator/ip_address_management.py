import sys
from ip_address_manager_v4 import main as v4
from ip_address_manager_v6 import main as v6


def select_ip_version():
    while True:
        try:
            ip_version = input("Select IP version (IPv4 or IPv6): ").strip().lower()
            if ip_version.lower() == 'exit':
                print("Exiting the program.")
                sys.exit(0)
            elif ip_version not in ['ipv4', 'ipv6']:
                print("Invalid input. Please enter 'IPv4', 'IPv6', or 'exit'.")
                continue
            else:
                return ip_version
        except ValueError:
            print("Invalid input. Please enter 'IPv4', 'IPv6', or 'exit'.")


def main():
    while True:
        try:
            ip_version = select_ip_version()
            if ip_version.lower() == "ipv4":
                v4()
            elif ip_version.lower() == "ipv6":
                v6()
            else:
                print("Can't continue the process...")
        except KeyboardInterrupt:
            print("\nProcess interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
    sys.exit(0)
