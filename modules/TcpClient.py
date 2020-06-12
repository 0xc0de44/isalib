#!/usr/bin/python3

import socket
from IO import *
from NetHandler import NetHandler


class TcpClient(NetHandler):
    def __init__(self):
        NetHandler.__init__(self)

    def init(self, ip="127.0.0.1", port=1337):
        NetHandler.init(self, ip, port)

    def start(self):
        if self.state != "INIT":
            IO().print_error("TcpClient : trying to start a connection without initialization")
            return False
        if self.state == "START":
            IO().print_warning("TcpClient : already started, skipping")
            return True

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((self.ip, self.port))
        except:
            IO().print_error(f"Couldn't connect to {self.ip}:{self.port} ")
            return False

        self.state = "START"
        return True

    def stop(self):
        if self.state != "START":
            return True
        self.sock.close()
        self.state = "INIT"
        return True

    def send(self, buf):
        if self.state != "START":
            return False
        if type(buf) is not bytes:
            buf = buf.encode('utf-8')
        return self.sock.send(buf)

    def recv(self):
        if self.state != "START":
            return False
        return self.sock.recv(self.bufsize)


if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 1337
    cli = TcpClient()
    cli.init(ip, port)
    if not cli.start():
        IO().print_error("Cannot start Tcp Client")
        quit()
    cli.send("test")
    resp = cli.recv().decode("utf-8")
    print("Received " + resp)
    cli.stop()
