#!/usr/bin/python3

import os, sys
from IO import *

class NetHandler:
    def __init__(self):
        self.sock = None
        self.ip = None
        self.port = None
        self.state = "NEW"
        self.bufsize = 4096

    def init(self, ip="127.0.0.1", port=1337):
        self.ip = ip
        self.port = port
        self.state = "INIT"

    def start(self):
        print("to inherit")

    def stop(self):
        print("to inherit")

    def send(self, data):
        print("to inherit")

    def recv(self):
        print("to inherit")
