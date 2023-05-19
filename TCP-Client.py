import socket

host_alvo = "businesscorp.com.br" #EXEMPLO
porta_alvo = 3333                 #EXEMPLO

#Cria um objeto de ataque
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conexão do cliente
cliente.connect((host_alvo, porta_alvo))

#Envio de dados
cliente.send(b'GET / HTTP/1.1\r\nHost: businesscorp.com.br\r\n\r\n')

#Recebimento de dados
resposta = cliente.recv(4096)

print(resposta.decode())
cliente.close()