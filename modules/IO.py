#!/usr/bin/python3

from colorama import *

def print_success(msg):
    print(f"{Style.BRIGHT}{Fore.GREEN}[*] {Style.NORMAL}{msg}{Fore.RESET}\n")

def print_error(msg):
    print(f"{Style.BRIGHT}{Fore.RED}[!] {Style.NORMAL}{msg}{Fore.RESET}\n")

def print_warning(msg):
    print(f"{Style.BRIGHT}{Fore.YELLOW}[#] {Style.NORMAL}{msg}{Fore.RESET}\n")

def print_info(msg):
    print(f"{Style.BRIGHT}[#] {Style.NORMAL}{msg}\n")
