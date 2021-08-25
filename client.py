import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 1024

client.connect((socket.gethostname(), port))

message = 'Hello from client'

encodedMessage = message.encode('utf-8')

client.send(encodedMessage)

for i in range(10):
    ip = input()
    if ip == 'exit':
        break
    client.send(ip.encode('utf-8'))

client.close()
