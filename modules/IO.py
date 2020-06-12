#!/usr/bin/python3
try:
    from colorama import *
except:
    import os

    os.system("pip3 install colorama")
    from colorama import *

import urllib.parse as ul
import threading
import datetime

init(convert=True)


class IO:
    class _IO:
        def __init__(self):
            self.sem = threading.Semaphore()
            self.logFile = None

        def setLogFile(self, logfile):
            self.logFile = logfile

        def log(self, msg):
            if not self.logFile:
                return False
            dh = datetime.datetime.now()
            line = f"[{dh}] {msg}\n"
            with open(self.logFile, "a"):
                f.write(line)
            return True

        def print_success(self, msg):
            self.sem.acquire()
            print(f"{Style.BRIGHT}{Fore.GREEN}[*] {Style.NORMAL}{msg}{Fore.RESET}\n")
            self.sem.release()

        def print_error(self, msg):
            self.sem.acquire()
            print(f"{Style.BRIGHT}{Fore.RED}[!] {Style.NORMAL}{msg}{Fore.RESET}\n")
            self.sem.release()

        def print_warning(self, msg):
            self.sem.acquire()
            print(f"{Style.BRIGHT}{Fore.YELLOW}[#] {Style.NORMAL}{msg}{Fore.RESET}\n")
            self.sem.release()

        def print_info(self, msg):
            self.sem.acquire()
            print(f"{Style.BRIGHT}[#] {Style.NORMAL}{msg}\n")
            self.sem.release()

        def print_debug(self,msg):
            self.sem.acquire()
            print(f"{Style.BRIGHT}{Fore.YELLOW}[DEBUG] {msg}{Style.NORMAL}{Fore.RESET}")
            self.sem.release()

        def print(self, msg):
            self.sem.acquire()
            print(msg)
            self.sem.release()

        def urlencode(self, data):
            return ul.quote(data)

    instance = None

    def __init__(self):
        if not IO.instance:
            IO.instance = IO._IO()

    def __getattr__(self, name):
        return getattr(self.instance, name)


if __name__ == "__main__":
    IO().print_success("hi")
