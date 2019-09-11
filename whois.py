#!/usr/bin/python

import socket
import sys

if len(sys.argv) < 2:
    print('python3 whois.py 127.0.0.1 or google.com')
    sys.exit(0)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('200.160.2.3',43))
s.send(sys.argv[1]+'\r\n')
resp = s.recv(1024)
print(resp)