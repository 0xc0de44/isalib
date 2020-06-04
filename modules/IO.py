#!/usr/bin/python3
try:
    from colorama import *
except:
    import os
    os.system("pip3 install colorama")
    from colorama import *

import urllib.parse as ul

init(convert=True)

def print_success(msg):
    print(f"{Style.BRIGHT}{Fore.GREEN}[*] {Style.NORMAL}{msg}{Fore.RESET}\n")

def print_error(msg):
    print(f"{Style.BRIGHT}{Fore.RED}[!] {Style.NORMAL}{msg}{Fore.RESET}\n")

def print_warning(msg):
    print(f"{Style.BRIGHT}{Fore.YELLOW}[#] {Style.NORMAL}{msg}{Fore.RESET}\n")

def print_info(msg):
    print(f"{Style.BRIGHT}[#] {Style.NORMAL}{msg}\n")

def urlencode(data):
    return ul.quote(data)
