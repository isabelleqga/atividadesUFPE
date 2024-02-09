from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread

def HandleRequest():
    while True:
        msg, cliente = mServerSocketUDP.recvfrom(2048)
        print(f'Requisição {msg.decode()} recebida de {cliente}')
        resposta = 'Mensagem recebida com sucesso!'
        mServerSocketUDP.sendto(resposta.encode(), cliente)
        print('Esperando o próximo pacote ...')

mServerSocketUDP = socket(AF_INET, SOCK_DGRAM)
print("Socket UDP criado.")
print("Aguardando conexão de um cliente...")
host = '127.0.0.1'
porta = 11810
origem = (host, porta)
mServerSocketUDP.bind(origem)

while True:
    Thread(target=HandleRequest).start()
