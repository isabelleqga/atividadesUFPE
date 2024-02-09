from socket import socket, AF_INET, SOCK_DGRAM



mClientSocketUDP = socket(AF_INET,SOCK_DGRAM)
host = "127.0.0.1"
porta = 11810
mClientSocketUDP.connect((host,porta))
print("Conexão realizado com sucesso!")

contmensagens = 3
while True:
    if contmensagens > 0:
        print(f"{contmensagens} mensagens ainda devem ser enviadas...")
    contmensagens -= 1
    msg = input(">>")
    mClientSocketUDP.send(msg.encode())

    msg, servidor = mClientSocketUDP.recvfrom(2048)
    print(msg.decode())


