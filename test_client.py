import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.connect(server_address)

try:
    data = sock.recv(16)
    print >>sys.stderr, 'received "%s"' % data

finally:
    sock.close()