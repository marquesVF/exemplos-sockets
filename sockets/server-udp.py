import socket

HOST = '127.0.0.1'
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = HOST, PORT
udp.bind(orig)

print('Servidor UDP - socket')
print()
while True:
    msg, client = udp.recvfrom(1024)
    c_addr, c_port = client
    print('Message from {} port {} -> `{}`'.format(c_addr, c_port,
                                                   msg.decode('utf-8')))
