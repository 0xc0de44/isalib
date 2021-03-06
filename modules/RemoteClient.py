#!/usr/bin/python3

import random
from IO import *
import threading

class RemoteClient(threading.Thread):
    def __init__(self, sock, ip):
        threading.Thread.__init__(self)
        self.bufsize = 4096
        self.sock = sock
        self.ip = ip
        rand=random.randint(10000000,99999999)
        random.seed(rand)
        self.id = f"{self.ip}.{rand}"

    def id(self):
        return self.id

    def run(self):
        print("to inherit") 

    def stop(self):
        self.sock.close()


