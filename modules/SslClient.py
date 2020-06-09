#!/usr/bin/python3

import socket
from IO import *
from NetHandler import NetHandler
from TcpClient import TcpClient
import ssl


class SslClient(TcpClient):
    def __init__(self):
        TcpClient.__init__(self)
        self.ssock = None
        self.context = ssl.create_default_context()

    def start(self):
        if self.state != "INIT":
            IO().print_error("SslClient : trying to start a connection without initialization")
            return False
        if self.state == "START":
            IO().print_warning("SslClient : already started, skipping")
            return True

        self.sock = socket.create_connection((self.ip,self.port))
        self.ssock = self.context.wrap_socket(self.sock, server_side=False, server_hostname=self.ip)
        IO().print_info(self.ssock.version())
        try:
            self.ssock.connect((self.ip, self.port))
        except:
            IO().print_error(f"Couldn't connect to {self.ip}:{self.port} ")
            return False

        self.state = "START"
        return True

    def stop(self):
        if self.state != "START":
            return True
        self.ssock.close()
        self.sock.close()
        self.state = "INIT"
        return True

    def send(self, buf):
        if self.state != "START":
            return False
        if type(buf) is not bytes:
            buf = buf.encode('utf-8')
        IO().print_debug(f"Sending : {buf}")
        return self.ssock.send(buf)

    def recv(self):
        if self.state != "START":
            return False
        return self.ssock.recv(self.bufsize)


if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 443
    cli = SslClient()
    cli.init(ip, port)
    if not cli.start():
        IO().print_error("Cannot start Ssl Client")
        quit()
    cli.send("test")
    resp = cli.recv().decode("utf-8")
    print("Received " + resp)
    cli.stop()
