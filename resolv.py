#!/usr/bin/python

import socket
import sys

if len(sys.argv) < 2:
    print('use python3 resolv.py dominio')
    print('ex: python3 resolv.py google.com')
    sys.exit(0)
print(sys.argv[1],'=====>',socket.gethostbyname(sys.argv[1]))