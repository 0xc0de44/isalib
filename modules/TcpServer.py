#!/usr/bin/python3

import socket
import IO
from NetHandler import NetHandler
import threading,hashlib

class TcpServer(NetHandler, threading.Thread):
    def __init__(self):
        NetHandler.__init__(self)
        threading.Thread(self)
        self.clients={}
    
    def init(self, ip="0.0.0.0", port=1337):
        NetHandler.init(self, ip, port)
    def run(self):
        self.start()

    def start(self):
        if self.state != "INIT":
            IO.print_error("TcpServer : trying to start a server listening without initialization")
            return False
        if self.state == "START":
            IO.print_warning("TcpServer : already started, skipping")
            return True

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            self.sock.bind(self.ip)
        except:
            IO.print_error(f"Couldn't bind to {self.ip[0]}:{self.ip[1]}")
            return False
        self.sock.listen(16)
        self.state = "START"

        while self.state == "START":
            clientsock, address = self.sock.accept()
            cli=TcpRemoteClient(clientsock, address)
            if not self.registerClient(cli.id(), cli):
                clientsock.close()
                continue
            cli.start()

        return True

    def stop(self):
        if self.state != "START":
            return True 
        self.state="INIT"
        self.sock.close()
        for k in self.clients.keys():
            self.unregisterClient(k)
        return True

    def send(self, buf):
        if self.state != "START":
            return False
        if type(buf) is not bytes:
            buf=buf.encode('utf-8')
        return self.sock.send(buf)
    
    def recv(self):
        if self.state != "START":
            return False
        return self.sock.recv(self.bufsize)

    def registerClient(self, clientid, client):
        if type(clientid) is not string or type(client) is not TcpRemoteClient:
            IO.print_error("TcpServer trying to register client with wrong ID or instance type")
            return False
        if clientid in self.clients:
            IO.print_error("TcpServer trying to register client with an existing ID")
            return False
        self.clients[clientid] = client
        return True

    def unregisterClient(self, clientid):
        if type(clientid) is not string:
            IO.print_error("TcpServer trying to unregister client with wrong ID type")
            return False
        cli=self.clients.pop(clientid)
        cli.stop()
        cli.join()
        return True
