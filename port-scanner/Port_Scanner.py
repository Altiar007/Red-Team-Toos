import socket, argparse, sys
from IPy import IP
def scan(targate, rang):
    converted_ip = check_ip(targate)
    print(f'\n[+]Scanning Target {targate}')
    for port in range(78, int(rang)): # Change the range to required range
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

title = """
 ______                      ______                                     
(_____ \             _      / _____)                                    
 _____) )__   ____ _| |_   ( (____   ____ _____ ____  ____  _____  ____ 
|  ____/ _ \ / ___|_   _)   \____ \ / ___|____ |  _ \|  _ \| ___ |/ ___)
| |   | |_| | |     | |_    _____) | (___/ ___ | | | | | | | ____| |    
|_|    \___/|_|      \__)  (______/ \____)_____|_| |_|_| |_|_____)_|
"""

custom_help = """
A Program to Fetch Open Ports of a Site. 
You can enter either IP Address of the website or you can use the Domain Name.
The Ports will be scanned from 1 to the the number specified by you.
"""

print(title)
custom_usage = "Port_Scanner.py [-i] [-p]"

if __name__ == '__main__':
    praser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(usage = custom_usage, add_help=False)
    praser.add_argument('--ip', '-i' ,type = str, default= "", help = "Domain Name/ IP Address of Target")
    praser.add_argument('--port', '-p', type = int, default= "", help = "Port Range(0 to Specified Value)")
    parser.add_argument('-h', '--help', action='store_true', help=print(custom_help))
    args = praser.parse_args()
    if not any(vars(args).values() or args.help or args.h):
        print(help)

targates = args.ip
user_range = args.port
scan(targates, user_range)