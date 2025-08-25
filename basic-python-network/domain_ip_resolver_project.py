import socket  # Import the socket module, which provides low-level networking capabilities

# Function to get hostnames
def get_hostnames():
    hosts = []  # Initialize empty list to store hostnames
    while True:  # Infinite loop to keep getting hostnames until the user decides to stop
        host = input("Enter a hostname or press enter to finish: ")
        if not host:  # If user didn't enter a hostname and just hit enter, break the loop
            break
        hosts.append(host)  # Add the entered hostname to the hosts list
    return hosts  # Return the list of entered hostnames

# Function to resolve hostnames to IP addresses
def resolve_hostnames(hosts):
    ip_addresses = []  # Initialize empty list to store resolved IP addresses
    for i, host in enumerate(hosts):  # Enumerate over the list of hostnames
        try:
            ip = socket.gethostbyname(host)  # Try to resolve each hostname to an IP address
            ip_addresses.append(ip)  # If successful, add the IP address to the ip_addresses list
            print(f"{i}: {host}")
        except socket.gaierror:  # If hostname resolution fails, handle the exception
            ip_addresses.append(None)  # Add None to the ip_addresses list for failed resolutions
            print(f"{i}: {host} - error resolving hostname")
    return ip_addresses  # Return the list of resolved IP addresses

# Function to look up a specific hostname's IP address based on user selection
def lookup_ip(ip_addresses, hosts):
    while True:  # Infinite loop to keep getting user selection until the user decides to stop
        selection = input("Enter the index of the hostname you want to look up (or press enter to quit): ")
        if not selection:  # If user didn't enter an index and just hit enter, break the loop
            break
        try:
            selection = int(selection)  # Try to convert user's selection to an integer
            ip = ip_addresses[selection]  # Get the corresponding IP address from the list
            if ip is None:  # If the IP address is None (i.e., resolution failed earlier)
                print(f"{hosts[selection]} - error resolving hostname")
            else:  # If an IP address was successfully retrieved
                print(f"{hosts[selection]} - {ip}")
        except IndexError:  # If user entered an index that's out of the range of the list
            print("Error: wrong index")
        except ValueError:  # If user entered something other than a number
            print("Error: not a number")

def main():
    hosts = get_hostnames()  # Get hostnames from the user
    ip_addresses = resolve_hostnames(hosts)  # Resolve those hostnames to IP addresses
    lookup_ip(ip_addresses, hosts)  # Let the user look up specific hostname's IP address

# If the script is being run (as opposed to being imported), call the main() function
if __name__ == "__main__":
    main()
