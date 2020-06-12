#!/usr/bin/python3
from RemoteClient import RemoteClient
from IO import *


class TcpRemoteClient(RemoteClient):
    def __init__(self, sock, ip):
        RemoteClient.__init__(self, sock, ip)
        self.running = False

    def run(self):
        self.running = True
        IO().print_info(f"[{self.ip}] joined")
        while self.running:
            try:
                data = self.sock.recv(self.bufsize)
                IO().print_debug(f"Received : {data}")
            except:
                self.running = false
                continue
            self.processData(data)
        IO().print_info(f"[{self.ip}] left")

    def stop(self):
        self.running = False
        RemoteClient.stop()


    def processData(self, data):
        if type(data) is not str:
            data = data.decode('utf-8')
        IO().print_info(f"[{self.ip}] > {data}\n")
        tosend = f"{data} acknowledged"
        IO().print_info(f"[{self.ip}] < {tosend}")
        self.sock.send(tosend.encode('utf-8'))
