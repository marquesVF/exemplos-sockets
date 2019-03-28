import socket


HOST = '127.0.0.1'
PORT = 5000
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = HOST, PORT

print('Cliente UDP - socket')
print()
msg = input('Insira a mensagem: ')
while msg != 'q':
    udp.sendto(msg.encode('utf-8'), dest)
    msg = input('Insira a mensagem: ')
udp.close()
