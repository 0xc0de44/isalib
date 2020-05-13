#!/usr/bin/python3

import IO

def test_TcpClient():
    import TcpClient
    cli=TcpClient.TcpClient()
    cli.init("51.15.174.68", 1337)
    cli.start()
    cli.send("hi there")
    msg=cli.recv()
    print(msg[0].decode('utf-8'))
    cli.stop()


if __name__ == "__main__":
    test_TcpClient()
