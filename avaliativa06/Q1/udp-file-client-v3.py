import socket

SERVER_ADDRESS = '127.0.0.1'
PORT = 31435

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.settimeout(5)

filename = 'discussao.txt'
sock.sendto(filename.encode('utf-8'), (SERVER_ADDRESS, PORT))

try:
    fileData, _ = sock.recvfrom(4096)
    if fileData:
        with open(f"recebido_{filename}", 'wb') as fd:
            fd.write(fileData)
        print(f"Arquivo '{filename}' recebido com sucesso.")
    else:
        print("Nenhum dado recebido.")
except socket.timeout:
    print("Tempo de espera esgotado. O servidor pode ter terminado de enviar os dados.")

sock.close()
