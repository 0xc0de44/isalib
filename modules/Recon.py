#!/usr/bin/python3

import platform
from IO import *

class Recon:
    def __init__(self):
        self.os_name = platform.system()
        self.os_release = platform.release()

        
if __name__ == "__main__":
    r=Recon()
