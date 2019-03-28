import socket


HOST = '127.0.0.1'
PORT = 8000
udp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = HOST, PORT
udp.connect(dest)

print('Cliente TCP - socket')
print()
msg = input('Insira a mensagem: ')
while msg != 'q':
    udp.sendto(msg.encode('utf-8'), dest)
    msg = input('Insira a mensagem: ')
udp.close()
