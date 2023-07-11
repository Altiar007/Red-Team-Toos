import socket
from IPy import IP

def scan(targate, rang):
    converted_ip = check_ip(targate)
    print(f'\n[+]Scanning Targate {targate}')
    for port in range(0, int(rang)): # Change the range to required range
        scan_port(targates , port)

# Check if the user Entered an IP Address or a Domain Name & change it to IP address
def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

def scan_port(ipaddress , port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5) # Setting a timeout Limit for a single scan
        sock.connect((ipaddress , port))
        print(f'[+] Port {port} is Open')
    except:
        pass

targates = input('[+] Enter Target(s) to Scan(seprate with ,):')
user_range = input("[+] Enter the Range of Ports(1 onwards): ")
if ',' in targates:
    for ip_add in targates.split(','):
        scan(ip_add.strip(' ') , user_range)
else:
    scan(targates, user_range)