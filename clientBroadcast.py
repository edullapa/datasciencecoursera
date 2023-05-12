import socket
import sys

#endereço para o qual os dados vão ser enviados
host = '192.168.100.255'

#número da porta que o servidor que vai receber os dados está escutando
port = 1234

#cria um UDP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#envio para varios
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

print('Para sair use CTRL+X e pressione enter\n')
msg = input()

while msg != '\x18':
	#envia os dados
	s.sendto(msg.encode(),(host, port))
	msg = input()
	
print('closing socket')
s.close()