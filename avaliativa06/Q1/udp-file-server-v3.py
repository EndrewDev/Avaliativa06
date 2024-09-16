import socket

INTERFACE = '127.0.0.1'
PORT = 31435

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((INTERFACE, PORT))

print('Escutando em ...', (INTERFACE, PORT))

while True:
    data, source = sock.recvfrom(512)
    strFileName = data.decode('utf-8')
    print('Recebi pedido para o arquivo ', strFileName)
    fd = open(strFileName, 'rb')

    print('Enviando arquivo ...', strFileName)
    fileData = fd.read(4096)
    sock.sendto(fileData, source)

    fd.close()

sock.close()
