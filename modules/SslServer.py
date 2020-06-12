#!/usr/bin/python3

import socket
from IO import *
from NetHandler import NetHandler
from TcpRemoteClient import TcpRemoteClient
from TcpServer import TcpServer
from NetHandler import NetHandler
import ssl

import threading, hashlib


class SslServer(TcpServer):
    def __init__(self):
        TcpServer.__init__(self)
        self.ssock = None
        self.context = ssl.create_default_context()
        self.context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        self.context.load_cert_chain('certs/cert.pem', 'certs/privkey.pem')

    def init(self, ip="0.0.0.0", port=1337):
        TcpServer.init(self, ip, port)

    def run(self):
        if self.state != "INIT":
            IO().print_error("SslServer : trying to start a server listening without initialization")
            return False
        if self.state == "START":
            IO().print_warning("SslServer : already started, skipping")
            return True

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            self.sock.bind((self.ip, self.port))
        except:
            IO().print_error(f"Couldn't bind to {self.ip}:{self.port}")
            return False
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.listen(16)
        self.state = "START"

        self.ssock = self.context.wrap_socket(self.sock, server_side=True)
        while self.state == "START":
            clientsock, address = self.ssock.accept()
            cli = TcpRemoteClient(clientsock, address)
            if not self.registerClient(cli.id, cli):
                clientsock.close()
                continue
            cli.start()

        return True

    def stop(self):
        if self.state != "START":
            return True
        self.state = "INIT"
        self.ssock.close()
        self.sock.close()
        for k in self.clients.keys():
            self.unregisterClient(k)
        return True

    def send(self, buf):
        if self.state != "START":
            return False
        if type(buf) is not bytes:
            buf = buf.encode('utf-8')
        return self.ssock.send(buf)

    def recv(self):
        if self.state != "START":
            return False
        return self.ssock.recv(self.bufsize)


if __name__ == "__main__":
    port = 443

    srv = TcpServer()
    srv.init("0.0.0.0", port)
    srv.start()
