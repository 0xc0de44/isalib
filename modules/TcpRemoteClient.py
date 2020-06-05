#!/usr/bin/python3
from RemoteClient import RemoteClient
import IO


class TcpRemoteClient(RemoteClient):
    def __init__(self, sock, ip):
        RemoteClient.__init__(self, sock, ip)

    def run(self):
        while True:
            data = self.sock.recv(self.bufsize)
            self.processData(data)

    def stop(self):
        RemoteClient.stop()

    def processData(self, data):
        if type(data) is not str:
            data = data.decode('utf-8')
        print(f"[{self.ip}] > {data}\n")
        tosend = f"{data} acknowledged"
        print(f"[{self.ip}] < {tosend}")
        self.sock.send(tosend.encode('utf-8'))
