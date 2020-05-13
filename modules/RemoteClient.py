#!/usr/bin/python3

import random,IO
import threading

class RemoteClient(threading.Thread):
    def __init__(self, sock, addr):
        threading.Thread(self)
        self.bufsize = 4096
        self.sock = sock
        self.addr = addr
        rand=random.randint(10000000,99999999)
        random.seed(rand)
        self.id = f"{self.addr}.{rand}"

    def id(self):
        return self.id

    def run(self):
        print("to inherit") 

    def stop(self):
        self.sock.close()


