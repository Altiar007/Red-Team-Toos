# Port Scanner

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)

Port Scanner is a simple Python script that scans for open ports of a website or IP address. It allows you to enter either the IP address or the domain name of the website and specify the port range to scan.

## Usage

```bash
python port_scanner.py [-i] [-p]
```
## Installation

1. Clone this repository to your local machine.
```
git clone https://github.com/your_username/port-scanner.git
cd port-scanner
```
2. Install the required Python library.
```
pip install IPy

```
## Arguments
- -i, --ip: Domain name or IP address of the target website. You can use either an IP address or a domain name.
- -p, --port: Port range from 1 to the specified value. The script will scan ports within this range.

## How it Works
The script uses Python's socket library to check for open ports. It supports both IP addresses and domain names as input. If a domain name is provided, the script converts it to an IP address. Then, it scans the specified port range for open ports using the scan_port function.

If a port is open, the script will print "[+] Port {port} is Open" for each open port found.

# Note
The default port range is from 1 to 78. You can change the range in the script as needed by modifying the range value in the scan function.

## Requirements
- Python 3.7 or higher is required to run the script.
- The IPy library is used to handle IP addresses and domain names. 
