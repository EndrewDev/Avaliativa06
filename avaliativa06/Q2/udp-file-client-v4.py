import socket

SERVER_ADDRESS = '127.0.0.1'
PORT = 31435

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = 'discussao.txt'
sock.sendto(filename.encode('utf-8'), (SERVER_ADDRESS, PORT))

fileSize, _ = sock.recvfrom(512)
fileSize = int(fileSize.decode('utf-8'))
receivedData = b''

while len(receivedData) < fileSize:
    fileData, _ = sock.recvfrom(4096)
    receivedData += fileData

with open(f"recebido_{filename}", 'wb') as fd:
    fd.write(receivedData)

print(f"Arquivo '{filename}' recebido com sucesso.")

# sock.close()