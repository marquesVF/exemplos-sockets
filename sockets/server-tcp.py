import socket

HOST = '127.0.0.1'
PORT = 8000
MAX_BUFFER_SIZE = 4096

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = HOST, PORT
tcp.bind(orig)
tcp.listen(1024)

print('Servidor TCP - socket')
print()
while True:
    conn, addr = tcp.accept()
    ip, port = str(addr[0]), str(addr[1])
    print('Aceitando conexões de ' + ip + ':' + port)

    input_from_client_bytes = conn.recv(MAX_BUFFER_SIZE)
    msg = input_from_client_bytes.decode("utf8")

    print('Mensagem -> `{}`'.format(msg))

    if not msg:
        conn.close()
        break
