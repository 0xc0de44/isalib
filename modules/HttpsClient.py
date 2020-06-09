#!/usr/bin/python3

import os
import base64
from IO import *

try:
    import requests
except:
    os.system("pip3 install requests")
    import requests

from NetHandler import NetHandler

class HttpsClient(NetHandler):
    def __init__(self):
        NetHandler.__init__(self)

    def init(self, ip="https://www.google.com/"):
        self.ip=ip
        self.state="INIT"

    def start(self):
        if self.state != "INIT":
            IO().print_error("HttpsClient : trying to start a connection without initialization")
            return False
        if self.state == "START":
            IO().print_warning("HttpsClient: already started, skipping")
            return True

        self.state = "START"
        return True

    def stop(self):
        if self.state != "START":
            return True
        self.state = "INIT"
        return True

    def send(self, data):
        if self.state != "START":
            IO().print_error("HttpsClient : cannot send data, use start() before")
            return False
        if type(data) is not bytes:
            data=data.encode("utf-8")
        data=IO().urlencode(base64.b64encode(data))
        IO().print_info(f"url is : {self.ip}?data={data}")
        r = requests.get(f"{self.ip}?data={data}")

        if r.status_code != 200:
            return False
        return r.text

    def recv(self):
        if self.state != "START":
            return False
        r=requests.get(self.ip)
        if r.status_code != 200:
            return False
        return r.text

if __name__ == "__main__":
    url="http://localhost/test"
    cli=HttpsClient()
    cli.init(url)
    cli.start()
    print(cli.recv())
    print(cli.send("some data to send"))

