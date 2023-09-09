import socket

my_sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock2.connect(('data.pr4e.org', 80))
