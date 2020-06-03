#!/usr/bin/python3

import requests
import IO
from NetHandler import NetHandler

class HttpsClient(NetHandler):
    def __init__(self):
        NetHandler.__init__(self)

    def init(self, ip="https://www.google.com/", port="")
        NetHandler.init(self, ip, port)

    def start(self):
        if self.state != "INIT":
            IO.print_error("HttpsClient : trying to start a connection without initialization")
            return False
        if self.state == "START":
            IO.print_warning("HttpsClient: already started, skipping")
            return True

        self.state = "START"
        return True

    def stop(self):
        if self.state != "START":
            return True
        self.state = "INIT"
        return True

    def send(self, data):
        if salf.state != "START":
            IO.print_error("HttpsClient : cannot send data, use start() before")
            return False
        if type(data) is not bytes:
            data=data.encode("utf-8")
        data=base64.b64encode(data)
        postdata={"data" : f"{data}" }
        r = requests.post(self.ip, postdata)

        if r.status_code != 200:
            return False
        return True

    def recv(self):
        if self.state != "START":
            return False
        r=requests.get(ip)
        if r.status_code != 200:
            return False
        return r.text
