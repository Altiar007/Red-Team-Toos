# Directory Buster

![DirBuster Logo](images/dirbuster-logo.svg)
![Python](https://img.shields.io/badge/Python-3.7%2B-blue)

## Description

DirBuster is a Python-based directory busting tool that allows you to discover directories of a target website. You can enter either the IP address or the domain name of the website you want to scan. Directories will be scanned using a wordlist specified by you.

## Requirements

To run DirBuster, make sure you have the following dependencies installed:

- certifi==2022.12.7
- chardet==3.0.4
- idna==2.8
- requests==2.21.0
- urllib3==1.26.5

You can install these dependencies using `pip` with the following command:
```
pip install -r requirements.txt
```
## Usage
```
python dirbuster.py [-i] [-w]
```

### Arguments

- `--ip` or `-i`: Domain name or IP address of the target website.
- `--wordlist` or `-w`: Path to the wordlist file containing directories to be scanned.
- `--output` or `-o`: (Optional) Write open directories to a specified file.
- `-h` or `--help`: (Optional) Show the help message and usage instructions.

## How to Use

1. Open a terminal or command prompt.
2. Navigate to the directory containing `dirbuster.py`.
3. Run the tool with the desired options. For example:

```
python dirbuster.py --ip example.com --wordlist wordlist.txt
```

Replace `example.com` with the target domain or IP address, and `wordlist.txt` with the path to your wordlist file.

## Disclaimer

This tool is meant to be used for legitimate security purposes only. Unauthorized scanning of websites without proper authorization is illegal. Users are solely responsible for any actions performed using this tool. The developer is not responsible for any misuse or damage caused by this program.

**Use it responsibly and with permission!**

## Credits

DirBuster was created by Killer Machine and is available under the MIT license. For more information, please visit the [Red-team-tools/dirbuster](https://github.com/killer-machine-007/Red-Team-Toos/tree/main/dirbuster).

